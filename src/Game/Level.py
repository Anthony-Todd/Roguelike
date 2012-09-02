'''
Created on Sep 2, 2012

@author: anthony
'''
import cocos.layer
class Level( cocos.layer.Layer ):
    '''
    classdocs
    '''

    def __init__(self, *argv, **kwargv ):
        '''
        Constructor
        '''
        self.parent = kwargv.get('parent')
        self.backGround  = cocos.layer.Layer()
        self.foreGround  = cocos.layer.Layer()
        self.player      = cocos.layer.Layer()
        super(Level, self).__init__()
        for l in [ self.backGround, self.foreGround, self.player ]:
            self.add( l )

        
