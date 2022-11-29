# Sign your name: Rachel Linthicum
import arcade
'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
# 24 lines across ; 19 lines (not counting border lines)
# RGB color https://htmlcolorcodes.com/
# Beginning Stuff
arcade.open_window(500, 400, "Jedi_Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()  # lrtb = left right top bottom
# Lines going vertical
startX = 1
startY = 1
endX = 1
endY = 500
for i in range(30):
    arcade.draw_line(startX, startY, endX, endY, (0, 0, 0), 1)
    startX += 20
    endX += 20
    endY += 20
# lines going horizontal  DONE
stX = 0
stY = 2
enX = 500
enY = 2
for i in range(30):
    arcade.draw_line(stX, stY, enX, enY, (0, 0, 0), 1)
    stY += 20
    enX += 20
    enY += 20
# circle in the middle of the image
arcade.draw_circle_filled(250, 202.5, 40, arcade.color.WISTERIA)
arcade.draw_circle_outline(250, 202.5, 40, arcade.color.WISTERIA, 3)
# Ellipse (bottom left)
arcade.draw_ellipse_filled(101, 102, 120, 40, arcade.color.AMBER)
arcade.draw_ellipse_outline(101, 102, 120, 40, arcade.color.AMBER)
# Purple rectangle (top left)
arcade.draw_rectangle_filled(50, 372, 59.3, 19.5, arcade.color.PHLOX)
arcade.draw_rectangle_outline(50, 372, 59.3, 19.5, arcade.color.PHLOX)
# Rose-ish rectangle (middle)
arcade.draw_rectangle_filled(200, 262, 38, 18, arcade.color.ROSE, -47)
arcade.draw_rectangle_outline(200, 262, 38, 18, arcade.color.ROSE, 1, 47)
# Words (middle left)
arcade.draw_text("I love you. I know.", 22, 163, arcade.color.BRICK_RED, 20)
# single line (bottom left)
arcade.draw_line(79.5, 21, 122, 63.5, (0, 0, 255), 1)
# pacman (top right)
arcade.draw_arc_filled(401, 300, 123, 123, (255, 255, 0), -15, 285, 45, 120)
# square (bottom right)
arcade.draw_rectangle_filled(461, 11, 5, 5, (255, 0, 0))
arcade.draw_rectangle_outline(461, 11, 5, 5, (255, 0, 0))
# drawing stuff
arcade.finish_render()
arcade.run()
