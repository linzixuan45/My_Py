from enum import Enum ,unique
import random


#检查枚举的重复值
@unique
class Suite(Enum):
    #花色
    Spade,Heart,Club,Diamond = range(4)

    def __lt__(self,other):
        return self.value < other.value

class Card():
    #牌
    def __init__(self,suite,face):
        self.suite = suite
        self.face = face

    def show(self):
        #显示牌面
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']

        # 以 f开头表示在字符串内支持大括号内的python 表达式
        return f'{suites[self.suite.value]}{faces[self.face]}'
        # ♠︎6

    def __repr__(self):
        return self.show()

class Poker():
    '''puke'''

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)  #self.cards 保存了4个花色，13个数字,即  4 X 13  52张卡牌
                     for suite in Suite
                     for face in range(1, 14)]



    def shuffle(self):

        random.shuffle(self.cards)  #方法将序列的所有元素随机排序。洗牌，打乱顺序
        #此时 cards列表在原本的列表上完全打乱，
        self.index = 0

    def deal(self):
        '''发牌'''

        card = self.cards[self.index]
        '''[♣︎6, ♥︎J, ♥︎7, ♥︎A, ♥︎3, ♥︎6, ♥︎10, ♦︎9, ♥︎5, ♣︎4, ♠︎A, ♠︎7, ♦︎J, ♦︎2, ♣︎K
        , ♣︎J, ♠︎2, ♣︎10, ♠︎8, ♦︎7, ♦︎A, ♣︎3, ♥︎K, ♠︎Q, ♦︎6, ♠︎10, ♦︎3, ♦︎8, ♣︎A,
         ♥︎9, ♣︎9, ♦︎Q, ♥︎8, ♦︎5, ♠︎9, ♠︎3, ♦︎K, ♥︎4, ♦︎10, ♣︎Q, ♠︎5, ♣︎8, ♥︎2, ♣︎2,
          ♠︎K, ♣︎7, ♥︎Q, ♦︎4, ♠︎6, ♠︎4, ♣︎5, ♠︎J]'''
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)

class Player():
    def __init__(self,name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def sort(self,comp = lambda card: (card.suite ,card.face)):
        print(type(cards))
        self.cards.sort(key = comp)


def main():
    poker = Poker() #4x13
    poker.shuffle() #打乱顺序
    players = [Player('黄政'),Player(' 蒋林轩'),Player('蒋明成'),Player(' 迪迦')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal()) #每次每个人发一张牌
    for player in players:
        player.sort() #将牌排序
        print(player.name, end=':')
        print(player.cards)

if __name__ =='__main__':
    main()

