
"""
Unit testing calc app
"""

import cal


class TestCalculatorApp:

    def test_add(self):
        assert 5 == cal.add(1, 4)

    def test_subtract(self):
        assert 2 == cal.subtract(5, 3)
