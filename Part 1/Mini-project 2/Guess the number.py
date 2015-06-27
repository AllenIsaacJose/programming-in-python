# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui 
import random 
import math 

#global variable 
num_range = 100 
random_number = 0
guess_number = 0 
count = 7 
count_limit = 7

# helper function to start and restart the game
def new_game(): 
    global num_range
    global random_number 
    global count 
    global count_limit 
    if count == count_limit: 
        random_number = random.randrange(0, num_range) 
        print "========================================"
        print "New Game, Range is from [ 0 to", num_range,")" 
        print "Number of remaining guess is ", count 
        print "Enter a guess and hit Enter " 
        print ""
    else: 
        print ""
        print "Guess was ", guess_number 
        print "Number of remaining guess is ", count 
        if guess_number >= num_range:
            print "Guess number should be less than ", num_range 
            return 
        if guess_number > random_number: 
            print "Lower!" 
        elif guess_number < random_number:  
            print "Higher!" 
        print ""
        

# define event handlers for control panel
def range100():
    global num_range 
    global count 
    global count_limit 
    num_range = 100  
    print "========================================" 
    print "Range set to 0 to ", num_range 
    count_limit = 7  
    count = 7
    new_game() 
    

def range1000(): 
    global num_range 
    global count 
    global count_limit 
    num_range = 1000  
    print "========================================" 
    print "Range set to 0 to ", num_range 
    count_limit = 10 
    count = 10 
    new_game() 
    
def input_guess(guess): 
    global num_range 
    global random_number
    global guess_number 
    global count 
    global count_limit
    count = count - 1  
    guess_number = int (guess) 
    if guess_number == random_number: 
        print "========================================" 
        print "Correct! You Won!" 
        count = count_limit  
    elif count == 0:  
        print "You Lost!" 
        count = count_limit 
    new_game() 
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200) 

# register event handlers for control elements and start frame
f.add_button("Range is [0,100) ", range100 , 200) 
f.add_button("Range is [0,1000) ", range1000 , 200) 
f.add_input("Enter a guess", input_guess, 200) 

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
