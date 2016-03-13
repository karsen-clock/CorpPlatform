
#coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render,RequestContext
from django.http import JsonResponse
from django.utils import timezone
import json,time,sys,os,random,subprocess,re,datetime
# from django.http import HttpResponse
# from .form import GetInterfaceList
from mock.models import interface
from api.models import reportData
from time import ctime
import urllib
import urllib.parse
import urllib.request


# Create your views here.
BASE_DIR = os.path.dirname(__file__)

def configPage(request):
    navActiveStatusDic={'home':'','mock':'','more':'','help':'','links':'','dataCount':''}
    submitMessage=''
    display='alert alert-success hidden'
#     print (timezone.now())
#     print (datetime.datetime.strptime(datetime.timezone(),'YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]')) 
    if request.method=='POST' and 'uploadResponseFile' in request.get_full_path():
        file_Obj=request.FILES.get('uploadResponseFile',None)
        submitMessage=handle_uploaded_file(file_Obj)
        display='alert alert-warning show'
        navActiveStatusDic['mock'] ='active'          
        return render(request,'index.html',{'submitMessageDic':submitMessage,'display':display,'navActiveStatusDic':navActiveStatusDic},context_instance=RequestContext(request))
    elif request.method == 'POST':
            protocol=request.POST.get('Protocol')
            interfaceName=str(request.POST.get('InterfaceName')).strip()
            businessName=str(request.POST.get('BusinessName')).strip()
            mockConfig=request.POST.get('ConfigParameter')
            try:
                result=interface.objects.get_or_create(protocol=protocol,interfaceName=interfaceName,businessName=businessName,mockConfig=mockConfig,operator='sysem',isvalid=True)
                if result[1] == False:
                    submitMessage=' record has already exist '
                    display='alert alert-info show'
                else:
                    saveResponseFile(interfaceName,mockConfig)
                    WriteAPIJson(interfaceName)
                    submitMessage=' add successfully,please remeber to upload your response data file '
                    display='alert alert-success show'

            except:
                submitMessage='interface '+interfaceName+' has already exist1'
                display='alert alert-warning show'
            navActiveStatusDic['mock'] ='active'          
            return render(request,'index.html',{'submitMessageDic':submitMessage,'display':display,'navActiveStatusDic':navActiveStatusDic},context_instance=RequestContext(request))
    else:
            navActiveStatusDic['mock'] ='active' 
            return render(request,'index.html',{'submitMessageDic':submitMessage,'display':display,'navActiveStatusDic':navActiveStatusDic},context_instance=RequestContext(request))


def getInterfaceList(request):
    navActiveStatusDic={'home':'','mock':'','more':'','help':'','links':'','dataCount':''}
    if 'home' in request.get_full_path():
        navActiveStatusDic['home'] ='active'
        navActiveStatusDic['mock'] =''  
    else:
        navActiveStatusDic['mock'] ='active'
        navActiveStatusDic['home'] =''  
        
    if 'Protocol' in request.get_full_path() :
            protocolGet=request.GET['Protocol']
            interfaceNameGet=request.GET['InterfaceName']
            interfaceListResult=interface.objects.filter(protocol=protocolGet).filter(interfaceName__icontains=interfaceNameGet)
            return render(request,'getInterfaceList.html',{'interfaceListResult':interfaceListResult,'navActiveStatusDic':navActiveStatusDic})

    else:
        return render(request,'getInterfaceList.html',{'navActiveStatusDic':navActiveStatusDic})   


def helpPage(request):
    navActiveStatusDic={'home':'','mock':'','more':'','help':'','links':'','dataCount':''}
    navActiveStatusDic['help'] ='active' 
    return render(request,'helpPage.html',{'navActiveStatusDic':navActiveStatusDic})

def links(request):
    navActiveStatusDic={'home':'','mock':'','more':'','help':'','links':'','dataCount':''}
    navActiveStatusDic['links'] ='active' 
    return render(request,'links.html',{'navActiveStatusDic':navActiveStatusDic})

