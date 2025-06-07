import unittest
from app import calculate_compound_interest  # Импортируем функцию из app.py

class TestCompoundInterestCalculator(unittest.TestCase):

    def test_positive_values(self):
        """Тест с положительными значениями."""
        principal = 1000
        rate = 5
        time = 10
        n = 1
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 1628.89, places=2)  # Используем assertAlmostEqual для float
        self.assertAlmostEqual(interest, 628.89, places=2)

    def test_different_compounding_periods(self):
        """Тест с разными периодами начисления процентов."""
        principal = 1000
        rate = 5
        time = 10
        n = 4  # Ежеквартально
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 1643.62, places=2)
        self.assertAlmostEqual(interest, 643.62, places=2)

        n = 12  # Ежемесячно
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 1647.01, places=2)
        self.assertAlmostEqual(interest, 647.01, places=2)

    def test_zero_rate(self):
        """Тест с нулевой процентной ставкой."""
        principal = 1000
        rate = 0
        time = 10
        n = 1
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 1000.00, places=2)
        self.assertAlmostEqual(interest, 0.00, places=2)

    def test_short_time_period(self):
        """Тест с коротким периодом времени."""
        principal = 1000
        rate = 5
        time = 1
        n = 1
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 1050.00, places=2)
        self.assertAlmostEqual(interest, 50.00, places=2)

    def test_large_time_period(self):
        """Тест с большим периодом времени."""
        principal = 1000
        rate = 5
        time = 50
        n = 1
        amount, interest = calculate_compound_interest(principal, rate, time, n)
        self.assertAlmostEqual(amount, 11467.40, places=2)
        self.assertAlmostEqual(interest, 10467.40, places=2)

if __name__ == '__main__':
    unittest.main()