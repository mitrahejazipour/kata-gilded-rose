class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"Item(name={self.name} sell_in={self.sell_in}, quality={self.quality})"

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


list_names = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert",
              "Sulfuras, Hand of Ragnaros"]


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    # /!\ Do not change code above this line /!\ #

    def update_quality(self):
        for item in self.items:
            if item.name not in list_names and item.quality > 0:
                item.quality = item.quality - 1

            if item.name in list_names and item.quality < 50:
                item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            
            if item.sell_in < 0:
                if item.name not in list_names and item.quality > 0:
                    item.quality = item.quality - 1
                if item.name in ["Backstage passes to a TAFKAL80ETC concert"]:
                    item.quality = item.quality - item.quality
                
                if item.name == "Aged Brie" and item.quality < 50:
                    item.quality = item.quality + 1


if __name__ == "__main__":
    main()
