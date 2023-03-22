
#inputting dimensions
width = int(input("Input the width in metres squared"))
depth = int(input("Input the depth in metres squared"))
height = int(input("Input the height in metres squared"))

#calc and print floor area
floor_area = width*depth
print("The area of the floor is",floor_area,"metres squared.")

#calc and print paint for walls
wall_area = 2*width*height + 2*depth*height
print("You will need about",round(wall_area/6.5,1),"litres of paint to paint all of the walls.")
#in above calculation, wall area is divided by 6.5. this is because according to Kraudelt Painting, one litre of paint
#can paint about 6.5 metres squared of wall.

#calc and print volume of room
room_volume = floor_area * height
print("The total volume of the room is",room_volume,"cubed.")
