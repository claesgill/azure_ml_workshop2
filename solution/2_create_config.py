# TODO: Import Workspace from azureml core
from azureml.core import Workspace

# TODO: Create a Workspace instance and the get method to get your workspace
ws = Workspace.get("wp-claes-ml")

# TODO: Use the write_config() method to get the workspace config on your local machine
ws.write_config()