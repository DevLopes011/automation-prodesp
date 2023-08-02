# resource "aws_lambda_function" "lambda" {
#   filename         = "lambda_function.zip" # Nome do arquivo .zip do seu código lambda
#   function_name    = "seu-nome-do-lambda" # Substitua pelo nome da função Lambda desejado
#   role             = aws_iam_role.lambda.arn
#   handler          = "lambda_function.lambda_handler" # Substitua pela função handler do seu código
#   runtime          = "python3.8" # Substitua pela runtime do seu código
# }

resource "aws_iam_role" "lambda" {
  name = "seu-nome-do-iam-role" 

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "lambda" {
  name       = "seu-nome-do-iam-role-attachment" # Substitua pelo nome da role desejada
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  roles      = [aws_iam_role.lambda.name]
}