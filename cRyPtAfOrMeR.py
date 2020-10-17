#A simple script for generating any number of shuffled strings
#Outputs the generated strings in file "cr_strings.txt 
#I use it for generating cryptographic libraries but it is 

import random

print("??? cRyPtAfOrMeR v1.0 ???")
print("Get a string  as many times as you want! Wow!")
s = str(input("Enter a string to randomize: "))
n = int(input("Enter the number of randomized strings you want: "))
f = open("cr_strings.txt", "w")
for x in range(n):
	sr = ''.join(random.sample(s, len(s)))
	print("Generating string number "+str(x)+"...")
	f.write(sr+"\n")

f.close()
print("Done!")
