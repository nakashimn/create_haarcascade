# create_vec.py

import os
import glob
import subprocess

""" ---------------------------------------------------------------------------
Path
--------------------------------------------------------------------------- """
dirpath_positive = "../assets/img/gray/face/positive"
dirpath_negative = "../assets/img/gray/face/negative"
dirpath_vec = "../assets/vec"

""" ---------------------------------------------------------------------------
Parameter
--------------------------------------------------------------------------- """
img_num = 8000
img_height = 100
img_width = 100

""" ---------------------------------------------------------------------------
Processing
--------------------------------------------------------------------------- """
filepathes_positive = glob.glob(dirpath_positive + "/*.jpg")
for filepath_img in filepathes_positive:
    img_name = os.path.basename(filepath_img)
    filepath_vec = dirpath_vec + "/parts/{}.vec".format(os.path.splitext(img_name)[0])
    cmd = "..\\bin\\opencv_createsamples.exe -img {} -num {:d} -h {:d} -w {:d} -vec {}".format(filepath_img,
                                                                                               img_num,
                                                                                               img_height,
                                                                                               img_width,
                                                                                               filepath_vec)

    print("{} Processing...".format(img_name))
    subprocess.run(cmd, shell=True)
    print("done.")

cmd = "python mergevec\\mergevec.py -v {} -o {}".format(dirpath_vec + "/parts",
                                                        dirpath_vec + "/output.vec")
