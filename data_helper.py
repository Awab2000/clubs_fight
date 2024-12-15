import pygame
from pygame.locals import *
from Frontend.Team import Team
def load_data():
    Liv = Team("Frontend/images/Liv2.PNG", "Frontend/images/Anfield14.PNG", "Frontend/sounds/Liverpool.mp3", "Frontend/images/ManU.PNG", 0, 0, 0, 500)
    ManU = Team("Frontend/images/ManU.PNG", "Frontend/images/OldTrafford2.PNG", "Frontend/sounds/Manchester United.mp3", "Frontend/images/ManCity2.PNG", 0, 0, 0, 500)
    Atl = Team("Frontend/images/Atleti4.PNG", "Frontend/images/Wanda2.PNG", "Frontend/sounds/Atletico Madrid.mp3", "Frontend/images/Real4.PNG", 0, 0, 0, 500)
    Rma = Team("Frontend/images/Real4.PNG", "Frontend/images/Santiago3.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Fcb2.PNG", 0, 0, 0, 500)
    Fcb = Team("Frontend/images/Fcb2.PNG", "Frontend/images/CampNou3.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Real4.PNG", 0, 0, 0, 500)
    Val = Team("Frontend/images/Valencia2.PNG", "Frontend/images/Mestalla4.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Atleti4.PNG", 0, 0, 0, 500)
    Int = Team("Frontend/images/Inter3.PNG", "Frontend/images/Meazza3.PNG", "Frontend/sounds/Internazionale.mp3", "Frontend/images/Milan4.PNG", 0, 0, 0, 500)
    Mil = Team("Frontend/images/Milan4.PNG", "Frontend/images/SanSiro3.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Inter3.PNG", 0, 0, 0, 500)
    Juv = Team("Frontend/images/Juve2.PNG", "Frontend/images/JuveStadium2.PNG", "Frontend/sounds/JUVENTUS.mp3", "Frontend/images/Inter3.PNG", 0, 0, 0, 500)
    Rom = Team("Frontend/images/Roma2.PNG", "Frontend/images/Olympico3.PNG", "Frontend/sounds/Roma.mp3", "Frontend/images/Lazio2.PNG", 0, 0, 0, 500)
    Laz = Team("Frontend/images/Lazio2.PNG", "Frontend/images/Olympico2.PNG", "Frontend/sounds/Lazio.mp3", "Frontend/images/Roma2.PNG", 0, 0, 0, 500)
    Ars = Team("Frontend/images/Arsenal2.PNG", "Frontend/images/Emirates3.PNG", "Frontend/sounds/Arsenal.mp3", "Frontend/images/Tottenham2.PNG", 0, 0, 0, 500)
    Che = Team("Frontend/images/Chelsea2.PNG", "Frontend/images/StamfordBridge2.PNG", "Frontend/sounds/Chelsea.mp3", "Frontend/images/Arsenal2.PNG", 0, 0, 0, 500)
    City = Team("Frontend/images/ManCity2.PNG", "Frontend/images/Ettihad2.PNG", "Frontend/sounds/Man city.mp3", "Frontend/images/ManU.PNG", 0, 0, 0, 500)
    Tot = Team("Frontend/images/Tottenham2.PNG", "Frontend/images/Spurs2.PNG", "Frontend/sounds/TOTTENHAM HOTSPUR.mp3", "Frontend/images/Arsenal2.PNG", 0, 0, 0, 500)
    Bay = Team("Frontend/images/Bayern2.PNG", "Frontend/images/Allianz2.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/BVB2.PNG", 0, 0, 0, 500)
    Bvb = Team("Frontend/images/BVB2.PNG", "Frontend/images/Signal3.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Bayern2.PNG", 0, 0, 0, 500)
    Ol = Team("Frontend/images/OL2.PNG", "Frontend/images/Groupama3.PNG", "Frontend/sounds/Lyon.mp3", "Frontend/images/Marseille2.PNG", 0, 0, 0, 500)
    Om = Team("Frontend/images/Marseille2.PNG", "Frontend/images/Velodrome2.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/OL2.PNG", 0, 0, 0, 500)
    Psg = Team("Frontend/images/PSG2.PNG", "Frontend/images/Parc2.PNG", "Frontend/sounds/Crowd Sound.mp3", "Frontend/images/Marseille2.PNG", 0, 0, 0, 500)
    Hilal_sudani = Team("Frontend/images/Al-Hilal Al-Sudani.PNG", "Frontend/images/Blue_Jawhara.PNG", "Frontend/sounds/Crowd Sound.mp3",
               "Frontend/images/Al-Merrikh.PNG", 0, 0, 0, 500)
    Al_merrikh = Team("Frontend/images/Al-Merrikh.PNG", "Frontend/images/Al-Qal3a Al-Hamraa.PNG",
                        "Frontend/sounds/Crowd Sound.mp3",
                        "Frontend/images/Al-Hilal Al-Sudani.PNG", 0, 0, 0, 500)
    Al_ahli = Team("Frontend/images/Al-Ahli.PNG", "Frontend/images/Al-Jawhara_Ahli.PNG",
                      "Frontend/sounds/Al-Ahli.mp3",
                      "Frontend/images/Ittihad.PNG", 0, 0, 0, 500)
    Ittihad = Team("Frontend/images/Ittihad.PNG", "Frontend/images/Al-Jawhara_itti.PNG",
                   "Frontend/sounds/Al-ittihad2.mp3",
                   "Frontend/images/Al-Ahli.PNG", 0, 0, 0, 500)
    Al_nassr = Team("Frontend/images/Al_Nassr.PNG", "Frontend/images/Al-Awwal Park.PNG",
                   "Frontend/sounds/Al-Nassr.mp3",
                   "Frontend/images/Al-Hilal Saudi.PNG", 0, 0, 0, 500)
    Hilal_saudi = Team("Frontend/images/Al-Hilal Saudi.PNG", "Frontend/images/Kingdom_Arena.PNG",
                    "Frontend/sounds/Al-Hilal Saudi.mp3",
                    "Frontend/images/Al_Nassr.PNG", 0, 0, 0, 500)

    teams = [Liv, ManU, Atl, Rma, Fcb, Val, Int, Mil, Juv, Rom, Laz, Ars, Che, City, Tot, Bay, Bvb, Ol, Om, Psg, Hilal_sudani, Al_merrikh, Al_ahli, Ittihad, Al_nassr, Hilal_saudi]
    BACKGROUND = pygame.image.load("Frontend/images/UCL2.PNG")
    CUP = pygame.image.load("Frontend/images/Cup2.PNG")

    return teams, BACKGROUND, CUP


