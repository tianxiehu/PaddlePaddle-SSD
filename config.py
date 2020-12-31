# Data shape
image_shape = [3, 300, 300]
# Minibatch size.
batch_size = 32
# train epoch number.
epoc_num = 300
# image mean.
img_mean = 127.5
# image std.
img_std = 0.007843
# optimizer parameter.
lr = 1e-3
lr_epochs = [40, 60, 80, 100]
lr_decay = [1, 0.5, 0.25, 0.1, 0.01]
ap_version = '11point'
# character class num.
class_num = 3
# use model name，resnet_ssd、mobilenet_v2_ssd、mobilenet_v1_ssd、vgg_ssd
use_model = 'vgg_ssd'
# data label/
label_file = 'dataset/label_list'
# The list file of images to be used for training.
train_list = 'dataset/trainval.txt'
# The list file of images to be used for testing.
test_list = 'dataset/test.txt'
nms_threshold = 0.45
# Save model path
persistables_model_path = 'models/%s/persistables' % use_model
infer_model_path = 'models/%s/infer' % use_model
# The init model file of directory.
pretrained_model = 'pretrained/vgg_ssd_pascalvoc'
# Whether use GPU to train.
use_gpu = True
# Whether use parallel to train.
parallel = True
# Whether user multiprocess to reader data.(Windows can't use)
use_multiprocess = False
# user number workers reader data.
num_workers = 6


def print_value():
    keys = ['image_shape', 'batch_size', 'epoc_num', 'img_mean', 'img_std', 'lr', 'lr_epochs', 'lr_decay', 'ap_version',
            'class_num', 'use_model', 'label_file', 'train_list', 'test_list', 'nms_threshold',
            'persistables_model_path',
            'infer_model_path', 'pretrained_model', 'use_gpu', 'parallel', 'use_multiprocess', 'num_workers']

    for key in keys:
        print("%s: %s" % (key, eval(key)))
