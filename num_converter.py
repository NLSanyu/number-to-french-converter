"""
"""

CONSTANTS = {
    0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
    6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze",
    12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize",
    20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante",
    70: "soixante-dix", 80: "quatre-vingts", 90: "quatre-vingt-dix",
    100: "cent", 1000: "mille"
}

def convert_num_to_french(num):
    num_in_french = ""

    if num in CONSTANTS:
        num_in_french = CONSTANTS[num]
    else:
        if num < 70:
            remainder = num % 10
            if remainder == 1:
                num_in_french = f"{CONSTANTS[num - remainder]}-et-un"
            else:
                num_in_french = f"{CONSTANTS[num - remainder]}-{CONSTANTS[remainder]}"
        else:
            if (num > 70) and (num < 80):
                num_in_french = f"{CONSTANTS[60]}-{CONSTANTS[num - 60]}"
            elif (num > 80) and (num < 100):
                num_in_french = f"{CONSTANTS[80][:-1]}-{CONSTANTS[num - 80]}"

    return(num_in_french)


if __name__=="__main__":
    n = 87
    print(convert_num_to_french(n))
