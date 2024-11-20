import pygame
from pygame.locals import *
from Frontend.Team import Team
from Frontend.images import *
def load_data():
    Liv = Team("Liv2.PNG", "Anfield14.PNG", "YNWA.mp3", "ManU.PNG", 0, 0, 0, 500)
    ManU = Team("ManU.PNG", "OldTrafford2.PNG", "GloryManU.mp3", "ManCity2.PNG", 0, 0, 0, 500)
    Atl = Team("Atleti4.PNG", "Wanda2.PNG", "AtletiSong.mp3", "Real4.PNG", 0, 0, 0, 500)
    Rma = Team("Real4.PNG", "Santiago3.PNG", "HalaMadridSong.mp3", "Fcb2.PNG", 0, 0, 0, 500)
    Fcb = Team("Fcb2.PNG", "CampNou3.PNG", "BarcaSong.mp3", "Real4.PNG", 0, 0, 0, 500)
    Val = Team("Valencia2.PNG", "Mestalla4.PNG", "ValenciaSong.mp3", "Atleti4.PNG", 0, 0, 0, 500)
    Int = Team("Inter3.PNG", "Meazza3.PNG", "InterSong.mp3", "Milan4.PNG", 0, 0, 0, 500)
    Mil = Team("Milan4.PNG", "SanSiro3.PNG", "AcMilanSong.mp3", "Inter3.PNG", 0, 0, 0, 500)
    Juv = Team("Juve2.PNG", "JuveStadium2.PNG", "JuveSong.mp3", "Inter3.PNG", 0, 0, 0, 500)
    Rom = Team("Roma2.PNG", "Olympico2.PNG", "RomaSong.mp3", "Lazio2.PNG", 0, 0, 0, 500)
    Laz = Team("Lazio2.PNG", "Olympico2.PNG", "LazioSong.mp3", "Roma2.PNG", 0, 0, 0, 500)
    Ars = Team("Arsenal2.PNG", "Emirates3.PNG", "ArsenalSong.mp3", "Tottenham2.PNG", 0, 0, 0, 500)
    Che = Team("Chelsea2.PNG", "StamfordBridge2.PNG", "ChelseaSong.mp3", "Arsenal2.PNG", 0, 0, 0, 500)
    City = Team("ManCity2.PNG", "Ettihad2.PNG", "CitySong.mp3", "ManU.PNG", 0, 0, 0, 500)
    Tot = Team("Tottenham2.PNG", "Spurs2.PNG", "SpursSong.mp3", "Arsenal2.PNG", 0, 0, 0, 500)
    Bay = Team("Bayern2.PNG", "Allianz2.PNG", "BayernSong.mp3", "BVB2.PNG", 0, 0, 0, 500)
    Bvb = Team("BVB2.PNG", "Signal3.PNG", "BVBSong.mp3", "Bayern2.PNG", 0, 0, 0, 500)
    Ol = Team("OL2.PNG", "Groupama3.PNG", "OLSong.mp3", "Marseille2.PNG", 0, 0, 0, 500)
    Om = Team("Marseille2.PNG", "Velodrome2.PNG", "OMSong.mp3", "OL2.PNG", 0, 0, 0, 500)
    Psg = Team("PSG2.PNG", "Parc2.PNG", "PsgSong.mp3", "Marseille2.PNG", 0, 0, 0, 500)

    teams = [Liv, ManU, Atl, Rma, Fcb, Val, Int, Mil, Juv, Rom, Laz, Ars, Che, City, Tot, Bay, Bvb, Ol, Om, Psg]
    BACKGROUND = pygame.image.load("UCL2.PNG")
    CUP = pygame.image.load("Cup2.PNG")

    return teams, BACKGROUND, CUP



High_score_file = "High_score.txt"
with open(High_score_file, 'r', encoding='UTF-8') as file:
    HIGH_SCORE = int(file.readline())

player_name_file = "Name.txt"
with open(player_name_file, 'r', encoding='UTF-8') as file:
    user_text = file.readline()


