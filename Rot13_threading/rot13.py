def rot13_func(mensaje):
    print("El mensaje recibido en la funcion de encriptar es: %s" % str(mensaje))
    mensaje_encriptado = []
    for letra in mensaje[:-1]:
        desp = ord(letra) + 13
        if ord(letra) >= 97 and ord(letra) <= 122:
            if desp > 122:
                desp = desp - 122 + 97 - 1
        else:
            if desp > 90:
                desp = desp - 90 + 65 - 1
        letra_encriptada = chr(desp)
        mensaje_encriptado.append(letra_encriptada)
    return "".join(mensaje_encriptado)