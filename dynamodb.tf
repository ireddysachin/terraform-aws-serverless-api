resource "aws_dynamodb_table" "users" {
    name = " users"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "userId"

    attribute {
        name ="userId"
        type = "S"
    }

    point_in_time_recovery {
        enabled = false
    }

    ttl {
        enabled = false
    }

    lifecycle {
        prevent_destroy = true

        ignore_changes = [
            name
        ]
    }
}