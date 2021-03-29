import argparse
import cv2 
import os
import time
import ntpath
from os import path
from pathlib import Path

def dir_path(string):
    if path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def file_path(string):
    if path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    cap = cv2.VideoCapture(input_loc)
    if cap.isOpened() != True:
        print("File not found try using double slashes in your path (.\\path\\file.mp4)")
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        cv2.imwrite(output_loc + f"\\{ntpath.basename(input_loc)[:-4]}_%#012d.jpg" % (count), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            cap.release()
            break

parser = argparse.ArgumentParser(description="motion-transfer-CLI")
subparsers = parser.add_subparsers(help="commands", dest='command')

#OPENPOSE COMMANDS

openpose_parser = subparsers.add_parser('openpose', help='openpose commands')
openpose_parser.add_argument('--video',  help='path to the video', required=True)
openpose_parser.add_argument('--outpose', action='store_true', help=' store video with pose overlay')

#SMPLX COMMANDS

smplx_parser = subparsers.add_parser('smplx', help="simplx commands")
group = smplx_parser.add_mutually_exclusive_group()
group.add_argument('--fit', action='store_true')
group.add_argument('--render', action='store_true')


args = parser.parse_args()
if args.command == 'openpose':
    video_to_frames(input_loc=args.video, output_loc='.\smplify-x\DATA_FOLDER\images')
    os.chdir('openpose')
    if args.outpose:
        os.system(f'cmd /c ".\\bin\OpenPoseDemo.exe --video .\..\\{args.video} --face --hand --write_json .\..\smplify-x\DATA_FOLDER\keypoints --write_video .\..\pose.avi" ')
    else:
        os.system(f'cmd /c ".\\bin\OpenPoseDemo.exe --video .\..\\{args.video} --face --hand --write_json .\..\smplify-x\DATA_FOLDER\keypoints" ')

else:
    if args.fit:
        os.system('cmd /c "python smplify-x\smplifyx\main.py --config smplify-x\cfg_files\\fit_smplx.yaml --data_folder smplify-x\DATA_FOLDER --output_folder smplify-x\OUTPUT_FOLDER --model_folder smplify-x\MODEL_FOLDER --vposer_ckpt smplify-x\VPOSER_FOLDER"')
    elif args.render:
        os.system('cmd /c "python smplify-x\smplifyx\\render_results.py --mesh_fns smplify-x\OUTPUT_FOLDER\meshes"')
