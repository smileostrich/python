# 3.1
year_lists = [i for i in range(1980, 1986)]
result = f'3.1 : {year_lists}'
print(result)

# 3.2
result = f'3.2 : {year_lists[3]}'
print(result)

# 3.3
result = f'3.3 : {year_lists[-1]}'
print(result)

# 3.4
things = ['mozzarella', 'cinderella', 'salmonella']
result = f'3.4 : {things}'
print(result)

# 3.5
result = f'3.5 : {things[1].capitalize()}, {things}'
print(result)

# 3.6
things[0] = things[0].upper()
result = f'3.6 : {things[0]}, {things}'
print(result)

# 3.7
del things[-1]
# things.remove('salmonella')
# things.pop(-1)
result = f'3.7 : {things}'
print(result)

# 3.8
surprize = ['Groucho', 'Chico', 'Harpo']
result = f'3:8 : {surprize}'
print(result)

# 3.9
surprize[-1] = surprize[-1].lower()[::-1].capitalize()
result = f'3.9 : {surprize}'
print(result)

# 3.10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
result = f'3.10 : {e2f}'
print(result)

# 3.11
result = f'3.11 : {e2f["walrus"]}'
print(result)

# 3.12
f2e = {v:k for k,v in e2f.items()}
result = f'3.12 : {f2e}'
print(result)

# 3.13
result = f'3.13 : {f2e["chien"]}'
print(result)

# 3.14
result = f'3.14 : {e2f.keys()}'
print(result)

# 3.15
life = {'animals':{}, 'plants':{}, 'other':{}}
life['animals'] = {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}
result = f'3.15 : {life}'
print(result)

# 3.16
result = f'3.16 : {life.keys()}'
print(result)

# 3.17
result = f'3.16 : {life["animals"].keys()}'
print(result)

# 3.18
result = f'3.16 : {life["animals"]["cats"]}'
print(result)