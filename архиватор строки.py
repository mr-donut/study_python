s = input()
a = ''
vasya = 0
i = 0

for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        vasya += 1
        i += 1

    else:
        vasya += 1
        a += s[i] + str(vasya)
        vasya = 0
        i += 1
if len(s) > 1:
    if s[-2] == s[-1]:
        vasya += 1
        a += s[-1] + str(vasya)
    elif s[-2] != s[-1]:
        a += s[-1] + str(1)
else:
    a = s + '1'

print(a)