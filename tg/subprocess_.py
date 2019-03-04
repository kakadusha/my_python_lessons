import subprocess
#subprocess.call(['ping', '10.8.5.9'])

process = subprocess.Popen(['ping', 'ya.ru'], stdout=subprocess.PIPE)
data = process.communicate()

for line in data:
    print(line)
