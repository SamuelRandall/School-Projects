# Complete the countingValleys function below.


def countingValleys(n, s):
    ups = 0
    downs = 0
    count = 0
    for num in list(s):
        if ups is 0 and downs is 0 and num is not 1:
            count += 1
        if num is 'U':
            ups += 1
        elif num is 'D':
            downs += 1
    return count


print(countingValleys(8, "UDDDUDUU"))
print(countingValleys(12, "DDUUDDUDUUUD"))
