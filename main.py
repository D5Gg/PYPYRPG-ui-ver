#-*- coding: utf-8 -*-

from os.path import exists
from os import makedirs
import sys
import pickle
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import map
import monster
import random
import skill
import nitem
import nplayer


def reset(mes):
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(mes, loop.quit)
    loop.exec_()


global mainWindow

출력초 = 1

main_text = ''

global player

global 몬스터들

global lastSelected

global id



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
login_form_class = uic.loadUiType("./ui/login.ui")[0]
main_form_class = uic.loadUiType("./ui/main.ui")[0]
input_name_form_class = uic.loadUiType("./ui/input_name.ui")[0]

player_statList = ['레벨', '경험치', '골드', '최대체력', '체력', '최대마력', '마력', '공격력', '힘', '민첩', '지능', '운', '스피드', '회피율', '방어력',
                    '물리저항', '화염저항', '냉기저항', '독저항', '전기저항', '암흑저항', '신성저항',
                    '추가피해_고블린',
                    '추가피해_오크',
                    '추가피해_스켈레톤',
                    '추가피해_좀비',
                    '추가피해_야수',
                    '추가피해_벌레',
                    '추가피해_기계',
                    '추가피해_무형',
                    '추가피해_정령',
                    '추가피해_악마',
                    '추가피해_천사',
                    '추가피해_식물']

player_equipList = ['머리', '상의', '하의', '신발', '무기', '보조장비']

player_stat = []
player_item = []
player_equip = []

def 저장(id):
    global player
    with open('./유저데이터/{}.pickle'.format(id), 'wb') as file:
        pickle.dump(player, file)
        pickle.dump(player.인벤토리, file)
        pickle.dump(player.스킬들, file)
        # pickle.dump(player.인벤토리, file)
        # pickle.dump(player.장비칸_머리, file)
        # pickle.dump(player.장비칸_상의, file)
        # pickle.dump(player.장비칸_하의, file)
        # pickle.dump(player.장비칸_신발, file)
        # pickle.dump(player.장비칸_무기, file)
        # pickle.dump(player.장비칸_보조장비, file)
        # pickle.dump(player.장비칸, file)
        # pickle.dump(player.스킬들, file)
        # pickle.dump(player.맵, file)
        
    print(player)
    print('저장됨')
    file.close()
    
        
def 불러오기(id):
    global player
    with open('./유저데이터/{}.pickle'.format(id), 'rb') as file:
        player = pickle.load(file)
        player.인벤토리 = pickle.load(file)
        player.스킬들 = pickle.load(file)
        # player.인벤토리 = pickle.load(file)
        # player.장비칸_머리 = pickle.load(file)
        # player.장비칸_상의 = pickle.load(file)
        # player.장비칸_하의 = pickle.load(file)
        # player.장비칸_신발 = pickle.load(file)
        # player.장비칸_무기 = pickle.load(file)
        # player.장비칸_보조장비 = pickle.load(file)
        # player.장비칸 = pickle.load(file)
        # player.스킬들 = pickle.load(file)
        # player.맵 = pickle.load(file)
    for i in player.인벤토리:
        if i.종류 == '장비':
            print(i.장착됨)
    
    print(player.장비칸_머리)
    print(player.장비칸_상의)
    print(player.장비칸_하의)
    print(player.장비칸_신발)
    print(player.장비칸_무기)
    print(player.장비칸_보조장비)
    
    file.close()
    
    
def MakeBtn(text:str, parent:QWidget):
    btn = QPushButton(parent)
    btn.setText(text)
    
# class statTableModel(QAbstractTableModel):
#     def __init__(self, data, headers, parent=None):
#         super().__init__(parent)
#         self._data = data
#         self._headers = headers

#     def RowCount(self, parent):
#         return len(self._data)

#     def columnCount(self, parent):
#         return len(self._data[0])

#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             return self._data[index.row()][index.column()]

#         return QVariant()

#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return self._headers[section]

#         return QVariant()
        
