import boto3

# Replace with your AWS credentials and region
dynamodb = boto3.client('dynamodb', region_name='<region name>', aws_access_key_id='<aws access key id>', aws_secret_access_key='<aws secret access key>')

# Specify the table name and the primary key of the item to delete
table_name = '<Table name>'

primary_key = {
    'ItemId': {'S': '<your-item-id>'}
}


response = dynamodb.delete_item(
    TableName=table_name,
    Key=primary_key
)

print("Item deleted successfully.")
