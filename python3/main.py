
clients = 'nicolas, chica,'

def create_client(client_name):
    global clients #Tenemos que declarar esta variable a nivel global para poder ocuparla dentro de la función
    clients += client_name
    _add_coma()
     
#Se debe dejar al menos 2 espacios entre cada función por una convención de python
def _add_coma():
    global clients
    clients += ','
     

def list_clients():
    global clients
    print(clients)

#Ojo, este es el punto de partida principal de python, son 2 '='
if __name__ == '__main__':
    list_clients()
    create_client('rex')
    list_clients()