
import urllib2, base64
import httplib
from datetime import *
import time


def ReadDenkovi():

    try:
        username="admin"
        password="admin"
        request = urllib2.Request("http://192.168.1.7:80/ioreg.js")
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        A= result.read()
        result.close

        B=A.split("(")
        A=B[1]
        D= A.split(")")
        A=D[0]
        InA=A.split(",")
        A=B[2]
        D=A.split(")")
        A=D[0]
        InB=A.split(",")

        A=B[3]
        D=A.split(")")
        A=D[0]
        D=A.split("\"")

        InC=D[1::2]


        InV=[]

        n='{:08b}'.format(int(InA[0],0))

        InV.append(int(n[7],0))
        InV.append(int(n[6],0))
        InV.append(int(n[5],0))
        InV.append(int(n[4],0))
        InV.append(int(n[3],0))
        InV.append(int(n[2],0))
        InV.append(int(n[1],0))
        InV.append(int(n[0],0))

        n='{:08b}'.format(int(InA[1],0))

        InV.append(int(n[7],0))
        InV.append(int(n[6],0))
        InV.append(int(n[5],0))
        InV.append(int(n[4],0))
        InV.append(int(n[3],0))
        InV.append(int(n[2],0))
        InV.append(int(n[1],0))
        InV.append(int(n[0],0))

        InV.append(float(int(InA[3],0))/1000*61.89)
        InV.append(int(InA[4],0))
        InV.append(int(InA[5],0))
        InV.append(int(InA[6],0))
        InV.append(int(InA[7],0))
        InV.append(int(InA[8],0))
        InV.append(int(InA[9],0))
        InV.append(int(InA[10],0))

    except:
        Inv=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    return InV

   
