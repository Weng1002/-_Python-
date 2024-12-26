import pygame
import random
import sys

# Constants
WINDOW_WIDTH = 500  # 視窗寬度
WINDOW_HEIGHT = 800  # 視窗高度
DELAY = 10  # 每幀延遲（毫秒）
SIZE = 30  # 磚塊邊長
MIN_Y_SPEED = 2  # y方向最小速度
MAX_Y_SPEED = 5  # y方向最大速度
MAX_MISSES = 3  # 最大失誤次數

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Bricks")

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BRICK_COLOR = (0, 128, 255)

def main():
    # 初始化變數
    brick_x = random.randint(0, WINDOW_WIDTH - SIZE)  # 磚塊初始x位置
    brick_y = 0  # 磚塊初始y位置
    brick_speed = random.randint(MIN_Y_SPEED, MAX_Y_SPEED)  # 隨機速度
    misses = 0  # 漏接次數
    running = True  # 遊戲是否進行中
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 檢查滑鼠是否點擊磚塊
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (brick_x <= mouse_x <= brick_x + SIZE) and (brick_y <= mouse_y <= brick_y + SIZE):
                    # 點擊成功，移除磚塊並重置
                    brick_x = random.randint(0, WINDOW_WIDTH - SIZE)
                    brick_y = 0
                    brick_speed = random.randint(MIN_Y_SPEED, MAX_Y_SPEED)

        # 更新磚塊位置
        brick_y += brick_speed

        # 如果磚塊掉出視窗底部
        if brick_y > WINDOW_HEIGHT:
            misses += 1
            if misses >= MAX_MISSES:
                running = False  # 結束遊戲
                break
            # 重置磚塊
            brick_x = random.randint(0, WINDOW_WIDTH - SIZE)
            brick_y = 0
            brick_speed = random.randint(MIN_Y_SPEED, MAX_Y_SPEED)

        # 繪製畫面
        screen.fill(WHITE)  # 清空畫布
        pygame.draw.rect(screen, BRICK_COLOR, (brick_x, brick_y, SIZE, SIZE))  # 畫磚塊

        # 繪製漏接次數
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Misses: {misses}", True, RED)
        screen.blit(text, (10, 10))

        pygame.display.flip()  # 更新畫面
        clock.tick(1000 // DELAY)  # 控制更新速度

    # 結束遊戲畫面
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over!", True, BLACK)
    screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)  # 顯示結束畫面2秒
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
