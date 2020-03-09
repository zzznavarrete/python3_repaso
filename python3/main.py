
clients = 'nicolas, chica,'

def create_client(client_name):
    global clients #Tenemos que declarar esta variable a nivel global para poder ocuparla dentro de la función
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client name already taken')
     
#Se debe dejar al menos 2 espacios entre cada función por una convención de python
def _add_coma():
    global clients
    clients += ','
     

def list_clients():
    global clients
    print(clients)
    

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name , updated_client_name)
    else:
        print('Client name is not in the list')


def _print_welcome():
    print('WELCOME TO MY APP')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')


    
#Ojo, este es el punto de partida principal de python, son 2 '='
if __name__ == '__main__':
   _print_welcome()
   
   command = input()
   command = command.upper()
   client_name = input('What is the client name?')
   
   if command == 'C':
       create_client(client_name)
       list_clients()
   elif command == 'D':
       pass
   elif command == 'U':
       updated_client_name = input('What is the client new name ?')
       update_client(client_name, updated_client_name)
       list_clients()
   else: 
       print('Invalid command')