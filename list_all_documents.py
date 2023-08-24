import boto3

# Replace with your AWS credentials and region
dynamodb = boto3.client('dynamodb', region_name='<region name>', aws_access_key_id='<insert>', aws_secret_access_key='<insert>')

# Specify the table name
table_name = '<Table Name>'

# Initialize an empty list to store item IDs
item_ids = []

# Paginate through all items in the table using scan
paginator = dynamodb.get_paginator('scan')
response_iterator = paginator.paginate(
    TableName=table_name
)

for response in response_iterator:
    items = response.get('Items', [])
    for item in items:
        item_id = item.get('ItemId', {}).get('S')
        if item_id:
            item_ids.append(item_id)

# Print all item IDs
print("All Item IDs:", item_ids)
