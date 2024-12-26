"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    true_width = width - 2 * GRAPH_MARGIN_SIZE
    interval = true_width / len(YEARS)
    x = (GRAPH_MARGIN_SIZE + year_index * interval)
    return x

def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.


    python3 babygraphics.py
    py babygraphics.py
    canvas.create_text( x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, str(YEARS[i]))
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)
    canvas.create_line(0, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    num_year = len(YEARS)
    for i in range(num_year):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)




def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of names, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # 繪製背景固定線條

    # 繪圖相關常數
    num_years = len(YEARS)
    color_index = 0

    for name in lookup_names:
        color = COLORS[color_index % len(COLORS)]  # 循環選取顏色
        color_index += 1
        prev_x, prev_y = None, None

        for i in range(num_years):
            year = YEARS[i]
            x = get_x_coordinate(CANVAS_WIDTH, i)
            
            # 獲取該年份的排名
            if str(year) in name_data.get(name, {}):
                rank = int(name_data[name][str(year)])
                y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank / MAX_RANK
                rank_text = f"{name} {rank}"
            else:
                rank = "*"
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank_text = f"{name} *"

            # 繪製該年份的點與標籤
            canvas.create_text(x + TEXT_DX, y, text=rank_text, anchor=tkinter.SW, fill=color)
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline=color)

            # 若不是第一個年份，繪製與上一年份的連線
            if prev_x is not None and prev_y is not None:
                canvas.create_line(prev_x, prev_y, x, y, width=LINE_WIDTH, fill=color)

            # 更新前一點的座標
            prev_x, prev_y = x, y



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
