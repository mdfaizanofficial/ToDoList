from django.db import models

# Create your models here.

class ToDo(models.Model):
    Id = models.IntegerField(auto_created=True)
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Complete = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
