from azure.storage.blob import BlobServiceClient
import os
import sys

# Use variável de ambiente para segurança
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "backup-container"

def upload_to_blob(file_path, blob_name):
    if not connection_string:
        print("Erro: Defina a variável de ambiente AZURE_STORAGE_CONNECTION_STRING.")
        sys.exit(1)
    if not os.path.isfile(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        sys.exit(1)
    try:
        blob_service = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service.get_blob_client(container=container_name, blob=blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Arquivo {blob_name} enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")

if __name__ == "__main__":
    upload_to_blob("local_file.txt", "backup_file.txt")