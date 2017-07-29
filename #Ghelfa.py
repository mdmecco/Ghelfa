import pygame
import sys
from pygame.locals import *
from eth484 import *
from datetime import *
import httplib
import string
from LetturaTelecamereWEB import *
from LGlobale import *
from Denkovi import *
from PyGameModule import *


ip_address="192.168.1.6"
port = 17494
password =""

Wn=Windows()

i=0

Wn.showTextScreen('GHELFA',1,(255,90,90),CENTER)

exit = connect(ip_address, int(port), password)

now=datetime.now()
DayTSec=(((now.hour *60) + now.minute)*60)+now.second

Wn.showTextScreen ("q=Quit 1=Apre Polli  2=Chiude Polli  4=Luce Fuori  R=Refresh IP",26, LIGHTYELLOW,LEFT)

SPul="0"
RLampione=0
TLampione=0
IPB=0
SR=0
Nv=0
BackLamp=0
TUpLoadTelecamere=0
RefreshTelecamere=300 #secondi di attesa per il refresh delle telecamere
RR1B="" #Definisce lo stato rele precedente


#TPApre="15:30"
#TPChiude="21:30"
PPS=0
TPApre="16:00"
TPChiude="23:00"
LPolliR="12:00"

SendStatoPolli=0
StatoPolli=0
MPApre=TimeConvert(TPApre)
MPChiude=TimeConvert(TPChiude)
LPolliRS=TimeConvert(LPolliR)
LPMS=0
LPLumLimit=20


if (DayTSec > MPApre ):
    PPS=3    

if (DayTSec > MPChiude ):
    PPS=6    




PPA=0
PPC=0

#Variabili di gestione del lampione e delle luci
TGestioneI="19:00" #Ora di inizio dell'orario continuo
TGestioneF="23:45" #Ora di fine dell'orario continuo

LIG=TimeConvert(TGestioneI) 
LFG=TimeConvert(TGestioneF)
LDG=30 #Durata accensione periodo luce
LDN=600 #Durata accensione periodo buio


#Variabili gestione degli ingressi analogici
NrElementi=50
A1A=range(NrElementi)
A2A=range(NrElementi)
A3A=range(NrElementi)
A4A=range(NrElementi)
AAI=0
AAS=0
AAE=0

ADCTLOG=0


Wn.showTextScreen ("Apertura:"+ str(MPApre) ,23, LIGHTBLUE,LEFT)
Wn.showTextScreen ("Chiusura:"+ str(MPChiude) ,24, LIGHTBLUE,LEFT)


def set_exit(command):
    disconnect()
    global exit
    exit = 0

while 1:
    Wn.showTextScreen ("Status:INIT          ",9,(50,255,50),LEFT)
    GT= pygame.time.get_ticks()
    Minuti=GT/60000
    Secondi=GT/1000

    now=datetime.now()
    #TData=str(now.year)+"/"+str(now.month)+"/" + str(now.day) + "  " +str(now.hour) +":" + str(now.minute)+":" + str(now.second)
    TData=str(now.year)+"/"+"{:0>2d}".format(now.month)+"/" + "{:0>2d}".format(now.day) + "  " +"{:0>2d}".format(now.hour) +":" + "{:0>2d}".format(now.minute)+":" + "{:0>2d}".format(now.second)
    TDataIt="{:0>2d}".format(now.day) +"/"+"{:0>2d}".format(now.month) + "/" + str(now.year)  + "T" +"{:0>2d}".format(now.hour) +":" + "{:0>2d}".format(now.minute)+":" + "{:0>2d}".format(now.second)
    Wn.showTextScreen ("   " + TData + " ",1 , LIGHTGREEN,RIGHT)

    #In un giorno ci sono 86400 secondi
    DayTSec=(((now.hour *60) + now.minute)*60)+now.second
    Wn.showTextScreen ("    M:"+str(Minuti)+ " S:"+ str(Secondi)+ " DT:" + str(DayTSec) + "    " ,25, LIGHTYELLOW,RIGHT)

