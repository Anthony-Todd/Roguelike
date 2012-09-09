'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos
import Level
import UI
import DebugMenu
import pyglet
from pyglet.window import key

class Game( cocos.scene.Scene ):
    '''
    classdocs
    '''


    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        self.level = Level.Level(parent=self);
        self.ui    = UI.UI()
        super(Game, self).__init__()
        for l in [self.level, self.ui]:
            self.add(l)
        self.schedule(self.Update)
        self.enable_handlers(True)
    
    def Update(self,dt):
        pass
    
    def on_key_press( self, k , m ):
        print k, m
        if k == key.ENTER:
            cocos.director.director.push(DebugMenu.debugMenu)
        
