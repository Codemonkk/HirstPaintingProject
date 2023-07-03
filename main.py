# import colorgram as c
#
# rgb_colors=[]
# colors = c.extract('image.jpeg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
t.colormode(255)
color_list = [(249, 233, 19), (199, 12, 31), (235, 151, 37), (34, 81, 190), (231, 229, 5), (49, 219, 54), (197, 68, 23), (34, 33, 154), (216, 13, 9), (245, 42, 160), (71, 8, 51), (243, 247, 252), (15, 154, 16), (227, 18, 119), (227, 152, 8), (14, 208, 223), (62, 19, 8), (224, 140, 208), (245, 45, 17), (248, 11, 8), (10, 97, 61), (90, 76, 11), (54, 210, 228), (17, 17, 57), (238, 156, 219), (83, 75, 211), (75, 213, 162)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1,no_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen.exitonclick()
