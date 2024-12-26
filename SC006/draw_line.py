from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# 常數設定
SIZE = 10  # 圓的半徑
window = GWindow()
first_click = None  # 紀錄第一次點擊的位置
circle = None  # 紀錄空心圓的物件

def main():
    """
    這個程式會根據使用者的點擊，交替顯示空心圓與直線。
    第一次點擊時會畫出空心圓，第二次點擊時空心圓消失，並畫出一條從第一次點擊
    到第二次點擊的直線，並依此規律重複。
    """
    onmouseclicked(handle_click)

def handle_click(event):
    global first_click, circle

    if first_click is None: # 如果是第一次點擊
        first_click = (event.x, event.y) #ㄐ紀錄第一次點擊的位置
        circle = GOval(SIZE * 2, SIZE * 2, x=event.x - SIZE, y=event.y - SIZE)  # 畫出空心圓
        circle.filled = False # 設定空心圓
        window.add(circle)

    else: # 第二次點擊
        if circle is not None: # 移除空心圓
            window.remove(circle)
        
        line = GLine(first_click[0], first_click[1], event.x, event.y) # 畫出從第一次點擊到第二次點擊的直線
        window.add(line)
        
        first_click = None  # 重置第一次點擊的紀錄

if __name__ == "__main__":
    main()
