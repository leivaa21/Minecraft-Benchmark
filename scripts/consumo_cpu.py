import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    x = []
    y1 = []
    y2 = []
    
    filenameY1 = "txts/node_cpu_seconds_total_0.txt"
    filenameY2 = "txts/node_cpu_seconds_total_1.txt"

    with open(filenameY1) as f:
        linesY1 = f.readlines()

    with open(filenameY2) as f:
        linesY2 = f.readlines()

    for i in range(0,15*60, 15):
        x.append(i)
    x.pop()

    index = 0
    lineaAnterior = 0
    for line in linesY1:
        vectorLinea = line.split(' @')
        if index == 0:
            y1.append(0)
        else:
            y1.append((15 - (float(vectorLinea[0]) - lineaAnterior))*100/15)
        index += 1
        lineaAnterior = float(vectorLinea[0])

    index = 0
    for line in linesY2:
        vectorLinea = line.split(' @')
        if index == 0:
            y2.append(0)
        else:
            y2.append((15 - (float(vectorLinea[0]) - lineaAnterior))*100/15)
        index += 1
        lineaAnterior = float(vectorLinea[0])

    plt.plot(x, y1, c="red", alpha=0.5, label="Core 1")
    plt.plot(x, y2, c="blue", alpha=0.5, label="Core 2")
    plt.legend()

    plt.title("Consumo de CPU", fontsize=16)
    plt.xlabel("Tiempo del experimento (s)", fontsize=16)
    plt.ylabel("CPU utilizada (%)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    # Muestra la gráfica
    plt.show()

main()