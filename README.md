# flow-python
- python implementation of Deqing's [flow-code-matlab.zip](http://vision.middlebury.edu/flow/code/flow-code-matlab.zip)
- for further information --> [http://vision.middlebury.edu/flow/data/](http://vision.middlebury.edu/flow/data/)

# usage

## read/write .flo file
``` python
import sys
sys.path.append('flow-python')
from flowio import readFlowFile, writeFlowFile

flow = readFlowFile(fname_input)
writeFlowFile(flow, fname_output)
```

## visualize flow in rgb code
```
python flowToColor.py --fname_flow examples/grove2.flo
```

## warp target image according to the flow
```
python warpImage.py --fname_image examples/grove2_frame10.png --fname_flow examples/grove2.flo
```

## overlay flow in rgb on an image
```
python createOverlayImage.py --fname_image examples/grove2_frame10.png --fname_flow examples/grove2.flo
```

## check color code
```
python colorTest.py
```