#-------------------------------------------------------------------------------------------------------------------
#----------------  Lettura Analogica  ------------------------------------------
#-------------------------------------------------------------------------------------------------------------------    
    Wn.showTextScreen ("Status:ANALOG          ",9,(50,255,50),LEFT)

    AAI=AAI+1
    AAI=AAI % (NrElementi-1)
    
    A1A[AAI] =int((float(get_analog(1))/1024*5)*20)
    A2A[AAI] =int((float(get_analog(2))/1024*5)*20)
    A3A[AAI] =int((float(get_analog(3))*3300 / 1024)-500)/10
    A4A[AAI] =int((float(get_analog(4))*3300 / 1024)-500)/10

    AAS=0
    for AAE in A1A:
        AAS=AAS+AAE
    A1=AAS/NrElementi

    AAS=0
    for AAE in A2A:
        AAS=AAS+AAE
    A2=AAS/NrElementi
    
    AAS=0
    for AAE in A3A:
        AAS=AAS+AAE
    A3=AAS/NrElementi

    AAS=0
    for AAE in A4A:
        AAS=AAS+AAE
    A4=AAS/NrElementi


         
    Wn.showTextScreen ( 'Analog1=' + str(A1) + "    - ",1 ,WHITE ,LEFT)
    Wn.showTextScreen ( 'Analog2=' + str(A2) + "    - ",2 ,WHITE ,LEFT)
    Wn.showTextScreen ( 'Analog3=' + str(A3) + "    - ",3 ,WHITE ,LEFT)
    Wn.showTextScreen ( 'Analog4=' + str(A4) + "    - ",4 ,WHITE ,LEFT)
    Wn.showTextScreen ( 'Analog1=' + str(get_analog(3)) + "    - ",5 ,WHITE ,LEFT)

#-------------------------------------------------------------------------------------------------------------------
#----------------  Lettura Digitale   ------------------------------------------
#-------------------------------------------------------------------------------------------------------------------    

    Wn.showTextScreen ("Status:DIGIT          ",9,(50,255,50),LEFT)

    DD=get_digital()
    RR=''.join('{0:04b}'.format(ord(x), 'b') for x in DD[0])
    RR1=RR[3] + RR[2]+RR[1]+RR[0]
    Wn.showTextScreen ('Relay  states: ' + RR1 ,6,(50,255,50),LEFT)
    Wn.showTextScreen (('Digital Output: '+''.join('{0:08b}'.format(ord(x), 'b') for x in DD[1])) ,7,(50,255,50),LEFT)

    #Lettura ingressi
    II=get_input()
    III=''.join('{0:08b}'.format(ord(x), 'b') for x in II[1])
    Wn.showTextScreen ('Digital Input:' + III ,8,(50,255,50),LEFT)

#-------------------------------------------------------------------------------------------------------------------
#----------------Gestione del sincronismo dell'inidirizzo IP sul sito web-------------------------------------------
#-------------------------------------------------------------------------------------------------------------------    
    Wn.showTextScreen ("Status:SINK IP          ",9,(50,255,50),LEFT)
    if (IPB==0):
        try:
            Nv=Nv+1
            conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
            conn.request("GET", "/Ghelfa/ip.php")
            r1=conn.getresponse()
            Wn.showTextScreen ("Nr Synk Request:" + str(Nv) +" IP:" + r1.read() + "   ",18 , GREEN,LEFT)
            Wn.showTextScreen ("Last Synk Request:" + TData + "   ",19 , GREEN,LEFT)
            IPB=Minuti +60
            conn.close
        except:
            IPB=Minuti +2

    if (Minuti>IPB ):
        IPB=0

    #Spedizione stato rele
    #if (RR1B <> RR1) :
    #    try:
    #        conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
    #        conn.request("GET", "/Ghelfa/RELESET.php?StatoR=" + RR1 + "&RELE.TXT")
    #        conn.close
    #        RR1B=RR1
    #    except:
    #        RR1B=""

