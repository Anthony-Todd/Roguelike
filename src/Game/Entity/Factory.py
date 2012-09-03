'''
Created on Sep 3, 2012

@author: anthony
'''
from Entity import Entity
from Components.Rendered_Component import RenderedSpriteComponent
def Create_Spirte( image, pos ):
    compSprite = RenderedSpriteComponent( image=image, position=pos )
    print type( compSprite )
    return Entity(Components=( compSprite ))