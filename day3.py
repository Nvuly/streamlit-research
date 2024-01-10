### 필요한 라이브러리 임폴트
import streamlit as st

### 제목 설정
st.header("st.button")

### 실행 코드
if st.button("Say Hello"):
    st.write("안녕하세요")
else:
    st.write("Goodbye")