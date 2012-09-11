'''
Created on Sep 11, 2012

@author: anthony
'''
from Component import Component
from Managers import Manager
from cocos.director import director

g_InputManager = Manager()

class InputComponent( Component ):
    
    def __init__(self, key_press=None, key_release=None, mouse_motion=None,
                 mouse_press=None, mouse_release=None, mouse_drag=None,
                 mouse_enter=None, mouse_leave=None, mouse_scroll=None ):
        self.key_press_function = key_press
        self.key_release_function = key_release
        self.mouse_motion_function = mouse_motion
        self.mouse_press_function = mouse_press
        self.mouse_release_function = mouse_release
        self.mouse_drag_function = mouse_drag
        self.mouse_enter_function = mouse_enter
        self.mouse_leave_function = mouse_leave
        self.mouse_scroll_function = mouse_scroll
        super( InputComponent, self ).__init__( isUnique=True )
        global g_InputManager
        g_InputManager.components.append(self)
        director.window.push_handlers(self)
        
    def __del__(self):
        global g_InputManager
        g_InputManager.components.remove(self)
        director.window.remove_handler(self)

    def Update(self,dt):
        pass

    def on_key_press( self, k , m ):
        if self.key_press_function is not None:
            self.key_press_function( self.entity, k, m )
        
    def on_key_release( self, k, m ):
        if self.key_release_function is not None:
            self.key_release_function( self.entity, k, m )

    def on_mouse_motion( self, x, y, dx, dy ):
        if self.mouse_motion_function is not None:
            self.mouse_motion_function(self.entity, x, y, dx, dy)
    
    def on_mouse_press( self, x, y, button, modifiers ):
        if self.mouse_press_function is not None:
            self.mouse_press_function( self.entity, x, y, button, modifiers )
    
    def on_mouse_release(self,x, y, button, modifiers):
        if self.mouse_release_function is not None:
            self.mouse_release_function( self.entity, x, y, button, modifiers )
    
    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        if self.mouse_drag_function is not None:
            self.mouse_drag_function( self.entity, x, y, dx, dy, buttons, modifiers )
    
    def on_mouse_enter(self,x, y):
        if self.mouse_enter_function is not None:
            self.mouse_enter_function( self.entity, x, y )
    
    def on_mouse_leave(self,x, y):
        if self.mouse_leave_function is not None:
            self.mouse_leave_function( self.entity, x, y )
    
    def on_mouse_scroll(self,x, y, scroll_x, scroll_y):
        if self.mouse_scroll_function is not None:
            self.mouse_scroll_function( self.entity, x, y, scroll_x, scroll_y )