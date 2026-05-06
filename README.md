HOW TO RUN

Clone the repository: git clone
 https://github.com/mbmani66-sys/shootthefruitgame.git
cd shootthefruitgame

Install the dependencies
pip install pygame

To Run the game in Terminal
python3 shootthefruit.py

AWS Cloud Deployment of Shoot the fruit game.
This project is deployed on AWS.

AWS Architecture
- Domain routing handled using Amazon Route 53
- Application hosted on Amazon EC2 (Ubuntu server)
- Network configured using Amazon VPC with a public
 subnet
- Security Groups used to control inbound traffic
 (SSH and application ports)
-Configured S3 standard storage service to deploy the 
front end part.
-For the backend and server part EC2 instance is 
configured.
-from the elastic computing cloud application artifact
file is pushed to docker container and
-RDS database is setted up to handle the application
data. 


 Deployment Steps
- Pushed Python application code to GitHub repository
-GitHub Actions automatically triggers on push, builds
Docker image, and prepares deployment.
-Application is deployed to Amazon EC2 where it runs 
inside a Docker container.
-User access is routed via Amazon Route 53 to the 
running application. 

Tools & Services Used
- AWS EC2
- AWS Route 53 Launched EC2 instance and configured Linux environment
- Connected to instance using SSH
- Cloned project repository from GitHub
- Installed Python and required dependencies
- Executed application on EC2 server
- AWS VPC
- Git & GitHub Actions
- Docker

## 🏗️ Architecture Diagram

![Architecture](architecture.png)
