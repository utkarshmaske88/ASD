import socket
Server_ip="localhost"
Server_host=8002
FORMAT="utf-8"
SS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SS.bind((Server_ip,Server_host))
SS.listen(5)
s1, addr=SS.accept()
file_name= s1.recv(1024).decode(FORMAT)
print(file_name)
file=open(file_name,"w")
s1.send("abc.txt".encode(FORMAT)) 
data=s1.recv(1024).decode(FORMAT)
print("File data received")
s1.send("abc.txt".encode(FORMAT))
file.write(data)
file.close()

