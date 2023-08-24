# dynamodb-python-scripts
```markdown
# DynamoDB Item Deletion Script

This script demonstrates how to use the Boto3 library to delete items from an AWS DynamoDB table.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This script utilizes the Boto3 library to delete items from an AWS DynamoDB table. It uses pagination to scan through the items and delete each item based on its primary key.

## Prerequisites

- Python 3.x
- AWS Account
- AWS Access Key ID and Secret Access Key with necessary DynamoDB permissions

## Installation

1. Clone this repository.
2. Install the required dependencies using pip:
   ```
   pip install boto3
   ```

## Usage

1. Open the `delete_dynamodb_items.py` script.
2. Fill in the following details:
   - AWS region name (`region_name`)
   - AWS access key ID (`aws_access_key_id`)
   - AWS secret access key (`aws_secret_access_key`)
   - DynamoDB table name (`table_name`)
3. Run the script using the following command:
   ```
   python delete_dynamodb_items.py
   ```

## Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact [your email here].

```
