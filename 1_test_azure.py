import azureml.core
from azureml.core import Workspace
from azureml.core import ComputeTarget, Datastore, Dataset


# Load the workspace
ws = Workspace() # TODO: Fill in your workspace

# Print Azure ML SDK version and workspace name
print("Ready to use Azure ML '{}' to work with '{}'.".format(azureml.core.VERSION, ws.name))

# Prints all the available compute targets
print("Compute Targets:")
for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print("\t{}: {}".format(compute.name, compute.type))
    
# Prints all the available datastores
print("Datastores:")
for datastore_name in ws.datastores:
    datastore = Datastore.get(ws, datastore_name)
    print("\t{}: {}".format(datastore.name, datastore.datastore_type))
    
# Prints all the available datasets
print("Datasets:")
for dataset_name in list(ws.datasets.keys()):
    dataset = Dataset.get_by_name(ws, dataset_name)
    print("\t{}".format(dataset.name))
