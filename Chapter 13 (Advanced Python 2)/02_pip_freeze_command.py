# 'pip freeze' returns all the package installed in a given python environment along with the versions.

# Command is:
pip3 freeze






# pip freeze > requirements .txt command:
# The above command creates a file named 'requirements.txt' int the same directory containing the output of 'pip freeze'

# We can distribute this file to other users, and they can recreate the same environment using:
# pip3 install -r requirements.txt