from nicegui import ui
WIDTH = 1200
HEIGHT= 1000
X_AXIS_HEIGHT =900
list_of_drawables = []
graph_tile = ui.label("How Much more do tech workers make in MA than the US?")
graph_tile.style("font-size: 24px;")
graph_space = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space.classes("w-lg bg-stone-100")
x_axis = f'''<line x1=100 y1={X_AXIS_HEIGHT} x2={WIDTH} y2={X_AXIS_HEIGHT} stroke='black'/>'''
y_axis= f'''<line x1=100 y1=0  x2=100 y2={X_AXIS_HEIGHT} stroke='black' stroke-width=3 />'''
list_of_drawables.append(y_axis)
list_of_drawables.append(x_axis)
#now let's draw the labels
for pay_value in range(0,40_000,5_000):
    label = f'''<text x={25} y={X_AXIS_HEIGHT-pay_value/50} fill="black" font-size="14" >{pay_value} </text>'''
    list_of_drawables.append(label)
bar_color = "black"
xpos = 100
with open("MedianSalariesTech.txt","r") as file:
    lines = file.readlines()
    data_lines = lines[1:]
    for line in data_lines:
        salary_data = line.split("~")
        job_name = salary_data[0]
        pay_as_string = salary_data[-2]
        pay_as_string = pay_as_string[1:]
        pay_all_us=int(pay_as_string)
        ma_pay_as_string = salary_data[-1]
        ma_pay_as_string = ma_pay_as_string[1:]
        ma_pay = int(ma_pay_as_string)
        pay_difference = ma_pay - pay_all_us
        bar_height = pay_difference/50
        if pay_difference >20_000:
            bar_color = "green"
        elif pay_difference > 10_000:
            bar_color = "yellow"
        elif pay_difference > 0:
            bar_color = "orange"
        else:
            bar_color = "red"
        bar_top_y = X_AXIS_HEIGHT-bar_height
        bar = f'''<rect x={xpos} y={bar_top_y} width=75 height={bar_height} fill="{bar_color}"/>'''
        label = f'''<text x={xpos+37} y={bar_top_y-10} fill="black" writing-mode="vertical-rl" font-size="14" >{job_name} </text>'''
        print(f"DEBUG: {bar}")
        xpos += 100
        list_of_drawables.append(bar)
        list_of_drawables.append(label)
        #I tried it out, the data ranges from -$1050 to $31170


big_string_of_drawables = "\n".join(list_of_drawables)
graph_space.set_content(big_string_of_drawables)
ui.run()