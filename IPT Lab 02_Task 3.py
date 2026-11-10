width=int(input("Enter the image width in pixels:"))
height=int(input("Enter the image height in pixels:"))

total_pixels=width*height

size_bytes=total_pixels

size_kb=size_bytes / 1024
print("Total Pixels:",total_pixels)
print("Image Size in KB:",round(size_kb,2),"KB")