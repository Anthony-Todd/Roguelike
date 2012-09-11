'''
Created on Sep 3, 2012

@author: anthony
'''
from Entity import Entity
from Components.Rendered_Component import RenderedSpriteComponent
from Components.Input_Component import InputComponent

def Create_Spirte(image, pos):
    compSprite = RenderedSpriteComponent(image=image, position=pos)
    return Entity(Components=(compSprite))

def Create_AnimatedSprite( animations, defaultAnimation, pos=(0,0)):
    compSprite = RenderedSpriteComponent( animations=animations, defaultAnimation=defaultAnimation, position=pos)
    return Entity( Components=(compSprite) )

def test(*arg):
    print 'test:', arg

def Create_TestInput( on_key ):
    return Entity( Components=InputComponent(key_press=test, key_release=test, mouse_motion=test) )