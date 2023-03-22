room_type = int(input("""Using the numbers provided, choose the general shape of your room:
1. cube/cuboid
2. cylinder
"""))

### FOR CUBE/CUBOID###

if room_type == 1:
#inputting dimensions
    width = int(input("Input the width in metres "))
    depth = int(input("Input the depth in metres "))
    height = int(input("Input the height in metres "))

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
    print("The total volume of the room is",room_volume,"metres cubed.")

###FOR CYLINDER###

if room_type == 2:
    diameter = int(input("Input the diameter in metres "))
    height = int(input("Input the height in metres "))

#calc and print floor area
    floor_area = round(3.1416*((diameter/2)**2),2)
    print("The area of the floor is",floor_area,"metres squared.")

#calc and print paint for walls
    wall_area = 3.1416*diameter*height
    print("You will need about",round(wall_area/6.5,1),"litres of paint to paint all of the walls.")
