import os
import datetime

print(dir(os))

print(os.getcwd())

print(os.listdir())

#os.chdir('..')

print(os.getcwd())

print(os.listdir())

# os mkdir to make directorys on surfes level
# os.mkdir('yash')

# os makedirs use to make child directory and perent directy in same code
# os.makedirs('yash/vachhani')

# rmdir use to remove directorys
# os.rmdir('yash')

# removedirs use to remove child and perent directory at the same time
# os.removedirs('yash/vachhani')

# to rename the folder
# os.rename('os.py','rename.txt')

# os stat gives information about last modification file size kind of file info
mod_time = os.stat('temp.py').st_mtime
#print(datetime.fromtimestamp(mod_time))

# walk returns tree of all the files and folders 
for dp, dn, fn in os.walk('.'):
   print(f'cp : {dp}')
   print(f'dir : {dn}')
   print(f'files : {fn}')
   print()

print(os.environ.get('HOME'))

# combine path using os path join

filepath = os.path.join(os.environ.get('HOME'),'test.txt')
print(filepath)

