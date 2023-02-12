from PIL import Image
import os
import glob
 
 #This is to fetch the contents from the folder
# for x in os.listdir('shirts'):
#     if x.endswith(".jpg") or x.endswith(".png"):
#          print(x)

path='/Users/Samir/Desktop/ETSY/GeekShirtDesigns/TEST WITH CODE/shirts/'




    # print(fg.size)
    # print(mask.size)

    # print(bg.size)

    # print(fs.size)




# for x in os.listdir(path):
#     print(x)

images = glob.glob("/Users/Samir/Desktop/ETSY/GeekShirtDesigns/TEST WITH CODE/shirts/*.png")
for image in images:
    with open(image, 'rb') as file:
        fg = Image.open(file)
        mask = Image.open("mask.png").convert("L")
        bg = Image.open("background.png")
        fs = Image.open("ship.png")
        if mask.size==fg.size:
            print("All Good with mask size")
        else:
            mask=mask.resize(fg.size, Image.Resampling.LANCZOS)
        # Apply Mask- This merges Mask template with our image
        fg.putalpha(mask)
        # resize background
        bg = bg.resize(fg.size, Image.Resampling.LANCZOS)
         # # This merges background with the masked image
        result = Image.alpha_composite(bg, fg)

        # Upscale everything back to 2000,2000
        result = result.resize((2000,2000),Image.Resampling.LANCZOS)

        # Add the free shipping badge
        result = Image.alpha_composite(result,fs)

        # # Save the result
        result.show()
        result.save(f"{image}")



# def merge_bg():
#     # Load the images
#     for x in os.listdir('shirts'):
#         if x.endswith(".jpg") or x.endswith(".png"):
#              with open(x, 'rb') as file:
#                  img=Image.open(file) 
#                  img.show()

# merge_bg()
    # mask = Image.open("mask.png").convert("L")
    # bg = Image.open("background.png")
    # fs = Image.open("ship.png")
    # if mask.size==fg.size:
    #     print("All Good with mask size")
    # else:
    #    mask = mask.resize(fg.size, Image.LANCZOS)
       
    # # Apply Mask- This merges Mask template with our image
    # fg.putalpha(mask)
    # # resize background
    # bg = bg.resize(fg.size, Image.LANCZOS)

    # # This merges background with the masked image
    # result = Image.alpha_composite(bg, fg)

    # # Upscale everything back to 2000,2000
    # result = result.resize((2000,2000),Image.LANCZOS)

    # # Add the free shipping badge
    # result = Image.alpha_composite(result,fs)

    # # # Save the result
    # result.save("result3.png")



