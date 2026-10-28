import math

from nicegui import ui

#Here are some "constants" for the graph
WIDTH = 1200
HEIGHT= 1000
X_AXIS_HEIGHT =900
#this is the list for the first graph
list_of_drawables = []
#I've added this second list of drawables for the second graph outside of class
list_of_drawables2 = []
#we need to add a Graph title
title= ui.label("How much more do tech jobs pay in MA compared to all of US")
title.style("font-size: 20px")
#when we want two graphs on one over the other, just add a second interactive image
graph_space = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space.classes("w-lg bg-stone-100")
graph_space2 = ui.interactive_image(size=(WIDTH, HEIGHT))
graph_space2.classes("w-lg bg-yellow-100")

#hwere we are building the horizontal and vertical axes for the graph
x_axis = f'''<line x1=100 y1={X_AXIS_HEIGHT} x2={WIDTH} y2={X_AXIS_HEIGHT} stroke='black'/>'''
y_axis= f'''<line x1=100 y1=0  x2=100 y2={X_AXIS_HEIGHT} stroke='black' stroke-width=3 />'''
list_of_drawables.append(y_axis)
list_of_drawables.append(x_axis)
list_of_drawables2.append(y_axis)
list_of_drawables2.append(x_axis)
#here is where we should add the labels for the vertical axis of the graph in class on Wednesday
for amount in range(0,35_000, 5000):
    location = X_AXIS_HEIGHT-amount/50
    axis_label=f'''<text x=30 y={location} fill='black' font-size=18> ${amount} </text>'''
    list_of_drawables.append(axis_label)

#now open the file and process it, finding the data we want
with open("MedianSalariesTech.txt","r") as file:
    lines = file.readlines()
    data_lines = lines[1:] # the first line is the header information
    xpos = 100  #start the first bar at 100 which is the location of the vertical axis
    bar_color = "black"
    for line in data_lines:
        salary_data = line.split("~") # for this data set the ~ separates the data items
        pay_as_string = salary_data[-2] # US media pay is found in the second to last item
        pay_as_string = pay_as_string[1:] # the $ sign is the first character, remove it
        pay_all_us=int(pay_as_string)
        ma_pay_as_string = salary_data[-1] #MA media pay is found in the last item
        ma_pay_as_string = ma_pay_as_string[1:] #remove the $ sign
        ma_pay = int(ma_pay_as_string)
        #I tried it out, the data ranges from -$1050 to $31170
        pay_difference = ma_pay - pay_all_us
        #remember, make the most restrictive condition first
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
        #scale the bar height to fit the graph - it might have been better to have the 50 be a constant
        bar_height = pay_difference/50
        #the one pay that is lower in MA than in the US as a whole doesn't draw write till we have a positive height
        if bar_height < 0:
            bar_height = math.fabs(bar_height)
        #now create the bar
        bar = f"""<rect  x={xpos} y={X_AXIS_HEIGHT-bar_height} width=100 height={bar_height} fill='{bar_color}'/>"""
        list_of_drawables.append(bar)
        #and the text label for the bar - the text label is drawn on the bar this time
        bar_label = f''''<text x={xpos+40} y={X_AXIS_HEIGHT-bar_height} fill='black' writing-mode='vertical-rl' font-size=16 >
{salary_data[0]} </text>'''
        list_of_drawables.append(bar_label)
        xpos +=100 #move to the next bar location

#finally put everything together and draw the graph
big_string_of_drawables = "\n".join(list_of_drawables)
graph_space.set_content(big_string_of_drawables)
#here we would do the same thing to the other graph with list_of_drawables2
second_drawables = "\n".join(list_of_drawables2)
graph_space2.set_content(second_drawables)
ui.run()