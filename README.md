# Work from local machine
In this task you will learn how you can work with Azure ML from your local machine using the Azure ML SDK library.

The main goal is to learn about Azure ML and the Azure ML SDK, but if would like to know more about the machinelearning algorithm and what it does, read the [Char RNN](#char-rnn) section.

> :warning: It's important that you go trough the [Requirements](#requirements) section to be able to do any of the tasks.

## Contents
0. [Char RNN](#char-rnn)
1. [Requirements](#requirements)
    1. [Installation](#installation)
2. [Getting started](#getting-started)
3. [Create a config](#create-a-config)
4. [Upload dataset](#upload-dataset)
5. [Train a model](#train-a-model)
6. [Register a trained model](#register-a-trained-model)
7. [Test trained model](#test-trained-model)
8. [What to do next](#what-to-do-next)
9. [Clean up](#clean-up)

## Char RNN
The machinelearning algorithm that is used in this workshop is the Char RNN model, and is taken from [this reposetory](https://github.com/spro/char-rnn.pytorch). It is a multi-layer *Recurrent Neural Network (RNN)* that uses the *GRU* gating mechanism which is quite similar to the *LSTM*. Both GRU and LSTM is a solution to short-term-memory which means that it uses it's internal gates to learn what data that is important given the context. Learning this way makes the model able to do predictions since it learns the context of what being fed into it. In our char rnn we predict characters given a sequence, but you could also make it predict full words in a sentence. 

As input, the trained model receives a sequence of characters where it tries to predict the next character in the given sequence, based of what data is has seen before. For training we use the `shakespeare.txt` dataset, from the data folder, so we expect the model to learn sequences in that context. So if we try to predict a sequence of range 100 character given a input sequence of `Hi` it might generate something like this:

> His hundgry father's dead deed,  
> To breathes then you, for spit them banishment yourself  
> From me? What

Beautiful, right?

I've also trained a model on some Skatteetaten job advertisement, and this was the result:

> Skatteetaten til enhver tid er er en av Norges behov for det.  
> Dersom du onsker a reservere deg fra oppforing pa offentlig sokerliste ma dette begrunnes.  
> Du vil bli varslet om reservasjon ikke tas til folg

#### Further readings
Here are some literature if you would like to learn more:
- [Char RNN repo](https://github.com/spro/char-rnn.pytorch)
- [RNN - illustrated guide to GRU and LSTM](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)


## Requirements
> :information_source: It is recomended to use a virtual envrionment for python, but it is not required.
> :warning: Run `bash install_requirements.sh` if on a clean VDI.

Before you start you need to check that you have the correct python version and all the packages you need.  
* Python v3.6.9 or higher
* pip3

You can check your python version in the terminal:  
```sh
python3 --version
```

### Installation
Copy and paste the following commands to install the requirements which includes all the packages you'll need for this workshop:  
```sh
cd local/
pip3 install -r requirements.txt
```

> :warning: This is only tested on Ubuntu 18.04. If you have issues you can try install the packages manually.

## Getting started
> :exclamation: Before you run the code it's important to note that all scripts include unfinished **todos**. These needs to be completed in each section to be able to run the script.

When you have verifyed that all [Requirements](#requirements) are in place, you can check your connection to Azure by running the script below.  
NB! Remember to fill in the **todos** first.
```sh
python3 1_test_azure.py
```
This script will output your *Azure ML version*, *compute targets*, *datastores* and *datasets* if any.

Now that you've verified the connection proceed to the next section, [Create a config](#create-a-config).

## Create a config
We need the [`Workspace`](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace) class to consume our workspace on Azure Cloud. In the previous section we used `Workspace.get()` method where we specified the `workspace_name` to get our workspace. Since we need to specify the workspace in each script, this becomes tedious over time. So, a solution is to use the `from_config` method instead to load the workspace from a config file. But before you can do that method you need to create the config using the `write_config` method.

Fill in the todos in `2_create_config.py`, and run your script to create the config:
```sh
python3 2_create_config.py
```

If your script worked, you should be able to locate a `.azureml/` folder containing a `.config.json` file.

#### Hints :bulb:
- Look for **3** todos.
- Check out the documentation for the [Workspace class](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace). 


## Upload dataset
In the [Datasets](https://github.com/claesgill/azure_ml_workshop#datasets) section you can learn how to upload a dataset manually into your workspace. However, in this section you'll learn how you can upload a dataset using the [Azure ML SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py), and don't worry you will also implement the `write_config` method to get use of your hard work from the previous section :wink:

Fill in the todos in `3_upload_dataset.py`, and run your script:
```sh
python3 3_upload_dataset.py
```

If your script ran successfully, you can visit your workspace at [https://ml.azure.com/](https://ml.azure.com/), and verify that your dataset exists in the **Datasets** page under Assets. You can also run `python3 1_test_azure.py` that will print your dataset name in the terminal.

#### Hints :bulb:
- Look for **3** todos.
- Check out the documentation for [register datasets](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets#register-datasets).

## Train a model
In this task you will upload and run the training script(`train_char_rnn.py`). You can read about what it does in the [Char RNN](#char-rnn) section. However, what it essentially does is that it trains a CharRNN model with the dataset you uploaded previously, and generates a trained model.

So, now that you have a dataset uploaded and ready to use, you need to make sure that it's included in the training script. This means that you have to implement the [Dataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.dataset.dataset?view=azure-ml-py) class using the `get_by_name` and `download` method.

Fill in the **FIRST** todo in `train_char_rnn.py` located in the `model` folder. 
NB! There is **2** todos here, but you only need to do the first one for this task.

Unfortunately there is no good way to check that your code is working by this point, but ask for help if you are unsure. We'll be happy to help you.

#### Hints :bulb:
- Look for **1** todo.
- In the `get_by_name` method the name input-field should be `name=args.dataset`
- Check out the [Dataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.dataset.dataset?view=azure-ml-py) class documentation and methods.

The next step is to work with the `4_deploy_to_azure.py` script. In this script you will se that we use an [Estimator](https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py) to create the python environment. The estimator/environment will be submitted to Azure using the [Experiment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py) class. Azure use the term experiments for each script you push to the cloud, and is quite convenient since it keeps track of all your runs which you can monitor in you [workspace](https://ml.azure.com).

For this task you will need a Compute Instance. If you don't have one already set up, you need to follow the steps in section [compute instance](https://github.com/claesgill/azure_ml_workshop/tree/issue_8_new_tasks#compute-instance) before you continue with the todos.

Fill in the todos in `4_deploy_to_azure.py`, and run your script:
```sh
python3 4_deploy_to_azure.py
```
> :coffee: This script will take some time to run the first time since it need to build the python environment in a docker container.

While your script runs, you can monitor that your experiment run successfully in the terminal. Another option is to monitor it in your [workspace](https://ml.azure.com). See the below steps.

_NB! You may want to hit **refresh** frequently in each of the following steps_

1. Navigate to the **Experiments** page and choose your experiment.
2. Click your latest run and navigate to the **Outputs + logs** tab. Note that all your outputfiles (if any) will appear here.
3. Expand **azureml-logs** and wait for **70_driver_log.txt** to show and click it when it does. In this log-file you watch all the outputs from the  training-script and verify that everything ran successfully.

#### Hints :bulb:
- Look for **4** todos.
- Check out the documentation for [Experiments](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py).
- Learn more about [Estimators](https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py) in the documentation.

## Register a trained model
In the previous section you traind your model, and you may have noticed that your model got saved. However, it got saved in the container environment in Azure ML in witch don't make it available for further usage. In order to make the model available we can use the `Model` class, and more specifically the `register` method to upload our model to Azure. The good thing about registering a model to Azure, is that you can keep track of all your versions. This can be very usefull when you are testing different hyperparameters to get the best possible model. But enough talk, let's dive into the code.

Fill in the todo in `train_char_rnn.py` located in the `model` folder. Run the `4_deploy_to_azure.py` script afterwards:
```sh
python3 4_deploy_to_azure.py
```

To verify that your model was successfully uploaded, navigate to the **Models** page and you should see your model with the same name as you gave it. You can click on it to see more details.

#### Hints :bulb:
- Look for **1** todo.
- The model is saved in the outputs folder in Azure ML.
- Check out the documentation for the [Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py) class.


## Test trained model
Now that you have trained and uploaded your model, it's time to test it and see how well it works. You can do this using the `5_generate.py` script. The only thing you'll need to do is to download the model you registered earlier using the `Model` class and `download` method.

Fill in the todo in `5_generate.py` and run it. Remember to specify your modelname:
```sh
python3 5_generate.py --modelname <your-model-name>
```

The script will output a predicted string based of the input-sequence, which is defaulted to the character `A`. The prediction string would probably not make any sense since we have only being training the model for 500 epochs. The important thing is that it predicts something, and feel free to play around with the input arguments for the script. Have a look at what flag you can sett and tune to get a more interesting/funny result.

| argument        | type   | default |
| :-------------- | :----- | :------ |
| `--prime_str`   | string | "A"     | 
| `--predict_len` | number | 100     |

There are other flags to set, but those are for other usecases so I wouldn't spend time on those.

#### Example tuning
```sh
python3 5_generate.py --modelname <your-model-name> --prime_str "Here" --predict_len 300
```

#### Hints :bulb:
- Look for **1** todo.
- If you uploaded multiple models you can specify a version number. I.e. `version=4`.
- Check out the methods in the [Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py#methods) class documentation.


## What to do next
If you reach this section, congrats and well done :clap: :tada:

But wait there is more! There are still a few more things you can do if you're up for it.

1. You can continue playing around with this setup and perhaps upload a different dataset to train a new model. You can ofc choose whatever text you want!
2. You can continue learning about Azure using the notebooks. In the root [README](https://github.com/claesgill/azure_ml_workshop#azure-ml-workshop-test_tube) you will find all the instructions you need!
 

## Clean up :coffee:
If you are completely done you can clean up you workspace. This means that you need to shut down or stop your compute instance for the reason that this is a pay-as-you-go service :money_with_wings:


1. In [Azure ML studio](https://ml.azure.com/), navigate to the **Compute** page and on the **Compute instances** tab choose your compute instanse.
    You can now choose one of the following options:  
    * Alt 1: Click **Stop** to shut it down.
    * Alt 2: Click **Delete** to remove it.
