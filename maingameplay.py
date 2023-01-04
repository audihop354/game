import pygame, sys
import function
from pygame.locals import *
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT
import ioexcel, try_nam
from pygame import mixer

def tongket(rank, manvcuoc, manvdoan, tongtien, tiencuoc):
    global luotdau
    tiengiaodong = 0
    checkwin = 0
    checkdoan = 0
    if manvcuoc == rank[0][0]:
        tiengiaodong += tiencuoc
        checkwin = 1
    else:
        tiengiaodong -= tiencuoc
    if manvdoan == rank[0][0]:
        tiengiaodong += 50
        checkdoan = 1
    luotdau = (checkwin, tiengiaodong, manvcuoc)
    tongtien += tiengiaodong
    thongtin = rank + (checkwin, checkdoan, tongtien, tiengiaodong)
    return thongtin

def gameplaymain(screen,track,username, nvcuoc, tennv, tiencuoc, tile, modedua):
    tongtien = ioexcel.layTongtien(username)
    trave = try_nam.play(screen,track, nvcuoc,tile,modedua,0,tennv)
    thongtin = tongket(trave,nvcuoc,tongtien,tiencuoc)
    ioexcel.writefile(username, luotdau)
    ioexcel.cout(username)
    function.score(screen, username, thongtin,tennv,nvcuoc,tile)
    # game_over_situation(thongtin,tennv,nvcuoc,tile)