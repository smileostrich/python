import re

# 7.1

# 7.7
mammoth = '''
We have seen the Queen of cheese, Laying quietly at your ease, Gently fanned by evening breeze, Thy fair form no flies dare seize.
All gaily dressed soon you’ll go To the great Provincial Show, To be admired by many a beau In the city of Toronto.
Cows numerous as a swarm of bees, Or as the leaves upon the trees, It did require to make thee please, And stand unrivalled Queen of Cheese.
May you not receive a scar as We have heard that Mr. Harris Intends to send you off as far as The great World’s show at Paris.
Of the youth beware of these, For some of them might rudely squeeze And bite your cheek; then songs or glees We could not sing o’ Queen of Cheese.
We’rt thou suspended from baloon, You’d cast a shade, even at noon, Folks would think it was the moon About to fall and crush them soon.
'''
# print(mammoth)


# 7.8
pat = r'\bc\w*'
print(re.findall(pat, mammoth))

# 7.9
pat = r'\bc\w{3}\b'
print(re.findall(pat, mammoth))

# 7.10
pat = r'\b\w*r\b'
print(re.findall(pat, mammoth))

# pat = r'\b\w*r\b'
pat = r'\w+?r[\b\W]'
matches = re.findall(pat, mammoth)
print(matches)
# pat = r'\w+r\b'
pat = r'\w+r[\b\W]'
matches = re.findall(pat, mammoth)
print(matches)

test = 'abcdef12345 ttt fff tttt t'
pat = r'\bt{2,4}?'
t = re.findall(pat, test)
# t = re.findall(r'\w', test)
print(t)