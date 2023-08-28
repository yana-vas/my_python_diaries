string = input()
n = int(input())
def repeat(text, rep):
    result = ''
    for i in range(rep):
        result += string
    return result
print(repeat(text=string, rep= n))