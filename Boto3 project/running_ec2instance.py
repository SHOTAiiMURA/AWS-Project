#Import all the modules and Libraries
import boto3
#Open Mangement Console
aws_management_console = boto3.session.Session(profile_name="default")
#Open EC2 Console
ec2_console = aws_management_console.client(service_name = 'ec2')
#Use boto3 documentation to get more information
result = ec2_console.describe_instance()
print(result)
