import data
import receiving
# Егупов Антон, 10-я когорта - Финальный проект. Инженер по тестированию плюс
def create_order():
    current_body = data.order_content.copy()
    current_body ["firstName"] = "Toni"
    track_num = receiving.post_new_order(current_body)
    return str(track_num.json()["track"])
def positive_assert():
    track_num = create_order()
    current_params = data.params_get.copy()
    current_params["t"] = track_num
    response = receiving.get_order(current_params)
    assert response.status_code == 200

def test_order():
    positive_assert()