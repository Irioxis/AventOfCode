###########################################################################################################################
#                                                                                                                         #
#                                                                                                                         #
#                 🎄🎄                         AVENT OF CODE                         🎄🎄                                 #
#                                                                                                                         #                                                                                   #
#                                               EVENT  #1                                                                 #
###########################################################################################################################



def find_key(line:str)->int:
    i = 0
    j = len(line)-1
    fstNb,sndNb = None,None
    while (i < len(line) or j > 0):
        if line[i].isdigit() and fstNb == None:
            fstNb = line[i]
        if line[j].isdigit() and sndNb == None:
            sndNb = line[j]
        if fstNb != None and sndNb != None:
            return fstNb + sndNb
        i+=1
        j-=1

sum = 0
file = open("./input").read().split("\n")
file.pop()

for line in file:
    sum+= int(find_key(line))

print("code : ",sum)

