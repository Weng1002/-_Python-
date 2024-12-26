from typing import Callable

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel  
from breakoutgraphics_ext import BreakoutGraphics_ext

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3   # Number of attempts


def main():
    graphics = BreakoutGraphics_ext()
    lives = NUM_LIVES
    graphics.update_lives(lives)
    
    # ---------------------------------------------------------------------------
    # Ext: 分數
    round_scores = [] 
    # ---------------------------------------------------------------------------
    
    while True:
        # 遊戲勝利條件
        if graphics.brick_count == 0:
            win_label = GLabel('You Win!')
            win_label.font = '-30'
            win_label.x = (graphics.window.width - win_label.width) / 2
            win_label.y = (graphics.window.height + win_label.height) / 2
            graphics.window.add(win_label)
            break
        
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            
            # ---------------------------------------------------------------------------
            # Ext: 分數
            round_scores.append(graphics.score)
            graphics.score = 0  # 重置分數
            graphics.update_score_label()
            # ---------------------------------------------------------------------------
            
            lives -= 1
            graphics.update_lives(lives)   # 更新生命值
            if lives == 0:
                graphics.window.remove(graphics.invisible_mode_button)
                graphics.window.remove(graphics.speed_mode_button)
                game_over_label = GLabel('Game Over')
                game_over_label.font = '-30'
                game_over_label.x = (graphics.window.width - game_over_label.width) / 2
                game_over_label.y = (graphics.window.height + game_over_label.height) / 2
                graphics.window.add(game_over_label)
                
                # ---------------------------------------------------------------------------
                # Ext: 分數
                graphics.display_round_scores(round_scores)
                # ---------------------------------------------------------------------------
                
                break
            else:
                graphics.reset_ball()  # 重置球的位置和速度
                graphics.generate_bricks()
        else:
            graphics.move_ball()
            graphics.handle_wall_collisions()
            check_collision(graphics)
        pause(FRAME_RATE)

def check_collision(graphics):
    x = graphics.ball.x
    y = graphics.ball.y
    r = graphics.get_ball_radius()

    obj1 = graphics.window.get_object_at(x, y)  # 左上
    obj2 = graphics.window.get_object_at(x + 2 * r, y)  # 右上
    obj3 = graphics.window.get_object_at(x, y + 2 * r)  # 左下
    obj4 = graphics.window.get_object_at(x + 2 * r, y + 2 * r)  # 右下

    # 檢測碰撞並執行相應動作
    for obj in [obj1, obj2, obj3, obj4]:
        if obj is not None:  # 如果物件非空，代表發生碰撞
            # 過濾掉非磚塊和非板子的物件
            if isinstance(obj, GLabel):
                continue
            
            if obj is graphics.paddle:  # 碰到板子
                # 判斷球的撞擊點
                if graphics.ball.y + graphics.ball.height - graphics.paddle.y < r:  # 上表面碰撞
                    graphics.handle_reflect(is_horizontal=False)
                    graphics.ball.y = graphics.paddle.y - graphics.ball.height - 1  # 移到板子外部
                else:  # 側邊碰撞
                    graphics.handle_reflect(is_horizontal=True)
                    if graphics.ball.x < graphics.paddle.x:  # 左側
                        graphics.ball.x = graphics.paddle.x - graphics.ball.width - 1
                    else:  # 右側
                        graphics.ball.x = graphics.paddle.x + graphics.paddle.width + 1
                return  # 碰撞處理結束
            elif obj is not graphics.paddle:  # 碰到磚塊
                if graphics.window.get_object_at(obj.x, obj.y) == obj:   # 確保磚塊尚未被移除
                    
                    # ---------------------------------------------------------------------------
                    # Ext: 分數
                    color = obj.color_name
                    score_to_add = graphics.color_to_score.get(color, 0)
                    graphics.score += score_to_add
                    graphics.update_score_label()
                    # ---------------------------------------------------------------------------
                    
                    graphics.window.remove(obj)  # 移除磚塊
                    graphics.brick_count -= 1    # 減少磚塊數量
                    graphics.handle_reflect(is_horizontal=False)  # 球反彈
                    return  # 碰到磚塊即可結束，無需檢查其他頂點


if __name__ == '__main__':
    main()