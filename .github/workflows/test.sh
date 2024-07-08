#!/bin/bash

# Ensure the environment variable is properly assigned
cluster_metadata="$CLUSTER_METADATA"

# Print the received metadata for verification
echo "$cluster_metadata"

# You can now use the JSON string in your script
# For example, you could parse it with jq if needed
echo "$cluster_metadata" | jq '.'
