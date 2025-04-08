
# define the chepoints to biasthe net towards the left/right/straight turn, 
# look at stuff/final_map.png to get the numbers
CP_COMMON = [
    (178,254), # highway
    (246,609), # highway
    (387,398), # connection to roundabout
    (373,384), # connection to roundabout
    (450,420), # park
    (472,420), # start
    (490,512), # weird merge
    (497,512), # weird merge
    (152,164), # speed turn
    (166,176), # speed turn
    ]
CP_LEFT = 2*[ # int = intersection
    (415,414), # avram square
    (406,405), # avram square
    (125,124), # int top right
    (140,139), # int top left
    (94,114), # int bottom left
    (114,93), # int bottom left
    (97,99), # int bottom right
    (99,96), # int bottom right
    (387,612),(387,612),(387,612),(387,612), # roundabout
    (353,600),(353,600),(353,600),(353,600), # roundabout
    (322,604),(322,604),(322,604),(322,604), # roundabout
    (218,608),(218,608),(218,608),(218,608), # roundabout
    (498,129), # weird merge
    (114,113), # int bottom left
    (198,175), # higwat -> speed turn
    (155,154), # speed turn
    (142,155), # speed turn
    (208,175), # speed turn
    (483,482), # unirii square
    ] #+ 1*CP_COMMON
CP_STRAIGHT = 2*[(203,451),(387,397),(436,435)] # + 1*CP_COMMON
CP_RIGHT = 2*[(100,122), (113, 95)] # + 1*CP_COMMON

# uncomment to train left/straight/right
DS_PATH, NET_PATH, CHECKPOINTS = 'data/left_ds.npz', 'data/he_left.onnx', CP_LEFT
# DS_PATH, NET_PATH, CHECKPOINTS = 'data/straight_ds.npz', 'data/he_straight.onnx', CP_STRAIGHT
# DS_PATH, NET_PATH, CHECKPOINTS = 'data/right_ds.npz', 'data/he_right.onnx', CP_RIGHT

# CHECKPOINTS =  [(389,395)] # comment this, used for testing

IMG_SIZE = 32
DIST_POINT_AHEAD = 0.35 # distance of the point ahead
INFERENCE_FLIP = False # flip the image for inference


import numpy as np
import cv2 as cv
from numpy.random import randint
from tqdm import tqdm
import matplotlib.pyplot as plt
import os

if not os.path.exists('data'): os.makedirs('data')

    
# NOTE: this function should be equal inside the detection.py file (same transformations for training and inference)
def preprocess_image(img, size=32, keep_bottom=0.66666667, canny1=100, canny2=200, blur=3):
    """
    Preprocesses an image to be used as input for the network.
    Note: the function modifies the image in place
    """
    img = cv.resize(img, (4*size, 4*size))
    #check if the imge is grayscale
    if not len(img.shape) == 2: img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cut the top part
    img = img[int(img.shape[0]*(1-keep_bottom)):,:]
    #resize 1
    img = cv.resize(img, (2*size, 2*size))
    #canny
    img = cv.Canny(img, canny1, canny2)
    #blur
    img = cv.blur(img, (blur,blur), 0)
    #resize 2
    img = cv.resize(img, (size, size))
    return img

def augment_img(img, size=32, keep_bottom=0.66666667, canny1=100, canny2=200, blur=3, 
                noise_std=80, max_tilt_fraction=0.1):
    """
    Augments an image by applying random transformations
    Note: the function modifies the image in place
    """

    # preaugmentation
    img = cv.resize(img, (4*size, 4*size)) # 128x128

    # # random flip
    # if randint(0, 2) == 0: img = cv.flip(img, 1)

    #create random ellipses to simulate light from the sun
    light = np.zeros(img.shape, dtype=np.uint8)
    #add ellipses
    for j in range(2):
        cent = (randint(0, img.shape[0]), randint(0, img.shape[1]))
        axes_length = (randint(int(4*size/42.67),int(4*size/10.67)), randint(int(4*size/10.67), int(size*4/1.70))) #(randint(3, 12), randint(12, 75))
        angle = randint(0, 360)
        light = cv.ellipse(light, cent, axes_length, angle, 0, 360, 255, -1)
    #create an image of random white and black pixels
    light = cv.blur(light, (50,50))
    noise = randint(0, 2, size=img.shape, dtype=np.uint8)*255
    light = cv.subtract(light, noise)
    light = np.clip(light, 0, 51)
    light *= 5
    #add light to the image
    img = cv.add(img, light)

    # dilation/erosion
    r = randint(0, 5)
    if r == 0: #dilate
        kernel = np.ones((randint(1, 5), randint(1, 5)), np.uint8)
        img = cv.dilate(img, kernel, iterations=1)
    elif r == 1: #erode
        kernel = np.ones((randint(1, 5), randint(1, 5)), np.uint8)
        img = cv.erode(img, kernel, iterations=1)

    #preprocessing
    img = preprocess_image(img, size, keep_bottom, canny1, canny2, blur)

    # second augmentation
    #add random tilt
    max_offset = int(size*max_tilt_fraction)
    offset = randint(-max_offset, max_offset)
    img = np.roll(img, offset, axis=0)
    if offset > 0:
        img[:offset, :] = 0 #randint(0,255)
    elif offset < 0:
        img[offset:, :] = 0 # randint(0,255)

    #add noise 
    std = noise_std if noise_std > 1 else 2
    std = randint(1, std)
    noisem = randint(0, std, img.shape, dtype=np.uint8)
    img = cv.subtract(img, noisem)
    noisep = randint(0, std, img.shape, dtype=np.uint8)
    img = cv.add(img, noisep)

    return img

