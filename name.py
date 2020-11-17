import modules
files = modules.browse()

for filenames in files:
    file = files[n]
    name = modules.name(file)
    encoded = modules.enc(file)
    list = [name , encoded]
    print(list)
