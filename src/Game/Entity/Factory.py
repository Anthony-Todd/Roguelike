'''
Created on Sep 3, 2012

@author: anthony
'''
from Entity import Entity
from Components.Rendered_Component import RenderedSpriteComponent

def Create_Spirte(image, pos):
    compSprite = RenderedSpriteComponent(image=image, position=pos)
    return Entity(Components=(compSprite))

def Create_AnimatedSprite( animations, defaultAnimation, pos=(0,0)):
    compSprite = RenderedSpriteComponent( animations=animations, defaultAnimation=defaultAnimation, position=pos)
    return Entity( Components=(compSprite) )