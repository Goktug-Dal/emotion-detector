import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1: Joy
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        # Test case 2: Anger
        result = emotion_detector("I am really angry right now!")
        self.assertEqual(result['dominant_emotion'], 'anger')
        
        # Test case 3: Fear
        result = emotion_detector("I am scared of the dark.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
