'''
python by:  youngjung uh, Clova ML, Naver
contact:    youngjung.uh@navercorp.com
date:       17 Dec 2018

-------------------------------------------------------------------
-- below comment came from the original (createOverlayImage.m) ----
-------------------------------------------------------------------
This file is part of the HCI-Correspondence Estimation Benchmark.

More information on this benchmark can be found under:
    http://hci.iwr.uni-heidelberg.de/Benchmarks/

Copyright (C) 2011  <Sellent, Lauer>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import numpy as np
from imageio import imwrite, imread
from readFlowFile import readFlowFile
from flowToColor import flowToColor


def createOverlayImage(image, visImage):
    '''
    Create an overlay of the input image and visualization of the
    correspondences
    '''

    # determine characteristics of input image
    height, width, channels = image.shape
    maxImage = image.max()

    maxVis = 2 ** np.ceil(np.log2(visImage.max()))

    # transfer input image to 3 channel rgb image with grayvalues in [0,1]
    # (youngjung: maybe rgb to gray...)
    if 1 < channels:
        image = image.sum(2)/channels

    image = image / maxImage
    image = np.tile(image.reshape(1, height, width), (3, 1, 1)).transpose(1, 2, 0)

    # Add images for overlay
    overlayImage = maxVis * image * 0.2 + visImage * 0.8
    # overlayImage = cast(overlayImage, class(visImage))
    return overlayImage


def main(fname_image, fname_flow):
    im1 = imread(fname_image)
    flow = readFlowFile(fname_flow)
    im_flow = flowToColor(flow)
    im_overlay = createOverlayImage(im1, im_flow)
    imwrite('overlay.png', im_overlay)


if __name__ == '__main__':
    import fire
    fire.Fire(main)
