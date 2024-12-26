import pygame
import sys

# Constants
VX = 3  # 水平速度
GRAVITY = 1  # 重力加速度
SIZE = 20  # 球的直徑
REDUCE = 0.9  # 彈跳時速度的減少比例
START_X = 30  # 球的初始x座標
START_Y = 40  # 球的初始y座標
SCREEN_WIDTH = 800  # 畫面寬度
SCREEN_HEIGHT = 500  # 畫面高度
DELAY = 10  # 動畫延遲，毫秒

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bouncing Ball')

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    # 初始球的位置與速度
    ball_x = START_X
    ball_y = START_Y
    ball_vy = 0
    bounce_count = 0  # 彈跳次數計數
    out_of_bounds_count = 0  # 球超出右邊界的次數
    ball_active = False  # 球是否啟動

    # 主循環
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 如果球未超出右邊界三次，允許啟動球
                if not ball_active and out_of_bounds_count < 3:
                    ball_active = True

        # 更新球的位置與速度
        if ball_active:
            ball_x += VX
            ball_vy += GRAVITY
            ball_y += ball_vy

            # 檢查球是否碰到地板
            if ball_y + SIZE > SCREEN_HEIGHT:
                ball_y = SCREEN_HEIGHT - SIZE
                ball_vy = -ball_vy * REDUCE
                bounce_count += 1

            # 如果超出右邊界，重置球的位置，增加超出次數
            if ball_x > SCREEN_WIDTH:
                ball_x = START_X
                ball_y = START_Y
                ball_vy = 0
                ball_active = False
                bounce_count = 0
                out_of_bounds_count += 1

        # 繪製畫面
        screen.fill(WHITE)  # 清空畫面
        pygame.draw.ellipse(screen, BLACK, (ball_x, ball_y, SIZE, SIZE))  # 畫球
        pygame.display.flip()  # 更新畫面
        clock.tick(1000 // DELAY)  # 控制動畫速度

        # 顯示警告訊息當球無法再啟動
        if out_of_bounds_count >= 3:
            print("球已超出右邊視窗三次，無法再啟動！")
            break

if __name__ == "__main__":
    main()


# from campy.graphics.gobjects import GOval
# from campy.graphics.gwindow import GWindow
# from campy.gui.events.timer import pause
# from campy.gui.events.mouse import onmouseclicked

# # Constants
# VX = 3  # 水平速度
# DELAY = 10  # 動畫間隔 (毫秒)
# GRAVITY = 1  # 重力加速度
# SIZE = 20  # 球的直徑
# REDUCE = 0.9  # 彈跳減速比例
# START_X = 30  # 起始 x 座標
# START_Y = 40  # 起始 y 座標

# # Global variables
# window = GWindow(800, 500, title='bouncing_ball.py')  # 建立視窗
# ball = GOval(SIZE, SIZE)  # 建立球物件
# ball.filled = True
# window.add(ball, START_X, START_Y)
# is_running = False  # 球是否在運動
# out_of_bounds_count = 0  # 球超出視窗右邊界的次數


# def main():
#     """
#     This program simulates a bouncing ball at (START_X, START_Y)
#     that has VX as x velocity and 0 as y velocity. Each bounce reduces
#     y velocity to REDUCE of itself.
#     """
#     onmouseclicked(start_bouncing)


# def start_bouncing(_):
#     global is_running, out_of_bounds_count
#     if not is_running:
#         is_running = True
#         y_velocity = 0  # 垂直速度初始化為 0
#         while True:
#             if is_running:
#                 # 更新球的位置
#                 ball.move(VX, y_velocity)
#                 y_velocity += GRAVITY  # 垂直速度受重力加速度影響

#                 # 檢查與地板碰撞
#                 if ball.y + SIZE >= window.height:
#                     y_velocity = -y_velocity * REDUCE

#                 # 檢查超出右邊界
#                 if ball.x > window.width:
#                     out_of_bounds_count += 1
#                     reset_ball()
#                     if out_of_bounds_count >= 3:
#                         break

#                 pause(DELAY)

#         is_running = False  # 停止運動


# def reset_ball():
#     """
#     將球重置到初始位置，並檢查是否需要完全停止。
#     """
#     global is_running
#     is_running = False
#     ball.x = START_X
#     ball.y = START_Y


# if __name__ == "__main__":
#     main()
