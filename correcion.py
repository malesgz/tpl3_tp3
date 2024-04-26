import matplotlib.pyplot as plt
import pandas as pd

def analisis_estadisticos(data_frame):
    try:
        df = pd.DataFrame(data_frame, columns = ['edad', 'fi'])

        # Frecuencia acomulada.
        df['Fi'] = df['fi'].cumsum()

        # Frecuencia relativa simple.
        df['ri'] = df['fi'] / df['fi'].sum()

        # Frecuencia relativa acumulada.
        df['Ri'] = df['ri'].cumsum()

        # Frecuencia porcentual simple.
        df['pi%'] = df['ri'] * 100

        # Frecuencia porcentual acumulada.
        df['Pi%'] = df['Ri'] * 100

        print(df)
        df.to_csv('edad.csv' , index=False)

        plt.plot(df["edad"], df["fi"])
        plt.xlabel("Edad")
        plt.ylabel("Alumnos")
        plt.title("Prueba de ejercicio con Matplotlib")
        plt.show()

    except Exception as e:
        print("Error", e)
        return None
    
data_frame = [
    [18,5],
    [19,7],
    [20,1],
    [21,4],
    [22,10],
    [23,1],
    [24,6],
    [25,2],
    [26,9],
    [27,3],
    [28,11],
    [29,8],
    [30,13],
]

analisis_estadisticos(data_frame)