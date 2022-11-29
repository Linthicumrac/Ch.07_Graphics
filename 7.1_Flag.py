import arcade
'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize 
accordingly.
************************* put stars on separate loops *************************
'''
arcade.open_window(494, 260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)  # white background = no need for white rectangles
arcade.start_render()  # lrtb = left right top bottom
# red rectangle
cY = 10
for i in range(7):
    arcade.draw_rectangle_filled(247, cY, 494, 20, (191, 10, 48))
    arcade.draw_rectangle_outline(247, cY, 494, 20, (191, 10, 48))
    cY += 40
# blue rectangle
arcade.draw_lrtb_rectangle_filled(0, 197.6, 294, 120, (0, 40, 104))
# stars in a loop
# for i in range(start, stop, step)
starY = 120
for i in range(5):
    # arcade.draw_text("text", startx, starty, color, size, width)
    # 16.9
    arcade.draw_text("*", 13.38, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 46.14, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 78.9, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 111.66, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 144.42, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 177.18, starY, (255, 255, 255), 20, 1, "center")
    starY += 28.08
starY = 134.04
for i in range(4):
    # arcade.draw_text("text", startx, starty, color, size, width)
    arcade.draw_text("*", 32.76, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 65.52, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 98.28, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 131.04, starY, (255, 255, 255), 20, 1, "center")
    arcade.draw_text("*", 163.8, starY, (255, 255, 255), 20, 1, "center")
    starY += 28.08
arcade.finish_render()
arcade.run()