import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    args = raw_input("ENTER URL and PORT and MSG (separated by space): ")
    args = args.split(" ")
    if len(args) == 3:
        
        server_address = (str(args[0]), int(args[1]))
        message = str(args[2])

        print >>sys.stderr, 'sending "%s"' % message
        sock.sendto(message, server_address)

    else:
        raise Exception("3 arg: url and port and msg")
except:
    raise Exception("Something is wrong")
    
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()