import os,sys;

if(len(sys.argv) >= 2) :
  dirPath = sys.argv[1];
else:
  dirPath = "~/share/Video";

command = 'sudo chown -R xbmc:xbmc ' + dirPath;

os.system(command);
