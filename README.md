가상환경 생성

cd SoGong/chatbot

python -m venv venv


가상환경 활성화

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate


필수 패키지 설치

pip install fastapi uvicorn


서버 실행

uvicorn main:app --reload
