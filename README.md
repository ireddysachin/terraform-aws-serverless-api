# 🚀 Terraform + Floci Serverless CRUD API

A hands-on **serverless CRUD API project** built using **Terraform, Floci, Docker, AWS Lambda, API Gateway, DynamoDB, Python, AWS CLI, Git, and GitHub**.

This project demonstrates how to design, provision, manage, and test a serverless application using **Infrastructure as Code (IaC)** in a local AWS-compatible environment.

---

## 📌 Project Overview

The project implements a simple **User Management REST API** with complete CRUD functionality:

- ✅ Create User
- ✅ Read User
- ✅ Update User
- ✅ Delete User

The infrastructure is managed using **Terraform**, while **Floci** runs locally through Docker to provide an AWS-compatible development environment.

The application logic is written in **Python** and runs inside AWS Lambda.

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │     Client / curl    │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP Request
                                    ▼
                         ┌──────────────────────┐
                         │     API Gateway      │
                         │                      │
                         │  /hello/{userId}     │
                         └──────────┬───────────┘
                                    │
                                    │ AWS Proxy
                                    ▼
                         ┌──────────────────────┐
                         │      AWS Lambda      │
                         │      users-api       │
                         │                      │
                         │   Python Handler     │
                         └──────────┬───────────┘
                                    │
                                    │ boto3
                                    ▼
                         ┌──────────────────────┐
                         │       DynamoDB       │
                         │                      │
                         │        users         │
                         │                      │
                         │   Partition Key:     │
                         │       userId         │
                         └──────────────────────┘

  

🔄 Request Flow
Client / curl
     |
     | HTTP Request
     v
API Gateway
     |
     | AWS_PROXY Integration
     v
AWS Lambda
     |
     | boto3
     v
DynamoDB
     |
     | Response
     v
AWS Lambda
     |
     v
API Gateway
     |
     v
Client
🛠️ Technologies Used
Technology	Purpose
Terraform	Infrastructure as Code
Floci	Local AWS-compatible development environment
Docker	Runs Floci locally
AWS API Gateway	API entry point
AWS Lambda	Serverless application logic
DynamoDB	NoSQL database
Python	Lambda application
boto3	AWS SDK for Python
AWS CLI	Resource management and testing
curl	API testing
Git	Version control
GitHub	Source code management
VS Code	Development environment
☁️ AWS Services Used
Amazon API Gateway

API Gateway is used as the entry point for the REST API.

Route:

ANY /hello/{userId}

API Gateway forwards requests to Lambda using an AWS_PROXY integration.

AWS Lambda

Lambda runs the Python application logic without requiring server management.

Lambda function:

users-api

The Lambda function implements:

Create User
Read User
Update User
Delete User
Amazon DynamoDB

DynamoDB is used as the NoSQL database.

Table:

users

Partition Key:

userId

Key Type:

String

Example item:

{
  "userId": "101",
  "name": "Sachin",
  "email": "sachin@example.com"
}

Billing mode:

PAY_PER_REQUEST
IAM / Lambda Permissions

Lambda permissions are configured so that API Gateway can invoke the Lambda function.

🐳 Floci Local Environment

This project uses Floci locally through Docker instead of creating production AWS resources.

Floci provides an AWS-compatible local development environment.

Default local endpoint:

http://localhost:4566

Floci runs inside Docker.

Example:

docker ps

The API Gateway local endpoint used for testing follows this format:

http://<api-id>.execute-api.localhost.floci.io:4566/hello/{userId}
📂 Project Structure
terraform-aws-serverless-api/
│
├── .gitignore
├── .terraform.lock.hcl
├── README.md
│
├── provider.tf
├── dynamodb.tf
├── lambda.tf
├── api_gateway.tf
├── integration.tf
├── route.tf
├── stage.tf
├── permission.tf
│
└── lambda_function.py
📄 Terraform Files
File	Purpose
provider.tf	Terraform provider and Floci configuration
dynamodb.tf	DynamoDB table configuration
lambda.tf	Lambda function configuration
api_gateway.tf	API Gateway configuration
integration.tf	API Gateway to Lambda integration
route.tf	API Gateway route
stage.tf	API Gateway stage
permission.tf	Lambda invocation permission
lambda_function.py	Python CRUD application
.gitignore	Files excluded from Git
README.md	Project documentation
⚙️ Terraform Workflow

Terraform is used to manage the infrastructure using Infrastructure as Code.

Terraform Configuration
        |
        v
