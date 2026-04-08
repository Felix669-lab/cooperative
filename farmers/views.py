from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count
from .models import Farmer
from .forms import FarmerForm

def home(request):
    # Get statistics for the home page
    total_farmers = Farmer.objects.count()
    total_goats = Farmer.objects.filter(animal_type='GOAT').aggregate(total=Sum('number_of_animals'))['total'] or 0
    total_sheep = Farmer.objects.filter(animal_type='SHEEP').aggregate(total=Sum('number_of_animals'))['total'] or 0
    total_counties = Farmer.objects.values('county').distinct().count()
    recent_farmers = Farmer.objects.all().order_by('-registration_date')[:6]
    
    context = {
        'total_farmers': total_farmers,
        'total_goats': total_goats,
        'total_sheep': total_sheep,
        'total_animals': total_goats + total_sheep,
        'total_counties': total_counties,
        'recent_farmers': recent_farmers,
    }
    return render(request, 'farmers/home.html', context)

def dashboard(request):
    # Get data for dashboard charts
    total_farmers = Farmer.objects.count()
    total_goats = Farmer.objects.filter(animal_type='GOAT').aggregate(total=Sum('number_of_animals'))['total'] or 0
    total_sheep = Farmer.objects.filter(animal_type='SHEEP').aggregate(total=Sum('number_of_animals'))['total'] or 0
    recent_farmers = Farmer.objects.all().order_by('-registration_date')[:5]
    
    # County distribution for chart
    county_stats = Farmer.objects.values('county').annotate(count=Count('id'))
    county_labels = [item['county'] for item in county_stats]
    county_data = [item['count'] for item in county_stats]
    
    context = {
        'total_farmers': total_farmers,
        'total_goats': total_goats,
        'total_sheep': total_sheep,
        'total_animals': total_goats + total_sheep,
        'recent_farmers': recent_farmers,
        'county_labels': county_labels,
        'county_data': county_data,
    }
    return render(request, 'farmers/dashboard.html', context)

def farmer_list(request):
    farmers = Farmer.objects.all()
    search_query = request.GET.get('search', '')
    animal_filter = request.GET.get('animal_type', '')
    county_filter = request.GET.get('county', '')
    
    if search_query:
        farmers = farmers.filter(
            Q(name__icontains=search_query) |
            Q(farm_name__icontains=search_query) |
            Q(county__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )
    
    if animal_filter:
        farmers = farmers.filter(animal_type=animal_filter)
    
    if county_filter:
        farmers = farmers.filter(county=county_filter)
    
    # Pagination - 9 farmers per page
    paginator = Paginator(farmers, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique counties for filter dropdown
    counties = Farmer.objects.values_list('county', flat=True).distinct().order_by('county')
    
    context = {
        'farmers': page_obj,
        'search_query': search_query,
        'animal_filter': animal_filter,
        'county_filter': county_filter,
        'counties': counties,
    }
    return render(request, 'farmers/farmer_list.html', context)

def farmer_detail(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    return render(request, 'farmers/farmer_detail.html', {'farmer': farmer})

def register_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmer registered successfully!')
            return redirect('farmer_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerForm()
    
    return render(request, 'farmers/register_farmer.html', {'form': form})

def edit_farmer(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmer information updated successfully!')
            return redirect('farmer_detail', pk=farmer.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerForm(instance=farmer)
    
    return render(request, 'farmers/edit_farmer.html', {'form': form, 'farmer': farmer})

def delete_farmer(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        farmer.delete()
        messages.success(request, 'Farmer deleted successfully!')
        return redirect('farmer_list')
    return render(request, 'farmers/delete_farmer.html', {'farmer': farmer})

def about(request):
    return render(request, 'farmers/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can add email sending logic here
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'farmers/contact.html')