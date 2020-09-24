from wordcloud import WordCloud , STOPWORDS , ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

text = open("beginner.txt", 'r').read()
stopwords = set(STOPWORDS)
custom_mask = np.array(Image.open('mask_girl.png'))
wd = WordCloud(background_color = 'White', stopwords = stopwords, mask = custom_mask, max_font_size = 500)
wd.generate(text)

plt.figure()
plt.imshow(wd, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
