# implementation of card game - Memory
#import simplegui
import simpleguitk as simplegui 

import random

# global variables 
numbers = range(0,8) 
numbers2 = range(0,8) 
exposed = [False,False,False,False,False,False,False,False,
           False,False,False,False,False,False,False,False] 
state = 0 
previous1 = 0 
previous2 = 0 
turn = 0 


# helper function to initialize globals
def new_game(): 
    global numbers, numbers2, state, exposed, previous1, previous2, turn  
    numbers = range(0,8) 
    numbers2 = range(0,8) 
    exposed = [False,False,False,False,False,False,False,False,
           False,False,False,False,False,False,False,False] 
    state = 0 
    previous1 = 0 
    previous2 = 0 
    turn = 0 
    random.shuffle(numbers) 
    random.shuffle(numbers2) 
    numbers += numbers2 
    random.shuffle(numbers)  
    label.set_text("Turns = "+str(turn)) 
                    
# define event handlers
def mouseclick(pos):
    global numbers, exposed, state, previous1, previous2, turn   
    position = pos[0] / 50  
    if state == 0: 
        exposed[position] = True 
        #previous1 = position 
        state = 1 
    elif state == 1: 
        if exposed[position] == False: 
            exposed[position] = True 
            previous2 = position 
            state = 2 
    elif state == 2: 
        if exposed[position] == False: 
            exposed[position] = True 
            if numbers[previous1] != numbers[previous2]: 
                exposed[previous1] = False 
                exposed[previous2] = False 
                turn += 1 
                label.set_text("Turns = "+str(turn))
            previous1 = position 
            state = 1 
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas): 
    global numbers 
    n = 0 
    for i in numbers: 
        position = 25+50*n 
        position1 = [0+50*n, 0] 
        position2 = [50+50*n, 0] 
        position3 = [50+50*n, 100] 
        position4 = [0+50*n, 100] 
         
        if exposed[n]: 
            canvas.draw_text(str(i), [position, 50], 24, "White") 
        else: 
            canvas.draw_polygon([position1, position2, position3, 
                                 position4], 0.1, 'Black', 'Green') 
        n += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric