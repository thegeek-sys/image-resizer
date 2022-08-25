import os
from PIL import Image
import argparse

os.system('cmd /c "cls"')
parser = argparse.ArgumentParser()

if not os.path.exists(os.path.join(os.getcwd(), 'imgs')):
    os.mkdir(os.path.join(os.getcwd(), 'imgs'))

parser.add_argument('-s', '--source', type=str, help="input source file")
parser.add_argument('-r', '--resize', type=str, help="percentage of resizing")
args = parser.parse_args()

def resize (path, resize):
    img = Image.open(path)
    resize = int(resize.replace('%', ''))
    size = tuple(int(ti-(ti*resize/100)) for ti in img.size)
    name, extension = os.path.splitext(path)
    
    print()
    print("Saving in: "+name+'_less'+extension)
    img.resize(size).save(name+'_less'+extension)

    print("Original resolution: "+str(img.size[0])+" x "+str(img.size[1]))
    ori_size = os.stat(path).st_size / (1024 * 1024)
    print("Original size: "+str(float(f'{ori_size:.3f}'))+"MB")
    print("Final resolution: "+str(size[0])+" x "+str(size[1]))
    fin_size = os.stat(name+'_less'+extension).st_size / (1024 * 1024)
    print("Final size: "+str(float(f'{fin_size:.3f}'))+"MB")

if args.source and args.resize:
    resize (args.source, args.resize)
    exit()
elif args.source and not args.resize:
    print("Input the percentage reduction of the photo")
    print("(25%, 50%, 75%...)")
    reduction = input("> ")
    resize (args.source, reduction)
    exit()
elif not args.source and args.resize:
    print("Input path of the file you want to resize")
    path = input("> ")
    resize (path, args.resize)
    exit()


while True:
    print("You would like to resize one/more or all the files in the ./imgs/ directory?")
    print("1. One or more files")
    print("2. All the files")
    type = input("> ")

    list_files = os.listdir("./imgs/")

    if type == "1":
        os.system('cmd /c "cls"')
        while True:
            print("Chose files:")
            print("(every number has to be separated by a space)")

            for i in range(0, len(list_files)):
                print(str(i) + ". " + list_files[i])
            list_opt = input("> ")

            files = [int(x) for x in list_opt.split()]
            if files[len(files)-1] <= len(list_files):
                break
            print("Invalid operation!")
            print()
        break
        
    elif type == "2":
        files = []
        for i in range(0, len(list_files)):
            files.append(i)
        break

    print("Invalid operation!")
    print()


print("Input the percentage reduction of the photo/s")
print("(25%, 50%, 75%...)")

reduction = input("> ")

for file in files:
    path = os.path.join(os.getcwd(), 'imgs', list_files[file])
    resize(path, reduction)

print()
print("Fatto!")
exit()