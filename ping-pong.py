import simplegui
import random
v=0
p1x=600
p1y=200
p2x=0
p2y=200
p=0
ball_x=300
ball_y=200
vh=random.random()*10
vv=random.random()*10
team_1=0
team_2=0

def kd(k):
    global p1x,p1y,v,p
    if simplegui.KEY_MAP['up']==k:
        v=-1
    if simplegui.KEY_MAP['down']==k:
        v=1
    if simplegui.KEY_MAP['W']==k:
        p=-1
    if simplegui.KEY_MAP['S']==k:
        p=1
        
def ku(k):
    global v,p
    if simplegui.KEY_MAP['up']==k:
        #if (p1y>40):
        v=0
    if simplegui.KEY_MAP['down']==k:
        #if(p1y<360):
        v=0
    if simplegui.KEY_MAP['W']==k:
        p=0
    if simplegui.KEY_MAP['S']==k:
        p=0

def draw(canvas):
    global p1x,p1y,v,p2y,p2x,p,vh,vv,ball_x,ball_y,team_1,team_2
    canvas.draw_line((590,0),(590,400),1,"white")
    canvas.draw_line((10,0),(10,400),1,"white")
    canvas.draw_line((300,0),(300,590),1,"white")
    canvas.draw_circle((ball_x,ball_y),20,1,"blue","blue")
    canvas.draw_line((p2x,p2y-40),(p2x,p2y+40),20,"red")
    canvas.draw_line((p1x,p1y-40),(p1x,p1y+40),20,"red")


    p1y+=v*4
    p2y+=p*4
    ball_x+=vh
    ball_y+=vv
    if ball_x>=570 or ball_x<=30:
        vh=-vh
    if ball_y>380 or ball_y<20:
        vv=-vv
    if (ball_x>=570)and(ball_y<=p1y-40 or ball_y>=p1y+40):
        team_1+=1
        ball_x=300
        ball_y=200
    if (ball_x<=30) and (ball_y<=p2y-40 or ball_y>=p2y+40):
        team_2+=1
        ball_x=300 
        ball_y=200
    canvas.draw_text(str(team_1),(150,50),30,"white")
    canvas.draw_text(str(team_2),(490,50),30,"white")

    if (p1y<40) or (p1y>360):
        v=0
    if(p2y<40) or (p2y>360):
        p=0        
    
    
frame=simplegui.create_frame("home",600,400)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
frame.set_keyup_handler(ku)
frame.start()
