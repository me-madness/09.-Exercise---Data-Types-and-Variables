n = int(input())

for i in range(n):
    list_count = input()
    if list_count == "(":
        print("BALANCED")
        break
    else:
        print("UNBALANCED")    