import streamlit as st
import datetime
import soporte as sp

st.markdown("# ¿Eres un apasionado del ciclismo y quieres saber cuántas bicicletas se alquilaron en una fecha determinada?")
st.markdown("## Si la respuesta es que sí ¡Este es tu sitio!")

st.markdown("### Antes de empezar necesitaremos saber qué grupo de ciclistas quieres predecir")


option = st.selectbox(
    '¿A cuál quieres predecir?',
    ("Elige una opción",'Casuales', 'Registrados', 'Totales'))

if option == "Casuales":
    st.write('Has seleccionado el grupo de ciclista', option, ":smile:")
    st.image("fotos/ciclista1.jpg")
elif option == "Registrados":
    st.write('Has seleccionado el grupo de ciclista', option, ":smile:")
    st.image("fotos/ciclista2.jpg")
elif option == "Totales":
    st.write('Has seleccionado el grupo de ciclista', option, ":smile:")
    st.image("fotos/ciclista3.jpg")

st.markdown("### Por último necesitaremos saber que fecha exacta es la que quieres predecir.")


d = st.date_input(
    "¿Qué fecha quieres predecir el alquiler de bicis?",
    datetime.date(2018, 1, 1))


st.write('La fecha que quieres predecir es:', d)

col1, col2 = st.columns(2)

with col1:
    estacion= sp.get_season(d)
    st.write("En esa fecha se encontraban en la estación de:", estacion)
    if estacion == "invierno":
        st.image("fotos/invierno.jpg")
    elif estacion == "verano":
        st.image("fotos/verano.jpg")
    elif estacion == "primavera":
        st.image("fotos/primavera.jpg")
    elif estacion == "otoño":
        st.image("fotos/otoño.jpg")

with col2:
    festivos = sp.detectar_feriados(d)
    st.write("Ese día era:",festivos)
    if festivos == "festivo":
        st.image("fotos/festivo.jpg")
    elif festivos == "no festivo":
        st.image("fotos/nofestivo.jpg")

dia_semana = sp.dia_semana(d)


diccionario = {'atemp':15.7, 'hum':78, 'windspeed':10.9,'season':estacion,'yr':d.year,'mnth':d.month,'holiday':festivos,'weekday':dia_semana,'weathersit':1}

if option == "Casuales":
    prediccion = sp.prediccion_casual(diccionario)
    st.write("La predicción para el grupo de casuales con un 76% de fiabilidad es:")
    st.write(prediccion[0])
elif option == "Registrados":
    prediccion = sp.prediccion_registered(diccionario)
    st.write("La predicción para el grupo de registrados con un 85% de fiabilidad es:")
    st.write(prediccion[0])
elif option == "Totales":
    prediccion = sp.prediccion_cnt(diccionario)
    st.write("La predicción para el grupo de casuales con un 88% de fiabilidad es:")
    st.write(prediccion[0])
    
st.markdown("# Estas serán las bicicletas alquiladas :smile:")
st.markdown("Happy Coding :smile:")




