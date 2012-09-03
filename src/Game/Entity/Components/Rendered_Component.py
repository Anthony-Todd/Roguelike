'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos import sprite
from Component import Component

from Managers import Manager

g_RenderSpriteManager = Manager.Manager()

class RenderedSpriteComponent( Component ):
    '''
    classdocs
    '''
    
    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        global g_RenderSpriteManager
        g_RenderSpriteManager.components.append(self)
        image = kwargv.get('image')
        if kwargv.has_key('position'):
            position = kwargv.get('position')
        else:
            position = (0,0)
        self.sprite = sprite.Sprite(image, position)
    
    def __del__(self):
        global g_RenderSpriteManager
        g_RenderSpriteManager.components.remove(self)
    
    def Update( self, dt ):
        pass
    
    def SetEntity(self, entity):
        print 'Chiled'
        entity.add( self.sprite )
        
