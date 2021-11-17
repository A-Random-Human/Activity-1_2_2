# a121_catch_a_turtle.py
# The update_leaderboard Function
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#Input from User
player_name = input ("Please enter your name: ")

#-----game configuration----
font_setup = ("Arial", 20, "bold")
font_setup2 = ("Arial", 10, "bold")
spotColor = "LightCoral"
spotShape = "circle"
spotSize = 15
score = 0

#-----initialize turtle-----
spot = trtl.Turtle(spotShape)
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.pencolor("pink")
spot.speed(5)
spot.penup()

#Score variables
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(60,120)

#timer variables
timer = 5
counter_interval = 500   
timer_up = False
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-200,120)

"""
#game Over
game_over = trtl.Turtle("turtle")
game_over.shape("turtle")
game_over.turtlesize(20)
game_over.fillcolor("YellowGreen")
game_over.pencolor("YellowGreen")
game_over.speed(5)
game_over.penup()
"""

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []

wn = trtl.Screen()
trtl.screensize(400, 300, "YellowGreen")
#-----game functions--------

def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,135)
  spot.goto(new_xpos, new_ypos)

def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
    global timer
    timer +=1
    update_score()
    change_size()
    change_position()
    
    
def change_size():
  global spotSize
  if spotSize > 0:
    spotSize -=1
  else:
    spotSize  +=1
  spot.turtlesize(spotSize)

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=font_setup)

"""
def game_over_leaderboard():
  global game_over
  game_over.left(20)
  game_over.shape("turtle")
  game_over.color("midnightblue")
  game_over.fillcolor("midnightblue")
  trtl.bgcolor ("plum")

def game_over():
  game_over.goto(-20,-150)
  game_over.showturtle()
  game_over.turtlesize(10)
  game_over.left(20)
  game_over.shape("turtle")
  game_over.fillcolor("FireBrick")
  trtl.bgcolor ("Yellow")
"""
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
  
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    #game_over_leaderboard()
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
    
  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
    #game_over()


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#Clicking Command
spot.onclick(spot_clicked)

#-----events----------------
wn.ontimer(countdown, counter_interval) 
wn.mainloop()