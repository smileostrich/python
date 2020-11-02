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

#

# answer print
print('\n'.join(answer_list))

