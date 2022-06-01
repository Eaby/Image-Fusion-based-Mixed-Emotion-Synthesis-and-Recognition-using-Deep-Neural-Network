# Image-Fusion-based-Mixed-Emotion-Synthesis-and-Recognition-using-Deep-Neural-Network
This is the official implementation code for Image Fusion based Mixed Emotion Synthesis and Recognition using Deep Neural Network. This algorithm uses a spatial domain approach, combining weighted average method and Principal Component Analysis. The output image created from this algorithm provides a new synthetic image which is a combination of 2 base facial expressions. The project also uses a CNN based Mixed emotion detection which is implemented using [[Tensorflow](https://pytorch.org/)](https://www.tensorflow.org/). 

## Install guidelines
- We recommend you to use an [Anaconda](https://www.anaconda.com/) virtual environment. Install [[Tensorflow](https://pytorch.org/)](https://www.tensorflow.org/). >= 2.0 according to your GPU driver and Python >= 3.7.2, and run `package_requirements.sh`.

## Quick demo
- If you don't want to train the classifier from scratch, you can make the use of `mxfertestcustom.py` directly as the repository already has `mxfer.json` (trained        model) and `mxfer.h5` (parameters) which can be used to predict emotion on any test image present in the folder. You can modify `mxfertestcustom.py` according to        your requirements and use it to predict facial emotion in any use case.
- Pre-trained models weights are in mxfer.h5 file (Location: MESR_Project>>CODE_PartA>>testing codes>>mxfer2022-master>>mxfer2022-master)
- Mixed emotion image generation is done using convert_mxfer2022_to_images_and_landmarks.py file (location: MESR_Project>>CODE_PartA)
- To see the mixed Emotion output please follow the below steps.
-     * Run the file names mxfertestcustom.py file (Location: MESR_Project>>CODE_PartA>>mxfer2022-master)
-     * you can change the input file name from test.tiff to any of your own facial image files.
-     * A mixed emotion based output will appear with the mixed emotion.

## Running the tests 
You can test the accuracy of trained classifier using `modXtest.npy` and `modytest.npy` by running `mxfertest.py` file. This would give the accuracy of the recently trained classifier.
