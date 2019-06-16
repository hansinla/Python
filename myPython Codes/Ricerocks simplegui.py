# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = [WIDTH, HEIGHT]
score = 0
lives = 3
time = 0.5
started = False

class ImageInfo:
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
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

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

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_center[0] + int(self.thrust) * self.image_size[0] , self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)

    def shoot(self):
        global missile_group
        vector = angle_to_vector(my_ship.angle)
        a_missile = Sprite([self.pos[0] + vector[0] * self.radius, self.pos[1]+vector[1] * self.radius], [self.vel[0] + vector[0]*5, self.vel[1] + vector[1]*5], self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        
    def update(self):
        self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)
        # wrap around space
        self.pos = screen_wrap(self.pos, self.radius)
        
        for i in range (2):
            # update ship position
            self.pos[i] += self.vel[i]
            # update velocity (friction)
            self.vel[i] *= 0.95
            # update velocity (thrust)
            if self.thrust:
                self.vel[i] += forward[i] * 0.5
            
# Sprite class
class Sprite:
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
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        # wrap around space
        self.pos = screen_wrap(self.pos, self.radius)
        # update sprite position
        if self.animated:
            self.image_center[0] =  self.image_center[1] + self.age * self.image_size[0] 
        for i in range (2):
            # update sprite position
            self.pos[i] += self.vel[i]
        # update age
        self.age += 1
        # delete this object if age > lifespan
        if self.age > self.lifespan:
            return True
        else:
            return False
        
        
    def collide(self, other_object):
        if dist(self.pos, other_object.pos) <= self.radius + other_object.radius:
            return True
        else:
            return False

        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        soundtrack.rewind()
        soundtrack.play()
            
            
def draw(canvas):
    global time, lives, score, rock_group, started
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw and update ship
    my_ship.draw(canvas)
    my_ship.update()
    
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosions_group, canvas)
    
    score += group_group_collide(rock_group, missile_group)
    lives -= group_collide(rock_group, my_ship)
    
    if lives < 1:
        started = False
        rock_group = set ([])
        soundtrack.pause()

    # display scores
    canvas.draw_text("Lives", (80, 25), 30, "White", "monospace")
    canvas.draw_text("Score", (580, 25), 30, "White", "monospace")
    canvas.draw_text(str(lives), (200, 25), 30, "White", "monospace")
    canvas.draw_text(str(score), (700, 25), 30, "White", "monospace")
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
                   
def process_sprite_group(group, canvas):
    # draw and update sprites if they exist
    if len(group) > 0:
        copy_group = set(group)
        for sprite in copy_group:
            sprite.draw(canvas)
            # delete this object if age > lifespan
            if sprite.update():
                group.discard(sprite)

def group_collide(group, other_object):
    collisions = 0
    copy_group = set(group)
    for item in copy_group:
        if item.collide(other_object):
            # trigger explosion
            explosion(item.pos, item.vel)
            group.discard(item)
            collisions += 1
    return collisions

def group_group_collide(rockgroup, missilegroup):
    collisions = 0
    copy_missilegroup =  set(missilegroup)
    for item in copy_missilegroup:
        control = 0
        control += group_collide(rockgroup, item)
        collisions += control
        if control > 0:
            missilegroup.discard(item)
    return collisions

def explosion(pos, vel):
    explosion_sound.rewind()
    explosion_sound.play()
    explode = Sprite(pos, vel, 0, 0, explosion_image, explosion_info)
    explosions_group.add(explode)


            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    
    if started:
        if len(rock_group) <= 12:
            # create a random position
            pos = [random.randint(0, WIDTH),random.randint(0, HEIGHT)]
            # create random velocity
            vel = [random.randint(0, 4) - 2, random.randint(0, 4) - 2]
            # if necessary; create a new random rock position far enough away from my_ship
            while dist(my_ship.pos, pos) <= my_ship.radius * 3:
                pos[0] = random.randint(0, WIDTH)
                pos[1] = random.randint(0, WIDTH)
            # create random angular velocity    
            ang_vel = (random.randint(0, 10) -  5) / 60
            # create rock and add it to rock_group
            new_rock = Sprite(pos, vel, 0, ang_vel, asteroid_image, asteroid_info)
            rock_group.add(new_rock)
        
def keydown(key):
    for i in press:
        if key == simplegui.KEY_MAP[i]:
            press[i]()
            
def keyup(key):
    for i in release:
        if key == simplegui.KEY_MAP[i]:
            release[i]()
            
def thrust():
    my_ship.thrust = True
    ship_thrust_sound.play()
    
def nothrust():
    my_ship.thrust = False
    ship_thrust_sound.pause()
    ship_thrust_sound.rewind()
    
def rotate_left():
    my_ship.angle_vel =  -0.1

def rotate_right():
    my_ship.angle_vel =  0.1
    
def rotation_stop():
    my_ship.angle_vel =  0
    
def shoot():
    my_ship.shoot()

def screen_wrap(pos, radius): # Not using % because this solution is smoother
    for i in range(2):
        if pos[i] - radius > SCREEN_SIZE[i]:
            pos[i] -= SCREEN_SIZE[i] + 2 * radius
        if pos[i] + radius < 0:
            pos[i] += SCREEN_SIZE[i] + 2 * radius
    return pos    

press = {"up": thrust, "left": rotate_left, "right": rotate_right, "space": shoot}
release = {"up": nothrust, "left": rotation_stop, "right": rotation_stop}
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosions_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)


timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
