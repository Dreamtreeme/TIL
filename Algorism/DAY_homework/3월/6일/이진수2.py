def decimal_to_binary_fraction(n):
    binary_string = ""
    for _ in range(12):
        n *= 2
        if n >= 1:
            binary_string += "1"
            n -= 1
        else:
            binary_string += "0"
        if n == 0:
            return binary_string
    if n > 0:
        return "overflow"
    else:
        return binary_string

T = int(input())
for t in range(1, T + 1):
    N_str = input()
    N = float(N_str)
    result = decimal_to_binary_fraction(N)
    output = ""
    if result == "overflow":
        output = "overflow"
    else:
        output = result
    print(f"#{t} {output}")