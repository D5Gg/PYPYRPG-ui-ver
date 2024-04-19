import monster
import string
import random

종족_리스트 = ['고블린', '오크', '스켈레톤', '좀비', '야수', '벌레', '기계', '무형', '정령', '악마', '천사', '식물']

def randomName(LEN):
    string_pool = string.ascii_letters
    result = 'MC:'
    
    for i in range(LEN):
        result += random.choice(string_pool)
    
    return result
    
def statGen(first, upNum, rePercent, limit = -1):
    result = random.random * first + random.random * first
    
    while True:
        if random.random() * 100 <= rePercent:
            result += random.random() * upNum
        else:
            break
    
    if limit == -1:
        return int(result)
    
    if result > limit:
        result = limit
    
    return int(result)


class Level:
    def __init__(self, 이름, 차원, 행동:list, 연결:list, 몬스터:list, 몬스터조우수:list, 상점:list):
        self.이름 = 이름
        self.차원 = 차원
        self.행동 = 행동
        self.연결 = 연결
        self.몬스터 = 몬스터
        self.상점 = 상점
        self.몬스터조우수 = 몬스터조우수
        
level_list = {
    '시작의 장소':Level('시작의 장소', 1, ['이동', '휴식'], ['초원1'], [], [], []),
    '초원1':Level('초원1', 1, ['이동', '탐색'], ['시작의 장소', '서울'], ['그린 고블린', '레드 고블린'], [1], []),
    '서울':Level('서울', 1, ['휴식', '상점', '이동', '도박장'], ['초원1', '숲1'], [], [], ['재래시장']),
    '숲1':Level('숲1', 1, ['상점', '이동', '탐색'], ['서울', '숲2'], ['뱀', '그린 고블린', '레드 고블린'], [1], ['숲의 여인']),
    '숲2':Level('숲2', 1, ['탐색', '이동'], ['숲1', '늪지대1'], ['그린 고블린', '레드 고블린', '뱀', '독사'], [1, 1, 1, 2, 2], []),
    '늪지대1':Level('늪지대1', 1, ['이동', '탐색', '상점'], ['숲2', '공동묘지'], ['일반 좀비', '뱀', '독사'], [1, 1, 1, 2], ['늪지 상점']),
    '공동묘지':Level('공동묘지', 2, ['이동', '탐색'], ['늪지대1', '숲2', '과수원'], ['일반 좀비', '화이트 스켈레톤'], [1, 1, 1, 2, 3], []),
    '과수원':Level('과수원', 1, ['이동', '탐색', '상점'], ['공동묘지', '서울'], ['뱀', '독사', '사자', '화이트 스켈레톤'], [1, 1, 1, 2, 2, 2, 3], ['과수원 여인']),
}

# 배율, (판매물품들)
shop_list = {
    '재래시장':(1, ('단검', '사과')),
    '숲의 여인':(1, ('의식용 단검', '사과', '바나나', '랜턴')),
    '늪지 상점':(1.5, ('마법부여:죽음의 고통', '롱소드', '천두건', '천갑옷', '천바지', '천신발')),
    '과수원 여인':(1.8, ('가죽 자켓', '랜턴', '구두', '사과'))
}
        
        