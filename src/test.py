from tensorflow.keras.preprocessing import image
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace


model=VGGFace(model='vgg16')
img_path='D:\\bollywood_celeb_recognition\\artifacts\\upload\\WhatsApp Image 2022-04-12 at 3.20.06 PM.jpeg'
img=image.load_img(img_path, target_size=(224,224))
