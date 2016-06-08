import os,sys;

if(len(sys.argv) >= 2) :
  dirPath = sys.argv[1];
else:
  dirPath = "~/share/Video";


fileGrep = '-not -iname "*.avi" -not -iname "*.mkv" -not -iname "*.rmvb" -not -iname "*.mp4" -not -iname "*.3gp" -not -iname "*.flv" -not -iname "*.mpg" -not -iname "*.mgeg" -not -iname "*.swf" -not -iname "*.wmv" -iname "*.rm"';

command = 'sudo find ' + dirPath + ' -type f -size -100000 ' + fileGrep + ' -exec rm -fv {} \;';

os.system(command);

command = 'sudo find ' + dirPath + ' -type d -empty -exec rmdir {} \;';
os.system(command);
