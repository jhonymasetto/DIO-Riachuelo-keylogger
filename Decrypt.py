import os
from cryptography.fernet import Fernet

def load_key():
    # Carrega a chave gerada anteriormente
    return open("secret.key", "rb").read().strip()

def decrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Ignora os scripts do laboratório
            if file in ["Crypt.py", "secret.key", "Decrypt.py", "key-gen.py"]:
                continue
                
            file_path = os.path.join(root, file)
            
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            
            try:
                # Tenta descriptografar os dados
                decrypted_data = fernet.decrypt(encrypted_data)
                
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)
                print(f"[+] Arquivo {file} recuperado com sucesso!")
            except Exception as e:
                print(f"[!] Erro ao recuperar {file}: Chave incorreta ou arquivo corrompido.")

if __name__ == "__main__":
    target_dir = "/home/kali/alvo"
    if os.path.exists(target_dir):
        decrypt_files(target_dir)
    else:
        print("Diretório alvo não encontrado.")