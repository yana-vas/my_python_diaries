software_version = input().split('.')
# next_version = [i for i in range(len(software_version)) if int(software_version[i]) > 9]
next_version = list(map(lambda x: str(int(-x) + 1), software_version))
print(next_version)

# if int(software_version[2]) == 9:
#     if int(software_version[1]) == 9:
#         software_version[2] = '0'
#         software_version[1] = '0'
#         software_version[0] = str(int(software_version[0]) + 1)
#     else:
#         software_version[2] = '0'
#         software_version[1] = str(int(software_version[1]) + 1)
# else:
#     software_version[2] = str(int(software_version[2]) + 1)
# print(".".join(software_version))

