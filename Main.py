"""setup"""
import pygame
from pygame import *
import sys
pygame.init()
screen = pygame.display.set_mode( (680,480) )
pygame.display.set_caption("TheLittleBlackBox 2.0")
img = pygame.image.load("C:/Python34/TheLittleBlackBox_2.0/Images/BlackBoxIcon.png")
icon = pygame.transform.scale(img, (32,32) )
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
bullets = []
XplusCycle = []
"""functions"""
def updateAll(array):
    #redraws everything
    screen.fill( (0,0,0) )
    screen.fill( (white) )
    for i in array:
	    i = pygame.draw.rect(screen,black,i)
    pass;
def upb(array):
    #screen.fill( (0,0,0) )
    for i in bullets:
        """
        print(i)
        print(i.x)
        print(i.y)
        print(i.width)
        print(i.height)
        """
        i = AAfilledRoundedRect(screen, (i.x,i.y,i.width,i.height) , (i.color) ,i.radius)
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
        ny = (height/2) + (y * -1)
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
def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)
def firebullet(power,velocity,startx,starty,direction):
    global plusCycle
    global bullets
    ThisBullet = bullet(power,startx,starty,direction)
    if direction == "E":
        XplusCycle.append(ThisBullet)
        bullets.append(ThisBullet)
"""object constructors"""
class bullet:
    'Game Bullet'
    x = None
    y = None
    height = None
    width = None
    color = None
    radius = None
    def __init__ (self,power,startx,starty,direction):
        #Making the rectangle/circle
        if direction == "E":
            AAfilledRoundedRect(screen, (cx(startx),cy(starty),30,3) , (red) ,0.5)
            bullet.x = startx
            bullet.y = starty
            bullet.height = 3
            bullet.width = 30
            bullet.color = red
            bullet.radius = 0.5
        print('made')
    def check(self):
        if self.x > pygame.Surface.get_width(screen):
            del XplusCycle[XplusCycle.index(self)]
            del bullets[bullets.index(self)]
class Velocity:
    #velocity
    v = 0
    #velocity counter
    vc = 0
    #velocity up counter
    vupc = 0
    #velocity down counter
    vdownc = 0
    #The delay between increasing the velocity
    vwait = None
    def __init__(self,waitIn):
        Velocity.wait = waitIn
class player:
    health = None
    RECT = None
    x = None
    y = None
    weapons = {
        "power" : None
        }
    def __init__(self,healthIn,rectIn,powerIn):
        self.health = healthIn
        self.RECT = rectIn
        self.x = self.RECT.x
        self.y = self.RECT.y
        self.weapons["power"] = powerIn
    def shoot(self):
        firebullet(self.weapons["power"],1,myrect.x,myrect.y,"E")
"""special values"""
#draw it just like in the original 'TheLittleBlackBox' game.
myrect = pygame.draw.rect(screen,black, (cx(0),cy(0),15,15) )
elements.append(myrect)
newx = cx(0)
newy = cy(0)
print("x: " + str(bullet.x) + " y: " + str(bullet.y) + " height: " + str(bullet.height) + " width: " + str(bullet.width) + " color:" + str(bullet.color) + " radius: " + str(bullet.radius))
firebullet(1,1,0,0,"E")
player = player(3,myrect,2)
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
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    """physics engine/events"""
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
    #print("Vx: " + str(velocity) + " Vy: " + str(velocityY) )
    clock.tick(1500)
    """update stuff"""
    chvx()
    chvy()
    """refresh"""
    screen.fill( black )
    newx += velocity
    newy += velocityY
    for i in XplusCycle:
        i.check()
        i.x = i.x + 9
    """redrawing"""
    myrect = pygame.draw.rect(screen,green, (newx,newy,15,15) )
    upb(bullets)
    """logging"""
    #print("x: " + str(bullet.x) + " y: " + str(bullet.y) + " height: " + str(bullet.height) + " width: " + str(bullet.width) + " color:" + str(bullet.color) + " radius: " + str(bullet.radius))
    #print("x: " + str(bullet.x) + " y: " + str(bullet.y) + " height: " + str(bullet.height) + " width: " + str(bullet.width) + " color:" + str(bullet.color) + " radius: " + str(bullet.radius))
    """Final - Update"""
    pygame.display.update()
