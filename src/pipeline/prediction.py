import tensorflow as tf
import numpy as np
import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    def predict(self):
        model = tf.keras.models.load_model(os.path.join("models", "model.h5"))

        test_image = tf.keras.preprocessing.image.load_img(self.filename, target_size = (224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        os.remove(self.filename)

        if result[0] == 1:
            prediction = 'Normal'
            return [{"image" : prediction}]
        else:
            prediction = 'Adenocarcinoma Cancer'
            return [{"image" : prediction}]
