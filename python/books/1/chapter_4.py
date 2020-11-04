answer_list = []

# 4.1
tmp = ''
guess_me = 7
if guess_me < 7:
    tmp = 'too low'
elif guess_me > 7:
    tmp = 'too high'
else:
    tmp = 'just right'
ans = f'4.1 : {tmp}'
answer_list.append(ans)

# 4.2
tmp = []
guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        tmp.append('too low')
    elif start == guess_me:
        tmp.append('found it!')
        break
    else:
        tmp.append('oops')
        break
    start += 1
processed_tmp = '\n\t  '.join(tmp)
ans = f'4.2 : {processed_tmp}'
answer_list.append(ans)

# 4.3
tmp = '\n\t  '.join(map(str, [3, 2, 1, 0]))
ans = f'4.3 : {tmp}'
answer_list.append(ans)

# 4.4
even = [i for i in range(10) if i % 2 == 0]
tmp = ' '.join(map(str, even))
ans = f'4.4 : {tmp}'
answer_list.append(ans)

# 4.5
squares = {i:i**2 for i in range(10)}
tmp = squares.items()
ans = f'4.5 : {tmp}'
answer_list.append(ans)

# 4.6
set_cmp = {i for i in range(10) if i % 2 == 1}
tmp = ' '.join(map(str, set_cmp))
ans = f'4.6 : {tmp}'
answer_list.append(ans)

# 4.7
gen_cmp = (f'Got {i}' for i in range(10))
tmp = '\n\t  '.join(gen_cmp)
# for line in gen_cmp:
ans = f'4.7 : {tmp}'
answer_list.append(ans)

# 4.8
def good():
    list = ['Harry', 'Ron', 'Hermione']
    return list
ans = f'4.8 : {good()}'
answer_list.append(ans)

# 4.9
def get_odds():
    for i in range(1, 10, 2):
        yield i
print(get_odds())

# 4.10


# answer print
print('\n'.join(answer_list))

