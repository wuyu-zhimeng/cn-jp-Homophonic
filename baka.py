import requests,re
from bs4 import BeautifulSoup
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES, TkinterDnD

def drop(event):
    global content
    # 获取拖入的文件路径
    file_path = event.data
    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            content = f.read()
            text_area.delete(1.0, tk.END)  # 清空文本区域
            text_area.insert(tk.END, content)  # 显示文件内容
    except Exception as e:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"错误: {str(e)}")
    return(content)

# 创建主窗口
root = TkinterDnD.Tk()
root.title("中文转日语空耳")

lab = tk.Label(root, text="请‘拖入’文本")
lab.pack()

# 创建文本区域
text_area = tk.Text(root, wrap=tk.WORD, height=20, width=40)
text_area.pack(padx=10, pady=10)

# 注册拖放功能
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)


def callback():
    post(content)
 
button = tk.Button(root, text="按钮", command=callback)
button.pack()


def post(content):
    cookies = {
        '_ga': 'GA1.1.1135822188.1727975398',
    }

    headers = {
        'Referer': 'https://www.ltool.net/chinese-simplified-and-traditional-characters-pinyin-to-katakana-converter-in-simplified-chinese.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    data = {
        'contents': content,
        'firstinput': 'OK',
        'option': '1',
        'optionext': 'zenkaku',
    }

    res = requests.post(
        'https://www.ltool.net/chinese-simplified-and-traditional-characters-pinyin-to-katakana-converter-in-simplified-chinese.php',
        headers=headers,
        data=data
        )
    soup = BeautifulSoup(res.text, 'html.parser')

    yiwen1 = soup.select("div[class='finalresult']")[0].text.strip()

    yiwen2 = yiwen1.replace(" ","")

    yiwen3 = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", yiwen2)

    with open('译本.txt', 'a',encoding='UTF-8') as f:

        f.write(yiwen3 + '\n')

# 运行应用
root.mainloop()