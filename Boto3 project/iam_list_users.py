# Import all the modules and libraries
import boto3
from pprint import pprint
#Oepn Management Console
aws_management_console = boto3.session.Session(profile_name="default")
#Oepen IAM Console
iam_console = aws_management_console.client(service_name='iam') #IAM is global service so that no specify region in here.

#Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
result = iam_console.list_users()
for each_user in result['Users']:
    print(each_user['UserName'])