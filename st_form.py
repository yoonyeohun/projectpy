import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
st.header('1. `with` 표기법 사용 예시')
st.subheader('일기장')

with st.form('my_form'):
    st.subheader('**일기 쓰기**')

    # 입력 위젯
    coffee_bean_val = st.selectbox('요일', ['월요일', '화요일', '수요일', '목요일', '금요일'])
    coffee_roast_val = st.selectbox('날씨', ['맑음', '흐림', '바람', '비', '구름'])
    brewing_val = st.selectbox('온도', ['더움', '추움', '따듯', '시원', ])
    serving_type_val = st.selectbox('기분', ['기쁨', '슬픔', ])
   
    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        📝 작성하신 내용:
        - 요일: `{coffee_bean_val}`
        - 날씨: `{coffee_roast_val}`
        - 온도: `{brewing_val}`
        - 기분: `{serving_type_val}`
        
        ''')
else:
    st.write('☝️ 작성하세요!')


# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.
st.write('선택된 값: ', selected_val)





