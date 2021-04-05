from functionCode.PixelType_header import *
import numpy as np

def Is_color_data(enGvspPixelType):
	if PixelType_Gvsp_BayerGR8 == enGvspPixelType or PixelType_Gvsp_BayerRG8 == enGvspPixelType \
			or PixelType_Gvsp_BayerGB8 == enGvspPixelType or PixelType_Gvsp_BayerBG8 == enGvspPixelType \
			or PixelType_Gvsp_BayerGR10 == enGvspPixelType or PixelType_Gvsp_BayerRG10 == enGvspPixelType \
			or PixelType_Gvsp_BayerGB10 == enGvspPixelType or PixelType_Gvsp_BayerBG10 == enGvspPixelType \
			or PixelType_Gvsp_BayerGR12 == enGvspPixelType or PixelType_Gvsp_BayerRG12 == enGvspPixelType \
			or PixelType_Gvsp_BayerGB12 == enGvspPixelType or PixelType_Gvsp_BayerBG12 == enGvspPixelType \
			or PixelType_Gvsp_BayerGR10_Packed == enGvspPixelType or PixelType_Gvsp_BayerRG10_Packed == enGvspPixelType \
			or PixelType_Gvsp_BayerGB10_Packed == enGvspPixelType or PixelType_Gvsp_BayerBG10_Packed == enGvspPixelType \
			or PixelType_Gvsp_BayerGR12_Packed == enGvspPixelType or PixelType_Gvsp_BayerRG12_Packed == enGvspPixelType \
			or PixelType_Gvsp_BayerGB12_Packed == enGvspPixelType or PixelType_Gvsp_BayerBG12_Packed == enGvspPixelType \
			or PixelType_Gvsp_YUV422_Packed == enGvspPixelType or PixelType_Gvsp_YUV422_YUYV_Packed == enGvspPixelType:
		return True
	else:
		return False


def Is_mono_data(enGvspPixelType):
	if PixelType_Gvsp_Mono8 == enGvspPixelType or PixelType_Gvsp_Mono10 == enGvspPixelType \
			or PixelType_Gvsp_Mono10_Packed == enGvspPixelType or PixelType_Gvsp_Mono12 == enGvspPixelType \
			or PixelType_Gvsp_Mono12_Packed == enGvspPixelType:
		return True
	else:
		return False


def Mono_numpy(data, nWidth, nHeight):
	data_ = np.frombuffer(data, count=int(nWidth * nHeight), dtype=np.uint8, offset=0)
	data_mono_arr = data_.reshape(nHeight, nWidth)
	numArray = np.zeros([nHeight, nWidth, 1], "uint8")
	numArray[:, :, 0] = data_mono_arr
	return numArray


def Color_numpy(data, nWidth, nHeight):
	data_ = np.frombuffer(data, count=int(nWidth * nHeight * 3), dtype=np.uint8, offset=0)
	data_r = data_[0:nWidth * nHeight * 3:3]
	data_g = data_[1:nWidth * nHeight * 3:3]
	data_b = data_[2:nWidth * nHeight * 3:3]

	data_r_arr = data_r.reshape(nHeight, nWidth)
	data_g_arr = data_g.reshape(nHeight, nWidth)
	data_b_arr = data_b.reshape(nHeight, nWidth)
	numArray = np.zeros([nHeight, nWidth, 3], "uint8")

	numArray[:, :, 2] = data_r_arr
	numArray[:, :, 1] = data_g_arr
	numArray[:, :, 0] = data_b_arr
	return numArray