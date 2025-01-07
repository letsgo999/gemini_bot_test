import streamlit as st
import requests

# 제미나이 AI API 키와 엔드포인트를 설정합니다.
API_URL = "https://api.google.com/gemini/v1/response"  # 제미나이 AI의 실제 엔드포인트를 사용해야 합니다.
API_KEY = "AIzaSyCwi2EAO8cxF8sfODw4gAgbUTi-GvHZK0c"  # 제미나이 AI API 키를 입력하세요.

# Streamlit UI 설정
st.title("Gemini AI Chatbot")
st.write("제미나이 AI와 대화해 보세요!")

# 사용자 입력 받기
user_input = st.text_input("Your message:", placeholder="Type your message here...")

# 버튼을 눌렀을 때 동작
if st.button("Send"):
    if user_input.strip():
        try:
            # 제미나이 AI API 호출
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"query": user_input}
            )
            
            if response.status_code == 200:
                ai_response = response.json().get("response", "No response from Gemini AI.")
                st.write("**Gemini AI's response:**")
                st.write(ai_response)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message.")

# 하단에 주석 추가
st.markdown("---")
st.caption("Powered by Streamlit and Gemini AI")
