# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse
import hashlib

def handleRequest(request):
    if request.method == 'GET':
           response = HttpResponse(checkSignature(request))
           return response

TOKEN = "Wenhan"
def checkSignature(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr", None)
 
    token = TOKEN
    tmpList = [token, timestamp, nonce]    
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
         return echoStr
    else:
        return 'wrong'    