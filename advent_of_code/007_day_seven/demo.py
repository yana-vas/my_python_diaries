input_data = open("seventh_day_input_data.txt", 'r').read().split('\n')
files = {}
directories = []
curr_dir = ''
dir = ''
size = []
for el in input_data:
    el = el.split()
    if el[0] == '$':
        if el[1] == 'cd':
            char = el[-1]
            if char == '...':
                if directories.index(curr_dir) != 0:
                    curr_dir = directories[directories.index(curr_dir)-1]
            else:
                curr_dir = el[2][-1]
                if curr_dir == '/':
                    files[curr_dir] = {}
                    files[curr_dir]['size'] = 0
                directories.append(curr_dir)

        elif el[1] == 'ls':
            print(files)
    elif el[0] == 'dir':
        name = el[1]
        path = files
        for i in range(len(directories)):
            d = directories[i]
            path = path[d]
        path[name] = {}
        path[name]['size'] = 0
    else:
        name = el[1]

        path = files
        for i in range(len(directories)-1):
            d = directories[i]
            path = path[d]
            if curr_dir in path.keys():
                break
        path[curr_dir][name] = int(el[0])
        path[curr_dir]["size"] += int(el[0])
        size.append(int(el[0]))


sum_list = []
for el in size:
    curr_sum_list = []
    for i in range(len(size) - 1):
        this_sum = el + size[i + 1]
        if this_sum < 100000:
            curr_sum_list.append(el+size[i+1])
    # curr_sum_list = [el+size[i+1] for i in range(len(size)-1) if el+size[i+1] < 100000]
    if len(curr_sum_list) > 0:
        sum_list.append(curr_sum_list)

print(sum_list)
print(files)