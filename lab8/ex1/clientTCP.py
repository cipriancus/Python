import socket,time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    args = raw_input("ENTER URL and PORT (separated by space): ")
    args = args.split(" ")
    if len(args) == 2:
        addr = args[0]
        port = args[1]
      
        s.connect((str(addr), int(port)))
        s.send(b"Mesaj 1")
        time.sleep(1)
        s.send(b"exit")
        s.close()

    else:
        raise Exception("2 arg: url and port")
except:
    raise Exception("Something is wrong")
