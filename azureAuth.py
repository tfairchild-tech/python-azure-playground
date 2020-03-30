from azure.common.client_factory import get_client_from_cli_profile
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient

# Create a Resource Management client
#resource_client = get_client_from_cli_profile(ComputeManagementClient)
#

# try this command on the command line and then use the output as input below:
# az login
# az ad sp create-for-rbac --sdk-auth > credentials.json

client = get_client_from_auth_file(ComputeManagementClient, auth_path='./credentials.json')