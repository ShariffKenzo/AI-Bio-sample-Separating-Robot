# AI-Bio-sample-Separating-Robot
This repository contains the entire source code used to control the precise movements of the AI Bio-sampling robot: everything from computer vision, colour detection, precise measurements of solution height , to G-code for the movement of the stepper motors. Here is a video of how the robot works : https://blogs.ntu.edu.sg/ps5888-2022-g04/project-overview/

What each file does:

1. Automatedinput.py is used to control the keyboard and mouse for automating the sending of G-code to pronterface.exe(downloaded separately)
2. LogitechCamera.py has function Pixelcount(x coords on camera, y coords on camera, index : which test tube)
3. Saturationhsvfn.py has function SampleDetector(x coords on camera, y coords on camera) to detect presence of test tube sample
4. PlasmaHeight.py has PlasmaCount() to get the height of plasma
5. ColourTag.py is used to identify colour markers for the type of test tube or eppendorf rack
6. PipetteTipDetection.py is used to detect whether the tip has been attached successfully to the pipette.

Note: Scaling factors may need to be changed if camera distance from sample changes.
