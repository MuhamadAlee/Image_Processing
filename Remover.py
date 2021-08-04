from PIL import Image
import hashlib
import glob
for img in glob.glob("images/*"):
    md5hash = hashlib.md5(Image.open(img).tobytes())
    hsh=md5hash.hexdigest()
    image=Image.open(img)
    image.save("results/"+str(hsh)+".jpg")
