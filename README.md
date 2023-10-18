# rodrigo
Sheet music video to pdf.
I used this when I wanted the sheet music for Rodrigo's Concierto de Aranjuez, but I never used it. These scripts can be used for any sheet music video.

This code only does part of the process as of now: 1-attempt.py takes a video and separates the unique frames into a directory, and manual.py is a second check to filter out frames which are practically identical but technically not duplicates (this is done by hand).

This repo includes a folder called final/ which would include the jpgs resulting from the code. I have only added one frame from this folder as an example. See below:

![](https://github.com/aisilva/rodrigo/blob/main/final/24.jpg)

In bugtesting this code I made some "difference frames" like this one:

![](https://github.com/aisilva/rodrigo/blob/main/first-diff.jpg)


Future steps include:

-deleting black bars from the image

-stitching jpgs into a pdf, perhaps by using LaTeX

