import torch 
import torch.nn as nn

class ResNet50(nn.Module):
    def __init__(self, in_channels, classes=6):
        super(ResNet50, self).__init__()

        self.pad = nn.ZeroPad2d((3,3))

        self.stage_1_conv2d = nn.Conv2d(in_channels=in_channels, out_channels=64, kernel_size=(7,7), stride=(2,2), padding='valid')
        self.stage_1_batchnorm = nn.BatchNorm2d(num_features=64)
        self.stage_1_activation = nn.ReLU()
        self.stage_1_pooling = nn.MaxPool2d(kernel_size=(3,3), stride=(2,2))

        self.stage_2_conv_block = self.get_convolutional_block(in_channels=64, f=3, filters=[64, 64, 256], s=1)
        self.stage_2_id_block_1 = self.get_identity_block(in_channels=256, f=3, filters=[64, 64, 256])
        self.stage_2_id_block_2 = self.get_identity_block(in_channels=256, f=3, filters=[64, 64, 256])

        self.stage_3_conv_block = self.get_convolutional_block(in_channels=256, f=3, filters=[128, 128, 512], s=2)
        self.stage_3_id_block_1 = self.get_identity_block(in_channels=512, f=3, filters=[128, 128, 512])
        self.stage_3_id_block_2 = self.get_identity_block(in_channels=512, f=3, filters=[128, 128, 512])

        self.stage_4_conv_block = self.get_convolutional_block(in_channels=512, f=3, filters=[256, 256, 1024], s=2)
        self.stage_4_id_block_1 = self.get_identity_block(in_channels=1024, f=3, filters=[256, 256, 1024])
        self.stage_4_id_block_2 = self.get_identity_block(in_channels=1024, f=3, filters=[256, 256, 1024])
        self.stage_4_id_block_3 = self.get_identity_block(in_channels=1024, f=3, filters=[256, 256, 1024])
        self.stage_4_id_block_4 = self.get_identity_block(in_channels=1024, f=3, filters=[256, 256, 1024])
        self.stage_4_id_block_5 = self.get_identity_block(in_channels=1024, f=3, filters=[256, 256, 1024])

        self.stage_5_conv_block = self.get_convolutional_block(in_channels=1024, f=3, filters=[512, 512, 2048], s=2)
        self.stage_5_id_block_1 = self.get_identity_block(in_channels=2048, f=3, filters=[512, 512, 2048])
        self.stage_5_id_block_2 = self.get_identity_block(in_channels=2048, f=3, filters=[512, 512, 2048])

        self.avg_pool = nn.AvgPool2d(kernel_size=(2,2))

        self.flat = nn.Flatten()

        self.fc = nn.Linear(2048, classes)

    def get_identity_block(self, in_channels, f, filters):

        block = nn.ModuleList()

        F1, F2, F3 = filters

        block.append(nn.Conv2d(in_channels=in_channels, out_channels=F1, kernel_size=(1,1), stride=(1,1), padding='valid'))
        block.append(nn.BatchNorm2d(num_features=F1))
        block.append(nn.ReLU())

        block.append(nn.Conv2d(in_channels=F1, out_channels=F2, kernel_size=(f,f), stride=(1,1), padding='same'))
        block.append(nn.BatchNorm2d(num_features=F2))
        block.append(nn.ReLU())

        block.append(nn.Conv2d(in_channels=F2, out_channels=F3, kernel_size=(1,1), stride=(1,1), padding='valid'))
        block.append(nn.BatchNorm2d(num_features=F3))

        block.append(nn.ReLU())

        return block


    def get_convolutional_block(self, in_channels, f, filters, s=2):

        block = nn.ModuleList()

        F1, F2, F3 = filters

        block.append(nn.Conv2d(in_channels=in_channels, out_channels=F1, kernel_size=(1,1), stride=(s,s), padding='valid'))
        block.append(nn.BatchNorm2d(num_features=F1))
        block.append(nn.ReLU())


        block.append(nn.Conv2d(in_channels=F1, out_channels=F2, kernel_size=(f,f), stride=(1,1), padding='same'))
        block.append(nn.BatchNorm2d(num_features=F2))
        block.append(nn.ReLU())

        block.append(nn.Conv2d(in_channels=F2, out_channels=F3, kernel_size=(1,1), stride=(1,1), padding='valid'))
        block.append(nn.BatchNorm2d(num_features=F3))

        block.append(nn.Conv2d(in_channels=in_channels, out_channels=F3, kernel_size=(1,1), stride=(s,s), padding='valid'))
        block.append(nn.BatchNorm2d(num_features=F3))

        block.append(nn.ReLU())

        return block


    def forward(self, X):

        X = self.pad(X)

        X = self.stage_1_conv2d(X)
        X = self.stage_1_batchnorm(X)
        X = self.stage_1_activation(X)
        X = self.stage_1_pooling(X)

        X = self.apply_conv_block(X, self.stage_2_conv_block)
        X = self.apply_identity_block(X, self.stage_2_id_block_1)
        X = self.apply_identity_block(X, self.stage_2_id_block_2)
        X = self.apply_conv_block(X, self.stage_3_conv_block)
        X = self.apply_identity_block(X, self.stage_3_id_block_1)
        X = self.apply_identity_block(X, self.stage_3_id_block_2)

        X = self.apply_conv_block(X, self.stage_4_conv_block)
        X = self.apply_identity_block(X, self.stage_4_id_block_1)
        X = self.apply_identity_block(X, self.stage_4_id_block_2)
        X = self.apply_identity_block(X, self.stage_4_id_block_3)
        X = self.apply_identity_block(X, self.stage_4_id_block_4)
        X = self.apply_identity_block(X, self.stage_4_id_block_5)

        X = self.apply_conv_block(X, self.stage_5_conv_block)
        X = self.apply_identity_block(X, self.stage_5_id_block_1)
        X = self.apply_identity_block(X, self.stage_5_id_block_2)

        X =  self.avg_pool(X)

        X = self.flat(X)
        X = self.fc(X)

        return X


    def apply_conv_block(self, X, conv_block):
        X_shortcut = X
        for component in conv_block[:-3]:
            X = component(X)
        X_shortcut = conv_block[-3](X_shortcut)
        X_shortcut = conv_block[-2](X_shortcut)
        X = torch.add(X, X_shortcut)
        X = conv_block[-1](X)
        return X


    def apply_identity_block(self, X, block):
        X_shortcut = X
        for component in block[:-1]:
            X = component(X)
        X = torch.add(X, X_shortcut)
        X = block[-1](X)
        return X