"""
A script to convert numbers from digits to their written version in French
"""

CONSTANTS = {
    0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
    5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf",
    10: "dix", 11: "onze", 12: "douze", 13: "treize",
    14: "quatorze", 15: "quinze", 16: "seize",
    17: "dix-sept", 18: "dix-huit", 19: "dix-neuf",
    20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante",
    70: "soixante-dix", 80: "quatre-vingts", 90: "quatre-vingt-dix",
    100: "cent", 1000: "mille"
}


def convert_0_to_99(number):
    """Convert numbers from 0 to 99"""

    number_in_french = ""

    if number < 70:
        remainder = number % 10
        if remainder == 1:
            number_in_french = f"{CONSTANTS[number - remainder]}-et-un"
        else:
            number_in_french = f"{CONSTANTS[number - remainder]}-{CONSTANTS[remainder]}"
    else:
        if 70 < number < 80:
            number_in_french = f"{CONSTANTS[60]}-{CONSTANTS[number - 60]}"
        elif 80 < number < 100:
            number_in_french = f"{CONSTANTS[80][:-1]}-{CONSTANTS[number - 80]}"

    return number_in_french


def convert_100_to_999(number):
    """Convert numbers from 100 to 999"""

    floor = number // 100
    if floor <= 1:
        return f"{CONSTANTS[100]} {convert_0_to_99(number % 100)}"
    return f"{CONSTANTS[floor]} {CONSTANTS[100]} {convert_0_to_99(number % 100)}"


def convert_1000_upwards(number):
    """Convert numbers from 1000 going upwards"""

    floor = number // 1000
    if floor <= 1:
        return f"{CONSTANTS[1000]} {convert_100_to_999(number % 100)}"
    return f"{CONSTANTS[floor]} {CONSTANTS[1000]} {convert_1000_upwards(number % 1000)}"


def convert_number_to_french(number):
    """Convert a given number n to French"""

    if number in CONSTANTS:
        return CONSTANTS[number]
    if number > 999:
        return convert_1000_upwards(number)
    if number > 100:
        return convert_100_to_999(number)
    if number > 10:
        return convert_0_to_99(number)


if __name__ == "__main__":
    input_list = [
        0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105,
        111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234
    ]

    #  1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

    # using a reduced version of the list for testing purposes
    # (TO DO: fix recursion error when testing with larger numbers)

    converted_numbers = list(map(convert_number_to_french, input_list))
    print(converted_numbers)
