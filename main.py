import streamlit as st

@st.cache_data
def load_data(value):

    import google.generativeai as genai
    API_KEY = 'AIzaSyDN8avHb3uwrEhIOtPj7PhkXlpUNeAdsh8'
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    q1 = value
    q2 = 'План диеты'
    q3 = 'План тренировок'
    r1 = chat.send_message(q1)
    r2 = chat.send_message(q2)
    r3 = chat.send_message(q3)
    return [r1.text, r2.text, r3.text]

st.header("Рекомендации AI для набора массы")

height = st.number_input("Рост (см)", value=170)
weight = st.number_input("Вес (кг)", value=60)
gender = st.selectbox("Пол", ['Мужчина', 'Женщина'])

btn = st.button("Отправить")
if btn:
    query = f"Как можно похудеть или набрать массуы при весе {weight} кг и при росте {height} см {gender}"

    r1, r2, r3 = load_data(query)
    if r:
        st.write(r1)
        st.write(r2)
        st.write(r3)