#화면을 띄우는데 사용되는 Class 선언
class LoginClass(QMainWindow, login_form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        
    
        self.Btn_new.clicked.connect(self.Start)
        self.Btn_fin.clicked.connect(self.FinGame)
        
    def 경고(self):
        QMessageBox.warning(self, '경고', '아이디가 비었습니다.')
        
    def Start(self):
        global id
        global mainWindow
        
        if self.input_id.text() == '':
            self.경고()
        else:
            id = self.input_id.text()
            
            
            if not exists('./유저데이터'):
                makedirs('./유저데이터')
                
            # 유저데이터 폴더에 이름이 플레이어 아이디인 pickle 이 없으면 생성.
            if not exists('./유저데이터/{}.pickle'.format(id)):
                
                nameWindow.show()
            
             # 있다면 불러오기.
            else:
                
                불러오기(id)
                reset(200)
                
                mainWindow.show()
            
                mainWindow.game_Start()
                
                loginWindow.hide()
                
                
    
    def FinGame(self):
        app.quit()
    



    
    
class NameClass(QMainWindow, input_name_form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hide()
        
        self.Btn_c.clicked.connect(self.GeneratePlayer)
    
    def 경고(self):
        QMessageBox.warning(self, '경고', '이름이 비었습니다.')
        
    def GeneratePlayer(self):
        global player
        global mainWindow
        
        if self.input_name.text() != '':
            
            player = nplayer.Player(self.input_name.text())
            
            mainWindow.show()
            
            mainWindow.game_Start()
            
            
            nameWindow.hide()
            
            loginWindow.hide()
            
        else:
            self.경고()
            
    
class MainClass(QMainWindow, main_form_class) :
    
    입력키 = ''
    selection_model = None
    rowrow = 0
    colcol = 0
    
    
    def __init__(self) :
        global lastSelected
        super().__init__()
        self.setupUi(self)
        self.hide()
        self.selected_indexes = []
        # 항목 선택 모델 가져오기

        # selectionChanged 신호와 연결
        
        self.Btn_save.clicked.connect(self.save)
        
        self.tabW_main.currentChanged.connect(self.seiChg)
        
        self.Btn_go.clicked.connect(self.itemAction)
        
        self.Btn_statpoint.clicked.connect(self.use_statpoint)
        
        self.Btn_cheat_item.clicked.connect(self.cheat_random_item)
        
    def game_Start(self):
        
        self.seiChg()
        
        self.currentMap_action()
        
        self.generate_Btn_for_map()
        
    def all_setDisabled(self):
        self.scrollArea.setDisabled(True)
        self.tabW_main.setDisabled(True)
        self.Btn_save.setDisabled(True)
        self.Btn_cheat_item.setDisabled(True)
        
    def all_setEnabled(self):
        self.scrollArea.setEnabled(True)
        self.tabW_main.setEnabled(True)
        self.Btn_save.setEnabled(True)
        self.Btn_cheat_item.setEnabled(True)
        
    def cheat_random_item(self):
        global player
        
        code, ok = QInputDialog.getText(self, '치트 코드', '[123123] 무작위 아이템 1개\n [124124] 무작위 아이템 3개\n [155155] 무작위 아이템 5개')
        
        if ok:
            if code == '123123': # 치트 사용 성공
                genitem = random.choice(nitem.item_list)
                player.인벤토리.append(nitem.item_generate(genitem, player))
                QMessageBox.about(self, '치트 성공', '개발용 입니다.')
            elif code == '124124': # 치트 사용 성공
                for _ in range(3):
                    genitem = random.choice(nitem.item_list)
                    player.인벤토리.append(nitem.item_generate(genitem, player))
                QMessageBox.about(self, '치트 성공', '개발용 입니다.')
            elif code == '155155': # 치트 사용 성공
                for _ in range(5):
                    genitem = random.choice(nitem.item_list)
                    player.인벤토리.append(nitem.item_generate(genitem, player))
                QMessageBox.about(self, '치트 성공', '개발용 입니다.')
            else:
                QMessageBox.about(self, '치트 실패', '잘못된 치트코드 입니다.')
                
            print(player.인벤토리)
            self.seiChg()
        
        
    def use_statpoint(self):
        global player
        
        stat, ok = QInputDialog.getText(self, '스탯 선택', '1. 최대체력 +10\n2. 최대마력 +10\n3. 힘 +3\n4. 민첩 +3\n5. 지능 +3\n6. 운 +3\n7. 공격력 +3')
        
        if ok:
            if stat == '1':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_최대체력 += ss * 10
                        QMessageBox.about(self, '완료', '최대체력 +{} 증가.'.format(ss * 10))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat == '2':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_최대마력 += ss * 10
                        QMessageBox.about(self, '완료', '최대마력 +{} 증가.'.format(ss * 10))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat =='3':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_힘 += ss * 3
                        QMessageBox.about(self, '완료', '힘 +{} 증가.'.format(ss * 3))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat =='4':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_민첩 += ss * 3
                        QMessageBox.about(self, '완료', '민첩 +{} 증가.'.format(ss * 3))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat =='5':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_지능 += ss * 103
                        QMessageBox.about(self, '완료', '지능 +{} 증가.'.format(ss * 3))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat =='6':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_운 += ss * 3
                        QMessageBox.about(self, '완료', '운 +{} 증가.'.format(ss * 3))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            elif stat =='7':
                try:
                    ss, okok = QInputDialog.getInt(self, '포인트 사용량', '몇 포인트 사용할까요?')
                    if okok and player.레벨업포인트 >= ss:
                        player.레벨업포인트 -= ss
                        player.스탯증가_합_공격력 += ss * 3
                        QMessageBox.about(self, '완료', '공격력 +{} 증가.'.format(ss * 3))
                    else:
                        QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
                except:
                    QMessageBox.about(self, '사용 실패', '사용에 실패했습니다.')
            else:
                QMessageBox.about(self, '잘못된 선택', '잘못된 선택입니다.')
        
    def get_index_from_itemCode(self, itcode):
        global player
        index = 0
        
        for i in player.인벤토리:
            if i.iid == itcode:
                return index
            index += 1
            
        return -1
    
    def item_ui(self):
        global player
        
        player_item.clear()
        
        self.TV_inven.setHorizontalHeaderLabels(['이름', '종류', '부위', '장착여부', 'id'])
        
        for i in player.인벤토리:
            if i.종류 == '장비':
                player_item.append([i.이름, i.종류, i.부위, i.장착됨, i.iid])
            else:
                player_item.append([i.이름, i.종류, '-', '-', i.iid])
        
        if player_item:
            self.TV_inven.setRowCount(len(player_item))
            self.TV_inven.setColumnCount(len(player_item[0]))
            
            row = self.TV_inven.rowCount()
            col = self.TV_inven.columnCount()
            
            
            for j in range(row):
                for k in range(col):
                    self.TV_inven.setItem(j, k, QTableWidgetItem(str(player_item[j][k])))
        
        
        self.TV_inven.itemClicked.connect(self.inven_selection_Chg)

        # # 데이터 모델 생성
        # model = QStandardItemModel(len(player.인벤토리), 5)
        # model.setHorizontalHeaderLabels(['이름', '종류', '부위', '장착여부', 'id'])
        
        # for row in range(len(player.인벤토리)):
        #     for column in range(5):
        #         if column == 0:
        #             item = QStandardItem(player.인벤토리[row].이름)
        #             model.setItem(row, column, item)
        #         elif column == 1:
        #             item = QStandardItem(player.인벤토리[row].종류)
        #             model.setItem(row, column, item)
        #         elif column == 2:
        #             if player.인벤토리[row].종류 == '장비':
        #                 item = QStandardItem(player.인벤토리[row].부위)
        #                 model.setItem(row, column, item)
        #             else:
        #                 model.setItem(row, column, QStandardItem(''))
        #         elif column == 3:
        #             if player.인벤토리[row].종류 == '장비':
        #                 item = QStandardItem('{}'.format(player.인벤토리[row].장착됨))
        #                 model.setItem(row, column, item)
        #             else:
        #                 model.setItem(row, column, QStandardItem(''))
        #         elif column == 4:
        #             item = QStandardItem('{}'.format(player.인벤토리[row].iid))
        #             model.setItem(row, column, item)

        # # 테이블 뷰 선택 모드 설정
        # self.TV_inven.setSelectionMode(QTableView.SingleSelection)
        # self.TV_inven.setSelectionBehavior(QTableView.SelectRows)
        
        # self.TV_inven.setModel(model)

        # # 테이블 뷰에서 선택이 변경될 때 신호 연결
        # self.TV_inven.selectionModel().selectionChanged.connect(self.inven_selection_Chg)

        # # 레이아웃 설정
        # layout = QVBoxLayout()
        # layout.addWidget(self.TV_inven)
        # self.setLayout(layout)

        # 데이터 추가
        
                    
    def inven_selection_Chg(self):
        global player
        global lastSelected
        
        self.si_action.clear()
        
        lastSelected = self.TV_inven.selectedItems()
        
        self.label_selected_item.setText(lastSelected[0].text())
        self.label_selected_item_id.setText(lastSelected[4].text())
        print(lastSelected)
        
        if lastSelected[1].text() == '장비':
            self.si_action.addItem('장착')
            self.si_action.addItem('해제')
            self.si_action.addItem('상세정보')
            self.si_action.addItem('버리기')
            self.si_action.addItem('마법부여')
            if player.차원판매스크롤 == True:
                self.si_action.addItem('판매')

        elif lastSelected[1].text() == '소비':
            self.si_action.addItem('사용')
            self.si_action.addItem('상세정보')
            self.si_action.addItem('버리기')
            if player.차원판매스크롤 == True:
                self.si_action.addItem('판매')
                
        elif lastSelected[1].text() == '주문서':
            self.si_action.addItem('상세정보')
            self.si_action.addItem('버리기')
            if player.차원판매스크롤 == True:
                self.si_action.addItem('판매')
                
    def get_selected_row_and_column(self, table_view):
        self.selection_model = table_view.selectionModel()
        if self.selection_model is not None and self.selection_model.hasSelection():
            selected_indexes = self.selection_model.selectedIndexes()
            first_index = selected_indexes[0]
            row = first_index.row()
            column = first_index.column()
            return row, column
        else:
            return None, None
        
    def get_selected_row_values(self, table_view):
        self.selected_indexes = table_view.selectionModel().selectedIndexes()
        model = table_view.model()
        selected_values = []
        for index in self.selected_indexes:
            row = index.row()
            column = index.column()
            item = model.item(row, column)
            selected_values.append(item.text())
        return selected_values
    
    def get_selected_column_index(self, tableView):
        self.selection_model = tableView.selectionModel()
        selected_indexes = self.selection_model.selectedIndexes()
        selected_columns = set(index.column() for index in selected_indexes)
        if len(selected_columns) == 1:
            return next(iter(selected_columns))
        else:
            return None
        
    def get_column_values(self, tableView, column_index):
        model = tableView.model()
        if not model:
            return None
        
        column_values = []
        for row in range(model.RowCount()):
            index = model.index(row, column_index)
            data = model.data(index)
            column_values.append(data)
    
        return column_values
    
    def itemAction(self):
        global lastSelected
        global player
        print(lastSelected)
        
        item = None
        
        clastSelected = self.TV_inven.selectedItems()
        
        if self.si_action.count():
        
            for i in player.인벤토리:
                if i.iid == int(clastSelected[4].text()):
                    item = i
            
            if clastSelected[1].text() == '장비':
                if self.si_action.currentText() == '장착':
                    장착결과 = item.장착(player)
                    if 장착결과:
                        QMessageBox.about(self, '아이템 장착.', '{} 을(를) 장착했습니다.'.format(item.이름))
                    else:
                        QMessageBox.about(self, '장착 실패', '{} 장착에 실패했습니다.'.format(item.이름))
                    self.seiChg()
                    
                    
                elif self.si_action.currentText() == '해제':
                    
                    해제결과 = item.장착해제(player)
                    if 해제결과:
                        QMessageBox.about(self, '아이템 장착해제.', '{} 을(를) 장착 해제했습니다.'.format(item.이름))
                    else:
                        QMessageBox.about(self, '해제 실패', '{} 해제에 실패했습니다.'.format(item.이름))
                    self.seiChg()
                    
                elif self.si_action.currentText() == '상세정보':
                    QMessageBox.about(self, '아이템 정보.', '아이템 이름: {}\n" {} "\n종류: {}  / 부위: {}\n<<<<< 상세정보 >>>>>\n{}\n{}\n============================================'.
                                    format(item.이름, item.설명, item.종류, item.부위, item.상세정보, item.마부_텍스트))
                    
                elif self.si_action.currentText() == '버리기':
                    button_Reply = QMessageBox.warning(self, '아이템 버리기.', '{} 을(를) 버리시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
                    
                    if button_Reply == QMessageBox.Yes:
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                    elif button_Reply == QMessageBox.No:
                        pass
                    else:
                        pass
                    
                elif self.si_action.currentText() == '판매':
                    button_Reply = QMessageBox.warning(self, '아이템 판매.', '{} 을(를) 판매 하시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
                    
                    if button_Reply == QMessageBox.Yes:
                        
                        판매골드 = item.판매가
                        
                        if item.장착됨 == True:
                            item.장착해제(player)
                        
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                        
                        player.골드 += 판매골드
                        
                        self.seiChg()
                        
                        QMessageBox.about(self, '아이템을 차원 상인에게 판매했습니다..@@', '{} G 를 획득했습니다. $$$'.format(판매골드))
                        
                    elif button_Reply == QMessageBox.No:
                        pass
                        
                    else:
                        pass
                
                elif self.si_action.currentText() == '마법부여':
                    
                    magic_scroll_t = ''
                    magic_scroll = []
                    index = 1
                    for i in player.인벤토리:
                        if i.종류 == '주문서':
                            magic_scroll.append([index, i])
                            magic_scroll_t  += str(index) + '. ' + i.이름 + '\n'
                            index += 1
                        
                    text, ok = QInputDialog.getText(self, '마법부여 주문서를 고르시오.', magic_scroll_t)
                    
                    if ok:
                        l = []
                        for j in range(index - 1):
                            l.append(str(j + 1))
                        
                        if text in l:
                            for k in magic_scroll:
                                if str(k[0]) == text:
                                    nitem.마법부여(item, k[1], self)
                                    player.인벤토리.remove(k[1])
                                    
                        else:
                            QMessageBox.information(self, '마법부여 없음.', '해당 마법부여는 존재하지 않습니다.')
                    
                    else:
                        pass
                          
                 
                

            elif clastSelected[1].text() == '소비':
                
                if self.si_action.currentText() == '사용':
                    
                    사용결과 = item.사용(player ,self)
                    
                    if 사용결과:
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                        QMessageBox.about(self, '아이템 사용.', '{} 을(를) 사용했습니다.'.format(item.이름))
                    else:
                        QMessageBox.about(self, '아이템 사용 실패..', '{} 사용에 실패했습니다.'.format(item.이름))
                        
                    
                elif self.si_action.currentText() == '상세정보':
                    
                    QMessageBox.about(self, '아이템 정보.', '아이템 이름: {}\n" {} "\n종류: {}\n<<<<< 상세정보 >>>>>\n{}\n============================================'.
                                    format(item.이름, item.설명, item.종류, item.상세정보))
                
                elif self.si_action.currentText() == '버리기':
                    
                    button_Reply = QMessageBox.warning(self, '아이템 버리기.', '{} 을(를) 버리시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
                    
                    if button_Reply == QMessageBox.Yes:
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                    elif button_Reply == QMessageBox.No:
                        pass
                    else:
                        pass
                    
                elif self.si_action.currentText() == '판매':
                    button_Reply = QMessageBox.warning(self, '아이템 판매.', '{} 을(를) 판매 하시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
                    
                    if button_Reply == QMessageBox.Yes:
                        
                        
                        판매골드 = item.판매가
                            
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                        
                        player.골드 += 판매골드
                        
                        QMessageBox.about(self, '아이템을 차원 상인에게 판매했습니다..@@', '{} G 를 획득했습니다. $$$'.format(판매골드))
                        
                    elif button_Reply == QMessageBox.No:
                        pass
                    
                    else:
                        pass
                    
                self.seiChg()
                    
            elif clastSelected[1].text() == '주문서':
                
                if self.si_action.currentText() == '상세정보':
                    
                    QMessageBox.about(self, '아이템 정보.', '아이템 이름: {}\n" {} "\n종류: {}\n<<<<< 상세정보 >>>>>\n{}\n============================================'.
                                    format(item.이름, item.설명, item.종류, item.상세정보))
                
                elif self.si_action.currentText() == '버리기':
                    
                    button_Reply = QMessageBox.warning(self, '아이템 버리기.', '{} 을(를) 버리시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
                    
                    if button_Reply == QMessageBox.Yes:
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                    elif button_Reply == QMessageBox.No:
                        pass
                    else:
                        pass
                    
                elif self.si_action.currentText() == '판매':
                    button_Reply = QMessageBox.warning(self, '아이템 판매.', '{} 을(를) 판매 하시겠습니까?'.format(item.이름), QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
                    
                    if button_Reply == QMessageBox.Yes:
                        
                        
                        판매골드 = item.판매가
                        
                        if item.장착됨 == True:
                            item.장착해제(player)
                            
                        player.인벤토리.pop(self.get_index_from_itemCode(int(clastSelected[4].text())))
                        
                        player.골드 += 판매골드
                        
                        QMessageBox.about(self, '아이템을 차원 상인에게 판매했습니다..@@', '{} G 를 획득했습니다. $$$'.format(판매골드))
                        
                    elif button_Reply == QMessageBox.No:
                        pass
                    
                    else:
                        pass
                    
            self.seiChg()
            
        else:
            pass
        
        self.si_action.clear()
        
        self.seiChg()    
        
    def seiChg(self):
        global player
        
        player.레벨업포인트 += player.레벨체크()
        
        player_equip.clear()
        
        self.TV_equip.setHorizontalHeaderLabels(['장비칸', '장착된 아이템', 'id'])
        
        for i in player_equipList:
            if getattr(player, '장비칸_' + i) == '-':
                player_equip.append([i, '장착 X', '-'])
            else:
                for j in player.인벤토리:
                    if j.iid == getattr(player, '장비칸_' + i):
                        player_equip.append([i, j.이름, j.iid])
        
        self.TV_equip.setRowCount(len(player_equip))
        self.TV_equip.setColumnCount(len(player_equip[0]))
        
        row = self.TV_equip.rowCount()
        col = self.TV_equip.columnCount()
        
        for j in range(row):
            for k in range(col):
                self.TV_equip.setItem(j, k, QTableWidgetItem(str(player_equip[j][k])))
        
        self.item_ui()

        self.스탯출력()
        
    def action_move_Map(self):
        global player
        can_move_maps = ''
        maplist = []
        index = 1
        for i in player.맵.연결:
            maplist.append([index, i])
            can_move_maps += str(index) + '. ' + i + '\n'
            index += 1
            
        text, ok = QInputDialog.getText(self, '이동할 곳을 고르시오.', can_move_maps)
        
        print(text)
        print(ok)
        
        if ok:
            
            l = []
            for i in range(index - 1):
                l.append(str(i + 1))
                
            if text in l:
                for j in maplist:
                    if str(j[0]) == text:
                        player.맵 = map.level_list[j[1]]
                        self.seiChg()
                        self.currentMap_action()          
                        self.clear_scrollArea()
                        self.generate_Btn_for_map()
                        break

        else:
            pass
        
    def action_researh(self):
        global player
        self.TB_main.clear()
        self.clear_scrollArea()
        self.all_setDisabled()
        
        self.TB_main.append('탐색중.')
        reset(1000)
        self.TB_main.append('탐색중..')
        reset(1000)
        self.TB_main.append('탐색중...')
        reset(1000)
        self.TB_main.append(' < !!! > ')
        reset(1000)
        
        self.all_setEnabled()
        
        mon_num = random.choice(player.맵.몬스터조우수)
        mon = []
        
        for _ in range(mon_num):
            mon.append(random.choice(player.맵.몬스터))
            
        self.battle(mon)
        
    def action_rest(self):
        global player
        self.TB_main.clear()
        self.clear_scrollArea()
        self.all_setDisabled()
        
        self.TB_main.append('휴식중.')
        reset(1000)
        self.TB_main.append('휴식중..')
        reset(1000)
        self.TB_main.append('휴식중...')
        reset(1000)
        self.seiChg()
        player.회복(player.최대체력)
        player.마력회복(player.최대마력)
        self.seiChg()
        self.TB_main.append('체력과 마력을 모두 회복했습니다.')
        
        reset(1000)
        
        self.all_setEnabled()
        self.currentMap_action()
        self.generate_Btn_for_map()
        
    def action_shop(self):
        global player
        self.TB_main.clear()
        self.clear_scrollArea()
        
        
        index = 1
        shopItems = []
        
        for i in player.맵.상점:
            for j in map.shop_list[i][1]:
                shopItems.append([index, nitem.item_generate(j, player, map.shop_list[i][0])])
                index += 1
                
        index = 0
        
        for i in player.맵.상점:
            self.TB_main.append('===  {}  ==='.format(i))
            for j in map.shop_list[i][1]:
                self.TB_main.append(str(index + 1) + '. ' + j + '  // 가격: {}  // " {} "'.format(shopItems[index][1].구매가, shopItems[index][1].설명))
                index += 1
                
        self.generate_Btn_for_shop()
    
    def action_gambit(self):
        self.TB_main.clear()
        self.clear_scrollArea()
        self.generate_Btn_for_gambit()
        self.TB_main.append('=== 목숨이 2개인자 어서오라... ===')
        self.TB_main.append('=================================================')
        self.TB_main.append('================  도  박  장  ===================')
        self.TB_main.append('=================================================')
        reset(1000)
        
    def battle_monsters_hp(self):
        global 몬스터들
        self.TB_main.clear()
        self.TB_main.append('=== 전투상대 ===')
        for i in 몬스터들:
            if i[1].체력 > 0:
                self.TB_main.append(str(i[0]) + '. ' + i[1].이름 + '  ///  HP: {} / {}'.format(i[1].체력, i[1].최대체력))
            else:
                self.TB_main.append(str(i[0]) + '. ' + i[1].이름 + '  ///  [ 죽음 ]'.format(i[1].체력, i[1].최대체력))
    
    def battle(self, monsters):
        global 몬스터들
        global player
        self.TB_main.clear()
        
        index = 1
        self.clear_scrollArea()
        self.generate_Btn_for_battle()
        
        for i in monsters:
            몬스터들.append([index, monster.monster_gen(i, player.맵.차원)])
            index += 1
            
        self.battle_monsters_hp()
        
    
    def isWin(self):
        global 몬스터들
        global player
        death = 0
        
        self.all_setEnabled()
        
        if player.체력 <= 0:
            self.TB_main.append('플레이어 사망...')
            reset(1000)
            self.TB_main.append('골드를 전부 잃습니다.')
            reset(1000)
            player.골드 = 0
            self.currentMap_action()          
            self.clear_scrollArea()
            self.generate_Btn_for_map()
            player.체력 = 0
            player.회복(player.최대체력)
            player.마력 = 0
            player.마력회복(player.최대마력)
            
            # 전투변수 초기화
            player.중독 = 0
            
            self.seiChg()
            return False
            
        for i in 몬스터들:
            if i[1].체력 <= 0:
                death += 1
        
        if death == len(몬스터들):
            골드량 = 0
            for i in 몬스터들:
                골드량 += i[1].골드
            player.골드 += 골드량 * len(몬스터들)
            
            경치량 = 0
            for i in 몬스터들:
                경치량 += i[1].경험치
            player.경험치 += 경치량 * len(몬스터들)
            
            for i in 몬스터들:
                for j in i[1].아이템:
                    if random.random()*100 <= j[1]: # 아이템 획득.
                        player.인벤토리.append(nitem.item_generate(j[0], player))
                        self.TB_main.append('{} 획득.'.format(j[0]))
                        reset(1000)
                        
            
            self.TB_main.append('골드 +{}'.format(골드량 * len(몬스터들)))
            reset(1000)
            self.TB_main.append('경험치 +{}'.format(경치량 * len(몬스터들)))
            reset(1000)
            
            # 전투변수 초기화
            player.중독 = 0
            
            self.currentMap_action()          
            self.clear_scrollArea()
            self.generate_Btn_for_map()
            self.seiChg()
            
            return True
    
    
    def skill_run(self):
        
        global 몬스터들
        self.all_setDisabled()
        
        self.TB_main.append('도망중입니다. =3')
        reset(400)
        self.TB_main.append('도망중입니다. ==3')
        reset(400)
        self.TB_main.append('도망중입니다. ===3')
        reset(400)
        
        if random.random() * 100 <= 50:
            self.TB_main.append('도망에 성공했습니다.')
            reset(400)
            self.all_setEnabled()
            
            self.currentMap_action()          
            self.clear_scrollArea()
            self.generate_Btn_for_map()
            self.seiChg()
        else:
            self.TB_main.append('도망에 실패했습니다.')
            reset(400)
            self.all_setEnabled()
            
            self.battle_monsters_turn(몬스터들)
            self.seiChg()
            결과 = self.isWin()
            if 결과 == True or 결과 == False:
                return
    
    def battle_end_process(self):
        global player
        if player.중독 > 0:
            player.체력 -= player.중독
            self.TB_main.append('{} (이)가 중독되어 {} 의 피해를 받습니다.'.format(player.이름, player.중독))
            
    def battle_monsters_turn(self, 몬스터들):
        for i in 몬스터들:
            if i[1].체력 > 0:
                skill.skill_list[random.choice(i[1].스킬)].시전(i[1], player, self)
        
    def player_skill_go(self, skillName, targetNum, enemys, index):
        global player
        l = []
        for i in range(index - 1):
            l.append(str(i + 1))
        
        if targetNum in l:
            for j in enemys:
                if str(j[0]) == targetNum:
                    skill.skill_list[skillName].시전(player, j[1], self)
                    return '사용성공'
        else:
            return '오류'
        
    def skill_punch(self):
        global 몬스터들
        can_attack_e = ''
        enemys = []
        index = 1
        for i in 몬스터들:
            if i[1].체력 > 0:
                enemys.append([index, i[1]])
                can_attack_e += str(index) + '. ' + i[1].이름 + '\n'
                index += 1
            
        text, ok = QInputDialog.getText(self, '공격할 대상을 고르시오.', can_attack_e)
        
        if ok:
            
            시전결과 = self.player_skill_go('주먹질', text, enemys, index)
                    
            self.seiChg()
            
            결과 = self.isWin()
            if 결과 == True:
                return
            
            # 적 턴
            if 시전결과 == '오류': # 스킬 사용 오류시 적도 턴 진행 안함.
                self.TB_main.append('잘못된 선택입니다...')
                reset(800)
                return
                
            else: # 스킬 사용 성공시 적 턴 진행.
                self.battle_monsters_turn(몬스터들)
                
            self.seiChg()
                
            결과 = self.isWin()
            if 결과 == False:
                return
            
            self.battle_end_process()
            reset(700)
            self.battle_monsters_hp()
        
        
        self.seiChg()
        
        결과 = self.isWin()
        if 결과 == True or 결과 == False:
            return
        
        self.seiChg()
        
    def skill_twice_slash(self):     
        global 몬스터들
        can_attack_e = ''
        enemys = []
        index = 1
        for i in 몬스터들:
            if i[1].체력 > 0:
                enemys.append([index, i[1]])
                can_attack_e += str(index) + '. ' + i[1].이름 + '\n'
                index += 1
            
        text, ok = QInputDialog.getText(self, '공격할 대상을 고르시오.', can_attack_e)
        
        if ok:
            
            시전결과 = self.player_skill_go('두번베기', text, enemys, index)
                    
            self.seiChg()
            
            결과 = self.isWin()
            if 결과 == True:
                return
            
            # 적 턴
            if 시전결과 == '오류': # 스킬 사용 오류시 적도 턴 진행 안함.
                self.TB_main.append('잘못된 선택입니다...')
                reset(800)
                return
                
            else: # 스킬 사용 성공시 적 턴 진행.
                self.battle_monsters_turn(몬스터들)
                
            self.seiChg()
                
            결과 = self.isWin()
            if 결과 == False:
                return
            
            self.battle_end_process()
            reset(700)
            self.battle_monsters_hp()
        
        
        self.seiChg()
        
        결과 = self.isWin()
        if 결과 == True or 결과 == False:
            return
        
        self.seiChg()
          
    def skill_AdoGen(self):
        global 몬스터들
        can_attack_e = ''
        enemys = []
        index = 1
        for i in 몬스터들:
            if i[1].체력 > 0:
                enemys.append([index, i[1]])
                can_attack_e += str(index) + '. ' + i[1].이름 + '\n'
                index += 1
        
        text, ok = QInputDialog.getText(self, '공격할 대상을 고르시오.', can_attack_e)
        
        if ok:
            
            시전결과 = self.player_skill_go('아도겐', text, enemys, index)
                    
            self.seiChg()
            
            결과 = self.isWin()
            if 결과 == True:
                return
            
            # 적 턴
            if 시전결과 == '오류': # 스킬 사용 오류시 적도 턴 진행 안함.
                self.TB_main.append('잘못된 선택입니다...')
                reset(800)
                return
                
            else: # 스킬 사용 성공시 적 턴 진행.
                self.battle_monsters_turn(몬스터들)
                
            self.seiChg()
                
            결과 = self.isWin()
            if 결과 == False:
                return
            
            self.TB_main.clear()
            self.battle_end_process()
            reset(700)
            self.battle_monsters_hp()
        
        
        self.isWin()
        self.seiChg()
        
    def clear_scrollArea(self):
        widget = self.scrollArea.widget()
        if widget is not None:
            layout = widget.layout()
            if layout is not None:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater() 
    
    def btn_gambit(self):
        global player
        text, ok = QInputDialog.getText(self, '도박장', '얼마를 거시겠습니까?')
        
        if ok:
            try:
                건돈 = int(text)
                if player.골드 >= 건돈:
                    player.골드 -= 건돈
                    
                    if random.random() * 100 <= 50:
                        self.TB_main.append('!!! 대박 !!!')
                        reset(800)
                        self.TB_main.append('건 돈의 2배인 {} 골드를 받습니다.'.format(건돈 * 2))
                        reset(1000)
                        player.골드 += 건돈 * 2
                        
                    else:
                        self.TB_main.append('ㅠㅠ 꽝 ㅠㅠ')
                        reset(800)
                        self.TB_main.append('건 돈을 모두 잃습니다... -{} 골드'.format(건돈))
                        reset(1000)
                    
                else:
                    QMessageBox.information(self, '돈 없음.', '도박할 돈이 없네...')
                
                self.seiChg()
            except:
                QMessageBox.information(self, '오류', '잘못된 선택입니다.')
        
        self.seiChg()
      
    def btn_purchase(self):
        global player
        purchase_text = ''
        purchase_list = []
        index = 1
        for i in player.맵.상점:
            purchase_text += ('===  {}  ===\n'.format(i))
            for j in map.shop_list[i][1]:
                purchase_list.append([index, nitem.item_generate(j, player, map.shop_list[i][0])])
                purchase_text += str(index) + '. ' + j + '  // 가격: {}  // " {} "\n'.format(purchase_list[index-1][1].구매가, purchase_list[index-1][1].설명)
                index += 1
            
        text, ok = QInputDialog.getText(self, '구매할 아이템을 고르시오.', purchase_text)
        
        if ok:
            l = []
            for k in range(index - 1):
                l.append(str(k + 1))
            
            if text in l:
                for p in purchase_list:
                    if str(p[0]) == text:
                        if player.골드 < p[1].구매가:
                            QMessageBox.information(self, '그지 쉑~.', '돈 더 가져와라~')
                        else:
                            player.골드 -= p[1].구매가
                            player.인벤토리.append(nitem.item_generate(p[1].이름, player))
                            QMessageBox.about(self, '구매 완료.', '{} 구매했습니다.'.format(p[1].이름))
                        
            else:
                QMessageBox.information(self, '잘못된 선택', '해당 아이템은 존재하지 않습니다.')
        else:
            pass
        
        self.seiChg()
        
    def btn_out_shop(self):
        self.TB_main.clear()
        self.clear_scrollArea()
        self.currentMap_action()
        self.generate_Btn_for_map()
        self.seiChg()
        
    def currentMap_action(self):
        global 몬스터들
        global player
        
        player.스탯새로고침()
        몬스터들 = []
        self.TB_main.clear()
        self.TB_main.append('<< 가능한 행동 >>')
        for i in player.맵.행동:
            self.TB_main.append(i)
        self.TB_main.append('==========================')
        
    def generate_Btn_for_gambit(self):
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        
        
        button = QPushButton('돈걸기')
        button.objectName = 'Btn_구매'
        button.clicked.connect(self.btn_gambit)
        buttons_layout.addWidget(button)
        
        button2 = QPushButton('도박장 나가기')
        button2.objectName = 'Btn_도박장_나가기'
        button2.clicked.connect(self.btn_out_shop)
        buttons_layout.addWidget(button2)
        
        self.scrollArea.setWidget(buttons_widget)
        
    def generate_Btn_for_shop(self):
        
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        
        
        button = QPushButton('구매')
        button.objectName = 'Btn_구매'
        button.clicked.connect(self.btn_purchase)
        buttons_layout.addWidget(button)
        
        button2 = QPushButton('상점 나가기')
        button2.objectName = 'Btn_상점_나가기'
        button2.clicked.connect(self.btn_out_shop)
        buttons_layout.addWidget(button2)
        
        self.scrollArea.setWidget(buttons_widget)
        
    def generate_Btn_for_battle(self):
        global player
        
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        
        for i in player.스킬들:
            button = QPushButton(i)
            button.objectName = 'Btn_' + i
            if i == '도망':
                button.clicked.connect(self.skill_run)
            elif i == '주먹질':
                button.clicked.connect(self.skill_punch)
            elif i == '아도겐':
                button.clicked.connect(self.skill_AdoGen)
            elif i == '두번베기':
                button.clicked.connect(self.skill_twice_slash)
                
            buttons_layout.addWidget(button)
        
        self.scrollArea.setWidget(buttons_widget)
    
    def generate_Btn_for_map(self):
        global player
        
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        
        for i in player.맵.행동:
            
            button = QPushButton(i)
            button.objectName = 'Btn_' + i
            
            if i == '이동':
                button.clicked.connect(self.action_move_Map)
            elif i == '탐색':
                button.clicked.connect(self.action_researh)
            elif i == '휴식':
                button.clicked.connect(self.action_rest)
            elif i == '도박장':
                button.clicked.connect(self.action_gambit)
            elif i == '상점':
                button.clicked.connect(self.action_shop)
            
                
            buttons_layout.addWidget(button)
        
        self.scrollArea.setWidget(buttons_widget)
         
    def showEvent(self, a0: QShowEvent | None) -> None:
        if a0.spontaneous():
            
            self.seiChg()
            
            
        super().showEvent(a0)
            
    def 스탯출력(self):
        global player

        player.스탯새로고침()
        
        self.Btn_statpoint.setText('스탯 포인트 사용 ({})'.format(player.레벨업포인트))
        
        player_stat.clear()
        
        self.TV_stat.setHorizontalHeaderLabels(['스탯', '수치'])
        
        for i in player_statList:
            
            player_stat.append([i, getattr(player, i)])
            
        
        self.TV_stat.setRowCount(len(player_stat))
        self.TV_stat.setColumnCount(len(player_stat[0]))
        
        row = self.TV_stat.rowCount()
        col = self.TV_stat.columnCount()
        
        for j in range(row):
            for k in range(col):
                self.TV_stat.setItem(j, k, QTableWidgetItem(str(player_stat[j][k])))
                
        self.label_playerName.setText('플레이어 이름 : [ {} ]'.format(player.이름))
        self.label_job.setText('직업 : [ {} ]'.format(player.직업))
        self.label_demen.setText('차원 : [ {} ]'.format(player.맵.차원))
        self.label_level.setText('레벨 : [ {} ]'.format(player.레벨))
        self.label_map.setText('맵이름 : [ {} ]'.format(player.맵.이름))
        self.label_hp.setText('HP : {} / {} '.format(player.체력, player.최대체력))
        self.label_map.setText('맵이름 : [ {} ]'.format(player.맵.이름))
        
    def save(self):
        저장(id)
        
        QMessageBox.information(self, '저장', '저장이 완료되었습니다.')
        
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    loginWindow = LoginClass()
     
    nameWindow = NameClass()
    

    mainWindow = MainClass()
    mainWindow.hide()
    
    #프로그램 화면을 보여주는 코드
    loginWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()