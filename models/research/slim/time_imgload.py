import tensorflow as tf
import urllib.request as urllib
import time
tf.enable_eager_execution()

url = 'https://upload.wikimedia.org/wikipedia/commons/7/70/EnglishCockerSpaniel_simon.jpg'
image_string = urllib.urlopen(url).read()
image = tf.image.decode_jpeg(image_string, channels=3)

start = time.clock()
image = tf.image.decode_jpeg(image_string, channels=3)
end = time.clock()
print('time', (end - start))
