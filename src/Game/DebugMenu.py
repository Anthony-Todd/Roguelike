'''
Created on Sep 9, 2012

@author: anthony
'''

import cocos

class PropertyMenue( cocos.menu.Menu):
    
    def __init__( self, title=''):
        super( PropertyMenue, self ).__init__(title)

class DebugMenu(cocos.scene.Scene):
    '''
    classdocs
    '''


    def __init__( self ):
        super( DebugMenu, self ).__init__()
        self.add( PropertyMenue('Debug Menue'), (0,640) )
        
debugMenu = DebugMenu()