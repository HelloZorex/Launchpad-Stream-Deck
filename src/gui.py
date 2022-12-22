import threading
import json
import sys
import os

import PyQt5.QtWidgets as qtw
# from qtwidgets import AnimatedToggle
        
import midi as mi
import mapper as rr


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Launchdeck')
        self.setWindowOpacity(0.99)
        # self.setWindowIcon(qtw.QIcon('LD.ico')) FIX THIS
        self.setStyleSheet("background-color: #1f1f1f;")
        # self.setStyleSheet("background-color: rgba(31, 31, 31, 50);")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("QPushButton {color: #bababa;}")
        self.setLayout(qtw.QVBoxLayout())
        self.topgrid()
        self.buttongrid()
        self.tooltip()

        self.show()

    def topgrid(self, parent=None):
        container2 = qtw.QWidget()
        container2.setLayout(qtw.QGridLayout())
        container2.setStyleSheet("padding: 8px; QInputDialog {background-color: #bababa;}")
        container2.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

        btn_func = qtw.QPushButton('Functions', clicked = self.onActivated)
        btn_func.setToolTip("Change function of button")
        btn_func.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        
        self.btn_start = qtw.QPushButton('Start', clicked = self.run)
        self.btn_start.setToolTip("Start Launchpad")
        self.btn_start.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        
        btn_stop = qtw.QPushButton('Stop', clicked = self.stop)
        btn_stop.setToolTip("Stop Launchpad")
        btn_stop.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

        container2.layout().addWidget(btn_func, 0, 1)        
        container2.layout().addWidget(self.btn_start, 0, 2)
        container2.layout().addWidget(btn_stop, 0, 3)

        self.layout().addWidget(container2, stretch=1)
        
    def buttongrid(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        container.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        # container.setStyleSheet("background-color: #171717; border-radius: 5px;")
        container.setStyleSheet("background-color: #171717; padding: 10px;")

        # Button creator - doesn't work when trying to change color of button after it's been created
        # for i in range(11,112):
        #     exec(eval("f'self.btn_{i} = qtw.QPushButton(clicked = lambda: self.buttonselect(\"{i}\", self.btn_{i}, self.prevbtn))'"))

        self.prevbtn = None
        self.btn_11 = qtw.QPushButton(clicked = lambda: self.buttonselect("11", self.btn_11, self.prevbtn))
        self.btn_12 = qtw.QPushButton(clicked = lambda: self.buttonselect('12', self.btn_12, self.prevbtn))
        self.btn_13 = qtw.QPushButton(clicked = lambda: self.buttonselect('13', self.btn_13, self.prevbtn))
        self.btn_14 = qtw.QPushButton(clicked = lambda: self.buttonselect('14', self.btn_14, self.prevbtn))
        self.btn_15 = qtw.QPushButton(clicked = lambda: self.buttonselect('15', self.btn_15, self.prevbtn))
        self.btn_16 = qtw.QPushButton(clicked = lambda: self.buttonselect('16', self.btn_16, self.prevbtn))
        self.btn_17 = qtw.QPushButton(clicked = lambda: self.buttonselect('17', self.btn_17, self.prevbtn))
        self.btn_18 = qtw.QPushButton(clicked = lambda: self.buttonselect('18', self.btn_18, self.prevbtn))
        self.btn_19 = qtw.QPushButton(clicked = lambda: self.buttonselect('19', self.btn_19, self.prevbtn))
        self.btn_21 = qtw.QPushButton(clicked = lambda: self.buttonselect('21', self.btn_21, self.prevbtn))
        self.btn_22 = qtw.QPushButton(clicked = lambda: self.buttonselect('22', self.btn_22, self.prevbtn))
        self.btn_23 = qtw.QPushButton(clicked = lambda: self.buttonselect('23', self.btn_23, self.prevbtn))
        self.btn_24 = qtw.QPushButton(clicked = lambda: self.buttonselect('24', self.btn_24, self.prevbtn))
        self.btn_25 = qtw.QPushButton(clicked = lambda: self.buttonselect('25', self.btn_25, self.prevbtn))
        self.btn_26 = qtw.QPushButton(clicked = lambda: self.buttonselect('26', self.btn_26, self.prevbtn))
        self.btn_27 = qtw.QPushButton(clicked = lambda: self.buttonselect('27', self.btn_27, self.prevbtn))
        self.btn_28 = qtw.QPushButton(clicked = lambda: self.buttonselect('28', self.btn_28, self.prevbtn))
        self.btn_29 = qtw.QPushButton(clicked = lambda: self.buttonselect('29', self.btn_29, self.prevbtn))
        self.btn_31 = qtw.QPushButton(clicked = lambda: self.buttonselect('31', self.btn_31, self.prevbtn))
        self.btn_32 = qtw.QPushButton(clicked = lambda: self.buttonselect('32', self.btn_32, self.prevbtn))
        self.btn_33 = qtw.QPushButton(clicked = lambda: self.buttonselect('33', self.btn_33, self.prevbtn))
        self.btn_34 = qtw.QPushButton(clicked = lambda: self.buttonselect('34', self.btn_34, self.prevbtn))
        self.btn_35 = qtw.QPushButton(clicked = lambda: self.buttonselect('35', self.btn_35, self.prevbtn))
        self.btn_36 = qtw.QPushButton(clicked = lambda: self.buttonselect('36', self.btn_36, self.prevbtn))
        self.btn_37 = qtw.QPushButton(clicked = lambda: self.buttonselect('37', self.btn_37, self.prevbtn))
        self.btn_38 = qtw.QPushButton(clicked = lambda: self.buttonselect('38', self.btn_38, self.prevbtn))
        self.btn_39 = qtw.QPushButton(clicked = lambda: self.buttonselect('39', self.btn_39, self.prevbtn))
        self.btn_41 = qtw.QPushButton(clicked = lambda: self.buttonselect('41', self.btn_41, self.prevbtn))
        self.btn_42 = qtw.QPushButton(clicked = lambda: self.buttonselect('42', self.btn_42, self.prevbtn))
        self.btn_43 = qtw.QPushButton(clicked = lambda: self.buttonselect('43', self.btn_43, self.prevbtn))
        self.btn_44 = qtw.QPushButton(clicked = lambda: self.buttonselect('44', self.btn_44, self.prevbtn))
        self.btn_45 = qtw.QPushButton(clicked = lambda: self.buttonselect('45', self.btn_45, self.prevbtn))
        self.btn_46 = qtw.QPushButton(clicked = lambda: self.buttonselect('46', self.btn_46, self.prevbtn))
        self.btn_47 = qtw.QPushButton(clicked = lambda: self.buttonselect('47', self.btn_47, self.prevbtn))
        self.btn_48 = qtw.QPushButton(clicked = lambda: self.buttonselect('48', self.btn_48, self.prevbtn))
        self.btn_49 = qtw.QPushButton(clicked = lambda: self.buttonselect('49', self.btn_49, self.prevbtn))
        self.btn_51 = qtw.QPushButton(clicked = lambda: self.buttonselect('51', self.btn_51, self.prevbtn))
        self.btn_52 = qtw.QPushButton(clicked = lambda: self.buttonselect('52', self.btn_52, self.prevbtn))
        self.btn_53 = qtw.QPushButton(clicked = lambda: self.buttonselect('53', self.btn_53, self.prevbtn))
        self.btn_54 = qtw.QPushButton(clicked = lambda: self.buttonselect('54', self.btn_54, self.prevbtn))
        self.btn_55 = qtw.QPushButton(clicked = lambda: self.buttonselect('55', self.btn_55, self.prevbtn))
        self.btn_56 = qtw.QPushButton(clicked = lambda: self.buttonselect('56', self.btn_56, self.prevbtn))
        self.btn_57 = qtw.QPushButton(clicked = lambda: self.buttonselect('57', self.btn_57, self.prevbtn))
        self.btn_58 = qtw.QPushButton(clicked = lambda: self.buttonselect('58', self.btn_58, self.prevbtn))
        self.btn_59 = qtw.QPushButton(clicked = lambda: self.buttonselect('59', self.btn_59, self.prevbtn))
        self.btn_61 = qtw.QPushButton(clicked = lambda: self.buttonselect('61', self.btn_61, self.prevbtn))
        self.btn_62 = qtw.QPushButton(clicked = lambda: self.buttonselect('62', self.btn_62, self.prevbtn))
        self.btn_63 = qtw.QPushButton(clicked = lambda: self.buttonselect('63', self.btn_63, self.prevbtn))
        self.btn_64 = qtw.QPushButton(clicked = lambda: self.buttonselect('64', self.btn_64, self.prevbtn))
        self.btn_65 = qtw.QPushButton(clicked = lambda: self.buttonselect('65', self.btn_65, self.prevbtn))
        self.btn_66 = qtw.QPushButton(clicked = lambda: self.buttonselect('66', self.btn_66, self.prevbtn))
        self.btn_67 = qtw.QPushButton(clicked = lambda: self.buttonselect('67', self.btn_67, self.prevbtn))
        self.btn_68 = qtw.QPushButton(clicked = lambda: self.buttonselect('68', self.btn_68, self.prevbtn))
        self.btn_69 = qtw.QPushButton(clicked = lambda: self.buttonselect('69', self.btn_69, self.prevbtn))
        self.btn_71 = qtw.QPushButton(clicked = lambda: self.buttonselect('71', self.btn_71, self.prevbtn))
        self.btn_72 = qtw.QPushButton(clicked = lambda: self.buttonselect('72', self.btn_72, self.prevbtn))
        self.btn_73 = qtw.QPushButton(clicked = lambda: self.buttonselect('73', self.btn_73, self.prevbtn))
        self.btn_74 = qtw.QPushButton(clicked = lambda: self.buttonselect('74', self.btn_74, self.prevbtn))
        self.btn_75 = qtw.QPushButton(clicked = lambda: self.buttonselect('75', self.btn_75, self.prevbtn))
        self.btn_76 = qtw.QPushButton(clicked = lambda: self.buttonselect('76', self.btn_76, self.prevbtn))
        self.btn_77 = qtw.QPushButton(clicked = lambda: self.buttonselect('77', self.btn_77, self.prevbtn))
        self.btn_78 = qtw.QPushButton(clicked = lambda: self.buttonselect('78', self.btn_78, self.prevbtn))
        self.btn_79 = qtw.QPushButton(clicked = lambda: self.buttonselect('79', self.btn_79, self.prevbtn))
        self.btn_81 = qtw.QPushButton(clicked = lambda: self.buttonselect('81', self.btn_81, self.prevbtn))
        self.btn_82 = qtw.QPushButton(clicked = lambda: self.buttonselect('82', self.btn_82, self.prevbtn))
        self.btn_83 = qtw.QPushButton(clicked = lambda: self.buttonselect('83', self.btn_83, self.prevbtn))
        self.btn_84 = qtw.QPushButton(clicked = lambda: self.buttonselect('84', self.btn_84, self.prevbtn))
        self.btn_85 = qtw.QPushButton(clicked = lambda: self.buttonselect('85', self.btn_85, self.prevbtn))
        self.btn_86 = qtw.QPushButton(clicked = lambda: self.buttonselect('86', self.btn_86, self.prevbtn))
        self.btn_87 = qtw.QPushButton(clicked = lambda: self.buttonselect('87', self.btn_87, self.prevbtn))
        self.btn_88 = qtw.QPushButton(clicked = lambda: self.buttonselect('88', self.btn_88, self.prevbtn))
        self.btn_89 = qtw.QPushButton(clicked = lambda: self.buttonselect('89', self.btn_89, self.prevbtn))
        self.btn_104 = qtw.QPushButton(clicked = lambda: self.buttonselect('104', self.btn_104, self.prevbtn))
        self.btn_105 = qtw.QPushButton(clicked = lambda: self.buttonselect('105', self.btn_105, self.prevbtn))
        self.btn_106 = qtw.QPushButton(clicked = lambda: self.buttonselect('106', self.btn_106, self.prevbtn))
        self.btn_107 = qtw.QPushButton(clicked = lambda: self.buttonselect('107', self.btn_107, self.prevbtn))
        self.btn_108 = qtw.QPushButton(clicked = lambda: self.buttonselect('108', self.btn_108, self.prevbtn))
        self.btn_109 = qtw.QPushButton(clicked = lambda: self.buttonselect('109', self.btn_109, self.prevbtn))
        self.btn_110 = qtw.QPushButton(clicked = lambda: self.buttonselect('110', self.btn_110, self.prevbtn))
        self.btn_111 = qtw.QPushButton(clicked = lambda: self.buttonselect('111', self.btn_111, self.prevbtn))
        spacer = qtw.QSpacerItem(40, 30)

        container.layout().addWidget(self.btn_104, 0, 0)
        container.layout().addWidget(self.btn_105, 0, 1)
        container.layout().addWidget(self.btn_106, 0, 2)
        container.layout().addWidget(self.btn_107, 0, 3)
        container.layout().addWidget(self.btn_108, 0, 4)
        container.layout().addWidget(self.btn_109, 0, 5)
        container.layout().addWidget(self.btn_110, 0, 6)
        container.layout().addWidget(self.btn_111, 0, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_81, 2, 0)
        container.layout().addWidget(self.btn_82, 2, 1)
        container.layout().addWidget(self.btn_83, 2, 2)
        container.layout().addWidget(self.btn_84, 2, 3)
        container.layout().addWidget(self.btn_85, 2, 4)
        container.layout().addWidget(self.btn_86, 2, 5)
        container.layout().addWidget(self.btn_87, 2, 6)
        container.layout().addWidget(self.btn_88, 2, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_89, 2, 9)
        container.layout().addWidget(self.btn_71, 3, 0)
        container.layout().addWidget(self.btn_72, 3, 1)
        container.layout().addWidget(self.btn_73, 3, 2)
        container.layout().addWidget(self.btn_74, 3, 3)
        container.layout().addWidget(self.btn_75, 3, 4)
        container.layout().addWidget(self.btn_76, 3, 5)
        container.layout().addWidget(self.btn_77, 3, 6)
        container.layout().addWidget(self.btn_78, 3, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_79, 3, 9)
        container.layout().addWidget(self.btn_61, 4, 0)
        container.layout().addWidget(self.btn_62, 4, 1)
        container.layout().addWidget(self.btn_63, 4, 2)
        container.layout().addWidget(self.btn_64, 4, 3)
        container.layout().addWidget(self.btn_65, 4, 4)
        container.layout().addWidget(self.btn_66, 4, 5)
        container.layout().addWidget(self.btn_67, 4, 6)
        container.layout().addWidget(self.btn_68, 4, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_69, 4, 9)
        container.layout().addWidget(self.btn_51, 5, 0)
        container.layout().addWidget(self.btn_52, 5, 1)
        container.layout().addWidget(self.btn_53, 5, 2)
        container.layout().addWidget(self.btn_54, 5, 3)
        container.layout().addWidget(self.btn_55, 5, 4)
        container.layout().addWidget(self.btn_56, 5, 5)
        container.layout().addWidget(self.btn_57, 5, 6)
        container.layout().addWidget(self.btn_58, 5, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_59, 5, 9)
        container.layout().addWidget(self.btn_41, 6, 0)
        container.layout().addWidget(self.btn_42, 6, 1)
        container.layout().addWidget(self.btn_43, 6, 2)
        container.layout().addWidget(self.btn_44, 6, 3)
        container.layout().addWidget(self.btn_45, 6, 4)
        container.layout().addWidget(self.btn_46, 6, 5)
        container.layout().addWidget(self.btn_47, 6, 6)
        container.layout().addWidget(self.btn_48, 6, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_49, 6, 9)
        container.layout().addWidget(self.btn_31, 7, 0)
        container.layout().addWidget(self.btn_32, 7, 1)
        container.layout().addWidget(self.btn_33, 7, 2)
        container.layout().addWidget(self.btn_34, 7, 3)
        container.layout().addWidget(self.btn_35, 7, 4)
        container.layout().addWidget(self.btn_36, 7, 5)
        container.layout().addWidget(self.btn_37, 7, 6)
        container.layout().addWidget(self.btn_38, 7, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_39, 7, 9)
        container.layout().addWidget(self.btn_21, 8, 0)
        container.layout().addWidget(self.btn_22, 8, 1)
        container.layout().addWidget(self.btn_23, 8, 2)
        container.layout().addWidget(self.btn_24, 8, 3)
        container.layout().addWidget(self.btn_25, 8, 4)
        container.layout().addWidget(self.btn_26, 8, 5)
        container.layout().addWidget(self.btn_27, 8, 6)
        container.layout().addWidget(self.btn_28, 8, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_29, 8, 9)
        container.layout().addWidget(self.btn_11, 9, 0)
        container.layout().addWidget(self.btn_12, 9, 1)
        container.layout().addWidget(self.btn_13, 9, 2)
        container.layout().addWidget(self.btn_14, 9, 3)
        container.layout().addWidget(self.btn_15, 9, 4)
        container.layout().addWidget(self.btn_16, 9, 5)
        container.layout().addWidget(self.btn_17, 9, 6)
        container.layout().addWidget(self.btn_18, 9, 7)
        container.layout().addItem(spacer)
        container.layout().addWidget(self.btn_19, 9, 9)

        self.layout().addWidget(container, stretch=4)

    def tooltip(self):
        with open('keymap.json', 'r') as d:
            hkparse = json.load(d)

        self.btn_11.setToolTip(hkparse["11"][1])
        self.btn_12.setToolTip(hkparse["12"][1])
        self.btn_13.setToolTip(hkparse["13"][1])
        self.btn_14.setToolTip(hkparse["14"][1])
        self.btn_15.setToolTip(hkparse["15"][1])
        self.btn_16.setToolTip(hkparse["16"][1])
        self.btn_17.setToolTip(hkparse["17"][1])
        self.btn_18.setToolTip(hkparse["18"][1])
        self.btn_19.setToolTip(hkparse["19"][1])
        self.btn_21.setToolTip(hkparse["21"][1])
        self.btn_22.setToolTip(hkparse["22"][1])
        self.btn_23.setToolTip(hkparse["23"][1])
        self.btn_24.setToolTip(hkparse["24"][1])
        self.btn_25.setToolTip(hkparse["25"][1])
        self.btn_26.setToolTip(hkparse["26"][1])
        self.btn_27.setToolTip(hkparse["27"][1])
        self.btn_28.setToolTip(hkparse["28"][1])
        self.btn_29.setToolTip(hkparse["29"][1])
        self.btn_31.setToolTip(hkparse["31"][1])
        self.btn_32.setToolTip(hkparse["32"][1])
        self.btn_33.setToolTip(hkparse["33"][1])
        self.btn_34.setToolTip(hkparse["34"][1])
        self.btn_35.setToolTip(hkparse["35"][1])
        self.btn_36.setToolTip(hkparse["36"][1])
        self.btn_37.setToolTip(hkparse["37"][1])
        self.btn_38.setToolTip(hkparse["38"][1])
        self.btn_39.setToolTip(hkparse["39"][1])
        self.btn_41.setToolTip(hkparse["41"][1])
        self.btn_42.setToolTip(hkparse["42"][1])
        self.btn_43.setToolTip(hkparse["43"][1])
        self.btn_44.setToolTip(hkparse["44"][1])
        self.btn_45.setToolTip(hkparse["45"][1])
        self.btn_46.setToolTip(hkparse["46"][1])
        self.btn_47.setToolTip(hkparse["47"][1])
        self.btn_48.setToolTip(hkparse["48"][1])
        self.btn_49.setToolTip(hkparse["49"][1])
        self.btn_51.setToolTip(hkparse["51"][1])
        self.btn_52.setToolTip(hkparse["52"][1])
        self.btn_53.setToolTip(hkparse["53"][1])
        self.btn_54.setToolTip(hkparse["54"][1])
        self.btn_55.setToolTip(hkparse["55"][1])
        self.btn_56.setToolTip(hkparse["56"][1])
        self.btn_57.setToolTip(hkparse["57"][1])
        self.btn_58.setToolTip(hkparse["58"][1])
        self.btn_59.setToolTip(hkparse["59"][1])
        self.btn_61.setToolTip(hkparse["61"][1])
        self.btn_62.setToolTip(hkparse["62"][1])
        self.btn_63.setToolTip(hkparse["63"][1])
        self.btn_64.setToolTip(hkparse["64"][1])
        self.btn_65.setToolTip(hkparse["65"][1])
        self.btn_66.setToolTip(hkparse["66"][1])
        self.btn_67.setToolTip(hkparse["67"][1])
        self.btn_68.setToolTip(hkparse["68"][1])
        self.btn_69.setToolTip(hkparse["69"][1])
        self.btn_71.setToolTip(hkparse["71"][1])
        self.btn_72.setToolTip(hkparse["72"][1])
        self.btn_73.setToolTip(hkparse["73"][1])
        self.btn_74.setToolTip(hkparse["74"][1])
        self.btn_75.setToolTip(hkparse["75"][1])
        self.btn_76.setToolTip(hkparse["76"][1])
        self.btn_77.setToolTip(hkparse["77"][1])
        self.btn_78.setToolTip(hkparse["78"][1])
        self.btn_79.setToolTip(hkparse["79"][1])
        self.btn_81.setToolTip(hkparse["81"][1])
        self.btn_82.setToolTip(hkparse["82"][1])
        self.btn_83.setToolTip(hkparse["83"][1])
        self.btn_84.setToolTip(hkparse["84"][1])
        self.btn_85.setToolTip(hkparse["85"][1])
        self.btn_86.setToolTip(hkparse["86"][1])
        self.btn_87.setToolTip(hkparse["87"][1])
        self.btn_88.setToolTip(hkparse["88"][1])
        self.btn_89.setToolTip(hkparse["89"][1])
        self.btn_104.setToolTip(hkparse["104"][1])
        self.btn_105.setToolTip(hkparse["105"][1])
        self.btn_106.setToolTip(hkparse["106"][1])
        self.btn_107.setToolTip(hkparse["107"][1])
        self.btn_108.setToolTip(hkparse["108"][1])
        self.btn_109.setToolTip(hkparse["109"][1])
        self.btn_110.setToolTip(hkparse["110"][1])
        self.btn_111.setToolTip(hkparse["111"][1])

    def buttonselect(self, text, button, prevbtn):        
        if prevbtn != None and prevbtn != button: 
            prevbtn.setStyleSheet("background-color: #171717")
            button.setStyleSheet("background-color: #3c85cf")
            self.prevbtn = button
            self.bNum = text
        
        elif prevbtn == button and self.bNum == text:
            button.setStyleSheet("background-color: #171717")
            self.prevbtn = button
            self.bNum = None
        
        else:
            button.setStyleSheet("background-color: #3c85cf")
            self.prevbtn = button
            self.bNum = text

        if isinstance(self.bNum, str):
            print(self.bNum)

    def onActivated(self):
        msg = qtw.QMessageBox()
        msg.setStyleSheet("background-color: #1f1f1f; color: #bababa")
        selectlist = ["Select Function", "Open File", "Play Sound", "Open Tab", "Keyboard Shortcut"]
        
        try:
            if isinstance(int(self.bNum), int):
                taskselect, _ = qtw.QInputDialog.getItem(self, "Select Function", f"Select Function for key {self.bNum}", selectlist, 0, False)
          
                if taskselect == "Select Function":
                    pass
          
                elif taskselect == "Open File":
                    self.getFileDir("1")
                    print("Finished")
          
                elif taskselect == "Play Sound":
                    self.getSoundFile()
                    print("Finished")
          
                elif taskselect == "Open Tab":
                    url, ok = qtw.QInputDialog.getText(self, "Open Tab", "Enter url:")
                    
                    if url and ok:
                        rr.opentab(self.bNum, url)
                        print("Finished")
                
                elif taskselect == "Keyboard Shortcut":
                    shortkey, ok = qtw.QInputDialog.getText(self, "Keyboard Shortcut", "Enter keyboard shortcut:")
                
                    if shortkey and ok:
                        rr.shortkeys(self.bNum, shortkey)
                        print("Finished")
            
            self.tooltip()
        
        except:
            msg.setText("Select a button you want to change function of first")
            retval = msg.exec_()

    def settings(self):
        selectlist = ["Select setting", "Chrome path"]
        taskselect, _ = qtw.QInputDialog.getItem(self, "Select setting", "Select setting", selectlist)
        if taskselect == "Chrome path":
            self.getFileDir("2")
            print("Finished")
            
    def getFileDir(self, func):
        file_filter = "Executable (*.exe)"
        response, _ = qtw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select File",
            directory=os.getcwd(),
            filter=file_filter
        )

        rr.openexe(self.bNum, response)

    def getSoundFile(self):
        file_filter = "MP3 File (*.mp3)"
        response, ok = qtw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select File",
            directory=os.getcwd(),
            filter=file_filter
        )
        rr.storesound(self.bNum, response)
        print("Store Sound Stored")

    def stop(self):
        self.m.stop()

        self.btn_start.setEnabled(True)
        self.btn_start.setStyleSheet("background-color: #1f1f1f")
        self.btn_start.setText("Start")

    def run(self):
        self.btn_start.setEnabled(False)
        self.btn_start.setStyleSheet("background-color: #3c85cf")
        self.btn_start.setText("Running")

        self.m = mi.Midi()
        try:
            self.newthread = threading.Thread(target=self.m.start)
            self.newthread.start()
        except:
            print("Midi not connected")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    # screenGeometry = qtw.QDesktopWidget().screenGeometry(-1)
    # screenGeometry = qtw.QDesktopWidget().primaryScreen()
    # size = mw.geometry()
    # print(screenGeometry)
    # print(size)

    mw.setMinimumSize(400, 400)
    mw.setMaximumSize(600, 600)

    # mw.setFixedSize(screenGeometry.width()*0.1564, screenGeometry.height()*0.2779)
    # mw.showMaximized()
    
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.setStyleSheet("QPushButton, QLabel, QLineEdit, QComboBox, QAbstractItemView, QMessageBox, QToolTip {color: #c7c7c7;}")
    app.exec_()
    app.quit()