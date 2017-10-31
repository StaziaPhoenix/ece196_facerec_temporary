import glob, os, time, cv2, shutil

def main():
    
   list1= glob.glob('./stazia/*.jpg')
   list2= glob.glob('./umut/*.jpg')

   for i in range(19):

       if i < 10:
           _list = glob.glob('./yaleB_faces/0%s/*' % i)
       else:
           _list = glob.glob('./yaleB_faces/%s/*' % i)

       os.mkdir('./data/train/%s' % i)
       os.mkdir('./data/validate/%s' % i)
       os.mkdir('./data/test/%s' % i)
   
#    shutil.copyfile(stazia,data)
       tr=int(0.7*len(_list));
       val=int(0.1*len(_list));
       tst=int(0.2*len(_list));
   
       for j in range(tr):
        shutil.copyfile(_list[j],'./data/train/%s/%s.jpg' % (i,j))
        shutil.copyfile(_list[j],'./data/train/%s/%s.jpg' % (i,j))
    
       for k in range(val):
        shutil.copyfile(_list[k+tr],'./data/validate/%s/%s.jpg' % (i,k+tr))
    
       for l in range(tst):
        shutil.copyfile(_list[l+tr+val],'./data/test/%s/%s.jpg' % (i,l+tr+val))
    
#   print (list1)

if __name__ == "__main__":
    main()

