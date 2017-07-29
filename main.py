from sys import *
from eth484 import *
from pygame import *
from pygame.locals import *
from random import *


FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480





py3 = version_info[0] > 2  #Get python version

exit = False

class cls(object):
    def __repr__(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        return ''

cls = cls()  # Now printing cls will clear the screen

def set_exit(command):
    disconnect()
    global exit
    exit = 0

def help_text(command):
    print (cls)
    print ("Invalid command entered.")
    print ("To change state of digital port type number of port followed by on of off,")
    print ("e.g. \'3 on\' to turn output 3 on.\n")
    print ("To refresh the displayed states on the screen type\'states\'.\n")
    print ("To exit type \'exit\'.\n")
    if py3:
        ip_address = input("Press enter to continue")
    else:
        ip_address = raw_input("Press enter to continue")

def no_action(comand):
    print (cls)

def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 1)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

function_dict = {
    "1 on": digital_command,
    "1 off": digital_command,
    "2 on": digital_command,
    "2 off": digital_command,
    "3 on": digital_command,
    "3 off": digital_command,
    "4 on": digital_command,
    "4 off": digital_command,
    "9 on": digital_command,
    "9 off": digital_command,
    "10 on": digital_command,
    "10 off": digital_command,
    "11 on": digital_command,
    "11 off": digital_command,
    "12 on": digital_command,
    "12 off": digital_command,
    "13 on": digital_command,
    "13 off": digital_command,
    "14 on": digital_command,
    "14 off": digital_command,
    "15 on": digital_command,
    "15 off": digital_command,
    "16 on": digital_command,
    "16 off": digital_command,
    "states": no_action,
    "exit": set_exit}

# print cls

ip_address="192.168.1.6"
port = 17494
password =""

global FPSCLOCK, DISPLAYSURF, BASICFONT

#pygame.init()
#FPSCLOCK = pygame.time.Clock()
#DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
#pygame.display.set_caption('Wormy')


exit = connect(ip_address, int(port), password)

get_states()

while exit:
    print cls 
    

    key = getkey()

    print key
    
    #if py3:
    #    response = input(">>")
    #else:
    #    response = raw_input(">>")

    #function_dict.get(response, help_text)(response)

