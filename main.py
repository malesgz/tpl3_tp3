# import pandas as pd

# data_frame = pd.read_csv("edades.csv", delimiter=",") 

# def analisis_estadisticos(data_frame):
#     try:
#         data_frame["Fi"]= data_frame['fi'].cumsum()
#         data_frame["ri"]= data_frame["fi"] / data_frame["fi"].sum()
#         data_frame["Ri"]= data_frame['ri'].cumsum()
#         data_frame['pi%']= data_frame["ri"] * 100
#         data_frame['Pi%']= data_frame['Ri'] * 100
#         print (data_frame)
#     except Exception as e:
#         print ("Error:", e)

# analisis_estadisticos(data_frame)
# data_frame.to_clipboard(index=False, decimal=',')

# import pandas as pd

# def analisis_estadisticos(data_frame):
#     try:
#         # Calcula las frecuencias absolutas y las asigna a la clave 'fi'
#         fi = data_frame['fi']
        
#         # Calcula las frecuencias acumuladas y las asigna a la clave 'Fi'
#         Fi = data_frame['fi'].cumsum()
        
#         # Calcula las frecuencias relativas y las asigna a la clave 'ri'
#         ri = (data_frame['fi'] / data_frame['fi'].sum())
        
#         # Calcula las frecuencias relativas acumuladas y las asigna a la clave 'Ri'
#         Ri = (data_frame['fi'].cumsum() / data_frame['fi'].sum())
        
#         # Calcula las probabilidades y las asigna a la clave 'pi'
#         pi = (ri * 100)
        
#         # Calcula las probabilidades acumuladas y las asigna a la clave 'Pi'
#         Pi = (Ri * 100)
        
#         # Imprime las estadísticas de manera organizada
#         print("Frecuencias absolutas (fi):\n", fi)
#         print("Frecuencias acumuladas (Fi):\n", Fi)
#         print("Frecuencias relativas (ri):\n", ri)
#         print("Frecuencias relativas acumuladas (Ri):\n", Ri)
#         print("Probabilidades (pi):\n", pi)
#         print("Probabilidades acumuladas (Pi):\n", Pi)
        
#         # Crea el diccionario de salida con las claves y valores calculados
#         estadisticas = {
#             'fi': fi.tolist(),
#             'Fi': Fi.tolist(),
#             'ri': ri.tolist(),
#             'Ri': Ri.tolist(),
#             'pi': pi.tolist(),
#             'Pi': Pi.tolist()
#         }
        
#         return estadisticas
    
#     except Exception as e:
#         print("Error:", e)
#         return None

# # Ejemplo de uso
# data_frame = pd.read_csv("edades.csv", delimiter=",")
# resultado = analisis_estadisticos(data_frame)
# print(resultado)

import pandas as pd

def analisis_estadistico(data_frame):
    try:
        #  calcula la frecuencias acumulas
        data_frame["Fi"] = data_frame["fi"].cumsum()

        # calcula la frecuencias relativas
        data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
      
        # calcula la frecuencias relaativaws acumuladas
        data_frame["Ri"] = data_frame['ri'].cumsum()
        
        # calcula la probabilidades en porcentaje
        data_frame["pi%"] = data_frame["ri"] * 100
        
        # calcula la probabilidades de acumuladas en porcentaje
        data_frame["Pi%"] = data_frame["Ri"] * 100
        
        estadistica = {
            'fi': data_frame['fi'].tolist(),
            'Fi': data_frame['Fi'].tolist(),
            'ri': data_frame['ri'].tolist(),
            'Ri': data_frame['Ri'].tolist(),
            'pi%': data_frame['pi%'].tolist(),
            'Pi%': data_frame['Ri'].tolist()

        }

        return estadistica
       
    except Exception as e:

        print(f"Error: la columna '{e.args[0]}' no existe en el data_frame")
        return None

data_frame = pd.read_csv("edad.csv", delimiter=";")
   
resultado = analisis_estadistico(data_frame)

if resultado is not None:
    print("Resultado:" )
    for key, value in resultado.items():
        print(f"{key}:{value}")
   
else:
    print("No funciona")