import pandas as pd

data_frame = pd.read_csv("edades.csv", delimiter=",") 

def analisis_estadisticos(data_frame):
    try:
        # Frecuencia absoluta acumulada - clave 'Fi'
        data_frame["Fi"]= data_frame['fi'].cumsum()
        
        # Frecuencia relativa simple - clave 'ri'
        data_frame["ri"]= data_frame["fi"] / data_frame["fi"].sum()
        
        # Frecuencia relativa acumulada - clave 'Ri'
        data_frame["Ri"]= data_frame['ri'].cumsum()
        
        # Frecuencia porcentual simple - clave 'pi%'
        data_frame['pi%']= data_frame["ri"] * 100
        
        # Frecuencia porcentual acumulada - clave 'Pi%'.
        data_frame['Pi%']= data_frame['Ri'] * 100
        
        # Crea el diccionario de salida con las claves y valores calculados
        estadisticas = {
            'Fi': data_frame['Fi'].tolist(),
            'ri': data_frame["ri"].tolist(),
            'Ri': data_frame['Ri'].tolist(),
            'pi': data_frame['pi%'].tolist(),
            'Pi': data_frame['Pi%'].tolist()
        }
        return estadisticas
    
    except Exception as e:
        print("Error:", e)
        return None
    
resolve = analisis_estadisticos(data_frame)
print(resolve)

# for key, value in resolve.items():
#         print(f"{key}:{value}")
