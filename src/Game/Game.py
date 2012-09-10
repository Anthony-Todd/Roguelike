'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos.layer
import Level
import UI
import DebugMenu
from pyglet.window import key

class GameLayer(cocos.layer.Layer):
    def __init__(self, gameScene):
        self.game = gameScene
        super(GameLayer, self).__init__()
        self.is_event_handler = True
    
    def on_key_press( self, k , m ):
        self.game.on_key_press(k,m)

class Game( cocos.scene.Scene ):
    '''
    classdocs
    '''

    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        super(Game, self).__init__()
        
        self.level = Level.Level(parent=self);
        self.ui    = UI.UI()
        self.gameLayer = GameLayer(self)
        
        for l in [self.level, self.ui,self.gameLayer]:
            self.add(l)
        
        self.schedule(self.Update)
    
    def Update(self,dt):
        pass
    
    def on_key_press( self, k , m ):
        print k, m
        if k == key.F1:
            cocos.director.director.push(DebugMenu.debugMenu)
        
