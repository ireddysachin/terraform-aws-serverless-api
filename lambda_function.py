import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("users")


def lambda_handler(event, context):

    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    # =========================
    # GET USER
    # =========================
    if method == "GET":

        user_id = (
            event.get("pathParameters", {}).get("userId")
            or event.get("pathParameters", {}).get("userId")
        )

        if not user_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "userId is required"
                })
            }

        response = table.get_item(
            Key={
                "userId": user_id
            }
        )

        item = response.get("Item")

        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "User not found"
                })
            }

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    # =========================
    # CREATE USER
    # =========================
    if method == "POST":

        body = json.loads(event.get("body", "{}"))

        user_id = body.get("userId")
        name = body.get("name")
        email = body.get("email")

        if not user_id or not name or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "userId, name and email are required"
                })
            }

        table.put_item(
            Item={
                "userId": user_id,
                "name": name,
                "email": email
            }
        )

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "User created successfully",
                "userId": user_id
            })
        }

    # =========================
    # UPDATE USER
    # =========================
    if method == "PUT":

        user_id = event.get("pathParameters", {}).get("userId")

        if not user_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "userId is required"
                })
            }

        body = json.loads(event.get("body", "{}"))

        name = body.get("name")
        email = body.get("email")

        if not name or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "name and email are required"
                })
            }

        response = table.update_item(
            Key={
                "userId": user_id
            },
            UpdateExpression="SET #name = :name, #email = :email",
            ExpressionAttributeNames={
                "#name": "name",
                "#email": "email"
            },
            ExpressionAttributeValues={
                ":name": name,
                ":email": email
            },
            ReturnValues="ALL_NEW"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "User updated successfully",
                "user": response.get("Attributes")
            })
        }

    # =========================
    # DELETE USER
    # =========================
    if method == "DELETE":

        user_id = event.get("pathParameters", {}).get("userId")

        if not user_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "userId is required"
                })
            }

        table.delete_item(
            Key={
                "userId": user_id
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "User deleted successfully",
                "userId": user_id
            })
        }

    # =========================
    # METHOD NOT ALLOWED
    # =========================
    return {
        "statusCode": 405,
        "body": json.dumps({
            "message": "Method not allowed"
        })
    }
        