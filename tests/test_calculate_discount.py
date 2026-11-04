from main import calculate_discount
def test_calculate_discount():
    assert calculate_discount(100, 0.2)== 80.0
    assert calculate_discount(50, 0)== 50.0
    assert calculate_discount(200, 1) ==0.0
    assert calculate_discount(100, -0.1)==ValueError
    assert calculate_discount(100, 1.5)==ValueError