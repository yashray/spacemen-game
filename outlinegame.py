#python project: spaceman game using python inbuild turtle module.
# made by: Yash Ray and Manushi Vakharia


#---import modules---
import turtle
import random
import time
import os
import math
#------create turtle objects-----
sc = turtle.Screen()
t=turtle.Turtle()
player=turtle.Turtle()
e=turtle.Turtle()
bullet=turtle.Turtle()
bullet1=turtle.Turtle()
s=turtle.Turtle()
point=turtle.Turtle()
life=turtle.Turtle()
e_weapon=turtle.Turtle()
#------define variables------
e_weapon_speed=15
e_weapon_state=1
shipspeed=16
bulletspeed=30
bulletspeed1=30
playerspeed=40
enemyspeed=7
score=0
bulletstate=True
bulletstate1=True
enemies=[]
alist=[]
blist=[]
plist=[1,2,3]
eneship=[]
#-------define list for enemy positios----------
posix=[-500,-450,-425,-400,-375,-350,-325,-300,-230,-273,-150,-131,-100,-12,-56,-80,-256,-289,0,89,137,189,210,265,300,278,300,325,350,375,400,425,450,475,500]
posiy=[-150,-123,-100,-50,-12,0,10,50,89,123,167,200,223,240]


#--------- create screen-----------
def screen():

        sc.bgcolor("black")
        sc.title("Spacemen")
#-------Register the shapes--------[2]
        turtle.register_shape("playerr.gif")
        turtle.register_shape("enemy.gif")
       
        
        turtle.register_shape("player.gif")
#-------create player---------

def p(player):
    player.clear()
    player.shape("playerr.gif")
    player.penup()
    player.speed(0)
    player.setposition(0,-300)  # set player for his posotion.

#--------create enemies--------
         
def ene(e):
        #-------ask player for total number of enemies----
                  no=5
         if no>=1:
                enemies.clear()
                for i in range(no):
                    
                    enemies.append(turtle.Turtle()) # create turtle object for all enemies
                for enemy in enemies:
                    enemy.shape("enemy.gif")
                    enemy.penup()
                    enemy.speed(0)
                    x=random.choice(posix)  # select x position form posix list
                    #print("x:",x)
                    #----to remove overriding enemy position-------
                    if x in alist:  # check it is already in alist or not if yes then
                            x=random.choice(posix)  # choice again
                                #print("x1:",x)
                    else:
                            alist.append(x) # otherwise add that number to alist
                            #print("alist",alist)
                        
                    y=random.choice(posiy)  # select y position
                    if y in blist:
                            y=random.choice(posiy)
                    else:
                            blist.append(y)
                            #print("blist",blist)
                    enemy.setposition(x,y)  # set enemy position
         else:
                print("enter valied number")
                ene(e)
#----------create enemy ship-------   
def ene_ship(s):
        for i in range(0,1):
                eneship.append(turtle.Turtle())
        for ship in eneship:
                ship.shape("player.gif")
                ship.penup()
                ship.speed(0)
                ship.setposition(0,290) # set ship at x=0 and y=290 position
                
#------create player 1st weapon as bullet--------
def player_weapon(bullet):
        bullet.color("green")   #give color for bullet
        bullet.shape("classic") #give shpae for bullet
        bullet.speed(0)         
        bullet.penup()
        bullet.setheading(90)   # rotate shape to 90 degree
        bullet.shapesize(1,1)   # set bullet size
        bullet.hideturtle()     # hide turtle
#-----------create player  2nd weapon as bullet1---------      
def player_weapon1(bullet1):
        bullet1.color("green")
        bullet1.speed(0)
        bullet1.shape("classic")
        bullet1.penup()
        bullet1.setheading(90)
        bullet1.shapesize(1,1)
        bullet1.hideturtle()

#def ene_weapon(e_weapon):
 #       e_weapon.color("green")
  #      e_weapon.shape("triangle")
   #     e_weapon.speed(0)
    #    e_weapon.penup()
     #   e_weapon.setheading(270)
      #  e_weapon.shapesize(1,1)
       # e_weapon.hideturtle()
#--------- for scoring--------        
def player_score(point):
        point.color("red")      # text color
        point.penup()
        point.speed(0)
        point.setposition(530,300)      # set text position
        point.write("Score:" ,align="right",font=("Jokerman",30,"bold"))
        point.hideturtle()
        
#--------define player life---------
def player_life(life):
        life.color("red")
        life.penup()
        life.speed(0)
        life.setposition(-530,300)
        playerlife=len(plist)
        life.write("Life: %d"%playerlife ,align="left",font=("Jokerman",30,"bold"))
        life.hideturtle()
#--------when bullet touch enemyship----------        
def touch_eneship_bullet(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))#[1]
	if distance < 65:       #[2]
		return True
	else:
		return False
#-----when bullet touch enemy-------

