from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
import logging

logger = logging.getLogger(__name__)

class Cake(models.Model):
    OCCASION_CHOICES = [
        ("wedding", "Wedding"),
        ("birthday", "Birthday"),
        ("anniversary", "Anniversary"),
        ("baby_shower", "Baby Shower"),
        ("gender_reveal", "Gender Reveal"),
        ("Communion", "Communion"),
        ("Confirmation", "Confirmation"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=OCCASION_CHOICES, default="other")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # Ensure the slug is unique
            while Cake.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{Cake.objects.filter(name=self.name).count()}"
        
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error while saving Cake: {e}")
            raise e
