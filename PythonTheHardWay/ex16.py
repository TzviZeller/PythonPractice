from sys import argv

script, filename = argv

print('we going to erase')
print('to stop hit cntrl+c')
print('to continue hit enter')

input('?')

print('Open file')
target = open(filename,'w')

print('truncating file')
target.truncate()

print('enter input')

line1 = input()

print('writing to file')

target.write(line1)

target.close
