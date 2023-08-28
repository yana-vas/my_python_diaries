# втора задача

# делимо : делител = частно

num_a = int(input())
# a = частно
# for b in range(1, num_a + 1):
#     # b = divisor_or_not_b
#     if (num_a % b) == 0:
#         print(b)
b = 1
while b <= num_a:
    if (num_a % b) == 0:
        print(b)
    b = b + 1

