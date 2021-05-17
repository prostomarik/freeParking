from simple_car_detectiong.detector import detect_img


def test_detect_img():
    assert "car" in [x['name'] for x in detect_img("picture5.jpg")]