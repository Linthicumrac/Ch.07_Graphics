import arcade
# RGB color https://htmlcolorcodes.com/
arcade.open_window(600, 600, "My Drawing")
arcade.set_background_color(arcade.color.DARK_CYAN)

arcade.start_render()  # lrtb = left right top bottom
# drawing stuff
arcade.draw_lrtb_rectangle_filled(250, 350, 200, 0, (0, 0, 255, 100))  # (R, G, B, A <-- transparency)
arcade.draw_lrtb_rectangle_outline(250, 350, 200, 0, (0, 0, 0))
arcade.draw_rectangle_filled(300, 300, 300, 300, arcade.color.LIGHT_CRIMSON, 45)
arcade.draw_rectangle_outline(300, 300, 300, 300, (0, 0, 0), 5, 45)
# points/lines
arcade.draw_line(100, 100, 500, 500, (0, 255, 0), 4)
arcade.draw_line(200, 200, 500, 500, (255, 0, 0), 4)
arcade.draw_line(300, 300, 500, 500, (0, 0, 255), 4)
# circles/ ellipses
arcade.draw_circle_filled(300, 300, 50, arcade.color.WHITE)
arcade.draw_circle_outline(300, 300, 50, arcade.color.BLACK, 3)
arcade.draw_ellipse_filled(400, 400, 100, 50, (255, 255, 125), 45)
point_list = ((100, 200), (200, 400), (150, 300), (250, 400))
arcade.draw_polygon_filled(point_list, (150, 150, 255))
# text
arcade.draw_text("PyCasso", 180, 540, arcade.color.YELLOW_ROSE, 50)
# myPic = arcade.load_texture("python.png")  # myPic isn't uploaded to Python so this code wouldn't work
# arcade.draw_texture_rectangle(550, 100, myPic.width, myPic.height, myPic, 45, 150)
# SNOWMAN!!!
radius = 50
y = 100
for i in range(3):
    arcade.draw_circle_filled(100, y, radius, arcade.color.ANTI_FLASH_WHITE)
    y = y + 1.5 * radius
    radius *= 0.8
# Fence posts
for i in range(0, 610, 20):
    arcade.draw_rectangle_filled(i, 70, 10, 60, (137, 63, 165))
# Fence rails
arcade.draw_rectangle_filled(300, 80, 600, 10, (137, 63, 165))
arcade.draw_rectangle_outline(300, 80, 600, 10, (137, 63, 165))

arcade.finish_render()
arcade.run()
