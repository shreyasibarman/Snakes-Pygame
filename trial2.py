import time
import pygame
import sys
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600),0,32)


pygame.display.set_caption('TRIAL1')
def foodloc():
    xfood=random.randint(1,599)
    yfood=random.randint(1,599)
    return (xfood,yfood)


def gameplay():
    speed=150
    x=300
    y=300
    clock=pygame.time.Clock()
    movex=0
    movey=0
    snakelist=[]
    snakelength=1
    score=0
    initial_pos=foodloc()
    newpos=initial_pos
    while True:
         k="ALIVE"
         for event in pygame.event.get():
            if event.type==QUIT:            
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and movey!=1:
                    movey=-1
                    movex=0
                elif event.key==pygame.K_DOWN and movey!=-1:
                    movey=+1
                    movex=0
                elif event.key==pygame.K_LEFT and movex!=1:
                    movex=-1
                    movey=0
                elif event.key==pygame.K_RIGHT and movex!=-1:
                    movex=+1
                    movey=0
         clock.tick(speed)
         x+=movex
         y+=movey
         if x>600:
             x=0
         if y>600:
             y=0
         elif x<0:
             x=600
         elif y<0:
             y=600
         screen.fill((0,0,0))
         screen.lock()
         pygame.draw.circle(screen,(0,0,255),(newpos),6)
         screen.unlock()
         font=pygame.font.SysFont(None,20)
         screen_text1=font.render("SCORE="+str(score),True,(255,255,255))
         screen.blit(screen_text1,(20,20))
         snakehead=(x,y)
         alpha=True
         if alpha:
             snakelist.append((x,y))
             if len(snakelist)>snakelength:
                 del snakelist[0]
                 for i in range(len(snakelist)):
                     if i%7==0:
                         screen.lock()
                         pygame.draw.polygon(screen,(0,0,0),[(snakelist[i][0]-7,snakelist[i][1]),(snakelist[i][0],snakelist[i][1]+8),(snakelist[i][0]+7,snakelist[i][1]),(snakelist[i][0],snakelist[i][1]-8)])
                         screen.unlock()
                     elif i%3==0:
                         screen.lock()
                         pygame.draw.polygon(screen,(255,200,155),[(snakelist[i][0]-7,snakelist[i][1]),(snakelist[i][0],snakelist[i][1]+8),(snakelist[i][0]+7,snakelist[i][1]),(snakelist[i][0],snakelist[i][1]-8)])
                         screen.unlock()
             else:
                 for a,b in snakelist:
                     screen.lock()
                     pygame.draw.polygon(screen,(255,0,0),[(a-7,b),(a,b+8),(a+7,b),(a,b-8)])
                     screen.unlock()
             screen.lock()
             pygame.draw.polygon(screen,(255,100,100),[(x-9,y),(x,y+10),(x+9,y),(x,y-10)])
             if movex==0:
                 pygame.draw.circle(screen,(0,255,0),(x-4,y),3)
                 pygame.draw.circle(screen,(0,255,0),(x+4,y),3)
                 pygame.draw.circle(screen,(0,0,0),(x-4,y),1)
                 pygame.draw.circle(screen,(0,0,0),(x+4,y),1)
             elif movey==0:
                 pygame.draw.circle(screen,(0,255,0),(x,y-4),3)
                 pygame.draw.circle(screen,(0,255,0),(x,y+4),3)
                 pygame.draw.circle(screen,(0,0,0),(x,y-4),1)
                 pygame.draw.circle(screen,(0,0,0),(x,y+4),1)
             
             screen.unlock()

             if x in [newpos[0]-a for a in range(-9,10)]  and y in [newpos[1]-a for a in range(-9,10)]:
                 newpos=foodloc()
                 
                 pygame.display.update()
                 snakelength+=10
                 score+=1
                 speed+=1
                 pygame.display.update()
             pygame.display.update()
         
         if snakelist[0] in set(snakelist[1:]):
             k="DEAD"
             break
    gameoverscreen()
def gameoverscreen():
    font=pygame.font.SysFont(None,30)
    screen_text=font.render("GAME OVER",True,(255,0,0))
    screen.fill((255,255,255))
    screen.blit(screen_text,(200,250))
    screen_text2=font.render("RESTART (R) OR Q to quit",True,(255,0,0))
    screen.blit(screen_text2,(100,400))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    screen.fill((255,255,255))
                    pygame.display.update()
                    gameplay()
                    return None
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                    return None
        
                             
                     
                
                
gameplay()        

    
    

    
