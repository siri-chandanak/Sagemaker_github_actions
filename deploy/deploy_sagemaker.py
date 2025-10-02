import boto3

ACCOUNT_ID = "<account_id>"  # Replace with your AWS account ID
REGION = "us-east-1"
IMAGE_URI = f"{ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/iris-model:latest"
MODEL_NAME = "iris-model"
ENDPOINT_CONFIG_NAME = "iris-endpoint-config"
ENDPOINT_NAME = "iris-endpoint"
ROLE_ARN = "<sagemaker_execution_role_arn>"  # Replace with your SageMaker execution role

sagemaker = boto3.client("sagemaker", region_name=REGION)

# Create model
sagemaker.create_model(
    ModelName=MODEL_NAME,
    PrimaryContainer={"Image": IMAGE_URI},
    ExecutionRoleArn=ROLE_ARN
)

# Create endpoint config
sagemaker.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": MODEL_NAME,
        "InitialInstanceCount": 1,
        "InstanceType": "ml.m5.large"
    }]
)

# Deploy endpoint
sagemaker.create_endpoint(
    EndpointName=ENDPOINT_NAME,
    EndpointConfigName=ENDPOINT_CONFIG_NAME
)

print(f"Deployment initiated for endpoint: {ENDPOINT_NAME}")