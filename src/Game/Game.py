'''
Created on Sep 2, 2012

@author: anthony
'''
from DebugMenu import DebugMenu
from pyglet.window import key
from cocos.director import director
from cocos.scene import Scene
from cocos import cocosnode, actions, tiles, layer
from cocos.sprite import Sprite

from CharacterSheet import DecodeCharacterSheet
from CodeWarrior.CodeWarrior_suite import target

#from Input import g_keyboardState, g_mouseState

class CharController(actions.Action, tiles.RectMapCollider):
    MOVE_SPEED = 200
    
    def step(self, dt):
        global keyboard, scroller, object_map

        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * self.MOVE_SPEED *dt
        dy = (keyboard[key.UP] - keyboard[key.DOWN]) * self.MOVE_SPEED *dt

        # get the player's current bounding rectangle
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy
        # run the collider
        #dx, dy = self.collide_map(object_map, last, new, dy, dx)
        
        # player position is anchored in the center of the image rect
        self.target.position = new.center

        # move the scrolling view to center on the player
        scroller.set_focus(*new.center)

class Character( layer.ScrollableLayer ):
    
    def __init__(self, animationDict):
        super(Character, self).__init__()
        self.animations = animationDict
        self.sprite = Sprite( self.animations['idle_down'] )
        self.sprite.position = (30,30)
        self.add(self.sprite)
        self.sprite.do(CharController())


class Game( Scene ):
    '''
    classdocs
    '''

    def __init__( self, *argv, **kwargv ):        
        super(Game, self).__init__()
        self.schedule(self.Update)
        
        self.CharacterAnimations = {}
        
        self.CharacterAnimations.update( DecodeCharacterSheet('../assets/textures/Characters.json').animations )
        self.CharacterAnimations.update( DecodeCharacterSheet('../assets/textures/George.json').animations )
        
        print self.CharacterAnimations
        
        global keyboard, scroller, object_map
        
        keyboard = key.KeyStateHandler()
        director.window.push_handlers(keyboard)
        
        object_map = None # for now
        
        scroller = layer.ScrollingManager()
        ## add other layers here
        self.player = Character( self.CharacterAnimations['george'] )
        scroller.add( self.player )
        self.add(scroller)
    
    def on_key_press( self, k , m ):
        if k is key.F1:
            director.push( DebugMenu() )

    def on_enter(self):
        print 'Debug Menu Push Handlers'
        director.window.push_handlers( self )
        super( Scene, self ).on_enter()
    
    def on_exit(self):
        print 'Debug Menu Remove Handlers'
        director.window.remove_handlers( self )
        super( Scene, self ).on_exit()
    
    def Update(self,dt):
        pass
    
    
        
