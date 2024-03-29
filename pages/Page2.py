import streamlit as st

st.title('ประกาศเริ่มต้นฤดูร้อน ปี พ.ศ. 2567')
st.image('https://www.tmd.go.th/media/climate/seasonal_announce/info_summer_2024n.jpg')
st.write('''
                ประเทศไทยได้สิ้นสุดฤดูหนาวและเข้าสู่ฤดูร้อนแล้ว ในวันที่ 21 กุมภาพันธ์ พ.ศ.2567 โดยในตอนกลางวันบริเวณประเทศไทยมีอากาศร้อนเกือบทั่วไปต่อเนื่อง อุณหภูมิสูงสุดมากกว่า 35 องศาเซลเซียส เนื่องจากได้รับอิทธิพลจากรังสีดวงอาทิตย์เพิ่มมากขึ้น ประกอบกับมีลมฝ่ายใต้พัดปกคลุมบริเวณประเทศไทยตอนบน ซึ่งเป็นรูปแบบลักษณะอากาศของฤดูร้อน อย่างไรก็ตามบริเวณภาคเหนือและภาคตะวันออกเฉียงเหนือจะยังคงมีอากาศเย็นในตอนเช้าจนถึงประมาณกลางเดือนมีนาคม และคาดว่า ฤดูร้อน จะสิ้นสุดประมาณกลางเดือนพฤษภาคม พ.ศ. 2567
                ''')

page_bg_img = '''
<style>
body {
background-image: url("https://images.pexels.com/photos/55787/pexels-photo-55787.jpeg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