def get_logos():
    return ["Frontend/images/Liv2.PNG", "Frontend/images/ManU.PNG", "Frontend/images/Atleti4.PNG", "Frontend/images/Real4.PNG",
            "Frontend/images/Fcb2.PNG", "Frontend/images/Valencia2.PNG", "Frontend/images/Inter3.PNG", "Frontend/images/Milan4.PNG",
            "Frontend/images/Juve2.PNG", "Frontend/images/Roma2.PNG", "Frontend/images/Lazio2.PNG", "Frontend/images/Arsenal2.PNG",
            "Frontend/images/Chelsea2.PNG", "Frontend/images/ManCity2.PNG", "Frontend/images/Tottenham2.PNG", "Frontend/images/Bayern2.PNG",
            "Frontend/images/BVB2.PNG", "Frontend/images/OL2.PNG", "Frontend/images/Marseille2.PNG", "Frontend/images/PSG2.PNG",
            "Frontend/images/Al-Hilal Al-Sudani.PNG","Frontend/images/Al-Merrikh.PNG","Frontend/images/Al-Ahli.PNG",
            "Frontend/images/Ittihad.PNG", "Frontend/images/Al_Nassr.PNG", "Frontend/images/Al-Hilal Saudi.PNG",
              ]

def get_small_stadiums():
    return ["Frontend/images/Anfield14_small.PNG", "Frontend/images/OldTrafford2_small.PNG", "Frontend/images/Wanda2_small.PNG",
            "Frontend/images/Santiago3_small.PNG",
            "Frontend/images/CampNou3_small.PNG", "Frontend/images/Mestalla4_small.PNG", "Frontend/images/Parc2_small.PNG",
            "Frontend/images/SanSiro3_small.PNG",
            "Frontend/images/JuveStadium2_small.PNG", "Frontend/images/Groupama3_small.PNG", "Frontend/images/Olympico3_small.PNG",
            "Frontend/images/Emirates3_small.PNG",
            "Frontend/images/StamfordBridge2_small.PNG", "Frontend/images/Ettihad2_small.PNG", "Frontend/images/Spurs2_small.PNG",
            "Frontend/images/Allianz2_small.PNG",
            "Frontend/images/Signal3_small.PNG", "Frontend/images/Olympico2_small.PNG", "Frontend/images/Velodrome2_small.PNG",
            "Frontend/images/Meazza3_small.PNG", "Frontend/images/Kingdom_Arena_small.PNG", "Frontend/images/Al-Awwal Park_small.PNG",
            "Frontend/images/Al-Jawhara_itti_small.PNG", "Frontend/images/Al-Jawhara_Ahli_small.PNG", "Frontend/images/Al-Qal3a Al-Hamraa_small.PNG",
            "Frontend/images/Blue_Jawhara_small.PNG"]


def get_stadiums():
    return ["Frontend/images/Anfield14.PNG", "Frontend/images/OldTrafford2.PNG", "Frontend/images/Wanda2.PNG",
            "Frontend/images/Santiago3.PNG",
            "Frontend/images/CampNou3.PNG", "Frontend/images/Mestalla4.PNG", "Frontend/images/Parc2.PNG",
            "Frontend/images/SanSiro3.PNG",
            "Frontend/images/JuveStadium2.PNG", "Frontend/images/Groupama3.PNG", "Frontend/images/Olympico3.PNG",
            "Frontend/images/Emirates3.PNG",
            "Frontend/images/StamfordBridge2.PNG", "Frontend/images/Ettihad2.PNG", "Frontend/images/Spurs2.PNG",
            "Frontend/images/Allianz2.PNG",
            "Frontend/images/Signal3.PNG", "Frontend/images/Olympico2.PNG", "Frontend/images/Velodrome2.PNG",
            "Frontend/images/Meazza3.PNG", "Frontend/images/Kingdom_Arena.PNG", "Frontend/images/Al-Awwal Park.PNG",
            "Frontend/images/Al-Jawhara_itti.PNG", "Frontend/images/Al-Jawhara_Ahli.PNG", "Frontend/images/Al-Qal3a Al-Hamraa.PNG",
            "Frontend/images/Blue_Jawhara.PNG"]