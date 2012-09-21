'''
Created on Sep 9, 2012

@author: anthony
'''

import json

class Configuration(object):
    AISpeed = 0.8
    PlayerSpeed = 1.0
    WindowWidth = 30
    WindowHeight = 30
    MapWidth = 40
    MapHeight = 40
    TileSize = 16
    CharSize = 32
            
def LoadConfigurationFile(filename):
    jsonFile = open(filename)
    d = json.loads(jsonFile.read())

    for key, value in d.items():
        setattr(Configuration, key.encode('ascii'), value)
        
def SaveConfigurationFile(filename):
    f = open(filename, 'w')
    test = dict((key, value) for key, value in Configuration.__dict__.items())
    test.pop('__dict__')
    test.pop('__weakref__')
    test.pop('__doc__')
    test.pop('__module__')

    f.write(json.dumps(test, sort_keys=True, indent=4))
