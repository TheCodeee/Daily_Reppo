# ROMAN TO INTEGER
def roman_to_integer(roman):
    roman_integers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    prev_char = 0

    for char in reversed(roman):
        value = roman_integers[char]

        if value < prev_char:
            total -= value

        else:
            total += value

        prev_char = value
    return total


print(roman_to_integer("MXDIVXC"))
