import random
import arcade
# RGB color https://htmlcolorcodes.com/
'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a "WHILE" or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
arcade.open_window(700, 700, "Rachel Linthicum")
arcade.set_background_color((255, 255, 255))

arcade.start_render()

# Raining Side
# ----- background color -----
arcade.draw_rectangle_filled(350, 200, 700, 500, (76, 72, 71), 0)
arcade.draw_rectangle_filled(295, 379, 300, 80, (28, 194, 231), 133)
arcade.draw_rectangle_filled(30, 350, 500, 500, (28, 194, 231), 140)
arcade.draw_rectangle_filled(380, 350, 280, 50, (76, 72, 71), 120)
arcade.draw_rectangle_filled(194, 600, 400, 400, (28, 194, 231))
# ----- Lightning! -----
arcade.draw_rectangle_filled(550, 380, 200, 40, arcade.color.YELLOW, 145)
arcade.draw_rectangle_filled(488, 268, 150, 40, arcade.color.YELLOW, 80)
point_list = ((380, 155), (485, 191), (475, 231))
arcade.draw_polygon_filled(point_list, arcade.color.YELLOW)
# ----- Cloud Loop -----
centX = random.randint(400, 700)
centY = random.randint(430, 700)
colorOptions = random.randint(20, 30)
for i in range(800):
    arcade.draw_circle_filled(centX, centY, 30, (colorOptions, colorOptions, colorOptions))
    centX = random.randint(400, 700)
    centY = random.randint(430, 700)
    colorOptions = random.randint(20, 30)
arcade.draw_rectangle_filled(535, 700, 370, 230, (28, 194, 231), 142)
arcade.draw_rectangle_filled(449, 555, 290, 100, (28, 194, 231), 142.1)
arcade.draw_rectangle_filled(415, 570, 105, 100, (28, 194, 231), 90)
arcade.draw_rectangle_filled(385, 473, 144, 80, (28, 194, 231), 120)
arcade.draw_rectangle_filled(339, 412, 90, 40, (28, 194, 231))
arcade.draw_rectangle_filled(360, 370, 280, 30, (28, 194, 231), 120)
# Line Seperator
# ----- Line trough middle (top right to bottom left) -----
arcade.draw_rectangle_filled(50, 50, 650, 30, arcade.color.BLACK, 140)
arcade.draw_rectangle_filled(360, 370, 280, 30, arcade.color.BLACK, 120)
arcade.draw_rectangle_filled(700, 700, 700, 30, arcade.color.BLACK, 142)
# ----- VS -----
# arcade.draw_rectangle_filled(350, 350, 200, 85, arcade.color.WHITE, 0)
arcade.draw_text("V S", 255, 312, arcade.color.CORAL, 100)

# SUN
arcade.draw_circle_filled(150, 600, 150, arcade.color.YELLOW)
arcade.draw_circle_outline(150, 600, 150, arcade.color.YELLOW, 3)
# ----- Rays -----
tiltR = 0
for i in range(4):
    arcade.draw_rectangle_filled(140, 600, 450, 40, arcade.color.YELLOW, tiltR)
    tiltR += 45
# ----- Sun's Smile -----
arcade.draw_ellipse_filled(170, 490, 80, 35, arcade.color.BLACK)
arcade.draw_ellipse_filled(170, 490, 70, 25, arcade.color.YELLOW)
arcade.draw_rectangle_filled(170, 510, 150, 40, arcade.color.YELLOW)
# ----- Sun's Sunglass -----
arcade.draw_rectangle_filled(148, 570, 350, 10, arcade.color.BLACK)
arcade.draw_rectangle_outline(148, 570, 350, 10, arcade.color.BLACK, 5)
arcade.draw_circle_filled(130, 560, 50, arcade.color.BLACK)
arcade.draw_circle_filled(230, 560, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(148, 595, 350, 40, arcade.color.YELLOW)
arcade.draw_rectangle_filled(321, 565, 30, 40, (28, 194, 231), 104)
arcade.draw_rectangle_filled(321, 565, 30, 40, (28, 194, 231), 90)
arcade.draw_rectangle_filled(140, 600, 450, 40, arcade.color.YELLOW, 0)

arcade.finish_render()
arcade.run()
