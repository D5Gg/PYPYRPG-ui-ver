import pickle


class Hobby:
    값 = '울기'
    
class Cat:
    이름 = '애옹이'
    나이 = 5
    취미 = Hobby()
    
    
cat = Cat()
cat2 = Cat()
cat_list = [[2853, cat], [cat2, 2358]]
cat_l = None

def save():
    with open("cat.pickle", 'wb') as file:
        pickle.dump(cat_list, file)
        
def load():
    with open("cat.pickle", 'rb') as file:
        cat_l = pickle.load(file)
        print(cat_l[0], cat_l[1])
        
save()
load()