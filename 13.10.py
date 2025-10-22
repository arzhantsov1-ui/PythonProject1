slovo = "letter"
long = len(slovo)

if long % 2 == 0:
    midl = long // 2
    print(slovo[midl - 1 : midl + 1])

else:
    midl = long // 2
    print(slovo[midl])
