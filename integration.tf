resource "aws_apigatewayv2_integration" "lambda"{
    api_id = aws_apigatewayv2_api.users_api.id
    integration_type =  "AWS_PROXY"
    integration_uri = aws_lambda_function.users_api.arn
    payload_format_version = "2.0"
}