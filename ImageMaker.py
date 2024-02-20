from PIL import Image

# Create a small image with a solid color (e.g., red)
img = Image.new('RGB', (100, 100), "red")
img.save("Assets/test_image.jpeg")