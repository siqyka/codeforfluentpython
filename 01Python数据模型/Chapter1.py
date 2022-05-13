import collections
from random import choice

Card = collections.namedtuple(
    'Card', ['rank', 'suit'])  # namedtuple可以构建一个简单类（只有属性，没有方法）


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')  # 生成扑克牌花色列表
    suits = "spades diamonds clubs hearts".split()  # 生成花色列表

    def __init__(self) -> None:
        '''初始化卡牌'''
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        '''获取卡牌数量'''
        return len(self._cards)

    def __getitem__(self, position):
        '''获取一张卡牌'''
        return self._cards[position]


deck = FrenchDeck()

print(len(deck))  # 52

print(deck[0])  # Card(rank='2', suit='spades')

print(deck[-1])  # Card(rank='A', suit='hearts')

print(choice(deck))  # 随机一张牌

print(deck[:3])
# [Card(rank='2', suit='spades'), Card(rank='2', suit='diamonds'), Card(rank='2', suit='clubs')]

print(deck[12::13])
# [Card(rank='5', suit='spades'), Card(rank='8', suit='diamonds'), Card(rank='J', suit='clubs'), Card(rank='A', suit='hearts')]

for card in deck:
    print(card)
# Card(rank='2', suit='spades')
# Card(rank='2', suit='diamonds')
# ...

print(Card('Q', 'hearts') in deck)  # True

print(Card('7', 'beaste') in deck)  # False


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    # 获取卡牌在ranks列表出现的位置，以获取大小
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 花色相当于影响因子，同一张数字的牌，加上影响因子后大小不同
    return rank_value * len(suit_values)+suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
