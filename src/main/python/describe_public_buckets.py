import boto3
import logging

# describe_public_buckets
# A Python script to use Boto3 to list out any AWS S3 buckets in your account that have public access based on their
# ACLs, either Read or Write permissions.
#


def describe_public_buckets():

    # Set up logger. Feel free to change the logging format or add a FileHandler per your needs.
    logformat = ('%(asctime)s %(levelname)s [%(name)s] %(message)s')
    logging.basicConfig(level=logging.INFO,format=logformat)
    logger = logging.getLogger()
    logger.info('Starting.')

    s3client = boto3.client('s3')


if __name__ == '__main__':
    describe_public_buckets()
