import argparse
import torch.nn.functional as F

from train import train_and_eval
from train import register_general_args
from gcn import GCN


def gcn_model_fn(args, data):
    return GCN(data.graph,
                data.n_feats,
                args.n_hidden,
                data.n_classes,
                args.n_layers,
                F.relu,
                args.dropout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GCN')
    register_general_args(parser)
    parser.add_argument("--n-hidden", type=int, default=16,
            help="number of hidden gcn units")
    parser.add_argument("--n-layers", type=int, default=1,
            help="number of hidden gcn layers")
    parser.add_argument("--dropout", type=float, default=0.5,
            help="dropout probability")
    args = parser.parse_args()
    print('Parsed args:', args)

    train_and_eval(gcn_model_fn, args)