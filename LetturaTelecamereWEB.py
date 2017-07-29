import urllib2, base64
import httplib
from datetime import *
import time
from PyGameModule import *


PathNow=""    



def SaveCAM(Wn):
    now=datetime.now()
    FileNow=str(now.year)+"{:0>2d}".format(now.month)+"{:0>2d}".format(now.day)+"-" + "{:0>2d}".format(now.hour)+"{:0>2d}".format(now.minute) +"{:0>2d}".format(now.second)
    PathNow=str(now.year)+ "\\" + "{:0>2d}".format(now.month)+ "\\" + "{:0>2d}".format(now.day)+ "\\" 

    Wn.showTextScreen ("Status:CAM G01         ",9,(50,255,50),LEFT)
    #---------------------------G01-----------------------------------
    try:
        NomeFile="G_"+FileNow+"_G01.jpg"
        username="admin"
        password="border"
        request = urllib2.Request("http://192.168.1.201:2001/jpg/image.jpg")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A= result.read()
        result.close

        #Posta sul web
        Wn.showTextScreen ("Status:CAM G01 WEB         ",9,(50,255,50),LEFT)
        headers = {"Content-type": "JPEG", "Accept": "text/plain", "CamName":"G01", "FileName": NomeFile, "IMAGEPATH": PathNow}
        conn=httplib.HTTPConnection("www.mdmecco.it",80, timeout=10)
        conn.request("POST", "/Ghelfa/SaveImage.php", A, headers)
        X=conn.getresponse()
        conn.close()

    except:
        A=""

    #---------------------------G02-----------------------------------
    Wn.showTextScreen ("Status:CAM G02         ",9,(50,255,50),LEFT)
    try:
        NomeFile="G_"+FileNow+"_G02.jpg"
        username="admin"
        password="border"
        request = urllib2.Request("http://192.168.1.202:2002/jpg/image.jpg")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A= result.read()
        result.close

        #Posta sul web
        Wn.showTextScreen ("Status:CAM G02 WEB         ",9,(50,255,50),LEFT)
        headers = {"Content-type": "JPEG", "Accept": "text/plain", "CamName":"G02", "FileName": NomeFile, "IMAGEPATH": PathNow}
        conn=httplib.HTTPConnection("www.mdmecco.it",80, timeout=10)
        conn.request("POST", "/Ghelfa/SaveImage.php", A, headers)
        X=conn.getresponse()
        conn.close()
    except:
        A=""

    #---------------------------G03-----------------------------------
    Wn.showTextScreen ("Status:CAM G03         ",9,(50,255,50),LEFT)
    try:
        NomeFile="G_"+FileNow+"_G03.jpg"
        username="admin"
        password="border"
        request = urllib2.Request("http://192.168.1.203:2003/jpg/image.jpg")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A=result.read()
        result.close

        #Posta sul web
        Wn.showTextScreen ("Status:CAM G03 WEB         ",9,(50,255,50),LEFT)
        headers = {"Content-type": "JPEG", "Accept": "text/plain", "CamName":"G03", "FileName": NomeFile, "IMAGEPATH": PathNow}
        conn=httplib.HTTPConnection("www.mdmecco.it",80, timeout=10)
        conn.request("POST", "/Ghelfa/SaveImage.php", A, headers)
        X=conn.getresponse()
        conn.close()
    except:
        A=""

    #---------------------------G04-----------------------------------
    Wn.showTextScreen ("Status:CAM G04         ",9,(50,255,50),LEFT)
    try:
        NomeFile="G_"+FileNow+"_G04.jpg"
        username="admin"
        password="border"
        request = urllib2.Request("http://192.168.1.204:2004/jpg/image.jpg")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A= result.read()
        result.close

        #Posta sul web
        Wn.showTextScreen ("Status:CAM G04 WEB         ",9,(50,255,50),LEFT)
        headers = {"Content-type": "JPEG", "Accept": "text/plain", "CamName":"G04", "FileName": NomeFile, "IMAGEPATH": PathNow}
        conn=httplib.HTTPConnection("www.mdmecco.it",80, timeout=10)
        conn.request("POST", "/Ghelfa/SaveImage.php", A, headers)
        X=conn.getresponse()
        conn.close()
    except:
        A=""

    #---------------------------G05-----------------------------------
    Wn.showTextScreen ("Status:CAM G05         ",9,(50,255,50),LEFT)
    try:
        NomeFile="G_"+FileNow+"_G05.jpg"
        username="admin"
        password="border"
        request = urllib2.Request("http://192.168.1.205:2005/snapshot.cgi")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A= result.read()
        result.close
        #Posta sul web
        Wn.showTextScreen ("Status:CAM G05 WEB         ",9,(50,255,50),LEFT)
        headers = {"Content-type": "JPEG", "Accept": "text/plain", "CamName":"G05", "FileName": NomeFile, "IMAGEPATH": PathNow}
        conn=httplib.HTTPConnection("www.mdmecco.it",80, timeout=10)
        conn.request("POST", "/Ghelfa/SaveImage.php", A, headers)
        X=conn.getresponse()
        conn.close()
    except:
        A="" 

