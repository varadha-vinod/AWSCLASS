import os

dirname = 'D:\Vinod'
folder = 'vinod'
os.chdir(dirname)
print(os.getcwd())
for i in range (10):
    print("Value is ", i)
    dir = f'{folder}{i}'
    print(dir)
    print(os.getcwd())
    if os.path.isdir(dir):
        print("dir exists")
    else:
        print("dir not exists")
        os.mkdir(dir)

    os.chdir(dir)
    filename = dir + '.txt'
    if os.path.isfile(filename):
        print (filename + '  ' "already exists")
    else:
        print(filename)
        open(filename,"w+")
    os.chdir(dirname)

print("Creating folders and files are done")