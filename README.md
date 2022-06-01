# Image-Fusion-based-Mixed-Emotion-Synthesis-and-Recognition-using-Deep-Neural-Network
This is the official implementation code for Image Fusion based Mixed Emotion Synthesis and Recognition using Deep Neural Network. This algorithm uses a spatial domain approach, combining weighted average method and Principal Component Analysis. The output image created from this algorithm provides a new synthetic image which is a combination of 2 base facial expressions. The project also uses a CNN based Mixed emotion detection which is implemented using [[Tensorflow](https://pytorch.org/)](https://www.tensorflow.org/). 

## Install guidelines
- We recommend you to use an [Anaconda](https://www.anaconda.com/) virtual environment. Install [[Tensorflow](https://pytorch.org/)](https://www.tensorflow.org/). >= 2.0 according to your GPU driver and Python >= 3.7.2, and run `package_requirements.sh`.

## Quick demo
- Pre-trained models weights are in fer.h5 file.
- Mixed emotion image generation is done using convert_mxfer2022_to_images_and_landmarks.py file at MERG/venv/.
- To see the mixed Emotion output please follow the below steps.
-     * Run the file names fertestcustom.py which is located at MERG/CODE/mxfer2022-master/mxfertestcustom.py
-     * you can change the input file name from test.tiff to any of your own facial image files.
-     * A mixed emotion based output will appear with the mixed emotion.
