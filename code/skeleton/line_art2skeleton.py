from ai import *

from pathlib import Path
import sys
import cv2

if __name__=='__main__':
    sketch_dir = Path(sys.argv[1])
    skeleton_dir = sketch_dir.with_name(f"{sketch_dir.name}_skeleton")

    if not skeleton_dir.exists():
        skeleton_dir.mkdir()

    for i in sketch_dir.iterdir():
        image = cv2.imread(str(i))
        image = (go_vector(image) * 255.0).clip(0, 255).astype(np.uint8)
        cv2.imwrite(str(skeleton_dir / i.name), image)