def touch(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 30:
		return True
	else:
		return False
       
#-------- Arrow key movements--------  [2] 
#---when left key press---- 
def leftmove():
    x=player.xcor()     # get current x cordinate of player
    x-=playerspeed      #- it with playerspeed
    # check it's boundery conditions
    if x< -620:     # if touch    
        x=-620
    player.setx(x)      #set new position as a x.
#----when right key press------
def rightmove():
    x=player.xcor()     # get x cordinate of player
    x+=playerspeed      # add playerspeed on it
    # check it's boundery conditions
    if x > 620:
        x=620
    player.setx(x)

#----- fire function is used to fire bullets-------

def fire():
	global bulletstate
	global bulletstate1
	if bulletstate == True: #[2] 
		
		bulletstate =False
		x = player.xcor()+ 15 #  x-position of bullet to fire
		y = player.ycor() + 10# y-position of bullet to fire
		bullet.setposition(x, y)        #set x and y positions
		bullet.showturtle()     #enable turtle to see bullets
	if bulletstate1 == True:        #[2]
		
		bulletstate1 = False
		x = player.xcor()- 15
		y = player.ycor() + 10                       
		bullet1.setposition(x, y)
		bullet1.showturtle()
#def enemy_fire():
 #       global e_weapon_state
  #      if e_weapon_state==True:
   #             e_weapon_state=False
    #            x=s.xcor()
     #           y=s.ycor()
      #          e_weapon.setposition(x,y)
       #         e_weapon.showturtle()

#----for pausing game-----
def pause():
       os.system("pause")
       
        
#-------call above define methods--------- 

screen()
p(player)
ene(e)
player_weapon(bullet)
player_weapon1(bullet1)
ene_ship(s)
player_score(point)
player_life(life)
#ene_weapon(e_weapon)

#-----keyevents------
turtle.listen()
turtle.onkey(leftmove,"Left")
turtle.onkey(rightmove,"Right")
turtle.onkey(fire,"space")
turtle.onkey(pause,"p")

#---------game loop---------

while True:

        
	for enemy in enemies:
                #move left and right enemy
		x = enemy.xcor()
		y=enemy.ycor()
		x += enemyspeed	
		enemy.setx(x)
		#------ check if bullet touch player then-------
		if touch(player, enemy):
			print ("Game Over")
			print("your score is", score)
			sc.bye()        # for closing turtle screen
			
                #--------check if 1st bullet touch enemy----------        
		if touch(bullet1, enemy):       #[2]
                        #----reset the enemy------
			
			x = random.choice(posix)
			y = random.choice(posiy)
			enemy.setposition(x, y)

			#Update the score

			score += 10
			point.clear()
			point.write("score: %s" %score, align="left", font=("Jokerman",30,"bold"))
			
			#Reset the bullet
                        
			bullet1.hideturtle()
			bulletstate1 = True
			bullet1.setposition(0, -300)
		#-------if 2nd bullet touch enemy---------      [2]	
		if touch(bullet, enemy):
                        #Reset the enemy
			x = random.choice(posix)
			y = random.choice(posiy)
			enemy.setposition(x, y)
			#Update the score
			
			score += 10
			
			point.clear()
			point.write("score: %s" %score, align="left", font=("Jokerman",30,"bold"))
                        
			#Reset the bullet

			bullet.hideturtle()
			bulletstate = True
			bullet.setposition(0, -300)
			
		#-----if enemy touch the end of screen then they move in oppositie direction and come one step down---------
                
		if enemy.xcor() > 620:  #[3]
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *=-1
		
		if enemy.xcor() < -630: #[3]
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *=-1
		 
	#-------enemyship movement----------
	for enemyship in eneship:
                
		x = enemyship.xcor()
		x += shipspeed
		enemyship.setx(x)
		if touch_eneship_bullet(bullet1, enemyship):
                        
			bullet1.hideturtle()
			bulletstate1 =True
			bullet1.setposition(0, -300)
			y=random.randint(280,290)
			enemyship.setposition(0,y)
			score+=15
			point.clear()
			point.write("score: %s" %score, align="left", font=("Jokerman",30,"bold"))
			
		
		#-------if enemyship touch screen bounderies then it move back to opposite direction------
		if enemyship.xcor() > 570:
			for e in eneship:
				y = e.ycor()
				y -= 0
				e.sety(y)
			shipspeed*=-1
			
		if enemyship.xcor() < -570:
			#Move all enemies dosc
			for e in eneship:
				y = e.ycor()
				y -=0
				e.sety(y)
			shipspeed*=-1
        #----for firing bullets------------         
	if bulletstate1 == False:       #[2]
		y = bullet1.ycor()
		y += bulletspeed1
		bullet1.sety(y)
	
                
	if bulletstate == False:        #[2]
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	

	#----Check to see if the bullet has gone to the top-----    [2]   
	if bullet.ycor() > 314:
		bullet.hideturtle()
		bulletstate = True

	if bullet1.ycor() > 314:
		bullet1.hideturtle()
		bulletstate1 = True
        
