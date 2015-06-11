from boto.s3.connection import S3Connection
from django_s3.settings import AWS_ACCESS_KEY_ID
from django_s3.settings import AWS_SECRET_ACCESS_KEY


def s3_connect():
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    return conn
