'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos.layer
import Entity

class Level( cocos.layer.Layer ):
    '''
    classdocs
    '''

    def __init__(self, *argv, **kwargv ):
        '''
        Constructor
        '''
        self.parent = kwargv.get('parent')
        self.backGround = cocos.layer.Layer()
        self.forGround  = cocos.layer.Layer()
        self.player     = cocos.layer.Layer()
        super(Level, self).__init__()
        for l in [ self.backGround, self.forGround, self.player ]:
            self.add( l )
        
        self.backGround.add( Entity.Factory.Create_Spirte('roguelike_basicclassdiagram.png', (320,240) ), 0, 'test' )
        