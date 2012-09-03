'''
Created on Sep 2, 2012

@author: anthony
'''

from cocos import sprite
from Component import Component

class RenderedSpriteComponent( Component ):
    '''
    classdocs
    '''
    
    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        image = kwargv.get('image')
        if kwargv.has_key('position'):
            position = kwargv.get('position')
        else:
            position = (0,0)
        self.sprite = sprite.Sprite(image, position)
    
    def Update( self, dt ):
        pass
    
    def SetEntity(self, entity):
        print 'Chiled'
        entity.add( self.sprite )