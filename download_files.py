import boto3

# Configure the DigitalOcean Spaces endpoint URL
endpoint_url = 'https://fra1.digitaloceanspaces.com'

# Specify your DigitalOcean Spaces credentials
access_key = 'DO00X4ND2YZ9YVZEY9EN'
secret_key = '/U77OrTYPrb9AJ64Y9/PL3Kv963xYgBnJ15CJgpjPeE'

# Specify the bucket and folder name
bucket_name = 'cxr'
folder_name = 'Expert-Source-Calls/jan/'

# Specify the local directory path where you want to save the downloaded files
local_directory_path = '/home/bharat/cxr-call/'

# Create a Boto3 S3 client with the custom endpoint URL
s3_client = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

def download_files_from_folder(bucket, folder, local_directory, num_files):
    # List objects in the folder
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=folder)

    # Download specified number of files from the folder
    downloaded_files = 0
    for obj in response['Contents']:
        if downloaded_files >= num_files:
            break
        file_name = obj['Key']
        local_file_path = local_directory + file_name[len(folder):]
        s3_client.download_file(bucket, file_name, local_file_path)
        print(f'Downloaded: {file_name}')
        downloaded_files += 1

if __name__ == '__main__':
    num_files_to_download = 10
    download_files_from_folder(bucket_name, folder_name, local_directory_path, num_files_to_download)
