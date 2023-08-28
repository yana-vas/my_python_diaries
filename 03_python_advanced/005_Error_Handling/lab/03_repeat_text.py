text = input()
try:
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")


# try - else - ако мине успешно през try, после автоматично ще отиде в else. Ако try е успешен ще отиде в else,
# но ако не успее да мине успешно през try, отива при except и не влиз в else. Else се изпълнява само при успешен try
# finally - finally и през try и през except се изпълнява за разлика от else.
