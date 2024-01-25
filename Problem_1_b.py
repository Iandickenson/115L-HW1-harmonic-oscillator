from Problem_1_a import recur


def normalize_2n(n):
    arr = recur(n)
    # print(arr) this was to check it was working properly, not needed for now
    length = len(arr)
    last_coeff = arr[length - 1]
    factor = 2**n / last_coeff
    new_coeff = arr * factor
    return new_coeff

print(normalize_2n(4))

for i in range(6):
    print(normalize_2n(i))