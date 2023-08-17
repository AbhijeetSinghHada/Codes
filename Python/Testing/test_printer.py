from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    # @classmethod  # single for all tests
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(3000)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = 'Printed 10 pages in 5.00 seconds.'

        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimal(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = 'Printed 11 pages in 3.67 seconds.'

        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_run_multiple_jobs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_run_multiple_jobs_error(self):
        self.printer.print(25)
        self.printer.print(50)
        with self.assertRaises(PrinterError):
            self.printer.print(226)
