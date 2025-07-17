import unittest
from payment_processor import PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_valid_amount(self):
        result = self.processor.process_payment(1000)
        self.assertEqual(result, 1020.00)

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(0)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(-58)

    def test_exceed_limit(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(10000)

    def test_fee_rounding(self):
        result = self.processor.process_payment(145.34)
        expected = round(145.34 * 1.02, 2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
