'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.cocosnode import CocosNode
class Entity( CocosNode ):
    '''
    classdocs
    '''


    def __init__(self, **kwargv ):
        super( Entity, self ).__init__()
        componentList = kwargv.get('Components')
        print componentList, type( componentList )
        self.componentDict = {}
        self.AddComonents( componentList )
        
    def AddComonents( self, *components ):
        for component in components:
            component_type = type(component)
            print "Type: %s" % component_type
            
            if self.componentDict.has_key(component_type) is True:
                if component.isUnique is False:
                    self.componentDict[component_type].append(component)
                    component.SetEntity( self )
            else:
                self.componentDict[component_type] = [ component ]
                component.SetEntity( self )
            
            
    
    def RemoveComponents( self, *components ):
        pass
    
    def RemoveComponentsOfType( self, component_type ):
        pass
        