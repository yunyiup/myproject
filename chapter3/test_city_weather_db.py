import unittest
from chapter3.city_weather_db import HefengDb
from chapter3.city_weather import HeFeng


class TestCityWeatherDbCase(unittest.TestCase):
    def test_save(self):
        hefengdb = HefengDb()
        hefengdb.save({"name": "yingkonglai", "class": "net19049"})
        hefengdb.show_all()
        results = hefengdb.find({"name": "yingkonglai"})
        for each in results:
            self.assertEqual("yingkonglai", each['name'])
            self.assertEqual("net19049", each['class'])
        hefengdb.delete()

    def test_save_all(self):
        hefeng = HeFeng()
        # codes=hefeng.get_city_code()
        # for each in codes:
        #     print(next(codes))
        weathers=hefeng.get_all_weather(7)

        # each = hefeng.get_weather("CN101010200")
        # print(each)
        hefengdb = HefengDb()
        hefengdb.save_all(weathers)
        print("show_all")
        hefengdb.show_all()
        self.assertEqual(7,hefengdb.count())
        hefengdb.delete()


if __name__ == '__main__':
    unittest.main()
