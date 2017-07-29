from network_socket import NetworkSocket

eth484 = NetworkSocket()

#These will be the relays

def connect(ip, port, password):
    return eth484.connect_socket(ip, port, password)

def disconnect():
    eth484.close_socket()

def digital_command(command):

    parts = command.split(" ")     # Seperate the parts of the command
    message = None

    if parts[1] == "on":           # Are we turning the io on or off
        message = '\x20'
    else:
        message = '\x21'

    message += chr(int(parts[0]))  # Which io is it

    message += '\x00'              # 0 pulse time

    eth484.write(message)          # send command and read back responce byte
    eth484.read(1)

def set_state(XRele, status):
    message = None
    if status =="on":
        message = '\x20'
    else:
        message = '\x21'

    message += chr(XRele)          # Which io is it
    message += '\x00'              # 0 pulse time
    eth484.write(message)          # send command and read back responce byte
    eth484.read(1)
    

def get_digital():
    command = '\x24'
    eth484.write(command)          # send command and read back responce byte
    states = eth484.read(2)
    return states

def get_analog(index):
    command = '\x32'+chr(index)
    eth484.write(command)
    an = bytearray(eth484.read(2))
    val = an[0] << 8 | an[1]
    return val

def get_input():
    command = '\x25'
    eth484.write(command)          # send command and read back responce byte
    states = eth484.read(2)
    return states
    

def get_states():
    command = '\x24'
    eth484.write(command)          # send command and read back responce byte
    states = eth484.read(2)

    print ('Relay states: '+''.join('{0:04b}'.format(ord(x), 'b') for x in states[0]))
    print ('Digital outputs: '+''.join('{0:08b}'.format(ord(x), 'b') for x in states[1]))

    command = '\x25'
    eth484.write(command)
    states = eth484.read(2)

    print ('Digital inputs: '+''.join('{0:08b}'.format(ord(x), 'b') for x in states[1]))

    for index in range(1, 5):   # Get Analogue values
        command = '\x32'+chr(index)
        eth484.write(command)
        an = bytearray(eth484.read(2))
        val = an[0] << 8 | an[1]
        print ('Analogue input {:d}: {:d}'.format(index, val))


