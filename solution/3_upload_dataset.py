import azureml.core
from azureml.core import Workspace, ComputeTarget, Datastore, Dataset


# TODO: Load the workspace using the from_config method
ws = Workspace.from_config()

# Print Azure ML SDK version and workspace name
print("Ready to use Azure ML '{}' to work with '{}'.".format(azureml.core.VERSION, ws.name))

# TODO: Fill in your dataset name and the dataset description.
# These will be used in the next todo.
dataset_name       = "shakespeare"
dataset_desciption = "This is a dataset filled with Shakespeare"

# Check if dataset already exist in the workspace
if dataset_name not in ws.datasets.keys():    
    print("Uploading '{}' ...".format(dataset_name))
    try:
        # Uploading and registering dataset
        default_ds = ws.get_default_datastore()
        default_ds.upload_files(files=['./data/shakespeare.txt'], # Upload the shakespeare file from data/
                                target_path='./',                 # Put it in a folder path in the datastore
                                overwrite=True,                   # Replace existing files of the same name
                                show_progress=True)               # Show progress while uploading

        # Creating a Dataset File object to store the stream
        shakespeare_data = Dataset.File.from_files(path=(default_ds, "./shakespeare.txt"))

        # TODO: Use the .register method on 'shakespeare_data' object to register your dataset to Azure ML
        # The name and description should be the 'dataset_name' and 'dataset_description' you provided in the last todo
        # HINT:
        #   https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets#register-datasets
        shakespeare_data.register(workspace=ws,
                                  name=dataset_name,
                                  description=dataset_desciption,
                                  create_new_version=False)

        print("Success uploading dataset: '{}'".format(dataset_name))
    except Exception as e:
        print("An error occured while uploading dataset: '{}'".format(dataset_name))
        print(e)
else:
    print("Dataset '{}' already exists. Please provide another name.".format(dataset_name))