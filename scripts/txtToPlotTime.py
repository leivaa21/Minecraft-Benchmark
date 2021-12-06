import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    valores = []
    tiempos = [0]
    indexTiempos = 0
    filename = "txts/memstat_alloc_bytes_total.txt"

    with open(filename) as f:
        lines = f.readlines()
    
    
    for line in lines:
        vectorLinea = line.split(' @')
        valores.append(float(vectorLinea[0]))
        tiempos.append(tiempos[indexTiempos] + 15)
        indexTiempos = indexTiempos + 1

    tiempos.pop()
    plt.plot(tiempos, valores, linewidth=3)

    # Título general y de los ejes
    plt.title("Prueba", fontsize=24)
    plt.xlabel("Segundos", fontsize=14)
    plt.ylabel("Valor", fontsize=14)

    # Etiquetado de los valores de los ejes
    plt.tick_params(axis="both", labelsize=14)

    # Muestra la gráfica
    plt.show()

main()