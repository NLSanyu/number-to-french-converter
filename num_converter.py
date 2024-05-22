CONSTANTS = {
    0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
    6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze",
    12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize",
    20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante",
    100: "cent", 1000: "mille"
}

def convert_num_to_french(num):
    num_in_french = ""

    if num < 70:
        if num in CONSTANTS:
            print(CONSTANTS[num])
        else:
            remainder = num % 10
            if remainder == 1:
                num_in_french = f"{CONSTANTS[num - remainder]}-et-un"
            else:
                num_in_french = f"{CONSTANTS[num - remainder]}-{CONSTANTS[remainder]}"
    else:
        if num >=70 :
            pass

    return(num_in_french)


if __name__=="__main__":
    n = 69
    print(convert_num_to_french(n))
