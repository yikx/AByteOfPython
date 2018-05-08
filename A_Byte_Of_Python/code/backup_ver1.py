# -*- coding: utf-8 -*-
#filename:backup_ver1.py

import os
import time

#1. the files and directories to be backed up are specified in a list.
source = [r'E:\code', r'E:\books']

#2. the backup must be stored in a mina backup directory
target_dir = r'E:\backup'

#3. The files are backed up to a zip file.
#4. the name of the zip archive is the current date and time.
target = target_dir + time.strftime('%Y%m%d%H%M%S')+ '.zip'

#5. Use the bandizip command to put the files in a zip  archive
#在自己电脑中安装7zip压缩软件，并把安装目录添加到系统PATH中
zip_command = '7z a {} {}'.format(target,' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")