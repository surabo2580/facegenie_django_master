from django.db import models


# Create your models here.
class ServiceDetails(models.Model):
    service_Id = models.AutoField(primary_key=True)
    ai_model = models.CharField(max_length=200)
    issue_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100,default=None)

    #def __str__(self):
     #   return 'serviceDetails' + self.location

class TriggerApp(models.Model):
    Trigger_id = models.AutoField(primary_key=True)
    port = models.IntegerField(default=0)
    appname = models.CharField(max_length=200)
    path = models.FilePathField(path = None)
