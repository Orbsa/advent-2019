def addCodes(i):
    intcode[intcode[i+3]]=intcode[intcode[i+1]]+intcode[intcode[i+2]]
def multCodes(i):
    intcode[intcode[i+3]]=intcode[intcode[i+1]]*intcode[intcode[i+2]]

#intcode[1]=12
#intcode[2]=2
for noun in range(100):
    for verb in range(100):
        intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
        intcode[1] = noun
        intcode[2] = verb
        i= 0;
        while(True):
            if intcode[i] == 1:
                addCodes(i)
            elif intcode[i] == 2:
                multCodes(i)
            elif intcode[i] == 99:
                if intcode[0] == 19690720:
                    print(100*noun + verb)
                break
            else:
                break
            i+=4

