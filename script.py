import subprocess

subprocess.Popen('for file in ./fixtures/*.json; do filename=$(basename "$file"); python manage.py loaddata ./fixtures/"$filename"; done', shell=True) 