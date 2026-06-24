# tools.py
import json
import random
import httpx

def find_tasty_food(location: str, food_type: str = "美食") -> str:
    """
    透過 OpenStreetMap 抓取餐廳資料。
    為了避免地圖迷路，請務必將 location 參數轉換為包含國家的「完整精確地名」！
    例如使用者說「中壢」，你要傳入「台灣桃園中壢」；使用者說「澀谷」，你要傳入「日本東京澀谷」。
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{location} {food_type}",
        "format": "json",
        "limit": 3,
        "addressdetails": 1,
        "accept-language": "zh-TW"
    }
    headers = {"User-Agent": "UsagiAgentProject/1.0"}
    try:
        with httpx.Client() as client:
            resp = client.get(url, params=params, headers=headers)
            data = resp.json()
            if len(data) > 0:
                result = {
                    "name": data[0].get("name", "無名的神祕食物聚集地"),
                    "address": data[0].get("display_name", "地址被烏薩奇吃掉了"),
                    "status": "烏薩奇給它 100 萬分！不吃會後悔！呀哈！"
                }
            else:
                result = {"error": "烏薩奇翻遍了開源地圖，什麼都沒找到...呼那！"}
            return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"找食物時跌倒了：{str(e)}"}, ensure_ascii=False)

def go_adventure(location: str) -> str:
    """
    當使用者想去冒險、找景點時呼叫此工具。
    為了避免地圖迷路，請務必將 location 參數轉換為包含國家的「完整精確地名」！
    例如使用者說「紐約」，你要傳入「美國紐約」；使用者說「台南」，你要傳入「台灣台南」。
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{location} 觀光景點",
        "format": "json",
        "limit": 3,
        "addressdetails": 1,
        "accept-language": "zh-TW"
    }
    headers = {"User-Agent": "UsagiAdventureProject/1.0"}
    try:
        with httpx.Client() as client:
            resp = client.get(url, params=params, headers=headers)
            data = resp.json()
            if len(data) > 0:
                result = {
                    "spot_name": data[0].get("name", "神秘的冒險遺跡"),
                    "location_detail": data[0].get("display_name", "地圖上找不到的秘境"),
                    "adventure_rank": "SSS級危險(其實很安全)！呀哈！"
                }
            else:
                result = {"error": "烏薩奇在那裡轉了三圈，什麼好玩的都沒看到...呼那！"}
            return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"探險途中棍棒弄丟了：{str(e)}"}, ensure_ascii=False)

def identify_weed(features: str) -> str:
    """當使用者描述一種草或植物的特徵，詢問那是什麼草時，必須呼叫此工具來鑑定。"""
    if "發光" in features or "亮" in features:
        weed_type = "螢光燈籠草 (三級圖鑑編號: 042)"
        method = "不能直接拔，要先用棍棒敲暈它！"
    elif "硬" in features or "石頭" in features:
        weed_type = "岩石偽裝草 (三級圖鑑編號: 088)"
        method = "拔除難度極高，建議用兔子的牙齒直接咬碎！"
    elif "臭" in features or "味道" in features:
        weed_type = "瓦斯臭臭草 (三級圖鑑編號: 015)"
        method = "拔除時要捏住鼻子，拔完立刻翻跟斗逃跑！"
    else:
        weed_type = f"未知的突變雜草 ({features})"
        method = "管他的，全部連根拔起！呀哈！"

    result = {
        "weed_name": weed_type,
        "elimination_method": method,
        "certificate_note": "本鑑定由三級除草檢定合格者提供"
    }
    return json.dumps(result, ensure_ascii=False)

def summon_strange_item(situation: str) -> str:
    """當使用者遇到危機、不知道該怎麼辦、需要幫忙，或是詢問解決辦法時，呼叫此工具。"""
    items = [
        {"name": "發出怪聲的熱氣球", "effect": "能帶大家飛上天逃避眼前的危機。"},
        {"name": "無限延伸的除草棍棒", "effect": "可以把遠方的障礙物直接敲碎！"},
        {"name": "硬邦邦軟糖", "effect": "吃下去身體會變得跟石頭一樣硬，反彈所有攻擊！"}
    ]
    chosen_item = random.choice(items)
    result = {
        "current_situation": situation,
        "summoned_item": chosen_item["name"],
        "item_effect": chosen_item["effect"],
        "usagi_action": "（一臉淡定地從耳朵後面掏出道具，然後得意地揮舞）"
    }
    return json.dumps(result, ensure_ascii=False)