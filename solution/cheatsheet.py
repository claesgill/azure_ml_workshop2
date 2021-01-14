##################################
# 1_test_azure.py
##################################
# TODO: Fill inn your workspace name
ws = Workspace(subscription_id="ec4e8801...",
               resource_group="testVDI",
               workspace_name="claes")

##################################
# 2_create_config
##################################
# TODO: Import Workspace from azureml core
from azureml.core import Workspace

# TODO: Create a Workspace instance and the get method to get your workspace
ws = Workspace(subscription_id="ec4e8801...",
               resource_group="testVDI",
               workspace_name="claes")

# TODO: Use the write_config() method to get the workspace config on your local machine
ws.write_config()

##################################
# 3_upload_dataset.py
##################################
# TODO: Load the workspace using the from_config method
ws = Workspace.from_config()

# TODO: Fill in your dataset name and the dataset description.
# These will be used in the next todo.
dataset_name       = "shakespeare"
dataset_desciption = "This is a dataset filled with Shakespeare"

# TODO: Use the .register method on 'shakespeare_data' object to register your dataset to Azure ML
# The name and description should be the 'dataset_name' and 'dataset_description' you provided in the last todo
# HINT:
#   https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets#register-datasets
shakespeare_data.register(workspace=ws,
                            name=dataset_name,
                            description=dataset_desciption,
                            create_new_version=False)

##################################
# train_char_rnn.py
##################################
# TODO: Download the dataset you uploaded earlier by using
# the Dataset class using the 'get_by_name' and 'download' methods.
# Use the recieved file_path as input to the 'read_file()' function.
# HINT: 
#   In the 'get_by_name' method the name input-field should be 'name=args.dataset'
#   The filepath is a list and 'read_file' expect a string
#   https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.dataset.dataset?view=azure-ml-py
dataset = Dataset.get_by_name(ws, name=args.dataset)
file_path = dataset.download(target_path='.', overwrite=True)

file, file_len = read_file(file_path[0]) # TODO: Input the file path here

# TODO: Use the Model class and the 'register' method to upload the model to Azure ML
# HINT:
#   https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py
model = Model.register(workspace=ws,
                       model_name=args.modelname,
                       model_path="outputs/")


##################################
# 4_deploy_to_azure.py
##################################
script_params={
    "--dataset": "shakespeare",         # TODO: Specify the same dataset_name you provided earlier 
    "--modelname": "shakespeare_model", # TODO: Specify your modelname
    "--n_epochs": 2000                  # TODO: Set number of epochs
    },
compute_target="ci-claes", # TODO: Specify your compute target

# TODO: Create a "Experiment" and use the 'submit' method to submit the 'estimator' object
# Recieve the return object of the submittet experiment and use the 'wait_for_completion(show_output=True)' method.
# This will show you the logs for the submitted experiment
# HINT:
#   https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py
experiment = Experiment(workspace=ws, name="demo-skatteetaten-dataset")
run = experiment.submit(config=estimator)
run.wait_for_completion(show_output=True)

##################################
# 5_generate.py
##################################
# TODO: Use the Model class and the 'download' method to download your trained model
# HINT:
#   https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py#methods
model = Model(workspace=ws, name=args.modelname)
model = model.download(target_dir='.', exist_ok=True)
