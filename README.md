# IP_Collision_Detection_k8
IP Collision Detection and Reporting Tool for Kubernetes (ip-tool)
########### Location: /home/mahima_10710568/IP_Collision_Detection_k8


## 1. build the Docker image after making this change:
##### docker build -t ip-tool .
###### docker run --rm ip-tool

## 2. Check for Collisions:
### Save the output from multiple containers into a file (e.g., ip-list.txt) and run:
##### docker run --rm -v $(pwd)/ip-list.txt:/app/ip-list.txt ip-tool -checkcollision ip-list.txt

### 3. Push the Docker image to Google Container Registry (GCR):
#### docker tag ip-tool gcr.io/gcpopenshift/ip-tool
#### docker push gcr.io/gcpopenshift/ip-tool

## 4. Deploy the Docker Image to GKE:
#### Create a Kubernetes deployment YAML file (ip-tool-deployment.yaml):
### Apply the deployment:
#### kubectl apply -f ip-tool-deployment.yaml


## 5. Now run the shells script
### write a script (e.g., collect-ips.sh) that collects IP addresses from all Kubernetes clusters and saves them into ip-list.txt.: collect-ips.sh
#### Once the IP addresses are collected, you can run the ip-tool.py script to check for collisions.: run-pipeline.sh
