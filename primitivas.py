def calcularSueldo():
    nombreEstudiante = input("digite el nombre del empleado: ")
    salario = int(input("digite el salario: "))
    devengados = int(input("digite los devengados: "))
    deducciones = int(input("digite las deducciones: "))
    sueldototal = salario + devengados - deducciones
    print(f"el nombre del estudiante es: {nombreEstudiante} y su salario es:  {sueldototal} ")

def main():
    calcularSueldo()



if __name__ == "__main__":
    main()
