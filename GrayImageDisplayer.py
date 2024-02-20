from PIL import Image


from PIL import Image

def show_image(image_path, convert_to_gray=False):
    # Open image
    image = Image.open(image_path)

    # Optionally convert to grayscale
    if convert_to_gray:
        image = image.convert('L')

    # Show the image
    image.show()