#-------------------------------------------------------------------------------------------------------------------
#---------------- Gestione log lumionosita' -----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


    Wn.showTextScreen ("Status:LUX          ",9,(50,255,50),LEFT)

    if Minuti > ADCTLOG:
        print "LUX"
        TDnk=0
        #TDenk=ReadDenkovi()
        #TDnk=float(int(TDenk[16]*10))/10
        LUXS= TDataIt + ";" + str(A1)+ ";" + str(A2)+ ";" + str(A3)+ ";" + str(A4) + ";" + str(TDnk)
        Wn.showTextScreen ("ADC:" + LUXS + " -> " +r1.reason + "      Next:" + str(ADCTLOG) + "    ",17 , GREEN,LEFT)
        try:
            conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
            conn.request("GET", "/Ghelfa/LOG.php?StatoR=" + LUXS + "&FileTS=ADCLOG")
            r1=conn.getresponse()
            conn.close
            ADCTLOG=Minuti+10
        except:
            ADCTLOG=0
            
        Wn.showTextScreen ("ADC:" + LUXS + " -> " +r1.reason + "      Next:" + str(ADCTLOG) + "    ",17 , GREEN,LEFT)

#-------------------------------------------------------------------------------------------------------------------
#---------------- Gestione Luce pollaio -----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


#LPolliRS=TimeConvert(LPolliR)
#LPMS=0
#LPLumLimit=20
#A2
#set_state(4,"off")        

    if (DayTSec > 43200) and (LPMS==0): #a mezzogiorno si resetta tutto
        LPMS=1
        
    if (LPMS==1):
        if (A2 < 20):
            set_state(3,"on")
            LPMS=2
            LPTSec=DayTSec

    if (LPMS==2):
        if (DayTSec > (LPTSec+10800)):
            set_state(3,"off")
            LPMS=3

    if (LPMS==3):
        if (DayTSec< 60):
            LPMS=0
    
    Wn.showTextScreen ( 'Gestione Polli= LPMS:' + str(LPMS) + "    - ",10 ,WHITE ,LEFT)
    
#-------------------------------------------------------------------------------------------------------------------
#---------------- Gestione upload Telecamere -----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    if (DayTSec > TUpLoadTelecamere):
        Wn.showTextScreen ("Status:CAM          ",9,(50,255,50),LEFT)
        TT=SaveCAM(Wn)
        TUpLoadTelecamere=DayTSec+RefreshTelecamere
        Wn.showTextScreen ("Refresh Telecamere:" + TData + "   ",20 , GREEN,LEFT)

    if (TUpLoadTelecamere > 86400) and (DayTSec < RefreshTelecamere):
        TUpLoadTelecamere=TUpLoadTelecamere - 86400


#-------------------------------------------------------------------------------------------------------------------
#----------------Gestione Apertura polli----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
    #Il meccanismo funziona con due rele che vengono attivati per apertura e
    #chiusura della porta polli
    #rele 2 > chiude
    #rele 1 > apre
    #servono circa 8 secondi per aprire o chiudere quindi i rele vengono disattivati dopo questo tempo

    #attivazione apertura ad orario
    if (DayTSec > MPApre) and (PPS==0): 
        if (MPApre >= MPChiude):
            PPS=6
        else:
            PPS=1
            set_state(1,"on")
            set_state(2,"off")

    if (RR[3]=="1") and (PPS<>2):
        set_state(2,"off")
        StatoPolli=1
        SendStatoPolli=1
        PPS=2
        PPA=Secondi + 15
        
    if (Secondi > PPA) and (RR[3]=="1"): #Stacco Rele
        set_state(1,"off")
        set_state(2,"off")
        PPS=3
        

    #attivazione chiusura ad orario
    if (DayTSec > MPChiude) and (PPS==3): 
        set_state(2,"on")
        set_state(1,"off")
        PPS=4

    if (RR[2]=="1") and (PPS<>5):
        set_state(1,"off")
        StatoPolli=2
        SendStatoPolli=1
        PPS=5
        PPA=Secondi + 15

    if (Secondi > PPA) and (RR[2]=="1"): #Stacco Rele
        set_state(2,"off")
        set_state(1,"off")
        PPS=6

    if (DayTSec < 5) and (PPS<>0):
        PPS=0

    Wn.showTextScreen ("Stato:"+ str(PPS) + "  SSP:" + str(SendStatoPolli) + "  SP:" + str(StatoPolli) + "  " ,25, LIGHTBLUE,LEFT)


    if (SendStatoPolli == 1):
        SendStatoPolli= 0
        try:    
            #trasmissione stato al sito web
            conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
            conn.request("GET", "/Ghelfa/RELESET.php?StatoR=" + StatoPolli + "&FileTS=PORTAP.TXT")
            r1=conn.getresponse()
            conn.close
        except:
            SendStatoPolli=1 #fa in modo che ci riprovi all'infinito
            IPB=Minuti +2 #Se salta, fa aggiornare anche l'IP




