

# import boto3

# # s3 = boto3.resource('s3', aws_access_key_id='AKIA3N2CFDTP6OZHB2NF', aws_secret_access_key= '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')

# # for bucket in s3.buckets.all():
# #     print(bucket)

# bucketName = "phdresults"
# Key = "learn.py"
# outPutname = "learn.py"

# s3 = boto3.client('s3', aws_access_key_id='AKIA3N2CFDTP6OZHB2NF', aws_secret_access_key= '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')
# s3.upload_file(Key,bucketName,outPutname)

import os
import sys
import boto3

# get an access token, local (from) directory, and S3 (to) directory
# from the command-line
local_directory = 'results'
bucket = 'system-a-001'
destination=''

client = boto3.client('s3', aws_access_key_id='AKIA3N2CFDTPQRPWUE3W', aws_secret_access_key= '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')

# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

    print(root)
    print(dirs)
    print(files)

    for filename in files:

        # construct the full local path
        local_path = os.path.join(root, filename)
        print(local_path)

        # construct the full Dropbox path
        relative_path = os.path.relpath(local_path, local_directory)
        print(relative_path)
        s3_path = os.path.join(destination, relative_path)
        print(s3_path)

        # relative_path = os.path.relpath(os.path.join(root, filename))

        print('Searching "%s" in "%s"' % (s3_path, bucket))
        try:
            client.head_object(Bucket=bucket, Key=s3_path)
            print("Path found on S3! Skipping %s..." % s3_path)

            # try:
                # client.delete_object(Bucket=bucket, Key=s3_path)
            # except:
                # print "Unable to delete %s..." % s3_path
        except:

            print("Uploading %s..." % s3_path)
            client.upload_file(local_path, bucket, s3_path)