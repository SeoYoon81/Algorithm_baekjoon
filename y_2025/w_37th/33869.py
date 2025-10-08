key = input()
decode = input()

ori_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
code_alph = []
alph_set = set()
for x in key:
    if x not in alph_set:
        code_alph.append(x)
        alph_set.add(x)
for x in ori_alph:
    if x not in alph_set:
        code_alph.append(x)
        alph_set.add(x)

code_dict = {}
for i in range(26):
    code_dict[ori_alph[i]] = code_alph[i]
answer = ''
for x in decode:
    answer += code_dict[x]
print(answer)