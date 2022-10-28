import sys
import cv2
import numpy as np

SPECTRUM_LENGTH = 256

def make_row_spectrum(FileName):
  img = cv2.imread(FileName)
  if img is None:
    sys.exit(f"Cannot open an image {FileName}")
  
  sp = cv2.cvtColor(cv2.resize(img, (SPECTRUM_LENGTH, 1)), cv2.COLOR_BGR2HSV)
  return sp

def make_cnv_map(SrcSpectrum, DstSpectrum):
  Result = [None] * 256 #180 for H actually
  # np.random.shuffle(DstSpectrum[0])
  for i in range(SrcSpectrum.shape[1]):
    Result[SrcSpectrum[0, i, 0]] = DstSpectrum[0, i, 0]

  return Result

def convert(Img, CnvMap):
  HSVImg = cv2.cvtColor(cv2.imread(sys.argv[3]), cv2.COLOR_BGR2HSV)

  for i in range(HSVImg.shape[0]):
    for j in range(HSVImg.shape[1]):
      V = CnvMap[HSVImg[i,j,0]] or HSVImg[i,j,0]
      # print(HSVImg[i,j,0], "->", V, ";", CnvMap[HSVImg[i,j,0]])
      HSVImg[i,j,0] = V

  return cv2.cvtColor(HSVImg, cv2.COLOR_HSV2BGR)
  
def main():
  if(len(sys.argv)) < 4:
    print("Usage: spectrum <SrcSpectrumFile> <DstSpectrumFile> <SourceFile>")
    return 1
  SrcSpectrumFile = sys.argv[1]
  DstSpectrumFile = sys.argv[2]

  print(f"Video spectrum conversion. Src spectrum: {SrcSpectrumFile}; dst spectrum: {DstSpectrumFile}")

  SrcSpectrum = make_row_spectrum(SrcSpectrumFile)
  DstSpectrum = make_row_spectrum(DstSpectrumFile)

  DstImg = convert(cv2.imread(sys.argv[3]), make_cnv_map(SrcSpectrum, DstSpectrum))
  cv2.imwrite("result.jpg", DstImg)
  cv2.imshow("result", DstImg)
  cv2.waitKey()
  cv2.destroyAllWindows()

  return 0

if __name__ == "__main__":
   main()