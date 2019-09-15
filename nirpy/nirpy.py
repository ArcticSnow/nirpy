'''
See the paper by Matzl and Schneebeli 2016 for more info

A calibration profile was derived from the camera with Micmac. This calibration profile is for correcting vigneting.
correct image for vignetting (calib profile is of the size of Raw images. Crop from center to use with jpegs
detrend if needed the luminosity, as it can vary linearly from top to bottom of the snowpit
sample targets for absolute reflectance calibration (white= 99%, and grey=50%). Fit a linear model
Convert reflectance image to SSA with the conversion equation  𝑆𝑆𝐴=𝐴𝑒𝑟/𝑡

Finally, use the ruler (or other object of know size) in image to scale image dimension to metric system.
TODO:

write functions for all steps
wrap all in a python package/class
write function to extract profiles, and maybe later identify layers using reflectance/SSA, and contrast enhanced image
write function to extract SSA profile to import in niviz.org
include class to compute
Raw images are in 12 bit. Find a way to convert to BW from original while maintaining the 12bit resolution. Rawpy might be useful. Then make sure the processing pipeline can accept 12bit data (i.e. all skimage functions)
wrap micmac function to extract profile 'mm3d vodka'. At least provide the method on how to do it.

'''

import skimage as sk
import rawpy
import imageio

raw = rawpy.imread('image.nef')
rgb = raw.postprocess()
imageio.imsave('default.tiff', rgb)

class micmac_nir():
    '''
    Class to correct images via micmac. with mm3d vodka
    '''



class nir(object):
    def __init__(self):
        self.fname = None

    def load_raw(self):
        '''
        1. open raw in 12bit
        2. convert RGB to HSV (only keep V) in 12bit
        :return: return the black and white array in 12bit
        '''
        return

    def load_jpeg(self):
        '''
        function to load jpeg NIR images, and convert them to BW
        :return:
        '''
        return

    def load_array(self):
        '''
        Function to data if saved in a 2D array format.
        '''
        return

    def read_exif(self):
        '''
        function to read image exif
        :return:
        '''
        return

    def apply_vignetting(self):
        '''
        Apply via Python the
        :return:
        '''

    def detrend_limunosity_gradient(self):
        '''
        Function to detrend the luminosity gradient (vertical and/or horizontal)
        :return:
        '''

    def extract_profile(self):
        '''function to extract profile
        1. one single pixel profile
        2. multiple profile, and return aggregate profile (mean, median, min, max, std)
        '''
        return

    def calibrate_targets(self):
        '''
        Function to derive reflectance calibration value from targets (50% and 90%)
        :return:
        '''
        return

    def apply_calibration(self):
        '''
        apply reflectance calibration from targets
        :return:
        '''
        return

    def ref2ssa(self):
        '''
        function to compute SSA from reflectance value
        :return:
        '''
        return

    def ssa2d(self):
        '''
        function to derive optical diameter of grain from SSA values
        :return:
        '''
        return