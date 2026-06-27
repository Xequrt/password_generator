LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"

def generate_password(length, seed, use_uppercase=True, use_digits=True, use_special=False):
    if length <= 0:
        return ""
    alphabet = (
        LOWERCASE +
        (UPPERCASE if use_uppercase else "") +
        (DIGITS if use_digits else "") +
        (SPECIAL if use_special else "")
    )
    if seed == 0:
        seed = 1
    current = abs(seed)
    result = ""
    for _ in range(length):
        current = next_random(current)
        index  = current % len(alphabet)
        result = result + alphabet[index]
    return result

def next_random(number):
    return (16807 * number) % 2147483647

def check_password(password):
    points = (
        (len(password) >= 8) +
        any(char.islower() for char in password) +
        any(char.isupper() for char in password) +
        any(char.isdigit() for char in password) +
        any(char in SPECIAL for char in password
        )
    )
    if points <= 2:
        verdict = 'Слабый'
    elif points == 3:
        verdict = 'Средний'
    elif points == 4:
        verdict = 'Надёжный'
    else:
        verdict = 'Очень надёжный'
    return f'{verdict} пароль (оценка {points} из 5)'