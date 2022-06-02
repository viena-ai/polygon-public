import json
import glob
import os
import argparse

def main(args)
    images_folder=args.imageFolderPath
    images = glob.glob(images_folder+'')
    lst = []
    for image in images
        filename = os.path.basename(image)
        d1 = {}
        d1['name']=filename
        lst.append(d1.copy())
    json.dumps(lst)

    with open('manifest.json', 'w', encoding='utf-8') as f
        json.dump(lst, f, ensure_ascii=False, indent=1)
    print(sccessfully created the manifest json)
if __name__ == '__main__'
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--imageFolderPath', dest='imageFolderPath', type=str, help='Images folder path')

    args = parser.parse_args()
    if (not (args.imageFolderPath and not args.imageFolderPath.isspace()))
        print(Please provide the images folder path)
    else
        main(args)