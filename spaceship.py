"""
Spaceship game
"""
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
FRICTION = 0.99
started = False
coeff = 1

class ImageInfo:
    """Class for sotring info abou images"""
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    """Information about ship"""
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0.0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.ship_acc = [0, 0]
        
    def draw(self,canvas):	
        if self.thrust == False:
            canvas.draw_image(self.image, self.image_center,
                              self.image_size, self.pos,
                              self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] ,
                              self.image_size, self.pos,
                              self.image_size, self.angle)
            

    def update(self):
        self.angle += self.angle_vel
        
        ship_vector = angle_to_vector(self.angle)
        self.vel[0] = (self.vel[0] + self.ship_acc[0] * ship_vector[0]) * FRICTION
        self.vel[1] = (self.vel[1] + self.ship_acc[1] * ship_vector[1]) * FRICTION
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
    
    def update_thrust_status(self, thrust):
            self.thrust = thrust
            if self.thrust:
                ship_thrust_sound.play()
            else:
                ship_thrust_sound.pause()
                
    def shoot(self):
        global missile_group
        v = 10
        vel = [v, v]
        pos = [0, 0]
        ship_vector = angle_to_vector(self.angle)
        pos[0] = self.pos[0] + self.radius * ship_vector[0]
        pos[1] = self.pos[1] + self.radius * ship_vector[1]
        
        vel[0] = self.vel[0] + vel[0] * ship_vector[0]
        vel[1] = self.vel[1] + vel[1] * ship_vector[1]
        missile = Sprite(pos, vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(missile)

    
    def handle_key(self, key, direction):
        angle_vel = 0.09
        angle_keys = {"right": {"down": angle_vel, "up": 0},
                      "left": {"down": -angle_vel, "up": 0}}
        for i in angle_keys:
            if key == simplegui.KEY_MAP[i]:
                self.angle_vel = angle_keys[i][direction]
                #print (self.vel, self.ship_acc)
                
        acc = 0.5
        thrust_key = {"up": {"down": [acc, True], "up": [0, False]}}
        for i in thrust_key:
            if key == simplegui.KEY_MAP[i]:
                self.ship_acc = [thrust_key[i][direction][0],
                                 thrust_key[i][direction][0]]
                #self.thrust = thrust_key[i][direction][1]
                self.update_thrust_status(thrust_key[i][direction][1])
        if key == simplegui.KEY_MAP["space"] and direction== "down":
            self.shoot()
            
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
                
    
# Sprite class
class Sprite:
    """Information about sprites"""
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
             canvas.draw_image(self.image, [self.image_center[0] + self.age * self.image_size[0], self.image_center[1]],
                          self.image_size, self.pos,
                          self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center,
                          self.image_size, self.pos,
                          self.image_size, self.angle)
    
    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        self.angle += self.angle_vel
        
        self.age += 1
        return self.age >= self.lifespan
        
    def collide(self, other_sprite):
        return dist(self.pos, other_sprite.get_pos()) <= self.radius + other_sprite.get_radius()
             
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

           
def draw(canvas):
    global time, lives, score, started, rock_group, missile_group, coeff, explosion_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    

    # draw ship and sprites
    
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    
    
    if group_collide(rock_group, my_ship):
        lives -= 1
        if lives <= 0:
            started = False
            timer.stop()
            soundtrack.pause()
            soundtrack.rewind()
            score = 0
            lives = 3
            rock_group = set([])
            missile_group = set([])
            
    score += group_group_collide(missile_group, rock_group)
    coeff = 1 + score * 0.05
        
    canvas.draw_text(str(lives), [30,70], 60, "Gray", "monospace")
    canvas.draw_text(str(score), [WIDTH - 70,70], 60, "Gray", "monospace")
    my_ship.draw(canvas)
    process_sprite_group(explosion_group, canvas)
    # update ship and sprites
    my_ship.update()
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    speed = [(random.random() * 6 - 3) * coeff , (random.random() * 6 - 3) * coeff]
    angle_speed = random.random() / 20 - 0.1
    if len(rock_group) <= 12 and dist(pos, my_ship.get_pos()) >= my_ship.get_radius() + asteroid_info.get_radius() +60: 
        rock = Sprite(pos, speed, 0, angle_speed,
                   asteroid_image, asteroid_info)
        rock_group.add(rock)
        
def group_collide(group, other_object):
    res = False
    for obj in set(group):
        if obj.collide(other_object):
            res = True
            group.remove(obj)
            explosion = Sprite(other_object.get_pos(), [0, 0], 0, 0, explosion_image, explosion_info)
            explosion_sound.play()
            explosion_group.add(explosion)
    return res
    
def group_group_collide(group1, group2):
    global explosion_group
    i = 0
    for item in set(group1):
        if group_collide(group2, item):
            i += 1
    return i
        
    
def process_sprite_group(sprites, canvas):
    for sprite in set(sprites):
        sprite.draw(canvas)
        if sprite.update():
            sprites.remove(sprite)
        
    
def down_key_handler(key):
    my_ship.handle_key(key, "down")

def up_key_handler(key):
    my_ship.handle_key(key, "up")
    
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        timer.start()
        soundtrack.play()
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(down_key_handler)
frame.set_keyup_handler(up_key_handler)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_mouseclick_handler(click)

# get things rolling
#timer.start()
frame.start()