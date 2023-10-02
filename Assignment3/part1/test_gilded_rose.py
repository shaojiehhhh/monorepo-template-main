import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_quality_degradation(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_normal_item_sell_in_degradation(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_normal_item_quality_degradation_after_sell_in_date(self):
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_normal_item_quality_does_not_go_below_zero(self):
        items = [Item("Normal Item", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    # Add similar test cases for "Aged Brie" as needed.

    def test_backstage_pass_quality_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    # Add similar test cases for "Backstage passes" as needed.

    def test_conjured_item_quality_degradation(self):
        items = [Item("Conjured", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    # Add similar test cases for "Conjured" items as needed.

    def test_sulfuras_quality_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    # Add similar test cases for other edge cases as needed.

if __name__ == '__main__':
    unittest.main()
