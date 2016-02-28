"""setup"""
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode( (680,480) )
pygame.display.set_caption("TheLittleBlackBox 2.0")
img = pygame.image.load("C:/Python34/TheLittleBlackBox_2.0/Images/BlackBoxIcon.png")
icon = pygame.transform.scale(img, (16,16) )
pygame.display.set_icon(icon)
screen.fill( (0,0,0) )
"""values : loop"""
running = True
clock = pygame.time.Clock()
"""values : colors"""
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
"""values : Physics"""
velocity = 0
velocityY = 0
vcounter = 0
vYcounter = 0
vupcounter = 0
vdowncounter = 0
vYucounter = 0
vYdcounter = 0
elements = []
"""functions"""
def updateAll(array):
    #redraws everything
    screen.fill( (0,0,0) )
    screen.fill( (white) )
    for i in array:
	    i = pygame.draw.rect(screen,black,i)
    pass;
def chvx():
    #updates the velocity so it decelerates (acceleration is in the game loop.
    global velocity
    global vcounter
    vcounter+= 1
    if vcounter == 15:
        velocity = int(velocity/2 + velocity/4)
        vcounter = 0
    pass;
def chvy():
    #updates <Y> velocity so it decelerates.
    global velocityY
    global vYcounter
    vYcounter+=1
    if vYcounter == 15:
        velocityY = int(velocityY/2 + velocityY/4)
        vYcounter = 0
    pass;
def cx(x):
        #cx stands for convert x. It's my solution for converting (0,0) in the screen.
        width = pygame.Surface.get_width(screen)
        nx = (width/2) + x
        return nx;
def cy(y):
        #cy stands for convert y. It's my solution for converting (0,0) in the screen.
        height = pygame.Surface.get_height(screen)
        ny = (height/2) + y
        return ny;
def MoveRect(x,y,obj):
        global myrect
        print(myrect)
        #-1 so we have a 4 quadrent graph going.
        newobj = obj.move(x,y * -1)
        newobj = pygame.draw.rect(screen,black,newobj)
        elements[elements.index(obj)] = newobj
        myrect = newobj
        #print("new " + str(newobj))
        #print("old " + str(myrect))
        pass;
"""special values"""
#draw it just like in the original 'TheLittleBlackBox' game.
myrect = pygame.draw.rect(screen,black, (cx(0),cy(0),15,15) )
elements.append(myrect)
newx = cx(0)
newy = cy(0)
"""game loop"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type== pygame.VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            #screen.blit(pygame.transform.scale(pic,event.dict['size']),(0,0))
            pygame.display.flip()
    """physics engine"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        vupcounter+= 1
        if vupcounter > 8:
            velocity += 1
            vupcounter = 0
    if keys[pygame.K_a]:
        vdowncounter+=1
        if vdowncounter > 8:
            velocity -= 1
            vdowncounter = 0
    if keys[pygame.K_s]:
        vYucounter+=1
        if vYucounter > 8:
            velocityY += 1
            vYucounter = 0
    if keys[pygame.K_w]:
        vYdcounter+=1
        if vYdcounter > 8:
            velocityY -= 1
            vYdcounter = 0
    print("Vx: " + str(velocity) + " Vy: " + str(velocityY) )
    clock.tick(1200)
    chvx()
    chvy()
    """refresh"""
    screen.fill( black )
    newx += velocity
    newy += velocityY
    myrect = pygame.draw.rect(screen,green, (newx,newy,15,15) )
    pygame.display.update()
