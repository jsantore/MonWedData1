import math

from nicegui import ui
WIDTH = 1200
HEIGHT= 1000
X_AXIS_HEIGHT =900
list_of_drawables = []
graph_space = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space.classes("w-lg bg-stone-100")
graph_space2 = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space2.classes("w-lg bg-yellow-100")
x_axis = f'''<line x1=100 y1={X_AXIS_HEIGHT} x2={WIDTH} y2={X_AXIS_HEIGHT} stroke='black'/>'''
y_axis= f'''<line x1=100 y1=0  x2=100 y2={X_AXIS_HEIGHT} stroke='black' stroke-width=3 />'''
list_of_drawables.append(y_axis)
list_of_drawables.append(x_axis)
with open("MedianSalariesTech.txt","r") as file:
    lines = file.readlines()
    data_lines = lines[1:]
    xpos = 100
    bar_color = "black"
    for line in data_lines:
        salary_data = line.split("~")
        pay_as_string = salary_data[-2]
        pay_as_string = pay_as_string[1:]
        pay_all_us=int(pay_as_string)
        ma_pay_as_string = salary_data[-1]
        ma_pay_as_string = ma_pay_as_string[1:]
        ma_pay = int(ma_pay_as_string)
        #I tried it out, the data ranges from -$1050 to $31170
        pay_difference = ma_pay - pay_all_us
        if pay_difference > 25_000:
            bar_color = "green"
        elif pay_difference > 15_000:
            bar_color = "pink"
        elif pay_difference > 7_000:
            bar_color = "blue"
        elif pay_difference > 0:
            bar_color = "yellow"
        else:
            bar_color = "red"
        #scale the bar height to fit the graph
        bar_height = pay_difference/50
        if bar_height < 0:
            bar_height = math.fabs(bar_height)
        bar = f"""<rect  x={xpos} y={X_AXIS_HEIGHT-bar_height} width=100 height={bar_height} fill='{bar_color}'/>"""
        list_of_drawables.append(bar)
        bar_label = f''''<text x={xpos+40} y={X_AXIS_HEIGHT-bar_height} fill='black' writing-mode='vertical-rl' font-size=16 >
{salary_data[0]} </text>'''
        list_of_drawables.append(bar_label)
        xpos +=100

big_string_of_drawables = "\n".join(list_of_drawables)
graph_space.set_content(big_string_of_drawables)
ui.run()