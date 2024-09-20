import unittest
from EmotionDetection import emotion_detector

# string for the emotions to test on
JOY_KEY = "joy"
ANGER_KEY = "anger"
DISGUST_KEY = "disgust"
SADNESS_KEY = "sadness"
FEAR_KEY = "fear"

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_valid_input(self):
        """
        Test the emotion_detector with valid input text.
        """

        # test joy
        test_text_joy = "I am glad this happened"
        self.ensure_correct_emotion(test_text_joy, JOY_KEY)

        # test anger
        test_text_anger = "I am really mad about this"
        self.ensure_correct_emotion(test_text_anger, ANGER_KEY)

        # test disgust
        test_text_disgust = "I feel disgusted just hearing about this"       
        self.ensure_correct_emotion(test_text_disgust, DISGUST_KEY)
        
        # test sadness
        test_text_sadness = "I am so sad about this"
        self.ensure_correct_emotion(test_text_sadness, SADNESS_KEY)

        # test fear
        test_text_fear = "I am really afraid that this will happen"
        self.ensure_correct_emotion(test_text_fear, FEAR_KEY)

    def ensure_correct_emotion(self, emotion_sentence, emotion_key):
        # This helper method verifies the result given text and its expected key
        result = emotion_detector(emotion_sentence)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], emotion_key)

if __name__ == '__main__':
    unittest.main()