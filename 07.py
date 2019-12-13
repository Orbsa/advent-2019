from itertools import permutations

# Add or Multiply
def arithCodes(i, intcode, mult=False):
    num1 = intcode[intcode[i+1]] if intcode[i]//10**2%10==0 else intcode[i+1]
    num2 = intcode[intcode[i+2]] if intcode[i]//10**3%10==0 else intcode[i+2]
    intcode[intcode[i+3]]=num1*num2 if mult else num1+num2
# Jump if True/False
def jumpIf(bolo,intcode,i):
    cond = intcode[intcode[i+1]] if intcode[i]//10**2%10==0 else intcode[i+1]
    if (cond == bolo):
        return intcode[intcode[i+2]] if intcode[i]//10**3%10==0 else intcode[i+2]
    else:
        return i+3
# Compare Less than or Equivalent
def compare(i,intcode,equiv=False):
    num1 = intcode[intcode[i+1]] if intcode[i]//10**2%10==0 else intcode[i+1]
    num2 = intcode[intcode[i+2]] if intcode[i]//10**3%10==0 else intcode[i+2]
    intcode[intcode[i+3]]= 1 if (not equiv and num1 < num2) or (equiv and num1==num2) else 0

myInput= None
with open('07.in', 'r') as f:
    myInput= [int(s) for s in f.readline().split(',')]

def runProgram(inputVars):
  intcode = myInput
  i= 0 # index of intcode
  j= 0 # index of inputVars
  instCount= 0
  while(True):
    instCount+=1
    if intcode[i]%100 == 1: # Addition
      arithCodes(i, intcode)
      i+=4
    elif intcode[i]%100 == 2: # Multiplication
      arithCodes(i, intcode, True)
      i+=4
    elif intcode[i]%100 == 3: # Input
      #intcode[intcode[i+1]]=input("In< ")
      intcode[intcode[i+1]]=int(inputVars[j])
      j+=1
      i+=2
    elif intcode[i]%100 == 4: # Output and Return
      #print("Out>",intcode[intcode[i+1]])
      return intcode[intcode[i+1]]
      #i+=2
    elif intcode[i]%100 == 5: # Jump-if-True
      i=jumpIf(True, intcode, i)
    elif intcode[i]%100 == 6: # Jump-if-False
      i=jumpIf(False, intcode, i)
    elif intcode[i]%100 == 7: # Less than
      compare(i, intcode)
      i+=4
    elif intcode[i]%100 == 8: # Equals
      compare(i,intcode, True)
      i+=4
    elif intcode[i]%100 == 99: # End Program
      break
    else:
      str("Program encountered error--\nInstruction#: " + str(instCount) + "\nIntCode: " + str(intcode[i]) +"\nIndex: " + str(i))
      break
  #print("Instructions ran: " + str(instCount))

permus= list(permutations(range(5)))
highest = 0
for argList in permus:
  prevRes=0
  for phaseSetting in argList:
    prevRes+= runProgram([phaseSetting,prevRes])
  highest = prevRes if prevRes > highest else highest

print("Highest Permutation Result:", highest)
