# rodrigo
Sheet music video to pdf
This code only does part of the process as of now: 1-attempt.py takes a video and separates the unique frames into a directory, and manual.py is a second check to filter out frames which are practically identical but technically not duplicates (this is done by hand).

Not added to the repo are the folders holding the resulting jpgs like the one below:

![](https://github.com/aisilva/rodrigo/blob/main/final/24.jpg)

In bugtesting this code I made some "difference frames" like this one:

![](https://github.com/aisilva/rodrigo/blob/main/first-diff.jpg)


Future steps include:

-deleting black bars from the image

-stitching jpgs into a pdf, perhaps by using LaTeX

