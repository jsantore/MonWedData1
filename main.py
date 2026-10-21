from nicegui import ui
WIDTH = 1200
HEIGHT= 1000
X_AXIS_HEIGHT =900
list_of_drawables = []
graph_space = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space.classes("w-lg bg-stone-100")
x_axis = f'''<line x1=100 y1={X_AXIS_HEIGHT} x2={WIDTH} y2={X_AXIS_HEIGHT} stroke='black'/>'''
y_axis= f'''<line x1=100 y1=0  x2=100 y2={X_AXIS_HEIGHT} stroke='black' stroke-width=3 />'''
list_of_drawables.append(y_axis)
list_of_drawables.append(x_axis)
with open("MedianSalariesTech.txt","r") as file:
    lines = file.readlines()
    data_lines = lines[1:]
    for line in data_lines:
        salary_data = line.split("~")
        pay_as_string = salary_data[-2]
        pay_as_string = pay_as_string[1:]
        pay_all_us=int(pay_as_string)
        ma_pay_as_string = salary_data[-1]
        ma_pay_as_string = ma_pay_as_string[1:]
        ma_pay = int(ma_pay_as_string)


big_string_of_drawables = "\n".join(list_of_drawables)
graph_space.set_content(big_string_of_drawables)
ui.run()