# main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# 匯入烏薩奇大腦
from agent import get_usagi_chat

# 1. 系統初始化與金鑰設定
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("請先在 .env 檔案中設定 GOOGLE_API_KEY！")

genai.configure(api_key=GOOGLE_API_KEY)

# 2. 建立 API 伺服器
app = FastAPI(title="Usagi Agent API")

# 3. 定義請求格式
class ChatRequest(BaseModel):
    message: str

# 4. 建立通訊端點
@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        # 每次呼叫都取得一個全新的烏薩奇大腦
        chat = get_usagi_chat()
        
        # 傳送訊息
        response = chat.send_message(request.message)
        
        return {
            "persona": "Usagi",
            "user_message": request.message,
            "answer": response.text,
            "status": "success"
        }
    except Exception as e:
        return {
            "persona": "Usagi",
            "user_message": request.message,
            "answer": f"烏拉！伺服器大腦當機啦！錯誤代碼：{str(e)}",
            "status": "error"
        }