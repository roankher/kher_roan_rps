# This file was created by: Roan Kher

import turtle #imports the turtle file
from turtle import * # imports turtle
import os # imports the turtle os
print("The current working directory is (getcwd): " + os.getcwd()) # tells the code where to look for images and turtle
print("The current working directory is (path.dirname): " + os.path.dirname(__file__)) # tells the code where to look for the code in the file. 


game_folder = os.path.dirname(__file__) # defines the path needed to get to the file
images_folder = os.path.join(game_folder, 'images') # within the path from above, this line tells the computer which folder to look in and what the name of the subfolder is. 

# this sets up the size of the turtle window
WIDTH, HEIGHT = 1000, 400
# the size of the rock image
rock_w, rock_h = 256, 280
# the size of the paper image
paper_w, paper_h = 256, 204
# the size of the scissors image
scissors_w, scissors_h = 256, 170


# This code all sets up the window that the turtle operates in. It tells it the heigh and initializes how we will determine the position later. Also it tells us the color it needs to be. 
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# this calls the screen to appear. 
cv = screen.getcanvas()

cv._rootwindow.resizable(False, False)


# The following 6 lines of code tell the computer where to go for each image (the folders)
rock_image = os.path.join(images_folder, 'rock.gif')

rock_instance = turtle.Turtle()

paper_image = os.path.join(images_folder, 'paper.gif')

paper_instance = turtle.Turtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')

scissors_instance = turtle.Turtle()

# all of the next lines tell the computer what to do know that it has the proper .gif images .
def show_rock(x,y):
    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup()
    rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)  
    paper_instance.shape(paper_image) 
    paper_instance.penup()  
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

# These setup how we are going to determine the rules for the text. 
t = turtle.Turtle() # one function of turtle that tells the turtle to move
text = turtle.Turtle() # the other function of turtle, that tells the text to move
text.color('deep pink') # The text color
t.penup() # makes sure lines aren't being drawn from one point to the next
text.hideturtle() # this hides the turtle animated

t.hideturtle()
# these lines tell the code where to put the images of rock, paper, and scissors, after we have the turtle screen initialized.
show_rock(-300, 0)
show_paper(0,0)
show_scissors (300,0)
# these lines of the code tell the code to ask the player to choose rock, paper or scissors. 
count = 0
while count < 10000:
    text.penup() # The penup removes the lines
    text.hideturtle() # hides any turtles
    text.setpos(-300,150) # where the text appears in the window (pixels)
    text.write("What do you choose, rock, paper, or scissors?", False, "left", ("Arial", 24, "normal"))
    # these lines of code are responsible for detecting whether or not the mouse button has hit an image. When they have hit something, they return true.
    def collide(x,y,obj,w,h):
        if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
            return True
        else: 
            return False
    # here I was trying to get the terminal to display a message when someone clicked on something that wasn't rock, paper, or scissors. 
    if collide == False:
        t.penup()
        text.setpos(-300,150)
        text.write("Please select an actual value", False, "left", ("Arial", 24, "normal"))
        
            
        


    '''
    all of these lines tell the code to use the previous function (collide), which we defined earlier. It tells them that if collide occurs in the same position as rock, paper, or scissors, the code should mark that that's the input. 
    When the code hits any of the options, it tells the code to assign the variable (userchoice) to the value the player clicked on.
    '''
    def player(x, y): 
        global text

        if (collide(x,y,rock_instance, rock_w, rock_h)):
            user_choice = "rock"
        elif(collide(x,y,paper_instance,rock_w,rock_h)):
            user_choice = "paper"
        elif(collide(x,y,scissors_instance,scissors_w,scissors_h)):
            user_choice = "scissors"

        # cleans up the writing so its in the right position and also clears the previous writing. 
        text.penup()
        text.clear()  
        text.goto(-120, 150)
        text.write(f"You chose {user_choice}!", align="left", font=("Arial", 24, "normal"))

        
        # imports randint, so the computer can randomly choose what it wants to pick
        from random import randint
        # the choices are the list of options and the computer function is how the computer randomly selects the values to select. 
        choices = ["rock", "paper", "scissors"]
        computer = choices[randint(0, 2)]

        # this writes that the computer has selected rock, paper or scissors. It tells the computer where to put the text, and also to clean up the lines. 
        message = f"Computer chooses... {computer}!"
        x, y = -200, -200
        target_x, target_y = -200, -200
        text.penup()
        text.goto(x, y)
        text.write(message, align="left", font=("Arial", 24, "normal"))
        text.goto(target_x, target_y)

        # these two lines serve to delay the time between the person choosing and the computer's choice staying on the screen. We want the result of the game to show after 1 second, not immediately. 
        import time

        time.sleep(1)
        # this is the logic. we feed in the two variables, so it can tell whether or not the person has won or lost. There are only 3 inputs the person can use to win, so we can code all the ties and losses out very fast, we just had to tell the computer to detect when the player won.
        if user_choice == computer:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer == "scissors") or \
            (user_choice == "paper" and computer == "rock") or \
            (user_choice == "scissors" and computer== "paper"):
            result = "You won!"
        else:
            result = "You lost!"
        # More text formatting and the text gets cleared after the person clicks on the text again
        text.clear()
        text.goto(-80, 150)
        text.write(result, align="left", font=("Arial", 24, "normal"))
        # waits for 1 second, then clears the result so the player knows they can play again. 
        time.sleep(1)

        text.clear()
        
    # closes the terminal and closes the loop of code 
    # 
    playerchoice = screen.onclick(player)

    playerchoice = screen.mainloop()



