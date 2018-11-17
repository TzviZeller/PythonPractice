from sys import argv

script, user_name = argv
prompt = '>'

print('Hi %s, Im the %s script' % (user_name, script))
print('do you like me?')
likes = input(prompt)

print('Where do you live %s ?' % user_name)
lives = input(prompt)

print(likes, lives)
