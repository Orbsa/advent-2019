def anyAdjacent(x):
  flag=False
  numAdjacent=1
  for i in range(5):
    if x[i] == x[i+1]:
      numAdjacent+=1
    else:
      if numAdjacent == 2:
        return True
      numAdjacent=1
  if numAdjacent == 2:
    return True
  return False

def noDecrease(x):
  for i in range(5):
    if x[i] > x[i+1]:
      return False
  return True

def main():
  numResults=0
  for i in range(183564,657474):
    i = [int(k) for k in list(str(i))]
    if anyAdjacent(i) and noDecrease(i):
      numResults+=1
  print(numResults)

if __name__ == "__main__":
  main()
