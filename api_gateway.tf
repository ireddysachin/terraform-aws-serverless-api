resource "aws_apigatewayv2_api" "users_api" {
    name = "users-api-gateway"
    protocol_type = "HTTP"
    route_selection_expression = "$${request.method} $${request.path}"
    }