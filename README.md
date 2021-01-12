# Azure ML Workshop :test_tube: 
In this workshop you are going to set up a [Compute instance](#compute-instance) with it's own [Datasets](#datasets) so that you can [Train and register models](#train-and-register-models). Finally, you will learn about [Pipeline](#pipeline)s and how to set it up.  

To get started, follow the [Contents](#contents) chronologically and complete each step in the sections before you move on.

> :information_source: If you want to take a longer break or you are finished with the workshop remember to visit the [Clean up](#clean-up-coffee) section.

## Contents
0. [Before you start](#before-you-start)
1. [Getting started](#getting-started)
2. [Compute instance](#compute-instance)  
    1. [Create a compute instance](#create-a-compute-instance)
    2. [Testing and verifying compute instance](#testing-and-verifying-compute-instance)
3. [Datasets](#datasets)
    1. [Creating a dataset](#creating-a-dataset)
4. [Train and register models](#train-and-register-models)
5. [Pipeline](#pipeline)
    1.  [Why build pipelines?](#why-build-pipelines)
    2. [Creating a pipeline](#creating-a-pipeline)
6. [Train from local machine](#train-from-local-machine)
7. [Clean up](#clean-up-coffee)
8. [Issues](#issues)
9. [Disclaimer](#disclaimer)

## Before you start
It's important to note that this is a workshop that's not fully tested, meaning it will contain minor bugs and probably a lot of typos in the READMEs.

A second note is that you have limited time completing the workshop and you might not be able to complete it in time, and that's ok. If you want to continue at home you can register a student account with free credits at [https://azure.microsoft.com/en-us/free/students/](https://azure.microsoft.com/en-us/free/students/).

Have fun and please ask questions if something is unclear or you need help! We'll be happy to guide you!

## Getting started
1. Login to the [Azure Portal](https://portal.azure.com/)
2. Go to *Subscriptions* and verify that `AI Studentlab` is available. If not, untick the box **Show only subscriptions selected in the global subscriptions filter** or ask for help.
3. Click the `AI Studentlab` subscription and go to *Resources* and click the `ml_aisl` resource.
4. Then click **Launch Now** to go to Azure Machine Learning studio. Alternatively you can open [Azure Machine Learning studio](https://ml.azure.com), where you need to sign in with the following selected:  
    * **Directory**: Skatteetaten
    * **Subscription**: AI Studentlab
    * **Machine Learning workspace**: ml-aisl
5. The next step is to create a [Compute instance](#compute-instance)

Feel free to explore Azure ML Studio.

> :information_source: If you are prompted to sign in again in this workshop it just means that your token has expired and you just need to use your Microsoft account associated with your Azure subscription to sign back in.

## Compute instance
> :information_source: Compute instances is a managed cloud-based workstation used by data scientists.

![other_image](images/overview.png)

### Create a compute instance
1. In [Azure ML studio](https://ml.azure.com/), navigate to **Compute** and chose **Compute instances**. Then create a **new** compute instance.
2. Fill in the following:  
    * **Compute name**: <your_name>workshop
    * **Region**: westeurope 
    * **Virtual machine type**: CPU (Central Processing Unit)
    * **Virtual machine size**: Standard_D1

> :warning: You need to provide the correct information otherwise you may encounter problems later in this workshop.

3. Make sure your information is correct before you click **create**.
4. For the next steps see section [Testing and verifying compute instance](#testing-and-verifying-compute-instance).

### Testing and verifying compute instance
> :information_source: In this workshop we are using python notebooks to run our code. To make notebooks available on our compute instance we need to clone this repository into it. We will also run some small test to check that everything works as expected.

1. In [Azure ML studio](https://ml.azure.com/), on the **Compute** page for your workspace, view the **Compute instances** tab, and if necessary, click **Refresh** periodically until the compute instance you created in the previous step has started. This may take a couple of minutes so that might be a good time for a :coffee: break.
2. Click your compute instance's Jupyter link to open **Jupyter** Notebooks in a new tab. You might see a warning pop-up where you need to click **Yes** to continue.
3. In the notebook environment, upper right corner, create a **new** Terminal. This will open a new tab with a command shell.
4. The Azure ML SDK is already installed in the compute instance image, but it's worth ensuring you have the latest version, with the optional packages you'll need in this workshop. Enter the following command to update the SDK packages:
```sh
pip install --upgrade azureml-sdk[notebooks,automl,explain]
```
You may see some warnings and errors as the package dependencies are installed, but you can ignore these.

5. Next, run the following commands to change the current directory to the Users directory, and retrieve the notebooks you will use in the workshop:
```sh
cd Users/<your name> # i.e cd Users/Jon.Doe/
git clone https://github.com/claesgill/azure_ml_workshop
```
6. After the command has completed, close the terminal tab and view the home page in your Jupyter notebook file explorer. Then open the `Users/<your name>` folder and go to the `azure_ml_workshop` folder. Here you should have everything you need to continue this workshop.
7. To check that everything works as expected, go to the `notebooks` folder and open the `1_testing_workspace.ipynb` notebook. Then read all the notes in the notebook, and run each code cell in turn.
8. When you have finished running the code in the notebook, on the **File** menu, click **Close and Halt** to close it and shut down its Python kernel.
9. Now, you can create a dataset. See [Datasets](#datasets).

## Datasets
> :information_source: Working with machine learning usually requires big chunks of data, and Azure ML provides multiple datastores for our usage. Your Azure ML workspace already includes two datastores based on the Azure Storage account that was created along with the workspace. These are used to store notebooks, configuration files and data. Where datasets represent specific data files or tables that you plan to work with. In [Azure ML studio](https://ml.azure.com/), you can navigate to the **Datastores** page to see the available datastores.

### Creating a dataset
1. In [Azure ML studio](https://ml.azure.com/), navigate to the **Datasets** page.
2. Create a **new** dataset from **web files**, using the following settings:
    * **Basic Info**:
        - **Web URL**: [https://aka.ms/diabetes-data](https://aka.ms/diabetes-data)
        - **Name**: diabetes dataset (be careful to match the case and spacing)
        - **Dataset type**: Tabular
        - **Description**: Diabetes data
    * **Settings and preview**:
        - **File format**: Delimited
        - **Delimiter**: Comma
        - **Encoding**: UTF-8
        - **Column headers**: Use headers from first file
        - **Skip rows**: None
    * **Schema**:
        - Include all columns other than Path
        - Review the automatically detected types
    * **Confirm details**:
        - Do **not** profile the dataset after creation
3. After the dataset has been created, you can open it to see a sample of the data. Click the **diabetes dataset** and go to the **Explore** tab. The data represents details from patients who have been tested for diabetes, and is the dataset we will use in this workshop.
4. Great! Now you are all set to [Train and register models](#train-and-register-models).

## Train and register models
> :information_source: In this task, you're going to train and register a model to Azure using a notebook.

1. In [Azure ML studio](https://ml.azure.com/), navigate to the **Compute** page and on the **Compute instances** tab, verify that your compute instance is running.
2. When the compute instance is running, click the *Jupyter* link to open the Jupyter home page in a new browser tab.
3. In the Jupyter home page, go to the `Users/<your name>/azure_ml_workshop/notebooks` folder and open the `2_training_models.ipynb` notebook. Then read all the notes in the notebook, and run each code cell in turn. You may see some warnings while running the cells, but these can be ignored.
4. When you have finished running the code in the notebook, on the **File** menu, click **Close and Halt** to close it and shut down its Python kernel.
5. Now it's time to learn about [Pipeline](#pipeline)s.

## Pipeline
> :information_source: If you are familiar with pipelines you can skip the [Why build pipelines?](#why-build-pipelines) section and go straight to [Creating a pipeline](#creating-a-pipeline).

### Why build pipelines?
With pipelines, you can optimize your workflow with simplicity, speed, portability, and reuse. Breaking it down to independent steps allow multiple data scientists to work on the same pipeline at the same time.

Using distinct steps makes it possible to rerun only the steps you need as you tweak and test your workflow. Once the pipeline is designed, there is often more fine-tuning around the training loop of the pipeline. When you rerun a pipeline, the execution jumps to the steps that need to be rerun, such as an updated training script, and skips what hasn't changed. The same paradigm applies to unchanged scripts and metadata.

With Azure ML, you can use distinct toolkits and frameworks for each step in your pipeline. Azure coordinates between the various compute targets you use so that your intermediate data can be shared with the downstream compute targets easily. The following figure illustrates a pipeline.

![image](images/pipeline.png)

An Azure ML pipeline is an independently executable workflow of a complete machine learning task. Subtasks are encapsulated as a series of steps within the pipeline. An Azure ML pipeline can be as simple as one that calls a Python script, so may do just about anything.

A typical pipeline contains:
* Data preparation (download dataset, normalize ++)
* Training configuration (arguments, parameters ++)
* Training and validating 
* Deployment, including versioning, scaling, provisioning, and access control

### Creating a pipeline
> :information_source: In this task, you'll create a pipeline to train and register a model using a notebook. Note that this task will create a **compute cluster** automatically for you.

1. In [Azure ML studio](https://ml.azure.com/), navigate to the **Compute** page and on the **Compute instances** tab, verify that your compute instance is running.
2. When the compute instance is running, click the *Jupyter* link to open the Jupyter home page in a new browser tab.
3. In the Jupyter home page, go to the `Users/azure_ml_workshop` folder and open the `3_creating_pipeline.ipynb` notebook. Then read all the notes in the notebook, and run each code cell in turn.
4. When you have finished running the code in the notebook, on the **File** menu, click **Close and Halt** to close it and shut down its Python kernel.
5. If you have completed all sections and don't want to play around anymore visit the [Clean up](#clean-up-coffee) section.

## Train from local machine
Checkout the README inside the **local/** folder.

## Clean up :coffee:
If you want to take a longer break or you are finished with the workshop, it's important that you either *shut down* or *delete* your compute instance and cluster since this is a pay-as-you-go service :money_with_wings:

1. In [Azure ML studio](https://ml.azure.com/), navigate to the **Compute** page and on the **Compute instances** tab choose your compute instanse.
    You can now choose one of the following options:  
    * Alt 1: Click **Stop** to shut it down.
    * Alt 2: Click **Delete** to remove it.
2. In [Azure ML studio](https://ml.azure.com/), navigate to the **Compute** page and on the **Compute clusters** tab click your compute cluster.
    You can now choose one of the following options:  
    * Alt 1: Choose the **Edit** tab and set **Minimum number of nodes** to 0. This will shut the cluster down.
    * Alt 2: Click **Delete** to remove it.

## Issues
If you experience any problems following this workshop or have suggestion for a change, please file a [issue](https://github.com/claesgill/azure_ml_workshop/issues).

## Disclaimer
This repo is heavily based of, and a very compressed version of @shoresh57's [AI-ML-Workshop-Azure](https://github.com/shoresh57/AI-ML-Workshop-Azure/) repository. If you want a deeper dive into Azure ML I suggest you check out his repository that contains very thorough tutorials.
