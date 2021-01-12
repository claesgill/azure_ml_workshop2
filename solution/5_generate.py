import os
import argparse
import string
import torch
from azureml.core import Workspace, Model
# local
from model.src.src import generate, CharRNN


# Loading the workspace
ws = Workspace.from_config()

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("--modelname",         type=str,   default="char_rnn_model")
argparser.add_argument("-p", "--prime_str",   type=str,   default="A")
argparser.add_argument("-l", "--predict_len", type=int,   default=100)
argparser.add_argument("-t", "--temperature", type=float, default=0.8)
argparser.add_argument("--cuda",              action="store_true")
args = argparser.parse_args()

all_characters = string.printable
n_characters = len(all_characters)

# TODO: Use the Model class to download your trained model
model = Model(workspace=ws, name=args.modelname)
model = model.download(target_dir='.', exist_ok=True)

# Loading the model and reconstructs the model
filename = "outputs/" + args.modelname + ".pt"
decoder_state = torch.load(filename)
char_rnn = CharRNN(n_characters, 100, n_characters, "gru", 2)
char_rnn.load_state_dict(decoder_state)

# Generate the predicted sequence based of the hyperparameters
predicted = generate(decoder=char_rnn,
                     prime_str=args.prime_str,
                     predict_len=args.predict_len,
                     temperature=args.temperature,
                     cuda=args.cuda)

print(predicted)
