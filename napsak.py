
class Napsak:
    def __init__(self, weight_limit=15):
        self.items = []
        self.weight_limit = weight_limit
        self.total_weight = 0
        self.total_value = 0

    def __repr__(self):
        return 'total_weight: {}, total_value: {},items: {}'.format(self.total_weight, self.total_value, self.items)

    def put(self, item):
        self.items.append(item)
        self.total_weight += item.weight
        self.total_value += item.value


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return '<weight: {}, value: {}>'.format(self.weight, self.value)


def make_napsak_set(items):
    napsak = Napsak()
    for item in items:
        napsak.put(item)
    return napsak


def napsak_filter(napsaks):
    return [napsak for napsak in napsaks if napsak.total_weight <= napsak.weight_limit]


def pickup_items_with_all_combinations(*args):
    items_conbinations = []
    for i in range(2 ** len(args)):
        index = [x + 1 for x in range(i) if 2 ** x & i]
        lst = [args[i - 1] for i in index]
        items_conbinations.append(lst)
    return items_conbinations


def evaluate(napsaks):
    res = Napsak()
    for napsak in napsaks:
        res = napsak if napsak.total_value >= res.total_value else res
    return res


def main():
    a = Item(1, 2)
    b = Item(3, 8)
    c = Item(6, 10)
    d = Item(10, 30)
    napsaks = []
    combinations = pickup_items_with_all_combinations(a, b, c, d)
    print(combinations)
    for items in combinations:
        napsak = make_napsak_set(items)
        napsaks.append(napsak)
    napsaks = napsak_filter(napsaks)
    print(evaluate(napsaks))


if __name__ == '__main__':
    main()
