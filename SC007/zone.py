from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    while True:
        graphics.move_ball()
        graphics.handle_wall_collisions()
        if graphics.ball_in_zone():
            graphics.lives -= 1
            graphics.lives_label.text = "lives:" + str(graphics.lives)
            if graphics.lives > 0 :
                graphics.reset_ball()
            else:
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
