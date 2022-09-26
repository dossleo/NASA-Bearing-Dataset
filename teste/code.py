from statistics import *
import pandas as pd
import glob
import numpy as np
import os


class Features_Extraction():
    def __init__(self,path):
        self.all_files = glob.glob(path + "\*")

    def time_features(self):
        
        self.lista = []
        for filename in self.all_files:

            self.dataset=pd.read_csv(filename, sep='\t',header=None)

            self.num_colunas = len(self.dataset.columns)

            self.df_bearing=np.array(self.dataset.iloc[:,1])

            #self.media = mean(self.df_bearing)
            #self.maximo = max(self.df_bearing)
            self.minimo = min(self.df_bearing)

            self.lista.append(self.minimo)

            #print(self.maximo)
            #print(self.minimo)
            #print(self.media)

        return self.lista

    def frequency_features(self):
        #Extrair informações da fft nas seguintes frequências:
            # rpm, pista interna, pista externa, rolo, gaiola
            # em cada uma dessas frequências, extrair a amplitude, rms, mean, max, min, curtose, impulsividade, numa janela temporal adequada
            # testar extrair amplitude crua vs extrair amplitude normalizada
        pass





