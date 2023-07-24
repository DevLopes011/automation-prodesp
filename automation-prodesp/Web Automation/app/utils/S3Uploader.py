import boto3
import io

class S3Uploader:
    def __init__(self):
        pass

    def upload_to_s3(file_data, bucket_name, s3_key):
        try:
            # Cria uma sessão do boto3
            s3 = boto3.client('s3')

            # Converte os dados binários para um objeto de leitura usando BytesIO
            file_obj = io.BytesIO(file_data)

            # Faz o upload do arquivo para o S3
            s3.upload_fileobj(file_obj, bucket_name, s3_key)

            return True
        except Exception as e:
            print(f"Erro ao fazer upload para o S3: {e}")
            return False


# Exemplo de uso:
# if __name__ == "__main__":
#     # Substitua com suas informações
#     arquivo_binario = b'\x89PNG\r\n\x1a\n\x00\x00...'  # Substitua isso com seus dados binários
#     nome_bucket_s3 = "seu-nome-de-bucket"
#     chave_no_s3 = "caminho/dentro/do/seu/bucket/arquivo.png"

#     s3_uploader = S3Uploader()
#     upload_sucesso = s3_uploader.upload_to_s3(arquivo_binario, nome_bucket_s3, chave_no_s3)
#     if upload_sucesso:
#         print("Upload para o S3 realizado com sucesso!")
