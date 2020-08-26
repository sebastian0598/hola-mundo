def devengado(sal):
    alimentacion = (sal * 1)/100
    transporte = (sal * 1.2)/100
    viaticos = int(input("digite el valor de los viaticos: "))
    totalDev =  alimentacion + transporte + viaticos
    return (totalDev)

def deducciones(sal):
    salud = (sal * 4)/100
    pensiones = (sal * 3.375)/100
    totalDed = salud + pensiones
    return (totalDed)

def leerEmpleado():
    nombreEmpleado = input("digite el nombre del empleado: ")
    salario = float(input("digite el salario del empleado: "))
    dev = devengado(salario)
    ded = deducciones(salario)
    totalPagar = salario + dev - ded 
    print (f"{nombreEmpleado} y su total a pagar es: {totalPagar}")
    #calcularTotalPagar(nombreEmpleado, salario, devengado, deducciones)




def main():
    leerEmpleado()



if __name__ == "__main__":
    main()