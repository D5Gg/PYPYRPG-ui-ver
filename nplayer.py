
import map
import random

종족_리스트 = ['고블린', '오크', '스켈레톤', '좀비', '야수', '벌레', '기계', '무형', '정령', '악마', '천사', '식물']

레벨당_경험치 = {}

경험치당_레벨 = {}

레벨당_경험치[1] = 0

최고레벨 = 500

for i in range(최고레벨 - 1):
    if i <= 18:
        레벨당_경험치[i+2] = 20 * (i + 1)
    elif i <= 48:
        레벨당_경험치[i+2] = 50 * (i + 1)
    elif i <= 98:
        레벨당_경험치[i+2] = 110 * (i + 1)
    elif i <= 198:
        레벨당_경험치[i+2] = 400 * (i + 1)
    elif i <= 298:
        레벨당_경험치[i+2] = 800 * (i + 1)
    elif i <= 398:
        레벨당_경험치[i+2] = 1200 * (i + 1)
    elif i <= 498:
        레벨당_경험치[i+2] = 2000 * (i + 1)

for level, exp in list(레벨당_경험치.items()):
    경험치당_레벨[exp] = level

class Player:
    직업:str = '무직'
    레벨:int = 1
    경험치:int = 0
    골드:int = 10
    
    ### 전투변수
    중독:int = 0
    #=======================
    
    인벤토리아이템개수:int = 0
    차원판매스크롤:bool = True
    
    맵:map.Level = map.level_list['시작의 장소']
    레벨업포인트:int = 0
    
    체력:int = 100
    최대체력:int = 체력
    마력:int = 0
    최대마력:int = 마력
    공격력:int = 10
    
    힘:int = 10
    민첩:int = 10
    지능:int = 10
    운:int = 10
    스피드:int = 10
    
    회피율:float = 0.0
    방어력:int = 0
    물리저항:float = 0.0
    화염저항:float = 0.0
    냉기저항:float = 0.0
    독저항:float = 0.0
    전기저항:float = 0.0
    암흑저항:float = 0.0
    신성저항:float = 0.0
    
    추가피해_고블린:float = 0.0
    추가피해_오크:float = 0.0
    추가피해_스켈레톤:float = 0.0
    추가피해_좀비:float = 0.0
    추가피해_야수:float = 0.0
    추가피해_벌레:float = 0.0
    추가피해_기계:float = 0.0
    추가피해_무형:float = 0.0
    추가피해_정령:float = 0.0
    추가피해_악마:float = 0.0
    추가피해_천사:float = 0.0
    추가피해_식물:float = 0.0
    
    고유_최대체력:int = 100
    고유_최대마력:int = 0
    고유_공격력:int = 10
    
    고유_힘:int = 10
    고유_민첩:int = 10
    고유_지능:int = 10
    고유_운:int = 10
    고유_스피드:int = 10
    
    고유_회피율:float = 0.0
    고유_방어력:int = 0
    고유_물리저항:float = 0.0
    고유_화염저항:float = 0.0
    고유_냉기저항:float = 0.0
    고유_독저항:float = 0.0
    고유_전기저항:float = 0.0
    고유_암흑저항:float = 0.0
    고유_신성저항:float = 0.0
    
    고유_추가피해_고블린:float = 0.0
    고유_추가피해_오크:float = 0.0
    고유_추가피해_스켈레톤:float = 0.0
    고유_추가피해_좀비:float = 0.0
    고유_추가피해_야수:float = 0.0
    고유_추가피해_벌레:float = 0.0
    고유_추가피해_기계:float = 0.0
    고유_추가피해_무형:float = 0.0
    고유_추가피해_정령:float = 0.0
    고유_추가피해_악마:float = 0.0
    고유_추가피해_천사:float = 0.0
    고유_추가피해_식물:float = 0.0
    
    스탯증가_합_최대체력:int = 0
    스탯증가_곱_최대체력:int = 0
    스탯증가_합_최대마력:int = 0
    스탯증가_곱_최대마력:int = 0
    스탯증가_합_공격력:int = 0
    스탯증가_곱_공격력:int = 0
    
    스탯증가_합_힘:int = 0
    스탯증가_곱_힘:int = 0
    스탯증가_합_민첩:int = 0
    스탯증가_곱_민첩:int = 0
    스탯증가_합_지능:int = 0
    스탯증가_곱_지능:int = 0
    스탯증가_합_운:int = 0
    스탯증가_곱_운:int = 0
    스탯증가_합_스피드:int = 0
    스탯증가_곱_스피드:int = 0
    
    스탯증가_합_회피율:float = 0.0
    스탯증가_합_방어력:int = 0 
    스탯증가_곱_방어력:int = 0
    
    스탯증가_합_물리저항:float = 0.0
    스탯증가_합_화염저항:float = 0.0
    스탯증가_합_냉기저항:float = 0.0
    스탯증가_합_독저항:float = 0.0
    스탯증가_합_전기저항:float = 0.0
    스탯증가_합_암흑저항:float = 0.0
    스탯증가_합_신성저항:float = 0.0
    
    인벤토리:list[list] = []
    스킬들:list = ['도망', '주먹질']
    
    장비칸_머리 = '-'
    장비칸_상의 = '-'
    장비칸_하의 = '-'
    장비칸_신발 = '-'
    장비칸_무기 = '-'
    장비칸_보조장비 = '-'
    
    고유_추가피해_고블린:float = 0.0
    고유_추가피해_오크:float = 0.0
    고유_추가피해_스켈레톤:float = 0.0
    고유_추가피해_좀비:float = 0.0
    고유_추가피해_야수:float = 0.0
    고유_추가피해_벌레:float = 0.0
    고유_추가피해_기계:float = 0.0
    고유_추가피해_무형:float = 0.0
    고유_추가피해_정령:float = 0.0
    고유_추가피해_악마:float = 0.0
    고유_추가피해_천사:float = 0.0
    고유_추가피해_식물:float = 0.0
    
    추가피해_합_고블린:float = 0.0
    추가피해_합_오크:float = 0.0
    추가피해_합_스켈레톤:float = 0.0
    추가피해_합_좀비:float = 0.0
    추가피해_합_야수:float = 0.0
    추가피해_합_벌레:float = 0.0
    추가피해_합_기계:float = 0.0
    추가피해_합_무형:float = 0.0
    추가피해_합_정령:float = 0.0
    추가피해_합_악마:float = 0.0
    추가피해_합_천사:float = 0.0
    추가피해_합_식물:float = 0.0
    
    
    def __init__(self, 이름:str):
        self.이름:str = 이름
        
    def 레벨체크(self):
        원래레벨 = self.레벨
        if 레벨당_경험치[500] <= self.경험치:
            self.레벨 = 500
            return (self.레벨 - 원래레벨)
        for i in list(레벨당_경험치.values()):
            if self.경험치 < i:
                self.레벨 = 경험치당_레벨[i] - 1
                break
        if self.레벨 - 원래레벨 > 0:
            return (self.레벨 - 원래레벨)
        else:
            return 0
        
        
    def 스탯새로고침(self):
        self.레벨업포인트 += self.레벨체크()
        self.최대체력 = int((self.고유_최대체력 + self.스탯증가_합_최대체력) * (100 + self.스탯증가_곱_최대체력) / 100)
        if self.최대체력 < self.체력:
            self.체력 = self.최대체력
        self.최대마력 = int((self.고유_최대마력 + self.스탯증가_합_최대마력) * (100 + self.스탯증가_곱_최대마력) / 100)
        if self.최대마력 < self.마력:
            self.마력 = self.최대마력
        self.공격력 = int((self.고유_공격력 + self.스탯증가_합_공격력) * (100 + self.스탯증가_곱_공격력) / 100)
        self.힘 = int((self.고유_힘 + self.스탯증가_합_힘) * (100 + self.스탯증가_곱_힘) / 100)
        self.민첩 = int((self.고유_민첩 + self.스탯증가_합_민첩) * (100 + self.스탯증가_곱_민첩) / 100)
        self.지능 = int((self.고유_지능 + self.스탯증가_합_지능) * (100 + self.스탯증가_곱_지능) / 100)
        self.운 = int((self.고유_운 + self.스탯증가_합_운) * (100 + self.스탯증가_곱_운) / 100)
        self.스피드 = int((self.고유_스피드 + self.스탯증가_합_스피드) * (100 + self.스탯증가_곱_스피드) / 100)
        self.회피율 = self.고유_회피율 + self.스탯증가_합_회피율
        self.방어력 = int((self.고유_방어력 + self.스탯증가_합_방어력) * (100 + self.스탯증가_곱_방어력) / 100)
        self.물리저항 = self.고유_물리저항 + self.스탯증가_합_물리저항
        self.화염저항 = self.고유_화염저항 + self.스탯증가_합_화염저항
        self.냉기저항 = self.고유_냉기저항 + self.스탯증가_합_냉기저항
        self.독저항 = self.고유_독저항 + self.스탯증가_합_독저항
        self.전기저항 = self.고유_전기저항 + self.스탯증가_합_전기저항
        self.암흑저항 = self.고유_암흑저항 + self.스탯증가_합_암흑저항
        self.신성저항 = self.고유_신성저항 + self.스탯증가_합_신성저항
        self.추가피해_고블린 = self.고유_추가피해_고블린 + self.추가피해_합_고블린
        self.추가피해_오크 = self.고유_추가피해_오크 + self.추가피해_합_오크
        self.추가피해_스켈레톤 = self.고유_추가피해_스켈레톤 + self.추가피해_합_스켈레톤
        self.추가피해_좀비 = self.고유_추가피해_좀비 + self.추가피해_합_좀비
        self.추가피해_야수 = self.고유_추가피해_야수 + self.추가피해_합_야수
        self.추가피해_벌레 = self.고유_추가피해_벌레 + self.추가피해_합_벌레
        self.추가피해_기계 = self.고유_추가피해_기계 + self.추가피해_합_기계
        self.추가피해_무형 = self.고유_추가피해_무형 + self.추가피해_합_무형
        self.추가피해_정령 = self.고유_추가피해_정령 + self.추가피해_합_정령
        self.추가피해_악마 = self.고유_추가피해_악마 + self.추가피해_합_악마
        self.추가피해_천사 = self.고유_추가피해_천사 + self.추가피해_합_천사
        self.추가피해_식물 = self.고유_추가피해_식물 + self.추가피해_합_식물
        
        if self.회피율 > 50:
            self.회피율 = 50
        if self.물리저항 > 80:
            self.물리저항 = 80
        if self.화염저항 > 80:
            self.화염저항 = 80
        if self.냉기저항 > 80:
            self.냉기저항 = 80
        if self.독저항 > 80:
            self.독저항 = 80
        if self.전기저항 > 80:
            self.전기저항 = 80
        if self.암흑저항 > 80:
            self.암흑저항 = 80
        if self.신성저항 > 80:
            self.신성저항 = 80
            
        print('스탯 새로고침 (완)')
    
    def 죽음판정(self):
        if self.체력 <= 0:
            return True
        else:
            return False

    def 피해받음(self, 피해량):
        self.체력 -= 피해량
        
    def 회복(self, 회복량):
        self.체력 += 회복량
        if self.체력 > self.최대체력:
            self.체력 = self.최대체력
    
    def 마력회복(self, 회복량):
        self.마력 += 회복량
        if self.마력 > self.최대마력:
            self.마력 = self.최대마력

def 아이템생성위치(player):
    while True:
        index = random.randint(1, 90000000)
        for i in player.인벤토리:
            if index == i.iid:
                continue
        return index