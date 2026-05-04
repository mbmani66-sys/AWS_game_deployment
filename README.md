HOW TO RUN

Clone the repository: git clone https://github.com/mbmani66-sys/shootthefruitgame.git
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
- Network configured using Amazon VPC with a public subnet
- Security Groups used to control inbound traffic (SSH and application ports)

 Deployment Steps
- Launched EC2 instance and configured Linux environment
- Connected to instance using SSH
- Cloned project repository from GitHub
- Installed Python and required dependencies
- Executed application on EC2 server

Process Flow
User → Route 53 → Internet → VPC → EC2 → Python Application

Tools & Services Used
- AWS EC2
- AWS Route 53
- AWS VPC
- Git & GitHub
- Linux (Ubuntu)
