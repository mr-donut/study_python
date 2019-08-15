# На вход подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек).
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

# first_string = ''
# second_string = ''
# third_string = ''
# forth_string = ''
# i = 0
# while i <9:
#     x = str(input())
#     if i < 3:
#         first_string += x
#         first_string += " "
#     elif i < 6:
#         second_string += x
#         second_string += " "
#     else:
#         third_string += x
#         third_string += " "
#     i = i + 1
# forth_string += str(input())
# first_string = first_string.rstrip(' ')
# second_string = second_string.rstrip(' ')
# third_string = third_string.rstrip(' ')
# print(first_string)
# print(second_string)
# print(third_string)
# print(forth_string)



# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1


#  Создание прямоугольной матрицы row - строк на col - столбцов.
# row, col = (int(i) for i in input().split())
# a = [[0 for j in range(col)]for i in range(row)]
# print(a)

#годное решение на ввод матрицы 3*3 с 4-й строкой end
# n = 3
# a = []
# for i in range (n):
#     a.append([int(j) for j in input().split()])
# a.append([str(input())])
#
#                i,j ____________ j
#                 |_ 9_|_5_|_3_
#                 | _0_|_7_|_-1
#                 | _-5|_2_|_9
#                 |    end
#                i
#


# for i in range(n):
#     a[i][i] = 1
# for i in range(n):
#     for j in range(i+1, n):
#         a[i][j] = 0
# for i in range(n):
#     for j in range(0, i):
#         a[i][j] = 2
#
# for row in a:
#     print(' '.join([str(elements) for elements in row]))

# a = [[((i-1, j)+(i+1, j)+(i, j-1)+(i, j+1)) for j in range(m)] for i in range(n)]
# for row in a:
#     print(' '.join([str(elements) for elements in row]))


def wrap_index(i, N):
    return (i + N) % N

n = 3
m = 3

a = []

line = input("Ввести линию матрицы")
while line != 'end':
    a.append([int(i) for i in line.split()])
    line = input()

print("\n --- a ---")
print(a)
for row in a:
    print(' '.join([str(elements) for elements in row]))

nn = len(a)
mm = len(a[0])

c = []
for i in range(len(a)):
    line = []
    for j in range(len(a[i])):
        line.append(0)
    c.append(line)

for i in range(len(a)):
    row_len = len(a[i])
    for j in range(row_len):
        c[i][j] = a[i][wrap_index(j - 1, row_len)] \
                  + a[i][wrap_index(j + 1, row_len)] \
                  + a[wrap_index(i - 1, len(a))][j] \
                  + a[wrap_index(i + 1, len(a))][j]

print("--- c ---")
for row in c:
    print(' '.join([str(elements) for elements in row]))