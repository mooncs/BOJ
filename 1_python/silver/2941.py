# 2941. 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for cro in croatia:
    word = word.replace(cro, '0')
print(len(word))

