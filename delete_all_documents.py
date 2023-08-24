import boto3
dynamodb = boto3.client('dynamodb', region_name='<region name>', aws_access_key_id='<insert>', aws_secret_access_key='<insert>')
table_name = '<Table Name>'
paginator = dynamodb.get_paginator('scan')
response_iterator = paginator.paginate(
    TableName=table_name
)
for response in response_iterator:
    items = response.get('Items', [])
    for item in items:
        item_id = item.get('ItemId', {}).get('S')
        if item_id:
            primary_key = {
                'ItemId': {'S': item_id}
            }
            response = dynamodb.delete_item(
                TableName=table_name,
                Key=primary_key
            )
            print("Item "+ item_id +" was deleted successfully.")
