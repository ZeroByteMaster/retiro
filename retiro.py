#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os

def generate_retiro_code():
    length = random.choice([6, 10])
    if random.random() <= 0.15:
        valid_code = ''.join(random.choices('0123456789', k=length - 2))
        return "12" + valid_code if length == 6 else valid_code + "99"
    else:
        return ''.join(random.choices('12345678992383817357', k=length))

def GCR():
    names = ["Daniel", "Julián", "Emiliano", "Juan", "Pedro", "Jose", "Antonio", "Francisco", "Luis", "Manuel", "Javier", "Carlos", "Sergio", "Raúl", "Emilio", "Brandon", "Ana", "Sofía", "Laura", "María", "Elizabeth", "Samira", "Rocio", "Gabriel", "Fernando", "Verónica", "Isabella", "Diego", "Roberto", "Valentina", "Fabián", "Lucía", "Andrés", "Carolina", "Martina", "Gonzalo", "Camila", "Tomás", "Victoria", "Matías", "Alejandra", "Maximiliano", "Valeria", "Eduardo", "Julia", "Nicolás", "Mariana", "Rafael", "Catalina", "Leandro", "Adriana", "Sebastián", "Daniela", "Facundo", "Margarita", "Lorenzo", "Abril", "Felipe", "Solange", "Benjamín", "Renata", "Pedro", "Constanza", "Ángel", "Antonia", "Gabriela", "Hugo", "René", "Paloma", "Rodrigo", "Elena", "Federico", "Juliana", "Ignacio", "Paula", "Martín", "Beatriz", "Matilde", "Francisca", "Esteban", "René", "Rosa", "Alberto", "Silvia", "Leonardo", "Natalia", "Bruno", "Valentín", "Juliana", "Gisela", "Fernando", "Cecilia", "Agustín", "Marina"]
    surnames = ["Giménez", "Fernández", "García", "López", "Martínez", "Pérez", "Sánchez", "Suárez", "Torres", "Díaz", "Gómez", "Vázquez", "Castro", "Morales", "Jiménez", "Ruiz", "Ramírez", "Herrera", "Medina", "Ortega", "Delgado", "Hernández", "Álvarez", "Navarro", "Moreno", "Guerrero", "Cabrera", "Vidal", "Mendoza", "Ponce", "Salazar", "Aguilar", "Rojas", "Sepúlveda", "Quintero", "Contreras", "Vega", "Escobar", "Soto", "Valenzuela", "Espinoza", "Muñoz", "Figueroa", "Chávez", "Rivas", "Suarez", "Montoya", "Fuentes", "Cruz", "Flores", "Martínez", "Gómez", "Franco", "Pérez", "León", "Reyes", "Vargas", "Rosales", "Campos", "Ibarra", "Guerrero"]

    name = f"{random.choice(names)} {random.choice(surnames)}"
    retiro_code = generate_retiro_code()
    
    crinf = f'Código de Retiro: {retiro_code} | Nombre: {name}'
    return crinf

def GCRs(num_codes):
    codes = []
    for _ in range(num_codes):
        crinf = GCR()
        codes.append(crinf)
    return codes

def WCTF(codes, filename):
    clines = sum(1 for _ in open(filename))

    with open(filename, 'a') as file:
        for i, acc_info in enumerate(codes, start=1):
            file.write(acc_info + "\n")
            if i == len(codes):
                print(f"- Nuevo código generado exitosamente. | Archivo: {filename} - Línea: {clines + i} \n\n")
            else:
                print(f"- Nuevo código generado exitosamente. | Archivo: {filename} - Línea: {clines + i} \n")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    filename = input("Introduce el nombre del archivo ->> ")
    if not filename.endswith(".txt"):
        print("Error: Solo se permiten archivos .txt.")
        return

    try:
        num_codes = int(input("Número de códigos de retiro a generar ->> "))
        print("")
    except ValueError:
        print("Error: Introduce un número válido.")
        return
    
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write("")

    codes = GCRs(num_codes)
    WCTF(codes, filename)

if __name__ == "__main__":
    main()
