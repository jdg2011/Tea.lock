#A simple script for generating any number of shuffled strings
#Outputs the generated strings in file "cr_strings.txt 
#I use it for generating cryptographic libraries but it is useful for other shuffling tasks too.

import random
import pyperclip

print("??? cRyPtAfOrMeR v1.1 ???")
print("Get a string shuffled as many times as you want! Wow!")
s = str(input("Enter a string to shuffle, or enter \"p\" to paste from clipboard\n > "))
if s == "p":
	s = pyperclip.paste()
	print("Pulled string \""+s+"\" from clipboard.")
n = int(input("Enter the number of shuffled strings you want\n > "))
f = open("cr_strings.txt", "w")
for x in range(n):
	sr = ''.join(random.sample(s, len(s)))
	print("Generating string number "+str(x+1)+"...")
	f.write(sr+"\n")
f.close()
print("Done!\n")
f = open("cr_strings.txt", "r")
y = 0
while y == 0:
	x = input("Enter \"c\" to copy the generated string(s), or enter anything else to exit\n > ")
	if x == "c":
		pyperclip.copy(f.read())
		print("String(s) copied to clipboard.\n")
	else:
		break
f.close()
