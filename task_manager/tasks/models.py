from django.db import models
from django.conf import settings
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField()
    tags = models.JSONField(default=list, blank=True)

    @property
    def is_overdue(self):
        return self.status != 'done' and self.due_date < date.today()
