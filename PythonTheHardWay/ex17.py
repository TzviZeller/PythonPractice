from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copying', from_file, 'to', to_file)
in_file = open(from_file)
indata = in_file.read()

print('The input file is %d bytews long' % len(indata))

print('was the new file made? %r' % exists(to_file))
input('Hit enter or cntrl +c')

out_file = open(to_file, 'w')
out_file.write(indata)

print('all done!')

out_file.close()
in_file.close()
