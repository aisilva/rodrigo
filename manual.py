import numpy as np
import glob
import cv2

count = 2

filenames = glob.glob("frames/*.jpg")
#filenames.sort()
#print(filenames)

d = {}


for f in filenames:
    try:
        d[int(f[13:-4])] = f
    except:
        print('not an int. you\'re doing something wrong.')
        raise TypeError


keys = sorted(d.keys())
name1 = d[keys[0]]
first = cv2.imread(name1)
cv2.imwrite('final/1.jpg', first)
saved = [name1]

count = 2


for i in range(2, len(keys)):
    key = keys[i]
    name = d[key]

    old_img = cv2.imread(saved[-1])
    img = cv2.imread(name)

    res_old = cv2.resize(old_img, dsize=(600,450), interpolation=cv2.INTER_CUBIC)
    res = cv2.resize(img, dsize=(600,450), interpolation=cv2.INTER_CUBIC)

    cv2.imshow('fuck', (res+res_old )//2)
  
    
    #numpy_horizontal_concat = np.concatenate((res_old, res), axis=1)
    #cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
    x=cv2.waitKey(0)


    if x == 110:
        print('no')
    elif x == 121:
        print('yes')
        cv2.imwrite('final/%d.jpg' % count, img)
        saved.append(name)
        count+=1 
        
    cv2.destroyAllWindows()
    



"""    
for x in sorted(d.keys()):
    #cv2.imshow('hello', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
 

    print(x, d[x])
        
#images = [cv2.imread(img) for img in filenames]

#cv2.imwrite('final/%d.jpg' % count)

#for img in images:
#print img
"""
