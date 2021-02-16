# To run this game use this url :  http://www.codeskulptor.org/#user48_jz3okBVt7B_0.py
#
# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
win = 0
total_attempts = 0
timer_stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global D
    global C
    A = 0
    B = 0
    C = 0
    D = 0
    if time < 10:
        D = time % 10
    elif time < 100:
        C = (time // 10) % 10
        D = (time - C * 10) % 10
    elif time < 600:
        B = time // 100
        C = ((time - B * 100) // 10) % 10
        D = (time - B * 100 + C * 10) % 10
    else:
        A = time // 600
        B = (time - A * 600) // 100
        C = ((time - A * 600 + B * 100) // 10) % 10
        D = (time - A * 600 + B * 100 + C * 10) % 10
        
    string = str(A) + ':' + str(B) + str(C) + '.' + str(D)  
    return string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_stopped
    timer_stopped = False
    timer.start()
    
def stop():
    global timer_stopped, total_attempts, win
    if timer_stopped == False:
        if (time % 10 == 0) and (time != 0):
            total_attempts += 1
            win += 1
        elif time != 0:
            total_attempts += 1            
    timer_stopped = True
    timer.stop()
           
def reset():
    global win, total_attempts, time
    time = 0 
    win = 0
    total_attempts = 0
    timer_stopped = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (100,140), 74, 'Red')
    canvas.draw_text(str(win) + '/' + str(total_attempts), (330, 30), 25, 'Red')
    
# create frame
frame = simplegui.create_frame('Stop Watch', 400, 250)

# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button('Start', start)
stop_button = frame.add_button('Stop', stop)
reset_button = frame.add_button('Reset', reset)

# start frame
frame.start()
