resource "aws_sqs_queue" "my_queue" {
  name                      = "prodesp"
  delay_seconds             = 5
  max_message_size          = 262144
  message_retention_seconds = 345600  # 4 dias (valor máximo permitido)
  visibility_timeout_seconds = 30
}
