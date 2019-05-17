# python-fourier-transform
Fourier Transform in Python applied on greyscale images using numpy and cv2

-----

This is my first project in Python using the Fourier Transform (DFT). The goal of this project was to get some more knowledge and understanding about how DFT works. As a part of my PhD study, I will be working with DFT and image processing, so this seemed like a good idea.

The original image, named 'Siqijor', is named after the location it was taken at - Siqijor Island in the Philippines. If you look closer, you can see me under the Ocean surface :)

Noises applied over the original image are examples of the Moiré Pattern (https://en.wikipedia.org/wiki/Moiré_pattern) Apart from Python, I used Adobe Photoshop CC to apply certain effect to the original image (the .psd file is also included in the repository).

-----

The result images are not perfect, but the main idea is pretty straightforward:
  1. After importing the 'noisy' image, transform the image into the Fourier Domain
  2. Find the frequency pattern that 'sticks out'
  3. Create an image to mask over that frequency (black areas block those frequencies)
  4. Create the return image using the Inverse Fourier Transform
  
-----

Hopefully, I'll be uploading more similar projects with more complex code and more precise results.

-----

Resources I found useful for the project:

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

https://youtu.be/spUNpyF58BY

https://youtu.be/mEN7DTdHbAU
