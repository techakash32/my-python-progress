num = int(123456789)
n = int(3)

power_n = 10 ** n

last = num % power_n
remaining_num = num // power_n
power_remaining = 1
temp = remaining_num
while temp > 0:
    power_remaining *= 10
    temp //= 10

new_num = last * power_remaining + remaining_num

print(new_num)
