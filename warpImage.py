'''
python by:  youngjung uh, Clova ML, Naver
contact:    youngjung.uh@navercorp.com
date:       17 Dec 2018

original:   SIFT Flow by Ce Liu
https://people.csail.mit.edu/celiu/SIFTflow/

'''

import numpy as np
from scipy.interpolate import interp2d
from imageio import imread, imwrite
from readFlowFile import readFlowFile


def warpImage(im, vx, vy):
    '''
    function to warp images with different dimensions
    '''

    height2, width2, nChannels = im.shape
    height1, width1 = vx.shape

    x = np.linspace(1, width2, width2)
    y = np.linspace(1, height2, height2)
    X = np.linspace(1, width1, width1)
    Y = np.linspace(1, height1, height1)
    xx, yy = np.meshgrid(x, y)
    XX, YY = np.meshgrid(X, Y)
    XX = XX + vx
    YY = YY + vy
    mask = (XX < 1) | (XX > width2) | (YY < 1) | (YY > height2)
    XX = np.clip(XX, 1, width2)
    YY = np.clip(XX, 1, height2)

    warpI2 = np.zeros((height1, width1, nChannels))
    for i in range(nChannels):
        f = interp2d(x, y, im[:, :, i], 'cubic')
        foo = f(X, Y)
        foo[mask] = 0.6
        warpI2[:, :, i] = foo

    mask = 1 - mask
    return warpI2, mask


def main(fname_image, fname_flow):
    im2 = imread(fname_image)
    flow = readFlowFile(fname_flow)
    im_warped, _ = warpImage(im2, flow[:, :, 0], flow[:, :, 1])
    imwrite('warped.png', im_warped)


if __name__ == '__main__':
    import fire
    fire.Fire(main)
