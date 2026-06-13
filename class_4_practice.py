#problem -3
#Story: You found an ancient scroll (a string). Legend says to unlock the chamber, you must find every unique character, calculate the square of its ASCII value, and store them in a set.

import sys
#1.Accept a string via Command Line Arguments (sys.argv). If none provided, default to "magic".
text=sys.argv[1] if len(sys.argv)>1 else "magic"
print(text)

#2.Use a Set Comprehension and a Lambda to generate a set of squared ASCII values (ord(char)**2) for every unique character in the string.

f=lambda x:ord(x)**2

s={f(x) for x in set(text) }
print(s)
# 3.Write the resulting set to a text file runes.txt.
with open("runs.txt",'w') as f:
    f.write(str(s))

with open("runs.txt",'r') as f:
    print(f.read())

# problem-2
import csv
from functools import reduce

n=int(input("Enter the number of rows: "))

rows=[]
for _ in range(n):
    member_id=input("Enter member ID: ")
    score=int(input("Enter score: "))
    rows.append((member_id,score))

with open("vault.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["Member ID","Score"])
    writer.writerows(rows)


