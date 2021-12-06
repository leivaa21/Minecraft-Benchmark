import matplotlib.pyplot as plt
        
from datetime import datetime

def main():
    x = []
    freeMemo = []
    cacheMemo = []
    bufferMemo = []
    memoriaTotal = 4127272960
    memoria = []
    
    filename1 = "txts/node_memory_MemFree_bytes.txt"
    filename2 = "txts/node_memory_Cached_bytes.txt"
    filename3 = "txts/node_memory_Buffers_bytes.txt"

    with open(filename1) as f:
        lines1 = f.readlines()

    with open(filename2) as f:
        lines2 = f.readlines()

    with open(filename3) as f:
        lines3 = f.readlines()

    for i in range(0,15*60, 15):
        x.append(i)
    x.pop()

    lineaAnterior = 0
    for line in lines1:
        vectorLinea = line.split(' @')
        if len(freeMemo) == 0:
            freeMemo.append(0)
        else:
            freeMemo.append(int(vectorLinea[0]))

    for line in lines2:
        vectorLinea = line.split(' @')
        if len(cacheMemo) == 0:
            cacheMemo.append(0)
        else:
            cacheMemo.append(int(vectorLinea[0]))

    for line in lines3:
        vectorLinea = line.split(' @')
        if len(bufferMemo) == 0:
            bufferMemo.append(0)
        else:
            bufferMemo.append(int(vectorLinea[0]))

    for i in range (0,59):
        memoria.append(freeMemo[i] + cacheMemo[i] + bufferMemo[i])
        if i == 0:
            memoria[i] = 24
        else:
            memoria[i] = ((memoriaTotal - memoria[i])/memoriaTotal)*100

    plt.plot(x, memoria, c="red", alpha=0.5)
    #plt.legend()

    plt.title("Consumo de memoria (RAM)", fontsize=16)
    plt.xlabel("Tiempo del experimento (s)", fontsize=16)
    plt.ylabel("RAM utilizada (%)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    # Muestra la gráfica
    plt.show()

main()