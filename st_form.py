import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
st.header('1. `with` 표기법 사용 예시')
st.subheader('커피 머신')

with st.form('my_form'):
    st.subheader('**커피 주문하기**')

    # 입력 위젯
    coffee_bean_val = st.selectbox('커피콩', ['아라비카', '로부스타'])
    coffee_roast_val = st.selectbox('커피 로스팅', ['라이트', '미디엄', '다크'])
    brewing_val = st.selectbox('추출 방법', ['에어로프레스', '드립', '프렌치 프레스', '모카 포트', '사이폰'])
    serving_type_val = st.selectbox('서빙 형식', ['핫', '아이스', '프라페'])
    milk_val = st.select_slider('우유 정도', ['없음', '낮음', '중간', '높음'])
    owncup_val = st.checkbox('자신의 컵 가져오기')

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        ☕ 주문하신 내용:
        - 커피콩: `{coffee_bean_val}`
        - 커피 로스팅: `{coffee_roast_val}`
        - 추출 방법: `{brewing_val}`
        - 서빙 형식: `{serving_type_val}`
        - 우유: `{milk_val}`
        - 자신의 컵 가져오기: `{owncup_val}`
        ''')
else:
    st.write('☝️ 주문하세요!')


# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.
st.write('선택된 값: ', selected_val)





st.header('3. `간단한 일기 쓰기')
st.subheader('일기장')

with st.form('my_form'):
    st.subheader('**오늘 하루는?**')

    # 입력 위젯
    today_weekday_val = st.selectbox('요일', ['월요일', '화요일', '수요일', '목요일', '금요일'])
    today_weather_val = st.selectbox('날씨', ['맑음', '흐림', '비', '눈', '바람'])
    today_emotion_val = st.selectbox('감정', ['기쁨', '슬픔', '보통',])
   

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        📝 오늘의 일기:
        - 요일: `{today_weekday_val}`
        - 날씨: `{today_weather_val}`
        - 감정: `{today_emotion_val}`
        
        ''')
else:
    st.write('작성하세요📝')