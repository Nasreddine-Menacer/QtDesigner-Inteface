########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QSizeGrip,QApplication, QMainWindow
import pandas as pd
import requests
import matplotlib.pyplot as plt
import pyqtgraph
from pyqtgraph import PlotWidget 
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot

import pdfplumber
from pdf2image import convert_from_path



########################################################################
# IMPORT GUI FILE
from logiciel import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        #######################################################################
        ## # Set main background to transparent
        ########################################################################  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        #######################################################################
        ## # Shadow effect style
        ########################################################################  
        #self.shadow = QGraphicsDropShadowEffect(self)
        #self.shadow.setBlurRadius(50)
        #self.shadow.setXOffset(0)
        #self.shadow.setYOffset(0)
        #self.shadow.setColor(QColor(0, 92, 157, 550))

        
        #######################################################################
        ## # Appy shadow to central widget
        ########################################################################  
        #self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #######################################################################
        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        #######################################################################
        #self.setWindowIcon(QtGui.QIcon(":/icons/github.svg"))
        # Set window tittle
        self.setWindowTitle("CVOCE")

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        QSizeGrip(self.ui.size_grip)

        #######################################################################
        #Minimize window
        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Close window
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_9.clicked.connect(lambda: self.close())


        #######################################################################
        #Restore/Maximize window
        self.ui.pushButton_3.clicked.connect(lambda: self.restore_or_maximize_window())

        #self.ui.pushButton_21.clicked.connect(self.combo)
        self.ui.comboBox_3.activated.connect(self.combo)
        self.ui.comboBox_2.activated.connect(self.combo)

        #self.ui.pushButton_22.clicked.connect(self.plot_data_marche_du_travail)

        #self.ui.pushButton_6.clicked.connect(self.plot_data_plus_recrute)



        #self.ui.pushButton_21.clicked.connect(self.competences)
        self.ui.comboBox_10.activated.connect(self.competences)

        self.ui.listWidget.activated.connect(self.defini)

        self.ui.pushButton_12.clicked.connect(lambda: self.formation())

        self.ui.pushButton_21.clicked.connect(lambda: self.affiche_formation())

        self.ui.browse.clicked.connect(self.browsepdf)
        
        



        
        




    


        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()






        
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.header.mouseMoveEvent = moveWindow
        #######################################################################


        #######################################################################
        #Left Menu toggle button
        self.ui.pushButton_8.clicked.connect(lambda: self.slideLeftMenu())


        self.show()

        self.ui.stackedWidget.setCurrentWidget(self.ui.donnees_metier)

        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mailing))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profil))



        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.donnees_metier))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.donnees_competence))
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.donnees_formations))


        self.ui.pushButton_13.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.saisi_manuelle))
        self.ui.pushButton_14.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.analyse_cvs))
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.trouver_emploi))
        self.ui.pushButton_16.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.trouver_formation))


        self.ui.pushButton_17.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profil))
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tableau_de_bord))
        self.ui.pushButton_19.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.agenda))
        self.ui.pushButton_20.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mailing))


        




    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slide_menu_contener.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            #self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            #self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_contener, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################



    def downolad_data(self):
        csv_url='https://statistiques.pole-emploi.org/offres/teleoffres'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open('series_offres_diffusees.xlsx', 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 1 enregistré avec succées')
        #############################################################ú#
        csv_url='https://images.pr-rooms.com/Handlers/HTFile.ashx?MZD=xW6gm%2fUvAeVjIY4Mi9aQYg%3d%3d&SITEKEY=987fc643-f04e-4330-bbe4-c53328125bed'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open('Series_CVS_2021_T1.xlsx', 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 2 enregistré avec succées')
        #############################################################ú#
        csv_url='https://images.pr-rooms.com/Handlers/HTFile.ashx?MZD=qYEPyk5lQZMv8lKt5Q01%2fQ%3d%3d'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open("Entrées_en_formation_des_demandeurs_d'emploi_au_3e_trimestre_2020.xlsx", 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 3 enregistré avec succées')
        #############################################################ú#
        csv_url='https://www.pole-emploi.org/files/live/sites/peorg/files/documents/Statistiques-et-analyses/Open-data/ROME/ROME_ArboPrincipale.xlsx'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open("ROME_ArboPrincipale.xlsx", 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 4 enregistré avec succées')
        #############################################################ú#
        csv_url='https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr_dictionnaire_competences_referens_3/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open("fr-esr_dictionnaire_competences_referens_3.csv", 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 5 enregistré avec succées')
        #############################################################ú#
        csv_url='https://data.education.gouv.fr/explore/dataset/fr-esr-cartographie_formations_parcoursup/download?format=csv'
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open("fr-esr-cartographie_formations_parcoursup.csv", 'wb')
        csv_file.write(url_content)
        csv_file.close()
        print('\nFichier 6 enregistré avec succées')
        

        
    def combo(self):
    
        xls = pd.ExcelFile('series_offres_diffusees.xlsx')
        df1 = pd.read_excel(xls, 'Total')
        df2 = pd.read_excel(xls, 'Contrat')
        df3 = pd.read_excel(xls, 'Metier')
        a = int(self.ui.comboBox_3.currentText())
        m = int(self.ui.comboBox_2.currentText())
        res=df1.loc[(df1['Année'] == int(a)) & (df1['Mois'] == int(m)),["Nombre d'offres diffusées"]].values
        self.ui.label_16.setText(str(res).translate({ord(i): None for i in '[]'}))
        ####################################################################################################
        res1=df2.loc[(df2['Année'] == int(a)) & (df2['Mois'] == int(m)),["CDI"]].values
        self.ui.label_33.setText(str(res1).translate({ord(i): None for i in '[]'}))
        ####################################################################################################
        res2=df2.loc[(df2['Année'] == int(a)) & (df2['Mois'] == int(m)),["CDD de moins d'un mois"]].values
        self.ui.label_24.setText(str(res2).translate({ord(i): None for i in '[]'}))
        ####################################################################################################
        res3=df2.loc[(df2['Année'] == int(a)) & (df2['Mois'] == int(m)),["Autres contrats (intérim, saisonniers, ...)"]].values
        self.ui.label_26.setText(str(res3).translate({ord(i): None for i in '[]'}))
        ####################################################################################################
        res4=df2.loc[(df2['Année'] == int(a)) & (df2['Mois'] == int(m)),["CDD de plus de 6 mois"]].values
        res5=df2.loc[(df2['Année'] == int(a)) & (df2['Mois'] == int(m)),["CDD de 1 à 6 mois"]].values
        res6 = res4+res5
        self.ui.label_32.setText(str(res6).translate({ord(i): None for i in '[]'}))





    def plot_data_marche_du_travail(self):

        xls = pd.ExcelFile('series_offres_diffusees.xlsx')
        df = pd.read_excel(xls, 'Total')

        

        nbr1=0
        for i in range(len(df)):
            if df["Année"][i]==2015:
               nbr1 = nbr1 + df["Nombre d'offres diffusées"][i]
      
        nbr2=0
        for i in range(len(df)):
            if df["Année"][i]==2016:
                nbr2 = nbr2 + df["Nombre d'offres diffusées"][i]
       
        nbr3=0
        for i in range(len(df)):
            if df["Année"][i]==2017:
                nbr3 = nbr3 + df["Nombre d'offres diffusées"][i]
       
        nbr4=0
        for i in range(len(df)):
            if df["Année"][i]==2018:
                nbr4 = nbr4 + df["Nombre d'offres diffusées"][i]
       
        nbr5=0
        for i in range(len(df)):
            if df["Année"][i]==2019:
                nbr5 = nbr5 + df["Nombre d'offres diffusées"][i]
       
       
        nbr6=0
        for i in range(len(df)):
            if df["Année"][i]==2020:
                nbr6 = nbr6 + df["Nombre d'offres diffusées"][i]
       
        nbr7=0
        for i in range(len(df)):
            if df["Année"][i]==2021:
                nbr7 = nbr7 + df["Nombre d'offres diffusées"][i]


        x = np.array([nbr1,nbr2,nbr3,nbr4,nbr5,nbr6,nbr7])
        y = np.array([2015,2016,2017,2018,2019,2020,2021])
        
        self.ui.graphicsView.plot(y,x,pen=pg.mkPen(color=(154, 188, 195)))
        self.ui.graphicsView.setLabel('left', "Nombre d'offres")
        self.ui.graphicsView.showGrid(x=True, y=True)
        self.ui.graphicsView.setBackground('w')




    def plot_data_plus_recrute(self):
        
        y1 = np.array([1.9, 0.2, 3.5,12,0.7,11.2,4,11.4,8.7,6.9,11.7,0.2,11.8,7.9])
        #x = ["agriculture et peche", "art et façonnage", "banque et assurance","commerce et vente","communication media","construction et batiment","hotellerie et restaurarion","Industrie","installation et maintenance","sante","service a la personne et a la collectivité","spectacle","support a lentrepriser","trasport et logistique"]
        #self.ui.graphicsView = pg.plot()
        #y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14]

        

        bargraph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush = (168, 227, 215))
        self.ui.graphicsView_2.setLabel('left', 'kjlkk,n', 'v')



        self.ui.graphicsView_2.addItem(bargraph)
        self.ui.graphicsView_2.setLabel('left', 'Pourcentage (%)')
        self.ui.graphicsView_2.showGrid(x=True, y=True)
        self.ui.graphicsView_2.setBackground('w')


    def competences(self):
        df = pd.read_csv('fr-esr_dictionnaire_competences_referens_3.csv', error_bad_lines=False,sep=';')
        a = str(self.ui.comboBox_10.currentText())
        comp1=[]
        comp2=[]
        comp3=[]
        comp4=[]
        comp5=[]
        comp6=[]
        comp7=[]
        comp8=[]
        comp9=[]
        comp10=[]
        comp11=[]
        comp12=[]
        comp13=[]
        comp14=[]
        comp15=[]
        comp16=[]
        comp17=[]
        comp18=[]
        comp19=[]
        comp20=[]
        comp21=[]
        for i in range(len(df)):
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear()
               comp1.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp1)

            if df['Domaine'][i] == a:
               self.ui.listWidget.clear()
               comp2.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp2)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp3.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp3)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp4.append(df['Compétence'][i]) 
               self.ui.listWidget.addItems(comp4)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp5.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp5)  
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp6.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp6)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp7.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp7)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp8.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp8)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp9.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp9)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp10.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp10)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp11.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp11)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp12.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp12)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp13.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp13)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp14.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp14)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp15.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp15)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp16.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp16)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp17.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp17)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp18.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp18)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp19.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp19)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp20.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp20)
            if df['Domaine'][i] == a:
               self.ui.listWidget.clear() 
               comp21.append(df['Compétence'][i])
               self.ui.listWidget.addItems(comp21)
    
        
    def defini(self):
        df = pd.read_csv('fr-esr_dictionnaire_competences_referens_3.csv', error_bad_lines=False,sep=';')
        a = self.ui.listWidget.currentItem().text()
        for i in range(len(df)):
            if df['Compétence'][i] == a:
               self.ui.textBrowser_4.setText(df['Définition'][i])

    def formation(self):
        df = pd.read_csv('fr-esr-cartographie_formations_parcoursup.csv', error_bad_lines=False,sep=';',low_memory=False)
        l=list(df['nm'].unique())
        domaine=[]
        
        for i in range(len(l)):
            t=l[i].split('-')
            t=t[-1]
            domaine.append(t)
        self.ui.comboBox_11.addItems(domaine)

        
        l1=list(df['tf'].unique())
        Type=[]
        for i in range(len(l1)):
            t1=l1[i].split('-')
            t1=t1[-1]
            Type.append(t1)
        Type=set(Type)
        self.ui.comboBox_12.addItems(Type)


        l2=list(df['region'].unique())
        del l2[19]
        self.ui.comboBox_13.addItems(l2)


    

    def affiche_formation(self):
        df = pd.read_csv('fr-esr-cartographie_formations_parcoursup.csv', error_bad_lines=False,sep=';',low_memory=False)

        a = str(self.ui.comboBox_11.currentText())
        print(a)
        b = str(self.ui.comboBox_12.currentText())
        print(b)
        c = str(self.ui.comboBox_13.currentText())
        print(c)

        nomf=[]
        nome=[]
        Type=[]
        lien=[]

        for i in range(len(df)):
            if str(a) in df['nm'][i]:
                if str(b) in df['tf'][i]: 
                    if str(c) in df['region'][i]: 
                        nomf.append(df['fl'][i])
                        nome.append(df["etab_nom"][i])
                        Type.append(df["tc"][i])
                        lien.append(df['fiche'][i])
        
        

        people=pd.DataFrame(list(zip(nomf, nome,Type,lien)),
               columns =['Nom long de la formation', "Nom de l'établissement","Types d'établissement",'Lien vers la fiche formation'])


        row=0
        self.ui.tableWidget.setRowCount(len(people))
        for person in range(len(people)):
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(people["Nom long de la formation"][person]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(people["Nom de l'établissement"][person]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(people["Types d'établissement"][person]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(people["Lien vers la fiche formation"][person]))
            row=row+1
    

    def browsepdf(self):
        
        #### importer le nom du fichier pdf #########
        fname=QFileDialog.getOpenFileName(self, 'Open file','D:','(*.pdf)')
        self.ui.filename.setText(fname[0])
        name = self.ui.filename.text()
        print(name)
        myText = open(r'lien.txt','w')
        myText.write(name)
        myText.close()
        #####################################################
        
        ### convertir pdf en images  #########
        images = convert_from_path(name, size=(300, 450))
        for i in range(len(images)):
            images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        ####################################################

        ### afficher l'image du pdf
        self.ui.label_51.setPixmap(QtGui.QPixmap("page0.jpg"))
        ####################################################
        ###Q lecture du dictionnaire des compétences
        with open('competence.txt','r',encoding='latin-1') as f:
             listl=[]
             for line in f:
                 listl.append(line)

        # enlever les lignes qui sont vides
        without_empty_strings = []
        for string in listl:
            if (len(string) > 1):
                without_empty_strings.append(string)

        
        ## extraction du texte du pdf  ####
        l=[]
        pdf = pdfplumber.open(name)
        txt = ''
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            txt = txt + single_page_text
            l = txt.split(',')

        # enlever les espaces en début de la phrase
        for i in range(len(l)):
            l[i]=l[i].lstrip()

        ## chercher les compétences présentes dans le cv en se basant sur le dictionaire
        com=[]
        for i in without_empty_strings:
            for j in l:
                if  i in j :
                    com.append(i)
            
        #liste = list(txt.split('\n'))
        #self.ui.listWidget_2.addItems(com)
        ####################################################
        
       
        #####################################################
        self.ui.tableWidget_5.setColumnCount(3)  
        self.ui.tableWidget_5.setRowCount(len(com)) 
        for i in range(len(com)):
            self.ui.tableWidget_5.setItem(i,1, QTableWidgetItem(com[i]))
            ### pour la pondération il faut réflichir à une façon de le faire, par défaut le niveau et max cad (3)
            self.ui.tableWidget_5.setItem(i,2, QTableWidgetItem('3'))
            ### pour le métier il faudra un dicrionnaire de métiers pour l'extraire du cv pour mon exemple je vais le mettre manuellement
            #self.ui.tableWidget_5.setItem(0,0, QTableWidgetItem('Data  Scientist'))
            

        

        

        



        
       
        
    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################
    #######################################################################



    #######################################################################
    # Update restore button icon on msximizing or minimizing window
    #######################################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            #self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            #self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/minimize-2.svg"))

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  

