# AWS Cloud-Based E-Commerce Shopping Portal

Flask/Python e-commerce learning project designed around AWS.

Stack: Flask, HTML/CSS/JavaScript, AWS EC2, Elastic Beanstalk, VPC, IAM, S3, RDS MySQL, DynamoDB, ALB, Auto Scaling, CloudWatch, SNS and Lambda.

Local setup:
1. Install Python 3.12.
2. `pip install -r requirements.txt`
3. `python application.py`
4. Open http://localhost:5000

The app uses demo products when DynamoDB is not configured. AWS credentials and database passwords should be supplied through environment variables, never hard-coded.

This ZIP is a clean implementation based on the AWS Shopping Portal architecture discussed previously; it is not a byte-for-byte copy of an older ZIP.
