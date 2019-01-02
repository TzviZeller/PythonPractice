#!/usr/bin/env python3

print('Please provide file number: ')
fileNum = int(input())
f = open(('ex'+str(fileNum)+'.py'), 'x')
print('Do you need a .txt file? Y/N')
textfile=input()
if textfile == 'Y':
  f = open(('ex'+str(fileNum)+'.txt'), 'x')