# TRAINING 
def train_epoch(net, dataloader, regr_loss_fn, optimizer, L1_lambda=0.0, L2_lambda=0.0):
    # Set the net to training mode
    net.train() #train
    # Initialize the loss
    he_losses = []
    # Loop over the training batches
    for (input, regr_label) in dataloader:
        # Zero the gradients
        optimizer.zero_grad()
        # Compute the output
        output = net(input)
        he = output[:, 0]
        he_label = regr_label[:, 0]
        # Compute the losses
        he_loss = 1.0*regr_loss_fn(he, he_label)
        #L1 regularization
        L1_norm = sum(p.abs().sum() for p in net.conv.parameters())
        L1_loss = L1_lambda * L1_norm 
        #L2 regularization
        L2_norm = sum(p.pow(2).sum() for p in net.conv.parameters())
        L2_loss = L2_lambda * L2_norm
        #total loss
        loss = he_loss + L1_loss + L2_loss
        # Compute the gradients
        loss.backward()
        # Update the weights
        optimizer.step()
        #batch loss
        he_losses.append(he_loss.detach().cpu().numpy())

    # Return the average training loss
    he_loss = np.mean(he_losses)
    return he_loss

def val_epoch(net, val_dataloader, regr_loss_fn):
    net.eval()
    he_losses = []
    for (input, regr_label) in val_dataloader:
        output = net(input)
        regr_out = output
        he = regr_out[:, 0]
        he_label = regr_label[:, 0]
        he_loss = 1.0*regr_loss_fn(he, he_label)
        he_losses.append(he_loss.detach().cpu().numpy())
    return np.mean(he_losses)



