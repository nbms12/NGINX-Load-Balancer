AIM: Design and deploy cotainers in Nginx  which can work as a load balancer/ reverse proxy and will ditribute traffic among various containers runs on same port , if one of container is down , other one is working. 

# DOCKER COMPOSE 
docker -compose Install: 

Docker Compose Installation
----------------------------------------
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

ls /usr/local/bin/

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version
............

docker-compose up -d --build

docker ps -a


# app running on ec2 public ip 


# 2 containers are stopped ,  but one contianer remain in running state since contianer " bf1472535ea5 " is only one . 

![image](https://github.com/user-attachments/assets/ae1c9367-26bb-4ddf-9f47-f1c7b89cc42d)


![image](https://github.com/user-attachments/assets/76ea1c65-7307-49ec-aa81-303ae7b21494)
