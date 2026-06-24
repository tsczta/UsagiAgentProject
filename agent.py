# agent.py
import os
import google.generativeai as genai
from persona import USAGI_PROMPT
from tools import find_tasty_food, go_adventure, identify_weed, summon_strange_item

def get_usagi_chat():
    """初始化大腦，裝備人設與四種工具，並回傳一個準備好的聊天物件"""
    
    # 初始化模型 
    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction=USAGI_PROMPT,
        tools=[find_tasty_food, go_adventure, identify_weed, summon_strange_item],
        generation_config={"temperature": 1.3} 
    )
    
    # 啟動自動呼叫工具功能
    chat = model.start_chat(enable_automatic_function_calling=True)
    return chat