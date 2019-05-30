import socket
import ctypes, sys

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

filename = 'open ports.txt'

# if is_admin():

host = input("ip компьютера: ")
ports = []

for i in range(100, 200):
    ports.append(i)
    open_port = []

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)
    try:
        sock.connect((host, port))
    except:
        print("Порт %s закрыт" % port)

    else:
        open_port.append(port)
        with open(filename, 'a') as file:
            file.write(str(port) + " " + str("OPEN") + '\n')

if len(open_port) == 0:
    print("Закрыто все!")

sock.close()


# else:
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)