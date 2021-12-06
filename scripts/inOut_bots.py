import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    x = []
    y1 = []
    y2 = []
    y3 = []
    
    filenameY1 = "txts/yardstick_packets_in.txt"
    filenameY2 = "txts/yardstick_packets_out.txt"
    
    filenameY3 = "txts/yardstick_bot_connected.txt"


    with open(filenameY1) as f:
        linesY1 = f.readlines()

    with open(filenameY2) as f:
        linesY2 = f.readlines()

    with open(filenameY3) as f:
        linesY3 = f.readlines()

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
            y1.append(float(vectorLinea[0])/1000 - lineaAnterior)
        index += 1
        lineaAnterior = float(vectorLinea[0])/1000

    index = 0
    for line in linesY2:
        vectorLinea = line.split(' @')
        if index == 0:
            y2.append(0)
        else:
            y2.append(float(vectorLinea[0])/1000 - lineaAnterior)
        index += 1
        lineaAnterior = float(vectorLinea[0])/1000

    index = 0
    for line in linesY3:
        vectorLinea = line.split(' @')
        if index == 0:
            y3.append(0)
        else:
            y3.append(float(vectorLinea[0]))
        index += 1
        lineaAnterior = float(vectorLinea[0])

    plt.plot(x, y1, c="red", alpha=0.5, label="Paquetes entrada")
    plt.plot(x, y2, c="blue", alpha=0.5, label="Paquetes salida")
    plt.plot(x, y3, c="orange", alpha=0.5, label="Núm bots")
    plt.legend()
    plt.annotate("50", (748, 52))
    plt.plot(750, 50, marker="o", markersize=5, markeredgecolor="orange", markerfacecolor="orange")

    plt.title("Paquetes de entrada/salida del servidor MC", fontsize=16)
    plt.xlabel("Tiempo del experimento (s)", fontsize=16)
    plt.ylabel("Paquetes (miles)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    # Muestra la gráfica
    plt.show()

main()