import os
from pylearn2.config import yaml_parse

dirname = os.path.abspath('.')
with open(os.path.join(dirname, 'sr_dataset.yaml'), 'r') as f:
    dataset = f.read()
hyper_params = {'train_stop' : 50000}
dataset = dataset % (hyper_params)
print dataset

with open(os.path.join(dirname, 'sr_model.yaml'), 'r') as f:
    model = f.read()

print model

with open(os.path.join(dirname, 'sr_algorithm.yaml'), 'r') as f:
    algorithm = f.read()
hyper_params = {'batch_size' : 10000,
                'valid_stop' : 60000}
algorithm = algorithm % (hyper_params)
print algorithm

with open(os.path.join(dirname, 'sr_train.yaml'), 'r') as f:
    train = f.read()
save_path = '.'
train = train %locals()
print train

train = yaml_parse.load(train)
train.main_loop()