terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.0"
                    }
    }
}

provider "aws" {
    region = "us-east-1"

    endpoints {
        dynamodb = "http://localhost:4566"
        lambda = "http://localhost:4566"
        apigatewayv2 = "http://localhost:4566"
        sts = "http://localhost:4566"
    }

    access_key = "test"
    secret_key = "test"
}