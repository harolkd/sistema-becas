users_dict = [{
            "name": "rodrigo",
            "password": "123",
            "notas": [{
                "name": "calculo",
                "creditos": 3,
                "nota": 4.3
            }, {
                "name": "fisica",
                "creditos": 4,
                "nota": 3.5
            }, {
                "name": "religion",
                "creditos": 1,
                "nota": 4.0
            }]
        },
        {
            "name": "admin",
            "password": "root",
            "notas": []
        }
        ]

def eliminar_usuario(name: str) -> int:
    users_dict.pop(name)
    return 0

def agregar_usuario(usuario) -> int:

    users_dict[usuario.name]
    return 0

def login_user(name: str, password:str):
    for user in users_dict:
        if user["name"] == name:
            if user["password"] == password:
                return True
            else:
                return False
    return False
        
    