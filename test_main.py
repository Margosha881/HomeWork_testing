from main import *
from unittest import TestCase


class TestVizitRu(TestCase):

    def test_matching_cls_expected(self):
        result = search_visit_ru()
        self.assertIsInstance(result, list)


    def test_count_vizit_ru(self):
        res = search_visit_ru()
        self.assertEqual(len(res),6)


    def test_search_vizit_ru(self):
        for vizits in search_visit_ru():
            for vizit,[sity,country] in vizits.items():
                self.assertIn('Россия', country)

        
class TestUniqId(TestCase):

    def test_matching_cls_expected(self):
        result = search_uniq_id()
        self.assertIsInstance(result, list)


    def test_unique_elements(self):
        result = search_uniq_id()
        set_result = list(set(result))
        self.assertEqual(result,set_result)


class Test_search_max_sales_amount(TestCase):

    def test_amount(self):
        result = search_max_sales_amount()
        self.assertEqual(len(result),2)


