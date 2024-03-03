import streamlit as st
from pages import Page1

page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/1367192/pexels-photo-1367192.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.subheader('สภาพอากาศ ณ วันนี้')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "35 °C", "2 °F")
col2.metric("Wind", "11 km/h ", "+3%")
col3.metric("Humidity", "50%", "4%")

number = st.number_input("ใส่อุณหภูมิ", value=None, placeholder="พิมพ์เลขที่นี่...")

unit_options = ["°C", "°F", "°K"]
selected_unit = st.selectbox("เลือกหน่วย:", options=unit_options)

if number is not None:
    if selected_unit == "°C":
        temp = number * 9%5 + 32
        st.write("อุณหภูมิคือ", temp, "°F")
    if selected_unit == "°K":
        temp = 9/5 * (number - 273) + 32
        st.write("อุณหภูมิคือ", round(temp), "°F")
    if selected_unit == "°F":
        temp = 5/9 * (number - 32)
        st.write("อุณหภูมิคือ", round(temp), "°C")



