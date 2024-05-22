"""
Convert numbers to French
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
        if (number > 70) and (number < 80):
            number_in_french = f"{CONSTANTS[60]}-{CONSTANTS[number - 60]}"
        elif (number > 80) and (number < 100):
            number_in_french = f"{CONSTANTS[80][:-1]}-{CONSTANTS[number - 80]}"

    return number_in_french


def convert_100_to_999(number):
    """Convert numbers from 100 to 999"""

    floor = number // 100
    if floor == 1:
        return f"{CONSTANTS[100]} {convert_0_to_99(number % 100)}"
    return f"{CONSTANTS[floor]} {CONSTANTS[100]} {convert_0_to_99(number % 100)}"


def convert_1000_upwards(number):
    """Convert numbers from 1000 going upwards"""

    floor = number // 1000
    if floor == 1:
        return f"{CONSTANTS[1000]} {convert_100_to_999(number % 100)}"
    return f"{CONSTANTS[floor]} {CONSTANTS[1000]} {convert_1000_upwards(number % 1000)}"


def convert_number_to_french(number):
    """Convert a given number n to French"""

    if number in CONSTANTS:
        return CONSTANTS[number]
    elif number > 999:
        return convert_1000_upwards(number)
    elif number > 100:
        return convert_100_to_999(number)
    elif number > 10:
        return convert_0_to_99(number)


if __name__=="__main__":
    n = 197
    print(convert_number_to_french(n))
