import numpy as np


def check_color_mode(colors):
    sorted_colors = np.sort(colors)[::-1]
    sorted_colors_str = ""
    for i in range(4):
        sorted_colors_str += str(sorted_colors[i])
    if sorted_colors_str == "1000":
        return 1000
    elif sorted_colors_str == "1100":
        return 1100
    elif sorted_colors_str == "1110":
        return 1110
    elif sorted_colors_str == "1111":
        return 1111
    elif sorted_colors_str == "2000" or sorted_colors_str == "3000":
        return 3000
    elif sorted_colors_str == "2100":
        return 2100
    elif sorted_colors_str == "2110" or sorted_colors_str == "3110":
        return 3110
    elif sorted_colors_str == "2200":
        return 2200
    elif sorted_colors_str == "2210":
        return 2210
    elif sorted_colors_str == "3100":
        return 3100
    elif sorted_colors_str == "3200":
        return 3200
    elif sorted_colors_str == "4000" or sorted_colors_str == "5000" or sorted_colors_str == "6000":
        return 6000
    elif sorted_colors_str == "4100" or sorted_colors_str == "5100" or sorted_colors_str == "6100":
        return 6100
    return "X"


empty_skill = -1
shape_style = "min-width:60px;\n" \
              "min-height:60px;\n" \
              "max-width:60px;\n" \
              "max-height:60px;\n" \
              "border-radius:30px;\n" \
              "border:1px solid black;\n" \
              "font-size:14px;\n" \
              "background:"
background_style = "background-color:"
color_list = {
    "red": "rgb(255,0,0)",
    "green": "rgb(0,255,0)",
    "blue": "rgb(0,0,255)",
    "yellow": "rgb(255,255,0)",
    "grey": "rgb(60,60,60)",
    "white": "rgb(255,255,255)",
    "colour": "qconicalgradient(cx:0.5,cy:0.5,angle:45, " +
              "stop:0 rgb(255,0,0), " +
              "stop:0.25 rgb(255,255,0), " +
              "stop:0.5 rgb(0,255,0)" +
              "stop:0.75 rgb(0,0,255)" +
              "stop:1 rgb(255,0,0))"
}
data_hero = []
data_zuoyou = []
data_type = 'hero'
search_mode = 0
search_text = ""

enable_collision = True
show_skill = True
