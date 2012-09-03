'''
Created on Sep 3, 2012

@author: anthony
'''

import abc
from _pyio import __metaclass__

class Manager(object):
    '''
    classdocs
    '''

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        '''
        Constructor
        '''
        self.components = []
    
    def VisitComponents(self, callback, **kwargs ):
        for c in self.components:
            callback( c, kwargs)
            
    def Update(self, dt):
        for c in self.components:
            print c
            c.Update(dt)
        