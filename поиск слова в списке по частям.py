list_0 = ["апельсин","слива","яблоко", "груша", "грузило"]
word = input('?')
for i in range(len(list_0)):
    if word in list_0[i]:
        print(list_0[i])