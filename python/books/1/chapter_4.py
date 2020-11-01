answer_list = []

# 4.1
ans = ''
guess_me = 7
if guess_me < 7:
    ans = 'too low'
elif guess_me > 7:
    ans = 'too high'
else:
    ans = 'just right'
tmp = f'4.1 : {ans}'
answer_list.append(tmp)

answer_list.append('22')
answer_list.append('22')
print('\n'.join(answer_list))

