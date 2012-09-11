'''
Created on Sep 2, 2012

@author: anthony
'''
import Level
import UI
from DebugMenu import DebugMenu
from pyglet.window import key
from cocos.director import director
from cocos.scene import Scene
#from Input import g_keyboardState, g_mouseState

class Game( Scene ):
    '''
    classdocs
    '''
    isDebugMenu = False;

    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        
        super(Game, self).__init__()
        
        self.level = Level.Level(parent=self);
        self.ui    = UI.UI()
        
        for l in [self.level, self.ui]:
            self.add( l )
        
        self.schedule(self.Update)

    
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
    
    
        
