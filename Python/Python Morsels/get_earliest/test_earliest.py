import unittest


from earliest import get_earliest


class GetEarliestTests(unittest.TestCase):

    """Tests for get_earliest."""

    def test_same_month_and_day(self):
        newer = "01/27/1832"
        older = "01/27/1756"
        self.assertEqual(get_earliest(newer, older), older)

    def test_february_29th(self):
        newer = "02/29/1972"
        older = "12/21/1946"
        self.assertEqual(get_earliest(newer, older), older)

    def test_smaller_month_bigger_day(self):
        newer = "03/21/1946"
        older = "02/24/1946"
        self.assertEqual(get_earliest(older, newer), older)

    def test_same_month_and_year(self):
        newer = "06/24/1958"
        older = "06/21/1958"
        self.assertEqual(get_earliest(older, newer), older)

    def test_invalid_date_allowed(self):
        newer = "02/29/2006"
        older = "02/28/2006"
        self.assertEqual(get_earliest(older, newer), older)

    def test_two_invalid_dates(self):
        newer = "02/30/2006"
        older = "02/29/2006"
        self.assertEqual(get_earliest(newer, older), older)

    def test_two_invalid_dates_v2(self):
        newer = "01/32/2007"
        older = "02/29/2006"
        self.assertEqual(get_earliest(newer, older), older)     

if __name__ == "__main__":
    unittest.main()