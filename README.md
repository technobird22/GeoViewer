# Geocapture
Automatic processing of geostationary satellite data

## About
GeoCapture is designed to automatically take raw infrared LRIT images to produce bring out subtle details and generate animations. This is currently designed to process them fully automatically, but it isn't too hard to manually run the scripts according to your needs.
**See more information below**

## Features:
- Fully automatic (after being run)
- Enhances landmass and brings out subtle details by running CLAHE (Contrast Limited Adaptive Histogram Equalisation) on each frame.
- Automatically parses and overlays data onto each frame
- Lots of debug output and comments

## Todo:
- Add false colour (eg. enhanced temerature)
- Underlay false colour
- Add crops of locations
- Repair dropped frames/packets
- Sharpen images

## Running GeoCapture
- Currently, the main script is `batch_process.py`, which, after being run, automatically does all the processing. It should be relatively easy to change input directories/output locations from the code, where everything is clearly commented. All the enhancements and processes are in the `geocap_utils.py` header file, although I am still moving some across.

## Output files
**These can easily be changed**
- Directory containing all processed frames
- One video animation **for each day**
- One video animation containing all processed frames

## System Requirements
This script is relatively lightweight, using less than `200mb` of RAM and less than `20%` utilisation of my CPU (Quad core - 1.8GHZ) during testing. This may change as I add in more features, but it should stay relatively light.
- Ram: I would suggest having some extra breathing room so maybe 
- Disk space shouldn't be a problem: The output data does take up roughly the same space as input data, but you can easily choose not to keep the processed frames or to overwrite the input files.
- Processor: Shouldn't matter too much but may affect running speed of the program. I have restricted the running speed of the program by having it pause every so often (200 frames right now), which **can** be disabled.

This script should be able to run on a raspberry pi, but I have yet to test it.

## Required libraries
Currently required libraries are `opencv-python` and `numpy`
If you run into import errors, you'll need to run the following commands to install the libraries:
- `pip install opencv-python`
- `pip install numpy`

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
