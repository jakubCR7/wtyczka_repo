# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyka2Dialog
                                 A QGIS plugin
 Wtyczka zalicza drugi projekt
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-06-04
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Jakub i Adam
        email                : kubafajfer59@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import numpy as np
from qgis.PyQt import uic
from qgis.utils import iface
from qgis.PyQt import QtWidgets
from qgis.core import QgsWkbTypes
from qgis.core import QgsMessageLog, Qgis
from qgis.core import QgsProject, QgsPointXY

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'zaliczka_dialog_base.ui'))

class wtyka2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(wtyka2Dialog, self).__init__(parent)
        self.setupUi(self)

        self.pbtnroznicaH.clicked.connect(self.roznicaH)


        self.pbpole.clicked.connect(self.pole)

        self.ha.stateChanged.connect(self.checkboxStateChanged)
        

        self.m2.stateChanged.connect(self.checkboxStateChanged)
        
        self.ar.stateChanged.connect(self.checkboxStateChanged)

    def checkboxStateChanged(self, state):
        pass
    def roznicaH(self):
        
        obiekt = self.layer.currentLayer()
        if obiekt is None:
            iface.messageBar().pushMessage("Różnica wysokosci", 'Nie wybrano aktywnej warstwy', level = Qgis.Warning)
            return
        
        obiekt2 = self.layer.currentLayer().selectedFeatures()
        if len(obiekt2) != 2:
            iface.messageBar().pushMessage("Różnica wysokosci", 'W celu obliczenia różnicy wysokosci wybierz 2 punkty.', level = Qgis.Warning)
            return
        
        if len(obiekt2) == 2:
            
            H1 = float(obiekt2[0]['wysokosc'])
            H2 = float(obiekt2[1]['wysokosc'])
            
            przewyzszenie = round(H2 - H1, 3)
            
            self.wynikroznicyh.setText(str(przewyzszenie) +'m')
            
            
        QgsMessageLog.logMessage('Różnica wysokości między punktami wynosi:' +str(przewyzszenie) +'m', level = Qgis.Success)
        
        iface.messageBar().pushMessage("Różnica wysokosci", 'Różnica wysokosci między punktami policzona.', level = Qgis.Success)
        
    def pole(self):
    
        obiekty = self.layer.currentLayer().selectedFeatures()
        punkty = []
        for o in obiekty:
            x = float(o.geometry().asPoint().x())
            y = float(o.geometry().asPoint().y())
            p = QgsPointXY(x, y)
            punkty.append(p)

        unit_ha = self.ha.isChecked()
        unit_m2 = self.m2.isChecked()
        unit_ar = self.ar.isChecked()
            
        if len(obiekty)<3:
            iface.messageBar().pushMessage("Pole powierzchni", 'W celu policzenia pola wybierz conajmniej 3 punkty.', level = Qgis.Warning)
            return
            
        if len(obiekty)>2:

            pole = 0
            dl = len(punkty)
            for e in range(dl):
                a = (e + 1) % dl
                pole += (punkty[a].x() * punkty[e].y() - punkty[e].x() * punkty[a].y())

            pole /= 2

            if unit_ha:
                pole = round(abs(pole) / 10000, 3)  # Konwersja do hektarów
                self.wynikpola.setText(str(pole) + ' ha')
            elif unit_m2:
                pole = round(abs(pole), 3)  # Pozostawienie w metrach kwadratowych
                self.wynikpola.setText(str(pole) + ' m²')
            elif unit_ar:
                pole = round(abs(pole) / 100, 3)  # Konwersja do arów
                self.wynikpola.setText(str(pole) + ' ar')
                pole = round(abs(pole/10000), 3)

            QgsMessageLog.logMessage('Pole powierzchni między punktami to: {pole} ha', level = Qgis.Success)
        
            iface.messageBar().pushMessage("Pole powierzchni", 'Pole powierzchnivpoliczone', level = Qgis.Success)
            