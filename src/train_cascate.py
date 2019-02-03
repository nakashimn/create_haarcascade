# train_cascade.py

import subprocess

""" ---------------------------------------------------------------------------
Path
--------------------------------------------------------------------------- """
dirpath_vec = "../assets/vec"
dirpath_negative = "../assets/img/gray/face/negative/txt"
dirpath_cascade = "../assets/cascades"
filename_vec = "hina_gray.vec"
filename_negtext = "negative.txt"
filename_cascade = "haarcascade_hina.xml"

""" ---------------------------------------------------------------------------
Parameter
--------------------------------------------------------------------------- """
num_pos = 8000
num_neg = 2000
img_width = 100
img_height = 100

""" ---------------------------------------------------------------------------
Processing
--------------------------------------------------------------------------- """
filepath_vec = dirpath_vec + "/" + filename_vec
filepath_negtext = dirpath_negative + "/" + filename_negtext

cmd = "..\\bin\\opencv_traincascade.exe -data {} -vec {} -bg {} -numPos {:d} -numNeg {:d} -w {:d} -h {:d}".format(dirpath_cascade,
                                                                                                                  filepath_vec,
                                                                                                                  filepath_negtext,
                                                                                                                  num_pos,
                                                                                                                  num_neg,
                                                                                                                  img_width,
                                                                                                                  img_height)

print("{} Processing...".format(filename_vec))
print(cmd)
subprocess.run(cmd, shell=True)
print("done.")
