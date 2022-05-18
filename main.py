import eel
import cv2 as cv
import os
import numpy as np

eel.init("web")
    


def get_file(filename):
    if os.path.exists(filename):
        return filename
    sub_directories = [name for name in os.listdir(".") if os.path.isdir(name)]
    for directory in sub_directories:
        path = os.path.join(directory, filename)
        if os.path.exists(path):
            return path
    return False

def count_frames_manual(video):
	# initialize the total number of frames read
	total = 0
	# loop over the frames of the video
	while True:
		# grab the current frame
		(grabbed, frame) = video.read()
	 
		# check to see if we have reached the end of the
		# video
		if not grabbed:
			break
		# increment the total number of frames read
		total += 1
	# return the total number of frames in the video file
	return total


@eel.expose
def run_image_generation(filename, coloring = 'single', method = 'mean', increment='default', added_thickness=0, size = 'default', x_size = 0, y_size = 0):
    #find file
    path = get_file(filename)

    #load vid
    video = cv.VideoCapture(path)


    try:
        len_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    except:
        len_frames = count_frames_manual(video)
        video.release()
        video = cv.VideoCapture(path)

    if increment =='default':
        increment = int(len_frames//1080)+1

    
    
    x_axis_index = 0
    if coloring =='single':
        method_axis = (0,1)
    else:
        method_axis = (1)
    
    if method == 'mean':
        def proc_method(frame):
            return np.average(frame, axis = method_axis)
    elif method == 'median':
        def proc_method(frame):
            return np.median(frame, axis = method_axis)
    elif method == 'mode':
        def proc_method(frame):
            return np.argmax([np.bincount(x) for x in frame.reshape(-1, 3).T], axis=method_axis)

    
    grabbed, frame = video.read()
    out_img = np.zeros((frame.shape[0],1+added_thickness,3))
    frame_i = 1
    col = 0
    
    while(True):
        if not grabbed:
            break
        if frame_i % increment ==  0:
            out_img = np.append(out_img, np.zeros((frame.shape[0],1+added_thickness,3)),1)
            out_img[:,-1*1+added_thickness] = proc_method(frame)
            col +=1 + added_thickness
        if col >= 1080 and size == 'default':
            break
        frame_i+=1

        grabbed, frame = video.read()

    if size =='source':
        out_img = cv.resize(out_img, [frame.shape[1],frame.shape[0]])
    elif size =='custom':
        out_img = cv.resize(out_img, (int(x_size),int(y_size)))

    print('done')
    #blank = blank[:][:]/[255,255,255]
    
    cv.imwrite(path.rsplit('.', 1)[0]+'.jpg', out_img)
    print('saved')
    return

# Start the index.html file
eel.start("index.html")