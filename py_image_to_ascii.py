import sys
from PIL import Image
import numpy as np

# taken from https://gist.github.com/cdiener/10491632
if __name__ == '__main__':
    chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    if len(sys.argv) != 4:
        print('Usage: ./asciinator.py image scale factor')
    f, SC, GCF, WCF = "images/test.jpg", float(0.1), float(1), 7 / 4
    img = Image.open(f)
    S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
    img = np.sum(np.asarray(img.resize(S)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)
    print("here")
    print("\n".join(("".join(r) for r in chars[img.astype(int)])))