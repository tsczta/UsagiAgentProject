# frontend.py (升級版：加入烏薩奇背景圖)
import streamlit as st
import requests
import base64  


def get_base64_of_bin_file(bin_file):
    """讀取本地圖片檔案並轉換為 base64 字串"""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    """將 base64 圖片設定為 Streamlit 網頁背景"""
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/jpeg;base64,%s");
        background-size: cover;
        background-position: right bottom;  
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* 為了讓對話泡泡清楚，對話區域加一點點白色半透明背景 */
    [data-testid="stChatMessageContainer"] {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    
    /* 讓底部的輸入框清楚 */
    .stChatInputContainer {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    ''' % bin_str
    
    # 注入 CSS
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 呼叫函數，載入圖片（確保 background.jpg 與此檔案在同資料夾）
try:
    set_png_as_page_bg('background.jpg')
except FileNotFoundError:
    st.error("烏拉！找不到圖片！請確認 background.jpg 是否放在專案資料夾中！呼那！")

# --- 原本的聊天室邏輯區 ---

st.title("烏薩奇的全能助理 (GaaS 測試前端)")

# 1. 建立記憶區
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 畫出過去的對話
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 3. 使用者輸入框
user_input = st.chat_input("呀哈！想問烏薩奇什麼？")

if user_input:
    # 先顯示使用者訊息
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 4. 呼叫後端 API
    with st.spinner("烏薩奇狂奔思考中..."):
        try:
            # 呼叫你的 FastAPI 後端
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_input}
            )
            
            if response.status_code == 200:
                usagi_reply = response.json()["answer"]
            else:
                usagi_reply = f"烏拉！連線失敗：{response.status_code}"
                
        except Exception as e:
            usagi_reply = "呼那！找不到後端伺服器，你是不是忘記開 FastAPI 了？"

    # 顯示烏薩奇回覆
    with st.chat_message("assistant"):
        st.markdown(usagi_reply)
    st.session_state.messages.append({"role": "assistant", "content": usagi_reply})