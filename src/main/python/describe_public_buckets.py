#!/usr/bin/env python
# -*- coding: utf-8 -*-

# describe_public_buckets
# A Python script to use Boto3 to list out any AWS S3 buckets in your account that have public access based on their
# ACLs, either Read or Write permissions.
#

import boto3
import logging
import sys

from pprint import pprint


def describe_public_buckets():
    """
    Search your AWS account for S3 buckets that have public READ and WRITE permissions.
    The returned dictionary looks something like the following:

    {
      'READ': ['a-readable-bucket', 'another-readable-bucket'],
      'READ_ACP': ['a-bucket-with-readable-permissions', 'another-bucket-with-readable-permissions'],
    }

    :return: A dictionary with keys consisting of permission names, and values as a list of buckets that have that permission.
    :rtype: dict
    """

    # Set up logger. Feel free to change the logging format or add a FileHandler per your needs.
    logformat = ('%(asctime)s %(levelname)s [%(name)s] %(message)s')
    logging.basicConfig(level=logging.INFO, format=logformat)
    logger = logging.getLogger()
    logger.info('Starting.')

    public_acl_indicator = 'http://acs.amazonaws.com/groups/global/AllUsers'
    permissions_to_check = ['READ', 'WRITE']
    public_buckets = {}

    try:
        # Create S3 client, describe buckets.
        s3client = boto3.client('s3')
        list_bucket_response = s3client.list_buckets()

        for bucket_dictionary in list_bucket_response['Buckets']:
            bucket_acl_response = s3client.get_bucket_acl(Bucket=bucket_dictionary['Name'])

            for grant in bucket_acl_response['Grants']:
                for (k, v) in grant.iteritems():
                    if k == 'Permission' and any(permission in v for permission in permissions_to_check):
                        for (grantee_attrib_k, grantee_attrib_v) in grant['Grantee'].iteritems():
                            if 'URI' in grantee_attrib_k and grant['Grantee']['URI'] == public_acl_indicator:
                                if v not in public_buckets:
                                    public_buckets[v] = [bucket_dictionary['Name']]
                                else:
                                    public_buckets[v] += [bucket_dictionary['Name']]

        logger.info('The following buckets have public permissions:')
        logger.info(pprint(public_buckets))

        return public_buckets

    except:
        err = 'describe_public_buckets Failed! '
        for e in sys.exc_info():
            err += str(e)
        logger.error(err)

if __name__ == '__main__':
    describe_public_buckets()
