# Object Tracking with GOTURN Algorithm using OpenCV

This project demonstrates object tracking using the GOTURN algorithm with OpenCV in Python.

## Overview

The GOTURN (Generic Object Tracking Using Regression Networks) algorithm is a deep learning-based tracking method used to track the motion of an object in a video. The algorithm determines the initial position of an object and then utilizes a regression network to predict the object's motion. GOTURN is trained to provide fast and accurate tracking results.

## Algorithm Description

The GOTURN algorithm follows these steps:

1. **Initial Position Determination**: Firstly, the algorithm determines the initial position of the object. This position is typically specified by the user or automatically detected.

2. **Preprocessing**: The algorithm preprocesses the input image to facilitate object tracking. Preprocessing steps may include image blurring, color transformation, and size transformation.

3. **Object Tracking**: The preprocessed image is fed into a deep learning regression network. This network is used to predict the motion of the object. The algorithm predicts the new position of the object in each frame.

4. **Updating Results**: After calculating the new position of the object, the algorithm tracks the object using this position. A bounding box is drawn around the object based on its motion, and it is added to the result image.

## Mathematical Description

The GOTURN algorithm utilizes a regression network and object bounding boxes to predict the new position of the object. The regression network takes input feature vectors and the object bounding box and predicts the new position of the object. This prediction is made using a regression model trained to minimize a loss function.

## Usage

1. Download the pre-trained GOTURN model files `goturn.prototxt` and `goturn.caffemodel` from [here](https://www.dropbox.com/s/ld535c8e0vueq6x/opencv_bootcamp_assets_NB11.zip?dl=1).
2. Place the downloaded `goturn.prototxt` and `goturn.caffemodel` files in the same directory as the Python script.
3. Update the `prototxt` and `model` variables in the Python script with the filenames of the downloaded files.
4. Set the `video_path` variable to the path of the input video file.
5. Run the Python script. The tracked video will be saved as `output.mp4`.

## Requirements

- OpenCV
