from math import *

class Bearing():

    def __init__(Self,rpm,D_pista_externa,D_pista_interna,n_rolos,phi = 0):

        Self.d_rolo = Self.D_pita_externa - Self.D_pista_interna
        Self.D_medio = (Self.D_pita_externa - Self.D_pista_interna)/2
        Self.freq_rot = Self.rpm*2*pi/60

    def freq_outer_race(Self):
        #Self.freq_rot = Self.rpm*2*pi/60
        return Self.freq_rot*Self.n_rolos*0.5*(1-(Self.d_rolo/Self.D_medio)*cos(Self.phi))

    def freq_innter_race(Self):
        #Self.freq_rot = Self.rpm*2*pi/60
        return Self.freq_rot*Self.n_rolos*0.5*(1+(Self.d_rolo/Self.D_medio)*cos(Self.phi))
    
    def freq_gaiola(Self):
        #Self.freq_rot = Self.rpm*2*pi/60
        return Self.freq_rot*0.5*(1-(Self.d_rolo/Self.D_medio)*cos(Self.phi))
    
    def freq_rolo(Self):
        #Self.freq_rot = Self.rpm*2*pi/60
        return (Self.D_medio/(2*Self.d_rolo))*(1-((Self.d_rolo/Self.D_medio)*cos(Self.phi))**2)

