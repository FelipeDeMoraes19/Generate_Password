import secrets
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def main():
    print("Bem-vindo ao Gerador de Senhas Seguras!")
    
    
    length = int(input("Qual o comprimento da senha desejada? "))
    use_uppercase = input("Incluir letras maiúsculas? (s/n) ") == 's'
    use_numbers = input("Incluir números? (s/n) ") == 's'
    use_special_chars = input("Incluir caracteres especiais? (s/n) ") == 's'

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print("Sua nova senha é:", password)

if __name__ == "__main__":
    main()
