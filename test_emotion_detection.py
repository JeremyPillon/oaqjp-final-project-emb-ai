import unittest
from unittest.mock import patch
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    @patch('emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        # Test case 1: Joy
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95, 'sadness': 0.02}}]
        }
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')

        # Test case 2: Anger
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.95, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.02}}]
        }
        res_2 = emotion_detector("I am really angry about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')

        # Test case 3: Disgust
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.01, 'disgust': 0.95, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.02}}]
        }
        res_3 = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')

        # Test case 4: Sadness
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.95}}]
        }
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')

        # Test case 5: Fear
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.01, 'disgust': 0.01, 'fear': 0.95, 'joy': 0.01, 'sadness': 0.02}}]
        }
        res_5 = emotion_detector("I am really afraid this will happen")
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
    