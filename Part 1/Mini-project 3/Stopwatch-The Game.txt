# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
t = 0 
time = "0:00.0" 
x = '0' 
y = '0' 
stop_count = 0 
whole_count = 0 
has_Stopped = True 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    number = int(t) 
    number1 = 0 
    number2 = 0 
    number3 = 0 
    if number < 10: 
        number3 = number 
        return str(number1)+':'+str(number2)+str(number2)+'.'+str(number3)
    elif number >= 10 and number < 100:
        number3 = number % 10 
        number2 = number / 10 
        return str(number1)+':'+str(0)+str(number2)+'.'+str(number3)
    elif number >= 100 and number < 600: 
        number3 = number % 10 
        number2 = number / 10 
        return str(number1)+':'+str(number2)+'.'+str(number3)
    elif number >= 600 and number < 6000: 
        number1 = number / 600 
        number = (number % 600) 
        if number < 10: 
            number3 = number 
            return str(number1)+':'+str(number2)+str(number2)+'.'+str(number3)
        elif number >= 10 and number < 100:
            number3 = number % 10 
            number2 = number / 10 
            return str(number1)+':'+str(0)+str(number2)+'.'+str(number3)
        elif number >= 100 and number < 600: 
            number3 = number % 10 
            number2 = number / 10 
            return str(number1)+':'+str(number2)+'.'+str(number3)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start(): 
    global has_Stopped 
    timer1.start()  
    has_Stopped = False

def stop(): 
    global y, x, stop_count, time, whole_count, has_Stopped   
    if (not(has_Stopped)): 
        timer1.stop() 
        stop_count += 1 
        y = str(stop_count) 
        if time[5] == "0": 
            whole_count += 1 
            x = str(whole_count) 
    has_Stopped = True
        

def reset(): 
    global t, time, x, y, stop_count, whole_count, has_Stopped
    timer1.stop() 
    t = 0 
    time = "0:00.0" 
    stop_count = 0 
    whole_count = 0 
    y = "0" 
    x = "0" 
    has_Stopped = True
    


# define event handler for timer with 0.1 sec interval
def tick(): 
    global t, time 
    t += 1 
    time = format(t) 
    
# define draw handler
def draw(canvas):
    canvas.draw_text(time, [100,100], 36, "Red") 
    canvas.draw_text(x+'/'+y, [140,20], 24, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)

# register event handlers
frame.add_button("Start", start , 200) 
frame.add_button("Stop", stop , 200) 
frame.add_button("Reset", reset , 200) 
frame.set_draw_handler(draw) 
timer1 = simplegui.create_timer(interval, tick)

# start frame
frame.start()
 

# Please remember to review the grading rubric
