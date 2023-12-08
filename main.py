# Day 18 - Dots Painting Code v0.1

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# Day 18 - Dots Painting Code v0.1

# Import the necessary modules
import turtle as turtle_module
import random

# List of RGB colors extracted from an image or manually defined
color_list = [(152, 72, 58), (41, 126, 82), (241, 223, 195), (197, 151, 119),
              (154, 59, 78), (13, 19, 41), (107, 172, 213), (115, 184, 151),
              (39, 14, 24), (43, 16, 10), (43, 107, 147), (199, 235, 215),
              (56, 171, 128), (234, 211, 101), (152, 27, 42), (208, 68, 81),
              (9, 40, 20), (242, 215, 226), (151, 29, 21), (195, 221, 238),
              (202, 83, 75), (198, 135, 156), (11, 101, 54), (134, 223, 185),
              (31, 36, 153), (46, 161, 187), (84, 111, 199), (248, 163, 152),
              (166, 151, 58), (134, 215, 231)]

# Set up the turtle
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Position the turtle to start painting dots
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

# Loop to paint dots in a grid pattern
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # Paint a dot with a random color
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Close the turtle graphics window when clicked
screen = turtle_module.Screen()
screen.exitonclick()

# END OF CODE
