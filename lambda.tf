resource "aws_lambda_function" "users_api" {
  function_name = "users-api"
  runtime       = "python3.12"
  handler       = "lambda_function.lambda_handler"

  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")

  role = "arn:aws:iam::000000000000:role/lambda-role"
}