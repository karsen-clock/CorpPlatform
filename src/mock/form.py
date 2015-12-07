#coding:utf-8
'''
Created on 2015年11月22日

@author: hasee
'''
from django import forms
from django.forms.widgets import Widget

# class SaveRequest(forms.Form):
#     protocol_choice=(
#     ('http',u'http'),
#     ('https',u'https'),
#     ('socket',u'socket'),
#     )
#     Protocol=forms.ChoiceField(label=(u'协议类型*'),required=True,choices=protocol_choice)    
#     InterfaceName=forms.CharField(label=(u'接口名称*'),required=True,max_length=100)
#     ResponseData=forms.CharField(widget=forms.Textarea,label=(u'响应内容*'),required=True,max_length=2000)
# class GetInterfaceList(forms.Form):
#     protocol_choice=(
#     ('http',u'http'),
#     ('https',u'https'),
#     ('socket',u'socket'),
#     )
#         
#     Protocol=forms.ChoiceField(label=(u'协议类型'),choices=protocol_choice)    
#     InterfaceName=forms.CharField(label=(u'接口名称'),required=True,max_length=100)

