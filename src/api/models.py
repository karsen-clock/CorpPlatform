from django.db import models

# Create your models here.
class reportData(models.Model):
    BuildNo=models.IntegerField()
    ProductLine=models.CharField(max_length=50,blank=True)
    TotalCases=models.IntegerField()
    FailureCases=models.IntegerField()
    SuccessRate=models.FloatField()
    AverageTime=models.IntegerField()
    MinTime=models.IntegerField()
    MaxTime=models.IntegerField()
    AverageLatency=models.IntegerField(blank=True)
    MinLatency=models.IntegerField(blank=True)
    MaxLatency=models.IntegerField(blank=True)
    CreateTime=models.DateTimeField(auto_now_add = True)  
