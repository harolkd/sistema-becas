from Becas import verificar_beca

class Estudiante:
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        self.calificacion = None
        self.promedio = None
    
    def consultar_calificaciones(self):
        if self.calificacion is not None:
            print(f"Calificación de {self.usuario}: {self.calificacion}")
        else:
            print(f"{self.usuario} aún no tiene calificaciones.")
    
    def verificar_si_es_apto(self):
        if self.calificacion is not None and self.calificacion >= 60:
            print(f"{self.usuario} es apto.")
        else:
            print(f"{self.usuario} no es apto.")
    
    def beca(self, promedio):
        resultado_beca = verificar_beca(self.usuario, promedio)
        print(resultado_beca)




        if user["name"] == name:
            print("name yes")
            if user["password"] == password:
                print("password yes")
                return True
            else:
                return False
        else:
            return False
