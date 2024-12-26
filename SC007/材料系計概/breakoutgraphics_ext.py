from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 30  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics_ext:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=window_width / 2 - paddle_width / 2,
                            y=window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.set_paddle()
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True
        self._dx = 0
        self._dy = 0
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)
        self.b = ball_radius
        
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'lime', 'brown']
        self.bricks = []
        self.generate_bricks(brick_rows, brick_cols)
        # Initialize our mouse listeners
        onmouseclicked(self.set_speed)
        
        # ----------------------------------------------------------------------------------------------
        # Ext: 分數
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'lime', 'brown']
        self.color_to_score = {
            'red': 50,
            'orange': 40,
            'yellow': 30,
            'green': 20,
            'blue': 10,
            'purple': 60,
            'pink': 70,
            'cyan': 80,
            'lime': 90,
            'brown': 100
        }
        # ----------------------------------------------------------------------------------------------

        self.brick_count = 0
        # Draw bricks
        self.brick = GRect(width=brick_width, height=brick_height)
        for j in range(brick_rows):  # 每行
            row_colors = self.colors.copy()
            random.shuffle(row_colors)  # 隨機排序顏色
            for i in range(brick_cols):  # 每列
                brick = GRect(
                    width=brick_width,
                    height=brick_height,
                    x=i * brick_width + i * brick_spacing,
                    y=j * brick_height + j * brick_spacing
                )
                color = row_colors[i % len(row_colors)]  # 循環取顏色
                brick.fill_color = color
                brick.color = color
                brick.color_name = color  # 自定義屬性記錄顏色名稱
                brick.filled = True
                self.window.add(brick)
                self.brick_count += 1
                
        self.obj = None
        
        # 生命值
        self.lives_label = GLabel('Lives: ')
        self.lives_label.font = '-20'
        self.window.add(self.lives_label, x=5, y=self.window.height - 5)
        
        # ----------------------------------------------------------------------------------------------
        # Ext: 分數
        self.score = 0
        self.score_label = GLabel('Score: 0')
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=self.window.width - 100, y=self.window.height - 5)
        # ----------------------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------------------
        # 困難模式按鈕
        self.original_radius = ball_radius  # 保存初始半徑
        self.original_dx = INITIAL_Y_SPEED / 2  # 初始水平速度
        self.original_dy = INITIAL_Y_SPEED  # 初始垂直速度
        
        # 隱形模式按鈕
        self.invisible_mode_button = GLabel('隱形模式')
        self.invisible_mode_button.font = '-20'
        self.invisible_mode_button.x = 165  # 左上角的 x 位置
        self.invisible_mode_button.y = 400  # 左上角的 y 位置
        self.window.add(self.invisible_mode_button)
        
        # 加速模式按鈕
        self.speed_mode_button = GLabel('加速模式')
        self.speed_mode_button.font = '-20'
        self.speed_mode_button.x = 165  # x 位置與隱形模式對齊
        self.speed_mode_button.y = 450  # 隱形模式按鈕下方
        self.window.add(self.speed_mode_button)
        
        self.is_invisible_mode_button = False  # 標記是否啟用困難模式
        self.is_speed_mode = False  # 用於標記加速模式是否啟用
        
        onmouseclicked(self.handle_hard_mode)
        # ----------------------------------------------------------------------------------------------


    def set_speed(self, event):
        if self._dx == 0 and self._dy == 0:
            self._dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self._dx = -self._dx
            self._dy = INITIAL_Y_SPEED
        if abs(self._dx) < 2:  # 最小水平速度為 2
            self._dx = 2 if self._dx > 0 else -2

    def get_ball_radius(self):
        return self.b

    def remove(self):
        self.window.remove(self.obj)

    def move_ball(self):
        self.ball.move(self._dx, self._dy)

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def set_paddle(self):
        onmousemoved(self.handle_move)

    def handle_move(self, event):
        new_x = event.x - self.paddle.width / 2
        if new_x < 0:
            new_x = 0
        elif new_x > self.window.width - self.paddle.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x

    def handle_wall_collisions(self):
        """
        Updates dx and dy depending on whether or not ball has hit a wall.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self._dx = -self._dx
        if self.ball.y <= 0 or self.ball.y >= self.window.height - self.ball.height:
            self._dy = -self._dy

    def handle_reflect(self, is_horizontal=False):
        if is_horizontal:
            self._dx = -self._dx
        else:
            self._dy = -self._dy
    
    def update_lives(self, lives):
        self.lives_label.text = 'Lives: ' + str(lives)
        self.lives_label.x = 5  
        self.lives_label.y = self.window.height - 5  

    # ----------------------------------------------------------------------------------------------
    # 困難模式按鈕
    def reset_ball(self):
        # 恢復球的初始大小
        self.window.remove(self.ball)
        self.ball = GOval(self.original_radius * 2, self.original_radius * 2)
        self.ball.filled = True
        self.b = self.original_radius  # 更新半徑

        # 將球放置在畫面中間
        self.window.add(
            self.ball,
            x=(self.window.width - self.ball.width) / 2,
            y=(self.window.height - self.ball.height) / 2
        )

        # 恢復速度
        self._dx = 0
        self._dy = 0

        # 如果處於隱形模式，恢復原始狀態
        if self.is_invisible_mode_button:
            # 恢復 Paddle
            try:
                self.paddle.color = 'black'  
                self.paddle.fill_color = 'black'  
                self.paddle.filled = True
            except ValueError:
                pass  # 如果 Paddle 已經存在，跳過

            # 恢復分數倍率
            for color in self.color_to_score:
                self.color_to_score[color] /= 1.5

            self.is_invisible_mode_button = False
            self.window.add(self.invisible_mode_button)
            self.window.add(self.speed_mode_button)
        
        
        # 如果處於加速模式，恢復原始狀態
        if self.is_speed_mode:
            if self._dx != 0:
                self._dx /= 1.3
            if self._dy != 0:
                self._dy /= 1.3

            self.is_speed_mode = False
            self.window.add(self.speed_mode_button)
            self.window.add(self.invisible_mode_button)
        
    # ----------------------------------------------------------------------------------------------
    
    # ---------------------------------------------------------------------------
    # Ext: 分數 
    def update_score_label(self):
        self.score_label.text = f'Score: {self.score}'
        self.score_label.x = self.window.width - self.score_label.width - 10  
    # Ext: 分數    
    def display_round_scores(self, round_scores):
        y_offset = 400  #顯示位置
        max_score = max(round_scores)
        
        for i, score in enumerate(round_scores, start=1):
            score_label = GLabel(f'Round {i} Score: {score}')
            score_label.font = '-20'

            # 如果是最高分數，將其顯示為紅色
            if score == max_score:
                score_label.color = 'red'  
            else:
                score_label.color = 'black'

            score_label.x = (self.window.width - score_label.width) / 2
            score_label.y = y_offset
            self.window.add(score_label)
            y_offset += 30  # 每行分數的間距
    # ----------------------------------------------------------------------------------------------
    
    
    # ----------------------------------------------------------------------------------------------
    # 困難模式按鈕
    def handle_hard_mode(self, event):
        if (
            self.invisible_mode_button.x <= event.x <= self.invisible_mode_button.x + self.invisible_mode_button.width and
            self.invisible_mode_button.y - self.invisible_mode_button.height <= event.y <= self.invisible_mode_button.y
        ):
            if not self.is_invisible_mode_button:  # 確保隱形模式只啟用一次
                self.is_invisible_mode_button = True
                self.activate_invisible_mode()
                self.window.remove(self.invisible_mode_button)
                self.window.remove(self.speed_mode_button)

        elif (
            self.speed_mode_button.x <= event.x <= self.speed_mode_button.x + self.speed_mode_button.width and
            self.speed_mode_button.y - self.speed_mode_button.height <= event.y <= self.speed_mode_button.y
        ):
            if not self.is_speed_mode:  # 確保加速模式只啟用一次
                self.is_speed_mode = True
                self.activate_speed_mode()
                self.window.remove(self.speed_mode_button)
                self.window.remove(self.invisible_mode_button)
        else:
            # 未點擊到任何按鈕，啟動遊戲
            self.set_speed(event)
            
      
    def activate_invisible_mode(self):  #隱形模式
        # 隱藏 Paddle
        self.paddle.color = 'white'  
        self.paddle.fill_color = 'white'  
        self.paddle.filled = False

        # 分數倍率 1.5x
        for color in self.color_to_score:
            self.color_to_score[color] *= 1.5

        # 標記隱形模式已啟用
        self.is_invisible_mode_button = True
        
    def activate_speed_mode(self):  # 加速模式
        # 如果速度為 0，初始化速度
        if self._dx == 0 and self._dy == 0:
            self._dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self._dx = -self._dx
            self._dy = INITIAL_Y_SPEED
            if abs(self._dx) < 2:
                self._dx = 2 if self._dx > 0 else -2

        # 增加速度 
        self._dx *= 1.3
        self._dy *= 1.3

        self.is_speed_mode = True
    # ----------------------------------------------------------------------------------------------
    def generate_bricks(self, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS):
            # 首先移除所有現有的磚塊
            for brick in self.bricks:
                self.window.remove(brick)
            self.bricks.clear()
            self.brick_count = 0  # 重置磚塊計數

            # 隨機生成磚塊
            for j in range(brick_rows):  # 每行
                row_colors = self.colors.copy()
                random.shuffle(row_colors)  # 隨機排序顏色
                for i in range(brick_cols):  # 每列
                    brick = GRect(
                        width=BRICK_WIDTH,
                        height=BRICK_HEIGHT,
                        x=i * (BRICK_WIDTH + BRICK_SPACING),
                        y=j * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_OFFSET
                    )
                    color = row_colors[i % len(row_colors)]  # 循環取顏色
                    brick.fill_color = color
                    brick.color = color
                    brick.color_name = color  
                    brick.filled = True
                    self.window.add(brick)
                    self.bricks.append(brick)
                    self.brick_count += 1
