from kubernetes import client, config

# Load Kubernetes configuration from default location
config.load_kube_config()

# Create an instance of the Kubernetes API client
api_instance = client.CoreV1Api()

# List all pods in a namespace
namespace = 'default'
pods = api_instance.list_namespaced_pod(namespace)

for pod in pods.items:
    print(pod.metadata.name)

# Create a new deployment
deployment_manifest = {
    'apiVersion': 'apps/v1',
    'kind': 'Deployment',
    'metadata': {'name': 'my-deployment'},
    'spec': {
        'replicas': 3,
        'selector': {'matchLabels': {'app': 'my-app'}},
        'template': {
            'metadata': {'labels': {'app': 'my-app'}},
            'spec': {
                'containers': [{
                    'name': 'my-container',
                    'image': 'nginx:latest',
                    'ports': [{'containerPort': 80}]
                }]
            }
        }
    }
}

api_instance.create_namespaced_deployment(namespace, deployment_manifest)

# Scale a deployment
deployment_name = 'my-deployment'
scale_manifest = {
    'metadata': {'name': deployment_name},
    'spec': {'replicas': 5}
}

api_instance.patch_namespaced_deployment_scale(deployment_name, namespace, scale_manifest)

# Delete a deployment
api_instance.delete_namespaced_deployment(deployment_name, namespace)

# List all services in a namespace
services = api_instance.list_namespaced_service(namespace)

for service in services.items:
    print(service.metadata.name)

# Create a new service
service_manifest = {
    'apiVersion': 'v1',
    'kind': 'Service',
    'metadata': {'name': 'my-service'},
    'spec': {
        'selector': {'app': 'my-app'},
        'ports': [{'protocol': 'TCP', 'port': 80, 'targetPort': 80}]
    }
}

api_instance.create_namespaced_service(namespace, service_manifest)

# Delete a service
service_name = 'my-service'
api_instance.delete_namespaced_service(service_name, namespace)
