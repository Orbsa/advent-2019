from math import prod

# Returns list of numbers to use in operations
def getNums(i, intcode, numNums):
  numList = []
  for j in range(numNums):
    if intcode[i]//10**(2+j)%10==0: numList.append(intcode[intcode[i+j+1]])
    elif intcode[i]//10**(2+j)%10==1: numList.append(intcode[i+j+1])
    elif intcode[i]//10**(2+j)%10==2: numList.append(intcode[intcode[i+j+1]+relBase])
  return numList
# Add or Multiply
def arithCodes(i, intcode, mult=False):
  intcode[intcode[i+3]]=prod(getNums(i,intcode,2)) if mult else sum(getNums(i,intcode,2))
# Jump if True/False
def jumpIf(bolo, i, intcode):
  nums = getNums(i, intcode, 2)
  return nums[1] if nums[0] == bolo else i+3

# Compare Less than or Equivalent
def compare(i,intcode,equiv=False):
  (num1,num2) = getNums(i,intcode, 2)
  intcode[intcode[i+3]]= 1 if (not equiv and num1 < num2) or (equiv and num1==num2) else 0

myInput= None
with open('09.in', 'r') as f:
  myInput= [int(s) for s in f.readline().split(',')]
  myInput+= [0]*3*len(myInput) # Quadruple memory header

relBase = 0
def runProgram():
  intcode = myInput
  i= 0 # index of intcode
  j= 0 # index of inputVars
  instCount= 0
  relBase = 0
  while(True):
    instCount+=1
    if intcode[i]%100 == 1: # Addition
      arithCodes(i, intcode)
      i+=4
    elif intcode[i]%100 == 2: # Multiplication
      arithCodes(i, intcode, True)
      i+=4
    elif intcode[i]%100 == 3: # Input
      intcode[intcode[i+1]]=input("In< ")
      #intcode[intcode[i+1]]=int(inputVars[j])
      j+=1
      i+=2
    elif intcode[i]%100 == 4: # Output and Return
      print("Out>",intcode[intcode[i+1]])
      #return intcode[intcode[i+1]]
      i+=2
    elif intcode[i]%100 == 5: # Jump-if-True
      i=jumpIf(True, i, intcode)
    elif intcode[i]%100 == 6: # Jump-if-False
      i=jumpIf(False,i, intcode)
    elif intcode[i]%100 == 7: # Less than
      compare(i, intcode)
      i+=4
    elif intcode[i]%100 == 8: # Equals
      compare(i,intcode, True)
      i+=4
    elif intcode[i]%100 == 9: # Adjust Relative Base
      relBase += getNums(i, intcode, 1)[0]
    elif intcode[i]%100 == 99: # End Program
      break
    else:
      str("Program encountered error--\nInstruction#: " + str(instCount) + "\nIntCode: " + str(intcode[i]) +"\nIndex: " + str(i))
      break
  #print("Instructions ran: " + str(instCount))

runProgram()
