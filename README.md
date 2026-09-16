# ☁️ AWS Cloud-Based E-Commerce Shopping Portal

A cloud-based e-commerce web application built with **Python Flask** and deployed using **AWS cloud services**. The project demonstrates cloud application deployment, database integration, object storage, monitoring, IAM, and scalable AWS infrastructure.

## 🚀 Project Overview

This project is a shopping portal that allows users to browse products and interact with an e-commerce web application.

The application is designed to demonstrate how a web application can be hosted and integrated with multiple AWS services for application hosting, database management, storage, security, and monitoring.

## 🏗️ Architecture

```text
                    Users
                      |
                      v
              Flask Web Application
                      |
          +-----------+-----------+
          |                       |
          v                       v
      DynamoDB                 RDS MySQL
   Product Catalog        Customer / Order Data
          |
          |
          v
          S3
     Object Storage

       AWS Monitoring
             |
             v
        CloudWatch

Application Deployment
             |
             v
      Elastic Beanstalk
             |
             v
            EC2
