import os
import glob
count=0
for img in sorted(glob.glob('images/*')):
  new=img.split('/')[:-1]
  new='/'.join(new)
  new=new+"/"+str(count)+".jpg"
  count+=1
  print(img,new)
  os.rename(img,new)
