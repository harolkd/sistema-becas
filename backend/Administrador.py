import Estudiante
class Administrador:
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        self.usuarios = {}
    
    def crear_usuario(self, usuario, clave):
        nuevo_estudiante = Estudiante(usuario, clave)
        self.usuarios[usuario] = nuevo_estudiante
        print(f"Usuario {usuario} creado exitosamente.")
    
    def actualizar_usuario(self, usuario, nueva_clave):
        if usuario in self.usuarios:
            self.usuarios[usuario].clave = nueva_clave
            print(f"Clave de {usuario} actualizada exitosamente.")
        else:
            print(f"Usuario {usuario} no encontrado.")
    
    def cargar_usuarios(self):
        for usuario, estudiante in self.usuarios.items():
            print(f"Usuario: {usuario}, Clave: {estudiante.clave}")
    
    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            del self.usuarios[usuario]
            print(f"Usuario {usuario} eliminado exitosamente.")
        else:
            print(f"Usuario {usuario} no encontrado.")
    
    def crear_calificacion(self, usuario, calificacion):
        if usuario in self.usuarios:
            self.usuarios[usuario].calificacion = calificacion
            print(f"Calificación {calificacion} asignada a {usuario}.")
        else:
            print(f"Usuario {usuario} no encontrado.")
    
    def cargar_calificaciones(self):
        for usuario, estudiante in self.usuarios.items():
            if hasattr(estudiante, 'calificacion'):
                print(f"Usuario: {usuario}, Calificación: {estudiante.calificacion}")
            else:
                print(f"Usuario: {usuario}, Calificación no asignada.")
    
    def eliminar_calificacion(self, usuario):
        if usuario in self.usuarios and hasattr(self.usuarios[usuario], 'calificacion'):
            del self.usuarios[usuario].calificacion
            print(f"Calificación de {usuario} eliminada.")
        else:
            print(f"Usuario {usuario} no tiene calificación asignada o no existe.")

