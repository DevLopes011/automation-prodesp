import boto3

class SNSManipulator:
    def __init__(self):
        self.sns = boto3.client('sns')

    def publicar_mensagem(self, file_key):
        try:
            
            response = self.sns.publish(
                TopicArn='arn:aws:sns:us-east-1:516152518716:sns-prodesp',
                Message=file_key, # o caminho do arquivo no bucket
            )
            print(f"Resultado da publicação {response}")

        except Exception as e:
            print(f"Erro ao publicar: {e}")
