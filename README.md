***************************************************************
HW1 Repostory on Github :>> https://github.com/obadaq/PIS_HW4 *
***************************************************************

the project consist of 2 .py files

- main.py : this file contain the defined functions
- test.py : the over all code that uses the functions to stitch the images

******************************************************************************************************************************
main.py :>>

the defined functions as follows :>>
1. read_images_paths :>> this function reads the test images folder inside the project and output a list of paths to use 
later in the code
2. rms  :>> this function compute RMS value for two 1 dim arrays																
3.test_sides :>> this function takes two image parts and slice the edges then test the similatites using prev. RMS function 
after converting to GRAY SCALE and output an integer number from 0->3 represinting the most similar edges to stitch later using another function
4.merge_images :>> this function takes the prev. function output and merge the two parts in the best position 


******************************************************************************************************************************

test.py :>>

the test progrom uses the functions in main.py to solve the hw>>

@ first the user is required to choose an image half to start stitching from and then follows the prev> mentioned algorithm
the program opens the selected half and shows the result after stitching "WITHOUT SAVING" to make it obvious that the program
is dowing the stitch not opening a prev> saved image 

******************************************************************************************************************************
******************************************************************************************************************************
# PIS_HW4
[HW04.pdf](https://github.com/obadaq/PIS_HW4/files/10472934/HW04.pdf)
