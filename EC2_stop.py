
import boto3
instances = ['i-07c4912097f787037']
def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    ec2.stop_instances(InstanceIds=instances)
