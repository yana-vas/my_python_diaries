rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary_diagonal = [matrix[index][index] for index in range(rows)]
secondary_diagonal = [matrix[i-1][-i] for i in range(1, rows+1)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
