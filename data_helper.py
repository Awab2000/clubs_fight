import pygame
from pygame.locals import *
from Frontend.Team import Team
def load_data():
    Liv = Team("Frontend/images/Liv2.PNG", "Frontend/images/Anfield14.PNG", "Frontend/sounds/YNWA.mp3", "Frontend/images/ManU.PNG", 0, 0, 0, 500)
    ManU = Team("Frontend/images/ManU.PNG", "Frontend/images/OldTrafford2.PNG", "Frontend/sounds/GloryManU.mp3", "Frontend/images/ManCity2.PNG", 0, 0, 0, 500)
    Atl = Team("Frontend/images/Atleti4.PNG", "Frontend/images/Wanda2.PNG", "Frontend/sounds/AtletiSong.mp3", "Frontend/images/Real4.PNG", 0, 0, 0, 500)
    Rma = Team("Frontend/images/Real4.PNG", "Frontend/images/Santiago3.PNG", "Frontend/sounds/HalaMadridSong.mp3", "Frontend/images/Fcb2.PNG", 0, 0, 0, 500)
    Fcb = Team("Frontend/images/Fcb2.PNG", "Frontend/images/CampNou3.PNG", "Frontend/sounds/BarcaSong.mp3", "Frontend/images/Real4.PNG", 0, 0, 0, 500)
    Val = Team("Frontend/images/Valencia2.PNG", "Frontend/images/Mestalla4.PNG", "Frontend/sounds/ValenciaSong.mp3", "Frontend/images/Atleti4.PNG", 0, 0, 0, 500)
    Int = Team("Frontend/images/Inter3.PNG", "Frontend/images/Meazza3.PNG", "Frontend/sounds/InterSong.mp3", "Frontend/images/Milan4.PNG", 0, 0, 0, 500)
    Mil = Team("Frontend/images/Milan4.PNG", "Frontend/images/SanSiro3.PNG", "Frontend/sounds/AcMilanSong.mp3", "Frontend/images/Inter3.PNG", 0, 0, 0, 500)
    Juv = Team("Frontend/images/Juve2.PNG", "Frontend/images/JuveStadium2.PNG", "Frontend/sounds/JuveSong.mp3", "Frontend/images/Inter3.PNG", 0, 0, 0, 500)
    Rom = Team("Frontend/images/Roma2.PNG", "Frontend/images/Olympico2.PNG", "Frontend/sounds/RomaSong.mp3", "Frontend/images/Lazio2.PNG", 0, 0, 0, 500)
    Laz = Team("Frontend/images/Lazio2.PNG", "Frontend/images/Olympico2.PNG", "Frontend/sounds/LazioSong.mp3", "Frontend/images/Roma2.PNG", 0, 0, 0, 500)
    Ars = Team("Frontend/images/Arsenal2.PNG", "Frontend/images/Emirates3.PNG", "Frontend/sounds/ArsenalSong.mp3", "Frontend/images/Tottenham2.PNG", 0, 0, 0, 500)
    Che = Team("Frontend/images/Chelsea2.PNG", "Frontend/images/StamfordBridge2.PNG", "Frontend/sounds/ChelseaSong.mp3", "Frontend/images/Arsenal2.PNG", 0, 0, 0, 500)
    City = Team("Frontend/images/ManCity2.PNG", "Frontend/images/Ettihad2.PNG", "Frontend/sounds/CitySong.mp3", "Frontend/images/ManU.PNG", 0, 0, 0, 500)
    Tot = Team("Frontend/images/Tottenham2.PNG", "Frontend/images/Spurs2.PNG", "Frontend/sounds/SpursSong.mp3", "Frontend/images/Arsenal2.PNG", 0, 0, 0, 500)
    Bay = Team("Frontend/images/Bayern2.PNG", "Frontend/images/Allianz2.PNG", "Frontend/sounds/BayernSong.mp3", "Frontend/images/BVB2.PNG", 0, 0, 0, 500)
    Bvb = Team("Frontend/images/BVB2.PNG", "Frontend/images/Signal3.PNG", "Frontend/sounds/BVBSong.mp3", "Frontend/images/Bayern2.PNG", 0, 0, 0, 500)
    Ol = Team("Frontend/images/OL2.PNG", "Frontend/images/Groupama3.PNG", "Frontend/sounds/OLSong.mp3", "Frontend/images/Marseille2.PNG", 0, 0, 0, 500)
    Om = Team("Frontend/images/Marseille2.PNG", "Frontend/images/Velodrome2.PNG", "Frontend/sounds/OMSong.mp3", "Frontend/images/OL2.PNG", 0, 0, 0, 500)
    Psg = Team("Frontend/images/PSG2.PNG", "Frontend/images/Parc2.PNG", "Frontend/sounds/PsgSong.mp3", "Frontend/images/Marseille2.PNG", 0, 0, 0, 500)

    teams = [Liv, ManU, Atl, Rma, Fcb, Val, Int, Mil, Juv, Rom, Laz, Ars, Che, City, Tot, Bay, Bvb, Ol, Om, Psg]
    BACKGROUND = pygame.image.load("Frontend/images/UCL2.PNG")
    CUP = pygame.image.load("Frontend/images/Cup2.PNG")

    return teams, BACKGROUND, CUP
