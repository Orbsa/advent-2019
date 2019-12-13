satList= []

class satellite:
  def __init__(self, name, pName = None, pNode = None):
    self.name= name
    self.pName = pName
    self.children = []
    self.parent = None
    if pNode is not None:
      self.setParent(pNode)
  def setParent(self, pNode):
    self.parent = pNode
    self.parent.children.append(self)
  def genParent(self): # If the generating list isn't ordered
    pSat = satellite(self.pName)
    self.setParent(pSat)
    return pSat
  # Get a List of Orbits
  def getOrbitList(self, endAt = None):
    if self.parent is None or self is endAt:
      return [self]
    return self.parent.getOrbitList(endAt) + [self]
  # Find the Common Ancestor Sattelite between this and another satellite
  def getCommonSat(self,coSat):
    myList = self.getOrbitList()
    coList = coSat.getOrbitList()
    i=0
    for i in range(len(myList)):
      if myList[i] is not coList[i]: break
    return myList[i-1]

  def __str__(self):
    return (str(self.parent) if self.parent is not None else "") +")"+ self.name

# Gen List
with open('06.in') as f:
  for x in f:
    orbits= [y.strip() for y in x.split(')')]
    pParent = [s for s in satList if s.name == orbits[0]]
    parent = pParent[0] if pParent else None
    mySat = satellite(orbits[1], orbits[0], parent)
    satList.append(mySat)
    pChildren = [s for s in satList if s.pName == orbits[1]] # Assign Missing Children
    for s in pChildren: s.setParent(mySat)
  satList += [sat.genParent() for sat in satList if sat.pName is not None and sat.parent is None]

def countOrbits(sat):
  if sat.parent is not None:
    return 1+countOrbits(sat.parent)
  return 0

def getTransfers(satFromName = "YOU", satToName= "SAN"):
  you= [s for s in satList if s.name == satFromName][0]
  santa= [s for s in satList if s.name == satToName][0]
  cSat= you.getCommonSat(santa)
  u2cSat = len(you.getOrbitList(cSat))
  s2cSat = len(santa.getOrbitList(cSat))
  return (u2cSat - 2 if u2cSat > 2 else 0) + (s2cSat - 2 if s2cSat > 2 else 0)




totalO=0
for s in satList: totalO += countOrbits(s)

numParents=0
for s in satList:
  if s.parent is not None: numParents+=1

print("NumSats",len(satList))
print("NumParents:",numParents)
print("Total Orbits in Satellite List:",totalO)
print("Orbital Changes to get to santa:",getTransfers())
