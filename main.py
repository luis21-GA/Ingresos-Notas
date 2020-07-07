# Luis Guillermo García Aguilar  GA14018
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
# Sirve para interactuar con el sistema operativo
from os import system

cls = lambda: system("cls")

# Nombre del archivo .csv que funcionará como base de datos
# para almacenar la información de los alumnos
BBDD_NAME = "bbdd"

def get_data(csv_name, orient='index'):
  """
    Obtiene los datos provenientes de un archivo .csv con el nombre especificado en
    csv_name. En caso de que el archivo no exista, se retornará False
  """
  try:
    return pd.read_csv(csv_name + ".csv",
                      sep=",",
                      names=['Id', 'Nombres', 'Nota1', 'Nota2', 'Nota3', 'Promedio'],
                      skiprows=1,
                      index_col='Id').to_dict(orient=orient)
  except:
    return False

def add_data(csv_name, data):
  """
    Inserta la información almacenada en data dentro del archivo .csv que responda
    al nombre almacenado en csv_name
  """
  df = pd.DataFrame(data, columns = ['Nombres', 'Nota1', 'Nota2', 'Nota3', 'Promedio'])
  df.to_csv(csv_name + ".csv", sep=",")

def add_student():
  global BBDD_NAME
  
  # Obteniendo los datos de los alumnos en forma de lista
  s = get_data(BBDD_NAME,"list")

  # Validando. Si la base de datos no existe, se hace la preparación
  # para crearla
  if not s: s = {'Nombres': [],'Nota1': [],'Nota2': [],'Nota3': [],'Promedio': []}

  # Obteniendo las credenciales del nuevo alumno

    # Se valida que el nombre no este vacio
  while True:
    noms = input("\nNombre completo del estudiante: ")
    if noms != "":
      print("\nEl nombre del estudiante es: ",noms,"\n")
      break
    else:
      print("\nError! ¡Ingrese el nombre del estudiante!\n")
	    
  # Se valida si su nota 1 esta entre 0 y 10
  while True:
    not1 = float(input("Nota 1 del estudiante: "))
    if not1 >= 0:
      if not1 <= 10:
        print("\nLa nota 1 de",noms,"es:",not1,"\n")
        break
      else: 
        print("\nError! La nota 1 debe estar entre 0 y 10. No pude ser:",not1,"\n")
    else:
      print("\nError! La nota 1 debe estar entre 0 y 10. No pude ser:",not1,"\n")  

  # Se valida si su nota 2 esta entre 0 y 10
  while True:
    not2 = float(input("Nota 2 del estudiante: "))
    if not2 >= 0:
      if not2 <= 10:
        print("\nLa nota 2 de",noms,"es:",not2,"\n")
        break
      else: 
        print("\nError! La nota 2 debe estar entre 0 y 10. No pude ser:",not2,"\n")
    else:
      print("\nError! La nota 2 debe estar entre 0 y 10. No pude ser:",not2,"\n")  

  # Se valida si su nota 3 esta entre 0 y 10
  while True:
    not3 = float(input("Nota 3 del estudiante: "))
    if not3 >= 0:
      if not3 <= 10:
        print("\nLa nota 3 de",noms,"es:",not3,"\n")
        break
      else: 
        print("\nError! La nota 3 debe estar entre 0 y 10. No pude ser:",not3,"\n")
    else:
      print("\nError! La nota 3 debe estar entre 0 y 10. No pude ser:",not3,"\n")  
  
  # Calculando el promedio (Se usa format para guardar solo 2 decimales)
  prom = float("{:.2f}".format(((not1 + not2 + not3) / 3)))

  # Mostrando mensaje si aprobo o reprobo
  if prom >= 6:
    print("Promedio de",noms,"es de:",prom,".APROBADO!")
  else:  
    print("Promedio de",noms,"es de:",prom,".REPROBADO!")
    
  # Añadiendo la información del nuevo alumno a la información ya obtenida
  # para poder ingresarla en la base de datos (el archivo .csv)
  s['Nombres'].append(noms or "---")
  s['Nota1'].append(not1 or "---")
  s['Nota2'].append(not2 or "---")
  s['Nota3'].append(not3 or "---")
  s['Promedio'].append(prom or "---")

  # Añadiendo todos los datos al archivos .csv
  add_data(BBDD_NAME, s)
  print("\nEstudiante añadido exitosamente...\n")

