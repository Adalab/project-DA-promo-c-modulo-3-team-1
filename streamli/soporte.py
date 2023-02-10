import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pickle
from datetime import date, datetime
import calendar
import holidays


def prediccion_cnt(prediccion):

    df_usuario = pd.DataFrame(prediccion,index =[0])

    df_usuario_numericas = df_usuario[['atemp','hum','windspeed']]
    
    # cargar estandarizacion

    with open('../borrador/11_robust_cnt.pkl','rb') as f:
        robust = pickle.load(f)
    
    df_usuario_estan = pd.DataFrame(robust.transform(df_usuario_numericas),columns = df_usuario_numericas.columns)

    # encoding

    mapa_season = {'invierno':0, 'primavera':1, 'otoño':1, 'verano':2} 
    mapa_holiday = {'festivo':0, 'no festivo':2} 
    mapa_weekday = {7:1, 1:0, 2:0, 3:0, 4:2, 5:1, 6:1}
    mapa_weather = {3:0, 2:1, 1:2}
    mapa_mes = {1:0, 2:0, 3:1, 4:2, 5:3, 6:3, 7:3, 8:3, 9:3, 10:3, 11:2, 12:1}

    df_usuario['season']= df_usuario['season'].map(mapa_season)
    df_usuario['holiday']= df_usuario['holiday'].map(mapa_holiday)
    df_usuario['weekday']= df_usuario['weekday'].map(mapa_weekday)
    df_usuario['weathersit']= df_usuario['weathersit'].map(mapa_weather)
    df_usuario['mnth']= df_usuario['mnth'].map(mapa_mes)
    
    with open('../datos/cnt/12-cnt-random.pkl','rb') as f:
        bosque = pickle.load(f)

    return bosque.predict(df_usuario), df_usuario 

def prediccion_casual(prediccion):

    df_usuario = pd.DataFrame(prediccion,index =[0])

    df_usuario_numericas = df_usuario[['atemp','hum','windspeed']]
    
    # cargar estandarizacion

    with open('../datos/casual/15_robust_casual.pkl','rb') as f:
        robust = pickle.load(f)
    
    df_usuario_estan = pd.DataFrame(robust.transform(df_usuario_numericas),columns = df_usuario_numericas.columns)

    # encoding

    mapa_season = {'invierno':0, 'otoño':1, 'primavera':2, 'verano':3} 
    mapa_holiday = {'festivo':0, 'no festivo':2} 
    mapa_weekday = { 1:3, 2:1, 3:0, 4:0, 5:0, 6:0, 7:2}
    mapa_weather = {3:0, 2:1, 1:2}
    mapa_mes = {1:0, 2:0, 3:1, 4:2, 5:3, 6:3, 7:3, 8:3, 9:3, 10:2, 11:1, 12:0}

    df_usuario['season']= df_usuario['season'].map(mapa_season)
    df_usuario['holiday']= df_usuario['holiday'].map(mapa_holiday)
    df_usuario['weekday']= df_usuario['weekday'].map(mapa_weekday)
    df_usuario['weathersit']= df_usuario['weathersit'].map(mapa_weather)
    df_usuario['mnth']= df_usuario['mnth'].map(mapa_mes)
    
    with open('../datos/casual/16_random_casual.pkl','rb') as f:
        bosque = pickle.load(f)

    return bosque.predict(df_usuario), df_usuario 

def prediccion_registered(prediccion):

    df_usuario = pd.DataFrame(prediccion,index =[0])

    df_usuario_numericas = df_usuario[['atemp','hum','windspeed']]
    
    # cargar estandarizacion

    with open('../datos/registrados/06_robust_registered.pkl','rb') as f:
        robust = pickle.load(f)
    
    df_usuario_estan = pd.DataFrame(robust.transform(df_usuario_numericas),columns = df_usuario_numericas.columns)

    # encoding

    mapa_season = {'invierno':0, 'primavera':1, 'otoño':1, 'verano':2} 
    mapa_holiday = {'festivo':0, 'no festivo':1} 
    mapa_weekday = {7:0, 1:0, 2:1, 3:2, 4:3, 5:3, 6:3}
    mapa_weather = {3: 0, 2:1, 1:2}
    mapa_mes = {1: 0, 2:0, 3:1, 4:1, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:1, 12:1}

    df_usuario['season']= df_usuario['season'].map(mapa_season)
    df_usuario['holiday']= df_usuario['holiday'].map(mapa_holiday)
    df_usuario['weekday']= df_usuario['weekday'].map(mapa_weekday)
    df_usuario['weathersit']= df_usuario['weathersit'].map(mapa_weather)
    df_usuario['mnth']= df_usuario['mnth'].map(mapa_mes)
    
    with open('../datos/registrados/07_random_casual.pkl','rb') as f:
        bosque = pickle.load(f)

    return bosque.predict(df_usuario), df_usuario 

#Funcion para redefinir las estaciones de acuerdo a fecha
def get_season(fecha):

  '''Función para categorizar las estaciones del año según la fecha
    Parámetros: año, fecha y estaciones
    Return: estación '''
    

  Y= fecha.year
  estaciones = [('invierno', date(Y,  1,  1),  date(Y,  3, 20)),
                ('primavera', date(Y,  3, 21),  date(Y,  6, 20)),
                ('verano', date(Y,  6, 21),  date(Y,  9, 22)),
                ('otoño', date(Y,  9, 23),  date(Y, 12, 20)),
                ('invierno', date(Y, 12, 21),  date(Y, 12, 31))]

  for estacion, inicio, fin in estaciones:
      if inicio <= fecha <= fin:
        return estacion        


#Festivos USA
us_festivos= holidays.US()

#Funcion para verificar segun fecha si es festivo o laboral
def detectar_feriados(fecha):
    
        '''Función para extraer si es feriado o laboral segun la fecha
          Parámetros: fecha y diccionario de festivos
          Return: si esta en el diccionario return = festivo sino return =laboral '''

        if fecha in us_festivos:
            return 'festivo'
        else:
            return 'no festivo'

def dia_semana(col):
    return col.isoweekday()
