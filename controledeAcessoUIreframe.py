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

class Ui_RegistroON(object):
    def cadastrar(self):
        print("confirmar")																							# mostra no terminal 'confirmar'
        cadastroc="insert into pessoas (nome, rg, ra) values ('{}', md5('{}'), md5('{}'))".format(ultimonome,ultimorg,ultimora)		# pega os dados de ra e ra lidos anteriormente e insere no banco de dados
        mycursor.execute(cadastroc)																				# executando a ação 
        cadastrodb.commit()
        RegistroON.hide()

    def cancelar(self):
        print("cancelou")
        RegistroON.hide()
        pass

    def setupUi(self, RegistroON):
        RegistroON.setObjectName("RegistroON")
        RegistroON.setWindowModality(QtCore.Qt.NonModal)
        RegistroON.resize(512, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegistroON.sizePolicy().hasHeightForWidth())
        RegistroON.setSizePolicy(sizePolicy)
        RegistroON.setMinimumSize(QtCore.QSize(512, 230))
        RegistroON.setMaximumSize(QtCore.QSize(512, 230))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        RegistroON.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegistroON.setWindowIcon(icon)
        RegistroON.setWindowOpacity(1.0)
        self.verticalLayoutWidget = QtWidgets.QWidget(RegistroON)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 511, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(RegistroON)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 169, 72))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RgL = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RgL.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RgL.sizePolicy().hasHeightForWidth())
        self.RgL.setSizePolicy(sizePolicy)
        self.RgL.setMinimumSize(QtCore.QSize(25, 30))
        self.RgL.setMaximumSize(QtCore.QSize(25, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.RgL.setFont(font)
        self.RgL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RgL.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RgL.setTextFormat(QtCore.Qt.AutoText)
        self.RgL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RgL.setObjectName("RgL")
        self.horizontalLayout.addWidget(self.RgL)
        self.RgNumeros = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RgNumeros.setMinimumSize(QtCore.QSize(120, 20))
        self.RgNumeros.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.RgNumeros.setFont(font)
        self.RgNumeros.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RgNumeros.setObjectName("RgNumeros")
        self.horizontalLayout.addWidget(self.RgNumeros)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Ra = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Ra.setMinimumSize(QtCore.QSize(25, 30))
        self.Ra.setMaximumSize(QtCore.QSize(25, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Ra.setFont(font)
        self.Ra.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Ra.setTextFormat(QtCore.Qt.AutoText)
        self.Ra.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Ra.setObjectName("Ra")
        self.horizontalLayout_2.addWidget(self.Ra)
        self.RaNumeros = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RaNumeros.setMinimumSize(QtCore.QSize(120, 20))
        self.RaNumeros.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.RaNumeros.setFont(font)
        self.RaNumeros.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RaNumeros.setObjectName("RaNumeros")
        self.horizontalLayout_2.addWidget(self.RaNumeros)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(RegistroON)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 160, 511, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confirmarb = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.confirmarb.setMinimumSize(QtCore.QSize(100, 35))
        self.confirmarb.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.confirmarb.setFont(font)
        self.confirmarb.setObjectName("confirmarb")
        self.horizontalLayout_3.addWidget(self.confirmarb)
        self.cancelarb = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.cancelarb.setMinimumSize(QtCore.QSize(100, 35))
        self.cancelarb.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cancelarb.setFont(font)
        self.cancelarb.setObjectName("cancelarb")
        self.horizontalLayout_3.addWidget(self.cancelarb)

        self.retranslateUi(RegistroON)
        QtCore.QMetaObject.connectSlotsByName(RegistroON)

        self.confirmarb.clicked.connect(self.cadastrar)
        self.cancelarb.clicked.connect(self.cancelar)        

    def retranslateUi(self, RegistroON):
        _translate = QtCore.QCoreApplication.translate
        RegistroON.setWindowTitle(_translate("RegistroON", "Registro"))
        self.label.setText(_translate("RegistroON", "Confirme os dados abaixo:"))
        self.RgL.setText(_translate("RegistroON", "RG:"))
        self.RgNumeros.setText(_translate("RegistroON", ultimorg))#"999999999"))
        self.Ra.setText(_translate("RegistroON", "RA:"))
        self.RaNumeros.setText(_translate("RegistroON", ultimora))# 1300000000000
        print("do retranslate "+ultimorg)
        self.confirmarb.setText(_translate("RegistroON", "Confirmar"))
        self.cancelarb.setText(_translate("RegistroON", "Cancelar"))

class Ui_MainWindow(object):
    def __init__(self):
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
        self.capture=VideoStream(src=0).start()     # 2
        self.timer = QTimer()
        self.timer.timeout.connect(self.qr)
        self.timer.start(15)

    def mensageboxInvalido(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Formato inválido!")
        msgBox.setWindowTitle("Inválido!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print("ok")																					# necessário para fazer as mudanças 

    def mensageboxCadastro(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Usuário não encontrado, deseja iniciar cadastramento?")
        msgBox.setWindowTitle("Cadastro")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            RegistroON.show()
            # if ultimorg!=ultimorg:

        if returnValue == QMessageBox.No:
            print("não quer cadastrar")
            pass

    def mensageboxBemVindo(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Bem-Vindo {}".format(str(self.myresult).replace("[('","").replace("',)]","")))
        msgBox.setWindowTitle("Bem-Vindo")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print("ok")

    def qr(self):
        # print("estou no qr")
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
            image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK  
            self.stream.setPixmap(QtGui.QPixmap(image))
            separar=barcodeData.split("\r\n")
            # try:
            global ultimorg
            global ultimora
            global ultimonome
            ultimorg=str(separar[1])
            ultimora=str(separar[2])
            ultimonome=str(separar[0])
            print("aqui temos rg={}, ra={} e nome={}".format(ultimorg,ultimora,ultimonome))
            comando="select nome from pessoas where rg=md5('{}') and ra=md5('{}')".format(ultimorg,ultimora)		# e prepará o envio da pergunta 'o rg e o ra estão no banco de dados?' e retorna o nome da pessoa ----- talvez vulnerável a sql injection
            mycursor.execute(comando)																	# executa a ação 
            self.myresult = mycursor.fetchall()
            ui2.retranslateUi(RegistroON)
            print("do for "+ultimorg)


            if str(self.myresult) == "[]":
                print("nao cadastrado, tentando cadastrar")
                self.mensageboxCadastro()


            else:
                print("usuario cadastrado")
                print("Bem Vindo {}".format(str(self.myresult).replace("[('","").replace("',)]","")))												# mostra no terminal a mensagem "Bem Vindo" + o nome do usuário formatado corretamente
                guardando="insert into controle (ra,datas) values ('{}',current_timestamp())".format(ultimora)				# guadando a quem entrou na sala no banco de dados
                mycursor.execute(guardando)																				# executando a ação
                cadastrodb.commit()																						# necessário para fazer as mudança
                print("sucesso?")
                self.mensageboxBemVindo()
            # except:
            #     print("formato qr invalido")
            #     self.mensageboxInvalido()


if __name__ == "__main__":
    import sys
    cadastrodb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")		# accesando o banco de dados
    mycursor = cadastrodb.cursor()
    ultimora="1300000000000"
    ultimorg="999999999"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RegistroON = QtWidgets.QWidget()
    ui2 = Ui_RegistroON()
    ui2.setupUi(RegistroON)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())