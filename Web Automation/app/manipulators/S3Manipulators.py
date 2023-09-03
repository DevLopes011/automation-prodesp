import boto3
import io
import traceback
class S3Uploader:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_to_s3(self, file_data, bucket_name, s3_key):
        try:
            
            file_obj = io.BytesIO(file_data)
            
            self.s3.upload_fileobj(file_obj, bucket_name, s3_key)

            print(f"Arquivo {s3_key} enviado para o AWS S3 com sucesso!")

        except Exception as e:
            print(f"Erro ao fazer upload para o S3: {e}")
            traceback.print_exc()
            raise e