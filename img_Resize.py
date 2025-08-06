#Sai

from PIL import Image

def resize_img(img):
    new_height = int(input("new Height?"))
    new_width = int(input("new Width?"))
    width, height = img.size
    resize_image =img.resize((new_width,new_height))
    resize_image.save("Resize_Image.jpg")
    print("Image saved as Resize_Image.jpg")

def main():
    path = input("Enter the path of image: ")
    try:
        img = Image.open(path)
        resize_img(img)
    except:
        print(path,"is not a valid path to an image ")

main()
