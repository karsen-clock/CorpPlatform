from django.db import models
from django.utils.log import RequireDebugFalse
# Create your models here.

class interface(models.Model):
    protocol=models.CharField(max_length=50)
    interfaceName=models.CharField(primary_key=True,max_length=100)
    businessName=models.CharField(max_length=50)
    mockConfig=models.CharField(max_length=2000)
    operator=models.CharField(max_length=20)
    createtime=models.DateTimeField(auto_now_add = True)
    updatetime=models.DateTimeField(auto_now_add = True)
    isvalid=models.BooleanField()
    
    
    
    