# Description: Simulación de la máquina de Galton
#importar librerias
import matplotlib.pyplot as plt
import random
#simulacion de maquina de galton 
def simular_canicas(num_canicas, num_niveles):
    #inicializar los contenedores, creando en la lista de resultados
    resultados = [0] * (num_niveles + 1)
    #simular el movimiento de las canicas
    for i in range(num_canicas):
        #inicializar la posicion de la canica
        posicion = 0
        #simular el movimiento de la canica
        for i in range(num_niveles):
            #generar un numero aleatorio
            if random.random() < 0.6:
                #mover la canica a la izquierda
                posicion += 1
        #incrementar el contador del cont
        resultados[posicion] += 1
    #retornar los resultados
    return resultados
#graficar los resultados
def graficar_histograma(resultados):
    #crear una lista con los niveles
    niveles = list(range(len(resultados)))
    plt.bar(niveles, resultados, color='blue')
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    #mostrar la grafica
    plt.grid(True)
    plt.show()
#funcion principal
def main():
    num_canicas = 3000
    num_niveles = 12
    #simular la maquina de galton
    resultados = simular_canicas(num_canicas, num_niveles)
    graficar_histograma(resultados)

if __name__ == "__main__":
    main()