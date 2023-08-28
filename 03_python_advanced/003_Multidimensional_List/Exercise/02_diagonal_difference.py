rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
primary_diagonal = [matrix[index][index] for index in range(rows)]
secondary_diagonal = [matrix[i-1][-i] for i in range(1, rows+1)]
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
