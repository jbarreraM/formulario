#Este es un programa para ingresar datos personales
from datetime import datetime
import pandas as pd
datos_persona = ["Nombre", "Apellido", "Edad", "Dirección", "Fecha Nacimiento", "Email", "Fono"]
fechas = ['2018-10-20', ' 1970-03-04' ]
alumnos = [' Pepe' , ' Sandra']
df = pd.DataFrame ({'imprimiendo año ': pd.to_datetime(fechas)},index=alumnos)
df['año '] = df['imprimiendo año '].dt.year
print(df)
respuesta_datos_persona = ["","",0,"", "","",""]
suma_edad_y_ano = 0
ano_fecha_nacimiento = 0
i = 0
while(i < 7):
    print(f"Por favor, ingresa tú {datos_persona[i]}" )
    respuesta_datos_persona[i] = input()
    print(f"Tu {datos_persona[i]} es {respuesta_datos_persona[i]}" )
    i = i + 1



