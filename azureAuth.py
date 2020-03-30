from azure.common.client_factory import get_client_from_cli_profile
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient

# Create a Resource Management client
#resource_client = get_client_from_cli_profile(ComputeManagementClient)
#
# List resource groups as an example. The only limit is what role and policy are assigned to this MSI token.
#for resource_group in resource_client.resource_groups.list():
#    print(resource_group.name)


client = get_client_from_auth_file(ComputeManagementClient, auth_path='./credentials.json')
