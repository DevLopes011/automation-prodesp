resource "aws_dynamodb_table" "automation_prodesp" {
  name         = "automations"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "automation_id"

  attribute {
    name = "automation_id"
    type = "S"
  }
}