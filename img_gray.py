#Sai

from PIL import Image

def main():
    path = input("Enter the path of image: ")
    try:
        img = Image.open(path)
        gray_scale(img)
    except:
        print(path,"is not a valid path to an image ")


def gray_scale(img):
    gray_img = img.convert('L')
    gray_img.save("Grayscale.jpg")
    print("Image saved as Grayscale.jpg")

main()