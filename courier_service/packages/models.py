from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Package(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_packages')
    tracking_number = models.CharField(max_length=36, unique=True)  
    recipient_name = models.CharField(max_length=255)
    recipient_address = models.TextField()
    weight = models.FloatField()
    description = models.TextField(default='No Description')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 

    def soft_delete(self):
        self.deleted_at = now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def is_deleted(self):
        return self.deleted_at is not None

    def __str__(self):
        return f'Tracking {self.tracking_number} - {self.status}'
