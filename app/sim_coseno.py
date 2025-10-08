import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt

def calcular_similitud_coseno(matriz_bow, doc = None, ver_grafico = True):

    # Convertir a matriz
    X = np.array(matriz_bow)

    # calcula la matriz de similitud
    similitud = cosine_similarity(X)

    #comprobar que se pasa nombre de documento
    if doc is None:
        doc = [f'doc[{i+1}' for i in range (len(X))]

    # dataframe de similitudes
    df_sim = pd.DataFrame(similitud, index=doc, columns = doc)

    # mostrar el resultado en gráfico de calor
    if ver_grafico:
        plt.figure(figsize=(10, 8))
        sns.set_theme(style="white")

        # Crear el heatmap sin anotaciones primero (mejor renderizado)
        ax = sns.heatmap(
            df_sim,
            cmap="coolwarm",
            cbar_kws={'label': 'Similitud del coseno'},
            linewidths=0.3,
            square=True
        )

        # Añadir anotaciones manualmente en cada celda
        for i in range(df_sim.shape[0]):
            for j in range(df_sim.shape[1]):
                ax.text(
                    j + 0.5,
                    i + 0.5,
                    f"{df_sim.iloc[i, j]:.2f}",
                    ha="center", va="center",
                    color="black", fontsize=8
                )

        plt.title("Matriz de Similitud del Coseno entre Documentos",
                  fontsize=13, weight='bold', pad=15)
        plt.xticks(rotation=45, ha='right', fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel("Documentos", fontsize=10, weight='bold')
        plt.ylabel("Documentos", fontsize=10, weight='bold')
        plt.tight_layout()
        plt.show()

    return df_sim