#-------------------------------------------------------------------------------------------------------------------
#----------------------GESTIONE LAMPIONE ---------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------        
        #Si tratta del rele nr 4 che viene letto dal byte RR[0]
        #Il la luce attiva viene letta dal canale III[0]

    #disattivazione automatica rele dopo 1 secondo
    #if (RR[0]=="1") and (RLampione == 0):
    #    RLampione = GT + 1500

    #if (RLampione < GT) and (RR[0]=="1") and (RLampione <> 0):
    #    set_state(4,"off")
    #    RLampione =0

    #gestione del tempo di attivazione
    #if (TLampione <> 0) and (TLampione < Secondi):
    #    set_state(4,"off")
    #    TLampione =0
    
    #if (BackLamp<>III[0]) :
    #    set_state(4,"off")
    #    RLampione =0
    #    BackLamp=III[0]
    #if (BackLamp == "1"): #Il lampione si è appena acceso
    #        if ((int(A2) > 0 ) or (DayTSec > LFG)): #significa che sono nella fase diurna
    #            TLampione = Secondi + LDG
    #        else: #sono nella fase notturna
    #            TLampione = Secondi + LDN 
    #    else:
    #        TLampione = 0

     #   try:    
     #       #trasmissione stato al sito web
     #       conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
     #       conn.request("GET", "/Ghelfa/RELESET.php?StatoR=" + BackLamp + "&FileTS=LUCE.TXT")
     #       r1=conn.getresponse()
     #       conn.close
     #   except:
     #       BackLamp=2 #fa in modo che ci riprovi all'infinito
     #       IPB=Minuti +2 #Se salta, fa aggiornare anche l'IP


    if (SPul <> III[0]):
        SPul = III[0]
        if (III[0]=="1"):
            if (BackLamp == "1"):
                set_state(4,"off")
            else:
                set_state(4,"on")


    if (TLampione <> 0) and (TLampione < Secondi):
        set_state(4,"off")
        TLampione =0


    if (BackLamp<>RR[0]):
        BackLamp=RR[0]
        if (BackLamp == "1"):
            #La luce si è accesa
            RLampione=0
            if ((int(A2) > 0 ) or (DayTSec > LFG)): #significa che sono nella fase diurna
                TLampione = Secondi + LDG
            else: #sono nella fase notturna
                TLampione = Secondi + LDN 
        else:
            #La luce si è spenta
            TLampione=0

        try:    
            #trasmissione stato al sito web
            conn=httplib.HTTPConnection("www.mdmecco.it",80,timeout=10)
            conn.request("GET", "/Ghelfa/RELESET.php?StatoR=" + BackLamp + "&FileTS=LUCE.TXT")
            r1=conn.getresponse()
            conn.close
        except:
            BackLamp=2 #fa in modo che ci riprovi all'infinito
            IPB=Minuti +2 #Se salta, fa aggiornare anche l'IP
            


            
        

#---------------------------------------------------------------------   
       
        
    

    #Attivazione rele
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                SR=1
                if RR[3]=="0":
                    set_state(1,"on")
                else:
                    set_state(1,"off")
                    

            if event.key == pygame.K_2:
                SR=1
                if RR[2]=="0":
                    set_state(2,"on")
                else:
                    set_state(2,"off")

            if event.key == pygame.K_3:
                SR=1
                if RR[1]=="0":
                    set_state(3,"on")
                else:
                    set_state(3,"off")

            if event.key == pygame.K_4:
                SR=1
                if RR[0]=="0":
                    set_state(4,"on")
                else:
                    set_state(4,"off")
                

            if event.key == pygame.K_r:
                IPB=0

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()



