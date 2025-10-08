import tkinter as tk
import math
import random
import time

# 預設選項
options = []

colors = ["#FF9999", "#FFCC99", "#FFFF99", "#99FF99", "#99CCFF", "#CC99FF"]

root = tk.Tk()
root.title("幸運轉盤")

canvas_size = 400
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

center = canvas_size // 2
radius = 150

# 畫轉盤
def draw_wheel(angle_offset=0):
    canvas.delete("all")
    if not options:  # 沒有輸入選項時顯示提示
        canvas.create_text(center, center, text="請先輸入選項", font=("Arial", 16))
        return
    
    slice_angle = 360 / len(options)
    
    for i, option in enumerate(options):
        start_angle = i * slice_angle + angle_offset
        canvas.create_arc(center-radius, center-radius, center+radius, center+radius,
                          start=start_angle, extent=slice_angle, fill=colors[i % len(colors)], outline="black")
        # 文字
        text_angle = math.radians(start_angle + slice_angle/2)
        x = center + (radius/1.5) * math.cos(text_angle)
        y = center - (radius/1.5) * math.sin(text_angle)
        canvas.create_text(x, y, text=option, font=("Arial", 12, "bold"))

    # 畫箭頭
    canvas.create_polygon(center-10, center-radius-20, center+10, center-radius-20,
                          center, center-radius, fill="red")

# 動畫旋轉
def spin_wheel():
    if not options:
        result_label.config(text="⚠️ 請先輸入選項！")
        return
    
    total_spins = random.randint(30, 50)  # 總共要轉多少次
    angle = 0
    for i in range(total_spins):
        angle += 15 + i*0.5   # 每次轉動的角度 (逐漸變慢)
        draw_wheel(angle)
        root.update()
        time.sleep(0.05 + i*0.01)

    # 計算最終結果
    slice_angle = 360 / len(options)
    final_angle = angle % 360
    index = int(((360 - final_angle + slice_angle/2) % 360) // slice_angle)
    result = options[index]
    result_label.config(text=f"🎉 結果：{result}")

# 讀取輸入
def set_options():
    global options
    user_input = entry.get().strip()
    if user_input:
        options = [item.strip() for item in user_input.split(",") if item.strip()]
        draw_wheel()

# 輸入框
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

set_button = tk.Button(root, text="設定選項", font=("Arial", 14), command=set_options)
set_button.pack(pady=5)

button = tk.Button(root, text="開始轉盤", font=("Arial", 16), command=spin_wheel)
button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=10)

draw_wheel()  # 初始畫面

root.mainloop()
