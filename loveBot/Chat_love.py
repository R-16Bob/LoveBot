import random

d_love={0:('你上辈子一定是碳酸饮料吧','不然为什么我一看到你就能开心的冒泡'),
    1:('你知道你和星星有什么区别吗?','星星在天上，你在我心里'),
    2:('先生你要点什么?','我想点开你的心'),
    3:('你累不累啊?','可是你都在我脑里跑了一天了'),
    4:('你知道我的缺点是什么吗','是缺点你'),
    5:('我背你好吗?','因为你是我一辈子的人'),
    6:('你知道你和猴子的区别是什么吗? ','猴子住在树上，你住在我心里'),
    7:('有件事我怕我说漏了嘴',' 我爱你这件事。'),
    8:('你知道为什么我不上天吗','因为地上有你啊'),
    9:('为什么我那么笨','因为就长了这么点脑子都用来想你了。'),
    10:('我要早点睡觉了','明天还要继续喜欢你呢。'),
    11:('最近开始冷了','需要躲进你怀里的那种。')
    }

def get_love():
    index = random.randint(0,11)
    return d_love[index]