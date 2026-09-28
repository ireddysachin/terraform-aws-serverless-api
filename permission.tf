resource "aws_lambda_permission" "api_gateway"{
    statement_id = "AllowAPIGatewayInvoke"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.users_api.function_name
    principal = "apigateway.amazonaws.com"
}
