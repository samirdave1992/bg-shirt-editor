import streamlit as st
from PIL import Image
import os
import glob
import numpy as np

st.header("Shirt Background Editor")

mask = Image.open("mask/mask.png").convert("L")
fs = Image.open("mask/ship.png")

st.markdown('<p class="font">Upload your Background photo here:</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
if uploaded_file is not None:

    bg=Image.open(uploaded_file)
    st.markdown(bg.size,unsafe_allow_html=True)
    st.image(bg)

st.markdown('<p class="font">Upload your shirts with white background here:</p>', unsafe_allow_html=True)


form=st.form("form")
with form:
    col1,col2,col3=st.columns(3)

    with col1:
        shirt1=st.file_uploader("Shirt #1", type=['jpg','png','jpeg'])


    with col2:
        shirt2=st.file_uploader("Shirt #2", type=['jpg','png','jpeg'])

    with col3:
        shirt3=st.file_uploader("Shirt #3", type=['jpg','png','jpeg'])


submitButton = form.form_submit_button(label = 'Submit')

@st.cache(suppress_st_warning=True)
def edits(img,bg):
    mask = Image.open("mask/mask.png").convert("L")
    fs = Image.open("mask/ship.png")
    image = Image.open(img)
    if mask.size==image.size:
        print("All Good with mask size")
    else:
        mask=mask.resize(image.size, Image.Resampling.LANCZOS)
    st.write(image.size)
    st.write(mask.size)
    # Apply Mask- This merges Mask template with our image
    image.putalpha(mask)
    # resize background
    bg = bg.resize(image.size, Image.Resampling.LANCZOS)
    # # This merges background with the masked image
    result = Image.alpha_composite(bg, image)

    # Upscale everything back to 2000,2000
    result = result.resize((2000,2000),Image.Resampling.LANCZOS)

    # Add the free shipping badge
    result = Image.alpha_composite(result,fs)

    if result is not None:
        st.image(
            result,
            caption=f"size of the image is {(result.size)}",
            use_column_width=True
        )



if submitButton:
    edits(shirt1,bg)
    edits(shirt2,bg)
    edits(shirt3,bg)



#    img_array = np.array(image)
 #   image.putalpha(mask)


# if image is not None:
#     st.image(
#         image,
#         caption=f"You image has shape {img_array.shape[0:2]}",
#         use_column_width=True
#     )

    # Apply Mask- This merges Mask template with our image

 #   img_array = np.array(shirt1)
    # Apply Mask- This merges Mask template with our image



        
    #     # Apply Mask- This merges Mask template with our image
    #     fg.putalpha(mask)
    #     # resize background
    #     bg = bg.resize(fg.size, Image.Resampling.LANCZOS)
    #     # # This merges background with the masked image
    #     result = Image.alpha_composite(bg, fg)

    #     # Upscale everything back to 2000,2000
    #     result = result.resize((2000,2000),Image.Resampling.LANCZOS)

    #     # Add the free shipping badge
    #     result = Image.alpha_composite(result,fs)

    # # # Save the result
    # st.image(result)

# if submitButton:
#     print("test")
#     edits(shirt1)
#     edits(shirt2)
#     edits(shirt3)











#st.image(image, caption='Sunrise by the mountains')
