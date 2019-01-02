states = {'bob': 'b', 'dave' : 'd' }

for state, abrv in states.items():
  print(state, abrv)

state = states.get('bob')
