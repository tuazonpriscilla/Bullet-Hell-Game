from graphics import*
from math import*
import random

#hearts 50 X 50
#Madoka 150 X 150

#Creates the window
win = GraphWin("Bullet Hell", 800, 900, autoflush = False)

#Makes and draws the start game button and villian character and starts
#the game when the player clicks it
def Start_Game():
    start = Image(Point(400,450), "Start.png")
    start.draw(win)
    
    win.getMouse()

    start.undraw()
    
    Homura = Image(Point(400,250), "Homura.png")
    Homura.draw(win)
    
#Creates and moves the 'bullets'            
class projectile:
    
    def __init__(self, win, x, y, velx, vely):
        self.ball = Circle(Point(x,y),10)
        self.ball.setFill("purple")
        self.ball.draw(win)
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        
    def simStep(self):
        self.ball.move(self.velx,self.vely)

#Makes a pattern of bullets
def wave_1():
    ball = []
    x = -100
    y = 100
    velx = 5
    vely = 5
    
    while win.isOpen():
        p = projectile(win, x, y, velx, vely)
        ball.append(p)

        if y > -300:
            
            x = x + 5
            y = y - 5
        
        else:
            
            return ball

#Makes a pattern of bullets
def wave_2():
    
    ball = []
    x = 900
    y = 100
    velx = -5
    vely = 5
    
    while win.isOpen():
        p = projectile(win, x, y, velx, vely)
        ball.append(p)

        if y > -300:
            
            x = x - 5
            y = y - 5
        
        else:
            
            return ball

#Makes a pattern of bullets
def wave_3():

    ball = []
    x = 800
    y = 0
    velx = 0
    vely = 5
    
    while win.isOpen():
        p = projectile(win, x, y, velx, vely)
        ball.append(p)

        if x > 400:
            
            x = x - 5
        
        else:
            
            return ball

#Makes a pattern of bullets
def wave_4():

    ball = []
    x = 0
    y = 0
    velx = 0
    vely = 5
    
    while win.isOpen():
        p = projectile(win, x, y, velx, vely)
        ball.append(p)

        if x < 400:
            
            x = x + 5
        
        else:
            
            return ball

#Makes a pattern of bullets
def wave_5():

    ball = []
    x = random.randrange(800)
    y = 0
    velx = 0
    vely = 5
    
    while win.isOpen():
        p = projectile(win, x, y, velx, vely)
        ball.append(p)

        if y < 200:
            
            y = y + 5
        
        else:
            
            return ball

# Checks whether the player character and bullets make contact
def check_collision(bullet, character):
    center = bullet.ball.getCenter()
    imgcenter = character.getAnchor()
    radius = bullet.ball.getRadius()
    imgradius = 75
    
    d = radius + imgradius
    
    x = imgcenter.getX()
    y = imgcenter.getY()
    otherx = center.getX()
    othery = center.getY()
    
    current_distance = sqrt((x - otherx)**2+(y - othery)**2)
    
    if current_distance <= d:
        return True
    else:
        return False

#Draws an image to indicate that the player won
def winner():
    winner = Image(Point(400,450), "winner.png")
    winner.draw(win)

#Draws an image to indicate that the player lost
def loser():
    loser = Image(Point(400,450), "lose.png")
    loser.draw(win)
    
           
def main():
    
    Start_Game()
    
    #Draws hearts that indicate lives in the window
    heart = Image(Point(760,40), "heart2.0.png")
    heart2 = Image(Point(760,80), "heart2.0.png")
    heart3 = Image(Point(760,120), "heart2.0.png")    
    heart.draw(win)
    heart2.draw(win)
    heart3.draw(win)
    
    #Sends out the first wave of bullets
    ball = wave_1() 
    ball.extend(wave_2())
    
    #Draws the player character
    img = Image(Point(400,800), "Madoka3.0.png")
    img.draw(win)
    
    time = 0
    life_counter = 0
    
    while win.isOpen():
        
        #Updates the time
        time = time + 1
        
        #Allows the player to move the character
        key = win.checkKey()
        if key == 'Up' and img.getAnchor().getY() > 0:
            img.move(0, -10)
        elif key == 'Down' and img.getAnchor().getY() < 900:
            img.move(0, 10)
        elif key == 'Right' and img.getAnchor().getX() < 800:
            img.move(10, 0)
        elif key == 'Left' and img.getAnchor().getX() > 0:
            img.move(-10, 0)
        
        #Moves the bullets
        for balls in ball:
            balls.simStep()
            
            #lives function: Keeps track of how many lives the player has
            #and erases hearts accordingly, also implements loser
            #function if player loses
            if check_collision(balls, img) == True:
                life_counter = life_counter + 1
        
            if life_counter == 180:
                heart.undraw()
            elif life_counter == 360:
                heart2.undraw()
            elif life_counter == 540:
                heart3.undraw()
                loser()
                
                break
            
        #Sends out waves of bullets at certain times    
        if time == 90:
            ball.extend(wave_1())            
            ball.extend(wave_2())
            
        elif time == 180:
            ball.extend(wave_1())            
            ball.extend(wave_2())
            
        elif time == 270:
            ball.extend(wave_3())
        
        elif time == 360:
            ball.extend(wave_4())
            
        elif time == 450:
            ball.extend(wave_3())
            
        elif time == 540:
            ball.extend(wave_4())
            
        elif time == 630:
            ball.extend(wave_3())
            
        elif time == 720:
            ball.extend(wave_4())
            
        elif time == 810:
            ball.extend(wave_5())
            
        elif time == 840:
            ball.extend(wave_5())
            
        elif time == 870:
            ball.extend(wave_5())
            
        elif time == 900:
            ball.extend(wave_5())
            
        elif time == 930:
            ball.extend(wave_5())
            
        elif time == 960:
            ball.extend(wave_5())
            
        elif time == 990:
            ball.extend(wave_5())
            
        elif time == 1020:
            ball.extend(wave_5())
            
        elif time == 1050:
            ball.extend(wave_5())
            
        elif time == 1080:
            ball.extend(wave_5())
            
        elif time == 1260:
            winner()
            
        update(60)        
main()

