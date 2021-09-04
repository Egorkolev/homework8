nums = int(input('введите число:'))
i = 0
ans = 1
while ans * 2 <= nums:
    ans *= 2
    i += 1
print(nums, i, ans, end='   ')
print('2 **', i, '=', ans, end='    ')
