import socket
conexao=socket.socket()
print ("$$$$ SEJA BEM VINDO AO PYTHON-SCANNER$$$$$")
IP= input("Digite o IP ou dominio:")
PORTA=int(input("Digite a Porta:"))
u=int(input("Digite o tempo de espera:"))
conexao.settimeout(u)
n=conexao.connect_ex((IP,PORTA))
if (n==0):
  print("Porta aberta")
else:
  print("porta fechada")
 

  
  