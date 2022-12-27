import threading
import json
import sys
import os

import PyQt5.QtGui as Qg
import PyQt5.QtCore as Qt
import PyQt5.QtWidgets as Qw
# from qtwidgets import AnimatedToggle
        
import midi as mi
import mapper as rr


class MainWindow(Qw.QWidget):
    def __init__(self):
        self.start_flag = False

        super().__init__()
        self.setWindowTitle('Launchdeck')
        self.setWindowOpacity(0.99)
        # self.setWindowIcon(Qw.QIcon('LD.ico')) FIX THIS
        self.setStyleSheet("background-color: #1f1f1f;")
        # self.setStyleSheet("background-color: rgba(31, 31, 31, 50);")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("QPushButton {color: #bababa;}")
        self.setLayout(Qw.QVBoxLayout())
        self.topgrid()
        self.button_generator()
        self.set_tooltip()
        self.show()

    def topgrid(self, parent=None):
        container2 = Qw.QWidget()
        container2.setLayout(Qw.QGridLayout())
        container2.setStyleSheet("padding: 8px; QInputDialog {background-color: #bababa;}")
        container2.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.btn_start = Qw.QPushButton('Start', clicked = self.run)
        self.btn_start.setToolTip("Start Launchpad")
        self.btn_start.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        
        self.btn_stop = Qw.QPushButton('Stop', clicked = self.stop)
        self.btn_stop.setToolTip("Stop Launchpad")
        self.btn_stop.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        container2.layout().addWidget(self.btn_start, 0, 1)
        container2.layout().addWidget(self.btn_stop, 0, 2)

        self.layout().addWidget(container2, stretch=1)
        
    def button_generator(self):
        # https://stackoverflow.com/questions/54927194/python-creating-buttons-in-loop-in-pyqt5
        # https://www.reddit.com/r/learnpython/comments/dvdfp5/add_qpushbuttons_in_loop_with_different_names/
        # https://stackoverflow.com/questions/19837486/lambda-in-a-loop
        # https://stackoverflow.com/questions/18836291/lambda-function-returning-false

        container = Qw.QWidget()
        container.setLayout(Qw.QGridLayout())
        container.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        container.setStyleSheet("background-color: #171717; padding: 10px;")

        def action_menu(button, idx):
            action1 = Qw.QAction('Change Tab', self)
            action1.triggered.connect(lambda ignore, y=idx: self.change_open_tab(y))
            action2 = Qw.QAction('Change Hotkey', self)
            action2.triggered.connect(lambda ignore, y=idx: self.change_hot_key(y))
            action3 = Qw.QAction('Change File', self)
            action3.triggered.connect(lambda ignore, y=idx: self.change_open_file(y))
            action4 = Qw.QAction('Change Sound', self)
            action4.triggered.connect(lambda ignore, y=idx: self.change_play_sound(y))
            action5 = Qw.QAction('Reset Button', self)
            action5.triggered.connect(lambda: print('coming soon'))

            buttonMenu = Qw.QMenu(button)
            buttonMenu.addAction(action1)
            buttonMenu.addAction(action2)
            buttonMenu.addAction(action3)
            buttonMenu.addAction(action4)
            buttonMenu.addAction(action5)

            button.installEventFilter(self)
            buttonMenu.installEventFilter(self)
            return buttonMenu

        # define base variables
        self.prev = None
        self.buttons = {}
        self.action_events = {}
        spacer = Qw.QSpacerItem(40, 30)

        # starts position at 104, ends at 19
        # the tens place descends, but the ones place ascends
        # pattern: 48, 49, 31, 32........38, 39, 21, 22, etc
        size = 10
        for btn_row in range(size):
            # top row seperator
            if btn_row == 1: container.layout().addItem(spacer, 1, 0)
            else:
                column_cnt = 0
                for btn_column in range(size):
                    tens, ones = size-btn_row, column_cnt+1
                    num = (tens*10)+ones
                    pos = str(num+3) if (btn_row==0) else str(num)

                    # right side column seperator
                    if btn_column == 8: container.layout().addItem(spacer, btn_row, btn_column)
                    else:
                        # button 112 is out of bounds, pass over and continue
                        if pos != '112':
                            self.buttons[pos] = Qw.QPushButton(clicked = lambda ignore, x=pos: self.button_select(x))
                            container.layout().addWidget(self.buttons[pos], btn_row, btn_column)
                            self.action_events[pos] = action_menu(self.buttons[pos], pos)
                            column_cnt+=1
                        else: pass

        self.layout().addWidget(container, stretch=4)

    def set_tooltip(self):
        # opens key function dictionary
        with open('keymap.json', 'r') as d:
            hkparse = json.load(d)

            for key in self.buttons.keys():
                self.buttons[key].setToolTip(hkparse[key][1])

    def eventFilter(self, source, event):
        if event.type() == Qt.QEvent.ContextMenu:
            if source in self.buttons.values():
                # checks for button number that matches the source button object id
                button_key = next((k for k, v in self.buttons.items() if v == source), None)
                self.action_events[button_key].exec_(event.globalPos())
                return True
        return super().eventFilter(source, event)

    def button_select(self, text):        
        if self.prev != None and self.prev != text: 
            self.buttons[self.prev].setStyleSheet("background-color: #171717")
            self.buttons[text].setStyleSheet("background-color: #3c85cf")
            self.prev = text
            self.bNum = text
        
        elif self.prev == text and self.bNum == text:
            self.buttons[text].setStyleSheet("background-color: #171717")
            self.prev = text
            self.bNum = None
        
        else:
            self.buttons[text].setStyleSheet("background-color: #3c85cf")
            self.prev = text
            self.bNum = text

        if isinstance(self.bNum, str):
            print(self.bNum)
        
    def change_open_file(self, pos):
        file_filter = "Executable (*.exe)"
        response, _ = Qw.QFileDialog.getOpenFileName(parent=self, caption="Select File", directory=os.getcwd(), filter=file_filter)
        rr.openexe(pos, response)

    def change_play_sound(self, pos):
        file_filter = "MP3 File (*.mp3)"
        response, ok = Qw.QFileDialog.getOpenFileName(parent=self, caption="Select File", directory=os.getcwd(), filter=file_filter)
        rr.storesound(pos, response)
        print("Store Sound Stored")

    def change_open_tab(self, pos):
        url, ok = Qw.QInputDialog.getText(self, "Open Tab", "Enter url:")
                    
        if url and ok:
            rr.opentab(pos, url)
            print("Finished")

    def change_hot_key(self, pos):
        shortkey, ok = Qw.QInputDialog.getText(self, "Keyboard Shortcut", "Enter keyboard shortcut:")
                
        if shortkey and ok:
            rr.shortkeys(pos, shortkey)
            print("Finished")

    # remove this function
    def onActivated(self):
        msg = Qw.QMessageBox()
        msg.setStyleSheet("background-color: #1f1f1f; color: #bababa")
        selectlist = ["Select Function", "Open File", "Play Sound", "Open Tab", "Keyboard Shortcut"]
        
        try:
            if isinstance(int(self.bNum), int):
               pass
            self.tooltip()
        
        except:
            msg.setText("Select a self.buttons[text] you want to change function of first")
            retval = msg.exec_()

    def stop(self):
        if self.start_flag == True:
            self.m.stop()
            self.start_flag = False

            self.btn_start.setEnabled(True)
            self.btn_start.setStyleSheet("background-color: #1f1f1f")
            self.btn_start.setText("Start")

    def run(self):
        self.btn_start.setEnabled(False)
        self.btn_start.setStyleSheet("background-color: #3c85cf")
        self.btn_start.setText("Running")

        self.start_flag = True

        self.m = mi.Midi()
        try:
            self.newthread = threading.Thread(target=self.m.start)
            self.newthread.start()
        except:
            print("Midi not connected")


if __name__ == "__main__":
    app = Qw.QApplication(sys.argv)
    mw = MainWindow()

    # screenGeometry = Qw.QDesktopWidget().screenGeometry(-1)
    # screenGeometry = Qw.QDesktopWidget().primaryScreen()
    # size = mw.geometry()
    # print(screenGeometry)
    # print(size)

    mw.setMinimumSize(400, 400)
    mw.setMaximumSize(600, 600)

    # mw.setFixedSize(screenGeometry.width()*0.1564, screenGeometry.height()*0.2779)
    # mw.showMaximized()
    
    app.setStyle(Qw.QStyleFactory.create('Fusion'))
    app.setStyleSheet("QPushButton, QLabel, QLineEdit, QComboBox, QAbstractItemView, QMessageBox, QToolTip {color: #c7c7c7;}")
    app.exec_()
    app.quit()