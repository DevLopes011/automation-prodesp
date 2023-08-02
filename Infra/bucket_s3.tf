resource "aws_s3_bucket" "prodesp_bucket" {
  bucket = "my-tf-prodesp-bucket"
}

resource "aws_s3_bucket_ownership_controls" "prodesp_bucket" {
  bucket = aws_s3_bucket.prodesp_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "prodesp_bucket" {
  bucket = aws_s3_bucket.prodesp_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "prodesp_bucket_acl" {
  depends_on = [
    aws_s3_bucket_ownership_controls.prodesp_bucket,
    aws_s3_bucket_public_access_block.prodesp_bucket,
  ]

  bucket = aws_s3_bucket.prodesp_bucket.id
  acl    = "private"
}

# resource "aws_s3_bucket_notification" "bucket_notification" {
#   bucket = aws_s3_bucket.bucket.id

#   lambda_function {
#     lambda_function_arn = aws_lambda_function.lambda.arn
#     events              = ["s3:ObjectCreated:*"]
#   }
# }
