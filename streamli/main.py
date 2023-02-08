import streamlit as st
import datetime
import soporte as sp
import time
import pandas as pd
import numpy as np

st.title(":green[RANDOM LOVE] :heart:")

st.markdown("# ¿Eres un apasionado del ciclismo y quieres saber cuántas bicicletas se alquilaron en una fecha determinada?")
st.markdown("## Si la respuesta es que sí ¡Este es tu sitio!")

st.markdown("### Antes de empezar necesitaremos saber qué grupo de ciclistas quieres predecir")


option = st.selectbox(
    '¿A cuál quieres predecir?',
    ("Elige una opción",'Casuales', 'Registrados', 'Totales'))

if option == "Casuales":
    st.write('Has seleccionado el grupo de ciclista', option, "🚴‍♀️")
    st.image("fotos/ciclista2.png")
elif option == "Registrados":
    st.write('Has seleccionado el grupo de ciclista', option, "🚴‍♀️")
    st.image("fotos/ciclista1.png")
elif option == "Totales":
    st.write('Has seleccionado el grupo de ciclista', option, "🚴‍♀️🚴‍♀️")
    st.image("fotos/ciclista3.png")

st.markdown("### Por último necesitaremos saber que fecha exacta es la que quieres predecir.")


d = st.date_input(
    "¿Qué fecha quieres predecir el alquiler de bicis?",
    datetime.date(2018, 1, 1), key = "Pon una fecha")

if d == datetime.date(2018,1,1):
    pass
else:


    st.write('La fecha que quieres predecir es:', d)

    col1, col2 = st.columns(2)

    with col1:
        estacion= sp.get_season(d)
        st.write("En esa fecha se encontraban en:")
        if estacion == "invierno":
            atemp = 14
            hum = 54
            windspeed = 13
            weathersit = 2
            st.image("fotos/invierno.png")
        elif estacion == "verano":
            atemp = 32
            hum = 63
            windspeed = 11
            weathersit = 1
            st.image("fotos/verano.png")
        elif estacion == "primavera":
            atemp = 26
            hum = 64
            windspeed = 13
            weathersit = 1
            st.image("fotos/primavera.png")
        elif estacion == "otoño":
            atemp = 20
            hum = 66
            windspeed = 11
            weathersit = 2
            st.image("fotos/otoño.png")

    with col2:
        festivos = sp.detectar_feriados(d)
        st.write("Ese día era:")
        if festivos == "festivo":
            st.image("fotos/festivo.png")
        elif festivos == "no festivo":
            st.image("fotos/nofestivo.png")

    dia_semana = sp.dia_semana(d)



    diccionario = {'atemp':atemp, 'hum':hum, 'windspeed':windspeed,'season':estacion,'yr':d.year,'mnth':d.month,'holiday':festivos,'weekday':dia_semana,'weathersit':weathersit}

    time.sleep(2)
    if option == "Casuales":
        prediccion = sp.prediccion_casual(diccionario)
        st.write("La predicción para el grupo de casuales con un 76% de fiabilidad es:")
        st.markdown(round(prediccion[0][0],0))
    elif option == "Registrados":
        prediccion = sp.prediccion_registered(diccionario)
        st.write("La predicción para el grupo de registrados con un 85% de fiabilidad es:")
        st.markdown(round(prediccion[0][0],0))
    elif option == "Totales":
        prediccion = sp.prediccion_cnt(diccionario)
        st.write("La predicción para el grupo de casuales con un 88% de fiabilidad es:")
        st.markdown(round(prediccion[0][0],0))
    
    st.write("Estas serían las bicicletas que necesitaremos para alquilar :smile:")
    st.markdown("Happy Coding :smile:")


    st.balloons()


