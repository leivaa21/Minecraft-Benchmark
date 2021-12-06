import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    x = []
    y = []
    
    filenameX = "txts/yardstick_packets_in.txt"
    filenameY = "txts/yardstick_packets_out.txt"

    with open(filenameX) as f:
        linesX = f.readlines()

    with open(filenameY) as f:
        linesY = f.readlines()
    
    for line in linesX:
        vectorLinea = line.split(' @')
        x.append(float(vectorLinea[0]))

    for line in linesY:
        vectorLinea = line.split(' @')
        y.append(float(vectorLinea[0]))

    plt.plot(x, y, linewidth=3)

    # Título general y de los ejes
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title("XY", fontsize=24)
    plt.xlabel("X", fontsize=14)
    plt.ylabel("Y", fontsize=14)

    # Etiquetado de los valores de los ejes
    plt.tick_params(axis="both", labelsize=14)

    # Muestra la gráfica
    plt.show()

main()