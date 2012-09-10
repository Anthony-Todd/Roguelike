'''
Created on Sep 9, 2012

@author: anthony
'''

from cocos.scene import Scene
from cocos.menu import Menu, EntryMenuItem, TOP, RIGHT
from cocos.director import director
from pyglet.window import key

import __builtin__
import sys

class Property( EntryMenuItem ):
    
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

class PropertyMenu( Menu ):
    
    PropertiesList = []
    
    def __init__( self, title=''):
        self.menu_valign = TOP
        self.menu_halign = RIGHT
        super( PropertyMenu, self ).__init__(title)
        self.menuItems = []
        
        self.AddObject(None, None)
        for prop in self.PropertiesList:
            self.AddObject(prop[0], prop[1])
        #item2= Property( Config.Configuration, 'PlayerSpeed')
        #self.create_menu( [item1, item2] )
        
    def AddObject(self, obj, key=None):
        if obj is not None:
            if key is None:
                for k in obj.__dict__.iterkeys():
                    if '__' in k:
                        pass
                    else:
                        self.menuItems.append( Property( obj, k ) )
            else:
                self.menuItems.append( Property( obj, key ) )
        self.create_menu( self.menuItems )
    
    def on_quit( self ):
        pass

def AppendProperty( obj, key = None ):
    PropertyMenu.PropertiesList.append( (obj, key) )

class DebugMenu(Scene):
    '''
    classdocs
    '''
    def __init__( self ):
        super( DebugMenu, self ).__init__()
        self.propMenu = PropertyMenu('Debug Menu')
        self.add( self.propMenu )
    
    def on_key_press( self, k , m ):
        print k, m
        if k is key.ESCAPE or k is key.F1:
            director.on_pop()
    
    def on_enter(self):
        print 'Debug Menu Push Handlers'
        director.window.push_handlers( self )
        super( Scene, self ).on_enter()
    
    def on_exit(self):
        print 'Debug Menu Remove Handlers'
        director.window.remove_handlers( self )
        super( Scene, self ).on_exit()