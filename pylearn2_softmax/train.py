import os
import pylearn2
dirname = os.path.abspath('.')
with open(os.path.join(dirname, 'sr_dataset.yaml'), 'r') as f:
    dataset = f.read()
hyper_params = {'train_stop' : 50000}
dataset = dataset % (hyper_params)
print dataset

with open(os.path.join(dirname, 'sr_algorithm.yaml'), 'r') as f:
    algorithm = f.read()
hyper_params = {'batch_size' : 10000,
                'valid_stop' : 60000}
algorithm = algorithm % (hyper_params)
print algorithm