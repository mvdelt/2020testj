# -*- coding: utf-8 -*-
"""
From scratch implementation of the famous ResNet models.
The intuition for ResNet is simple and clear, but to code
it didn't feel super clear at first, even when reading Pytorch own
implementation. 

Video explanation: 
Got any questions leave a comment on youtube :)

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*    2020-04-12 Initial coding
"""

import torch
import torch.nn as nn


class block(nn.Module):
    def __init__(
        self, in_channels, intermediate_channels, identity_downsample=None, stride=1
    ):
        super(block, self).__init__()
        self.expansion = 4
        self.conv1 = nn.Conv2d(
            in_channels, intermediate_channels, kernel_size=1, stride=1, padding=0
        )
        self.bn1 = nn.BatchNorm2d(intermediate_channels)
        # i. stride=2 인경우에 첫번째 conv 말고 요 두번째conv 에서 stride 2 를 적용하나보네. 
        # 뭐 그렇게하긴해야댈듯. 왜냐면 첫번째랑 세번째 conv는 1x1 conv라서 거기서 stride 2 적용하는것보단 요 3x3 conv 에서 stride 2 적용하는게 정보 손실 줄이는데 좀더 낫겠네. 
        self.conv2 = nn.Conv2d(
            intermediate_channels,
            intermediate_channels,
            kernel_size=3,
            stride=stride,
            padding=1,
        )
        self.bn2 = nn.BatchNorm2d(intermediate_channels)
        self.conv3 = nn.Conv2d(
            intermediate_channels,
            intermediate_channels * self.expansion,
            kernel_size=1,
            stride=1,
            padding=0,
        )
        self.bn3 = nn.BatchNorm2d(intermediate_channels * self.expansion)
        self.relu = nn.ReLU()
        self.identity_downsample = identity_downsample
        self.stride = stride

    def forward(self, x):
        identity = x.clone()

        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.bn3(x)

        if self.identity_downsample is not None:
            identity = self.identity_downsample(identity)

        x += identity
        x = self.relu(x)
        return x


class ResNet(nn.Module):
    def __init__(self, block, layers, image_channels, num_classes):
        super(ResNet, self).__init__()
        self.in_channels = 64
        self.conv1 = nn.Conv2d(image_channels, 64, kernel_size=7, stride=2, padding=3)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        # Essentially the entire ResNet architecture are in these 4 lines below
        self.layer1 = self._make_layer(
            block, layers[0], intermediate_channels=64, stride=1
        )
        self.layer2 = self._make_layer(
            block, layers[1], intermediate_channels=128, stride=2
        )
        self.layer3 = self._make_layer(
            block, layers[2], intermediate_channels=256, stride=2
        )
        self.layer4 = self._make_layer(
            block, layers[3], intermediate_channels=512, stride=2
        )

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512 * 4, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc(x)

        return x

    # i. resnet 논문의 Table 1. 에서 대괄호 x N 부분 만들어주는 함수. (N이 요기 두번째인풋인자인 num_residual_blocks 인거지.)
    def _make_layer(self, block, num_residual_blocks, intermediate_channels, stride):
        identity_downsample = None
        layers = []

        # Either if we half the input space for ex, 56x56 -> 28x28 (stride=2), or channels changes
        # we need to adapt the Identity (skip connection) so it will be able to be added
        # to the layer that's ahead
        # i. 요 if문 필요없는것같은데?? 지금 resnet 50,101,152에대해서만 구현하고있는듯한데,
        #    resnet50,101,152에서는 어차피 요 if문 조건 필요없고,
        #    resnet18,34를 구현한다해도 걍 첫번째 _make_layer호출할때만 identity_downsample=None으로 해주면 될듯.
        if stride != 1 or self.in_channels != intermediate_channels * 4:  
            identity_downsample = nn.Sequential(
                # i. resnet논문 p.4 우상단 내용 중 옵션B, 즉 eq.2 의 구현임. x의 디멘션과 F의아웃풋의 디멘션을 맞춰주는거.(여기서 즉 resnet논문에서 '디멘션' 이라 함은, 그냥 피쳐맵(conv연산의 결과)의 채널수 말하는거임. 스페이셜디멘션이라하면 피쳐맵의 가로세로 길이를 말하는거고.)
                # 1x1 conv 이용해서 디멘션(채널수) 맞춰주고, spatial dimension (가로세로길이) 달라질경우 stride 2 로 해서 스페이셜디멘션도 맞춰주고.
                nn.Conv2d(
                    self.in_channels, # i. 기존 x의 채널수.
                    intermediate_channels * 4, # i. F의 아웃풋의 채널수. x는 이제 이값으로 채널수가 바뀌는거지.  
                    kernel_size=1, # i. 1x1 conv.
                    stride=stride, # i. stride=2 면 스페이셜디멘션 줄여줘야하니까.
                ),
                nn.BatchNorm2d(intermediate_channels * 4),
            )

        layers.append(
            block(self.in_channels, intermediate_channels, identity_downsample, stride)
        )

        # The expansion size is always 4 for ResNet 50,101,152
        self.in_channels = intermediate_channels * 4

        # For example for first resnet layer: 256 will be mapped to 64 as intermediate layer,
        # then finally back to 256. Hence no identity downsample is needed, since stride = 1,
        # and also same amount of channels.
        for i in range(num_residual_blocks - 1):
            layers.append(block(self.in_channels, intermediate_channels))

        return nn.Sequential(*layers)


def ResNet50(img_channel=3, num_classes=1000):
    return ResNet(block, [3, 4, 6, 3], img_channel, num_classes)


def ResNet101(img_channel=3, num_classes=1000):
    return ResNet(block, [3, 4, 23, 3], img_channel, num_classes)


def ResNet152(img_channel=3, num_classes=1000):
    return ResNet(block, [3, 8, 36, 3], img_channel, num_classes)


def test():
    net = ResNet101(img_channel=3, num_classes=1000)
    y = net(torch.randn(4, 3, 224, 224)).to("cuda")
    print(y.size())


test()