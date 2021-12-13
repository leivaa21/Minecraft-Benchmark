import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    x = []
    y1 = []
    y2 = []
    y4 = []
    y5 = []
    y3 = []
    
    filenameY1 = "txts/node_cpu_seconds_total_0.txt"
    filenameY2 = "txts/node_cpu_seconds_total_1.txt"
    filenameY4 = "txts/node_cpu_seconds_total_2.txt"
    filenameY5 = "txts/node_cpu_seconds_total_3.txt"

    filenameY3 = "txts/yardstick_bot_connected.txt"


    with open(filenameY1) as f:
        linesY1 = f.readlines()

    with open(filenameY2) as f:
        linesY2 = f.readlines()

    with open(filenameY4) as f:
        linesY4 = f.readlines()

    with open(filenameY5) as f:
        linesY5 = f.readlines()


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

    index = 0
    lineaAnterior = 0
    for line in linesY4:
        vectorLinea = line.split(' @')
        if index == 0:
            y4.append(0)
        else:
            y4.append((15 - (float(vectorLinea[0]) - lineaAnterior))*100/15)
        index += 1
        lineaAnterior = float(vectorLinea[0])

    index = 0
    for line in linesY5:
        vectorLinea = line.split(' @')
        if index == 0:
            y5.append(0)
        else:
            y5.append((15 - (float(vectorLinea[0]) - lineaAnterior))*100/15)
        index += 1
        lineaAnterior = float(vectorLinea[0])


    index = 0
    for line in linesY3:
        vectorLinea = line.split(' @')
        if index == 0:
            y3.append(0)
        else:
            y3.append(float(vectorLinea[0]))
        index += 1
        lineaAnterior = float(vectorLinea[0])

    plt.plot(x, y1, c="red", alpha=0.5, label="Core 1")
    plt.plot(x, y2, c="blue", alpha=0.5, label="Core 2")
    plt.plot(x, y4, c="yellow", alpha=0.5, label="Core 3")
    plt.plot(x, y5, c="green", alpha=0.5, label="Core 4")
    plt.plot(x, y3, c="orange", alpha=0.5, label="Núm bots")
    plt.legend()
    plt.annotate("50", (748, 52))
    plt.plot(750, 50, marker="o", markersize=5, markeredgecolor="orange", markerfacecolor="orange")

    plt.title("Consumo de CPU", fontsize=16)
    plt.xlabel("Tiempo del experimento (s)", fontsize=16)
    plt.ylabel("CPU utilizada (%)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    # Muestra la gráfica
    plt.show()

main()