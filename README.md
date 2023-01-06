# Haar Classifier for Fish Detection in Roblox
This directory contains an example of how to use the Haar feature-based cascade classifier implemented in OpenCV to perform real-time object recognition on fishes in the popular online game Roblox. The classifier was trained using over 1000 manually taken screenshots of fish in the game, which were sorted and labeled manually.

# Prerequisites
To use this example, you will need to have Python and OpenCV installed on your system. You will also need to have Roblox installed and running on your computer. You can install OpenCV by following the instructions on the OpenCV installation page or by using pip:

```
pip install opencv-python
Running the example
To run the example, navigate to the cascade_classifier directory and run the detect_fishes.py script using Python:

python detect_fishes.py
```


# Automating fishing with the classifier
The program will open a window showing the live video feed from your default camera. The Haar classifier will be used to detect fish in the video and draw rectangles around them. When the program detects multiple rectangles, the program automates the catching process.

