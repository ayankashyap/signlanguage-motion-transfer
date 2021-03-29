# signlanguage-motion-transfer

Rendered          |  Actual
:-------------------------:|:-------------------------:
![](./docs/rendergif.gif)  |  ![](./docs/cropall2.gif)

This tool allows you to enter any video of a person speaking in sign language, and applies the motion to a 3d mesh  

## Steps to use this tool:
1. Clone this repository: 
```
git clone https://github.com/ayankashyap/signlanguage-motion-transfer.git`
```
2. Change into the repo directory: 
```
cd signlanguage-motion-transfer
```
3. Create a virtual environment (using conda or venv):  
```
python3 -m venv venv
source venv/bin/activate
```
4. Install the requirements: 
```
$ pip install requirements.txt
```
- *Note:* To run this project your system must have a GPU and CUDA installed for pytorch and several other libraries to function!
5. Download the openpose-gpu binaries from the repository's [releases page](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases) :
    1. Extract the zip file and place the openpose directory inside "signlanguage-motion-transfer"
    2. open openpose\models and run the "getModels.bat" batch file. This will download all the trained weights for openpose
6. Download and extract the SMPL-X model and VPoser from this [website](https://smpl-x.is.tue.mpg.de/) :  
- *Note:* You are required to register and agree to the SMPL terms and conditions to download the files.
7. Clone the smplify-x repository.
```
git clone https://github.com/vchoutas/smplify-x.git`
```

8. Create the following directories inside smplify-x: MODEL_FOLDER, DATA_FOLDER,  OUTPUT_FOLDER, V_POSER_FOLDER. And inside DATA_FOLDER create two more directories: images, keypoints
-*Note* the names of the folders must be identical to the names above, or the script fails.

9. Copy the smplx folder and place it in MODEL_FOLDER. Copy the **contents** of VPoser and place it in V_POSER_FOLDER. The directory structure should be looking something like this.
```bash
smplify-x
+---cfg_files
+---DATA_FOLDER
|   +---images
|   +---keypoints
+---images
+---MODEL_FOLDER
|   +---smplx
+---OUTPUT_FOLDER
+---smplifyx
+---smplx_debug 
+---smpl_debug 
+---src    
+---VPOSER_FOLDER
    +---snapshots
    +---__pycache__
```

10. Make sure your files and folders are in place, and you are now ready to use the tool! 
```bash
signlanguage-motion-transfer
+---docs
+---openpose
+---smplify-x
``` 

11. Open a terminal to use the cli. Make sure you have activated your environment. 
