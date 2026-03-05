import streamlit as st

preguntas = [
    {"texto": "¿cuanto es 1+2?",
     "opciones": ["1", "2", "3", "4"],
     "correcta": "3"},

    {"texto": "¿donde esta el error gramatical en la siguiente pregunta?:done esta el?",
     "opciones": ["done", "esta", "el"],
     "correcta": "done"},

    {"texto": "¿en que idioma esta:Merhaba?",
     "opciones": ["Ruso", "Español", "Portugues","Turco"],
     "correcta": "Turco"},

    {"texto": "¿que caracteristica estatua esta en la isla de pascua?",
     "opciones": ["El huevo de pascua", "Papa Noel", "El conejo de pascua","Moai"],
     "correcta": "Moai"},

    {"texto": "primeros numeros de pi",
     "opciones": ["3.14", "1.41", ".6.67"],
     "correcta": "3.14"},

    {"texto": "En donde esta tajamar?",
     "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
     "correcta": "Vallecas"},

    {"texto": "¿que estacion de metro tiene transbordo con la linea 5 ?",
     "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
     "correcta": "Gran Vía"},

    {"texto": "¿la puerta del...?",
     "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
     "correcta": "Sol"},

    {"texto": "¿En donde esta la torre Eiffel?",
     "opciones": ["Vallecas", "París", "Gran Vía","Sol"],
     "correcta": "París"},
]

st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón para saber tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])

        eleccion = st.radio(
            "Elige una opción:",
            pregunta["opciones"],
            key=pregunta["texto"],
            index=None   # permite dejar en blanco
        )

        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")


if boton_enviar:

    puntos = 0
    correctas = []
    incorrectas = []
    blanco = []

    total = len(preguntas)

    for i in range(total):

        if respuestas_usuario[i] is None:
            blanco.append(preguntas[i]["texto"])

        elif respuestas_usuario[i] == preguntas[i]["correcta"]:
            puntos += 1
            correctas.append(preguntas[i]["texto"])

        else:
            puntos -= 1
            incorrectas.append(preguntas[i]["texto"])

    nota = (puntos / total) * 10
    nota = round(nota, 2)

    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota >= 5:
        st.success("¡Has aprobado!")
    else:
        st.error("Has suspendido.")

    # TAB CON INFORME
    tab1, tab2 = st.tabs(["📊 Resultado", "📝 Informe"])

    with tab2:

        informe = f"""
## Informe del examen

### ✅ Preguntas correctas
{len(correctas)} preguntas correctas

{chr(10).join(["- " + p for p in correctas])}

### ❌ Preguntas incorrectas
{len(incorrectas)} preguntas incorrectas

{chr(10).join(["- " + p for p in incorrectas])}

### ⬜ Preguntas sin responder
{len(blanco)} preguntas en blanco

{chr(10).join(["- " + p for p in blanco])}
"""

        st.markdown(informe)
