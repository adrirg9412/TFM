images = [os.path.join('images', x) for x in os.listdir('images')]
annotations = [os.path.join('annotations', x) for x in os.listdir('annotations') if x[-3:] == "txt"]

list_img=[]
list_ann=[]

for name_img in images:
    list_img.append(name_img.split('/')[1].split('.')[0])

for name_ann in annotations:
    list_ann.append(name_ann.split('/')[1].split('.')[0])

for item in list_img:
    if item not in list_ann:
        print(item)