import time

import pygame
import numpy as np
from gamejam7.card import card
import random
N = 4
value_list1=["\u222B0 dx","\u222B1 dx","\u222Bk dx","\u222Be^x dx","\u222Be^(-x) dx","\u222Bsin(x) dx","\u222Bcos(x) dx","\u222Bsinh(x) dx"]
value_list2=["C","x+C","kx+C","e^x+C","-e^(-x)+C","-cos(x)+C","sin(x)+C","cosh(x)+C"]
value_list=value_list1+value_list2
restore=value_list
card_list=[]
score_comp=0
score_player=0

"""for i in range(N*N //2):
    value_list.append(str(i))
    value_list.append(str(i))"""

for i in range(N):
    for j in range(N):
        temp=random.choice(value_list)
        card_list.append(card(i*190+20,j*190+20,temp))
        value_list.remove(temp)
value_list=value_list1+value_list2
def check(a,b):
    c=value_list.index(a)
    d=value_list.index(b)
    if c+8==d or d+8==c:
        return True
    else:
        return False



current_content1 =""
current_content2 =""
current_count=0

pygame.init()
screen = pygame.display.set_mode((800,800))
s1 = pygame.image.load("gamejam7/png/av.png")
surf1=pygame.surfarray.make_surface(np.full((800,800,3),(50,50,50)))
font = pygame.font.Font('freesansbold.ttf', 20)
Running=True


text = font.render("Grzegorz Gaming proudly presents:", True, (255, 255, 255), (50, 50, 50))
screen.blit(surf1, (0, 0))
screen.blit(text, (230, 200))
screen.blit(s1, (300, 300))
pygame.display.flip()
time.sleep(2)
screen.blit(surf1, (0, 0))
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render("Memory Game", True, (255, 255, 255), (50, 50, 50))
screen.blit(text, (250, 300))
pygame.display.flip()
time.sleep(2)
font = pygame.font.Font('freesansbold.ttf', 15)
Flag=True
end=False
while Running:

    screen.blit(surf1, (0, 0))
    end=True
    for i in card_list:
        i.display(screen,font)
        if i.state != 2:
            end=False
    for i in card_list:
        if current_count==2 and i.state!=2:
            if check(current_content1,current_content2):
                card_list[content_num1].hide()
                card_list[content_num2].hide()
                if Flag:
                    score_player=score_player+1
                else:
                    score_comp=score_comp+1

            else:
                card_list[content_num1].turnback()
                card_list[content_num2].turnback()
                Flag=not Flag


            current_content2=""
            current_content1="something else"
            current_count=3
    if end==True:
        screen.blit(surf1, (0, 0))
        text = font.render("your score "+str(score_player), True, (255, 255, 255), (50, 50, 50))
        screen.blit(text, (250, 300))
        text = font.render("comp score: "+str(score_comp), True, (255, 255, 255), (50, 50, 50))
        screen.blit(text, (250, 500))
    pygame.display.flip()
    if current_count==3:
        time.sleep(1)
        current_count=0



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0] == True:
            a= pygame.mouse.get_pos()
            num=0
            if Flag == False:
                temp_list = []
                for i in card_list:
                    if i.state == 0:
                        temp_list.append(i)
                if len(temp_list)>0:
                    res = random.choice(temp_list)
                    a=(res.x+1,res.y+1)

            for i in card_list:
                control=i.check_click(a[0],a[1])
                if control == True:
                    current_count=current_count+1

                    if current_count==1:
                        current_content1=i.content
                        content_num1= num
                    else:
                        current_content2=i.content
                        content_num2 = num
                num=num+1




