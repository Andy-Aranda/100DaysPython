'''https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#paso 1: asegurarnos de 
#que primero tiene que toparse con un muro
while front_is_clear():
    move()
turn_left()

#cuando se haya topado con un muro
#puede entrar a este while
while not at_goal():
    if right_is_clear():
        turn_right()
        move()   
    elif front_is_clear():
        move()
    else:
        #si le pongo un turn right
        #se va a quedar girando
        turn_left()
        #porque entra en que la derecha está libre
        #y gira a la derecha
'''