def dataCount(request):
    navActiveStatusDic={'home':'','mock':'','more':'','help':'','links':'','dataCount':''}
    navActiveStatusDic['dataCount'] ='active' 
    return render(request,'automationTrend.html',{'navActiveStatusDic':navActiveStatusDic})

def getDataCount(request):
    startDate=request.POST.get('StartDate')
    endDate=request.POST.get('EndDate')
    print(request.POST.get('StartDate'))
    print(request.POST.get('EndDate'))
    #filter(CreateTime__lte=endDate)
    queryData=reportData.objects.filter(CreateTime__gte=startDate).filter(CreateTime__lte=endDate).values('BuildNo','TotalCases','FailureCases','SuccessRate','AverageTime','MinTime','MaxTime','AverageLatency','MinLatency','MaxLatency')
    print(queryData)
    categoriesRoot={}
    categoriesList=[]
    totalCasesDic={}
    totalCasesList=[]
    failureCasesDic={}
    failureCasesList=[]
    successRateDic={}
    successRateList=[]
    successRateBuildNoList=[]
    subSuccessRateBuildNoList=[]
    averageTimeDic={}
    averageTimeList=[]
    minTimeDic={}
    minTimeList=[]
    maxTimeDic={}
    maxTimeList=[]
    averageLatencyDic={}
    averageLatencyList=[]
    minLatencyDic={}
    minLatencyList=[]
    maxLatencyDic={}
    maxLatencyList=[]
    casesList=[]
    rateList=[]
    timeList=[]
    
    for buildQuery in queryData:
        print(buildQuery)
        subSuccessRateBuildNoList=[]
        categoriesList.append(str(buildQuery['BuildNo']))
        totalCasesList.append(int(buildQuery['TotalCases']))
        
        failureCasesList.append(int(buildQuery['FailureCases']))
        
        successRateList.append(float(buildQuery['SuccessRate']))   
        subSuccessRateBuildNoList.append(str(buildQuery['BuildNo']))
        subSuccessRateBuildNoList.append(float(buildQuery['SuccessRate']))
        successRateBuildNoList.append(subSuccessRateBuildNoList)
        
                
        averageTimeList.append(int(buildQuery['AverageTime']))
        
        minTimeList.append(int(buildQuery['MinTime']))
        
        maxTimeList.append(int(buildQuery['MaxTime']))

        averageLatencyList.append(int(buildQuery['AverageLatency']))
        
        minLatencyList.append(int(buildQuery['MinLatency']))
        
        maxLatencyList.append(int(buildQuery['MaxLatency']))
                          
    totalCasesDic['name']='TotalTestCases'
    totalCasesDic['data']=totalCasesList
    
    failureCasesDic['name']='FailureTestCaes'
    failureCasesDic['data']=failureCasesList
    
    successRateDic['name']='SuccessRate'
    successRateDic['data']=successRateList
           
    averageTimeDic['name']='AverageTime'
    averageTimeDic['data']=averageTimeList
    
    minTimeDic['name']='MinTime'
    minTimeDic['data']=minTimeList
 
    maxTimeDic['name']='MaxTime'
    maxTimeDic['data']=maxTimeList

    averageLatencyDic['name']='AverageLatency'
    averageLatencyDic['data']=averageLatencyList
    
    minLatencyDic['name']='MinLatency'
    minLatencyDic['data']=minLatencyList
 
    maxLatencyDic['name']='MaxLatency'
    maxLatencyDic['data']=maxLatencyList
        
    casesList.append(totalCasesDic)
    casesList.append(failureCasesDic)

    rateList.append(successRateDic)
   
    timeList.append(averageTimeDic)
    timeList.append(minTimeDic)
    timeList.append(maxTimeDic)    
    timeList.append(averageLatencyDic)
    timeList.append(minLatencyDic) 
    timeList.append(maxLatencyDic) 
            
    categoriesRoot['categories']=categoriesList
    categoriesRoot['casesCount']=casesList
    categoriesRoot['rate']=rateList
    categoriesRoot['time']=timeList    
    categoriesRoot['successRateBuildNo']=successRateBuildNoList
