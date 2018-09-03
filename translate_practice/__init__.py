import os
import boto3


if not os.environ.get('AWS_ACCESS_KEY_ID', None):
    from s3creds import AWSAccessKeyId
    os.environ['AWS_ACCESS_KEY_ID'] = AWSAccessKeyId
if not os.environ.get('AWS_SECRET_ACCESS_KEY', None):
    from s3creds import AWSSecretKey
    os.environ['AWS_SECRET_ACCESS_KEY'] = AWSSecretKey

boto3.resource('s3').Bucket('translate-app').download_file('TranslationAppCreds.json', 'TranslationAppCreds.json')
