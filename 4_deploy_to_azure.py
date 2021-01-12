import azureml
from azureml.core import Workspace, Experiment
from azureml.train.estimator import Estimator
azureml._restclient.snapshots_client.SNAPSHOT_MAX_SIZE_BYTES = 10 * 10**9 # 10GB


# Loading the workspace
ws = Workspace.from_config()

# Creating an Estimator which is the environment for your experiment
estimator = Estimator(
    source_directory="./model",
    entry_script="train_char_rnn.py",
    script_params={
        "--dataset": "",   # TODO: Specify the same dataset_name you provided earlier 
        "--modelname": "", # TODO: Specify your modelname
        "--n_epochs": 500
        },
    compute_target="", # TODO: Specify your compute target
    pip_packages=[
        "azureml-core",
        "azureml-dataprep",
        "azureml-train",
        "pandas",
        "torch",
        "torchvision",
        "tqdm",
        "Unidecode"
    ]
)

# TODO: Create a "Experiment" and use the submit method to submit the "estimator" object
# Recieve the return object of the submittet experiment and use the "wait_for_completion(show_output=True)" method.
# This will show you the logs for the submitted experiment



