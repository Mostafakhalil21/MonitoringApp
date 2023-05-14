from kubernetes import client, config

config.load_kube_config()

api_client = client.ApiClient()

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-monitor-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-monitor-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-monitor-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-monitor-container",
                        image="009438978745.dkr.ecr.eu-north-1.amazonaws.com/my-monitor-app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

app_instance = client.AppsV1Api(api_client)
app_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment

)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-monitor-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-monitor-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)