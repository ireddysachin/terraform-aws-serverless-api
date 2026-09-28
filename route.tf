resource "aws_apigatewayv2_route" "hello" {
    api_id = aws_apigatewayv2_api.users_api.id
    route_key = "ANY /hello/{userId}"
    target = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}