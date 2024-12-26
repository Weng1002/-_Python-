from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2
NUM_LIVES = 3


# __init__ 這是一個初始的函數，如同胚胎，以下()的東西都是初始值
# self 就是要幫胚胎加手 眼睛等器官
#
class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height, title='Zone Game')

        # Create zone
        self.zone = GRect(width=zone_width, height=zone_height, x=(window_width - zone_width) / 2,
                          y=(window_height - zone_height) / 2)
        self.zone.color = 'blue'
        self.window.add(self.zone)

        # Create label
        self.lives = NUM_LIVES
        self.lives_label = GLabel('Lives: ' + str(self.lives))
        self.lives_label.font = '-60'
        self.window.add(self.lives_label, 0, self.lives_label.height)

        # Create ball and initialize velocity/position
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True

        self.dx = 0
        self.dy = 0

        self.reset_ball()

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

    def reset_ball(self):
        """
        Sets the ball in a new position and new velocity. Displays in window.
        """
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_position(self):
        """
        Sets the ball position to a random x, y where ball contained in window.
        """
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = random.randint(0, self.window.height - self.ball.height)

    def set_ball_velocity(self):
        """
        Sets ball x velocity to random negative or positive number.
        Sets ball y velocity to random positive number.
        """
        self.dx = random.randint(0, MAX_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        self.dy = random.randint(MIN_Y_SPEED,MAX_SPEED)
        if random.random()>0.5:
            self.dy = -self.dy

    def ball_in_zone(self):
        """
        Returns whether or not the ball is completely contained within zone.
        """
        zone_left_side = self.zone.x
        zone_right_side = self.zone.x + self.zone.width
        ball_x_in_zone = zone_left_side <= self.ball.x <= zone_right_side - self.ball.width

        zone_top = self.zone.y
        zone_bottom = self.zone.y + self.zone.height
        ball_y_in_zone = zone_top <= self.ball.y <= zone_bottom - self.ball.height

        return ball_y_in_zone and ball_x_in_zone

    def handle_click(self, event):
        """
        Resets the ball if the ball was clicked.

        Input:
            event (GMouseEvent): mouse clicked event
        """
        obj = self.window.get_object_at(event.x, event.y)
        if self.ball is obj:
            self.reset_ball()

    def move_ball(self):
        """
        Moves ball by the change in x and change in y stored in ZoneGraphics class.
        """
        self.ball.move(self.dx, self.dy)

    def handle_wall_collisions(self):
        """
        Updates dx and dy depending on whether or not ball has hit a wall.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.dx = -self.dx
        if self.ball.y <= 0 or self.ball.y >= self.window.height - self.ball.height:
            self.dy = -self.dy
