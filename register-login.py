import os 

caracteres_especiales = ["@","#","$","€","&"]

def verificacion_de_contraseña (contraseña):
    if len(contraseña) < 8:
        print("La contraseña NO cumple con los requisitos de longitud ")
        return 
    mayus = False
    minus = False
    numero = False
    especial = False
    
    for i in contraseña:
        if i.isupper():
            mayus = True
        elif i.islower():
            minus = True
        elif i.isnumeric():
            numero = True            
    for i in caracteres_especiales:
        especial = True
    
    if mayus == True and minus == True and numero == True and especial == True:
        return True
    else:
        print("La contraseña NO cumple con los requisitos ")
        return False

def verificacion_de_usuario(usuario):
    with open ('users.json', 'r') as f:
        caracter = ":"
        for i in f:
            i = i.strip()
            posicion = i.find(caracter)
            comprobacion = i[:posicion]
            if usuario == comprobacion:
                print("Ese usuario ya existe prueba con otro: ")
                return
    return True
    
if not os.path.exists('users.json'):
    with open ('users.json', 'w'):
        pass
usuario = input("Introduce el nombre de usuario: ")
verificacion_de_usuario(usuario)
while not verificacion_de_usuario(usuario):
    usuario = input("Introduce el nombre de usuario: ")
    
contraseña = input("Introduce la contraseña de usuario, ten en cuenta que debe de tener 8 caracteres minimo, 1 numero, 1 mayuscula, 1 minuscula y  un caracter especial: ")
verificacion_de_contraseña(contraseña)
while not verificacion_de_contraseña(contraseña):
    contraseña = input("Introduce la contraseña de usuario: ")
    
with open ('users.json', 'a') as f:
    print(f"{usuario}:{contraseña}",file=f)

