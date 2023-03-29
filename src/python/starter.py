from test.test_linear import test_linear_module
from test.test_conv2d import test_conv2d_module
from test.test_resnet import test_cifar10_inference_resnet20
from utils.analysis_helper import resnet20_layers

if __name__ == "__main__":
    # test_linear_module(128, 64, 16, 9.0, -0.35, False, 32, False, True)
    # test_conv2d_module(
    #     32, 32, 7, 3, False, 32, 16, 1.0, 0.0, 1, False, 2, 0, "im2col", False
    # )
    acc = {}
    for layer in resnet20_layers[:3]:
        accuracy = test_cifar10_inference_resnet20(layer)
        acc[layer] = accuracy
    print(acc)
    # test_cifar10_inference_resnet20("layer1.2.conv1")
