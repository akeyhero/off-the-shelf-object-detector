import tensorflow as tf
import tensorflow_hub as hub


class Detector():
    """Off-the-shelf object detector interface"""

    def __init__(self, hub_model_url):
        self.hub_model_url = hub_model_url

    def prepare(self):
        """Prepare for detection"""
        self.detector = hub.load(self.hub_model_url).signatures['default']

    def detect(self, image_bin, threshold=0.5):
        """Detect objects"""
        image = tf.image.decode_image(image_bin, channels=3)
        converted_image = tf.image.convert_image_dtype(image, tf.float32)[tf.newaxis, ...]
        result = self.detector(converted_image)
        return [list(box.numpy().astype(float))
                for box, score in zip(result['detection_boxes'], result['detection_scores'])
                if score >= threshold]

