import boto3

# Set up AWS credentials (access key and secret access key) and region
access_key = 'your_access_key'
secret_key = 'your_secret_key'
region = 'your_region'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

# List all S3 buckets
response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])

# Create a new S3 bucket
bucket_name = 'your_bucket_name'
s3.create_bucket(Bucket=bucket_name)

# Upload a file to an S3 bucket
file_path = 'path_to_file'
object_key = 'your_object_key'
s3.upload_file(file_path, bucket_name, object_key)

# Download a file from an S3 bucket
download_path = 'path_to_download_file'
s3.download_file(bucket_name, object_key, download_path)

# Delete a file from an S3 bucket
s3.delete_object(Bucket=bucket_name, Key=object_key)

# Delete an S3 bucket
s3.delete_bucket(Bucket=bucket_name)
