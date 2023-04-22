# def some():
#     print('Hello world')
#
# some()

a, b, c, d = int(input()), int(input()), int(input()), int(input())

for i in range(c, d + 1):
    print('\t' + str(i), end='')
print()

for i in range(a,b+1):
    print(i, end ='\t')
    for n in range(c,d+1):
        print(i*n,end='\t')
    print()