from django.db import models
from cms.models import CMSPlugin


class CustomerPluginModel(CMSPlugin):
    title = models.CharField(max_length=50)
    is_display = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class CustomerMaster(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name