terraform init
        |
        v
terraform validate
        |
        v
terraform plan
        |
        v
terraform apply
        |
        v
Infrastructure
🧰 Terraform Commands
Initialize Terraform
terraform init
Validate Terraform Configuration
terraform validate

Expected result:

Success! The configuration is valid.
Review Infrastructure Changes
terraform plan

Final verification:

No changes. Your infrastructure matches the configuration.

This confirms that the Terraform configuration matches the managed infrastructure.

Apply Infrastructure
terraform apply
Check Terraform State
terraform state list

This displays the resources currently managed by Terraform.

📦 Terraform Import

The existing DynamoDB table was imported into Terraform state.

Example:

terraform import aws_dynamodb_table.users users

This demonstrates how Terraform can begin managing infrastructure that already exists.

🗄️ DynamoDB Configuration

The DynamoDB table is configured with:

Table Name: users
Partition Key: userId
Key Type: String
Billing Mode: PAY_PER_REQUEST

Terraform configuration:

resource "aws_dynamodb_table" "users" {
  name         = "users"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"

  attribute {
    name = "userId"
    type = "S"
  }
}
🐍 Lambda Application

The Lambda function is written in Python.

File:

lambda_function.py

Handler:

lambda_function.lambda_handler

The application uses the AWS SDK for Python:

import boto3

The Lambda function communicates with DynamoDB using boto3.

🔄 CRUD Operations

The application implements all four CRUD operations.

1️⃣ CREATE USER — POST

Creates a new user.

Example:

curl -X POST \
http://<api-id>.execute-api.localhost.floci.io:4566/hello/102 \
-H "Content-Type: application/json" \
-d '{"userId":"102","name":"Rahul","email":"rahul@example.com"}'

Example response:

{
  "message": "User created successfully",
  "userId": "102"
}
2️⃣ READ USER — GET

Retrieves a user from DynamoDB.

Example:

curl \
http://<api-id>.execute-api.localhost.floci.io:4566/hello/102

Example response:

{
  "userId": "102",
  "name": "Rahul",
  "email": "rahul@example.com"
}
3️⃣ UPDATE USER — PUT

Updates an existing user.

Example:

curl -X PUT \
http://<api-id>.execute-api.localhost.floci.io:4566/hello/102 \
-H "Content-Type: application/json" \
-d '{"name":"Rahul","email":"rahul.new@example.com"}'

Example response:

{
  "message": "User updated successfully",
  "user": {
    "userId": "102",
    "name": "Rahul",
    "email": "rahul.new@example.com"
  }
}
4️⃣ DELETE USER — DELETE

Deletes an existing user.

Example:

curl -X DELETE \
http://<api-id>.execute-api.localhost.floci.io:4566/hello/102

Example response:

{
  "message": "User deleted successfully",
  "userId": "102"
}

After deletion, a GET request returns:

User not found
🧪 CRUD Testing

The complete CRUD workflow was tested successfully.

              POST
                |
                v
          Create User
                |
                v
              GET
                |
                v
           Read User
                |
                v
              PUT
                |
                v
          Update User
                |
                v
              GET
                |
                v
      Verify Updated User
                |
                v
            DELETE
                |
                v
          Delete User
                |
                v
              GET
                |
                v
         User Not Found
Testing Summary
Operation	HTTP Method	Purpose	Result
Create	POST	Create a new user	✅ Successful
Read	GET	Retrieve user details	✅ Successful
Update	PUT	Update user details	✅ Successful
Delete	DELETE	Delete user	✅ Successful
Verify Delete	GET	Confirm user no longer exists	✅ User Not Found
✅ Project Verification

The following components were successfully tested:

✅ Terraform initialization
✅ Terraform validation
✅ Terraform plan
✅ Terraform apply
✅ Terraform state management
✅ DynamoDB
✅ AWS Lambda
✅ API Gateway
✅ Floci
✅ Docker
✅ Python Lambda application
✅ boto3
✅ POST API
✅ GET API
✅ PUT API
✅ DELETE API
✅ CRUD workflow
✅ Git version control
🎯 Key DevOps Concepts Demonstrated
Infrastructure as Code
Terraform
Terraform State
Terraform Import
Terraform Plan
Terraform Apply
Terraform Validate
Serverless Architecture
API Gateway
AWS Lambda
DynamoDB
Docker
Floci
AWS CLI
REST APIs
CRUD Operations
Python
boto3
Git
GitHub
Infrastructure Testing
Troubleshooting