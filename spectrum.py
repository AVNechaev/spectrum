import sys
import cv2

SPECTRUM_LENGTH = 256

def make_row_spectrum(FileName):
  img = cv2.imread(FileName)
  if img is None:
    sys.exit(f"Cannot open an image {FileName}")
  
  sp = cv2.resize(img, (SPECTRUM_LENGTH, 10))  
  return sp

def main():
  if(len(sys.argv)) < 3:
    print("Usage: spectrum <SrcSpectrumFile> <DstSpectrumFile>")
    return 1
  SrcSpectrumFile = sys.argv[1]
  DstSpectrumFile = sys.argv[2]
  print(f"Video spectrum conversion. Src spectrum: {SrcSpectrumFile}; dst spectrum: {DstSpectrumFile}")

  SrcSpectrum = make_row_spectrum(SrcSpectrumFile)
  DstSpectrum = make_row_spectrum(DstSpectrumFile)
  
  return 0

if __name__ == "__main__":
   main()