#     print(categoriesRoot)           
#     categories={'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],'series':[{
#     'name': 'Tokyo',
#       'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
#     }, {
#       'name': 'New York',
#       'data': [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
#     }, {
#      'name': 'Berlin',
#       'data': [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
#     }, {
#       'name': 'London',
#       'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
#     }]}
    print(categoriesRoot)
    return JsonResponse(categoriesRoot)


def deleteInterfaceConfig(request):
    deleteDic={}
    info='Delete record successfully'
    try:
        if request.is_ajax() and request.method == 'POST':
            protocolGet=request.POST.get('protocol').strip()
            interfaceNameGet=str(request.POST.get('interfaceName')).strip()
            message=DeleteAPIJson(interfaceNameGet)
            interface.objects.filter(interfaceName=interfaceNameGet).filter(protocol=protocolGet).delete()
    except: 
        info = '%s || %s' % (sys.exc_info()[0], sys.exc_info()[1])
    deleteDic['message']=info
    deleteDic['time']=str(ctime())
    return JsonResponse(deleteDic)


def editInterfaceConfig(request):
    editDic={}
    info='Delete record successfully'
    try:
        if request.is_ajax() and request.method == 'POST':
            protocolGet=request.POST.get('protocol').strip()
            interfaceNameGet=str(request.POST.get('interfaceName')).strip()
            businessNameGet=str(request.POST.get('businessName')).strip()
            parameterConfigGet=str(request.POST.get('configParameter')).strip()
            saveResponseFile(interfaceNameGet,parameterConfigGet)
            interface.objects.filter(interfaceName=interfaceNameGet).filter(protocol=protocolGet).update(businessName=businessNameGet,mockConfig=parameterConfigGet,updatetime=timezone.now())
    except: 
        info = '%s || %s' % (sys.exc_info()[0], sys.exc_info()[1])
    editDic['message']=info
    editDic['time']=str(ctime())
    print (editDic)
    return JsonResponse(editDic)
#runservice page
def runService(request):
    returnMessage=''
    navActiveStatusDic={'home':'','mock':'active','more':'','help':''}        
    if 'runServices' in request.get_full_path():
        protocolGet=request.GET['runProtocol']
        mode=request.GET['Mode']
        returnMessage=RunCMD(protocolGet,mode)
        return render(request,'runservice.html',{'returnMessage':returnMessage,'navActiveStatusDic':navActiveStatusDic})
    else:
        return render(request,'runservice.html',{'returnMessage':returnMessage,'navActiveStatusDic':navActiveStatusDic})
    
    
#以下内容均为被调用方法，导航相关请写在上面
def saveResponseFile(fileName,fileContent):
    try:
        filePath=os.path.join(BASE_DIR,'static/responseconfig/'+fileName+'.json').replace('\\','/')
        fileObject=open(filePath,'w')
        fileObject.write(fileContent)
        fileObject.close()
    except IOError as err:  #使用as将异常对象，并将其赋值给一个标识符  
        print('File Error:'+str(err)) #‘+’用于字符串直接的连接

  
