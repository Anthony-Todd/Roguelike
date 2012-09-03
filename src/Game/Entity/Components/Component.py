'''
Created on Sep 2, 2012

@author: anthony
'''
import abc
from _pyio import __metaclass__

class Component(object):
    '''
    classdocs
    '''

    __metaclass__ = abc.ABCMeta

    def __init__(self, *argv, **kwargv ):
        '''
        Constructor
        '''
        self.isUnique = kwargv.get('isUnique')
        self.entity = None
        
    @abc.abstractmethod
    def Update(self, dt):
        pass
    @abc.abstractmethod
    def SetEntity(self, entity):
        print 'base'
        self.entity = entity