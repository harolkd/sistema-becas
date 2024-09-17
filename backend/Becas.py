def verificar_beca(usuario, promedio):
    if promedio >= 4.8:
        return f"Ha obtenido la beca del 50%"
    elif 4.8 > promedio >= 4.3:
        return f"Ha obtenido la beca del 20%"
    else:
        return f"Lo sentimos, {usuario} no puede adquirir una beca."