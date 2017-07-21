## DescribePublicBuckets

A Bash and Python script (your choice of flavour) for listing out any AWS S3 buckets you own that have either Public Read or Public Write ACLs. Protect your data!

### Dependencies

For the Bash script:
```
awscli
```

For the Python script (pulled right from requirements.txt):
```
boto3==1.4.4
botocore==1.5.85
docutils==0.13.1
futures==3.1.1
jmespath==0.9.3
python-dateutil==2.6.1
s3transfer==0.1.10
six==1.10.0
```

For both scripts, AWS credentials will be used from `~/.aws/credentials` per the default behaviour of the `awscli` package and the `boto3` package, respectively.

### Using the Bash Version

1. Clone the repository, or just save the `src/main/bash/DescribePublicBuckets.sh` file locally.
```bash
$ wget -O https://github.com/jgreenemi/DescribePublicBuckets/raw/master/src/main/bash/DescribePublicBuckets.sh
```
1. Give the file executable permissions.
```bash
$ chmod +x DescribePublicBuckets.sh
```
1. If you haven't yet configured your AWS CLI credentials, do so now.
```bash
$ aws configure
```
1. Now you're ready - run the script and review the results.
```bash
$ ./DescribePublicBuckets.sh
```

### Using the Python Version

1. Clone the repository.
```bash
$ git clone https://github.com/jgreenemi/DescribePublicBuckets.git
```
1. Install the dependencies. Virtual environment lines optional but recommended.
```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
1. Now run the script and review the results.
```bash
$ python src/main/python/describe_public_buckets.py
```

### Problems

Please open an Issue on [this Github repository](https://github.com/jgreenemi/DescribePublicBuckets/issues) if you run into any problems.
