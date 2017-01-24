import socket
import sys
import hashlib

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10002)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

f = open('udpFile', 'w')


def compute_sha256(data):
    m = hashlib.sha256()
    m.update(data)
    return m.hexdigest()

def compute_md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()
    

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    x = ('received %s bytes from %s' % (len(data), address))
    f.write(str(x))
    f.write('\n')

    x = ('sha256 ', compute_sha256(data))
    f.write(str(x))
    f.write('\n')
    
    x = ('md5 ', compute_md5(data))
    f.write(str(x))
    f.write('\n')

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data


