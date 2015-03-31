import os
import pylearn2
dirname = os.path.abspath('.')
with open(os.path.join(dirname, 'sr_dataset.yaml'), 'r') as f:
    dataset = f.read()
hyper_params = {'train_stop' : 50000}
dataset = dataset % (hyper_params)
print dataset
