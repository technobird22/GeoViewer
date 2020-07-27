# GeoCapture
GeoCapture is a program for automatically processing data received from geostationary satellites such as the **GOES**, **GK-2**, and **Himawari** series.

## About
GeoCapture is designed to automatically take raw infrared LRIT images to bring out subtle details otherwise not recognized in the original image, as well as generate animations. GeoCapture is
built to process all of this data automatically, so you don't have to lift a finger. However, GeoCapture can be easily configured for manual use.
**See more information below**

## Features:
- Fully Automatic Image Processing
- Enhances Landmass and brings out subtle details by running Contrast Limited Adaptive Histogram Equalisation (CLAHE) on each frame.
- Automatically Parses and overlays relevant data
- Can directly take input from XRIT-RX output
- *Incredibly* detailed log files.
-----

## Todo:
### Program:
- [ ] Have configuration in a seperate file
- [x] <del>Add option to ignore certain folders</del>
- [x] <del>Read directly from directory output structure of XRIT-RX</del>

### Features:
- [ ] Add false colour Overlays (eg. Enhanced Temperature)
- [ ] Underlay false colour
- [ ] Add crops for certain locations
- [ ] Repair dropped frames/packets
- [ ] Sharpen images

-----

## Running GeoCapture
- Currently, the main script is `batch_process.py`, which, after being run, automatically does all the processing. It's relatively easy to change input directories/output locations from the code, where everything is clearly commented, however the ability to parse this argument wise will be added in the future. All the enhancements and processing scripts are in the `geocap_utils.py` header file, although some are still being moved across.

## Required Libraries
Currently required libraries are `opencv-python` and `numpy`.
If you run into import errors, you'll need to run the following commands to install the libraries:
- `pip install opencv-python`
- `pip install numpy`

## System Requirements
This script is very lightweight, using less than `200mb` of RAM and less than `20%` utilisation of my CPU (Quad core - 1.8GHZ) during testing. This may change as I add in more features, but it should stay relatively light. During testing, I have found that the script takes around `90` seconds to process a day's worth of images (143 frames)
<br>
I have restricted the running speed of the program by having it pause after processing a certain number of frames (200 frames right now). This **can** be disabled.

Here are some recommended specs for running GeoCapture:
- Ram: `4Gb`
- Disk Space: >`10Gb`
- Processor: `1Ghz Dual Core` - (Anything built within the past 5 years for a laptop or desktop should work just fine)

This script should be able to be run alongside programs such as `GOESRECV` and `XRIT-RX` on a Raspberry Pi 3B, however this has **not yet been tested**.

## Input files
GeoCapture can take input directly from the output directory structure of XRIT-RX.
<br>
However, you need to first add in a "config" directory containing the appropriate configuration `JSON` files.
<br>
***There is an example config directory in the "data" directory in this repository.***
<br>
<br>
**Here is an example of such a structure:**
```
[Working directory (called "LRIT", which is inside "recieved" in the LRIT-RX output)]
│
├───config
│   ├───config.json
│   └───data.json
├───20200628
│   ├───FD
│   ├───GWW3F
│   ├───RWW3A
│   ├───RWW3F
│   ├───SSTA
│   ├───UP50F24
│   └───UP50F48
├───20200629
│   ├───ANT
│   ├───FD
│   ├───RWW3A
│   ├───SICEA
│   ├───SSTF24
│   ├───SSTF48
│   ├───SSTF72
│   └───SUFA03
└───[More daily directories...]
```
**Remember to add in the config directory!**
<br>
*Remember that there is an example config directory in the "data" directory in this repository.*

## Output files
**These can easily be changed via the configuration files**
- Directory containing processed frames per day
- One video animation **for each day**
- Directory containing all processed frames
- One video animation containing all processed frames

-----

## Examples
You can find some examples of what GeoCapture can do below:

### Video animation:
External link to YouTube:
https://youtu.be/TZ3zU0zz20M

### Raw frame (unprocessed):
<img src="https://raw.githubusercontent.com/technobird22/geocapture/master/examples/raw.jpg" width="300" title="raw frame">

### CLAHE applied:
<img src="https://raw.githubusercontent.com/technobird22/geocapture/master/examples/clahe.jpg" width="300" title="CLAHE applied">

### Overlay and CLAHE applied:
<img src="https://raw.githubusercontent.com/technobird22/geocapture/master/examples/clahe_overlay.jpg" width="300" title="Overlay and CLAHE applied">
