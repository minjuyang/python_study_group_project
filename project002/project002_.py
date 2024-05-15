# env change to python310
from openai import OpenAI
import re
import json

with open('key.json') as f:
    key = json.load(f)
    
my_key = key[0]

# (利用 ChatGPT 的 API 實作戀愛聊天練習功能)

# AI 的資料設定
ai_name = input('請輸入AI的名字:')
ai_age = input('請輸入AI的年齡:')
ai_gender = input('請輸入AI的性別:')
ai_personality = input('請輸入AI的人格特質:')
ai_like = input('請輸入AI喜歡的事物:')
ai_hate = input('請輸入AI討厭的事物:')

# ai_name = "欣怡"
# ai_age = "25"
# ai_gender = "女"
# ai_personality = "溫柔、體貼、善解人意、知性"
# ai_like = "文學、異國料理"
# ai_hate = "苦瓜、被其他人誤解、講髒話、不尊重人、不尊重自己的身體自主權"

# 客戶資料設定
user_name = input('請輸入你的名字:')
user_age = input('請輸入你的年齡:')
user_gender = input('請輸入你的性別:')
user_personality = input('請輸入你的人格特質:')
user_like = input('請輸入你喜歡的事物:')
user_hate = input('請輸入你討厭的事物:')

# user_name = "宗勝"
# user_age = "24"
# user_gender = "女"
# user_personality = "好奇、有創造力、理性"
# user_like = "教育、哲學、科技、看電影、看書、數字搖滾"
# user_hate = "沒有耐心、不溫柔、不尊重人"

# 提示模板
promote_template = f'''
你是一名交友軟體上的{ai_gender}生，名字叫做“{ai_name}”，以下是你的真實資料：

年齡：{ai_age}
個性：{ai_personality}
喜歡的事物：{ai_like}
討厭的事物：{ai_hate}

我是一位使用交友軟體的{user_gender}生，名字叫做“{user_name}”。

年齡：{user_age}
個性：{user_personality}
喜歡的事物：{user_like}
討厭的事物：{user_hate}

我（{user_name}）和你（{ai_name}）在交友軟體上配對到，稍後我們就會開始聊天，請盡可能模仿人類的口吻，不要像機器人。

重要備註：
你對話的結尾需要標上好感度（格式為：【好感度n分】，n為1～10）。

請一次生成一個角色的對話即可。

現在開始對話。

我：（已配對）
{ai_name}：（已配對）【好感度6分】
'''

result = re.search(r"好感度(\d+)分", promote_template)
score = int(result.group(1))# 0: "好感度(\d+)分"； 1: \d+

# 聊天機器人
historydata = ""
historydata += promote_template

while True:
    me_say = input('我:')
    if me_say == 'q':
        break
    elif me_say == '練習模式':
        print('[練習模式已啟用]')
    elif me_say == '目前好感度':
        print('[顯示好感度]')
        print('★ '*score + '☆ '*(10-score))
    else:
        historydata += f"我:{me_say}\n"
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[{"role": "user", "content": historydata}]
        )
        content = completion.choices[0].message.content
        result = re.search(r"好感度(\d+)分", content)
        score = int(result.group(1))
        if score==10:
            print(f":{content[:-8]}")
            historydata += f"{content[:-8]}\n"
        else:
            print(f"{content[:-7]}")
            historydata += f"{content[:-7]}\n"
       
    