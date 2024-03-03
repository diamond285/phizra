import streamlit as st

@st.cache_data
def load_data(value):

    import google.generativeai as genai
    API_KEY = 'AIzaSyDN8avHb3uwrEhIOtPj7PhkXlpUNeAdsh8'
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    q1 = value
    r1 = chat.send_message(q1)
    return r1.text

st.header("Рекомендации AI для набора массы")

height = st.number_input("Рост (см)", value=170)
weight = st.number_input("Вес (кг)", value=60)
age = st.number_input("Возраст", value=20)
gender = st.selectbox("Пол", ['Мужчина', 'Женщина'])

btn = st.button("Отправить")
if gender == "Мужчина":
    if age < 16:
        gender = "Мальчику"
    else:
        gender = "Мужчине"
if gender == "Женщина":
    if age < 16:
        gender = "Девочке"
    else:
        gender = "Женщине"
if btn:
    query = f"Напиши у меня лишний вес или недостаток веса при весе {weight} кг и при росте {height} см {gender} {age} лет"

    r1 = load_data(query)
    if r1:
        st.write(r1)
    r2 = load_data(r1 + f"\nСоздай план тренировок {gender} {age} лет")
    if r2:
        st.write(r2)
    r3 = load_data(r1 + f"\nСоздай план питания {gender} {age} лет")
    if r3:
        st.write(r3)

