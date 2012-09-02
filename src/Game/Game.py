'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos
import Level
import UI

class Game( cocos.scene.Scene ):
    '''
    classdocs
    '''


    def __init__( self, *argv, **kwargv ):
        '''
        Constructor
        '''
        self.level = Level.Level( parent=self );
        self.ui    = UI.UI()
        super( Game, self ).__init__( )
        for l in [ self.level, self.ui ]:
            self.add( l )