def print_two(*args):
  arg1, arg2 = args
  print('arg1:%r, arg2: %r' % (arg1,arg2))

def print_two_again(arg1,arg2):
  print('arg1:%r, arg2: %r' % (arg1,arg2))

def print_one(arg1):
  print(arg1)

def print_none():
  print(None)

print_two('b', 'd')
print_two_again('b','d')
print_one('b')
print_none()
