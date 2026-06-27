from password_generator import check_password, generate_password

print("== Генерация паролей ==")
print("буквы и цифры:   ", generate_password(length=12, seed=123))
print("со спецсимволами:", generate_password(length=16, seed=7, use_special=True))

print()
print("== Проверка надёжности ==")
print("abc        ->", check_password("abc"))
print("abcdef1234 ->", check_password("abcdef1234"))
print("Abcdef123! ->", check_password("Abcdef123!"))
