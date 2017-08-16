def findNumber(arr, k):
    if k in arr:
        return "YES"
    else:
        return "NO"


def oddNumbers(l, r):
    if l % 2 == 1:
        return range(l, r + 1, 2)
    else:
        return range(l + 1, r + 1, 2)


def sum_matching_range(x1, x2, y1, y2):
    xs = range(x1, x2)
    print(xs)
    ys = range(y1, y1)
    temp = []
    for y in ys:
        if y in xs:
            temp.append(y)
    return sum(temp)

#print(sum_matching_range(1, 10, 5, 20))


def clock_angles(hour, minute):
    bigA = 30  # 360 / 12
    smallA = 6  # 360/60
    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 0
    if(minute > 30 and hour < 6):
        hour += 360
    bigAngle = hour * bigA
    smallAngle = minute * smallA
    subtraction1 = abs(bigAngle - smallAngle)
    subtraction2 = abs(smallAngle - bigAngle)
    print(subtraction1, subtraction2)
    if subtraction1 < subtraction2:
        return subtraction1
    else:
        return subtraction2

print(clock_angles(1, 45))


def check_divisors(divisor_array, low, high):
    for x in range(low, high + 1):
        count = 0
        for y in divisor_array:
            if x % y == 0:
                count += 1
        if count == len(divisor_array):
            print(x, " all_match")
        elif count > 0:
            print(x, " one_match")
        else:
            print(x)


def multi_array_sum(arr):
    output = 0
    for x in arr:
        ouput += sum(x)
    return output

multi_array_sum([1], [2.3], [4])
check_divisors([2, 3], 1, 7)
