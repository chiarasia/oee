from core.oee_calculator import OEECalculator


def test_oee_result_contains_required_fields():
    calculator = OEECalculator()

    result = calculator.calculate()

    assert "availability" in result
    assert "performance" in result
    assert "quality" in result
    assert "oee" in result


def test_oee_is_valid_percentage():
    calculator = OEECalculator()

    result = calculator.calculate()

    assert 0 <= result["oee"] <= 100
