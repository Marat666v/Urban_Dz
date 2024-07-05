a = int(input())
s = []
for i in range(1, a):
    for j in range(1, a):
        n = i+j
        if a%n==0 and i<j:
            s.append(1)
            s.append(1)
print(print(''.join(map(str, s))))