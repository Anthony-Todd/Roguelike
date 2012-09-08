'''
Created on Sep 2, 2012

@author: anthony
'''
from cocos.cocosnode import CocosNode
class Entity( CocosNode ):
    '''
    classdocs
    '''


    def __init__(self, **kwargv):
        super(Entity, self).__init__()
        componentList = kwargv.get('Components')
        self.componentDict = {}
        self.AddComponents(componentList)
        
    def AddComponents(self, *components):
        for component in components:
            component_type = type(component)
            
            if component_type in self.componentDict:
                if not component.isUnique:
                    self.componentDict[component_type].append(component)
                    component.SetEntity( self )
            else:
                self.componentDict[component_type] = [component]
                component.SetEntity(self)
            
            
    
    def RemoveComponents(self, *components):
        pass
    
    def RemoveComponentsOfType(self, component_type):
        pass
        
