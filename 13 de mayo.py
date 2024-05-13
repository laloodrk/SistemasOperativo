import subprocess

def ejecutar (comando):
    subprocess.run(comando, shell=True)

while True:
    
    print("1.Crear archivo 'mis notas.txt'")
    print("2.Crear carpeta 'calificaciones'")
    print("3.Crear subcarpeta 'Primer Parcial'")
    print("4.Mover archivo 'Mis notas.txt' a la carpeta 'calificaciones'")
    print("5.Mover programa'Calculadora.py' a la subcarpeta 'primerparcial'")
    print("6.Salir")

    opcion = input ("Selecciona una opcion:")

    if opcion == "1":
      ejecutar ("touch misnotas.txt")

    elif opcion == "2":
        ejecutar ("mkdir calificaciones")
    elif opcion == "3":
        ejecutar ("mkdir calificaciones/primerparcial")
    elif opcion == "4":
         ejecutar ("mv misnotas.txt calificaciones")
    elif opcion == "5":
        ejecutar ("mv Documentos/Calculadora.py calificaciones/primerparcial")
    elif opcion == "6":
        print("Finalizando el programa")
        break
    else:
        print("Ingresa una opcion del menu")
    

    
