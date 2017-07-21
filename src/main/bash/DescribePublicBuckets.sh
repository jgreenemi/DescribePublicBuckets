#!/usr/bin/env bash

# DescribePublicBuckets
# A script using the AWS CLI to determine if any S3 buckets in your account are using Public ACLs.
#

# If you haven't updated your AWS CLI in a while and installed it through pip, go ahead and update it now.
#pip install --user --upgrade awscli

# List out all the buckets you have, store the results in a variable.
BUCKETS_LIST=(`aws s3api list-buckets --output text | grep BUCKETS | cut -f3`)
PUBLIC_READ_BUCKETS=()
PUBLIC_WRITE_BUCKETS=()

for BUCKET_NAME in "${BUCKETS_LIST[@]}"; do
  # Describe this bucket's ACLs. If there is a "GRANTS READ" line that is followed by a
  # "GRANTEE Group http://acs.amazonaws.com/groups/global/AllUsers" line, this means Everyone has read access
  # to the bucket.
  # Checks for the same group being present with "GRANTS WRITE".

  PUBLIC_ACL_INDICATOR="http://acs.amazonaws.com/groups/global/AllUsers"
  printf "%s\n" "Checking Bucket ${BUCKET_NAME}:"

  if echo `aws s3api get-bucket-acl --output text --bucket ${BUCKET_NAME} | grep -A1 READ` | grep -q "${PUBLIC_ACL_INDICATOR}"
    then
      printf "%s\n" "Bucket ${BUCKET_NAME} allows Everyone to list its objects!"
      PUBLIC_READ_BUCKETS+=(${BUCKET_NAME})
    else
      printf "%s\n" "No public read access detected."
  fi

  if echo `aws s3api get-bucket-acl --output text --bucket ${BUCKET_NAME} | grep -A1 WRITE` | grep -q "${PUBLIC_ACL_INDICATOR}"
    then
      printf "%s\n" "Bucket ${BUCKET_NAME} allows Everyone to write objects!"
      PUBLIC_WRITE_BUCKETS+=(${BUCKET_NAME})
    else
      printf "%s\n" "No public write access detected."
  fi

  printf "%s\n" "----"
done

printf "%s\n" ""
printf "%s\n" "Buckets with READ permission issues (if any):"
printf "%s\n" "${PUBLIC_READ_BUCKETS[@]}"

printf "%s\n" ""
printf "%s\n" "Buckets with WRITE permission issues (if any):"
printf "%s\n" "${PUBLIC_WRITE_BUCKETS[@]}"
