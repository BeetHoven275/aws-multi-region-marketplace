# AWS Multi-Region Marketplace Project

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A high-availability marketplace web application deployed across multiple AWS regions, featuring custom authentication and cross-region redundancy.

## 🌟 Project Highlights

- **Multi-Region Architecture**: Deployed across N. Virginia (us-east-1) and Ohio (us-east-2)
- **Custom Authentication**: Flask-based auth system replacing AWS Cognito
- **High Availability**: Transit Gateway + VPC Peering for cross-region communication
- **Full-Stack Solution**: Complete marketplace with user management and product catalog
- **Sandbox Innovation**: Creative workarounds for AWS Academy limitations

## 📚 Documentation

Full project documentation with architecture details, implementation challenges, and solutions:

📄 [AWS_MultiRegion_Marketplace_Documentation.docx](./AWS_MultiRegion_Marketplace_Documentation.docx)
📄 [Backend_File_By_Python](./app-backen.py)
📄 [Frontend_File_By_HTML+Javascript+CSS](./App.html)

## 🏗️ Architecture Overview


```mermaid
graph LR
    A[Users] --> B[Load Balancer<br/>us-east-1]
    A --> C[Load Balancer<br/>us-east-2]
    B --> D[Web App<br/>N. Virginia]
    C --> E[Web App<br/>Ohio]
    D --> F[users.json]
    E --> F
    D --> G[S3 Placeholder<br/>Product Images]
    E --> G
    D <--> H[Transit Gateway]
    E <--> H
