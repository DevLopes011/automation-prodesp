import boto3
import io

class S3Uploader:
    def __init__(self):
        pass

    def upload_to_s3(self, file_data, bucket_name, s3_key):
        try:

            s3 = boto3.client('s3')

            file_obj = io.BytesIO(file_data)
            
            s3.upload_fileobj(file_obj, bucket_name, s3_key)

            print(f"Arquivo {s3_key} enviado para o AWS S3 com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao fazer upload para o S3: {e}")
            return False
        #     s3_uploader = S3Uploader()
        #     upload_sucesso = s3_uploader.upload_to_s3(arquivo_binario, nome_bucket_s3, chave_no_s3)
        #     if upload_sucesso:
        #         print("Upload para o S3 realizado com sucesso!")


    def new_folder_s3 (self, bucket_name, folder_name):
        # Cria uma sessão do Boto3
        s3 = boto3.client('s3')

        # Certifica-se de que a folder_name termine com uma barra para indicar que é uma pasta
        if not folder_name.endswith('/'):
            folder_name += '/'

        # Cria um objeto vazio com uma chave correspondente para criar a pasta virtual
        s3.put_object(Bucket=bucket_name, Key=folder_name)

        print(f"Pasta '{folder_name}' criada com sucesso no bucket '{bucket_name}'.")

        # Exemplo de uso:
        # if __name__ == "__main__":
        #     # Substitua com suas informações
        #     arquivo_binario = b'\x89PNG\r\n\x1a\n\x00\x00...'  # Substitua isso com seus dados binários
        #     nome_bucket_s3 = "seu-nome-de-bucket"
        #     chave_no_s3 = "caminho/dentro/do/seu/bucket/arquivo.png"

