resource "aws_apigatewayv2_stage" "default"{
    api_id = aws_apigatewayv2_api.users_api.id
    name = "$default"
    auto_deploy = true
}