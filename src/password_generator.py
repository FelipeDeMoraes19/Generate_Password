import secrets
import string
from datetime import datetime
from colorama import Fore, Style

def generate_password(length, use_uppercase, use_numbers, use_special_chars, exclude_similar):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if exclude_similar:
        characters = characters.translate(str.maketrans('', '', 'l1Io0O'))

    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def save_password(password):
    with open("passwords.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {password}\n")

def main():
    print(Fore.GREEN + "Bem-vindo ao Gerador de Senhas Seguras!\n" + Style.RESET_ALL)
    while True:
        try:
            length = int(input("Qual o comprimento da senha desejada (6-128)? "))
            if not 6 <= length <= 128:
                raise ValueError("O comprimento deve estar entre 6 e 128.")
        except ValueError as e:
            print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)
            continue

        use_uppercase = input("Incluir letras maiúsculas? (s/n) ") == 's'
        use_numbers = input("Incluir números? (s/n) ") == 's'
        use_special_chars = input("Incluir caracteres especiais? (s/n) ") == 's'
        exclude_similar = input("Excluir caracteres semelhantes? (s/n) ") == 's'

        password = generate_password(length, use_uppercase, use_numbers, use_special_chars, exclude_similar)
        print(Fore.YELLOW + "Sua nova senha é: " + Fore.CYAN + password + Style.RESET_ALL)

        if input(Fore.GREEN + "\nSalvar esta senha em um arquivo? (s/n) " + Style.RESET_ALL) == 's':
            save_password(password)
            print(Fore.GREEN + "Senha salva com sucesso!" + Style.RESET_ALL)

        if input(Fore.GREEN + "\nGerar outra senha? (s/n) " + Style.RESET_ALL) != 's':
            break

if __name__ == "__main__":
    main()
