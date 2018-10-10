

try :
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.uic import loadUiType
    import os, time
    from os import path
    import sys
    import urllib.request
    import pafy
    labelmess = "Python libraries imported successfully"
except Exception as e:
    labelmess = str(e)
# import ui File
FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))

# Intiate Ui file

class MainApp(QMainWindow, FORM_CLASS):

    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handel_Buttons()
        self.label_7.setText(labelmess)

    def Handle_UI(self):
        # self = QMainWindow
        self.setWindowTitle('PyDownload')
        self.setFixedSize(900,450)
    def Handel_Buttons(self):
        self.actionExit.triggered.connect(self.exit)
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handel_Browse)
        self.pushButton_4.clicked.connect(self.Download_Youtube_Video)
        self.pushButton_11.clicked.connect(self.Get_Youtube_Video)
        self.pushButton_3.clicked.connect(self.Save_Browse)
        self.pushButton_10.clicked.connect(self.Playlist_Download)
        self.pushButton_9.clicked.connect(self.Save_Browse)


    def Handel_Browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit_2.setText(name)
    def Handle_Progress(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize
        if totalsize > 0 :
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents() #Not Responding solotion
    def Download(self):
        # need to : url - save location - size
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.Handle_Progress)
        except Exception :
            QMessageBox.warning(self, "Download Error", "The Download Failed")
            return
        QMessageBox.information(self , "Download Completed", "The Download Finshed")

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_3.setText(save)
        self.lineEdit_11.setText(save)
    def Get_Youtube_Video(self):
        try :
            video_link = self.lineEdit_4.text()
            v =  pafy.new(video_link)
            #print(v.title) #title
            #print(v.duration) # time
            #print(v.rating) # raiting
            #print(v.author) # channel name
            #print(v.length) #
            #print(v.keywords)
            #print(v.thumb) # pic
            #print(v.videoid)
            #print(v.viewcount) # count
            st = v.videostreams
            print(st)
            for s in st:
                data = '{} {} {} {} MB '.format(s.mediatype, s.extension, s.quality , round( (s.get_filesize() / (1024**2)), 1 ))
                self.comboBox.addItem(data)
        except Exception as e:
            QMessageBox.warning(self, "Error", "Error While Getting Youtube Video Info: \n {}.".format(e))
            #print ("\n", e)


    def Download_Youtube_Video(self):
        video_link = self.lineEdit_4.text()
        save_location = self.lineEdit_3.text()
        v =  pafy.new(video_link)
        st = v.videostreams
        quality = self.comboBox.currentIndex()
        down = st[quality].download(filepath= save_location)

        QMessageBox.information(self , "Download Completed", "The Video Download Finshed")

    def Playlist_Download(self):
        Playlist_url = self.lineEdit_5.text()
        save_location = self.lineEdit_11.text()
        playlist = pafy.get_playlist(Playlist_url)
        videos = playlist['items']

        os.chdir(save_location)

        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:

            os.mkdir(str(playlist['title'])) # make folder
            os.chdir(str(playlist['title']))

        for video in videos:
            p = video['pafy']
            best = p.getbest(preftype='any')
            best.download()

    def exit(self):
        QMessageBox.information(self, "Exitting", "See You Next Time (:")
        sys.exit()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
