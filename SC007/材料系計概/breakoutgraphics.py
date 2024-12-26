from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 4  # Number of rows of bricks
BRICK_COLS = 4  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 2  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

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
        # Initialize our mouse listeners
        onmouseclicked(self.set_speed)
        
        self.brick_count = 0
        # Draw bricks
        self.brick = GRect(width=brick_width, height=brick_height)
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height, x=i * brick_width + (i) * brick_spacing,
                                   y=j * brick_height + j * brick_spacing)
                if j == 0 or j == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j == 2 or j == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j == 4 or j == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j == 6 or j == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.brick.filled = True
                self.window.add(self.brick)
                self.brick_count += 1  
        self.obj = None
        
        # 生命值
        self.lives_label = GLabel('Lives: ')
        self.lives_label.font = '-20'
        self.window.add(self.lives_label, x=5, y=self.window.height - 5)

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

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self._dx = 0
        self._dy = 0