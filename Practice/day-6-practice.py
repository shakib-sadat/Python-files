def my_function():
    print("hello")


num_print = 6
while num_print > 0:
    my_function()
    num_print -= 1

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# hurdle-2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# num_jump = 6
# while at_goal() != True:
#     jump()
#     num_jump -=1

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# hurdle-3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():

#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     if front_is_clear() == True and at_goal() != True:
#         move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     if front_is_clear() == True and at_goal() != True:
#         move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
