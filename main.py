import os
from PIL import Image

os.system('cmd /c "cls"')

while True:
    print("Vuoi ridimensionare un file o tutti i file della cartella corrente?")
    print("1. Uno o più files")
    print("2. Tutti i files")
    type = input("> ")

    list_files = os.listdir("./imgs/")

    if type == "1":
        os.system('cmd /c "cls"')
        while True:
            print("Selezionare files:")
            print("(ogni numero deve essere diviso da uno spazio)")

            for i in range(0, len(list_files)):
                print(str(i) + ". " + list_files[i])
            list_opt = input("> ")

            files = [int(x) for x in list_opt.split()]
            if files[len(files)-1] <= len(list_files):
                break
            print("Opzione invalida!")
            print()
        break
        
    elif type == "2":
        files = []
        for i in range(0, len(list_files)):
            files.append(i)
        break

    print("Opzione non valida!")
    print()


print("Di quanto vorresti ridimensionare la/le foto?")
print("(25%, 50%, 75%...)")

resize = int(input("> ").replace('%', ''))

for file in files:
    print(list_files[file])
    img = Image.open("./imgs/"+list_files[file])
    size = tuple(int(ti-(ti*resize/100)) for ti in img.size)
    name, extension = os.path.splitext('./imgs/'+list_files[file])
    
    img.resize(size).save(name+'_less'+extension)

    print("Original resolution: "+str(img.size[0])+" x "+str(img.size[1]))
    ori_size = os.stat("./imgs/"+list_files[file]).st_size / (1024 * 1024)
    print("Original size: "+str(float(f'{ori_size:.3f}'))+"MB")
    print("Final resolution: "+str(size[0])+" x "+str(size[1]))
    fin_size = os.stat(name+'_less'+extension).st_size / (1024 * 1024)
    print("Final size: "+str(float(f'{fin_size:.3f}'))+"MB")
    print()

print()
print("Fatto!")
exit()