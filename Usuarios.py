class Usuario:
    def __init__(self, name, clave, type, notas):
        self.name = name
        self.clave = clave
        self.type = type
        self.notas = None
    
    def get_Name():

    def get_Notas():

    def get_Promedio() -> int:
        promedio = 0

        if notas == []:
            return 0

        for i in notas:
            x = i.promedio * i.creditos
            promedio += x
        return promedio