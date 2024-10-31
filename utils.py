from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.
print(openai_api_key)

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.