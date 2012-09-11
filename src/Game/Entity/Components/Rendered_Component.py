'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos import sprite
from Component import Component

from Managers import Manager

g_RenderSpriteManager = Manager()

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
        
        #super(Component, self).__init__(isUnique=False)
        Component.__init__(self,isUnique=False)
        image = None
        self.animations = {}
        self.sprite = None
        position = (0,0)
        if 'position' in kwargv:
            position = kwargv['position']
        if 'animations' in kwargv:
            self.animations = kwargv['animations']
        if 'image' in kwargv:
            image = kwargv.get('image')
        if 'defaultAnimation' in kwargv:
            default = kwargv.get('defaultAnimation')
            if default in self.animations:
                self.sprite = sprite.Sprite(self.animations[default], position)
        else:
            self.sprite = sprite.Sprite(image, position)
        
        if self.entity is not None:
            self.SetEntity(self.entity)
    
    def __del__(self):
        global g_RenderSpriteManager
        g_RenderSpriteManager.components.remove(self)
    
    def Update( self, dt ):
        pass
    
    def SetEntity(self, entity):
        self.entity = entity
        if self.sprite is not None:
            entity.add( self.sprite )
    
    def SetAnimations(self, **animations):
        self.animations = animations
    
    def Play(self, key):
        if key in self.animations:
            self.sprite.setImage( self.animations[key] )
        
