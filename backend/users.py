import json

with open('backend/db.json', 'r') as data:
    users_dict = json.load(data)

ultimo_usuario = "admin"

def eliminar_usuario(name: str):
    i = -1
    for user in users_dict:
        i += 1
        if user["name"] == name:
            users_dict.pop(i)
    return

def agregar_usuario(usuario):
    users_dict.append(usuario)
    ultimo_usuario = str(usuario["name"])
    return

def agregar_nota(nota):
    i = -1
    for user in users_dict:
        i += 1
        if user["name"] == ultimo_usuario:
            nuevas_notas = user["notas"]
            nuevas_notas.append(nota)

            nuevo_usuario = {
                "name": user["name"],
                "password": user["password"],
                "notas": nuevas_notas
            }

            eliminar_usuario(user["name"])
            agregar_usuario(nuevo_usuario)
    return

def eliminar_notas(username: str, name: str):
    i = -1
    for user in users_dict:
        i += 1
        if user["name"] == username:
            nuevas_notas = user["notas"]
            j = -1
            for nota in nuevas_notas:
                j += 1
                if nota == name:
                    nuevas_notas.pop(j)
            print(nuevas_notas)

            nuevo_usuario = {
                "name": user["name"],
                "password": user["password"],
                "notas": nuevas_notas
            }

            eliminar_usuario(user["name"])
            agregar_usuario(nuevo_usuario)
    return

def login_user(name: str, password:str):
    for user in users_dict:
        if user["name"] == name:
            if user["password"] == password:
                return True
            else:
                return False
    return False
        
if __name__ == "__main__":
    print(users_dict)