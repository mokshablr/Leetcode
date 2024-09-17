nums=[3,2,1,0,5]

l = len(nums)
curr = 0;
stack = list()

def jump(nums, curr):
    while True:
        curr += stack[-1]
        if curr == (l-1):
            return True

        if curr >= l or nums[curr]==0:
            curr -= stack[-1]
            stack[-1] -=1
            if stack[-1]==0:
                stack.pop()
            if len(stack)<1:
                return False
            continue
        else:
            stack.append(nums[curr])
            return jump(curr, nums)

stack.append(nums[curr])
# print(jump(nums, curr))
def test():
    nums.pop()

test()
print(nums)
