def readIn(filename):
  with open(filename,'r') as f:
    return f.readline().strip()

def splitList(l, chunkSize):
  return [l[i*chunkSize :(i+1)*chunkSize ] for i in range((len(l) + chunkSize -1) // chunkSize )]

def printLayer(layer):
  cols = ['X','-',' ']
  for row in layer:
    rowStr = ''
    for col in row:
      rowStr+= cols[col]
    print(rowStr)

def combineLayers(bot, top):
  com= top
  for row in range(len(com)):
    print(com[row])
    #for col in range(len(row)):
      #if com[row][col] == 2: com[row][col] = bot[row][col]

def solve1(puzIn):
  layers= splitList(puzIn, imgSize[0]*imgSize[1]) # Split layers up unto 2d matrix
  minlayer = layers.pop(0)
  for layer in layers:
    if layer.count(0) < minlayer.count(0):
      minlayer = layer
  return minlayer.count(1) * minlayer.count(2)

def solve2(puzIn):
  layers = [splitList(j,imgSize[0]) for j in splitList(puzIn, imgSize[0]*imgSize[1])] # Split layers up into 3d matrix
  layers.reverse() # Reverse to loop through as first layer goes on top
  combined = layers.pop(0)
  for layer in layers:
    combineLayers(combined,layer)

  printLayer(combined)

imgSize= (25,6) # Image Size in pixels
def main():
  puzIn= [int(i) for i in list(readIn('08.in'))]
  print("Problem 1:", solve1(puzIn))
  print("Problem 2:")
  solve2(puzIn)


if __name__ == "__main__":
  main()
