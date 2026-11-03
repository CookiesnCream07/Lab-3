import price_info


def test_cost_of_fruits():
    # 5 apples at $1.20 each = $6.00
    result = price_info.cost_of_fruits('apple', 5)
    assert result == 6.00


def test_total_cost_shopping():
    # Sum of all fruit items = 46.60
    result = price_info.total_cost_shopping()
    assert round(result, 2) == 46.60