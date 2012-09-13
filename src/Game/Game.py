'''
Created on Sep 2, 2012

@author: anthony
'''

from CharacterSheet import DecodeCharacterSheet
from Config import Configuration
from DebugMenu import DebugMenu
import loadLevel

from pyglet.window import key

import cocos
from cocos.director import director
from cocos.scene import Scene
from cocos import actions, tiles, layer
from cocos.sprite import Sprite
import cocos.euclid as eu

class CharController(actions.Action, tiles.RectMapCollider):
    
    def step(self, dt):
        global keyboard, scroller, object_map

        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * Configuration.PlayerSpeed * dt
        dy = (keyboard[key.UP] - keyboard[key.DOWN]) * Configuration.PlayerSpeed * dt

        # get the player's current bounding rectangle
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy

        # run the collider
        #dx, dy = self.collide_map(object_map, last, new, dy, dx)
        
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
        
        # player position is anchored in the center of the image rect
        self.target.position = new.center

        # move the scrolling view to center on the player
        scroller.set_focus(*new.center)

class CharacterSprite(Sprite):

    def __init__(self, animations, defaultAnimation, position=(0,0), 
            rotation=0, scale=1, opacity=255, color=(255,255,255), anchor=None):

        self.animations = animations    
        super(CharacterSprite, self).__init__(animations[defaultAnimation], 
                position, rotation, scale, opacity, color, anchor)

class Character(layer.ScrollableLayer):
    
    def __init__(self, animationDict):
        super(Character, self).__init__()
        self.sprite = CharacterSprite(animationDict, 'idle_down')
        self.sprite.position = (30,30)
        self.add(self.sprite)
        self.sprite.do(CharController())
        self.sprite.cshape = cocos.collision_model.AARectShape(eu.Vector2(0.0, 0.0), 16, 16)


class Game(Scene):
    '''
    classdocs
    '''

    def __init__(self, *argv, **kwargv):        
        super(Game, self).__init__()
        self.schedule(self.Update)
        
        self.CharacterAnimations = {}
        
        self.CharacterAnimations.update(DecodeCharacterSheet('../assets/textures/Characters.json').animations)
        self.CharacterAnimations.update(DecodeCharacterSheet('../assets/textures/George.json').animations)
        
        #print self.CharacterAnimations
        
        global keyboard, scroller, object_map

        keyboard = key.KeyStateHandler()
        director.window.push_handlers(keyboard)
        
        scroller = layer.ScrollingManager()
        
        ## add other layers here
        tilemap = cocos.tiles.load('../assets/level0.tmx')
        
        scroller.add(tilemap['background0'], z=0)
        scroller.add(tilemap['background1'], z=1)
                 
        object_layer = loadLevel.CollisionLayer(tilemap['blocks0'])
        scroller.add(object_layer, z=2)

        self.player = Character(self.CharacterAnimations['george'])
        scroller.add(self.player, z=3)
        
        self.add(scroller)
    
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
    
    
        
