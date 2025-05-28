import difflib
import json
import torch
import cv2
import inspect
try:
    from spconv.pytorch.core import *
    spc=True
except:
    spc=False
import numpy

space='\t'



def debug0(x):
    if spc and isinstance(x, SparseConvTensor):
        return '"' + str([x.batch_size, x.features.shape[1]] +x.spatial_shape) + " " + str(x)[:100] + '"'
    elif isinstance(x, torch.Tensor):
        return '"' + str(x.shape) + '"'
    elif isinstance(x,  list) :
        return "["+",".join([debug0(t) for t in x])+"]"
    elif isinstance(x, numpy.ndarray):
        return '"' + str(x.shape) + '"'
    elif isinstance(x, dict):
        return "{"+",".join(['"' + str(key) + '":'+debug0(x[key]) for key in x])+"}"
    else:
        return  str(x)[:100]




def get_lineno(level):
    stack = inspect.stack()
    filename = stack[level].filename 
    lineno = stack[level].lineno  
    filename=filename.replace("/mnt/data/zbh_data/project","/home/zbh/project")
    return filename + ":" + str(lineno)  

def debug_path(include_conda=False):
    stack = inspect.stack()
    s=""
    for level in range(len(stack)):
        filename = stack[level].filename 
        lineno = stack[level].lineno  
        filename=filename.replace("/mnt/data/zbh_data/project","/home/zbh/project")
        if 'debug/debug' in filename:
            continue
        if 'miniconda3' not in filename and include_conda == False:
            s+=filename + ":" + str(lineno) +"\n"
    return s

def debug_line(x):
    return " "+ debug0(x)+ " "+get_lineno(2)  +" "


def debug_img(path, img):
    import cv2
    import numpy as np
    if isinstance(img, list):
        img = np.array(img)

    if "torch" in str(type(img)):
        img = img.detach().cpu().numpy()

    if isinstance(img, np.ndarray):
        if len(img.shape) == 2:
            img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
        elif len(img.shape) == 3 and img.shape[2] == 1:
            img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
        elif len(img.shape) == 3 and img.shape[2] == 3:
            img = img.astype(np.uint8)
        else:
            raise ValueError("Unsupported image dimensions")

    if isinstance(img, np.ndarray) and img.dtype == np.float32:
        img = (img * 255.0).astype(np.uint8)
    # print(img)
    cv2.imwrite(path, img)

