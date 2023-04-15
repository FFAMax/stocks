import unittest
from datetime import datetime
from convert_date_format import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date_formats(self):
        # список кортежей в формате (date_string, expected_date), содержащих даты в разных форматах и ожидаемые результаты
        date_strings = [
            ('2022-01-01', '2022-01-01'),
            ('2022/01/01', '2022-01-01'),
            ('2022.01.01', '2022-01-01'),
            ('01.02.2022', '2022-02-01'),
            ('01-22-2022', '2022-01-22'),
            ('01/22/2022', '2022-01-22'),
            ('01 January 2022', '2022-01-01'),
            ('01 Jan 2022', '2022-01-01'),
            ('2022-01-01 12:30:00', '2022-01-01'),
            ('2022-01-01 12:30', '2022-01-01'),
            ('2022-01-01 12:30:00 PM', '2022-01-01'),
            ('2022-01-01 12:30 PM', '2022-01-01'),
            ('1640995200', '2022-01-01'),
            ('2022-01-01 12:30:00 UTC', '2022-01-01'),
            ('2022-01-01 12:30 UTC', '2022-01-01'),
        ]
        
        for date_string, expected_date in date_strings:
            with self.subTest(date_string=date_string):
                self.assertEqual(convert_date_format(date_string), expected_date)
    
    def test_invalid_date_formats(self):
        # список строк, содержащих даты в неверном формате
        invalid_date_strings = [
            '2022.01-01',  # неверный разделитель
            '2022/13/01',  # неверный месяц
            '32/01/2022',  # неверный день
            '2022-01-01 12:30:00 ET', # неверный часовой пояс
            '2022-01-01 13:30:00 PM', # неверное время
        ]
        
        for date_string in invalid_date_strings:
            with self.subTest(date_string=date_string):
                with self.assertRaises(ValueError):
                    convert_date_format(date_string)

if __name__ == '__main__':
    unittest.main()

