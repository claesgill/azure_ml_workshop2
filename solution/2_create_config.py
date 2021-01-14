# HINT: https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py

# TODO: Import Workspace from azureml core
from azureml.core import Workspace

# TODO: Create a Workspace instance and the get method to get your workspace
ws = Workspace(subscription_id="ec4e8801...",
               resource_group="testVDI",
               workspace_name="claes")

# TODO: Use the write_config() method to get the workspace config on your local machine
ws.write_config()