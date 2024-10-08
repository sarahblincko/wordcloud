import streamlit as st
import wordcloud_starter_code as wc

st.title("Wordcloud Creator")

text =st.text_area("Please add your text", value="Please add your text or upload a text file below")

uploaded_text =st.file_uploader(
    "Please upload a text file",
    type=['txt']
)

chosen_colour_option = st.selectbox(
   "Choose a colour scheme",
    ["Blues", "Reds", "Greens"],
)

stopwords_extra_users= st.text_area("Please add words to remove from the wordcloud")

# # setting as a list
stopwords_extra_users_list=stopwords_extra_users.split()

image_mask = st.file_uploader(
    "Please upload a jpg file to be used as a mask",
    type=['jpg']
)

if uploaded_text is not None:
    uploaded_text = uploaded_text.read().decode("utf-8")
    text=uploaded_text
    
    wc.make_wordcloud_with_image_mask(text, "penguin_sample_wordcloud_sb.png",
                                    colormap=chosen_colour_option,
                                    mask_image=image_mask,
                                    stopwords_extra=stopwords_extra_users_list 
                                    )

    st.image("penguin_sample_wordcloud_sb.png")

    with open("penguin_sample_wordcloud_sb.png", "rb") as file:
        btn = st.download_button(
            label="Click Here to Download Your Word Cloud!",
            data=file,
            file_name="my_wordcloud.png",
            mime="image/png",
        )
elif text is not None:
    wc.make_wordcloud_with_image_mask(text, "penguin_sample_wordcloud_sb.png",
                                      colormap=chosen_colour_option,
                                      mask_image=image_mask,
                                      stopwords_extra=stopwords_extra_users_list 
                                      )

    st.image("penguin_sample_wordcloud_sb.png")

    with open("penguin_sample_wordcloud_sb.png", "rb") as file:
        btn = st.download_button(
            label="Click Here to Download Your Word Cloud!",
            data=file,
            file_name="my_wordcloud.png",
            mime="image/png",
        )