from PIL import Image


# Load the images
fg = Image.open("white.jpg")
mask = Image.open("mask.png").convert("L")
bg = Image.open("background.png")
fs = Image.open("ship.png")
mask = mask.resize(fg.size, Image.LANCZOS)

print(fg.size)
print(mask.size)

print(bg.size)

print(fs.size)


# # Apply Mask
# fg.putalpha(mask)

# # resize background
# bg = bg.resize(fg.size, Image.LANCZOS)


# # merk the 2
# result = Image.alpha_composite(bg, fg)

# # Upscale everything back to 2000,2000
# result = result.resize((2000,2000),Image.LANCZOS)

# # Add the free shipping badge
# result = Image.alpha_composite(result,fs)


# # # Save the result
# result.save("result.png")




