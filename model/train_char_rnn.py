import argparse
import os
import random
import time
from azureml.core import Workspace, Dataset, Run, Experiment, RunConfiguration, ScriptRunConfig, Model
from torch.autograd import Variable
import torch.nn as nn
import torch
from tqdm import tqdm
# local 
from src.src import read_file, char_tensor, time_since, CharRNN, generate, all_characters, n_characters


# Get experiment run context and workspace details
run = Run.get_context()
ws = run.experiment.workspace

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('--dataset',       type=str, default='shakespeare.txt')
argparser.add_argument('--modelname',     type=str, default='char_rnn_model')
argparser.add_argument('--model',         type=str, default='gru')
argparser.add_argument('--n_epochs',      type=int, default=10)
argparser.add_argument('--print_every',   type=int, default=100)
argparser.add_argument('--hidden_size',   type=int, default=100)
argparser.add_argument('--n_layers',      type=int, default=2)
argparser.add_argument('--learning_rate', type=float, default=0.01)
argparser.add_argument('--chunk_len',     type=int, default=200)
argparser.add_argument('--batch_size',    type=int, default=100)
argparser.add_argument('--shuffle',       action='store_true')
argparser.add_argument('--cuda',          action='store_true')
args = argparser.parse_args()


# TODO: Download the dataset you uploaded earlier by using the Dataset class
# Use the recieved file_path as input to the "read_file()" function.
# NB! The filepath is a list and read_file expect a string



file, file_len = read_file() # <-- Input the file path


# Splitting dataset function
def random_training_set(chunk_len, batch_size):
    inp = torch.LongTensor(batch_size, chunk_len)
    target = torch.LongTensor(batch_size, chunk_len)
    for bi in range(batch_size):
        start_index = random.randint(0, file_len - chunk_len)
        end_index = start_index + chunk_len + 1
        chunk = file[start_index:end_index]
        if len(chunk[:-1]) < 200: continue
        inp[bi] = char_tensor(chunk[:-1])
        target[bi] = char_tensor(chunk[1:])
    inp = Variable(inp)
    target = Variable(target)
    if args.cuda:
        inp = inp.cuda()
        target = target.cuda()
    return inp, target

# Training function
def train(inp, target):
    hidden = decoder.init_hidden(args.batch_size)
    if args.cuda:
        hidden = hidden.cuda()
    decoder.zero_grad()
    loss = 0

    for c in range(args.chunk_len):
        output, hidden = decoder(inp[:,c], hidden)
        loss += criterion(output.view(args.batch_size, -1), target[:,c])

    loss.backward()
    decoder_optimizer.step()

    # return loss.data[0] / args.chunk_len
    return loss.data / args.chunk_len


# Initialize model
decoder = CharRNN(
    n_characters,
    args.hidden_size,
    n_characters,
    model=args.model,
    n_layers=args.n_layers,
)
decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=args.learning_rate)
criterion = nn.CrossEntropyLoss()

if args.cuda: decoder.cuda()

start = time.time()
all_losses = []
loss_avg = 0
print("Start training for {} epochs...".format(args.n_epochs))
for epoch in tqdm(range(1, args.n_epochs + 1)):
    loss = train(*random_training_set(args.chunk_len, args.batch_size))
    loss_avg += loss

    if epoch % args.print_every == 0:
        print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / args.n_epochs * 100, loss))
        print(generate(decoder, 'Wh', 100, cuda=args.cuda), '\n')

# Saving model to outputs/ in Azure ML
save_filename = "outputs/" + args.modelname + ".pt"
torch.save(decoder.state_dict(), save_filename)

# TODO: Use the Model class and the register method to upload the model to Azure ML



# Complete the run
run.complete()