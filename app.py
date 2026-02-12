import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas: 
preguntas = [
    {
        "texto": "¿cuanto es 1+2?",
        "opciones": ["1", "2", "3", "4"],
        "correcta": "3"
    },
    {
        "texto": "¿donde esta el error gramatical en la siguiente pregunta?:done esta el?",
        "opciones": ["done", "esta", "el"],
        "correcta": "done"
    },
    {
        "texto": "¿en que idioma esta:Merhaba?",
        "opciones": ["Ruso", "Español", "Portugues","Turco"],
        "correcta": "Turco"
    },
    {
        "texto": "¿que caracteristica estatua esta en la isla de pascua?",
        "opciones": ["El huevo de pascua", "Papa Noel", "El conejo de pascua","Moai"],
        "correcta": "Moai"
    },
    {
        "texto": "primeros numeros de pi",
        "opciones": ["3.14", "1.41", ".6.67",],
        "correcta": "3.14"
    },
     {
        "texto": "En donde esta tajamar?",
        "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
        "correcta": "Vallecas"
    },
     {
        "texto": "¿que estacion de metro tiene transbordo con la linea 5 ?",
        "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
        "correcta": "Gran Vía"
    },
     {
        "texto": "¿la puerta del...?",
        "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
        "correcta": "Sol"
    },
     {
        "texto": "¿En donde esta la torre Eiffel?",
        "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
        "correcta": "París"
    },
]

# Configuración visual de la página
st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
    
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1

    # Calculamos la nota sobre 10
    nota = (aciertos / total) * 10
    nota_redondeada = round(nota)

    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota_redondeada} / 10")

    if nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    else:
        st.error(f"Has sacado un {aciertos}. ¡Toca estudiar un poco más!")
