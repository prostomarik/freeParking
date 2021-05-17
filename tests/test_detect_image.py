import pytest
from simple_car_detectiong.detector import detect_img


@pytest.mark.skip(reason="no data")
def test_detect_img():
    assert "car" in [x['name'] for x in detect_img("picture5.jpg")]
