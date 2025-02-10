# IP_Collision_Detection_k8
IP Collision Detection and Reporting Tool for Kubernetes (ip-tool)




## 2. Check for Collisions:
### Save the output from multiple containers into a file (e.g., ip-list.txt) and run:
##### docker run --rm -v $(pwd)/ip-list.txt:/app/ip-list.txt ip-tool -checkcollision ip-list.txt

## 3. Deploy the Docker Image to GKE:
### Push the Docker image to Google Container Registry (GCR):
#### docker tag ip-tool gcr.io/gcpopenshift/ip-tool
#### docker push gcr.io/gcpopenshift/ip-tool


Create a Kubernetes deployment YAML file (ip-tool-deployment.yaml):
Apply the deployment:
kubectl apply -f ip-tool-deployment.yaml