from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Farmer(models.Model):
    # Personal Information
    name = models.CharField(max_length=200, verbose_name="Full Name")
    id_number = models.CharField(max_length=20, unique=True, verbose_name="ID Number")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    
    # Location Information
    county = models.CharField(max_length=100, verbose_name="County")
    sub_county = models.CharField(max_length=100, verbose_name="Sub-County")
    ward = models.CharField(max_length=100, verbose_name="Ward")
    
    # Farm Information
    farm_name = models.CharField(max_length=200, verbose_name="Farm Name")
    
    # Livestock Information
    GOAT = 'GOAT'
    SHEEP = 'SHEEP'
    ANIMAL_TYPES = [
        (GOAT, 'Goat'),
        (SHEEP, 'Sheep'),
    ]
    
    animal_type = models.CharField(
        max_length=5,
        choices=ANIMAL_TYPES,
        verbose_name="Type of Animal"
    )
    number_of_animals = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Number of Animals"
    )
    animal_age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        verbose_name="Age of Animals (months)"
    )
    
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-registration_date']
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"
    
    def __str__(self):
        return f"{self.name} - {self.farm_name}"
    
    def get_absolute_url(self):
        return reverse('farmer_detail', args=[str(self.id)])