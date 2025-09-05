import matplotlib.pyplot as plt
from load_file import LoadFile
from longest_word import LongestWord

if __name__ == "__main__":
    
    load_file = LoadFile()
    contenido = load_file.load_words()

    lg = LongestWord()

    tiempos = []
    tiempos.append(lg.method_1(contenido))
    tiempos.append(lg.method_2(contenido))
    tiempos.append(lg.method_3(contenido))
    tiempos.append(lg.method_4(contenido))
    tiempos.append(lg.method_5(contenido))
    # Etiquetas para cada método
    etiquetas = ["method_1", "method_2", "method_3", "method_4", "method_5"]

    # Graficar
    plt.bar(etiquetas, tiempos, color="skyblue")
    plt.xlabel("Método")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempos de ejecución")
    plt.show()

    mejor_idx = tiempos.index(min(tiempos))
    print(f" El método más rápido es {etiquetas[mejor_idx]} con {tiempos[mejor_idx]} segundos")
