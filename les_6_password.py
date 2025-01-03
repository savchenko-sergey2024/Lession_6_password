def is_very_long(password):
    length = len(password) > 12
    return length

def has_digit(password):
    return any(numbers.isdigit() for numbers in password)

def has_symbols(password):
    return (symbols1 != symbols.isalpha() and symbols2 != symbols.isdigit() for symbols in password)

def has_upper_letters(password):
    return any(letters_upper.isupper() for letters_upper in password)

def has_lower_letters(password):
    return any(letters_lower.islower() for letters_lower in password)

def password_verification(password):
    password_verification_list = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]
    score = 0
    for verification in password_verification_list:
        if verification:
            score += 2
    return score

def main():
    password = input()
    print(password_verification(password))

if __name__ == '__main__':
    main()