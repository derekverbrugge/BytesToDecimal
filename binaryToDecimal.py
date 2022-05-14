#binaryToDecimal.py

#settings
inputF = 'binaryTest.bin' #input file
outputF = 'oFile.o' #output file
printFlag = 1 #0 -off | 1 - min | 2 - detailed | 3 - debug

#open binary
inFile = open(inputF, 'r')
count = 0
L = ""

for line in inFile:
  count += 1
  
  a = line.strip()

  if printFlag == 3:
	#prints file in binary
    print("Line {}: {}".format(count, a))
  if printFlag == 2:
    #prints in binary and decimal while read in
    print("Line {}: {} \n   Dec: {}".format(count, a, int(a,2)))

  #converts file to decimal
  L = L + str(int(a,2)) + "\n"

if printFlag == 3:  
  print("\n")
if printFlag == 1:  
#prints the content of L that will be written to the output file
  print("Writing to file: \n" + L)

inFile.close() 
# Writing to file

oFile = open(outputF, 'w')
oFile.writelines(L)
oFile.close()

#printing oFile
if printFlag == 3:
	oFile = open(outputF, 'r')
	count = 0

	for line in oFile:
  		count += 1
  
  		a = line.strip()

  		#prints in decimal while read in
  		print("Line {}: {}".format(count, a))

	oFile.close()


