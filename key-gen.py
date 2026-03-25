from cryptography.fernet import Fernet

def generate_key():
    # Gera uma chave aleatória e segura
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Chave 'secret.key' gerada com sucesso!")

if __name__ == "__main__":
    generate_key()