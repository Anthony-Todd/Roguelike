'''
Created on Sep 2, 2012

@author: anthony
'''

from CharacterSheet import DecodeCharacterSheet
from Config import Configuration as Conf
from DebugMenu import DebugMenu
import loadLevel

from pyglet.window import key

import cocos.collision_model
from cocos.director import director
from cocos.scene import Scene
import cocos.euclid as eu

ox = 300  # player starting positions
oy = 100  # TODO set starting position using tmx map

cm = cocos.collision_model.CollisionManagerGrid(0, Conf.MapWidth * Conf.TileSize,
                                                0, Conf.MapHeight * Conf.TileSize,
                                                Conf.TileSize * 1.25,
                                                Conf.TileSize * 1.25)

class CharController(cocos.actions.Action):

    def step(self, dt):
        global keyboard, scroller

        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * Conf.PlayerSpeed * dt
        dy = (keyboard[key.UP] - keyboard[key.DOWN]) * Conf.PlayerSpeed * dt
        
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy

        # run the collider
        cols = check_collisions(new)

        if len(cols) == 0:
            # fetch character movement animations
            if dx < 0.1 and dx > -0.1 and dy < 0.1 and dy > -0.1:
                if self.target.image is not self.target.animations['idle_down']:
                    self.target.image = self.target.animations['idle_down']
            elif dx > 0.0:
                if self.target.image is not self.target.animations['walk_right']:
                    self.target.image = self.target.animations['walk_right']
            elif dx < 0.0:
                if self.target.image is not self.target.animations['walk_left']:
                    self.target.image = self.target.animations['walk_left']
            elif dy > 0.0:
                if self.target.image is not self.target.animations['walk_up']:
                    self.target.image = self.target.animations['walk_up']
            elif dy < 0.0:
                if self.target.image is not self.target.animations['walk_down']:
                    self.target.image = self.target.animations['walk_down']
        
            # move character
            self.target.position = new.center

            # move the scrolling view to center on the player
            scroller.set_focus(*new.center)


class CharacterSprite(cocos.sprite.Sprite):

    def __init__(self, animations, defaultAnimation, position=(0,0), 
            rotation=0, scale=1, opacity=255, color=(255,255,255), anchor=None):

        self.animations = animations    
        super(CharacterSprite, self).__init__(animations[defaultAnimation], 
                position, rotation, scale, opacity, color, anchor)

class Character(cocos.layer.ScrollableLayer):
    
    def __init__(self, animationDict):
        super(Character, self).__init__()
        self.sprite = CharacterSprite(animationDict, 'idle_down')
        self.sprite.position = (ox,oy)
        self.add(self.sprite)
        self.sprite.do(CharController())
        self.sprite.cshape = cocos.collision_model.AARectShape(eu.Vector2(0.0, 0.0), 16, 16)

def check_collisions(rect):
    return cm.objs_into_box(rect.left, rect.right, rect.bottom, rect.top)

class Game(Scene):
    '''
    classdocs
    '''

    def __init__(self, *argv, **kwargv): 
        global keyboard, scroller, cm

        super(Game, self).__init__()
        self.schedule(self.Update)
        
        self.CharacterAnimations = {}
        
        self.CharacterAnimations.update(DecodeCharacterSheet('../assets/textures/Characters.json').animations)
        self.CharacterAnimations.update(DecodeCharacterSheet('../assets/textures/George.json').animations)
        
        keyboard = key.KeyStateHandler()
        director.window.push_handlers(keyboard)
        
        scroller = cocos.layer.ScrollingManager()
                
        ## add layers here
        tilemap = cocos.tiles.load('../assets/level0.tmx')
        layers, cm = loadLevel.load_level(tilemap, cm)
        
        topz=0
        for l in layers:
            scroller.add(l,z=topz)
            topz += 1

        self.player = Character(self.CharacterAnimations['george'])
        scroller.add(self.player, z=topz)
        
        self.add(scroller,z=0)
    
    def on_key_press(self, k, m):
        if k is key.F1:
            director.push(DebugMenu())

    def on_enter(self):
        print 'Debug Menu Push Handlers'
        director.window.push_handlers(self)
        super(Scene, self).on_enter()
    
    def on_exit(self):
        print 'Debug Menu Remove Handlers'
        director.window.remove_handlers(self)
        super(Scene, self).on_exit()
    
    def Update(self,dt):
        pass
    
    
        
