from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

###################################################
###################################################
# Advanced wordcloud function
# This accepts an optional additional image to act
# as a 'mask'
# It also allows users to pass in additional
# parameters that are accepted by the wordcloud
# function itself
###################################################
###################################################

def make_wordcloud_with_image_mask(
        text_input,
        filename="wordcloud.png",
        mask_image=None,
        stopwords_extra=None,
        **kwargs
        ):
    stopwords = set(STOPWORDS)
    if stopwords_extra is not None:
        stopwords.update(stopwords_extra)
        tokens = text_input.split()
        punctuation_mapping_table = str.maketrans('', '', string.punctuation)
        tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                    for token in tokens]
        lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

        joined_string = (" ").join(lower_tokens)

        plt.figure(figsize=(30,40))
        plt.axis("off")

        if mask_image is not None:
            mask_image_opened = Image.open(mask_image)
            mask_array = np.array(mask_image_opened)

            wordcloud = WordCloud(width=mask_array.shape[1],
                        height=mask_array.shape[0],
                        stopwords=stopwords,
                        mask=mask_array,
                        **kwargs).generate(joined_string)

            plt.imshow(wordcloud, interpolation='bilinear')

        else:
            wordcloud = WordCloud(width=1800,
                        height=1800,
                        stopwords=stopwords,
                        **kwargs).generate(joined_string)

            plt.imshow(wordcloud)

        plt.savefig(filename)
    else:
        tokens = text_input.split()
        punctuation_mapping_table = str.maketrans('', '', string.punctuation)
        tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                    for token in tokens]
        lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

        joined_string = (" ").join(lower_tokens)

        plt.figure(figsize=(30,40))
        plt.axis("off")

        if mask_image is not None:
            mask_image_opened = Image.open(mask_image)
            mask_array = np.array(mask_image_opened)

            wordcloud = WordCloud(width=mask_array.shape[1],
                        height=mask_array.shape[0],
                        stopwords=stopwords,
                        mask=mask_array,
                        **kwargs).generate(joined_string)

            plt.imshow(wordcloud, interpolation='bilinear')

        else:
            wordcloud = WordCloud(width=1800,
                        height=1800,
                        stopwords=stopwords,
                        **kwargs).generate(joined_string)

            plt.imshow(wordcloud)

        plt.savefig(filename)