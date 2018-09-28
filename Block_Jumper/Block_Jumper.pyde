#Author: Jatin Karthik Tripathy.
#Guided by: S. Sibi Chakkaravarthy Sethuraman.
#Title: Block - Jumper Game.


import random

class obstacle:
    def __init__(self , x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw_ob(self): 
        fill(60)   
        rect(self.x, self.y, self.w, self.h)
    
    def move(self):
        global speed
        self.x -= speed
        if self.x <= 0 :
            self.x=780
            self.h = random.randrange(20, 50)
            self.y = 200 - self.h
    
    def collision(self, x, y):
        global diameter
        if(self.y < (y+(diameter/2))) and (self.x < ( x+(diameter/2)) and (x-(diameter/2)) < (self.x+self.w)):
            return True
        else:
            return False
    
class stats:
    def __init__(self, score=0):
        self.score = score
    
    def update_score(self):
        global highscore
        self.score += .005
        if highscore < self.score:
            highscore = self.score   
     
                   
def speed_inc(score):
    global speed
    score *= .00001
    speed += score                    
    
def setup():
    global x, y, diameter, lim, game_over, highscore, obs, stat, speed
    size(800, 300)
    
    x = 50
    y = 185
    diameter = 30
    lim = 0
    game_over = False
    highscore = 0
    
    obs = []
    x_val = 780
    y_val = 180
    ht = 20
    wdt = 20
    for i in range(4):
        ob = obstacle(x_val, y_val, wdt, ht)
        x_val += 200
        ht = random.randrange(20, 50) #Height of the collision 
        y_val = 200 - ht
        obs.append(ob)
    
    stat = stats(highscore)
    speed = 1.5    
    
def draw():
    global x, y, diameter, lim, game_over, speed
    
    background(255)

    if game_over == False:
        #frameRate(4)
        fill(51)
        rect(0, 200, 800, 300)
        fill(255)
        ellipse(x, y, diameter, diameter)
        
        if(y<185):
            y += speed + 0.5
        if(y>=185):
            lim = 0
        
        for ob in obs:
            ob.draw_ob()
            ob.move()
            game_over = ob.collision(x, y)
            if game_over == True:
                break
            else:
                stat.update_score()
                speed_inc(stat.score)

        textSize(12);
        textAlign(LEFT)
        fill(0)
        text("PRESS P TO PAUSE", 300, 25, -30)
        text("PRESS R TO RESUME", 300, 50, -30)
                        
        textSize(14);
        textAlign(CENTER)
        fill(0)
        text("Score", 720, 25, -30)
        text(int(stat.score), 770, 25, -30)
        text("HIGH SCORE", 700, 50, -30)
        text(int(highscore), 770, 50, -30)
    
    else:
        background(0)
        textSize(32);
        textAlign(CENTER)
        fill(200);
        text("GAME OVER", 402, 152, -30)
        fill(255) 
        text("GAME OVER", 400, 150)  
        textSize(14)
        text("YOUR SCORE", 370, 200)
        text(int(stat.score), 460, 200)
        text("Press Space To Replay", 400, 250)

        x_val = 780
        for ob in obs:
            ob.x = x_val
            x_val += 200

def keyPressed():
    global lim
    global y
    global game_over, stat, speed
    if key == CODED:
        if keyCode == UP and lim < 1:
            y -= 180
            lim += 1
    if key == ' ':
        game_over = False
        stat.score = 0
        speed = 1.5
    if key == 'p' or key == 'P':
        noLoop()
    if key == 'r' or key == 'R':
        loop()
        
    if y<=15:
        y=15
