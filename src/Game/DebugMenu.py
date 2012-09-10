'''
Created on Sep 9, 2012

@author: anthony
'''

import cocos.layer
from pyglet.window import key
import Config
import __builtin__
import sys
class Property( cocos.menu.EntryMenuItem ):
    
    def __init__(self, obj, key):
        self.key = key
        self.obj = obj
        value = self.obj.__dict__[self.key]
        self.valueType = value.__class__.__name__
        print self.valueType
        super(Property, self).__init__(key+':', self.on_entry_callback, str(value), max_length=64)
    
    def on_entry_callback(self, value):
        print value
        try:
            type_ = getattr(__builtin__,self.valueType )
            typedValue = type_(value)
            setattr(self.obj, self.key, typedValue);
        except:
            print "Unexpected error:", sys.exc_info()[0]

class PropertyMenu( cocos.menu.Menu ):
    
    def __init__( self, title=''):
        super( PropertyMenu, self ).__init__(title)
        self.menuItems = []
        
        self.AddObject(Config.Configuration, None)
        
        #item2= Property( Config.Configuration, 'PlayerSpeed')
        #self.create_menu( [item1, item2] )
        
    def AddObject(self, obj, key=None):
        if key is None:
            for k in obj.__dict__.iterkeys():
                if '__' in k:
                    pass
                else:
                    self.menuItems.append( Property( obj, k ) )
        self.create_menu( self.menuItems )
                
        
class DebugMenuLayer(cocos.layer.Layer):
    def __init__(self, gameScene):
        self.game = gameScene
        super(DebugMenuLayer, self).__init__()
        self.is_event_handler = True
    
    def on_key_press( self, k , m ):
        self.game.on_key_press(k,m)

class DebugMenu(cocos.scene.Scene):
    '''
    classdocs
    '''


    def __init__( self ):
        super( DebugMenu, self ).__init__()
        self.layer = DebugMenuLayer(self)
        self.layer.add( PropertyMenu('Debug Menu'), (0,640) )
        self.add( self.layer )
    
    def on_key_press( self, k , m ):
        print k, m
        if k is key.F1:
            cocos.director.director.pop()
debugMenu = DebugMenu()