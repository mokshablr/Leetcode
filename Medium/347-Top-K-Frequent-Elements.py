import json

def topKFrequent(nums, k):
    sorted_nums = sorted(nums)
    print(sorted_nums)
    curr = sorted_nums[0]
    count = 1
    count_list = list()
    for i in sorted_nums[1:]:
        if i != curr:
            ele = (count, curr)
            count_list.append(ele)
            count = 1
            curr = i
        else:
            count += 1

    ele = (count, curr)
    count_list.append(ele)

    print(count_list)
    
    count_list = sorted(count_list, reverse=True)

    top_freq = list()

    for i in range(k):
        top_freq.append(count_list[i][1])

    print(top_freq)

    return top_freq

with open("testcase.txt", "r") as file:
    testcases = [line.strip() for line in file]

nums = json.loads(testcases[0])
k = int(testcases[1])

top = topKFrequent(nums, k)