#保存上传的文件
def handle_uploaded_file(f):
    file_name = ""
    responseMessage="Save file successfully"
    try:
        if f.name.endswith('.response') and f.size < 1000:
            path = os.path.join(BASE_DIR,'static/responseconfig/').replace('\\','/')
            print (path)
            file_name = path + f.name
            print (file_name)
            destination = open(file_name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
                destination.close()
        else:
            responseMessage='invalid response data,file should be end with .response'    
    except IOError as err:
            print (err)
            responseMessage= "Save file failed,please try again"
    return responseMessage

#读取json文件
def WriteAPIJson(configFileName):
    if configFileName != '' :
            path = os.path.join(BASE_DIR,'static/globalconfig/api.json').replace('\\','/')
            responseDataPath=os.path.join(BASE_DIR,'static/responseconfig').replace('\\','/')  
            f=open(path,'r') 
            dic=json.load(f)   #读取
            f.close()
            for i in dic[:-1]: 
                print (i.get('include'))
            data={
                  "file_root":responseDataPath,
                  "include" : configFileName+'.json'
                  }
            dic.append(data)
            print (dic)
            f=open(path,'w') 
            json.dump(dic,f)  #将字符串qqq写入到f中 
            f.close()
            responseMessage='Save config file successfully'
    else:
        responseMessage='Interface name is none'
    return responseMessage



#删除记录的同时删除对应的LIST
def DeleteAPIJson(interfaceName):
    responseMessage=''
    try:
        path = os.path.join(BASE_DIR,'static/globalconfig/api.json').replace('\\','/')
        configFilePath=os.path.join(BASE_DIR,'static/responseconfig/'+interfaceName+'.json').replace('\\','/')
        f=open(path,'r') 
        dic=json.load(f)   #读取
        f.close()
        print ('before delete')
        for i in dic:
            print (str(i.get('include')) == interfaceName+'.json')
            if str(i.get('include')) == interfaceName+'.json':
                dic.remove(i)
                responseMessage='global config settings file update successfully'
        print ('after delete')
        print (dic)
        f=open(path,'w') 
        json.dump(dic,f)  #将字符串qqq写入到f中 
        f.close()
        if os.path.exists(configFilePath):
            os.remove(configFilePath)
            responseMessage=responseMessage+'config file delete successfully'
        responseMessage=responseMessage+'delete config file successfully'
    except IOError as e:
            responseMessage=responseMessage+str(e)
    return responseMessage

#run cmd
def RunCMD(protocol,mode):
    runCommanderDic = {'http':'moco-runner-0.10.2-standalone.jar http -p 12306 -g','https':'moco-runner-0.10.2-standalone.jar https -p 12307 ','socket':'moco-runner-0.10.2-standalone.jar socket -p 12308 '}
    stopCommanderDic= {'http':'moco-runner-0.10.2-standalone.jar shutdown -s 12306','https':'moco-runner-0.10.2-standalone.jar shutdown -s 12307','socket':'moco-runner-0.10.2-standalone.jar shutdown -s 12308'}
    portCommanderDic={'http':'12306','https':'12307','socket':'12308'}
    protocol=protocol.lower()
    cmd=''
    if mode.lower() =='run':
       cmd=str(runCommanderDic.get(protocol))
    else:
       cmd=str(stopCommanderDic.get(protocol))
       cmdFindProcess='netstat -ano|findstr '+'"'+str(portCommanderDic.get(protocol))+'"'
       cmdTaskKill='taskkill /f /pid '
    stringReturn='command line: '+cmd
    mocoPath = os.path.join(BASE_DIR,'static/globalconfig/').replace('\\','/')
    cmd='java -jar '+mocoPath+cmd+mocoPath+'api.json'  
    stringReturn=stringReturn+' command result: '+ExecuteCMD(cmd)+'\r\n'
    if mode.lower() =='stop':
        stringReturn=stringReturn+' \r\n  command line: '+cmdFindProcess
        getPortListening=ExecuteCMD(cmdFindProcess)
        stringReturn=stringReturn+' \r\n  command result: '+getPortListening
        getPortListening=getPortListening.replace(' ','')
        processID=re.findall(r'LISTENING(.*[0-9])',getPortListening)
        print (processID)
#         for pid in processID:
        if len(processID) > 0:
            stringReturn= stringReturn=stringReturn+' \r\n  command line: '+cmdTaskKill+str(processID[0]) 
            stringReturn=stringReturn=stringReturn+' \r\n  command result: '+ExecuteCMD(cmdTaskKill+str(processID[0]))
    return str(stringReturn)

#命令行执行方法
def ExecuteCMD(cmd):
    print (cmd)
    returnData=''
    p = subprocess.Popen('cmd /C '+cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readline()
    returnData=returnData+str(output.decode('GBK'))
    print (returnData)
    return returnData

def buildJenkins(request):
    test_data = {'token':'3d145266c0d3b8966eac4d5782d150a3','cause':'triggred by user from corp flight test platform'}
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    requrl = "http://ciapi.qa.nt.ctripcorp.com:8080/job/Corp-CtripAutomationJars/build?"
    try:
        req = urllib.request.Request(requrl,test_data_urlencode)
    except:
        print (sys.exc_info())
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