def get_students():
  global BBDD_NAME

  # Obteniendo los datos de los alumnos en forma de indice
  students = get_data(BBDD_NAME)

  # Validando. En caso de no exitir el archivo o que no haya ningún registro en él,
  # se le hará a conocer al usuario
  if not students or not students.keys():
    print("\nNo hay usuarios registrados\n")
    return
  
  print("\n")
  # Iniciando recorrido de los datos obtenidos en el archivo
  f = True
  for i, student in students.items():
    if f: f = False
    else: print("-----------------------------------")
    print("Id alumno:",i)
    print("   Nombres:",student['Nombres'])
    print("   Nota 1:",student['Nota1'])
    print("   Nota 2:",student['Nota2'])
    print("   Nota 3:",student['Nota3'])
    print("   Promedio:",student['Promedio'])
  print("\n")  

def update_student():
  global BBDD_NAME

  # Obteniendo los datos de los alumnos en forma de lista
  s = get_data(BBDD_NAME, 'list')

  # Validando. En caso de no exitir el archivo o que no haya ningún registro en él,
  # se le hará a conocer al usuario
  if not s or not s.keys():
    print("\nNo hay usuarios registrados\n")
    return

  # Obteniendo Id del usuario a modificar
  # Se valida para que el Id sea positivo
  while True:
    n_id = int(input("\nId del estudiante a modificar: "))
    if n_id >= 0:
      break
    else:
      print("\nError! El Id es negativo...\n")  

  if n_id >= len(s['Nombres']):
    print("\n<<<<< El estudiante que quieres modificar no existe >>>>>\n")
    return
  
  # Mostrando información del usuario a modificar
  print("\nDatos del estudiante a modificar. ID:",n_id)
  print("Nombre Completo:", s['Nombres'][n_id])
  print("Nota 1:", s['Nota1'][n_id])
  print("Nota 2:", s['Nota2'][n_id])
  print("Nota 3:", s['Nota3'][n_id])
  print("Promedio:", s['Promedio'][n_id])

  # Obteniendo nueva información del usuario a modificar
  
  # Se valida que el nombre a modificar no este vacio
  while True:
    n_noms = input("\nIngrese el nuevo nombre del estudiante: ")
    if n_noms != "":
      print("\nEl nuevo nombre del estudiante es: ",n_noms,"\n")
      break
    else:
      print("\nError! ¡Ingrese el nombre del estudiante a modificar!\n")
  

  # Se valida si su nota 1 a modificar esta entre 0 y 10
  while True:
    n_nota1 = float(input("Ingrese Nota 1 a modificar: "))
    if n_nota1 >= 0:
      if n_nota1 <= 10:
        print("\nLa nueva nota 1 de",n_noms,"es:",n_nota1,"\n")
        break
      else: 
        print("\nError! La nota 1 debe estar entre 0 y 10. No pude ser:",n_nota1,"\n")
    else:
      print("\nError! La nota 1 debe estar entre 0 y 10. No pude ser:",n_nota1,"\n")  

  # Se valida si su nota 2 a modificar esta entre 0 y 10
  while True:
    n_nota2 = float(input("Ingrese Nota 2 a modificar: "))
    if n_nota2 >= 0:
      if n_nota2 <= 10:
        print("\nLa nueva nota 2 de",n_noms,"es:",n_nota2,"\n")
        break
      else: 
        print("\nError! La nota 2 debe estar entre 0 y 10. No pude ser:",n_nota2,"\n")
    else:
      print("\nError! La nota 2 debe estar entre 0 y 10. No pude ser:",n_nota2,"\n")  

  # Se valida si su nota 3 a modificar esta entre 0 y 10
  while True:
    n_nota3 = float(input("Ingrese Nota 3 a modificar: "))
    if n_nota3 >= 0:
      if n_nota3 <= 10:
        print("\nLa nueva nota 3 de",n_noms,"es:",n_nota3,"\n")
        break
      else: 
        print("\nError! La nota 3 debe estar entre 0 y 10. No pude ser:",n_nota3,"\n")
    else:
      print("\nError! La nota 3 debe estar entre 0 y 10. No pude ser:",n_nota3,"\n")  

  # Calculando el promedio (Se usa format para guardar solo 2 decimales)
  n_prom = float("{:.2f}".format(((n_nota1 + n_nota2 + n_nota3) / 3)))

  # Mostrando mensaje si aprobo o reprobo
  if n_prom >= 6:
    print("Promedio nuevo de",n_noms,"es de:",n_prom,".APROBADO!")
  else:  
    print("Promedio nuevo de",n_noms,"es de:",n_prom,".REPROBADO!")

  # Reemplazando información antigua por la nueva
  s["Nombres"][n_id] = n_noms or s["Nombres"][n_id]
  s["Nota1"][n_id] = n_nota1 or s["Nota1"][n_id]
  s["Nota2"][n_id] = n_nota2 or s["Nota2"][n_id]
  s["Nota3"][n_id] = n_nota3 or s["Nota3"][n_id]
  s["Promedio"][n_id] = n_prom or s["Promedio"][n_id]
  # Guardando datos modificados
  add_data(BBDD_NAME, s)
  print("\nEstudiante modificado exitosamente...\n")

