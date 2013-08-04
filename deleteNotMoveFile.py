import os;

fileGrep = '-not -iname "*.avi" -not -iname "*.mkv" -not -iname "*.rmvb" -not -iname "*.mp4" -not -iname "*.3gp" -not -iname "*.flv" -not -iname "*.mpg" -not -iname "*.mgeg" -not -iname "*.swf" -not -iname "*.wmv"';

command = 'sudo find ~/share/movie/Video -type f -size -100000 ' + fileGrep + ' -exec rm -fv {} \;';

os.system(command);
