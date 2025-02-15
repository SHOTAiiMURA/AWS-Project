import boto3

aws_management_console = boto3.session.Seeion(profile_name="default")

ec2_console = aws_management_console.client('ec2')

#documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html
response = ec2_console.stop_instances(
    InstanceIds=[''],#specify ec2 instance id that you want to stop running.
)