def delete_student():
  global BBDD_NAME

  # Obteniendo los datos de los alumnos en forma de lista
  s = get_data(BBDD_NAME, 'list')

  # Validando. En caso de no exitir el archivo o que no haya ningún registro en él,
  # se le hará a conocer al usuario
  if not s or not s.keys():
    print("\nNo hay usuarios registrados\n")
    return

  # Obteniendo Id del usuario a modificar
  # Se valida para que el Id sea positivo
  while True:
    n_id = int(input("\nId del estudiante a eliminar: "))
    if n_id >= 0:
      break
    else:
      print("\nError! El Id es negativo...\n")  
  
  if n_id >= len(s['Nombres']):
    print("\n<<<<< El estudiante que quieres eliminar no existe >>>>>\n")
    return

  # Mostrando información del usuario a eliminar
  print("\nNombre Completo:", s['Nombres'][n_id])
  print("Nota 1:", s['Nota1'][n_id])
  print("Nota 2:", s['Nota2'][n_id])
  print("Nota 3:", s['Nota3'][n_id])
  print("Promedio:", s['Promedio'][n_id])
  
  # Reafirmando
  r = input("\n¿Seguro que quieres eliminar este usuario? (s/n): ")

  if r.lower() == 's':
    del s['Nombres'][n_id]
    del s['Nota1'][n_id]
    del s['Nota2'][n_id]
    del s['Nota3'][n_id]
    del s['Promedio'][n_id]

    # Guardando datos modificados
    add_data(BBDD_NAME, s)
    print("\nEstudiante eliminado exitosamente...")
    print("Los Id de los estudiantes han sido modificados...\n")

def graph_student():    

  # Leyendo el csv
  df=pd.read_csv("bbdd.csv")

  # Definiendo las columnas
  df.columns=["Id,","Nombres","Nota1","Nota2","Nota3","Promedio"]
  Titulos=df["Nombres"]
  p1=df["Nota1"]
  p2=df["Nota2"]
  p3=df["Nota3"]
  Promedio = df["Promedio"]

  # Definiendo el tamaño de la vista
  plt.figure(figsize=(12, 5))
  plt.suptitle('Gráficas')

  # Primer grafica (tamano, datos)
  plt.subplot(2, 1, 1)
  plt.title("Gráfica de Promedio")
  plt.xlabel("NOMBRE ESTUDIANTES")
  plt.ylabel("PROMEDIO")
  plt.bar(Titulos, Promedio)

  # Segunda grafica (tamano, datos)
  plt.subplot(223)
  plt.title("Gráfica de Notas")
  plt.xlabel("NOMBRE ESTUDIANTES")
  plt.ylabel("NOTAS")
  plt.scatter(Titulos, p1, color='tab:blue', label="Parcial 1")
  plt.scatter(Titulos, p2, color='tab:green', label="Parcial 2")
  plt.legend(p2)
  plt.scatter(Titulos, p3, color='tab:red', label="Parcial 3") 
  plt.legend(p3)

  # Modificacion de label y distancia de las graficas
  plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
  plt.subplots_adjust(hspace=0.50, wspace=0.0)
  plt.show()
  print("\n")

def main():
  print("---------- Registro de alumnos ----------")
  print("1. Agregar un nuevo estudiante")
  print("2. Obtener lista de todos los estudiantes")
  print("3. Actualizar información de un estudiante")
  print("4. Eliminar un estudiante")
  print("5. Estadisticas de los estudiantes")
  print("6. Salir del programa")
  op = input("Elige una opción: ")

  if op == "1":
    add_student()
  elif op == "2":
    get_students()
  elif op == "3":
    update_student()
  elif op == "4":
    delete_student()
  elif op == "5":
    graph_student()
  elif op == "6":
    print("Que tenga un buen día :)")
    input("\nPresione Enter para salir...")
    exit()
  else:
    print("Opción inválida")
    input("\nPresione Enter para continuar...")

while True: main()
