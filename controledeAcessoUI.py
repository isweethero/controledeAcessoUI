# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controledeAcesso.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
import cv2
import qimage2ndarray #SOLUTION FOR MEMORY LEAK
import mysql.connector
from pyzbar import pyzbar
import mysql.connector
from imutils.video import VideoStream

class Ui_MainWindow(object):
    def __init__(self):
        #self.video_size = QSize(320, 240)
        self.setup_camera()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        MainWindow.setWindowTitle("LabMaker")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_labmaker = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(40)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_labmaker.setFont(font)
        self.label_labmaker.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_labmaker.setAutoFillBackground(False)
        self.label_labmaker.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_labmaker.setAlignment(QtCore.Qt.AlignCenter)
        self.label_labmaker.setWordWrap(False)
        self.label_labmaker.setObjectName("label_labmaker")
        self.verticalLayout.addWidget(self.label_labmaker)
        self.stream = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stream.setMaximumSize(QtCore.QSize(1024, 600))
        self.stream.setText("")
        self.stream.setPixmap(QtGui.QPixmap("924x450.png"))
        self.stream.setAlignment(QtCore.Qt.AlignCenter)
        self.stream.setObjectName("stream")
        self.verticalLayout.addWidget(self.stream)
        self.aguardando = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.aguardando.setMaximumSize(QtCore.QSize(16777215, 1024))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.aguardando.setFont(font)
        self.aguardando.setAlignment(QtCore.Qt.AlignCenter)
        self.aguardando.setObjectName("aguardando")
        self.verticalLayout.addWidget(self.aguardando)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_labmaker.setText(_translate("MainWindow", "Laboratório Maker"))
        self.aguardando.setText(_translate("MainWindow", "Aguardando código QR"))

    def setup_camera(self): #Initialize camera.        
        self.capture=VideoStream(src=0).start()
        #self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
        #self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.principal)
        self.timer.start(30)

    def mensagebox(self,op):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        if op=="invalido":
            msgBox.setText("Formato inválido!")
            msgBox.setWindowTitle("Inválido!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            #msgBox.buttonClicked.connect(msgButtonClick)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print("ok")

        if op=="cadastro":
            msgBox.setText("Usuário não encontrado, deseja iniciar cadastramento?")
            msgBox.setWindowTitle("Cadastro")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Yes:
                print("quer cadastrar")

            if returnValue == QMessageBox.No:
                print("não quer cadastrar")
                pass

        if op=="bem-vindo":
            msgBox.setText("Bem-Vindo {}".format(str(self.myresult).replace("[('","").replace("',)]","")))
            msgBox.setWindowTitle("Bem-Vindo")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print("ok")

    def principal(self):
        frame = self.capture.read()     #Read frame from camera and repaint QLabel widget.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK
        self.stream.setPixmap(QtGui.QPixmap(image))
        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:			# loop nos códigos reconhecidos
            (x, y, w, h) = barcode.rect										# pegando as bordas do qr 
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)	# e desenhando em volta 
            barcodeData = barcode.data.decode("utf-8")	# o que foi lido é em bytes, transformando em texto
            #text = "{}".format(barcodeData)	# transformando em uma string para ser mostrado
            #print(barcodeData) # esse é o que tem no qrcode
            #cv2.putText(frame, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)		# desenhando o código e o tipo dele na imagem 
            image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK  
            self.stream.setPixmap(QtGui.QPixmap(image))
            separar=barcodeData.split("\r\n")																# separando os dados lidos, é separado no \r\n de cada. exemplo TESTE3\r\n1\r\n1 ficará TESTE3,1,1 ---  rg=9 números ra=13 números
            print("Separando "+str(separar))

            try:
                nome=separar[0]
                rg=str(separar[1])																			# rg
                ra=str(separar[2])																			# ra
                print("rg="+str(rg))
                comando="select nome from pessoas where rg=md5('{}') and ra=md5('{}')".format(rg,ra)		# e prepará o envio da pergunta 'o rg e o ra estão no banco de dados?' e retorna o nome da pessoa ----- talvez vulnerável a sql injection
                mycursor.execute(comando)																	# executa a ação 
                self.myresult = mycursor.fetchall()		    													# terminado a execução do comando é necessário isso -- https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

                if str(self.myresult) == "[]":
                    print("nao cadastrado, tentando cadastrar")
                    self.mensagebox("cadastro")

                else:
                    print("usuario cadastrado")
                    print("Bem Vindo {}".format(str(self.myresult).replace("[('","").replace("',)]","")))												# mostra no terminal a mensagem "Bem Vindo" + o nome do usuário formatado corretamente
                    guardando="insert into controle (ra,datas) values ('{}',current_timestamp())".format(ra)				# guadando a quem entrou na sala no banco de dados
                    mycursor.execute(guardando)																				# executando a ação
                    cadastrodb.commit()																						# necessário para fazer as mudança
                    print("sucesso?")
                    self.mensagebox("bem-vindo")
            except:
                print("formato invalido")
                self.mensagebox("invalido")
                
if __name__ == "__main__":
    import sys
    cadastrodb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")		# accesando o banco de dados
    mycursor = cadastrodb.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())