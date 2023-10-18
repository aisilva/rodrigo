#attempting to use mean and std dev cuts on differences of frames.
#compare current frame to last saved frame

import cv2
vidcap = cv2.VideoCapture('aranjuez.mp4')

downsample_factor = 30
start_frame = 0

verbose = False
v = verbose

verbose_mean_stddev = True
m = verbose_mean_stddev

save_all_diffs = False
save_only_big_diffs = True


if v: print('hello world')
last_saved = None

success,image = vidcap.read()
count=0

max_count = -1
there_is_a_max =  (max_count > 0)

saved_count = 0


#made-up thresholds
"""
mean_low_bound = 125
mean_high_bound = 128
stddev_lower = 3
"""
mean_low_bound = 115
mean_high_bound = 127.5
stddev_lower = 30


while success:
    if count % downsample_factor != start_frame:
        success,image = vidcap.read()
        count+=1
        continue
        
    
    count += 1

    #doing comparison differently
    #frames are unique but to the human eye are the exact same
    #therefore will blur and compare
    #nix that
    #I am doing an average pixel difference

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image_blurred = cv2.medianBlur(image, 3)


    
    if there_is_a_max:
        if count > max_count:
            break


    if type(last_saved) == type(None):
        cv2.imwrite('frames/frame-%d.jpg' % count, image)
        saved_count +=1
        
        last_saved = image
        success,image = vidcap.read()
        continue
        
    if (image == last_saved).all(): #since it is an array of bools
        if v: print('frame %d seen' % count)
        pass
    
    else:
        #if count > 1:
        if v: print('count=',count)
        
        diff = ((image-last_saved) + 255) // 2
        if save_all_diffs: cv2.imwrite('frames/diff-%d-%d.jpg' % (count-1, count), diff)
            
        #mean, stddev=cv.meanStdDev(src[, mean[, stddev[, mask]]])
        if v: print(diff)
        mean, stddev= cv2.meanStdDev(diff)


        #this is an OR, not an AND
        #if (int(mean) not in mean_bounds) or (stddev > stddev_lower):
        #if mean > mean_high_bound or mean < mean_low_bound or stddev > stddev_lower:
        #want to be more strict. changing to an AND.
        if (mean > mean_high_bound or mean < mean_low_bound) and stddev > stddev_lower:
            if v: print('frame %d unique' % count)
            last_saved = image
            cv2.imwrite('frames/frame-%d.jpg' % count, image)
            saved_count+=1


            if save_only_big_diffs: cv2.imwrite('frames/diff-%d-%d.jpg' % (count-1, count), diff)
            
            saved_bool = True
        else:
            saved_bool = False
                
            
        #if m: print('frame', count, saved_bool, ':', mean[0][0], stddev[0][0], saved_bool)

        if m: print('frame %d %d m%d s%d' % (count, int(saved_bool), mean[0][0], stddev[0][0]))




            
    success,image = vidcap.read()

print('\nreviewed %d frames and saved %d to frames/' % (count, saved_count))

'''
#testing saving file to a directory
#this works

if success:
    print('unique frame')
    cv2.imwrite('frames/frame.jpg', image)
    current_frame = image

success,image = vidcap.read()

if (image == current_frame).all():
    print('duplicate')
else:
    print('unique frame')
    cv2.imwrite('frames/next.jpg', image)
    current_frame = image
'''

'''
#original code

https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
accessed June 11 2020 around noon

while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
'''