if __name__ == "__main__":

    # torch imports here bc torch not installed in the container
    import torch
    import torch.nn as nn
    from torch.utils.data import Dataset, DataLoader

    # NETWORK ARCHITECTURE
    class HEstimator(nn.Module):
        def __init__(self,dropout=0.3):
            super().__init__()
            self.conv = nn.Sequential( #in = 32x32
                nn.Conv2d(1, 4, 5, 1), #out = 28
                nn.ReLU(True),
                nn.Dropout(p=dropout),
                nn.MaxPool2d(2, 2), #out=14
                nn.BatchNorm2d(4),
                nn.Dropout(p=dropout),
                nn.Conv2d(4, 4, 5, 1), #out = 10
                nn.ReLU(True),
                nn.Dropout(p=dropout),
                nn.MaxPool2d(2, 2), #out=5
                nn.Dropout(p=dropout),
                nn.Conv2d(4, 32, 5, 1), #out = 1
                nn.ReLU(True),
            )
            self.flatten = nn.Flatten()
            self.lin = nn.Sequential(
                nn.Linear(1*1*32, 16),
                nn.ReLU(True),
                # nn.Tanh(),
                nn.Linear(16, 1),
            )

        def forward(self, x):
            x = self.conv(x)
            x = self.flatten(x)
            x = self.lin(x)
            return x

    class DS(Dataset):
        def __init__(self):
            d = np.load(DS_PATH)
            dimgs = d['imgs']
            dalphas = d['alphas']
            print(f"Dataset: {DS_PATH}, n={len(dimgs)}")

            # initialize tensors
            self.imgs = torch.zeros((len(dimgs), 1, IMG_SIZE, IMG_SIZE), dtype=torch.float32)
            self.alphas = torch.zeros((len(dimgs), 1), dtype=torch.float32)

            # Augment and preprocess images
            pp_imgs = np.zeros((len(dimgs), IMG_SIZE, IMG_SIZE), dtype=np.uint8)
            for i in tqdm(range(len(dimgs)), desc="Prep dataset", ncols=80):
                img = dimgs[i]
                pp_imgs[i] = preprocess_image(img, size=IMG_SIZE)
                img = augment_img(img, size=IMG_SIZE)
                img = torch.from_numpy(img.astype(np.float32))
                self.imgs[i] = img
                self.alphas[i] = float(dalphas[i])

            # plotting
            plt.figure(figsize=(10, 10)) # augmented images
            random_idxs = np.random.randint(0, len(dimgs), 100)
            for i in range(100):
                plt.subplot(10, 10, i+1)
                img = self.imgs[random_idxs[i]][0].numpy()
                α = self.alphas[random_idxs[i]][0].numpy()
                plt.imshow(img, cmap='gray', origin='upper')
                plt.title(f'α={np.rad2deg(α):.1f}°')
                plt.axis('off')
            plt.tight_layout()

            plt.figure(figsize=(10, 10)) # preprocessed images
            for i in range(100):
                plt.subplot(10, 10, i+1)
                img = preprocess_image(dimgs[random_idxs[i]], size=IMG_SIZE)
                α = self.alphas[random_idxs[i]][0].numpy()
                plt.imshow(img, cmap='gray', origin='upper')
                plt.title(f'α={np.rad2deg(α):.1f}°')
                plt.axis('off')
            plt.tight_layout()
            plt.show()

        def __len__(self): return len(self.imgs)
        def __getitem__(self, idx): return self.imgs[idx], self.alphas[idx]









    BATCH_SIZE = 16384 #16384
    EPOCHS = 200 # 200
    L1_LAMBDA = 1e-4 # 1e-4
    L2_LAMBDA = 1e-2 # 1e-2
    LOSS_FN = nn.MSELoss() # nn.MSELoss()
    DROP = 0.3 # 0.3
    LR = 3e-3 # 3e-3


    ds = DS() # dataset
    dl = DataLoader(ds, batch_size=BATCH_SIZE, shuffle=True) # dataloader

    net = HEstimator(dropout=DROP) # model

    opt = torch.optim.Adam(net.parameters(), lr=LR, weight_decay=0.0) # optimizer

    #train
    net.to('cpu')
    tlosses = np.zeros((EPOCHS, 2))
    for ep in tqdm(range(EPOCHS), desc="Training", ncols=80):
        tlosses[ep] = train_epoch(net, dl, LOSS_FN, opt, L1_LAMBDA, L2_LAMBDA)
    
    # plot losses
    plt.figure(figsize=(10, 5))
    plt.plot(tlosses[:, 0], label='Train Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Losses')
    plt.legend()
    plt.show()        


    # convert to onnx
    print("Exporting to ONNX")
    os.remove(NET_PATH) if os.path.exists(NET_PATH) else None
    net.eval()
    dummy_input = torch.randn(1, 1, IMG_SIZE, IMG_SIZE)
    torch.onnx.export(net, dummy_input, NET_PATH, verbose=False)

    # test the model on some images
    print("Testing the model")
    onnx_net = cv.dnn.readNetFromONNX(NET_PATH)
    # load test images
    d = np.load(DS_PATH)
    test_imgs = d['imgs']
    test_alphas = d['alphas']
    rand_idxs = np.random.randint(0, len(test_imgs), 100)
    pred_alphas = np.zeros((100, 1), dtype=np.float32)
    for i in range(100):
        idx = rand_idxs[i]
        img = test_imgs[idx].copy()
        img = preprocess_image(img)
        if INFERENCE_FLIP:
            img_flip = cv.flip(img, 1)
            imgs = np.stack((img, img_flip), axis=0)
        else: imgs = np.stack((img,), axis=0)
        blob = cv.dnn.blobFromImages(imgs, 1.0, (IMG_SIZE, IMG_SIZE), 0, swapRB=True, crop=False)
        onnx_net.setInput(blob)
        out = onnx_net.forward()
        if INFERENCE_FLIP:
            α, α_flip = out[0][0], out[1][0]
            α = (α - α_flip) / 2
        else: α = out[0][0]
        pred_alphas[i] = α
        print(f'α -> gt={np.rad2deg(test_alphas[idx]):.1f}°, pred={np.rad2deg(α):.1f}°')
    
    print(f'Mean error: {np.rad2deg(np.mean(np.abs(pred_alphas - test_alphas))):.1f}°')
    print(f'Max error: {np.rad2deg(np.max(np.abs(pred_alphas - test_alphas))):.1f}°')
    print(f'MSE: {np.rad2deg(np.mean((pred_alphas - test_alphas)**2)):.1f}°')