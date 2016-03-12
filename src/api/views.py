from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib
import sys
from django.http.response import HttpResponse
from api.models import reportData

# Create your views here.
#send post request to build jenkins


#receive data from jenkins
@csrf_exempt
def dataTrip(request):
    try:
        print('wee')
        buildNo=str(request.POST.get('BuildNo'))
        productLine=str(request.POST.get('ProductLine'))
        totalCases=str(request.POST.get('Total'))
        failureCases=str(request.POST.get('Failures'))
        successRate=str(request.POST.get('SuccessRate'))
        averageTime=str(request.POST.get('AverageTime'))
        minTime=str(request.POST.get('MinTime'))
        maxTime=str(request.POST.get('MaxTime'))
        averageLatency=str(request.POST.get('AverageLatency'))
        minLatency=str(request.POST.get('MinLatency'))
        maxLatency=str(request.POST.get('MaxLatency'))
        print(averageTime)
        print(successRate)
        print(minTime)
        print(maxTime)
        reportData.objects.create(BuildNo=buildNo,ProductLine=productLine,TotalCases=totalCases,FailureCases=failureCases,SuccessRate=successRate,AverageTime=averageTime,MinTime=minTime,MaxTime=maxTime,AverageLatency=averageLatency,MinLatency=minLatency,MaxLatency=maxLatency)
    except:
        print(sys.exc_info())
    return HttpResponse(status=200)