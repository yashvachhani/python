'''
# pip help
shows all the commands

# pip help <command>
shows help for spacific command

# pip search <package name>
shows package name and discription

# pip list
shows all the installed package

# pip uninstall <package name>
for uninstall package

# pip list -o
or
# pip list --outdated
shows list of package who has update

# pip install -U <package name>
update package

# pip install <package name> 
install package

# pip freeze > requirements.txt
creats file with package name and version

# pip install -r <file name>.txt
install all the package in requirements.txt file
-r shows that is requirements.txt file to the pip

# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
make list of all outdated packages and updates all
'''