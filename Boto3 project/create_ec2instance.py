#Import
import boto3
#open manengement console
aws_management_conle = boto3.session.Session(profile_name="default")
#open ec2 instance to create it
ec2_console = aws_management_conle.client('ec2')

#use documentation to get more informaiton (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html)
response = ec2_console.run_instances(
    ImageId='ami-053a45fff0a704a47',#ImageId is AMI ID (amazon machine image)
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)