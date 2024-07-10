import os
import json

# Get the cluster metadata from environment variable
cluster_metadata = os.getenv('CLUSTER_METADATA')

# Load the JSON 
clusters = json.loads(cluster_metadata)

 # Process each cluster
for cluster in clusters:
  cluster_name = cluster['cluster-name']
  env_file = cluster['env-file']
  print(f"Cluster Name: {cluster_name}")
  print(f"Env File: {env_file}")
  # Example operation: Source the env file and run a command
  # os.system(f"source {env_file}")
  # os.system(f"your_command --cluster-name {cluster_name} --env-file {env_file}")
