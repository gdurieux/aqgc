from __future__ import absolute_import
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (November 18, 2022)
# Date: Fri 19 Apr 2024 15:40:09


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3, L.SSSS4 ],
             couplings = {(0,0):C.GC_696,(0,1):C.GC_28,(0,2):C.GC_28,(0,3):C.GC_28})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
             couplings = {(0,0):C.GC_618,(0,1):C.GC_618,(0,2):C.GC_618})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_4609})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1, L.UUV2 ],
             couplings = {(0,0):C.GC_691,(0,1):C.GC_691})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
             couplings = {(0,0):C.GC_691,(0,1):C.GC_693,(0,2):C.GC_693,(0,3):C.GC_691,(0,4):C.GC_691,(0,5):C.GC_693})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV146, L.VVVV178, L.VVVV210 ],
             couplings = {(1,0):C.GC_695,(0,0):C.GC_695,(2,1):C.GC_695,(0,1):C.GC_694,(2,2):C.GC_694,(1,2):C.GC_694})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1, L.FFS2 ],
             couplings = {(0,0):C.GC_7172,(0,1):C.GC_7172})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ta__plus__, P.ta__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1, L.FFS2 ],
             couplings = {(0,0):C.GC_7174,(0,1):C.GC_7174})

V_9 = Vertex(name = 'V_9',
             particles = [ P.t__tilde__, P.t, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1, L.FFS2 ],
             couplings = {(0,0):C.GC_7173,(0,1):C.GC_7173})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
              couplings = {(0,0):C.GC_71,(0,1):C.GC_70,(0,2):C.GC_70,(0,3):C.GC_71,(0,4):C.GC_71,(0,5):C.GC_70})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
              couplings = {(0,7):C.GC_20,(0,8):C.GC_19,(0,18):C.GC_20,(0,0):C.GC_6751,(0,22):C.GC_19,(0,19):C.GC_6751,(0,12):C.GC_1677,(0,11):C.GC_4,(0,20):C.GC_4,(0,10):C.GC_19,(0,21):C.GC_3,(0,6):C.GC_19,(0,1):C.GC_3,(0,9):C.GC_19,(0,17):C.GC_3,(0,14):C.GC_4,(0,5):C.GC_19,(0,23):C.GC_3,(0,15):C.GC_4,(0,3):C.GC_2,(0,4):C.GC_1,(0,2):C.GC_7,(0,13):C.GC_5363,(0,16):C.GC_8})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
              couplings = {(0,0):C.GC_6816,(0,9):C.GC_6816,(0,3):C.GC_544,(0,10):C.GC_544,(0,11):C.GC_543,(0,1):C.GC_543,(0,8):C.GC_543,(0,5):C.GC_544,(0,12):C.GC_543,(0,6):C.GC_544,(0,2):C.GC_450,(0,4):C.GC_5404,(0,7):C.GC_451})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_4762})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV111, L.VVVV112, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV124, L.VVVV125, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV144, L.VVVV145, L.VVVV146, L.VVVV147, L.VVVV15, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV16, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV178, L.VVVV179, L.VVVV18, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV190, L.VVVV197, L.VVVV198, L.VVVV2, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV21, L.VVVV210, L.VVVV211, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV49, L.VVVV50, L.VVVV52, L.VVVV53, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV58, L.VVVV59, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV81, L.VVVV89, L.VVVV90, L.VVVV91, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
              couplings = {(0,75):C.GC_6844,(0,81):C.GC_6845,(0,0):C.GC_6847,(0,56):C.GC_6846,(0,83):C.GC_3870,(0,84):C.GC_3856,(0,80):C.GC_3874,(0,82):C.GC_3874,(0,87):C.GC_3872,(0,88):C.GC_3047,(0,85):C.GC_3049,(0,86):C.GC_3049,(0,89):C.GC_3856,(0,90):C.GC_3879,(0,91):C.GC_3878,(0,92):C.GC_3047,(0,93):C.GC_3878,(0,94):C.GC_3879,(0,46):C.GC_3874,(0,52):C.GC_3049,(0,21):C.GC_3881,(0,28):C.GC_4279,(0,34):C.GC_4275,(0,72):C.GC_3874,(0,73):C.GC_3049,(0,64):C.GC_4279,(0,70):C.GC_3881,(0,71):C.GC_4275,(0,74):C.GC_4275,(0,76):C.GC_4275,(0,78):C.GC_3869,(0,79):C.GC_3871,(0,77):C.GC_3877,(0,95):C.GC_6848,(0,96):C.GC_6848,(0,107):C.GC_6847,(0,106):C.GC_6850,(0,4):C.GC_6846,(0,3):C.GC_6850,(0,15):C.GC_6847,(0,14):C.GC_6850,(0,26):C.GC_149,(0,33):C.GC_6846,(0,32):C.GC_6850,(0,44):C.GC_149,(0,51):C.GC_6836,(0,53):C.GC_6838,(0,50):C.GC_6842,(0,65):C.GC_150,(0,104):C.GC_3872,(0,105):C.GC_3870,(0,97):C.GC_3876,(0,108):C.GC_4274,(0,7):C.GC_4274,(0,16):C.GC_4274,(0,27):C.GC_6848,(0,37):C.GC_4274,(0,45):C.GC_6848,(0,54):C.GC_4275,(0,57):C.GC_4275,(0,66):C.GC_6840,(0,98):C.GC_4274,(0,1):C.GC_3875,(0,2):C.GC_3048,(0,109):C.GC_3880,(0,5):C.GC_4278,(0,17):C.GC_4278,(0,35):C.GC_4279,(0,38):C.GC_4275,(0,58):C.GC_4274,(0,100):C.GC_4274,(0,111):C.GC_4278,(0,12):C.GC_3875,(0,13):C.GC_3048,(0,9):C.GC_3880,(0,19):C.GC_4279,(0,22):C.GC_4275,(0,39):C.GC_4278,(0,60):C.GC_4274,(0,99):C.GC_4274,(0,110):C.GC_4278,(0,6):C.GC_4279,(0,8):C.GC_4275,(0,24):C.GC_3875,(0,25):C.GC_3048,(0,18):C.GC_3880,(0,36):C.GC_4278,(0,55):C.GC_4274,(0,29):C.GC_3881,(0,47):C.GC_4279,(0,67):C.GC_4275,(0,101):C.GC_4274,(0,112):C.GC_4279,(0,113):C.GC_4275,(0,10):C.GC_4278,(0,20):C.GC_4278,(0,42):C.GC_3875,(0,43):C.GC_3048,(0,40):C.GC_3880,(0,59):C.GC_4274,(0,30):C.GC_4279,(0,48):C.GC_3881,(0,68):C.GC_4275,(0,102):C.GC_4275,(0,103):C.GC_4275,(0,114):C.GC_4274,(0,11):C.GC_4274,(0,23):C.GC_4274,(0,41):C.GC_4274,(0,62):C.GC_3871,(0,63):C.GC_3869,(0,61):C.GC_3876,(0,31):C.GC_4275,(0,49):C.GC_4275,(0,69):C.GC_3877})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV102, L.VVVV117, L.VVVV124, L.VVVV135, L.VVVV14, L.VVVV147, L.VVVV153, L.VVVV156, L.VVVV172, L.VVVV179, L.VVVV186, L.VVVV188, L.VVVV205, L.VVVV211, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV67, L.VVVV80, L.VVVV90 ],
              couplings = {(0,4):C.GC_4272,(0,15):C.GC_4272,(0,16):C.GC_4268,(0,17):C.GC_6892,(0,18):C.GC_6892,(0,20):C.GC_6894,(0,0):C.GC_6894,(0,2):C.GC_6894,(0,7):C.GC_6894,(0,11):C.GC_6891,(0,19):C.GC_4267,(0,5):C.GC_6892,(0,9):C.GC_6892,(0,13):C.GC_6889,(0,21):C.GC_4271,(0,1):C.GC_4271,(0,3):C.GC_4271,(0,6):C.GC_4272,(0,8):C.GC_4271,(0,10):C.GC_4272,(0,12):C.GC_4267,(0,14):C.GC_4268})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6 ],
              couplings = {(0,0):C.GC_2210,(0,1):C.GC_2209,(0,2):C.GC_2209,(0,3):C.GC_2210,(0,4):C.GC_2210,(0,5):C.GC_2209})

V_17 = Vertex(name = 'V_17',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV100, L.VVVV101, L.VVVV104, L.VVVV105, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV109, L.VVVV11, L.VVVV110, L.VVVV111, L.VVVV112, L.VVVV113, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV12, L.VVVV120, L.VVVV121, L.VVVV122, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV129, L.VVVV13, L.VVVV130, L.VVVV131, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV136, L.VVVV137, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV143, L.VVVV144, L.VVVV145, L.VVVV146, L.VVVV148, L.VVVV149, L.VVVV15, L.VVVV150, L.VVVV151, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV158, L.VVVV159, L.VVVV16, L.VVVV160, L.VVVV161, L.VVVV162, L.VVVV163, L.VVVV164, L.VVVV165, L.VVVV166, L.VVVV167, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV176, L.VVVV178, L.VVVV18, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV19, L.VVVV191, L.VVVV192, L.VVVV193, L.VVVV194, L.VVVV195, L.VVVV197, L.VVVV198, L.VVVV199, L.VVVV20, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV208, L.VVVV209, L.VVVV21, L.VVVV210, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV28, L.VVVV29, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV34, L.VVVV35, L.VVVV36, L.VVVV37, L.VVVV39, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV5, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV6, L.VVVV60, L.VVVV61, L.VVVV62, L.VVVV63, L.VVVV64, L.VVVV65, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV70, L.VVVV71, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV8, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV85, L.VVVV86, L.VVVV87, L.VVVV89, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97, L.VVVV99 ],
              couplings = {(0,169):C.GC_6747,(0,0):C.GC_6749,(0,9):C.GC_6747,(0,19):C.GC_6746,(0,133):C.GC_6747,(0,142):C.GC_6747,(0,152):C.GC_6749,(0,161):C.GC_6746,(0,119):C.GC_6748,(0,120):C.GC_6749,(0,121):C.GC_6748,(0,122):C.GC_6746,(0,125):C.GC_34,(0,126):C.GC_37,(0,127):C.GC_36,(0,123):C.GC_32,(0,124):C.GC_32,(0,130):C.GC_35,(0,131):C.GC_36,(0,132):C.GC_37,(0,128):C.GC_33,(0,129):C.GC_33,(0,134):C.GC_37,(0,135):C.GC_36,(0,136):C.GC_31,(0,137):C.GC_30,(0,138):C.GC_36,(0,139):C.GC_37,(0,140):C.GC_30,(0,141):C.GC_31,(0,27):C.GC_6748,(0,72):C.GC_32,(0,80):C.GC_33,(0,37):C.GC_39,(0,46):C.GC_666,(0,54):C.GC_674,(0,89):C.GC_6748,(0,110):C.GC_32,(0,111):C.GC_33,(0,99):C.GC_666,(0,108):C.GC_39,(0,109):C.GC_674,(0,112):C.GC_6749,(0,113):C.GC_6746,(0,114):C.GC_674,(0,115):C.GC_674,(0,117):C.GC_34,(0,118):C.GC_35,(0,116):C.GC_41,(0,145):C.GC_6748,(0,146):C.GC_6748,(0,143):C.GC_6743,(0,144):C.GC_6743,(0,153):C.GC_6747,(0,154):C.GC_6747,(0,147):C.GC_6743,(0,148):C.GC_6743,(0,165):C.GC_6747,(0,162):C.GC_6742,(0,163):C.GC_6745,(0,164):C.GC_6744,(0,172):C.GC_6746,(0,173):C.GC_5358,(0,178):C.GC_5359,(0,166):C.GC_6745,(0,167):C.GC_5361,(0,5):C.GC_6746,(0,6):C.GC_5358,(0,7):C.GC_5359,(0,3):C.GC_6745,(0,4):C.GC_5361,(0,22):C.GC_6747,(0,8):C.GC_6742,(0,10):C.GC_6745,(0,13):C.GC_6744,(0,26):C.GC_6747,(0,23):C.GC_6745,(0,24):C.GC_6742,(0,25):C.GC_6744,(0,33):C.GC_5358,(0,34):C.GC_6746,(0,40):C.GC_5359,(0,28):C.GC_5361,(0,29):C.GC_6745,(0,43):C.GC_1678,(0,55):C.GC_5358,(0,56):C.GC_6746,(0,57):C.GC_5359,(0,52):C.GC_5361,(0,53):C.GC_6745,(0,70):C.GC_6747,(0,58):C.GC_6745,(0,59):C.GC_6742,(0,62):C.GC_6744,(0,71):C.GC_1678,(0,83):C.GC_6746,(0,84):C.GC_6749,(0,81):C.GC_6743,(0,82):C.GC_6743,(0,97):C.GC_6746,(0,98):C.GC_6749,(0,85):C.GC_6743,(0,88):C.GC_6743,(0,100):C.GC_1679,(0,159):C.GC_35,(0,160):C.GC_34,(0,149):C.GC_40,(0,168):C.GC_673,(0,14):C.GC_673,(0,30):C.GC_673,(0,63):C.GC_673,(0,86):C.GC_674,(0,90):C.GC_674,(0,150):C.GC_673,(0,1):C.GC_33,(0,2):C.GC_32,(0,170):C.GC_38,(0,11):C.GC_665,(0,31):C.GC_665,(0,44):C.GC_6742,(0,60):C.GC_666,(0,64):C.GC_674,(0,73):C.GC_5360,(0,91):C.GC_673,(0,101):C.GC_6744,(0,155):C.GC_673,(0,174):C.GC_665,(0,20):C.GC_33,(0,21):C.GC_32,(0,16):C.GC_38,(0,35):C.GC_666,(0,38):C.GC_674,(0,47):C.GC_5360,(0,65):C.GC_665,(0,75):C.GC_6742,(0,93):C.GC_673,(0,103):C.GC_6744,(0,151):C.GC_673,(0,171):C.GC_665,(0,12):C.GC_666,(0,15):C.GC_674,(0,41):C.GC_33,(0,42):C.GC_32,(0,32):C.GC_38,(0,45):C.GC_5360,(0,61):C.GC_665,(0,74):C.GC_6742,(0,87):C.GC_673,(0,102):C.GC_6744,(0,49):C.GC_39,(0,77):C.GC_666,(0,105):C.GC_674,(0,156):C.GC_673,(0,175):C.GC_666,(0,176):C.GC_674,(0,17):C.GC_665,(0,36):C.GC_665,(0,48):C.GC_6742,(0,68):C.GC_33,(0,69):C.GC_32,(0,66):C.GC_38,(0,76):C.GC_5360,(0,92):C.GC_673,(0,104):C.GC_6744,(0,50):C.GC_666,(0,78):C.GC_39,(0,106):C.GC_674,(0,157):C.GC_674,(0,158):C.GC_674,(0,177):C.GC_673,(0,18):C.GC_673,(0,39):C.GC_673,(0,67):C.GC_673,(0,95):C.GC_35,(0,96):C.GC_34,(0,94):C.GC_40,(0,51):C.GC_674,(0,79):C.GC_674,(0,107):C.GC_41})

V_18 = Vertex(name = 'V_18',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV104, L.VVVV105, L.VVVV109, L.VVVV110, L.VVVV113, L.VVVV117, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV130, L.VVVV131, L.VVVV135, L.VVVV14, L.VVVV146, L.VVVV148, L.VVVV149, L.VVVV150, L.VVVV151, L.VVVV153, L.VVVV158, L.VVVV159, L.VVVV163, L.VVVV164, L.VVVV167, L.VVVV172, L.VVVV178, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV186, L.VVVV191, L.VVVV192, L.VVVV195, L.VVVV199, L.VVVV205, L.VVVV210, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV60, L.VVVV61, L.VVVV64, L.VVVV65, L.VVVV67, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV86, L.VVVV87, L.VVVV90 ],
              couplings = {(0,12):C.GC_659,(0,42):C.GC_659,(0,43):C.GC_661,(0,44):C.GC_6808,(0,45):C.GC_6808,(0,46):C.GC_6808,(0,47):C.GC_6808,(0,49):C.GC_5390,(0,50):C.GC_5389,(0,51):C.GC_6807,(0,52):C.GC_5389,(0,53):C.GC_5386,(0,0):C.GC_5389,(0,1):C.GC_5386,(0,2):C.GC_5390,(0,3):C.GC_5389,(0,4):C.GC_6807,(0,6):C.GC_5389,(0,7):C.GC_5390,(0,8):C.GC_6807,(0,9):C.GC_5386,(0,10):C.GC_5389,(0,13):C.GC_7164,(0,19):C.GC_5386,(0,20):C.GC_5389,(0,21):C.GC_5389,(0,22):C.GC_5390,(0,23):C.GC_6807,(0,25):C.GC_7164,(0,31):C.GC_6808,(0,32):C.GC_6808,(0,33):C.GC_6808,(0,34):C.GC_6808,(0,36):C.GC_5442,(0,48):C.GC_660,(0,54):C.GC_658,(0,14):C.GC_5390,(0,26):C.GC_5385,(0,37):C.GC_6807,(0,5):C.GC_658,(0,16):C.GC_5385,(0,28):C.GC_5390,(0,39):C.GC_6807,(0,11):C.GC_658,(0,15):C.GC_5385,(0,27):C.GC_5390,(0,38):C.GC_6807,(0,18):C.GC_659,(0,17):C.GC_5390,(0,24):C.GC_658,(0,29):C.GC_5385,(0,40):C.GC_6807,(0,30):C.GC_659,(0,35):C.GC_660,(0,41):C.GC_661})

V_19 = Vertex(name = 'V_19',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV146, L.VVVV178, L.VVVV210 ],
              couplings = {(0,0):C.GC_7165,(0,1):C.GC_7165,(0,2):C.GC_5443})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV106, L.VVVV109, L.VVVV111, L.VVVV112, L.VVVV113, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV124, L.VVVV125, L.VVVV126, L.VVVV129, L.VVVV130, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV136, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV143, L.VVVV144, L.VVVV145, L.VVVV146, L.VVVV147, L.VVVV148, L.VVVV15, L.VVVV150, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV158, L.VVVV16, L.VVVV160, L.VVVV163, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV176, L.VVVV178, L.VVVV179, L.VVVV18, L.VVVV180, L.VVVV182, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV191, L.VVVV193, L.VVVV195, L.VVVV197, L.VVVV198, L.VVVV2, L.VVVV20, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV208, L.VVVV21, L.VVVV210, L.VVVV211, L.VVVV212, L.VVVV214, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV34, L.VVVV35, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV51, L.VVVV53, L.VVVV54, L.VVVV56, L.VVVV58, L.VVVV59, L.VVVV6, L.VVVV60, L.VVVV62, L.VVVV64, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV70, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV81, L.VVVV82, L.VVVV84, L.VVVV86, L.VVVV89, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
              couplings = {(0,100):C.GC_6956,(0,108):C.GC_6953,(0,0):C.GC_6954,(0,76):C.GC_6951,(0,145):C.GC_6950,(0,1):C.GC_6955,(0,124):C.GC_6948,(0,131):C.GC_6954,(0,105):C.GC_6764,(0,106):C.GC_6763,(0,110):C.GC_2794,(0,111):C.GC_3306,(0,112):C.GC_3305,(0,107):C.GC_2794,(0,109):C.GC_3296,(0,115):C.GC_3302,(0,116):C.GC_3305,(0,117):C.GC_3306,(0,113):C.GC_3302,(0,114):C.GC_3298,(0,118):C.GC_2793,(0,119):C.GC_2793,(0,120):C.GC_3300,(0,121):C.GC_3300,(0,62):C.GC_3297,(0,70):C.GC_3299,(0,30):C.GC_3304,(0,39):C.GC_3813,(0,47):C.GC_3813,(0,77):C.GC_6692,(0,96):C.GC_3301,(0,97):C.GC_2795,(0,86):C.GC_3813,(0,94):C.GC_3308,(0,95):C.GC_3803,(0,98):C.GC_6691,(0,99):C.GC_3803,(0,101):C.GC_3813,(0,103):C.GC_3301,(0,104):C.GC_2795,(0,102):C.GC_3308,(0,122):C.GC_6940,(0,123):C.GC_6943,(0,126):C.GC_6952,(0,125):C.GC_6937,(0,132):C.GC_6761,(0,127):C.GC_6857,(0,140):C.GC_6946,(0,139):C.GC_6938,(0,141):C.GC_6939,(0,142):C.GC_6944,(0,148):C.GC_6762,(0,143):C.GC_6856,(0,5):C.GC_6949,(0,4):C.GC_6941,(0,7):C.GC_6947,(0,6):C.GC_6942,(0,8):C.GC_6855,(0,11):C.GC_6854,(0,20):C.GC_6954,(0,19):C.GC_6941,(0,22):C.GC_6948,(0,21):C.GC_6942,(0,27):C.GC_6852,(0,33):C.GC_6853,(0,23):C.GC_6859,(0,36):C.GC_2321,(0,45):C.GC_6951,(0,44):C.GC_6938,(0,48):C.GC_6758,(0,46):C.GC_6759,(0,59):C.GC_6689,(0,49):C.GC_6856,(0,60):C.GC_2320,(0,69):C.GC_6758,(0,68):C.GC_6759,(0,72):C.GC_6945,(0,71):C.GC_6937,(0,85):C.GC_6690,(0,73):C.GC_6857,(0,87):C.GC_2320,(0,137):C.GC_2795,(0,138):C.GC_3301,(0,128):C.GC_3307,(0,144):C.GC_3804,(0,12):C.GC_3814,(0,24):C.GC_3814,(0,37):C.GC_6940,(0,52):C.GC_3804,(0,61):C.GC_6943,(0,74):C.GC_3813,(0,78):C.GC_3803,(0,88):C.GC_6760,(0,129):C.GC_3804,(0,2):C.GC_2795,(0,3):C.GC_3301,(0,146):C.GC_3307,(0,9):C.GC_3814,(0,25):C.GC_3814,(0,38):C.GC_6939,(0,50):C.GC_3813,(0,53):C.GC_3803,(0,63):C.GC_6760,(0,79):C.GC_3804,(0,89):C.GC_6944,(0,133):C.GC_3814,(0,149):C.GC_3814,(0,17):C.GC_3299,(0,18):C.GC_3297,(0,14):C.GC_3303,(0,28):C.GC_3813,(0,31):C.GC_3813,(0,40):C.GC_6858,(0,54):C.GC_3814,(0,64):C.GC_6855,(0,81):C.GC_3814,(0,90):C.GC_6854,(0,130):C.GC_3814,(0,147):C.GC_3814,(0,10):C.GC_3813,(0,13):C.GC_3813,(0,34):C.GC_3298,(0,35):C.GC_3296,(0,26):C.GC_3303,(0,51):C.GC_3814,(0,75):C.GC_3814,(0,41):C.GC_3304,(0,65):C.GC_3813,(0,91):C.GC_3813,(0,134):C.GC_3804,(0,150):C.GC_3813,(0,151):C.GC_3803,(0,15):C.GC_3814,(0,29):C.GC_3814,(0,57):C.GC_3302,(0,58):C.GC_2794,(0,55):C.GC_3307,(0,80):C.GC_3804,(0,42):C.GC_3813,(0,66):C.GC_3308,(0,92):C.GC_3803,(0,135):C.GC_3813,(0,136):C.GC_3803,(0,152):C.GC_3804,(0,16):C.GC_3814,(0,32):C.GC_3814,(0,56):C.GC_3804,(0,83):C.GC_3302,(0,84):C.GC_2794,(0,82):C.GC_3307,(0,43):C.GC_3813,(0,67):C.GC_3803,(0,93):C.GC_3308})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV102, L.VVVV104, L.VVVV109, L.VVVV113, L.VVVV117, L.VVVV124, L.VVVV126, L.VVVV130, L.VVVV135, L.VVVV14, L.VVVV147, L.VVVV148, L.VVVV150, L.VVVV153, L.VVVV156, L.VVVV158, L.VVVV163, L.VVVV172, L.VVVV179, L.VVVV180, L.VVVV182, L.VVVV186, L.VVVV188, L.VVVV191, L.VVVV195, L.VVVV205, L.VVVV211, L.VVVV212, L.VVVV214, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV60, L.VVVV64, L.VVVV67, L.VVVV80, L.VVVV82, L.VVVV84, L.VVVV86, L.VVVV90 ],
              couplings = {(0,9):C.GC_3806,(0,30):C.GC_3809,(0,31):C.GC_3809,(0,32):C.GC_6995,(0,33):C.GC_6993,(0,34):C.GC_6994,(0,35):C.GC_6897,(0,37):C.GC_6994,(0,38):C.GC_6995,(0,39):C.GC_6993,(0,40):C.GC_6897,(0,0):C.GC_6992,(0,1):C.GC_6992,(0,2):C.GC_6896,(0,3):C.GC_6896,(0,5):C.GC_6992,(0,6):C.GC_6992,(0,7):C.GC_6886,(0,14):C.GC_6994,(0,15):C.GC_6802,(0,16):C.GC_6897,(0,22):C.GC_6802,(0,23):C.GC_6994,(0,24):C.GC_6897,(0,36):C.GC_3810,(0,10):C.GC_6995,(0,18):C.GC_6993,(0,26):C.GC_6803,(0,41):C.GC_3810,(0,11):C.GC_6995,(0,19):C.GC_6803,(0,27):C.GC_6993,(0,4):C.GC_3807,(0,12):C.GC_6887,(0,20):C.GC_6896,(0,28):C.GC_6896,(0,8):C.GC_3807,(0,13):C.GC_3806,(0,17):C.GC_3810,(0,21):C.GC_3809,(0,25):C.GC_3810,(0,29):C.GC_3809})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
              couplings = {(0,7):C.GC_2791,(0,8):C.GC_2791,(0,18):C.GC_2791,(0,0):C.GC_7028,(0,22):C.GC_2791,(0,19):C.GC_7028,(0,12):C.GC_4072,(0,11):C.GC_3819,(0,20):C.GC_3819,(0,10):C.GC_2792,(0,21):C.GC_3816,(0,6):C.GC_2792,(0,1):C.GC_3816,(0,9):C.GC_2791,(0,17):C.GC_3816,(0,14):C.GC_3819,(0,5):C.GC_2791,(0,23):C.GC_3816,(0,15):C.GC_3819,(0,3):C.GC_3823,(0,4):C.GC_3820,(0,2):C.GC_3824,(0,13):C.GC_7031,(0,16):C.GC_3827})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
              couplings = {(0,0):C.GC_7056,(0,9):C.GC_7056,(0,3):C.GC_4160,(0,10):C.GC_4160,(0,11):C.GC_4161,(0,1):C.GC_4161,(0,8):C.GC_4161,(0,5):C.GC_4160,(0,12):C.GC_4161,(0,6):C.GC_4160,(0,2):C.GC_4149,(0,4):C.GC_7063,(0,7):C.GC_4152})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_6458})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV105, L.VVVV106, L.VVVV108, L.VVVV109, L.VVVV11, L.VVVV110, L.VVVV111, L.VVVV112, L.VVVV113, L.VVVV114, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV12, L.VVVV120, L.VVVV121, L.VVVV122, L.VVVV123, L.VVVV124, L.VVVV125, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV129, L.VVVV13, L.VVVV130, L.VVVV131, L.VVVV132, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV137, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV142, L.VVVV143, L.VVVV144, L.VVVV145, L.VVVV146, L.VVVV147, L.VVVV148, L.VVVV149, L.VVVV15, L.VVVV150, L.VVVV151, L.VVVV152, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV158, L.VVVV159, L.VVVV16, L.VVVV161, L.VVVV162, L.VVVV163, L.VVVV164, L.VVVV165, L.VVVV166, L.VVVV167, L.VVVV168, L.VVVV169, L.VVVV17, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV176, L.VVVV177, L.VVVV178, L.VVVV179, L.VVVV18, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV184, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV190, L.VVVV191, L.VVVV192, L.VVVV193, L.VVVV194, L.VVVV195, L.VVVV196, L.VVVV197, L.VVVV198, L.VVVV199, L.VVVV2, L.VVVV20, L.VVVV200, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV208, L.VVVV209, L.VVVV21, L.VVVV210, L.VVVV211, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV216, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV24, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV28, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV34, L.VVVV35, L.VVVV36, L.VVVV37, L.VVVV38, L.VVVV39, L.VVVV4, L.VVVV40, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV49, L.VVVV5, L.VVVV50, L.VVVV52, L.VVVV53, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV58, L.VVVV59, L.VVVV6, L.VVVV60, L.VVVV61, L.VVVV62, L.VVVV63, L.VVVV64, L.VVVV65, L.VVVV66, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV70, L.VVVV71, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV76, L.VVVV77, L.VVVV78, L.VVVV79, L.VVVV8, L.VVVV80, L.VVVV81, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV85, L.VVVV86, L.VVVV87, L.VVVV88, L.VVVV89, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97, L.VVVV98, L.VVVV99 ],
              couplings = {(0,139):C.GC_7026,(0,150):C.GC_7026,(0,0):C.GC_7026,(0,108):C.GC_7026,(0,201):C.GC_6765,(0,1):C.GC_6767,(0,11):C.GC_6767,(0,22):C.GC_6768,(0,159):C.GC_6928,(0,168):C.GC_6925,(0,179):C.GC_6922,(0,190):C.GC_6926,(0,144):C.GC_6768,(0,145):C.GC_6767,(0,146):C.GC_6766,(0,147):C.GC_6768,(0,153):C.GC_3857,(0,154):C.GC_53,(0,148):C.GC_6847,(0,149):C.GC_54,(0,151):C.GC_6846,(0,152):C.GC_54,(0,157):C.GC_3858,(0,158):C.GC_3873,(0,155):C.GC_3866,(0,156):C.GC_3866,(0,160):C.GC_53,(0,161):C.GC_3864,(0,162):C.GC_3863,(0,163):C.GC_3873,(0,164):C.GC_3863,(0,165):C.GC_3864,(0,33):C.GC_6921,(0,75):C.GC_6844,(0,86):C.GC_54,(0,97):C.GC_3866,(0,43):C.GC_3868,(0,54):C.GC_4283,(0,65):C.GC_4290,(0,109):C.GC_6924,(0,133):C.GC_6845,(0,134):C.GC_54,(0,135):C.GC_3866,(0,120):C.GC_4283,(0,131):C.GC_3868,(0,132):C.GC_4290,(0,136):C.GC_6922,(0,137):C.GC_6926,(0,138):C.GC_4290,(0,140):C.GC_4290,(0,142):C.GC_3861,(0,143):C.GC_3862,(0,141):C.GC_3860,(0,166):C.GC_7021,(0,167):C.GC_7021,(0,171):C.GC_6768,(0,172):C.GC_6766,(0,169):C.GC_6936,(0,170):C.GC_6934,(0,180):C.GC_6765,(0,181):C.GC_6767,(0,186):C.GC_6839,(0,187):C.GC_6837,(0,173):C.GC_6936,(0,174):C.GC_6934,(0,175):C.GC_6841,(0,192):C.GC_7025,(0,191):C.GC_7022,(0,196):C.GC_6928,(0,193):C.GC_6932,(0,194):C.GC_6935,(0,195):C.GC_6929,(0,204):C.GC_6766,(0,209):C.GC_6847,(0,210):C.GC_6918,(0,197):C.GC_6933,(0,198):C.GC_6920,(0,199):C.GC_6849,(0,5):C.GC_7025,(0,4):C.GC_7022,(0,8):C.GC_6766,(0,9):C.GC_6918,(0,6):C.GC_6933,(0,7):C.GC_6920,(0,25):C.GC_6928,(0,26):C.GC_6847,(0,10):C.GC_6932,(0,12):C.GC_6935,(0,15):C.GC_6929,(0,16):C.GC_6849,(0,28):C.GC_7026,(0,27):C.GC_7022,(0,32):C.GC_6925,(0,29):C.GC_6933,(0,30):C.GC_6930,(0,31):C.GC_6931,(0,40):C.GC_6768,(0,46):C.GC_6846,(0,47):C.GC_6918,(0,34):C.GC_6920,(0,35):C.GC_6935,(0,36):C.GC_6849,(0,50):C.GC_1765,(0,62):C.GC_7026,(0,61):C.GC_7022,(0,66):C.GC_6768,(0,67):C.GC_6918,(0,63):C.GC_6920,(0,64):C.GC_6935,(0,82):C.GC_6925,(0,83):C.GC_6846,(0,68):C.GC_6933,(0,69):C.GC_6930,(0,72):C.GC_6931,(0,73):C.GC_6849,(0,84):C.GC_1765,(0,96):C.GC_7019,(0,98):C.GC_7020,(0,95):C.GC_7024,(0,101):C.GC_6927,(0,102):C.GC_6923,(0,99):C.GC_6936,(0,100):C.GC_6934,(0,118):C.GC_6927,(0,119):C.GC_6923,(0,103):C.GC_6936,(0,104):C.GC_6851,(0,107):C.GC_6934,(0,110):C.GC_6851,(0,121):C.GC_1766,(0,188):C.GC_3858,(0,189):C.GC_3857,(0,176):C.GC_3859,(0,200):C.GC_4289,(0,17):C.GC_4289,(0,37):C.GC_4289,(0,51):C.GC_7021,(0,74):C.GC_4289,(0,85):C.GC_7021,(0,105):C.GC_4290,(0,111):C.GC_4290,(0,122):C.GC_7023,(0,177):C.GC_4289,(0,2):C.GC_55,(0,3):C.GC_3865,(0,202):C.GC_3867,(0,13):C.GC_4282,(0,38):C.GC_4282,(0,52):C.GC_6932,(0,70):C.GC_4283,(0,76):C.GC_4290,(0,87):C.GC_6919,(0,112):C.GC_4289,(0,123):C.GC_6929,(0,182):C.GC_4289,(0,205):C.GC_4282,(0,23):C.GC_55,(0,24):C.GC_3865,(0,19):C.GC_3867,(0,41):C.GC_4283,(0,44):C.GC_4290,(0,55):C.GC_6919,(0,77):C.GC_4282,(0,89):C.GC_6932,(0,114):C.GC_4289,(0,125):C.GC_6929,(0,178):C.GC_4289,(0,203):C.GC_4282,(0,14):C.GC_4283,(0,18):C.GC_4290,(0,48):C.GC_55,(0,49):C.GC_3865,(0,39):C.GC_3867,(0,53):C.GC_6919,(0,71):C.GC_4282,(0,88):C.GC_6930,(0,106):C.GC_4289,(0,124):C.GC_6931,(0,58):C.GC_3868,(0,92):C.GC_4283,(0,128):C.GC_4290,(0,183):C.GC_4289,(0,206):C.GC_4283,(0,207):C.GC_4290,(0,20):C.GC_4282,(0,42):C.GC_4282,(0,56):C.GC_6930,(0,80):C.GC_55,(0,81):C.GC_3865,(0,78):C.GC_3867,(0,90):C.GC_6919,(0,113):C.GC_4289,(0,126):C.GC_6931,(0,59):C.GC_4283,(0,93):C.GC_3868,(0,129):C.GC_4290,(0,184):C.GC_4290,(0,185):C.GC_4290,(0,208):C.GC_4289,(0,21):C.GC_4289,(0,45):C.GC_4289,(0,57):C.GC_6851,(0,79):C.GC_4289,(0,91):C.GC_6851,(0,116):C.GC_3862,(0,117):C.GC_3861,(0,115):C.GC_3859,(0,127):C.GC_6843,(0,60):C.GC_4290,(0,94):C.GC_4290,(0,130):C.GC_3860})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV102, L.VVVV104, L.VVVV105, L.VVVV109, L.VVVV110, L.VVVV113, L.VVVV114, L.VVVV117, L.VVVV124, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV130, L.VVVV131, L.VVVV132, L.VVVV135, L.VVVV14, L.VVVV146, L.VVVV147, L.VVVV148, L.VVVV149, L.VVVV150, L.VVVV151, L.VVVV152, L.VVVV153, L.VVVV156, L.VVVV158, L.VVVV159, L.VVVV163, L.VVVV164, L.VVVV167, L.VVVV168, L.VVVV172, L.VVVV178, L.VVVV179, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV184, L.VVVV186, L.VVVV188, L.VVVV191, L.VVVV192, L.VVVV195, L.VVVV196, L.VVVV199, L.VVVV200, L.VVVV205, L.VVVV210, L.VVVV211, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV216, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV60, L.VVVV61, L.VVVV64, L.VVVV65, L.VVVV66, L.VVVV67, L.VVVV80, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV86, L.VVVV87, L.VVVV88, L.VVVV90 ],
              couplings = {(0,16):C.GC_4287,(0,57):C.GC_4287,(0,58):C.GC_4285,(0,59):C.GC_7052,(0,60):C.GC_7052,(0,61):C.GC_6990,(0,62):C.GC_6990,(0,63):C.GC_6990,(0,64):C.GC_6990,(0,65):C.GC_6888,(0,67):C.GC_7053,(0,68):C.GC_6988,(0,69):C.GC_6991,(0,70):C.GC_6989,(0,71):C.GC_6991,(0,72):C.GC_6987,(0,73):C.GC_6893,(0,0):C.GC_7053,(0,1):C.GC_6991,(0,2):C.GC_6987,(0,3):C.GC_6988,(0,4):C.GC_6991,(0,5):C.GC_6989,(0,6):C.GC_6893,(0,8):C.GC_7053,(0,9):C.GC_6991,(0,10):C.GC_6988,(0,11):C.GC_6989,(0,12):C.GC_6987,(0,13):C.GC_6991,(0,14):C.GC_6893,(0,17):C.GC_7166,(0,25):C.GC_7053,(0,26):C.GC_6987,(0,27):C.GC_6991,(0,28):C.GC_6991,(0,29):C.GC_6988,(0,30):C.GC_6989,(0,31):C.GC_6893,(0,33):C.GC_7166,(0,41):C.GC_7049,(0,42):C.GC_6990,(0,43):C.GC_6990,(0,44):C.GC_6990,(0,45):C.GC_6895,(0,46):C.GC_6990,(0,47):C.GC_6895,(0,49):C.GC_7167,(0,66):C.GC_4284,(0,18):C.GC_7052,(0,34):C.GC_7052,(0,50):C.GC_7048,(0,74):C.GC_4286,(0,19):C.GC_6988,(0,35):C.GC_6986,(0,51):C.GC_6989,(0,7):C.GC_4286,(0,21):C.GC_6986,(0,37):C.GC_6988,(0,53):C.GC_6989,(0,15):C.GC_4286,(0,20):C.GC_6986,(0,36):C.GC_6988,(0,52):C.GC_6989,(0,24):C.GC_4287,(0,22):C.GC_6988,(0,32):C.GC_4286,(0,38):C.GC_6986,(0,54):C.GC_6989,(0,40):C.GC_4287,(0,23):C.GC_6895,(0,39):C.GC_6895,(0,48):C.GC_4284,(0,55):C.GC_6890,(0,56):C.GC_4285})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV146, L.VVVV178, L.VVVV210 ],
              couplings = {(0,0):C.GC_7169,(0,1):C.GC_7169,(0,2):C.GC_7168})

V_28 = Vertex(name = 'V_28',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_70})

V_29 = Vertex(name = 'V_29',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_70})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_70})

V_31 = Vertex(name = 'V_31',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_69})

V_32 = Vertex(name = 'V_32',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_69})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_69})

V_34 = Vertex(name = 'V_34',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_68})

V_35 = Vertex(name = 'V_35',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_68})

V_36 = Vertex(name = 'V_36',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_68})

V_37 = Vertex(name = 'V_37',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_38 = Vertex(name = 'V_38',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_39 = Vertex(name = 'V_39',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_40 = Vertex(name = 'V_40',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_41 = Vertex(name = 'V_41',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_42 = Vertex(name = 'V_42',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_692})

V_43 = Vertex(name = 'V_43',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_44 = Vertex(name = 'V_44',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_45 = Vertex(name = 'V_45',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_46 = Vertex(name = 'V_46',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_47 = Vertex(name = 'V_47',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_48 = Vertex(name = 'V_48',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_49 = Vertex(name = 'V_49',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_50 = Vertex(name = 'V_50',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_51 = Vertex(name = 'V_51',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_52 = Vertex(name = 'V_52',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_53 = Vertex(name = 'V_53',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_54 = Vertex(name = 'V_54',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2183})

V_55 = Vertex(name = 'V_55',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3447,(0,1):C.GC_2810})

V_56 = Vertex(name = 'V_56',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3447,(0,1):C.GC_2810})

V_57 = Vertex(name = 'V_57',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3447,(0,1):C.GC_2810})

V_58 = Vertex(name = 'V_58',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3446,(0,1):C.GC_2809})

V_59 = Vertex(name = 'V_59',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3446,(0,1):C.GC_2809})

V_60 = Vertex(name = 'V_60',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3446,(0,1):C.GC_2809})

V_61 = Vertex(name = 'V_61',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3449})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3449})

V_63 = Vertex(name = 'V_63',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3449})

V_64 = Vertex(name = 'V_64',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3448,(0,1):C.GC_2811})

V_65 = Vertex(name = 'V_65',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3448,(0,1):C.GC_2811})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_3448,(0,1):C.GC_2811})

V_67 = Vertex(name = 'V_67',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_28,(0,1):C.GC_28,(0,2):C.GC_28})

V_68 = Vertex(name = 'V_68',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_618,(0,1):C.GC_618,(0,2):C.GC_618})

V_69 = Vertex(name = 'V_69',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_22,(0,2):C.GC_29})

V_70 = Vertex(name = 'V_70',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_615,(0,1):C.GC_615,(0,2):C.GC_593})

V_71 = Vertex(name = 'V_71',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_26,(0,1):C.GC_26,(0,2):C.GC_24})

V_72 = Vertex(name = 'V_72',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_616,(0,1):C.GC_616,(0,2):C.GC_578})

V_73 = Vertex(name = 'V_73',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_25,(0,1):C.GC_21})

V_74 = Vertex(name = 'V_74',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_614,(0,1):C.GC_631})

V_75 = Vertex(name = 'V_75',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_23,(0,2):C.GC_27})

V_76 = Vertex(name = 'V_76',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_577,(0,1):C.GC_577,(0,2):C.GC_617})

V_77 = Vertex(name = 'V_77',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_22,(0,2):C.GC_29})

V_78 = Vertex(name = 'V_78',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3, L.SSSS4 ],
              couplings = {(0,0):C.GC_615,(0,1):C.GC_615,(0,2):C.GC_593})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_4993,(0,1):C.GC_5862,(0,2):C.GC_5862})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5175,(0,1):C.GC_6115,(0,2):C.GC_6115})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5863,(0,1):C.GC_5863,(0,2):C.GC_4992})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_6116,(0,1):C.GC_6116,(0,2):C.GC_5165})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS3 ],
              couplings = {(0,0):C.GC_5860,(0,1):C.GC_5861})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS3 ],
              couplings = {(0,0):C.GC_6114,(0,1):C.GC_6113})

V_85 = Vertex(name = 'V_85',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5862,(0,1):C.GC_5862,(0,2):C.GC_4993})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_6115,(0,1):C.GC_6115,(0,2):C.GC_5175})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS21, L.VVSS5 ],
              couplings = {(0,0):C.GC_6753,(0,2):C.GC_6753,(0,1):C.GC_5362})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS21, L.VVSS5 ],
              couplings = {(0,0):C.GC_6817,(0,2):C.GC_6817,(0,1):C.GC_5399})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_4993,(0,1):C.GC_5862,(0,2):C.GC_5862})

V_90 = Vertex(name = 'V_90',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5175,(0,1):C.GC_6115,(0,2):C.GC_6115})

V_91 = Vertex(name = 'V_91',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_4992,(0,1):C.GC_5863,(0,2):C.GC_5863})

V_92 = Vertex(name = 'V_92',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5165,(0,1):C.GC_6116,(0,2):C.GC_6116})

V_93 = Vertex(name = 'V_93',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS3 ],
              couplings = {(0,0):C.GC_5861,(0,1):C.GC_5860})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS3 ],
              couplings = {(0,0):C.GC_6113,(0,1):C.GC_6114})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_5862,(0,1):C.GC_5862,(0,2):C.GC_4993})

V_96 = Vertex(name = 'V_96',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
              couplings = {(0,0):C.GC_6115,(0,1):C.GC_6115,(0,2):C.GC_5175})

V_97 = Vertex(name = 'V_97',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
              couplings = {(0,7):C.GC_16,(0,8):C.GC_17,(0,17):C.GC_15,(0,0):C.GC_6753,(0,21):C.GC_18,(0,18):C.GC_5362,(0,11):C.GC_12,(0,19):C.GC_10,(0,10):C.GC_17,(0,20):C.GC_11,(0,6):C.GC_18,(0,1):C.GC_9,(0,9):C.GC_17,(0,16):C.GC_9,(0,13):C.GC_12,(0,5):C.GC_18,(0,22):C.GC_11,(0,14):C.GC_10,(0,3):C.GC_2,(0,4):C.GC_1,(0,2):C.GC_7,(0,12):C.GC_6753,(0,15):C.GC_8})

V_98 = Vertex(name = 'V_98',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
              couplings = {(0,0):C.GC_6817,(0,9):C.GC_5399,(0,3):C.GC_472,(0,10):C.GC_546,(0,11):C.GC_545,(0,1):C.GC_473,(0,8):C.GC_473,(0,5):C.GC_472,(0,12):C.GC_545,(0,6):C.GC_546,(0,2):C.GC_450,(0,4):C.GC_6817,(0,7):C.GC_451})

V_99 = Vertex(name = 'V_99',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
              couplings = {(0,7):C.GC_20,(0,8):C.GC_19,(0,17):C.GC_20,(0,0):C.GC_6751,(0,21):C.GC_19,(0,18):C.GC_6751,(0,11):C.GC_4,(0,19):C.GC_4,(0,10):C.GC_19,(0,20):C.GC_3,(0,6):C.GC_19,(0,1):C.GC_3,(0,9):C.GC_19,(0,16):C.GC_3,(0,13):C.GC_4,(0,5):C.GC_19,(0,22):C.GC_3,(0,14):C.GC_4,(0,3):C.GC_2,(0,4):C.GC_1,(0,2):C.GC_7,(0,12):C.GC_5363,(0,15):C.GC_8})

V_100 = Vertex(name = 'V_100',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6816,(0,9):C.GC_6816,(0,3):C.GC_544,(0,10):C.GC_544,(0,11):C.GC_543,(0,1):C.GC_543,(0,8):C.GC_543,(0,5):C.GC_544,(0,12):C.GC_543,(0,6):C.GC_544,(0,2):C.GC_450,(0,4):C.GC_5404,(0,7):C.GC_451})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,4):C.GC_6,(0,5):C.GC_5,(0,12):C.GC_5,(0,0):C.GC_6750,(0,16):C.GC_6,(0,13):C.GC_6752,(0,8):C.GC_14,(0,14):C.GC_13,(0,7):C.GC_5,(0,15):C.GC_14,(0,3):C.GC_6,(0,1):C.GC_13,(0,6):C.GC_5,(0,11):C.GC_13,(0,9):C.GC_14,(0,2):C.GC_6,(0,17):C.GC_14,(0,10):C.GC_13})

V_102 = Vertex(name = 'V_102',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6818,(0,6):C.GC_6815,(0,2):C.GC_547,(0,7):C.GC_548,(0,8):C.GC_547,(0,1):C.GC_548,(0,5):C.GC_548,(0,3):C.GC_547,(0,9):C.GC_547,(0,4):C.GC_548})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS11, L.VVVS12, L.VVVS13, L.VVVS14, L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS21, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS34, L.VVVS36, L.VVVS37, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS46, L.VVVS47, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS53, L.VVVS54, L.VVVS56, L.VVVS57, L.VVVS59, L.VVVS6, L.VVVS60, L.VVVS61, L.VVVS63, L.VVVS7 ],
               couplings = {(0,16):C.GC_5856,(0,17):C.GC_5856,(0,14):C.GC_5856,(0,15):C.GC_5856,(0,30):C.GC_5857,(0,38):C.GC_4989,(0,42):C.GC_4988,(0,13):C.GC_5852,(0,21):C.GC_4990,(0,2):C.GC_4989,(0,3):C.GC_5857,(0,4):C.GC_4988,(0,0):C.GC_4990,(0,1):C.GC_5852,(0,7):C.GC_5857,(0,8):C.GC_5858,(0,5):C.GC_5854,(0,6):C.GC_5854,(0,24):C.GC_5859,(0,25):C.GC_5859,(0,18):C.GC_5436,(0,33):C.GC_5856,(0,26):C.GC_7118,(0,41):C.GC_5856,(0,34):C.GC_7118,(0,19):C.GC_5853,(0,27):C.GC_4991,(0,35):C.GC_5855,(0,11):C.GC_5858,(0,29):C.GC_5855,(0,37):C.GC_5852,(0,20):C.GC_5853,(0,28):C.GC_5855,(0,36):C.GC_4991,(0,12):C.GC_5857,(0,31):C.GC_5852,(0,39):C.GC_5855,(0,9):C.GC_5858,(0,10):C.GC_5857,(0,22):C.GC_5854,(0,23):C.GC_5854,(0,32):C.GC_5853,(0,40):C.GC_5853})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS11, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS34, L.VVVS36, L.VVVS37, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS46, L.VVVS47, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS56, L.VVVS57, L.VVVS59, L.VVVS60, L.VVVS61 ],
               couplings = {(0,4):C.GC_5121,(0,8):C.GC_5112,(0,0):C.GC_5112,(0,1):C.GC_5121,(0,2):C.GC_6087,(0,3):C.GC_6087,(0,5):C.GC_5439,(0,11):C.GC_7121,(0,17):C.GC_7121,(0,6):C.GC_6088,(0,12):C.GC_5113,(0,18):C.GC_5120,(0,14):C.GC_5120,(0,20):C.GC_5121,(0,7):C.GC_6088,(0,13):C.GC_5120,(0,19):C.GC_5113,(0,15):C.GC_5121,(0,21):C.GC_5120,(0,9):C.GC_6087,(0,10):C.GC_6087,(0,16):C.GC_6088,(0,22):C.GC_6088})

V_105 = Vertex(name = 'V_105',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS21, L.VVSS5 ],
               couplings = {(0,0):C.GC_6753,(0,2):C.GC_6753,(0,1):C.GC_5362})

V_106 = Vertex(name = 'V_106',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS21, L.VVSS5 ],
               couplings = {(0,0):C.GC_6817,(0,2):C.GC_6817,(0,1):C.GC_5399})

V_107 = Vertex(name = 'V_107',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,15):C.GC_5857,(0,14):C.GC_5857,(0,18):C.GC_5857,(0,17):C.GC_5857,(0,8):C.GC_5859,(0,0):C.GC_5854,(0,31):C.GC_5856,(0,16):C.GC_5854,(0,42):C.GC_5856,(0,41):C.GC_5852,(0,2):C.GC_4989,(0,3):C.GC_4988,(0,1):C.GC_4990,(0,5):C.GC_4989,(0,6):C.GC_4988,(0,4):C.GC_4990,(0,9):C.GC_5856,(0,7):C.GC_5852,(0,25):C.GC_5858,(0,19):C.GC_7118,(0,33):C.GC_5858,(0,26):C.GC_7118,(0,39):C.GC_5857,(0,40):C.GC_5857,(0,34):C.GC_5436,(0,20):C.GC_4991,(0,27):C.GC_5855,(0,35):C.GC_5853,(0,21):C.GC_5855,(0,28):C.GC_4991,(0,36):C.GC_5853,(0,11):C.GC_5856,(0,13):C.GC_5859,(0,22):C.GC_5853,(0,30):C.GC_5853,(0,37):C.GC_5854,(0,38):C.GC_5854,(0,10):C.GC_5856,(0,23):C.GC_5855,(0,29):C.GC_5852,(0,12):C.GC_5859,(0,24):C.GC_5852,(0,32):C.GC_5855})

V_108 = Vertex(name = 'V_108',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6087,(0,4):C.GC_6087,(0,22):C.GC_5121,(0,1):C.GC_5112,(0,2):C.GC_5112,(0,3):C.GC_5121,(0,5):C.GC_7121,(0,11):C.GC_7121,(0,17):C.GC_5439,(0,6):C.GC_5113,(0,12):C.GC_5120,(0,18):C.GC_6088,(0,7):C.GC_5120,(0,13):C.GC_5113,(0,19):C.GC_6088,(0,8):C.GC_6088,(0,15):C.GC_6088,(0,20):C.GC_6087,(0,21):C.GC_6087,(0,9):C.GC_5120,(0,14):C.GC_5121,(0,10):C.GC_5121,(0,16):C.GC_5120})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6190,(0,1):C.GC_6190,(0,2):C.GC_6190})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6397,(0,1):C.GC_6397,(0,2):C.GC_6397})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6186,(0,1):C.GC_6186,(0,2):C.GC_6188})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6395,(0,1):C.GC_6395,(0,2):C.GC_6383})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6184,(0,1):C.GC_6185})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6394,(0,1):C.GC_6393})

V_115 = Vertex(name = 'V_115',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6187,(0,1):C.GC_6187,(0,2):C.GC_6189})

V_116 = Vertex(name = 'V_116',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS1, L.VSSS2, L.VSSS3 ],
               couplings = {(0,0):C.GC_6382,(0,1):C.GC_6382,(0,2):C.GC_6396})

V_117 = Vertex(name = 'V_117',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_57,(0,7):C.GC_3231,(0,16):C.GC_56,(0,0):C.GC_6757,(0,20):C.GC_3233,(0,17):C.GC_6755,(0,10):C.GC_3247,(0,18):C.GC_3244,(0,9):C.GC_62,(0,19):C.GC_3243,(0,5):C.GC_63,(0,1):C.GC_3240,(0,8):C.GC_3231,(0,15):C.GC_3240,(0,12):C.GC_3247,(0,4):C.GC_3233,(0,21):C.GC_3243,(0,13):C.GC_3244,(0,3):C.GC_2783,(0,2):C.GC_2786,(0,11):C.GC_6755,(0,14):C.GC_2787})

V_118 = Vertex(name = 'V_118',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6810,(0,9):C.GC_6820,(0,3):C.GC_3689,(0,10):C.GC_3690,(0,11):C.GC_3687,(0,1):C.GC_3688,(0,8):C.GC_3688,(0,5):C.GC_3689,(0,12):C.GC_3687,(0,6):C.GC_3690,(0,2):C.GC_2984,(0,4):C.GC_6820,(0,7):C.GC_2985})

V_119 = Vertex(name = 'V_119',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_60,(0,7):C.GC_3228,(0,16):C.GC_61,(0,0):C.GC_6754,(0,19):C.GC_3229,(0,10):C.GC_3250,(0,17):C.GC_3249,(0,9):C.GC_59,(0,18):C.GC_3238,(0,5):C.GC_58,(0,1):C.GC_3237,(0,8):C.GC_3228,(0,15):C.GC_3237,(0,12):C.GC_3250,(0,4):C.GC_3229,(0,20):C.GC_3238,(0,13):C.GC_3249,(0,3):C.GC_2782,(0,2):C.GC_2785,(0,11):C.GC_6756,(0,14):C.GC_2788})

V_120 = Vertex(name = 'V_120',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6821,(0,3):C.GC_3692,(0,9):C.GC_3691,(0,10):C.GC_3686,(0,1):C.GC_3685,(0,8):C.GC_3685,(0,5):C.GC_3692,(0,11):C.GC_3686,(0,6):C.GC_3691,(0,2):C.GC_2983,(0,4):C.GC_6819,(0,7):C.GC_2986})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_63,(0,7):C.GC_3232,(0,16):C.GC_62,(0,0):C.GC_6757,(0,20):C.GC_3230,(0,17):C.GC_6755,(0,10):C.GC_3245,(0,18):C.GC_3246,(0,9):C.GC_56,(0,19):C.GC_3241,(0,5):C.GC_57,(0,1):C.GC_3242,(0,8):C.GC_3232,(0,15):C.GC_3242,(0,12):C.GC_3245,(0,4):C.GC_3230,(0,21):C.GC_3241,(0,13):C.GC_3246,(0,3):C.GC_2783,(0,2):C.GC_2786,(0,11):C.GC_6755,(0,14):C.GC_2787})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6810,(0,9):C.GC_6820,(0,3):C.GC_3689,(0,10):C.GC_3690,(0,11):C.GC_3687,(0,1):C.GC_3688,(0,8):C.GC_3688,(0,5):C.GC_3689,(0,12):C.GC_3687,(0,6):C.GC_3690,(0,2):C.GC_2984,(0,4):C.GC_6820,(0,7):C.GC_2985})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_61,(0,7):C.GC_3234,(0,16):C.GC_60,(0,0):C.GC_6756,(0,19):C.GC_3235,(0,10):C.GC_3239,(0,17):C.GC_3236,(0,9):C.GC_58,(0,18):C.GC_3251,(0,5):C.GC_59,(0,1):C.GC_3248,(0,8):C.GC_3234,(0,15):C.GC_3248,(0,12):C.GC_3239,(0,4):C.GC_3235,(0,20):C.GC_3251,(0,13):C.GC_3236,(0,3):C.GC_2784,(0,2):C.GC_2788,(0,11):C.GC_6754,(0,14):C.GC_2785})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_6819,(0,3):C.GC_3685,(0,9):C.GC_3686,(0,10):C.GC_3691,(0,1):C.GC_3692,(0,8):C.GC_3692,(0,5):C.GC_3685,(0,11):C.GC_3691,(0,6):C.GC_3686,(0,2):C.GC_2986,(0,4):C.GC_6821,(0,7):C.GC_2983})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS13, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS18, L.VVVS19, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS52, L.VVVS53, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS62, L.VVVS63, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,20):C.GC_6183,(0,19):C.GC_6183,(0,24):C.GC_5920,(0,25):C.GC_5925,(0,22):C.GC_5926,(0,23):C.GC_5921,(0,10):C.GC_6182,(0,0):C.GC_6174,(0,43):C.GC_5918,(0,58):C.GC_4478,(0,21):C.GC_5908,(0,32):C.GC_4481,(0,60):C.GC_6183,(0,59):C.GC_6174,(0,3):C.GC_5923,(0,4):C.GC_4478,(0,1):C.GC_4481,(0,2):C.GC_5909,(0,6):C.GC_6173,(0,7):C.GC_6172,(0,5):C.GC_6178,(0,11):C.GC_5919,(0,12):C.GC_5922,(0,8):C.GC_5897,(0,9):C.GC_5896,(0,35):C.GC_5923,(0,36):C.GC_5918,(0,26):C.GC_7139,(0,46):C.GC_6182,(0,47):C.GC_5926,(0,37):C.GC_7136,(0,56):C.GC_6183,(0,57):C.GC_5921,(0,48):C.GC_7136,(0,27):C.GC_6179,(0,38):C.GC_6175,(0,49):C.GC_6175,(0,28):C.GC_5910,(0,39):C.GC_4484,(0,50):C.GC_5899,(0,14):C.GC_6183,(0,17):C.GC_5925,(0,30):C.GC_6175,(0,42):C.GC_5899,(0,52):C.GC_6174,(0,53):C.GC_5908,(0,29):C.GC_5911,(0,40):C.GC_5898,(0,51):C.GC_4484,(0,13):C.GC_6183,(0,18):C.GC_5923,(0,31):C.GC_6175,(0,41):C.GC_6174,(0,44):C.GC_5909,(0,54):C.GC_5898,(0,15):C.GC_5927,(0,16):C.GC_5924,(0,33):C.GC_5897,(0,34):C.GC_5896,(0,45):C.GC_5910,(0,55):C.GC_5911})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS15, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS8 ],
               couplings = {(0,0):C.GC_6362,(0,6):C.GC_6089,(0,13):C.GC_4581,(0,32):C.GC_6362,(0,1):C.GC_4581,(0,2):C.GC_6089,(0,3):C.GC_6329,(0,4):C.GC_6095,(0,5):C.GC_6095,(0,7):C.GC_7140,(0,16):C.GC_7141,(0,24):C.GC_7141,(0,8):C.GC_6330,(0,17):C.GC_6365,(0,25):C.GC_6365,(0,9):C.GC_6090,(0,18):C.GC_4584,(0,26):C.GC_6096,(0,11):C.GC_6365,(0,21):C.GC_6096,(0,28):C.GC_6362,(0,29):C.GC_6089,(0,10):C.GC_6090,(0,19):C.GC_6096,(0,27):C.GC_4584,(0,12):C.GC_6365,(0,20):C.GC_6362,(0,22):C.GC_6089,(0,30):C.GC_6096,(0,14):C.GC_6095,(0,15):C.GC_6095,(0,23):C.GC_6090,(0,31):C.GC_6090})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS13, L.VVVS14, L.VVVS18, L.VVVS19, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS52, L.VVVS53, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS62, L.VVVS63, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,17):C.GC_6177,(0,16):C.GC_6177,(0,21):C.GC_5912,(0,22):C.GC_5915,(0,19):C.GC_5916,(0,20):C.GC_5914,(0,7):C.GC_6177,(0,0):C.GC_6181,(0,38):C.GC_5915,(0,53):C.GC_4479,(0,18):C.GC_5902,(0,27):C.GC_4482,(0,55):C.GC_6176,(0,54):C.GC_6180,(0,3):C.GC_5912,(0,4):C.GC_4480,(0,1):C.GC_4483,(0,2):C.GC_5904,(0,8):C.GC_5917,(0,9):C.GC_5931,(0,5):C.GC_5907,(0,6):C.GC_5901,(0,30):C.GC_5930,(0,31):C.GC_5928,(0,41):C.GC_6176,(0,42):C.GC_5916,(0,32):C.GC_7137,(0,51):C.GC_6177,(0,52):C.GC_5914,(0,43):C.GC_7138,(0,33):C.GC_6181,(0,44):C.GC_6180,(0,23):C.GC_5900,(0,34):C.GC_4482,(0,45):C.GC_5905,(0,11):C.GC_6176,(0,14):C.GC_5928,(0,25):C.GC_6180,(0,37):C.GC_5905,(0,47):C.GC_6181,(0,48):C.GC_5902,(0,24):C.GC_5906,(0,35):C.GC_5903,(0,46):C.GC_4483,(0,10):C.GC_6176,(0,15):C.GC_5912,(0,26):C.GC_6181,(0,36):C.GC_6180,(0,39):C.GC_5904,(0,49):C.GC_5903,(0,12):C.GC_5929,(0,13):C.GC_5913,(0,28):C.GC_5907,(0,29):C.GC_5901,(0,40):C.GC_5900,(0,50):C.GC_5906})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS8 ],
               couplings = {(0,0):C.GC_6363,(0,5):C.GC_6094,(0,10):C.GC_4582,(0,29):C.GC_6364,(0,1):C.GC_4583,(0,2):C.GC_6091,(0,3):C.GC_6092,(0,4):C.GC_6093,(0,13):C.GC_7143,(0,21):C.GC_7142,(0,14):C.GC_6363,(0,22):C.GC_6364,(0,6):C.GC_6093,(0,15):C.GC_4582,(0,23):C.GC_6091,(0,8):C.GC_6364,(0,18):C.GC_6091,(0,25):C.GC_6363,(0,26):C.GC_6094,(0,7):C.GC_6092,(0,16):C.GC_6094,(0,24):C.GC_4583,(0,9):C.GC_6363,(0,17):C.GC_6364,(0,19):C.GC_6091,(0,27):C.GC_6094,(0,11):C.GC_6092,(0,12):C.GC_6093,(0,20):C.GC_6093,(0,28):C.GC_6092})

V_129 = Vertex(name = 'V_129',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,7):C.GC_2791,(0,8):C.GC_2791,(0,17):C.GC_2791,(0,0):C.GC_7030,(0,21):C.GC_2791,(0,18):C.GC_7030,(0,11):C.GC_3819,(0,19):C.GC_3819,(0,10):C.GC_2792,(0,20):C.GC_3816,(0,6):C.GC_2792,(0,1):C.GC_3816,(0,9):C.GC_2791,(0,16):C.GC_3816,(0,13):C.GC_3819,(0,5):C.GC_2791,(0,22):C.GC_3816,(0,14):C.GC_3819,(0,3):C.GC_3823,(0,4):C.GC_3820,(0,2):C.GC_3824,(0,12):C.GC_7030,(0,15):C.GC_3827})

V_130 = Vertex(name = 'V_130',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_7062,(0,9):C.GC_7062,(0,3):C.GC_4160,(0,10):C.GC_4160,(0,11):C.GC_4161,(0,1):C.GC_4161,(0,8):C.GC_4161,(0,5):C.GC_4160,(0,12):C.GC_4161,(0,6):C.GC_4160,(0,2):C.GC_4149,(0,4):C.GC_7062,(0,7):C.GC_4152})

V_131 = Vertex(name = 'V_131',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,7):C.GC_3293,(0,8):C.GC_3293,(0,17):C.GC_3292,(0,0):C.GC_7027,(0,21):C.GC_3292,(0,18):C.GC_7027,(0,11):C.GC_3818,(0,19):C.GC_3818,(0,10):C.GC_3290,(0,20):C.GC_3817,(0,6):C.GC_3291,(0,1):C.GC_3817,(0,9):C.GC_3293,(0,16):C.GC_3817,(0,13):C.GC_3818,(0,5):C.GC_3292,(0,22):C.GC_3817,(0,14):C.GC_3818,(0,3):C.GC_3822,(0,4):C.GC_3821,(0,2):C.GC_3825,(0,12):C.GC_7029,(0,15):C.GC_3826})

V_132 = Vertex(name = 'V_132',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS21, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_7061,(0,9):C.GC_7061,(0,3):C.GC_4159,(0,10):C.GC_4159,(0,11):C.GC_4162,(0,1):C.GC_4162,(0,8):C.GC_4162,(0,5):C.GC_4159,(0,12):C.GC_4162,(0,6):C.GC_4159,(0,2):C.GC_4150,(0,4):C.GC_7057,(0,7):C.GC_4151})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS13, L.VVVS14, L.VVVS15, L.VVVS17, L.VVVS18, L.VVVS19, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS52, L.VVVS53, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS6, L.VVVS60, L.VVVS61, L.VVVS62, L.VVVS63, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,19):C.GC_6168,(0,18):C.GC_6426,(0,23):C.GC_6168,(0,24):C.GC_5452,(0,21):C.GC_5453,(0,22):C.GC_6426,(0,9):C.GC_6170,(0,0):C.GC_6432,(0,42):C.GC_6169,(0,53):C.GC_6145,(0,58):C.GC_6144,(0,20):C.GC_6432,(0,31):C.GC_6146,(0,60):C.GC_6424,(0,59):C.GC_6431,(0,3):C.GC_5451,(0,4):C.GC_6421,(0,1):C.GC_6422,(0,2):C.GC_6142,(0,6):C.GC_6421,(0,5):C.GC_6422,(0,10):C.GC_6424,(0,11):C.GC_5451,(0,7):C.GC_6431,(0,8):C.GC_6142,(0,34):C.GC_6171,(0,35):C.GC_5453,(0,25):C.GC_7144,(0,45):C.GC_6171,(0,46):C.GC_5453,(0,36):C.GC_7144,(0,56):C.GC_6426,(0,57):C.GC_6426,(0,47):C.GC_7145,(0,26):C.GC_6423,(0,37):C.GC_6436,(0,48):C.GC_6435,(0,27):C.GC_6436,(0,38):C.GC_6423,(0,49):C.GC_6435,(0,13):C.GC_6169,(0,16):C.GC_6170,(0,29):C.GC_6435,(0,41):C.GC_6435,(0,51):C.GC_6432,(0,52):C.GC_6432,(0,28):C.GC_6143,(0,39):C.GC_6143,(0,50):C.GC_6147,(0,12):C.GC_6424,(0,17):C.GC_5451,(0,30):C.GC_6436,(0,40):C.GC_6431,(0,43):C.GC_6142,(0,54):C.GC_6143,(0,14):C.GC_6429,(0,15):C.GC_5454,(0,32):C.GC_6431,(0,33):C.GC_6142,(0,44):C.GC_6436,(0,55):C.GC_6143})

V_134 = Vertex(name = 'V_134',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS15, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS8 ],
               couplings = {(0,0):C.GC_6569,(0,6):C.GC_6569,(0,13):C.GC_6336,(0,32):C.GC_6568,(0,1):C.GC_6562,(0,2):C.GC_6343,(0,3):C.GC_6562,(0,4):C.GC_6568,(0,5):C.GC_6343,(0,7):C.GC_7153,(0,16):C.GC_7153,(0,24):C.GC_7150,(0,8):C.GC_6563,(0,17):C.GC_6571,(0,25):C.GC_6570,(0,9):C.GC_6571,(0,18):C.GC_6563,(0,26):C.GC_6570,(0,11):C.GC_6570,(0,21):C.GC_6570,(0,28):C.GC_6569,(0,29):C.GC_6569,(0,10):C.GC_6342,(0,19):C.GC_6342,(0,27):C.GC_6337,(0,12):C.GC_6571,(0,20):C.GC_6568,(0,22):C.GC_6343,(0,30):C.GC_6342,(0,14):C.GC_6568,(0,15):C.GC_6343,(0,23):C.GC_6571,(0,31):C.GC_6342})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS13, L.VVVS14, L.VVVS15, L.VVVS17, L.VVVS18, L.VVVS19, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS52, L.VVVS53, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS6, L.VVVS60, L.VVVS61, L.VVVS62, L.VVVS63, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,19):C.GC_6170,(0,18):C.GC_6425,(0,23):C.GC_6170,(0,24):C.GC_5451,(0,21):C.GC_5454,(0,22):C.GC_6425,(0,9):C.GC_6168,(0,0):C.GC_6430,(0,42):C.GC_6171,(0,53):C.GC_6145,(0,58):C.GC_6144,(0,20):C.GC_6430,(0,31):C.GC_6146,(0,60):C.GC_6427,(0,59):C.GC_6433,(0,3):C.GC_5452,(0,4):C.GC_6421,(0,1):C.GC_6422,(0,2):C.GC_6142,(0,6):C.GC_6421,(0,5):C.GC_6422,(0,10):C.GC_6427,(0,11):C.GC_5452,(0,7):C.GC_6433,(0,8):C.GC_6142,(0,34):C.GC_6169,(0,35):C.GC_5454,(0,25):C.GC_7144,(0,45):C.GC_6169,(0,46):C.GC_5454,(0,36):C.GC_7144,(0,56):C.GC_6425,(0,57):C.GC_6425,(0,47):C.GC_7145,(0,26):C.GC_6423,(0,37):C.GC_6434,(0,48):C.GC_6437,(0,27):C.GC_6434,(0,38):C.GC_6423,(0,49):C.GC_6437,(0,13):C.GC_6171,(0,16):C.GC_6168,(0,29):C.GC_6437,(0,41):C.GC_6437,(0,51):C.GC_6430,(0,52):C.GC_6430,(0,28):C.GC_6143,(0,39):C.GC_6143,(0,50):C.GC_6147,(0,12):C.GC_6427,(0,17):C.GC_5452,(0,30):C.GC_6434,(0,40):C.GC_6433,(0,43):C.GC_6142,(0,54):C.GC_6143,(0,14):C.GC_6428,(0,15):C.GC_5453,(0,32):C.GC_6433,(0,33):C.GC_6142,(0,44):C.GC_6434,(0,55):C.GC_6143})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS15, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS8 ],
               couplings = {(0,0):C.GC_6569,(0,6):C.GC_6569,(0,13):C.GC_6336,(0,32):C.GC_6568,(0,1):C.GC_6562,(0,2):C.GC_6343,(0,3):C.GC_6562,(0,4):C.GC_6568,(0,5):C.GC_6343,(0,7):C.GC_7153,(0,16):C.GC_7153,(0,24):C.GC_7150,(0,8):C.GC_6563,(0,17):C.GC_6571,(0,25):C.GC_6570,(0,9):C.GC_6571,(0,18):C.GC_6563,(0,26):C.GC_6570,(0,11):C.GC_6570,(0,21):C.GC_6570,(0,28):C.GC_6569,(0,29):C.GC_6569,(0,10):C.GC_6342,(0,19):C.GC_6342,(0,27):C.GC_6337,(0,12):C.GC_6571,(0,20):C.GC_6568,(0,22):C.GC_6343,(0,30):C.GC_6342,(0,14):C.GC_6568,(0,15):C.GC_6343,(0,23):C.GC_6571,(0,31):C.GC_6342})

V_137 = Vertex(name = 'V_137',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS12, L.VVVS13, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS18, L.VVVS19, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS42, L.VVVS43, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS51, L.VVVS52, L.VVVS53, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS6, L.VVVS60, L.VVVS61, L.VVVS62, L.VVVS63, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,21):C.GC_6419,(0,20):C.GC_6418,(0,25):C.GC_6419,(0,26):C.GC_6419,(0,23):C.GC_6418,(0,24):C.GC_6418,(0,11):C.GC_6418,(0,0):C.GC_6614,(0,44):C.GC_6419,(0,55):C.GC_6617,(0,60):C.GC_6616,(0,22):C.GC_6614,(0,33):C.GC_6618,(0,62):C.GC_6418,(0,61):C.GC_6614,(0,3):C.GC_6617,(0,4):C.GC_6419,(0,5):C.GC_6616,(0,1):C.GC_6618,(0,2):C.GC_6614,(0,7):C.GC_6617,(0,8):C.GC_6616,(0,6):C.GC_6618,(0,12):C.GC_6418,(0,13):C.GC_6419,(0,9):C.GC_6614,(0,10):C.GC_6614,(0,36):C.GC_6418,(0,37):C.GC_6418,(0,27):C.GC_7160,(0,47):C.GC_6418,(0,48):C.GC_6418,(0,38):C.GC_7160,(0,58):C.GC_6418,(0,59):C.GC_6418,(0,49):C.GC_7160,(0,28):C.GC_6619,(0,39):C.GC_6615,(0,50):C.GC_6615,(0,29):C.GC_6615,(0,40):C.GC_6619,(0,51):C.GC_6615,(0,15):C.GC_6419,(0,18):C.GC_6418,(0,31):C.GC_6615,(0,43):C.GC_6615,(0,53):C.GC_6614,(0,54):C.GC_6614,(0,30):C.GC_6615,(0,41):C.GC_6615,(0,52):C.GC_6619,(0,14):C.GC_6418,(0,19):C.GC_6419,(0,32):C.GC_6615,(0,42):C.GC_6614,(0,45):C.GC_6614,(0,56):C.GC_6615,(0,16):C.GC_6419,(0,17):C.GC_6418,(0,34):C.GC_6614,(0,35):C.GC_6614,(0,46):C.GC_6615,(0,57):C.GC_6615})

V_138 = Vertex(name = 'V_138',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS11, L.VVVS15, L.VVVS18, L.VVVS19, L.VVVS3, L.VVVS34, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS39, L.VVVS4, L.VVVS40, L.VVVS41, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS47, L.VVVS48, L.VVVS49, L.VVVS50, L.VVVS51, L.VVVS54, L.VVVS55, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS60, L.VVVS61, L.VVVS8 ],
               couplings = {(0,0):C.GC_6657,(0,6):C.GC_6657,(0,13):C.GC_6654,(0,32):C.GC_6657,(0,1):C.GC_6654,(0,2):C.GC_6657,(0,3):C.GC_6654,(0,4):C.GC_6657,(0,5):C.GC_6657,(0,7):C.GC_7161,(0,16):C.GC_7161,(0,24):C.GC_7161,(0,8):C.GC_6655,(0,17):C.GC_6656,(0,25):C.GC_6656,(0,9):C.GC_6656,(0,18):C.GC_6655,(0,26):C.GC_6656,(0,11):C.GC_6656,(0,21):C.GC_6656,(0,28):C.GC_6657,(0,29):C.GC_6657,(0,10):C.GC_6656,(0,19):C.GC_6656,(0,27):C.GC_6655,(0,12):C.GC_6656,(0,20):C.GC_6657,(0,22):C.GC_6657,(0,30):C.GC_6656,(0,14):C.GC_6657,(0,15):C.GC_6657,(0,23):C.GC_6656,(0,31):C.GC_6656})

V_139 = Vertex(name = 'V_139',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV10, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV105, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV109, L.VVVV11, L.VVVV110, L.VVVV111, L.VVVV112, L.VVVV113, L.VVVV114, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV12, L.VVVV120, L.VVVV121, L.VVVV122, L.VVVV123, L.VVVV124, L.VVVV125, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV129, L.VVVV13, L.VVVV130, L.VVVV131, L.VVVV132, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV136, L.VVVV137, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV142, L.VVVV143, L.VVVV144, L.VVVV145, L.VVVV146, L.VVVV147, L.VVVV148, L.VVVV149, L.VVVV15, L.VVVV150, L.VVVV151, L.VVVV152, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV158, L.VVVV159, L.VVVV16, L.VVVV160, L.VVVV161, L.VVVV162, L.VVVV163, L.VVVV164, L.VVVV165, L.VVVV166, L.VVVV167, L.VVVV168, L.VVVV169, L.VVVV17, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV176, L.VVVV177, L.VVVV178, L.VVVV179, L.VVVV18, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV184, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV190, L.VVVV191, L.VVVV192, L.VVVV193, L.VVVV194, L.VVVV195, L.VVVV196, L.VVVV197, L.VVVV198, L.VVVV199, L.VVVV2, L.VVVV20, L.VVVV200, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV208, L.VVVV209, L.VVVV21, L.VVVV210, L.VVVV211, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV216, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV24, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV28, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV34, L.VVVV35, L.VVVV36, L.VVVV37, L.VVVV38, L.VVVV39, L.VVVV4, L.VVVV40, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV5, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV58, L.VVVV59, L.VVVV6, L.VVVV60, L.VVVV61, L.VVVV62, L.VVVV63, L.VVVV64, L.VVVV65, L.VVVV66, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV70, L.VVVV71, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV76, L.VVVV77, L.VVVV78, L.VVVV79, L.VVVV8, L.VVVV80, L.VVVV81, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV85, L.VVVV86, L.VVVV87, L.VVVV88, L.VVVV89, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97, L.VVVV98, L.VVVV99 ],
               couplings = {(0,142):C.GC_7070,(0,153):C.GC_7070,(0,0):C.GC_7071,(0,111):C.GC_7071,(0,208):C.GC_7070,(0,1):C.GC_7071,(0,12):C.GC_7070,(0,23):C.GC_7070,(0,164):C.GC_7071,(0,175):C.GC_7071,(0,186):C.GC_7070,(0,197):C.GC_7071,(0,147):C.GC_7071,(0,148):C.GC_7071,(0,149):C.GC_7071,(0,150):C.GC_7070,(0,156):C.GC_4403,(0,157):C.GC_4406,(0,158):C.GC_4405,(0,151):C.GC_7070,(0,152):C.GC_4403,(0,154):C.GC_7070,(0,155):C.GC_4403,(0,161):C.GC_4404,(0,162):C.GC_4405,(0,163):C.GC_4406,(0,159):C.GC_4404,(0,160):C.GC_4404,(0,165):C.GC_4406,(0,166):C.GC_4405,(0,167):C.GC_4406,(0,168):C.GC_4405,(0,169):C.GC_4405,(0,170):C.GC_4406,(0,171):C.GC_4405,(0,172):C.GC_4406,(0,34):C.GC_7070,(0,78):C.GC_7071,(0,89):C.GC_4403,(0,100):C.GC_4404,(0,45):C.GC_4402,(0,56):C.GC_4477,(0,67):C.GC_4477,(0,112):C.GC_7070,(0,136):C.GC_7071,(0,137):C.GC_4403,(0,138):C.GC_4404,(0,123):C.GC_4477,(0,134):C.GC_4402,(0,135):C.GC_4477,(0,139):C.GC_7070,(0,140):C.GC_7071,(0,141):C.GC_4477,(0,143):C.GC_4477,(0,145):C.GC_4403,(0,146):C.GC_4404,(0,144):C.GC_4402,(0,173):C.GC_7079,(0,174):C.GC_7079,(0,178):C.GC_7071,(0,179):C.GC_7071,(0,176):C.GC_7080,(0,177):C.GC_7080,(0,187):C.GC_7070,(0,188):C.GC_7070,(0,193):C.GC_7081,(0,194):C.GC_7082,(0,180):C.GC_7080,(0,181):C.GC_7080,(0,182):C.GC_7084,(0,199):C.GC_7071,(0,198):C.GC_7080,(0,203):C.GC_7071,(0,200):C.GC_7079,(0,201):C.GC_7080,(0,202):C.GC_7079,(0,211):C.GC_7070,(0,212):C.GC_7081,(0,217):C.GC_7070,(0,218):C.GC_7082,(0,204):C.GC_7080,(0,205):C.GC_7084,(0,206):C.GC_7080,(0,5):C.GC_7071,(0,4):C.GC_7080,(0,8):C.GC_7070,(0,9):C.GC_7081,(0,10):C.GC_7082,(0,6):C.GC_7080,(0,7):C.GC_7084,(0,26):C.GC_7071,(0,27):C.GC_7070,(0,11):C.GC_7079,(0,13):C.GC_7080,(0,16):C.GC_7079,(0,17):C.GC_7080,(0,29):C.GC_7071,(0,28):C.GC_7080,(0,33):C.GC_7071,(0,30):C.GC_7080,(0,31):C.GC_7079,(0,32):C.GC_7079,(0,41):C.GC_7081,(0,42):C.GC_7070,(0,48):C.GC_7070,(0,49):C.GC_7082,(0,35):C.GC_7084,(0,36):C.GC_7080,(0,37):C.GC_7080,(0,52):C.GC_7170,(0,64):C.GC_7071,(0,63):C.GC_7080,(0,68):C.GC_7081,(0,69):C.GC_7070,(0,70):C.GC_7082,(0,65):C.GC_7084,(0,66):C.GC_7080,(0,85):C.GC_7071,(0,86):C.GC_7070,(0,71):C.GC_7080,(0,72):C.GC_7079,(0,75):C.GC_7079,(0,76):C.GC_7080,(0,87):C.GC_7170,(0,99):C.GC_7081,(0,101):C.GC_7082,(0,98):C.GC_7084,(0,104):C.GC_7071,(0,105):C.GC_7070,(0,102):C.GC_7080,(0,103):C.GC_7080,(0,121):C.GC_7071,(0,122):C.GC_7070,(0,106):C.GC_7080,(0,107):C.GC_7079,(0,110):C.GC_7080,(0,113):C.GC_7079,(0,124):C.GC_7170,(0,195):C.GC_4404,(0,196):C.GC_4403,(0,183):C.GC_4401,(0,207):C.GC_4476,(0,18):C.GC_4476,(0,38):C.GC_4476,(0,53):C.GC_7079,(0,77):C.GC_4476,(0,88):C.GC_7079,(0,108):C.GC_4477,(0,114):C.GC_4477,(0,125):C.GC_7083,(0,184):C.GC_4476,(0,2):C.GC_4404,(0,3):C.GC_4403,(0,209):C.GC_4401,(0,14):C.GC_4476,(0,39):C.GC_4476,(0,54):C.GC_7079,(0,73):C.GC_4477,(0,79):C.GC_4477,(0,90):C.GC_7083,(0,115):C.GC_4476,(0,126):C.GC_7079,(0,189):C.GC_4476,(0,213):C.GC_4476,(0,24):C.GC_4404,(0,25):C.GC_4403,(0,20):C.GC_4401,(0,43):C.GC_4477,(0,46):C.GC_4477,(0,57):C.GC_7083,(0,80):C.GC_4476,(0,92):C.GC_7079,(0,117):C.GC_4476,(0,128):C.GC_7079,(0,185):C.GC_4476,(0,210):C.GC_4476,(0,15):C.GC_4477,(0,19):C.GC_4477,(0,50):C.GC_4404,(0,51):C.GC_4403,(0,40):C.GC_4401,(0,55):C.GC_7083,(0,74):C.GC_4476,(0,91):C.GC_7079,(0,109):C.GC_4476,(0,127):C.GC_7079,(0,60):C.GC_4402,(0,95):C.GC_4477,(0,131):C.GC_4477,(0,190):C.GC_4476,(0,214):C.GC_4477,(0,215):C.GC_4477,(0,21):C.GC_4476,(0,44):C.GC_4476,(0,58):C.GC_7079,(0,83):C.GC_4404,(0,84):C.GC_4403,(0,81):C.GC_4401,(0,93):C.GC_7083,(0,116):C.GC_4476,(0,129):C.GC_7079,(0,61):C.GC_4477,(0,96):C.GC_4402,(0,132):C.GC_4477,(0,191):C.GC_4477,(0,192):C.GC_4477,(0,216):C.GC_4476,(0,22):C.GC_4476,(0,47):C.GC_4476,(0,59):C.GC_7079,(0,82):C.GC_4476,(0,94):C.GC_7079,(0,119):C.GC_4404,(0,120):C.GC_4403,(0,118):C.GC_4401,(0,130):C.GC_7083,(0,62):C.GC_4477,(0,97):C.GC_4477,(0,133):C.GC_4402})

V_140 = Vertex(name = 'V_140',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV102, L.VVVV104, L.VVVV105, L.VVVV109, L.VVVV110, L.VVVV113, L.VVVV114, L.VVVV117, L.VVVV124, L.VVVV126, L.VVVV127, L.VVVV128, L.VVVV130, L.VVVV131, L.VVVV132, L.VVVV135, L.VVVV14, L.VVVV146, L.VVVV147, L.VVVV148, L.VVVV149, L.VVVV150, L.VVVV151, L.VVVV152, L.VVVV153, L.VVVV156, L.VVVV158, L.VVVV159, L.VVVV163, L.VVVV164, L.VVVV167, L.VVVV168, L.VVVV172, L.VVVV178, L.VVVV179, L.VVVV180, L.VVVV181, L.VVVV182, L.VVVV183, L.VVVV184, L.VVVV186, L.VVVV188, L.VVVV191, L.VVVV192, L.VVVV195, L.VVVV196, L.VVVV199, L.VVVV200, L.VVVV205, L.VVVV210, L.VVVV211, L.VVVV212, L.VVVV213, L.VVVV214, L.VVVV215, L.VVVV216, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV60, L.VVVV61, L.VVVV64, L.VVVV65, L.VVVV66, L.VVVV67, L.VVVV80, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV86, L.VVVV87, L.VVVV88, L.VVVV90 ],
               couplings = {(0,16):C.GC_4475,(0,57):C.GC_4475,(0,58):C.GC_4475,(0,59):C.GC_7106,(0,60):C.GC_7106,(0,61):C.GC_7105,(0,62):C.GC_7105,(0,63):C.GC_7105,(0,64):C.GC_7105,(0,65):C.GC_7104,(0,67):C.GC_7105,(0,68):C.GC_7106,(0,69):C.GC_7105,(0,70):C.GC_7106,(0,71):C.GC_7105,(0,72):C.GC_7104,(0,73):C.GC_7105,(0,0):C.GC_7105,(0,1):C.GC_7105,(0,2):C.GC_7104,(0,3):C.GC_7106,(0,4):C.GC_7105,(0,5):C.GC_7106,(0,6):C.GC_7105,(0,8):C.GC_7105,(0,9):C.GC_7105,(0,10):C.GC_7106,(0,11):C.GC_7106,(0,12):C.GC_7104,(0,13):C.GC_7105,(0,14):C.GC_7105,(0,17):C.GC_7171,(0,25):C.GC_7105,(0,26):C.GC_7104,(0,27):C.GC_7105,(0,28):C.GC_7105,(0,29):C.GC_7106,(0,30):C.GC_7106,(0,31):C.GC_7105,(0,33):C.GC_7171,(0,41):C.GC_7104,(0,42):C.GC_7105,(0,43):C.GC_7105,(0,44):C.GC_7105,(0,45):C.GC_7106,(0,46):C.GC_7105,(0,47):C.GC_7106,(0,49):C.GC_7171,(0,66):C.GC_4474,(0,18):C.GC_7106,(0,34):C.GC_7106,(0,50):C.GC_7103,(0,74):C.GC_4474,(0,19):C.GC_7106,(0,35):C.GC_7103,(0,51):C.GC_7106,(0,7):C.GC_4474,(0,21):C.GC_7103,(0,37):C.GC_7106,(0,53):C.GC_7106,(0,15):C.GC_4474,(0,20):C.GC_7103,(0,36):C.GC_7106,(0,52):C.GC_7106,(0,24):C.GC_4475,(0,22):C.GC_7106,(0,32):C.GC_4474,(0,38):C.GC_7103,(0,54):C.GC_7106,(0,40):C.GC_4475,(0,23):C.GC_7106,(0,39):C.GC_7106,(0,48):C.GC_4474,(0,55):C.GC_7103,(0,56):C.GC_4475})

V_141 = Vertex(name = 'V_141',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_2792,(0,7):C.GC_2792,(0,15):C.GC_2792,(0,18):C.GC_2792,(0,10):C.GC_3850,(0,16):C.GC_3850,(0,9):C.GC_2791,(0,17):C.GC_3849,(0,5):C.GC_2791,(0,0):C.GC_3849,(0,8):C.GC_2792,(0,14):C.GC_3849,(0,11):C.GC_3850,(0,4):C.GC_2792,(0,19):C.GC_3849,(0,12):C.GC_3850,(0,2):C.GC_3846,(0,3):C.GC_3845,(0,1):C.GC_3853,(0,13):C.GC_3854})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4212,(0,7):C.GC_4212,(0,8):C.GC_4211,(0,0):C.GC_4211,(0,6):C.GC_4211,(0,3):C.GC_4212,(0,9):C.GC_4211,(0,4):C.GC_4212,(0,1):C.GC_4141,(0,5):C.GC_4142})

V_143 = Vertex(name = 'V_143',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_3290,(0,7):C.GC_3290,(0,15):C.GC_3291,(0,18):C.GC_3291,(0,10):C.GC_3851,(0,16):C.GC_3851,(0,9):C.GC_3293,(0,17):C.GC_3848,(0,5):C.GC_3292,(0,0):C.GC_3848,(0,8):C.GC_3290,(0,14):C.GC_3848,(0,11):C.GC_3851,(0,4):C.GC_3291,(0,19):C.GC_3848,(0,12):C.GC_3851,(0,2):C.GC_3847,(0,3):C.GC_3844,(0,1):C.GC_3852,(0,13):C.GC_3855})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4213,(0,7):C.GC_4213,(0,8):C.GC_4210,(0,0):C.GC_4210,(0,6):C.GC_4210,(0,3):C.GC_4213,(0,9):C.GC_4210,(0,4):C.GC_4213,(0,1):C.GC_4140,(0,5):C.GC_4143})

V_145 = Vertex(name = 'V_145',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_2792,(0,7):C.GC_2792,(0,15):C.GC_2792,(0,18):C.GC_2792,(0,10):C.GC_3850,(0,16):C.GC_3850,(0,9):C.GC_2791,(0,17):C.GC_3849,(0,5):C.GC_2791,(0,0):C.GC_3849,(0,8):C.GC_2792,(0,14):C.GC_3849,(0,11):C.GC_3850,(0,4):C.GC_2792,(0,19):C.GC_3849,(0,12):C.GC_3850,(0,2):C.GC_3846,(0,3):C.GC_3845,(0,1):C.GC_3853,(0,13):C.GC_3854})

V_146 = Vertex(name = 'V_146',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4212,(0,7):C.GC_4212,(0,8):C.GC_4211,(0,0):C.GC_4211,(0,6):C.GC_4211,(0,3):C.GC_4212,(0,9):C.GC_4211,(0,4):C.GC_4212,(0,1):C.GC_4141,(0,5):C.GC_4142})

V_147 = Vertex(name = 'V_147',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_52,(0,7):C.GC_3046,(0,15):C.GC_52,(0,18):C.GC_3046,(0,10):C.GC_3841,(0,16):C.GC_3841,(0,9):C.GC_51,(0,17):C.GC_3838,(0,5):C.GC_51,(0,0):C.GC_3838,(0,8):C.GC_3046,(0,14):C.GC_3838,(0,11):C.GC_3841,(0,4):C.GC_3046,(0,19):C.GC_3838,(0,12):C.GC_3841,(0,2):C.GC_3294,(0,3):C.GC_3828,(0,1):C.GC_3830,(0,13):C.GC_3833})

V_148 = Vertex(name = 'V_148',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4187,(0,7):C.GC_4187,(0,8):C.GC_4184,(0,0):C.GC_4184,(0,6):C.GC_4184,(0,3):C.GC_4187,(0,9):C.GC_4184,(0,4):C.GC_4187,(0,1):C.GC_4170,(0,5):C.GC_4171})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_64,(0,7):C.GC_3837,(0,15):C.GC_65,(0,18):C.GC_3836,(0,10):C.GC_3839,(0,16):C.GC_3840,(0,9):C.GC_67,(0,17):C.GC_3842,(0,5):C.GC_66,(0,0):C.GC_3843,(0,8):C.GC_3837,(0,14):C.GC_3843,(0,11):C.GC_3839,(0,4):C.GC_3836,(0,19):C.GC_3842,(0,12):C.GC_3840,(0,2):C.GC_3295,(0,3):C.GC_3829,(0,1):C.GC_3832,(0,13):C.GC_3831})

V_150 = Vertex(name = 'V_150',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4185,(0,7):C.GC_4185,(0,8):C.GC_4186,(0,0):C.GC_4186,(0,6):C.GC_4186,(0,3):C.GC_4185,(0,9):C.GC_4186,(0,4):C.GC_4185,(0,1):C.GC_4172,(0,5):C.GC_4169})

V_151 = Vertex(name = 'V_151',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_52,(0,7):C.GC_3046,(0,15):C.GC_52,(0,18):C.GC_3046,(0,10):C.GC_3841,(0,16):C.GC_3841,(0,9):C.GC_51,(0,17):C.GC_3838,(0,5):C.GC_51,(0,0):C.GC_3838,(0,8):C.GC_3046,(0,14):C.GC_3838,(0,11):C.GC_3841,(0,4):C.GC_3046,(0,19):C.GC_3838,(0,12):C.GC_3841,(0,2):C.GC_3294,(0,3):C.GC_3828,(0,1):C.GC_3830,(0,13):C.GC_3833})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_4187,(0,7):C.GC_4187,(0,8):C.GC_4184,(0,0):C.GC_4184,(0,6):C.GC_4184,(0,3):C.GC_4187,(0,9):C.GC_4184,(0,4):C.GC_4187,(0,1):C.GC_4170,(0,5):C.GC_4171})

V_153 = Vertex(name = 'V_153',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS2, L.VVVS22, L.VVVS23, L.VVVS28, L.VVVS29, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS52, L.VVVS55, L.VVVS58, L.VVVS62, L.VVVS8, L.VVVS9 ],
               couplings = {(0,8):C.GC_5453,(0,7):C.GC_5452,(0,4):C.GC_5451,(0,0):C.GC_6164,(0,19):C.GC_5451,(0,18):C.GC_6164,(0,2):C.GC_6163,(0,3):C.GC_6162,(0,1):C.GC_6166,(0,14):C.GC_5452,(0,17):C.GC_5452,(0,9):C.GC_6167,(0,12):C.GC_6165,(0,15):C.GC_6165,(0,6):C.GC_5454,(0,10):C.GC_6165,(0,16):C.GC_6164,(0,5):C.GC_5451,(0,11):C.GC_6165,(0,13):C.GC_6164})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS55, L.VVVS58, L.VVVS8 ],
               couplings = {(0,0):C.GC_6360,(0,9):C.GC_6360,(0,1):C.GC_6327,(0,2):C.GC_6328,(0,5):C.GC_6361,(0,7):C.GC_6361,(0,3):C.GC_6361,(0,8):C.GC_6360,(0,4):C.GC_6361,(0,6):C.GC_6360})

V_155 = Vertex(name = 'V_155',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,14):C.GC_6456,(0,13):C.GC_6455,(0,17):C.GC_5935,(0,16):C.GC_6156,(0,7):C.GC_6451,(0,0):C.GC_6445,(0,28):C.GC_5936,(0,15):C.GC_6160,(0,38):C.GC_6452,(0,37):C.GC_6440,(0,2):C.GC_5932,(0,3):C.GC_6149,(0,1):C.GC_6152,(0,5):C.GC_6148,(0,4):C.GC_6153,(0,8):C.GC_6157,(0,6):C.GC_6161,(0,23):C.GC_5934,(0,30):C.GC_6448,(0,35):C.GC_6455,(0,36):C.GC_6156,(0,18):C.GC_6150,(0,24):C.GC_6443,(0,31):C.GC_6438,(0,19):C.GC_6158,(0,25):C.GC_6151,(0,32):C.GC_6159,(0,10):C.GC_6453,(0,12):C.GC_5933,(0,20):C.GC_6438,(0,27):C.GC_6159,(0,33):C.GC_6445,(0,34):C.GC_6160,(0,9):C.GC_6452,(0,21):C.GC_6443,(0,26):C.GC_6440,(0,11):C.GC_6154,(0,22):C.GC_6161,(0,29):C.GC_6158})

V_156 = Vertex(name = 'V_156',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6580,(0,4):C.GC_6354,(0,19):C.GC_6582,(0,1):C.GC_6348,(0,2):C.GC_6349,(0,3):C.GC_6354,(0,5):C.GC_6346,(0,10):C.GC_6579,(0,15):C.GC_6581,(0,6):C.GC_6353,(0,11):C.GC_6347,(0,16):C.GC_6353,(0,7):C.GC_6581,(0,13):C.GC_6353,(0,17):C.GC_6580,(0,18):C.GC_6354,(0,8):C.GC_6579,(0,12):C.GC_6582,(0,9):C.GC_6354,(0,14):C.GC_6353})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS2, L.VVVS22, L.VVVS23, L.VVVS28, L.VVVS29, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS52, L.VVVS55, L.VVVS58, L.VVVS62, L.VVVS8, L.VVVS9 ],
               couplings = {(0,8):C.GC_5454,(0,7):C.GC_5451,(0,4):C.GC_5452,(0,0):C.GC_6164,(0,19):C.GC_5452,(0,18):C.GC_6164,(0,2):C.GC_6163,(0,3):C.GC_6162,(0,1):C.GC_6166,(0,14):C.GC_5451,(0,17):C.GC_5451,(0,9):C.GC_6167,(0,12):C.GC_6165,(0,15):C.GC_6165,(0,6):C.GC_5453,(0,10):C.GC_6165,(0,16):C.GC_6164,(0,5):C.GC_5452,(0,11):C.GC_6165,(0,13):C.GC_6164})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS55, L.VVVS58, L.VVVS8 ],
               couplings = {(0,0):C.GC_6360,(0,9):C.GC_6360,(0,1):C.GC_6327,(0,2):C.GC_6328,(0,5):C.GC_6361,(0,7):C.GC_6361,(0,3):C.GC_6361,(0,8):C.GC_6360,(0,4):C.GC_6361,(0,6):C.GC_6360})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,14):C.GC_6450,(0,13):C.GC_6449,(0,17):C.GC_5936,(0,16):C.GC_6157,(0,7):C.GC_6457,(0,0):C.GC_6444,(0,28):C.GC_5935,(0,15):C.GC_6161,(0,38):C.GC_6446,(0,37):C.GC_6441,(0,2):C.GC_5932,(0,3):C.GC_6149,(0,1):C.GC_6152,(0,5):C.GC_6148,(0,4):C.GC_6153,(0,8):C.GC_6156,(0,6):C.GC_6160,(0,23):C.GC_5933,(0,30):C.GC_6454,(0,35):C.GC_6449,(0,36):C.GC_6157,(0,18):C.GC_6150,(0,24):C.GC_6442,(0,31):C.GC_6439,(0,19):C.GC_6159,(0,25):C.GC_6151,(0,32):C.GC_6158,(0,10):C.GC_6447,(0,12):C.GC_5934,(0,20):C.GC_6439,(0,27):C.GC_6158,(0,33):C.GC_6444,(0,34):C.GC_6161,(0,9):C.GC_6446,(0,21):C.GC_6442,(0,26):C.GC_6441,(0,11):C.GC_6155,(0,22):C.GC_6160,(0,29):C.GC_6159})

V_160 = Vertex(name = 'V_160',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6580,(0,4):C.GC_6354,(0,19):C.GC_6582,(0,1):C.GC_6348,(0,2):C.GC_6349,(0,3):C.GC_6354,(0,5):C.GC_6346,(0,10):C.GC_6579,(0,15):C.GC_6581,(0,6):C.GC_6353,(0,11):C.GC_6347,(0,16):C.GC_6353,(0,7):C.GC_6581,(0,13):C.GC_6353,(0,17):C.GC_6580,(0,18):C.GC_6354,(0,8):C.GC_6579,(0,12):C.GC_6582,(0,9):C.GC_6354,(0,14):C.GC_6353})

V_161 = Vertex(name = 'V_161',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS2, L.VVVS22, L.VVVS23, L.VVVS28, L.VVVS29, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS52, L.VVVS55, L.VVVS58, L.VVVS62, L.VVVS8, L.VVVS9 ],
               couplings = {(0,8):C.GC_6418,(0,7):C.GC_6419,(0,4):C.GC_6419,(0,0):C.GC_6633,(0,19):C.GC_6419,(0,18):C.GC_6633,(0,2):C.GC_6632,(0,3):C.GC_6631,(0,1):C.GC_6635,(0,14):C.GC_6419,(0,17):C.GC_6419,(0,9):C.GC_6636,(0,12):C.GC_6634,(0,15):C.GC_6634,(0,6):C.GC_6418,(0,10):C.GC_6634,(0,16):C.GC_6633,(0,5):C.GC_6419,(0,11):C.GC_6634,(0,13):C.GC_6633})

V_162 = Vertex(name = 'V_162',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS15, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS45, L.VVVS48, L.VVVS55, L.VVVS58, L.VVVS8 ],
               couplings = {(0,0):C.GC_6662,(0,9):C.GC_6662,(0,1):C.GC_6652,(0,2):C.GC_6653,(0,5):C.GC_6663,(0,7):C.GC_6663,(0,3):C.GC_6663,(0,8):C.GC_6662,(0,4):C.GC_6663,(0,6):C.GC_6662})

V_163 = Vertex(name = 'V_163',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS15, L.VVVS16, L.VVVS17, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,15):C.GC_6193,(0,14):C.GC_6627,(0,18):C.GC_6193,(0,17):C.GC_6627,(0,8):C.GC_6194,(0,0):C.GC_6629,(0,29):C.GC_6193,(0,16):C.GC_6629,(0,39):C.GC_6627,(0,38):C.GC_6629,(0,2):C.GC_6420,(0,3):C.GC_6620,(0,1):C.GC_6621,(0,5):C.GC_6420,(0,6):C.GC_6620,(0,4):C.GC_6621,(0,9):C.GC_6627,(0,7):C.GC_6629,(0,24):C.GC_6194,(0,31):C.GC_6194,(0,36):C.GC_6627,(0,37):C.GC_6627,(0,19):C.GC_6622,(0,25):C.GC_6630,(0,32):C.GC_6630,(0,20):C.GC_6630,(0,26):C.GC_6622,(0,33):C.GC_6630,(0,11):C.GC_6193,(0,13):C.GC_6194,(0,21):C.GC_6630,(0,28):C.GC_6630,(0,34):C.GC_6629,(0,35):C.GC_6629,(0,10):C.GC_6627,(0,22):C.GC_6630,(0,27):C.GC_6629,(0,12):C.GC_6628,(0,23):C.GC_6629,(0,30):C.GC_6630})

V_164 = Vertex(name = 'V_164',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6660,(0,4):C.GC_6660,(0,19):C.GC_6660,(0,1):C.GC_6658,(0,2):C.GC_6658,(0,3):C.GC_6660,(0,5):C.GC_6659,(0,10):C.GC_6661,(0,15):C.GC_6661,(0,6):C.GC_6661,(0,11):C.GC_6659,(0,16):C.GC_6661,(0,7):C.GC_6661,(0,13):C.GC_6661,(0,17):C.GC_6660,(0,18):C.GC_6660,(0,8):C.GC_6661,(0,12):C.GC_6660,(0,9):C.GC_6660,(0,14):C.GC_6661})

V_165 = Vertex(name = 'V_165',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV111, L.VVVV112, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV124, L.VVVV125, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV144, L.VVVV145, L.VVVV147, L.VVVV15, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV16, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV179, L.VVVV18, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV190, L.VVVV197, L.VVVV198, L.VVVV2, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV21, L.VVVV211, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV58, L.VVVV59, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV81, L.VVVV89, L.VVVV90, L.VVVV91, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
               couplings = {(0,72):C.GC_7071,(0,78):C.GC_7071,(0,0):C.GC_7070,(0,54):C.GC_7070,(0,80):C.GC_4407,(0,81):C.GC_3885,(0,82):C.GC_3884,(0,77):C.GC_3882,(0,79):C.GC_3882,(0,85):C.GC_4408,(0,86):C.GC_3884,(0,87):C.GC_4419,(0,83):C.GC_4416,(0,84):C.GC_4416,(0,88):C.GC_3885,(0,89):C.GC_3884,(0,90):C.GC_4414,(0,91):C.GC_4413,(0,92):C.GC_3884,(0,93):C.GC_4419,(0,94):C.GC_4413,(0,95):C.GC_4414,(0,44):C.GC_3882,(0,50):C.GC_4416,(0,21):C.GC_4418,(0,27):C.GC_4467,(0,33):C.GC_4473,(0,69):C.GC_3882,(0,70):C.GC_4416,(0,62):C.GC_4467,(0,67):C.GC_4418,(0,68):C.GC_4473,(0,71):C.GC_4473,(0,73):C.GC_4473,(0,75):C.GC_4411,(0,76):C.GC_4412,(0,74):C.GC_4410,(0,96):C.GC_7094,(0,97):C.GC_7094,(0,108):C.GC_7070,(0,107):C.GC_7095,(0,4):C.GC_7070,(0,3):C.GC_7095,(0,15):C.GC_7070,(0,14):C.GC_7095,(0,32):C.GC_7070,(0,31):C.GC_7095,(0,49):C.GC_7092,(0,51):C.GC_7093,(0,48):C.GC_7097,(0,105):C.GC_4408,(0,106):C.GC_4407,(0,98):C.GC_4409,(0,109):C.GC_4472,(0,7):C.GC_4472,(0,16):C.GC_4472,(0,26):C.GC_7094,(0,36):C.GC_4472,(0,43):C.GC_7094,(0,52):C.GC_4473,(0,55):C.GC_4473,(0,63):C.GC_7096,(0,99):C.GC_4472,(0,1):C.GC_3883,(0,2):C.GC_4415,(0,110):C.GC_4417,(0,5):C.GC_4466,(0,17):C.GC_4466,(0,34):C.GC_4467,(0,37):C.GC_4473,(0,56):C.GC_4472,(0,101):C.GC_4472,(0,112):C.GC_4466,(0,12):C.GC_3883,(0,13):C.GC_4415,(0,9):C.GC_4417,(0,19):C.GC_4467,(0,22):C.GC_4473,(0,38):C.GC_4466,(0,58):C.GC_4472,(0,100):C.GC_4472,(0,111):C.GC_4466,(0,6):C.GC_4467,(0,8):C.GC_4473,(0,24):C.GC_3883,(0,25):C.GC_4415,(0,18):C.GC_4417,(0,35):C.GC_4466,(0,53):C.GC_4472,(0,28):C.GC_4418,(0,45):C.GC_4467,(0,64):C.GC_4473,(0,102):C.GC_4472,(0,113):C.GC_4467,(0,114):C.GC_4473,(0,10):C.GC_4466,(0,20):C.GC_4466,(0,41):C.GC_3883,(0,42):C.GC_4415,(0,39):C.GC_4417,(0,57):C.GC_4472,(0,29):C.GC_4467,(0,46):C.GC_4418,(0,65):C.GC_4473,(0,103):C.GC_4473,(0,104):C.GC_4473,(0,115):C.GC_4472,(0,11):C.GC_4472,(0,23):C.GC_4472,(0,40):C.GC_4472,(0,60):C.GC_4412,(0,61):C.GC_4411,(0,59):C.GC_4409,(0,30):C.GC_4473,(0,47):C.GC_4473,(0,66):C.GC_4410})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV102, L.VVVV117, L.VVVV124, L.VVVV135, L.VVVV14, L.VVVV147, L.VVVV153, L.VVVV156, L.VVVV172, L.VVVV179, L.VVVV186, L.VVVV188, L.VVVV205, L.VVVV211, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV67, L.VVVV80, L.VVVV90 ],
               couplings = {(0,4):C.GC_4471,(0,15):C.GC_4471,(0,16):C.GC_4469,(0,17):C.GC_7111,(0,18):C.GC_7111,(0,20):C.GC_7112,(0,0):C.GC_7112,(0,2):C.GC_7112,(0,7):C.GC_7112,(0,11):C.GC_7102,(0,19):C.GC_4468,(0,5):C.GC_7111,(0,9):C.GC_7111,(0,13):C.GC_7101,(0,21):C.GC_4470,(0,1):C.GC_4470,(0,3):C.GC_4470,(0,6):C.GC_4471,(0,8):C.GC_4470,(0,10):C.GC_4471,(0,12):C.GC_4468,(0,14):C.GC_4469})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV1, L.VVVV10, L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV106, L.VVVV109, L.VVVV111, L.VVVV112, L.VVVV113, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV124, L.VVVV125, L.VVVV126, L.VVVV129, L.VVVV130, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV136, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV143, L.VVVV144, L.VVVV145, L.VVVV147, L.VVVV148, L.VVVV15, L.VVVV150, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV156, L.VVVV157, L.VVVV158, L.VVVV16, L.VVVV160, L.VVVV162, L.VVVV163, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV176, L.VVVV179, L.VVVV18, L.VVVV180, L.VVVV182, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV188, L.VVVV189, L.VVVV19, L.VVVV190, L.VVVV191, L.VVVV193, L.VVVV195, L.VVVV197, L.VVVV198, L.VVVV2, L.VVVV20, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV208, L.VVVV21, L.VVVV211, L.VVVV212, L.VVVV214, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV29, L.VVVV3, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV34, L.VVVV35, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV58, L.VVVV59, L.VVVV6, L.VVVV60, L.VVVV62, L.VVVV64, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV70, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV81, L.VVVV82, L.VVVV84, L.VVVV86, L.VVVV89, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
               couplings = {(0,99):C.GC_7018,(0,107):C.GC_7018,(0,0):C.GC_7089,(0,76):C.GC_7089,(0,148):C.GC_7018,(0,1):C.GC_7017,(0,127):C.GC_7089,(0,134):C.GC_7088,(0,104):C.GC_7017,(0,105):C.GC_7017,(0,109):C.GC_4295,(0,110):C.GC_4294,(0,111):C.GC_4293,(0,106):C.GC_4295,(0,108):C.GC_4291,(0,114):C.GC_4296,(0,115):C.GC_4301,(0,116):C.GC_4302,(0,112):C.GC_4296,(0,113):C.GC_4298,(0,117):C.GC_4294,(0,118):C.GC_4301,(0,119):C.GC_4294,(0,120):C.GC_4301,(0,121):C.GC_4293,(0,122):C.GC_4302,(0,123):C.GC_4293,(0,124):C.GC_4302,(0,61):C.GC_4295,(0,69):C.GC_4296,(0,30):C.GC_4300,(0,38):C.GC_4399,(0,46):C.GC_4399,(0,77):C.GC_7088,(0,95):C.GC_4291,(0,96):C.GC_4298,(0,86):C.GC_4399,(0,93):C.GC_4300,(0,94):C.GC_4399,(0,97):C.GC_7088,(0,98):C.GC_4399,(0,100):C.GC_4399,(0,102):C.GC_4291,(0,103):C.GC_4298,(0,101):C.GC_4300,(0,125):C.GC_7090,(0,126):C.GC_7090,(0,129):C.GC_7017,(0,128):C.GC_7091,(0,135):C.GC_7018,(0,130):C.GC_7091,(0,143):C.GC_7017,(0,142):C.GC_7091,(0,144):C.GC_7090,(0,145):C.GC_7090,(0,151):C.GC_7018,(0,146):C.GC_7091,(0,5):C.GC_7017,(0,4):C.GC_7091,(0,7):C.GC_7018,(0,6):C.GC_7091,(0,8):C.GC_7090,(0,11):C.GC_7090,(0,20):C.GC_7089,(0,19):C.GC_7091,(0,22):C.GC_7089,(0,21):C.GC_7091,(0,27):C.GC_7072,(0,33):C.GC_7085,(0,23):C.GC_7087,(0,44):C.GC_7089,(0,43):C.GC_7091,(0,47):C.GC_7072,(0,48):C.GC_7085,(0,45):C.GC_7087,(0,59):C.GC_7089,(0,49):C.GC_7091,(0,68):C.GC_7072,(0,70):C.GC_7085,(0,67):C.GC_7087,(0,72):C.GC_7089,(0,71):C.GC_7091,(0,85):C.GC_7089,(0,73):C.GC_7091,(0,140):C.GC_4296,(0,141):C.GC_4295,(0,131):C.GC_4299,(0,147):C.GC_4400,(0,12):C.GC_4400,(0,24):C.GC_4400,(0,36):C.GC_7090,(0,52):C.GC_4400,(0,60):C.GC_7090,(0,74):C.GC_4399,(0,78):C.GC_4399,(0,87):C.GC_7086,(0,132):C.GC_4400,(0,2):C.GC_4296,(0,3):C.GC_4295,(0,149):C.GC_4299,(0,9):C.GC_4400,(0,25):C.GC_4400,(0,37):C.GC_7090,(0,50):C.GC_4399,(0,53):C.GC_4399,(0,62):C.GC_7086,(0,79):C.GC_4400,(0,88):C.GC_7090,(0,136):C.GC_4400,(0,152):C.GC_4400,(0,17):C.GC_4296,(0,18):C.GC_4295,(0,14):C.GC_4299,(0,28):C.GC_4399,(0,31):C.GC_4399,(0,39):C.GC_7086,(0,54):C.GC_4400,(0,63):C.GC_7090,(0,81):C.GC_4400,(0,89):C.GC_7090,(0,133):C.GC_4400,(0,150):C.GC_4400,(0,10):C.GC_4399,(0,13):C.GC_4399,(0,34):C.GC_4292,(0,35):C.GC_4297,(0,26):C.GC_4299,(0,51):C.GC_4400,(0,75):C.GC_4400,(0,40):C.GC_4300,(0,64):C.GC_4399,(0,90):C.GC_4399,(0,137):C.GC_4400,(0,153):C.GC_4399,(0,154):C.GC_4399,(0,15):C.GC_4400,(0,29):C.GC_4400,(0,57):C.GC_4292,(0,58):C.GC_4297,(0,55):C.GC_4299,(0,80):C.GC_4400,(0,41):C.GC_4399,(0,65):C.GC_4300,(0,91):C.GC_4399,(0,138):C.GC_4399,(0,139):C.GC_4399,(0,155):C.GC_4400,(0,16):C.GC_4400,(0,32):C.GC_4400,(0,56):C.GC_4400,(0,83):C.GC_4292,(0,84):C.GC_4297,(0,82):C.GC_4299,(0,42):C.GC_4399,(0,66):C.GC_4399,(0,92):C.GC_4300})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV102, L.VVVV104, L.VVVV109, L.VVVV113, L.VVVV117, L.VVVV124, L.VVVV126, L.VVVV130, L.VVVV135, L.VVVV14, L.VVVV147, L.VVVV148, L.VVVV150, L.VVVV153, L.VVVV156, L.VVVV158, L.VVVV163, L.VVVV172, L.VVVV179, L.VVVV180, L.VVVV182, L.VVVV186, L.VVVV188, L.VVVV191, L.VVVV195, L.VVVV205, L.VVVV211, L.VVVV212, L.VVVV214, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV58, L.VVVV59, L.VVVV60, L.VVVV64, L.VVVV67, L.VVVV80, L.VVVV82, L.VVVV84, L.VVVV86, L.VVVV90 ],
               couplings = {(0,9):C.GC_4397,(0,30):C.GC_4397,(0,31):C.GC_4397,(0,32):C.GC_7109,(0,33):C.GC_7109,(0,34):C.GC_7110,(0,35):C.GC_7110,(0,37):C.GC_7110,(0,38):C.GC_7109,(0,39):C.GC_7109,(0,40):C.GC_7110,(0,0):C.GC_7110,(0,1):C.GC_7110,(0,2):C.GC_7109,(0,3):C.GC_7109,(0,5):C.GC_7110,(0,6):C.GC_7110,(0,7):C.GC_7108,(0,14):C.GC_7110,(0,15):C.GC_7108,(0,16):C.GC_7110,(0,22):C.GC_7108,(0,23):C.GC_7110,(0,24):C.GC_7110,(0,36):C.GC_4398,(0,10):C.GC_7109,(0,18):C.GC_7109,(0,26):C.GC_7107,(0,41):C.GC_4398,(0,11):C.GC_7109,(0,19):C.GC_7107,(0,27):C.GC_7109,(0,4):C.GC_4398,(0,12):C.GC_7107,(0,20):C.GC_7109,(0,28):C.GC_7109,(0,8):C.GC_4398,(0,13):C.GC_4397,(0,17):C.GC_4398,(0,21):C.GC_4397,(0,25):C.GC_4398,(0,29):C.GC_4397})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,5):C.GC_3286,(0,6):C.GC_3271,(0,14):C.GC_3289,(0,17):C.GC_3268,(0,9):C.GC_3257,(0,15):C.GC_3260,(0,8):C.GC_3272,(0,16):C.GC_3259,(0,4):C.GC_3269,(0,0):C.GC_3262,(0,7):C.GC_3271,(0,13):C.GC_3262,(0,10):C.GC_3257,(0,3):C.GC_3268,(0,18):C.GC_3259,(0,11):C.GC_3260,(0,2):C.GC_43,(0,1):C.GC_47,(0,12):C.GC_46})

V_170 = Vertex(name = 'V_170',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_3716,(0,7):C.GC_3714,(0,8):C.GC_3717,(0,0):C.GC_3715,(0,6):C.GC_3715,(0,3):C.GC_3716,(0,9):C.GC_3717,(0,4):C.GC_3714,(0,1):C.GC_504,(0,5):C.GC_503})

V_171 = Vertex(name = 'V_171',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,5):C.GC_3277,(0,6):C.GC_3278,(0,14):C.GC_3275,(0,17):C.GC_3281,(0,9):C.GC_3265,(0,15):C.GC_3252,(0,8):C.GC_3279,(0,16):C.GC_3267,(0,4):C.GC_3282,(0,0):C.GC_3254,(0,7):C.GC_3278,(0,13):C.GC_3254,(0,10):C.GC_3265,(0,3):C.GC_3281,(0,18):C.GC_3267,(0,11):C.GC_3252,(0,2):C.GC_42,(0,1):C.GC_48,(0,12):C.GC_45})

V_172 = Vertex(name = 'V_172',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_3712,(0,7):C.GC_3718,(0,8):C.GC_3713,(0,0):C.GC_3719,(0,6):C.GC_3719,(0,3):C.GC_3712,(0,9):C.GC_3713,(0,4):C.GC_3718,(0,1):C.GC_505,(0,5):C.GC_502})

V_173 = Vertex(name = 'V_173',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,5):C.GC_3270,(0,6):C.GC_3287,(0,14):C.GC_3273,(0,17):C.GC_3284,(0,9):C.GC_3256,(0,15):C.GC_3261,(0,8):C.GC_3288,(0,16):C.GC_3258,(0,4):C.GC_3285,(0,0):C.GC_3263,(0,7):C.GC_3287,(0,13):C.GC_3263,(0,10):C.GC_3256,(0,3):C.GC_3284,(0,18):C.GC_3258,(0,11):C.GC_3261,(0,2):C.GC_43,(0,1):C.GC_47,(0,12):C.GC_46})

V_174 = Vertex(name = 'V_174',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_3716,(0,7):C.GC_3714,(0,8):C.GC_3717,(0,0):C.GC_3715,(0,6):C.GC_3715,(0,3):C.GC_3716,(0,9):C.GC_3717,(0,4):C.GC_3714,(0,1):C.GC_504,(0,5):C.GC_503})

V_175 = Vertex(name = 'V_175',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,5):C.GC_3274,(0,6):C.GC_3281,(0,14):C.GC_3276,(0,17):C.GC_3278,(0,9):C.GC_3255,(0,15):C.GC_3266,(0,8):C.GC_3283,(0,16):C.GC_3253,(0,4):C.GC_3280,(0,0):C.GC_3264,(0,7):C.GC_3281,(0,13):C.GC_3264,(0,10):C.GC_3255,(0,3):C.GC_3278,(0,18):C.GC_3253,(0,11):C.GC_3266,(0,2):C.GC_44,(0,1):C.GC_45,(0,12):C.GC_48})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS24, L.VVSS3, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,2):C.GC_3719,(0,7):C.GC_3713,(0,8):C.GC_3718,(0,0):C.GC_3712,(0,6):C.GC_3712,(0,3):C.GC_3719,(0,9):C.GC_3718,(0,4):C.GC_3713,(0,1):C.GC_502,(0,5):C.GC_505})

V_177 = Vertex(name = 'V_177',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS15, L.VVVS16, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,13):C.GC_5865,(0,12):C.GC_5447,(0,16):C.GC_5866,(0,15):C.GC_5445,(0,6):C.GC_5876,(0,0):C.GC_5892,(0,27):C.GC_5864,(0,14):C.GC_5894,(0,37):C.GC_5448,(0,36):C.GC_5895,(0,2):C.GC_4994,(0,1):C.GC_5000,(0,4):C.GC_4994,(0,3):C.GC_5000,(0,7):C.GC_5446,(0,5):C.GC_5893,(0,22):C.GC_5877,(0,29):C.GC_5878,(0,34):C.GC_5447,(0,35):C.GC_5445,(0,17):C.GC_4997,(0,23):C.GC_5880,(0,30):C.GC_5883,(0,18):C.GC_5882,(0,24):C.GC_4997,(0,31):C.GC_5881,(0,9):C.GC_5867,(0,11):C.GC_5879,(0,19):C.GC_5883,(0,26):C.GC_5881,(0,32):C.GC_5892,(0,33):C.GC_5894,(0,8):C.GC_5448,(0,20):C.GC_5880,(0,25):C.GC_5895,(0,10):C.GC_5447,(0,21):C.GC_5893,(0,28):C.GC_5882})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6070,(0,4):C.GC_6070,(0,19):C.GC_6069,(0,1):C.GC_5131,(0,2):C.GC_5131,(0,3):C.GC_6069,(0,5):C.GC_5128,(0,10):C.GC_6064,(0,15):C.GC_6063,(0,6):C.GC_6064,(0,11):C.GC_5128,(0,16):C.GC_6063,(0,7):C.GC_6063,(0,13):C.GC_6063,(0,17):C.GC_6070,(0,18):C.GC_6070,(0,8):C.GC_6064,(0,12):C.GC_6069,(0,9):C.GC_6069,(0,14):C.GC_6064})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS12, L.VVVS15, L.VVVS16, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,13):C.GC_5873,(0,12):C.GC_5450,(0,16):C.GC_5869,(0,15):C.GC_5449,(0,6):C.GC_5868,(0,0):C.GC_5885,(0,27):C.GC_5871,(0,14):C.GC_5888,(0,37):C.GC_5449,(0,36):C.GC_5886,(0,2):C.GC_4995,(0,1):C.GC_4999,(0,4):C.GC_4996,(0,3):C.GC_4998,(0,7):C.GC_5450,(0,5):C.GC_5891,(0,22):C.GC_5874,(0,29):C.GC_5870,(0,34):C.GC_5450,(0,35):C.GC_5449,(0,17):C.GC_4999,(0,23):C.GC_5889,(0,30):C.GC_5890,(0,18):C.GC_5884,(0,24):C.GC_4998,(0,31):C.GC_5887,(0,9):C.GC_5875,(0,11):C.GC_5872,(0,19):C.GC_5890,(0,26):C.GC_5887,(0,32):C.GC_5885,(0,33):C.GC_5888,(0,8):C.GC_5449,(0,20):C.GC_5889,(0,25):C.GC_5886,(0,10):C.GC_5444,(0,21):C.GC_5891,(0,28):C.GC_5884})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS10, L.VVVS15, L.VVVS18, L.VVVS3, L.VVVS35, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS45, L.VVVS46, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS8 ],
               couplings = {(0,0):C.GC_6065,(0,4):C.GC_6068,(0,19):C.GC_6066,(0,1):C.GC_5130,(0,2):C.GC_5129,(0,3):C.GC_6067,(0,5):C.GC_5130,(0,10):C.GC_6067,(0,15):C.GC_6068,(0,6):C.GC_6066,(0,11):C.GC_5129,(0,16):C.GC_6065,(0,7):C.GC_6068,(0,13):C.GC_6065,(0,17):C.GC_6065,(0,18):C.GC_6068,(0,8):C.GC_6067,(0,12):C.GC_6066,(0,9):C.GC_6067,(0,14):C.GC_6066})

V_181 = Vertex(name = 'V_181',
               particles = [ P.a, P.a, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS4, L.VVSS8 ],
               couplings = {(0,2):C.GC_2790,(0,3):C.GC_2790,(0,6):C.GC_2789,(0,7):C.GC_2789,(0,5):C.GC_2789,(0,1):C.GC_2790,(0,4):C.GC_2790,(0,0):C.GC_2789})

V_182 = Vertex(name = 'V_182',
               particles = [ P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS2, L.VVSS22, L.VVSS23, L.VVSS3, L.VVSS4, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,3):C.GC_50,(0,4):C.GC_3044,(0,11):C.GC_49,(0,14):C.GC_3045,(0,7):C.GC_3835,(0,12):C.GC_3834,(0,6):C.GC_49,(0,13):C.GC_3835,(0,2):C.GC_50,(0,0):C.GC_3834,(0,5):C.GC_3044,(0,10):C.GC_3834,(0,8):C.GC_3835,(0,1):C.GC_3045,(0,15):C.GC_3835,(0,9):C.GC_3834})

V_183 = Vertex(name = 'V_183',
               particles = [ P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17, L.VVSS18, L.VVSS19, L.VVSS4, L.VVSS8 ],
               couplings = {(0,2):C.GC_2789,(0,3):C.GC_2789,(0,6):C.GC_2790,(0,7):C.GC_2790,(0,5):C.GC_2790,(0,1):C.GC_2789,(0,4):C.GC_2789,(0,0):C.GC_2790})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS22, L.VVVS23, L.VVVS28, L.VVVS29, L.VVVS52, L.VVVS62, L.VVVS9 ],
               couplings = {(0,4):C.GC_6416,(0,3):C.GC_6417,(0,0):C.GC_6416,(0,7):C.GC_6416,(0,5):C.GC_6417,(0,6):C.GC_6417,(0,2):C.GC_6417,(0,1):C.GC_6416})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS18, L.VVVS2, L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS26, L.VVVS28, L.VVVS29, L.VVVS3, L.VVVS31, L.VVVS32, L.VVVS36, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS42, L.VVVS45, L.VVVS48, L.VVVS49, L.VVVS5, L.VVVS51, L.VVVS52, L.VVVS55, L.VVVS56, L.VVVS58, L.VVVS59, L.VVVS62, L.VVVS63, L.VVVS8, L.VVVS9 ],
               couplings = {(0,9):C.GC_6191,(0,8):C.GC_6625,(0,12):C.GC_6191,(0,11):C.GC_6625,(0,2):C.GC_6191,(0,0):C.GC_6623,(0,21):C.GC_6192,(0,10):C.GC_6623,(0,31):C.GC_6626,(0,30):C.GC_6624,(0,3):C.GC_6626,(0,1):C.GC_6624,(0,17):C.GC_6192,(0,23):C.GC_6192,(0,28):C.GC_6625,(0,29):C.GC_6625,(0,18):C.GC_6623,(0,24):C.GC_6624,(0,13):C.GC_6623,(0,25):C.GC_6624,(0,5):C.GC_6192,(0,7):C.GC_6191,(0,14):C.GC_6624,(0,20):C.GC_6624,(0,26):C.GC_6623,(0,27):C.GC_6623,(0,4):C.GC_6626,(0,15):C.GC_6623,(0,19):C.GC_6624,(0,6):C.GC_6625,(0,16):C.GC_6624,(0,22):C.GC_6623})

V_186 = Vertex(name = 'V_186',
               particles = [ P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS13, L.VVVS2, L.VVVS20, L.VVVS21, L.VVVS22, L.VVVS23, L.VVVS24, L.VVVS25, L.VVVS26, L.VVVS27, L.VVVS28, L.VVVS29, L.VVVS30, L.VVVS31, L.VVVS32, L.VVVS33, L.VVVS42, L.VVVS43, L.VVVS5, L.VVVS52, L.VVVS53, L.VVVS62, L.VVVS63, L.VVVS9 ],
               couplings = {(0,11):C.GC_6417,(0,10):C.GC_6416,(0,14):C.GC_6417,(0,15):C.GC_6417,(0,12):C.GC_6416,(0,13):C.GC_6416,(0,1):C.GC_6417,(0,18):C.GC_6416,(0,23):C.GC_6417,(0,0):C.GC_6416,(0,2):C.GC_6417,(0,3):C.GC_6416,(0,16):C.GC_6416,(0,17):C.GC_6416,(0,19):C.GC_6416,(0,20):C.GC_6416,(0,21):C.GC_6416,(0,22):C.GC_6416,(0,5):C.GC_6416,(0,8):C.GC_6417,(0,4):C.GC_6417,(0,9):C.GC_6416,(0,6):C.GC_6416,(0,7):C.GC_6417})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV100, L.VVVV101, L.VVVV111, L.VVVV112, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV144, L.VVVV145, L.VVVV15, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV16, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV18, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV19, L.VVVV197, L.VVVV198, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV21, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV29, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV39, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV89, L.VVVV90, L.VVVV91, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
               couplings = {(0,64):C.GC_4420,(0,65):C.GC_4423,(0,66):C.GC_4422,(0,62):C.GC_4420,(0,63):C.GC_4420,(0,69):C.GC_4421,(0,70):C.GC_4422,(0,71):C.GC_4423,(0,67):C.GC_4421,(0,68):C.GC_4421,(0,72):C.GC_4423,(0,73):C.GC_4422,(0,74):C.GC_4423,(0,75):C.GC_4422,(0,76):C.GC_4422,(0,77):C.GC_4423,(0,78):C.GC_4422,(0,79):C.GC_4423,(0,35):C.GC_4420,(0,39):C.GC_4421,(0,16):C.GC_4425,(0,21):C.GC_4465,(0,25):C.GC_4465,(0,55):C.GC_4420,(0,56):C.GC_4421,(0,49):C.GC_4465,(0,53):C.GC_4425,(0,54):C.GC_4465,(0,57):C.GC_4465,(0,58):C.GC_4465,(0,60):C.GC_4420,(0,61):C.GC_4421,(0,59):C.GC_4425,(0,87):C.GC_4421,(0,88):C.GC_4420,(0,80):C.GC_4424,(0,89):C.GC_4464,(0,4):C.GC_4464,(0,11):C.GC_4464,(0,28):C.GC_4464,(0,40):C.GC_4465,(0,42):C.GC_4465,(0,81):C.GC_4464,(0,0):C.GC_4421,(0,1):C.GC_4420,(0,90):C.GC_4424,(0,2):C.GC_4464,(0,12):C.GC_4464,(0,26):C.GC_4465,(0,29):C.GC_4465,(0,43):C.GC_4464,(0,83):C.GC_4464,(0,92):C.GC_4464,(0,9):C.GC_4421,(0,10):C.GC_4420,(0,6):C.GC_4424,(0,14):C.GC_4465,(0,17):C.GC_4465,(0,30):C.GC_4464,(0,45):C.GC_4464,(0,82):C.GC_4464,(0,91):C.GC_4464,(0,3):C.GC_4465,(0,5):C.GC_4465,(0,19):C.GC_4421,(0,20):C.GC_4420,(0,13):C.GC_4424,(0,27):C.GC_4464,(0,41):C.GC_4464,(0,22):C.GC_4425,(0,36):C.GC_4465,(0,50):C.GC_4465,(0,84):C.GC_4464,(0,93):C.GC_4465,(0,94):C.GC_4465,(0,7):C.GC_4464,(0,15):C.GC_4464,(0,33):C.GC_4421,(0,34):C.GC_4420,(0,31):C.GC_4424,(0,44):C.GC_4464,(0,23):C.GC_4465,(0,37):C.GC_4425,(0,51):C.GC_4465,(0,85):C.GC_4465,(0,86):C.GC_4465,(0,95):C.GC_4464,(0,8):C.GC_4464,(0,18):C.GC_4464,(0,32):C.GC_4464,(0,47):C.GC_4421,(0,48):C.GC_4420,(0,46):C.GC_4424,(0,24):C.GC_4465,(0,38):C.GC_4465,(0,52):C.GC_4425})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV117, L.VVVV135, L.VVVV14, L.VVVV153, L.VVVV172, L.VVVV186, L.VVVV205, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV67, L.VVVV90 ],
               couplings = {(0,2):C.GC_4463,(0,8):C.GC_4463,(0,9):C.GC_4463,(0,10):C.GC_4462,(0,11):C.GC_4462,(0,0):C.GC_4462,(0,1):C.GC_4462,(0,3):C.GC_4463,(0,4):C.GC_4462,(0,5):C.GC_4463,(0,6):C.GC_4462,(0,7):C.GC_4463})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV100, L.VVVV101, L.VVVV111, L.VVVV112, L.VVVV115, L.VVVV116, L.VVVV117, L.VVVV118, L.VVVV119, L.VVVV120, L.VVVV121, L.VVVV133, L.VVVV134, L.VVVV135, L.VVVV138, L.VVVV139, L.VVVV14, L.VVVV140, L.VVVV141, L.VVVV144, L.VVVV145, L.VVVV15, L.VVVV153, L.VVVV154, L.VVVV155, L.VVVV16, L.VVVV165, L.VVVV166, L.VVVV169, L.VVVV170, L.VVVV171, L.VVVV172, L.VVVV173, L.VVVV174, L.VVVV175, L.VVVV18, L.VVVV185, L.VVVV186, L.VVVV187, L.VVVV19, L.VVVV197, L.VVVV198, L.VVVV201, L.VVVV202, L.VVVV203, L.VVVV204, L.VVVV205, L.VVVV206, L.VVVV207, L.VVVV21, L.VVVV217, L.VVVV218, L.VVVV219, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV29, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV33, L.VVVV39, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV44, L.VVVV45, L.VVVV46, L.VVVV47, L.VVVV48, L.VVVV49, L.VVVV50, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV54, L.VVVV55, L.VVVV56, L.VVVV57, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV75, L.VVVV78, L.VVVV79, L.VVVV89, L.VVVV90, L.VVVV91, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
               couplings = {(0,64):C.GC_4303,(0,65):C.GC_4311,(0,66):C.GC_4309,(0,62):C.GC_4303,(0,63):C.GC_4303,(0,69):C.GC_4308,(0,70):C.GC_4310,(0,71):C.GC_4312,(0,67):C.GC_4308,(0,68):C.GC_4308,(0,72):C.GC_4311,(0,73):C.GC_4309,(0,74):C.GC_4311,(0,75):C.GC_4309,(0,76):C.GC_4310,(0,77):C.GC_4312,(0,78):C.GC_4310,(0,79):C.GC_4312,(0,35):C.GC_4304,(0,39):C.GC_4307,(0,16):C.GC_4314,(0,21):C.GC_4395,(0,25):C.GC_4395,(0,55):C.GC_4304,(0,56):C.GC_4307,(0,49):C.GC_4395,(0,53):C.GC_4314,(0,54):C.GC_4395,(0,57):C.GC_4395,(0,58):C.GC_4395,(0,60):C.GC_4304,(0,61):C.GC_4307,(0,59):C.GC_4314,(0,87):C.GC_4306,(0,88):C.GC_4305,(0,80):C.GC_4313,(0,89):C.GC_4396,(0,4):C.GC_4396,(0,11):C.GC_4396,(0,28):C.GC_4396,(0,40):C.GC_4395,(0,42):C.GC_4395,(0,81):C.GC_4396,(0,0):C.GC_4306,(0,1):C.GC_4305,(0,90):C.GC_4313,(0,2):C.GC_4396,(0,12):C.GC_4396,(0,26):C.GC_4395,(0,29):C.GC_4395,(0,43):C.GC_4396,(0,83):C.GC_4396,(0,92):C.GC_4396,(0,9):C.GC_4307,(0,10):C.GC_4304,(0,6):C.GC_4313,(0,14):C.GC_4395,(0,17):C.GC_4395,(0,30):C.GC_4396,(0,45):C.GC_4396,(0,82):C.GC_4396,(0,91):C.GC_4396,(0,3):C.GC_4395,(0,5):C.GC_4395,(0,19):C.GC_4306,(0,20):C.GC_4305,(0,13):C.GC_4313,(0,27):C.GC_4396,(0,41):C.GC_4396,(0,22):C.GC_4314,(0,36):C.GC_4395,(0,50):C.GC_4395,(0,84):C.GC_4396,(0,93):C.GC_4395,(0,94):C.GC_4395,(0,7):C.GC_4396,(0,15):C.GC_4396,(0,33):C.GC_4307,(0,34):C.GC_4304,(0,31):C.GC_4313,(0,44):C.GC_4396,(0,23):C.GC_4395,(0,37):C.GC_4314,(0,51):C.GC_4395,(0,85):C.GC_4395,(0,86):C.GC_4395,(0,95):C.GC_4396,(0,8):C.GC_4396,(0,18):C.GC_4396,(0,32):C.GC_4396,(0,47):C.GC_4307,(0,48):C.GC_4304,(0,46):C.GC_4313,(0,24):C.GC_4395,(0,38):C.GC_4395,(0,52):C.GC_4314})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV117, L.VVVV135, L.VVVV14, L.VVVV153, L.VVVV172, L.VVVV186, L.VVVV205, L.VVVV219, L.VVVV22, L.VVVV31, L.VVVV67, L.VVVV90 ],
               couplings = {(0,2):C.GC_4393,(0,8):C.GC_4393,(0,9):C.GC_4393,(0,10):C.GC_4394,(0,11):C.GC_4394,(0,0):C.GC_4394,(0,1):C.GC_4394,(0,3):C.GC_4393,(0,4):C.GC_4394,(0,5):C.GC_4393,(0,6):C.GC_4394,(0,7):C.GC_4393})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_105,(0,3):C.GC_104,(0,1):C.GC_415,(0,4):C.GC_414,(0,2):C.GC_415,(0,5):C.GC_414})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_595,(0,3):C.GC_594,(0,1):C.GC_634,(0,4):C.GC_633,(0,2):C.GC_634,(0,5):C.GC_633})

V_193 = Vertex(name = 'V_193',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_103,(0,6):C.GC_103,(0,4):C.GC_418,(0,7):C.GC_417,(0,9):C.GC_418,(0,11):C.GC_417,(0,5):C.GC_418,(0,8):C.GC_417,(0,10):C.GC_418,(0,1):C.GC_417,(0,2):C.GC_102,(0,3):C.GC_102})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_580,(0,6):C.GC_580,(0,4):C.GC_636,(0,7):C.GC_635,(0,9):C.GC_636,(0,11):C.GC_635,(0,5):C.GC_636,(0,8):C.GC_635,(0,10):C.GC_636,(0,1):C.GC_635,(0,2):C.GC_579,(0,3):C.GC_579})

V_195 = Vertex(name = 'V_195',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS4, L.VSSSS5, L.VSSSS8 ],
               couplings = {(0,1):C.GC_413,(0,2):C.GC_413,(0,3):C.GC_416,(0,0):C.GC_416})

V_196 = Vertex(name = 'V_196',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS4, L.VSSSS5, L.VSSSS8 ],
               couplings = {(0,1):C.GC_637,(0,2):C.GC_637,(0,3):C.GC_632,(0,0):C.GC_632})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS5, L.VSSSS6, L.VSSSS9 ],
               couplings = {(0,3):C.GC_415,(0,5):C.GC_415,(0,4):C.GC_414,(0,0):C.GC_414,(0,1):C.GC_105,(0,2):C.GC_104})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS5, L.VSSSS6, L.VSSSS9 ],
               couplings = {(0,3):C.GC_634,(0,5):C.GC_634,(0,4):C.GC_633,(0,0):C.GC_633,(0,1):C.GC_595,(0,2):C.GC_594})

V_199 = Vertex(name = 'V_199',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_5994,(0,1):C.GC_5994,(0,2):C.GC_5017})

V_200 = Vertex(name = 'V_200',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_6121,(0,1):C.GC_6121,(0,2):C.GC_5177})

V_201 = Vertex(name = 'V_201',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1033,(0,6):C.GC_2207,(0,4):C.GC_1033,(0,7):C.GC_2207,(0,9):C.GC_1027,(0,11):C.GC_1027,(0,5):C.GC_1033,(0,8):C.GC_2207,(0,10):C.GC_1027,(0,1):C.GC_1027,(0,2):C.GC_1027,(0,3):C.GC_1027})

V_202 = Vertex(name = 'V_202',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1362,(0,6):C.GC_2714,(0,4):C.GC_1362,(0,7):C.GC_2714,(0,9):C.GC_1360,(0,11):C.GC_1360,(0,5):C.GC_1362,(0,8):C.GC_2714,(0,10):C.GC_1360,(0,1):C.GC_1360,(0,2):C.GC_1360,(0,3):C.GC_1360})

V_203 = Vertex(name = 'V_203',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5015,(0,1):C.GC_5996,(0,2):C.GC_5015,(0,3):C.GC_5995,(0,4):C.GC_5996,(0,5):C.GC_5995,(0,6):C.GC_5996,(0,7):C.GC_5996,(0,8):C.GC_5014})

V_204 = Vertex(name = 'V_204',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5167,(0,1):C.GC_6122,(0,2):C.GC_5167,(0,3):C.GC_6117,(0,4):C.GC_6122,(0,5):C.GC_6117,(0,6):C.GC_6122,(0,7):C.GC_6122,(0,8):C.GC_5166})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2208,(0,5):C.GC_1031,(0,3):C.GC_1029,(0,6):C.GC_1028,(0,8):C.GC_2199,(0,4):C.GC_1029,(0,7):C.GC_1028,(0,9):C.GC_2199,(0,1):C.GC_1023,(0,2):C.GC_1023})

V_206 = Vertex(name = 'V_206',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2715,(0,5):C.GC_1355,(0,3):C.GC_1368,(0,6):C.GC_1356,(0,8):C.GC_2690,(0,4):C.GC_1368,(0,7):C.GC_1356,(0,9):C.GC_2690,(0,1):C.GC_1367,(0,2):C.GC_1367})

V_207 = Vertex(name = 'V_207',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2200,(0,5):C.GC_2200,(0,3):C.GC_2197,(0,7):C.GC_2197,(0,4):C.GC_2206,(0,6):C.GC_1035,(0,8):C.GC_2206,(0,1):C.GC_1035,(0,2):C.GC_2203})

V_208 = Vertex(name = 'V_208',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2691,(0,5):C.GC_2691,(0,3):C.GC_2738,(0,7):C.GC_2738,(0,4):C.GC_2713,(0,6):C.GC_1364,(0,8):C.GC_2713,(0,1):C.GC_1364,(0,2):C.GC_2694})

V_209 = Vertex(name = 'V_209',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1038,(0,4):C.GC_2205,(0,2):C.GC_1038,(0,5):C.GC_2205,(0,6):C.GC_2199,(0,8):C.GC_2199,(0,3):C.GC_2204,(0,7):C.GC_2196,(0,1):C.GC_2196})

V_210 = Vertex(name = 'V_210',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1369,(0,4):C.GC_2712,(0,2):C.GC_1369,(0,5):C.GC_2712,(0,6):C.GC_2690,(0,8):C.GC_2690,(0,3):C.GC_2695,(0,7):C.GC_2737,(0,1):C.GC_2737})

V_211 = Vertex(name = 'V_211',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_5993,(0,1):C.GC_5992})

V_212 = Vertex(name = 'V_212',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_6119,(0,1):C.GC_6120})

V_213 = Vertex(name = 'V_213',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1025,(0,5):C.GC_1025,(0,6):C.GC_2200,(0,9):C.GC_2200,(0,4):C.GC_1026,(0,7):C.GC_1027,(0,8):C.GC_1026,(0,1):C.GC_1027,(0,2):C.GC_1034,(0,3):C.GC_2207})

V_214 = Vertex(name = 'V_214',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1359,(0,5):C.GC_1359,(0,6):C.GC_2691,(0,9):C.GC_2691,(0,4):C.GC_1358,(0,7):C.GC_1360,(0,8):C.GC_1358,(0,1):C.GC_1360,(0,2):C.GC_1363,(0,3):C.GC_2714})

V_215 = Vertex(name = 'V_215',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS4, L.VVSSS6, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5994,(0,1):C.GC_5994,(0,2):C.GC_5017})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS4, L.VVSSS6, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6121,(0,1):C.GC_6121,(0,2):C.GC_5177})

V_217 = Vertex(name = 'V_217',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1029,(0,6):C.GC_1029,(0,4):C.GC_1029,(0,7):C.GC_1029,(0,9):C.GC_1029,(0,11):C.GC_1029,(0,5):C.GC_2208,(0,8):C.GC_1030,(0,10):C.GC_2208,(0,1):C.GC_1030,(0,2):C.GC_2208,(0,3):C.GC_1030})

V_218 = Vertex(name = 'V_218',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1368,(0,6):C.GC_1368,(0,4):C.GC_1368,(0,7):C.GC_1368,(0,9):C.GC_1368,(0,11):C.GC_1368,(0,5):C.GC_2715,(0,8):C.GC_1354,(0,10):C.GC_2715,(0,1):C.GC_1354,(0,2):C.GC_2715,(0,3):C.GC_1354})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5576,(0,1):C.GC_5576,(0,2):C.GC_5576,(0,3):C.GC_5580,(0,4):C.GC_5576,(0,5):C.GC_5580,(0,6):C.GC_4774,(0,7):C.GC_4774,(0,8):C.GC_4785})

V_220 = Vertex(name = 'V_220',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5789,(0,1):C.GC_5789,(0,2):C.GC_5789,(0,3):C.GC_5806,(0,4):C.GC_5789,(0,5):C.GC_5806,(0,6):C.GC_4978,(0,7):C.GC_4978,(0,8):C.GC_4949})

V_221 = Vertex(name = 'V_221',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5578,(0,1):C.GC_5578,(0,2):C.GC_5577,(0,3):C.GC_5577,(0,4):C.GC_5577,(0,5):C.GC_5577,(0,6):C.GC_4783,(0,7):C.GC_4777,(0,8):C.GC_4777})

V_222 = Vertex(name = 'V_222',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5804,(0,1):C.GC_5804,(0,2):C.GC_5790,(0,3):C.GC_5790,(0,4):C.GC_5790,(0,5):C.GC_5790,(0,6):C.GC_4947,(0,7):C.GC_4981,(0,8):C.GC_4981})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6770,(0,1):C.GC_6770,(0,2):C.GC_6770,(0,3):C.GC_6770,(0,4):C.GC_5371,(0,5):C.GC_5371})

V_224 = Vertex(name = 'V_224',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6822,(0,1):C.GC_6822,(0,2):C.GC_6822,(0,3):C.GC_6822,(0,4):C.GC_5400,(0,5):C.GC_5400})

V_225 = Vertex(name = 'V_225',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_5991,(0,1):C.GC_5991,(0,2):C.GC_5016})

V_226 = Vertex(name = 'V_226',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_6118,(0,1):C.GC_6118,(0,2):C.GC_5176})

V_227 = Vertex(name = 'V_227',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1037,(0,6):C.GC_2206,(0,4):C.GC_1037,(0,7):C.GC_2206,(0,9):C.GC_1024,(0,11):C.GC_1024,(0,5):C.GC_1037,(0,8):C.GC_2206,(0,10):C.GC_1024,(0,1):C.GC_1024,(0,2):C.GC_1024,(0,3):C.GC_1024})

V_228 = Vertex(name = 'V_228',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1366,(0,6):C.GC_2713,(0,4):C.GC_1366,(0,7):C.GC_2713,(0,9):C.GC_1357,(0,11):C.GC_1357,(0,5):C.GC_1366,(0,8):C.GC_2713,(0,10):C.GC_1357,(0,1):C.GC_1357,(0,2):C.GC_1357,(0,3):C.GC_1357})

V_229 = Vertex(name = 'V_229',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2208,(0,5):C.GC_1031,(0,3):C.GC_1029,(0,6):C.GC_1028,(0,8):C.GC_2199,(0,4):C.GC_1029,(0,7):C.GC_1028,(0,9):C.GC_2199,(0,1):C.GC_1023,(0,2):C.GC_1023})

V_230 = Vertex(name = 'V_230',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8 ],
               couplings = {(0,0):C.GC_2715,(0,5):C.GC_1355,(0,3):C.GC_1368,(0,6):C.GC_1356,(0,8):C.GC_2690,(0,4):C.GC_1368,(0,7):C.GC_1356,(0,9):C.GC_2690,(0,1):C.GC_1367,(0,2):C.GC_1367})

V_231 = Vertex(name = 'V_231',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5996,(0,1):C.GC_5996,(0,2):C.GC_5995,(0,3):C.GC_5995,(0,4):C.GC_5014,(0,5):C.GC_5014,(0,6):C.GC_5015,(0,7):C.GC_5995,(0,8):C.GC_5995})

V_232 = Vertex(name = 'V_232',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6122,(0,1):C.GC_6122,(0,2):C.GC_6117,(0,3):C.GC_6117,(0,4):C.GC_5166,(0,5):C.GC_5166,(0,6):C.GC_5167,(0,7):C.GC_6117,(0,8):C.GC_6117})

V_233 = Vertex(name = 'V_233',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,3):C.GC_2198,(0,4):C.GC_2198,(0,6):C.GC_2201,(0,8):C.GC_2201,(0,5):C.GC_2202,(0,7):C.GC_2207,(0,0):C.GC_1032,(0,1):C.GC_2207,(0,2):C.GC_1032})

V_234 = Vertex(name = 'V_234',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,3):C.GC_2739,(0,4):C.GC_2739,(0,6):C.GC_2692,(0,8):C.GC_2692,(0,5):C.GC_2693,(0,7):C.GC_2714,(0,0):C.GC_1361,(0,1):C.GC_2714,(0,2):C.GC_1361})

V_235 = Vertex(name = 'V_235',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS5, L.VSSSS6, L.VSSSS9 ],
               couplings = {(0,0):C.GC_2204,(0,4):C.GC_1038,(0,6):C.GC_2205,(0,8):C.GC_2196,(0,5):C.GC_1038,(0,7):C.GC_2205,(0,1):C.GC_2196,(0,2):C.GC_2199,(0,3):C.GC_2199})

V_236 = Vertex(name = 'V_236',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS5, L.VSSSS6, L.VSSSS9 ],
               couplings = {(0,0):C.GC_2695,(0,4):C.GC_1369,(0,6):C.GC_2712,(0,8):C.GC_2737,(0,5):C.GC_1369,(0,7):C.GC_2712,(0,1):C.GC_2737,(0,2):C.GC_2690,(0,3):C.GC_2690})

V_237 = Vertex(name = 'V_237',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_5993,(0,1):C.GC_5992})

V_238 = Vertex(name = 'V_238',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_6119,(0,1):C.GC_6120})

V_239 = Vertex(name = 'V_239',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1026,(0,5):C.GC_1026,(0,6):C.GC_2201,(0,9):C.GC_2201,(0,4):C.GC_1025,(0,7):C.GC_1024,(0,8):C.GC_1025,(0,1):C.GC_1024,(0,2):C.GC_1036,(0,3):C.GC_2206})

V_240 = Vertex(name = 'V_240',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1358,(0,5):C.GC_1358,(0,6):C.GC_2692,(0,9):C.GC_2692,(0,4):C.GC_1359,(0,7):C.GC_1357,(0,8):C.GC_1359,(0,1):C.GC_1357,(0,2):C.GC_1365,(0,3):C.GC_2713})

V_241 = Vertex(name = 'V_241',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS4, L.VVSSS6, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5991,(0,1):C.GC_5991,(0,2):C.GC_5016})

V_242 = Vertex(name = 'V_242',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS4, L.VVSSS6, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6118,(0,1):C.GC_6118,(0,2):C.GC_5176})

V_243 = Vertex(name = 'V_243',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1029,(0,6):C.GC_1029,(0,4):C.GC_1029,(0,7):C.GC_1029,(0,9):C.GC_1029,(0,11):C.GC_1029,(0,5):C.GC_2208,(0,8):C.GC_1030,(0,10):C.GC_2208,(0,1):C.GC_1030,(0,2):C.GC_2208,(0,3):C.GC_1030})

V_244 = Vertex(name = 'V_244',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1368,(0,6):C.GC_1368,(0,4):C.GC_1368,(0,7):C.GC_1368,(0,9):C.GC_1368,(0,11):C.GC_1368,(0,5):C.GC_2715,(0,8):C.GC_1354,(0,10):C.GC_2715,(0,1):C.GC_1354,(0,2):C.GC_2715,(0,3):C.GC_1354})

V_245 = Vertex(name = 'V_245',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS12, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS144, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS164, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS21, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS37, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS51, L.VVVSS53, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS6, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS66, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS85, L.VVVSS86, L.VVVSS88, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS93, L.VVVSS94, L.VVVSS95, L.VVVSS96, L.VVVSS97, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,86):C.GC_1049,(0,87):C.GC_412,(0,84):C.GC_412,(0,85):C.GC_409,(0,103):C.GC_1052,(0,111):C.GC_91,(0,118):C.GC_90,(0,83):C.GC_1055,(0,92):C.GC_96,(0,14):C.GC_2214,(0,22):C.GC_411,(0,0):C.GC_2216,(0,5):C.GC_407,(0,74):C.GC_410,(0,78):C.GC_410,(0,56):C.GC_1059,(0,65):C.GC_405,(0,128):C.GC_1051,(0,129):C.GC_410,(0,130):C.GC_410,(0,2):C.GC_1043,(0,1):C.GC_410,(0,4):C.GC_410,(0,3):C.GC_410,(0,6):C.GC_411,(0,7):C.GC_410,(0,8):C.GC_411,(0,9):C.GC_411,(0,89):C.GC_1050,(0,88):C.GC_1062,(0,91):C.GC_90,(0,93):C.GC_91,(0,90):C.GC_97,(0,98):C.GC_1048,(0,99):C.GC_412,(0,100):C.GC_409,(0,94):C.GC_1060,(0,95):C.GC_407,(0,96):C.GC_1057,(0,97):C.GC_408,(0,102):C.GC_409,(0,101):C.GC_1064,(0,105):C.GC_409,(0,104):C.GC_408,(0,110):C.GC_409,(0,112):C.GC_412,(0,106):C.GC_1063,(0,107):C.GC_405,(0,108):C.GC_408,(0,109):C.GC_405,(0,114):C.GC_2213,(0,113):C.GC_2217,(0,116):C.GC_412,(0,115):C.GC_406,(0,122):C.GC_409,(0,123):C.GC_412,(0,117):C.GC_1054,(0,119):C.GC_406,(0,120):C.GC_406,(0,121):C.GC_407,(0,19):C.GC_1047,(0,20):C.GC_409,(0,13):C.GC_6770,(0,34):C.GC_411,(0,21):C.GC_5372,(0,41):C.GC_412,(0,35):C.GC_5371,(0,53):C.GC_1053,(0,54):C.GC_410,(0,42):C.GC_6771,(0,62):C.GC_409,(0,55):C.GC_6770,(0,77):C.GC_410,(0,63):C.GC_6771,(0,23):C.GC_2216,(0,43):C.GC_1056,(0,64):C.GC_1058,(0,15):C.GC_1061,(0,36):C.GC_2217,(0,57):C.GC_1065,(0,81):C.GC_1044,(0,10):C.GC_1042,(0,25):C.GC_1063,(0,38):C.GC_1065,(0,45):C.GC_1054,(0,59):C.GC_1055,(0,125):C.GC_1046,(0,134):C.GC_1045,(0,27):C.GC_1058,(0,30):C.GC_1060,(0,49):C.GC_1057,(0,69):C.GC_1062,(0,16):C.GC_408,(0,24):C.GC_407,(0,37):C.GC_406,(0,44):C.GC_405,(0,58):C.GC_97,(0,66):C.GC_96,(0,82):C.GC_411,(0,11):C.GC_410,(0,26):C.GC_407,(0,39):C.GC_407,(0,60):C.GC_406,(0,67):C.GC_406,(0,124):C.GC_409,(0,127):C.GC_409,(0,135):C.GC_409,(0,28):C.GC_1056,(0,31):C.GC_405,(0,47):C.GC_1064,(0,48):C.GC_408,(0,70):C.GC_405,(0,72):C.GC_408,(0,79):C.GC_411,(0,80):C.GC_411,(0,12):C.GC_411,(0,17):C.GC_1059,(0,18):C.GC_405,(0,40):C.GC_1061,(0,46):C.GC_408,(0,61):C.GC_408,(0,68):C.GC_405,(0,126):C.GC_409,(0,136):C.GC_412,(0,29):C.GC_406,(0,50):C.GC_406,(0,71):C.GC_407,(0,73):C.GC_407,(0,131):C.GC_1039,(0,132):C.GC_92,(0,133):C.GC_92,(0,32):C.GC_1041,(0,33):C.GC_96,(0,51):C.GC_1040,(0,52):C.GC_97,(0,75):C.GC_97,(0,76):C.GC_96})

V_246 = Vertex(name = 'V_246',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS164, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS66, L.VVVSS69, L.VVVSS70, L.VVVSS71, L.VVVSS72 ],
               couplings = {(0,56):C.GC_1293,(0,59):C.GC_452,(0,0):C.GC_2611,(0,1):C.GC_573,(0,37):C.GC_1291,(0,45):C.GC_475,(0,57):C.GC_1294,(0,58):C.GC_453,(0,60):C.GC_1296,(0,61):C.GC_573,(0,62):C.GC_1292,(0,63):C.GC_474,(0,64):C.GC_1295,(0,65):C.GC_474,(0,66):C.GC_1296,(0,67):C.GC_475,(0,68):C.GC_474,(0,69):C.GC_475,(0,70):C.GC_2612,(0,71):C.GC_574,(0,72):C.GC_1292,(0,73):C.GC_574,(0,74):C.GC_574,(0,75):C.GC_573,(0,2):C.GC_6822,(0,7):C.GC_5401,(0,19):C.GC_5400,(0,25):C.GC_6823,(0,36):C.GC_6822,(0,43):C.GC_6823,(0,8):C.GC_2611,(0,26):C.GC_1291,(0,44):C.GC_1293,(0,3):C.GC_1295,(0,20):C.GC_2612,(0,38):C.GC_1294,(0,10):C.GC_1296,(0,22):C.GC_1294,(0,28):C.GC_1292,(0,40):C.GC_1293,(0,12):C.GC_1293,(0,15):C.GC_1296,(0,32):C.GC_1292,(0,49):C.GC_1294,(0,4):C.GC_474,(0,9):C.GC_573,(0,21):C.GC_574,(0,27):C.GC_475,(0,39):C.GC_453,(0,46):C.GC_452,(0,11):C.GC_573,(0,23):C.GC_573,(0,41):C.GC_574,(0,47):C.GC_574,(0,13):C.GC_1291,(0,16):C.GC_475,(0,30):C.GC_1295,(0,31):C.GC_474,(0,50):C.GC_475,(0,52):C.GC_474,(0,5):C.GC_1291,(0,6):C.GC_475,(0,24):C.GC_1295,(0,29):C.GC_474,(0,42):C.GC_474,(0,48):C.GC_475,(0,14):C.GC_574,(0,33):C.GC_574,(0,51):C.GC_573,(0,53):C.GC_573,(0,17):C.GC_1290,(0,18):C.GC_452,(0,34):C.GC_1289,(0,35):C.GC_453,(0,54):C.GC_453,(0,55):C.GC_452})

V_247 = Vertex(name = 'V_247',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5578,(0,1):C.GC_4783,(0,2):C.GC_4787,(0,3):C.GC_4776,(0,4):C.GC_4776,(0,5):C.GC_4787,(0,6):C.GC_5578,(0,7):C.GC_4782,(0,8):C.GC_4782})

V_248 = Vertex(name = 'V_248',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5804,(0,1):C.GC_4947,(0,2):C.GC_4961,(0,3):C.GC_4980,(0,4):C.GC_4980,(0,5):C.GC_4961,(0,6):C.GC_5804,(0,7):C.GC_4946,(0,8):C.GC_4946})

V_249 = Vertex(name = 'V_249',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_5573,(0,1):C.GC_5573,(0,2):C.GC_4788})

V_250 = Vertex(name = 'V_250',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS7 ],
               couplings = {(0,0):C.GC_5803,(0,1):C.GC_5803,(0,2):C.GC_4962})

V_251 = Vertex(name = 'V_251',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_4775,(0,1):C.GC_4786,(0,2):C.GC_4789,(0,3):C.GC_4778,(0,4):C.GC_4781,(0,5):C.GC_4784})

V_252 = Vertex(name = 'V_252',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_4979,(0,1):C.GC_4960,(0,2):C.GC_4963,(0,3):C.GC_4982,(0,4):C.GC_4945,(0,5):C.GC_4948})

V_253 = Vertex(name = 'V_253',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_5572,(0,1):C.GC_5574,(0,2):C.GC_5572,(0,3):C.GC_5574})

V_254 = Vertex(name = 'V_254',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5 ],
               couplings = {(0,0):C.GC_5805,(0,1):C.GC_5802,(0,2):C.GC_5805,(0,3):C.GC_5802})

V_255 = Vertex(name = 'V_255',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5573,(0,1):C.GC_5573,(0,2):C.GC_5573,(0,3):C.GC_5573,(0,4):C.GC_5573,(0,5):C.GC_5573,(0,6):C.GC_4788,(0,7):C.GC_4788,(0,8):C.GC_4788})

V_256 = Vertex(name = 'V_256',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5803,(0,1):C.GC_5803,(0,2):C.GC_5803,(0,3):C.GC_5803,(0,4):C.GC_5803,(0,5):C.GC_5803,(0,6):C.GC_4962,(0,7):C.GC_4962,(0,8):C.GC_4962})

V_257 = Vertex(name = 'V_257',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS100, L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS109, L.VVVVS110, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS123, L.VVVVS124, L.VVVVS125, L.VVVVS127, L.VVVVS128, L.VVVVS13, L.VVVVS130, L.VVVVS14, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS15, L.VVVVS150, L.VVVVS151, L.VVVVS152, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS16, L.VVVVS160, L.VVVVS161, L.VVVVS163, L.VVVVS164, L.VVVVS168, L.VVVVS169, L.VVVVS17, L.VVVVS170, L.VVVVS171, L.VVVVS174, L.VVVVS18, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS19, L.VVVVS190, L.VVVVS191, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS199, L.VVVVS20, L.VVVVS201, L.VVVVS202, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS21, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS23, L.VVVVS24, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS244, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS253, L.VVVVS255, L.VVVVS256, L.VVVVS26, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS27, L.VVVVS29, L.VVVVS30, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS35, L.VVVVS36, L.VVVVS38, L.VVVVS39, L.VVVVS49, L.VVVVS50, L.VVVVS54, L.VVVVS56, L.VVVVS58, L.VVVVS60, L.VVVVS62, L.VVVVS63, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS74, L.VVVVS75, L.VVVVS76, L.VVVVS77, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS82, L.VVVVS83, L.VVVVS84, L.VVVVS86, L.VVVVS87, L.VVVVS94, L.VVVVS95, L.VVVVS96, L.VVVVS97, L.VVVVS98, L.VVVVS99 ],
               couplings = {(0,50):C.GC_5985,(0,59):C.GC_5985,(0,66):C.GC_5982,(0,70):C.GC_5979,(0,71):C.GC_5981,(0,72):C.GC_5979,(0,18):C.GC_5982,(0,20):C.GC_5981,(0,24):C.GC_5012,(0,34):C.GC_5979,(0,41):C.GC_5012,(0,45):C.GC_5979,(0,106):C.GC_5582,(0,107):C.GC_5582,(0,108):C.GC_5984,(0,110):C.GC_5984,(0,112):C.GC_5979,(0,113):C.GC_5979,(0,87):C.GC_5982,(0,95):C.GC_5981,(0,96):C.GC_5958,(0,97):C.GC_5982,(0,98):C.GC_5007,(0,99):C.GC_5983,(0,100):C.GC_5958,(0,101):C.GC_5007,(0,102):C.GC_5982,(0,103):C.GC_5983,(0,104):C.GC_5981,(0,105):C.GC_5982,(0,117):C.GC_5990,(0,118):C.GC_5981,(0,119):C.GC_5009,(0,120):C.GC_5008,(0,114):C.GC_4794,(0,115):C.GC_5972,(0,116):C.GC_5010,(0,126):C.GC_5583,(0,127):C.GC_5979,(0,128):C.GC_5984,(0,121):C.GC_5969,(0,122):C.GC_5010,(0,123):C.GC_5972,(0,124):C.GC_5975,(0,125):C.GC_5973,(0,132):C.GC_5990,(0,133):C.GC_5009,(0,134):C.GC_5981,(0,0):C.GC_5008,(0,129):C.GC_4794,(0,130):C.GC_5010,(0,131):C.GC_5972,(0,6):C.GC_5583,(0,7):C.GC_5979,(0,8):C.GC_5984,(0,1):C.GC_5969,(0,2):C.GC_5972,(0,3):C.GC_5010,(0,4):C.GC_5975,(0,5):C.GC_5973,(0,13):C.GC_5981,(0,14):C.GC_5982,(0,9):C.GC_4795,(0,10):C.GC_5975,(0,11):C.GC_4795,(0,12):C.GC_5975,(0,15):C.GC_5968,(0,16):C.GC_5977,(0,17):C.GC_5968,(0,19):C.GC_5977,(0,25):C.GC_4791,(0,26):C.GC_5979,(0,27):C.GC_5979,(0,21):C.GC_4792,(0,22):C.GC_5975,(0,23):C.GC_5975,(0,35):C.GC_5984,(0,36):C.GC_5984,(0,37):C.GC_5987,(0,28):C.GC_5966,(0,29):C.GC_5975,(0,30):C.GC_5975,(0,31):C.GC_5973,(0,32):C.GC_5973,(0,33):C.GC_5978,(0,38):C.GC_5437,(0,51):C.GC_5013,(0,52):C.GC_5984,(0,46):C.GC_4794,(0,47):C.GC_5973,(0,48):C.GC_5976,(0,49):C.GC_5972,(0,58):C.GC_5984,(0,60):C.GC_5979,(0,53):C.GC_5961,(0,54):C.GC_5973,(0,55):C.GC_5011,(0,56):C.GC_5976,(0,57):C.GC_5974,(0,61):C.GC_7119,(0,77):C.GC_5013,(0,78):C.GC_5984,(0,73):C.GC_4794,(0,74):C.GC_5973,(0,75):C.GC_5972,(0,76):C.GC_5976,(0,84):C.GC_5984,(0,85):C.GC_5979,(0,79):C.GC_5961,(0,80):C.GC_5973,(0,81):C.GC_5976,(0,82):C.GC_5011,(0,83):C.GC_5974,(0,86):C.GC_7119,(0,39):C.GC_4793,(0,62):C.GC_4795,(0,88):C.GC_4795,(0,43):C.GC_5959,(0,65):C.GC_5964,(0,91):C.GC_5964,(0,40):C.GC_5973,(0,63):C.GC_5011,(0,89):C.GC_5976,(0,109):C.GC_5982,(0,67):C.GC_5976,(0,92):C.GC_5972,(0,42):C.GC_5973,(0,64):C.GC_5976,(0,90):C.GC_5011,(0,111):C.GC_5981,(0,68):C.GC_5972,(0,93):C.GC_5976,(0,44):C.GC_5971,(0,69):C.GC_5975,(0,94):C.GC_5975})

V_258 = Vertex(name = 'V_258',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS105, L.VVVVS106, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS125, L.VVVVS127, L.VVVVS128, L.VVVVS130, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS164, L.VVVVS168, L.VVVVS169, L.VVVVS170, L.VVVVS171, L.VVVVS174, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS202, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS82, L.VVVVS83, L.VVVVS94, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,62):C.GC_4919,(0,63):C.GC_5123,(0,64):C.GC_5114,(0,65):C.GC_6103,(0,66):C.GC_5114,(0,67):C.GC_5123,(0,68):C.GC_6098,(0,69):C.GC_6105,(0,70):C.GC_4919,(0,71):C.GC_5114,(0,72):C.GC_5123,(0,0):C.GC_6103,(0,1):C.GC_5123,(0,2):C.GC_5114,(0,3):C.GC_6098,(0,4):C.GC_6105,(0,5):C.GC_4920,(0,6):C.GC_6098,(0,7):C.GC_4920,(0,8):C.GC_6098,(0,9):C.GC_6101,(0,10):C.GC_6057,(0,11):C.GC_6101,(0,12):C.GC_6057,(0,13):C.GC_4912,(0,14):C.GC_6098,(0,15):C.GC_6098,(0,16):C.GC_6104,(0,17):C.GC_6098,(0,18):C.GC_6098,(0,19):C.GC_6105,(0,20):C.GC_6105,(0,21):C.GC_6097,(0,22):C.GC_5440,(0,28):C.GC_4919,(0,29):C.GC_6105,(0,30):C.GC_5122,(0,31):C.GC_5123,(0,32):C.GC_6100,(0,33):C.GC_6105,(0,34):C.GC_5115,(0,35):C.GC_5122,(0,36):C.GC_6058,(0,37):C.GC_7122,(0,45):C.GC_4919,(0,46):C.GC_6105,(0,47):C.GC_5123,(0,48):C.GC_5122,(0,49):C.GC_6100,(0,50):C.GC_6105,(0,51):C.GC_5122,(0,52):C.GC_5115,(0,53):C.GC_6058,(0,54):C.GC_7122,(0,23):C.GC_4913,(0,38):C.GC_4920,(0,55):C.GC_4920,(0,26):C.GC_6099,(0,41):C.GC_6102,(0,58):C.GC_6102,(0,24):C.GC_6105,(0,39):C.GC_5115,(0,56):C.GC_5122,(0,42):C.GC_5122,(0,59):C.GC_5123,(0,25):C.GC_6105,(0,40):C.GC_5122,(0,57):C.GC_5115,(0,43):C.GC_5123,(0,60):C.GC_5122,(0,27):C.GC_6106,(0,44):C.GC_6098,(0,61):C.GC_6098})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS119, L.VVVSS12, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS140, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS155, L.VVVSS156, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS171, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS187, L.VVVSS188, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS20, L.VVVSS203, L.VVVSS21, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS45, L.VVVSS46, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS52, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS59, L.VVVSS6, L.VVVSS60, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS71, L.VVVSS74, L.VVVSS75, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS97, L.VVVSS98 ],
               couplings = {(0,76):C.GC_1020,(0,77):C.GC_1020,(0,74):C.GC_1020,(0,75):C.GC_1020,(0,89):C.GC_1019,(0,99):C.GC_2185,(0,106):C.GC_2186,(0,73):C.GC_1004,(0,82):C.GC_2190,(0,13):C.GC_2185,(0,21):C.GC_1019,(0,29):C.GC_2186,(0,0):C.GC_2190,(0,5):C.GC_1004,(0,66):C.GC_1019,(0,68):C.GC_1010,(0,50):C.GC_1002,(0,58):C.GC_1002,(0,114):C.GC_1021,(0,115):C.GC_1021,(0,3):C.GC_1019,(0,4):C.GC_1019,(0,1):C.GC_1019,(0,2):C.GC_1019,(0,6):C.GC_1008,(0,7):C.GC_1008,(0,8):C.GC_1021,(0,9):C.GC_1008,(0,80):C.GC_1020,(0,81):C.GC_2186,(0,83):C.GC_2185,(0,78):C.GC_1001,(0,79):C.GC_2189,(0,87):C.GC_1022,(0,88):C.GC_1007,(0,84):C.GC_2194,(0,85):C.GC_2193,(0,86):C.GC_2193,(0,92):C.GC_2186,(0,93):C.GC_1020,(0,94):C.GC_2185,(0,90):C.GC_2189,(0,91):C.GC_1001,(0,98):C.GC_1022,(0,100):C.GC_1007,(0,95):C.GC_2193,(0,96):C.GC_2194,(0,97):C.GC_2193,(0,103):C.GC_1020,(0,104):C.GC_1009,(0,101):C.GC_1003,(0,102):C.GC_1003,(0,108):C.GC_1022,(0,109):C.GC_1007,(0,105):C.GC_2194,(0,107):C.GC_2194,(0,18):C.GC_1009,(0,19):C.GC_1009,(0,12):C.GC_5318,(0,31):C.GC_1010,(0,32):C.GC_1010,(0,20):C.GC_5321,(0,39):C.GC_1020,(0,33):C.GC_6722,(0,48):C.GC_1019,(0,40):C.GC_6719,(0,56):C.GC_1020,(0,49):C.GC_6722,(0,67):C.GC_1019,(0,57):C.GC_6719,(0,14):C.GC_1003,(0,22):C.GC_1002,(0,34):C.GC_2189,(0,41):C.GC_2190,(0,51):C.GC_1001,(0,59):C.GC_1004,(0,71):C.GC_1010,(0,10):C.GC_1008,(0,24):C.GC_2193,(0,36):C.GC_1001,(0,43):C.GC_2194,(0,53):C.GC_1004,(0,112):C.GC_1009,(0,116):C.GC_1007,(0,28):C.GC_2194,(0,44):C.GC_1004,(0,47):C.GC_2193,(0,62):C.GC_1001,(0,15):C.GC_1003,(0,23):C.GC_1002,(0,35):C.GC_1001,(0,42):C.GC_1004,(0,52):C.GC_2189,(0,60):C.GC_2190,(0,72):C.GC_1019,(0,11):C.GC_1021,(0,25):C.GC_2193,(0,37):C.GC_1004,(0,54):C.GC_1001,(0,61):C.GC_2194,(0,113):C.GC_1020,(0,117):C.GC_1022,(0,30):C.GC_2194,(0,45):C.GC_1001,(0,63):C.GC_1004,(0,65):C.GC_2193,(0,69):C.GC_1010,(0,70):C.GC_1019,(0,16):C.GC_1002,(0,17):C.GC_1002,(0,38):C.GC_1003,(0,55):C.GC_1003,(0,110):C.GC_1009,(0,111):C.GC_1020,(0,26):C.GC_1003,(0,27):C.GC_1003,(0,46):C.GC_1002,(0,64):C.GC_1002})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS3, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS71 ],
               couplings = {(0,46):C.GC_2583,(0,49):C.GC_2559,(0,0):C.GC_2559,(0,1):C.GC_2583,(0,31):C.GC_1312,(0,38):C.GC_1312,(0,47):C.GC_2584,(0,48):C.GC_2558,(0,50):C.GC_2659,(0,51):C.GC_2660,(0,52):C.GC_2660,(0,53):C.GC_2558,(0,54):C.GC_2584,(0,55):C.GC_2660,(0,56):C.GC_2659,(0,57):C.GC_2660,(0,58):C.GC_1311,(0,59):C.GC_1311,(0,60):C.GC_2659,(0,61):C.GC_2659,(0,2):C.GC_5356,(0,7):C.GC_5349,(0,16):C.GC_6732,(0,22):C.GC_6735,(0,30):C.GC_6732,(0,37):C.GC_6735,(0,3):C.GC_1311,(0,8):C.GC_1312,(0,17):C.GC_2558,(0,23):C.GC_2559,(0,32):C.GC_2584,(0,39):C.GC_2583,(0,10):C.GC_2660,(0,19):C.GC_2584,(0,25):C.GC_2659,(0,34):C.GC_2583,(0,14):C.GC_2659,(0,26):C.GC_2583,(0,29):C.GC_2660,(0,42):C.GC_2584,(0,4):C.GC_1311,(0,9):C.GC_1312,(0,18):C.GC_2584,(0,24):C.GC_2583,(0,33):C.GC_2558,(0,40):C.GC_2559,(0,11):C.GC_2660,(0,20):C.GC_2583,(0,35):C.GC_2584,(0,41):C.GC_2659,(0,15):C.GC_2659,(0,27):C.GC_2584,(0,43):C.GC_2583,(0,45):C.GC_2660,(0,5):C.GC_1312,(0,6):C.GC_1312,(0,21):C.GC_1311,(0,36):C.GC_1311,(0,12):C.GC_1311,(0,13):C.GC_1311,(0,28):C.GC_1312,(0,44):C.GC_1312})

V_261 = Vertex(name = 'V_261',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS119, L.VVVSS12, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS140, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS155, L.VVVSS156, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS171, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS187, L.VVVSS188, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS20, L.VVVSS203, L.VVVSS21, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS45, L.VVVSS46, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS52, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS59, L.VVVSS6, L.VVVSS60, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS71, L.VVVSS74, L.VVVSS75, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS97, L.VVVSS98 ],
               couplings = {(0,76):C.GC_1011,(0,77):C.GC_1011,(0,74):C.GC_1011,(0,75):C.GC_1011,(0,89):C.GC_1012,(0,99):C.GC_2187,(0,106):C.GC_2184,(0,73):C.GC_999,(0,82):C.GC_2188,(0,13):C.GC_2187,(0,21):C.GC_1012,(0,29):C.GC_2184,(0,0):C.GC_2188,(0,5):C.GC_999,(0,66):C.GC_1012,(0,68):C.GC_1013,(0,50):C.GC_1005,(0,58):C.GC_1005,(0,114):C.GC_1016,(0,115):C.GC_1016,(0,3):C.GC_1012,(0,4):C.GC_1012,(0,1):C.GC_1012,(0,2):C.GC_1012,(0,6):C.GC_1017,(0,7):C.GC_1017,(0,8):C.GC_1016,(0,9):C.GC_1017,(0,80):C.GC_1011,(0,81):C.GC_2184,(0,83):C.GC_2187,(0,78):C.GC_1006,(0,79):C.GC_2191,(0,87):C.GC_1015,(0,88):C.GC_1018,(0,84):C.GC_2192,(0,85):C.GC_2195,(0,86):C.GC_2195,(0,92):C.GC_2184,(0,93):C.GC_1011,(0,94):C.GC_2187,(0,90):C.GC_2191,(0,91):C.GC_1006,(0,98):C.GC_1015,(0,100):C.GC_1018,(0,95):C.GC_2195,(0,96):C.GC_2192,(0,97):C.GC_2195,(0,103):C.GC_1011,(0,104):C.GC_1014,(0,101):C.GC_1000,(0,102):C.GC_1000,(0,108):C.GC_1015,(0,109):C.GC_1018,(0,105):C.GC_2192,(0,107):C.GC_2192,(0,18):C.GC_1014,(0,19):C.GC_1014,(0,12):C.GC_5320,(0,31):C.GC_1013,(0,32):C.GC_1013,(0,20):C.GC_5319,(0,39):C.GC_1011,(0,33):C.GC_6718,(0,48):C.GC_1012,(0,40):C.GC_6723,(0,56):C.GC_1011,(0,49):C.GC_6718,(0,67):C.GC_1012,(0,57):C.GC_6723,(0,14):C.GC_1000,(0,22):C.GC_1005,(0,34):C.GC_2191,(0,41):C.GC_2188,(0,51):C.GC_1006,(0,59):C.GC_999,(0,71):C.GC_1013,(0,10):C.GC_1017,(0,24):C.GC_2195,(0,36):C.GC_1006,(0,43):C.GC_2192,(0,53):C.GC_999,(0,112):C.GC_1014,(0,116):C.GC_1018,(0,28):C.GC_2192,(0,44):C.GC_999,(0,47):C.GC_2195,(0,62):C.GC_1006,(0,15):C.GC_1000,(0,23):C.GC_1005,(0,35):C.GC_1006,(0,42):C.GC_999,(0,52):C.GC_2191,(0,60):C.GC_2188,(0,72):C.GC_1012,(0,11):C.GC_1016,(0,25):C.GC_2195,(0,37):C.GC_999,(0,54):C.GC_1006,(0,61):C.GC_2192,(0,113):C.GC_1011,(0,117):C.GC_1015,(0,30):C.GC_2192,(0,45):C.GC_1006,(0,63):C.GC_999,(0,65):C.GC_2195,(0,69):C.GC_1013,(0,70):C.GC_1012,(0,16):C.GC_1005,(0,17):C.GC_1005,(0,38):C.GC_1000,(0,55):C.GC_1000,(0,110):C.GC_1014,(0,111):C.GC_1011,(0,26):C.GC_1000,(0,27):C.GC_1000,(0,46):C.GC_1005,(0,64):C.GC_1005})

V_262 = Vertex(name = 'V_262',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS121, L.VVVSS122, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS146, L.VVVSS148, L.VVVSS149, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS178, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS3, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS71 ],
               couplings = {(0,46):C.GC_2585,(0,49):C.GC_2557,(0,0):C.GC_2557,(0,1):C.GC_2585,(0,31):C.GC_1310,(0,38):C.GC_1310,(0,47):C.GC_2582,(0,48):C.GC_2560,(0,50):C.GC_2661,(0,51):C.GC_2658,(0,52):C.GC_2658,(0,53):C.GC_2560,(0,54):C.GC_2582,(0,55):C.GC_2658,(0,56):C.GC_2661,(0,57):C.GC_2658,(0,58):C.GC_1313,(0,59):C.GC_1313,(0,60):C.GC_2661,(0,61):C.GC_2661,(0,2):C.GC_5348,(0,7):C.GC_5357,(0,16):C.GC_6734,(0,22):C.GC_6733,(0,30):C.GC_6734,(0,37):C.GC_6733,(0,3):C.GC_1313,(0,8):C.GC_1310,(0,17):C.GC_2560,(0,23):C.GC_2557,(0,32):C.GC_2582,(0,39):C.GC_2585,(0,10):C.GC_2658,(0,19):C.GC_2582,(0,25):C.GC_2661,(0,34):C.GC_2585,(0,14):C.GC_2661,(0,26):C.GC_2585,(0,29):C.GC_2658,(0,42):C.GC_2582,(0,4):C.GC_1313,(0,9):C.GC_1310,(0,18):C.GC_2582,(0,24):C.GC_2585,(0,33):C.GC_2560,(0,40):C.GC_2557,(0,11):C.GC_2658,(0,20):C.GC_2585,(0,35):C.GC_2582,(0,41):C.GC_2661,(0,15):C.GC_2661,(0,27):C.GC_2582,(0,43):C.GC_2585,(0,45):C.GC_2658,(0,5):C.GC_1310,(0,6):C.GC_1310,(0,21):C.GC_1313,(0,36):C.GC_1313,(0,12):C.GC_1313,(0,13):C.GC_1313,(0,28):C.GC_1310,(0,44):C.GC_1310})

V_263 = Vertex(name = 'V_263',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5579,(0,1):C.GC_5579,(0,2):C.GC_5579,(0,3):C.GC_5575,(0,4):C.GC_5579,(0,5):C.GC_5575,(0,6):C.GC_4779,(0,7):C.GC_4779,(0,8):C.GC_4780})

V_264 = Vertex(name = 'V_264',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5791,(0,1):C.GC_5791,(0,2):C.GC_5791,(0,3):C.GC_5801,(0,4):C.GC_5791,(0,5):C.GC_5801,(0,6):C.GC_4983,(0,7):C.GC_4983,(0,8):C.GC_4944})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5578,(0,1):C.GC_5578,(0,2):C.GC_5577,(0,3):C.GC_5577,(0,4):C.GC_5577,(0,5):C.GC_5577,(0,6):C.GC_4783,(0,7):C.GC_4777,(0,8):C.GC_4777})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5804,(0,1):C.GC_5804,(0,2):C.GC_5790,(0,3):C.GC_5790,(0,4):C.GC_5790,(0,5):C.GC_5790,(0,6):C.GC_4947,(0,7):C.GC_4981,(0,8):C.GC_4981})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS107, L.VVVSS108, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS127, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS14, L.VVVSS140, L.VVVSS143, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS154, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS16, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS167, L.VVVSS17, L.VVVSS170, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS202, L.VVVSS203, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS26, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS31, L.VVVSS32, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS38, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS52, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS64, L.VVVSS65, L.VVVSS67, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS89, L.VVVSS9, L.VVVSS92, L.VVVSS93, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,75):C.GC_1010,(0,74):C.GC_1010,(0,78):C.GC_1010,(0,77):C.GC_1010,(0,66):C.GC_1020,(0,0):C.GC_1003,(0,89):C.GC_1009,(0,76):C.GC_1003,(0,113):C.GC_1009,(0,108):C.GC_1001,(0,13):C.GC_2186,(0,27):C.GC_2185,(0,1):C.GC_2189,(0,41):C.GC_2186,(0,47):C.GC_2185,(0,33):C.GC_2189,(0,67):C.GC_1009,(0,51):C.GC_1001,(0,114):C.GC_1007,(0,115):C.GC_1007,(0,3):C.GC_1009,(0,2):C.GC_1009,(0,5):C.GC_1009,(0,4):C.GC_1009,(0,6):C.GC_1022,(0,7):C.GC_1007,(0,8):C.GC_1022,(0,9):C.GC_1022,(0,80):C.GC_1019,(0,79):C.GC_1002,(0,82):C.GC_1010,(0,81):C.GC_1002,(0,85):C.GC_1021,(0,86):C.GC_1008,(0,83):C.GC_2193,(0,84):C.GC_2193,(0,88):C.GC_1010,(0,87):C.GC_1004,(0,91):C.GC_2185,(0,92):C.GC_2186,(0,90):C.GC_2190,(0,96):C.GC_1008,(0,97):C.GC_1021,(0,93):C.GC_2194,(0,94):C.GC_2193,(0,95):C.GC_2194,(0,99):C.GC_2185,(0,100):C.GC_2186,(0,98):C.GC_2190,(0,102):C.GC_1010,(0,101):C.GC_1004,(0,106):C.GC_1008,(0,107):C.GC_1021,(0,103):C.GC_2194,(0,104):C.GC_2194,(0,105):C.GC_2193,(0,19):C.GC_1019,(0,12):C.GC_6720,(0,29):C.GC_1020,(0,20):C.GC_6721,(0,37):C.GC_1019,(0,30):C.GC_6720,(0,48):C.GC_1020,(0,38):C.GC_6721,(0,55):C.GC_1010,(0,56):C.GC_1010,(0,49):C.GC_5317,(0,68):C.GC_1009,(0,69):C.GC_1009,(0,57):C.GC_5322,(0,14):C.GC_2190,(0,21):C.GC_2189,(0,31):C.GC_1004,(0,39):C.GC_1001,(0,50):C.GC_1002,(0,58):C.GC_1003,(0,15):C.GC_1004,(0,22):C.GC_1001,(0,32):C.GC_2190,(0,40):C.GC_2189,(0,52):C.GC_1002,(0,59):C.GC_1003,(0,71):C.GC_1009,(0,73):C.GC_1020,(0,16):C.GC_1002,(0,35):C.GC_1002,(0,53):C.GC_1003,(0,54):C.GC_1003,(0,110):C.GC_1010,(0,112):C.GC_1019,(0,24):C.GC_1003,(0,44):C.GC_1003,(0,62):C.GC_1002,(0,63):C.GC_1002,(0,70):C.GC_1009,(0,10):C.GC_1007,(0,17):C.GC_1004,(0,23):C.GC_2193,(0,34):C.GC_1001,(0,60):C.GC_2194,(0,109):C.GC_1010,(0,116):C.GC_1008,(0,25):C.GC_1001,(0,28):C.GC_2194,(0,43):C.GC_1004,(0,64):C.GC_2193,(0,72):C.GC_1020,(0,11):C.GC_1022,(0,18):C.GC_1001,(0,36):C.GC_1004,(0,42):C.GC_2193,(0,61):C.GC_2194,(0,111):C.GC_1019,(0,117):C.GC_1021,(0,26):C.GC_1004,(0,45):C.GC_1001,(0,46):C.GC_2194,(0,65):C.GC_2193})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS140, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS167, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_1311,(0,46):C.GC_1311,(0,61):C.GC_2584,(0,1):C.GC_2558,(0,19):C.GC_2558,(0,33):C.GC_2584,(0,47):C.GC_1312,(0,48):C.GC_1312,(0,49):C.GC_2660,(0,50):C.GC_2660,(0,51):C.GC_2583,(0,52):C.GC_2559,(0,53):C.GC_2659,(0,54):C.GC_2660,(0,55):C.GC_2659,(0,56):C.GC_2559,(0,57):C.GC_2583,(0,58):C.GC_2659,(0,59):C.GC_2659,(0,60):C.GC_2660,(0,2):C.GC_6731,(0,8):C.GC_6736,(0,16):C.GC_6731,(0,23):C.GC_6736,(0,31):C.GC_5355,(0,37):C.GC_5350,(0,3):C.GC_2559,(0,9):C.GC_2558,(0,17):C.GC_2583,(0,24):C.GC_2584,(0,32):C.GC_1312,(0,38):C.GC_1311,(0,4):C.GC_2583,(0,10):C.GC_2584,(0,18):C.GC_2559,(0,25):C.GC_2558,(0,34):C.GC_1312,(0,39):C.GC_1311,(0,5):C.GC_1312,(0,21):C.GC_1312,(0,35):C.GC_1311,(0,36):C.GC_1311,(0,12):C.GC_1311,(0,28):C.GC_1311,(0,42):C.GC_1312,(0,43):C.GC_1312,(0,6):C.GC_2583,(0,11):C.GC_2660,(0,20):C.GC_2584,(0,40):C.GC_2659,(0,13):C.GC_2584,(0,15):C.GC_2659,(0,27):C.GC_2583,(0,44):C.GC_2660,(0,7):C.GC_2584,(0,22):C.GC_2583,(0,26):C.GC_2660,(0,41):C.GC_2659,(0,14):C.GC_2583,(0,29):C.GC_2584,(0,30):C.GC_2659,(0,45):C.GC_2660})

V_269 = Vertex(name = 'V_269',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS107, L.VVVSS108, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS127, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS14, L.VVVSS140, L.VVVSS143, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS154, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS16, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS167, L.VVVSS17, L.VVVSS170, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS202, L.VVVSS203, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS26, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS31, L.VVVSS32, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS38, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS52, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS64, L.VVVSS65, L.VVVSS67, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS89, L.VVVSS9, L.VVVSS92, L.VVVSS93, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,75):C.GC_1012,(0,74):C.GC_1012,(0,78):C.GC_1012,(0,77):C.GC_1012,(0,66):C.GC_1014,(0,0):C.GC_1005,(0,89):C.GC_1011,(0,76):C.GC_1005,(0,113):C.GC_1011,(0,108):C.GC_999,(0,13):C.GC_2187,(0,27):C.GC_2184,(0,1):C.GC_2188,(0,41):C.GC_2187,(0,47):C.GC_2184,(0,33):C.GC_2188,(0,67):C.GC_1011,(0,51):C.GC_999,(0,114):C.GC_1015,(0,115):C.GC_1015,(0,3):C.GC_1011,(0,2):C.GC_1011,(0,5):C.GC_1011,(0,4):C.GC_1011,(0,6):C.GC_1018,(0,7):C.GC_1015,(0,8):C.GC_1018,(0,9):C.GC_1018,(0,80):C.GC_1013,(0,79):C.GC_1000,(0,82):C.GC_1012,(0,81):C.GC_1000,(0,85):C.GC_1017,(0,86):C.GC_1016,(0,83):C.GC_2192,(0,84):C.GC_2192,(0,88):C.GC_1012,(0,87):C.GC_1006,(0,91):C.GC_2184,(0,92):C.GC_2187,(0,90):C.GC_2191,(0,96):C.GC_1016,(0,97):C.GC_1017,(0,93):C.GC_2195,(0,94):C.GC_2192,(0,95):C.GC_2195,(0,99):C.GC_2184,(0,100):C.GC_2187,(0,98):C.GC_2191,(0,102):C.GC_1012,(0,101):C.GC_1006,(0,106):C.GC_1016,(0,107):C.GC_1017,(0,103):C.GC_2195,(0,104):C.GC_2195,(0,105):C.GC_2192,(0,19):C.GC_1013,(0,12):C.GC_6718,(0,29):C.GC_1014,(0,20):C.GC_6723,(0,37):C.GC_1013,(0,30):C.GC_6718,(0,48):C.GC_1014,(0,38):C.GC_6723,(0,55):C.GC_1012,(0,56):C.GC_1012,(0,49):C.GC_5320,(0,68):C.GC_1011,(0,69):C.GC_1011,(0,57):C.GC_5319,(0,14):C.GC_2191,(0,21):C.GC_2188,(0,31):C.GC_1006,(0,39):C.GC_999,(0,50):C.GC_1000,(0,58):C.GC_1005,(0,15):C.GC_1006,(0,22):C.GC_999,(0,32):C.GC_2191,(0,40):C.GC_2188,(0,52):C.GC_1000,(0,59):C.GC_1005,(0,71):C.GC_1011,(0,73):C.GC_1014,(0,16):C.GC_1000,(0,35):C.GC_1000,(0,53):C.GC_1005,(0,54):C.GC_1005,(0,110):C.GC_1012,(0,112):C.GC_1013,(0,24):C.GC_1005,(0,44):C.GC_1005,(0,62):C.GC_1000,(0,63):C.GC_1000,(0,70):C.GC_1011,(0,10):C.GC_1015,(0,17):C.GC_1006,(0,23):C.GC_2192,(0,34):C.GC_999,(0,60):C.GC_2195,(0,109):C.GC_1012,(0,116):C.GC_1016,(0,25):C.GC_999,(0,28):C.GC_2195,(0,43):C.GC_1006,(0,64):C.GC_2192,(0,72):C.GC_1014,(0,11):C.GC_1018,(0,18):C.GC_999,(0,36):C.GC_1006,(0,42):C.GC_2192,(0,61):C.GC_2195,(0,111):C.GC_1013,(0,117):C.GC_1017,(0,26):C.GC_1006,(0,45):C.GC_999,(0,46):C.GC_2195,(0,65):C.GC_2192})

V_270 = Vertex(name = 'V_270',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS140, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS167, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_1310,(0,46):C.GC_1310,(0,61):C.GC_2585,(0,1):C.GC_2557,(0,19):C.GC_2557,(0,33):C.GC_2585,(0,47):C.GC_1313,(0,48):C.GC_1313,(0,49):C.GC_2661,(0,50):C.GC_2661,(0,51):C.GC_2582,(0,52):C.GC_2560,(0,53):C.GC_2658,(0,54):C.GC_2661,(0,55):C.GC_2658,(0,56):C.GC_2560,(0,57):C.GC_2582,(0,58):C.GC_2658,(0,59):C.GC_2658,(0,60):C.GC_2661,(0,2):C.GC_6734,(0,8):C.GC_6733,(0,16):C.GC_6734,(0,23):C.GC_6733,(0,31):C.GC_5348,(0,37):C.GC_5357,(0,3):C.GC_2560,(0,9):C.GC_2557,(0,17):C.GC_2582,(0,24):C.GC_2585,(0,32):C.GC_1313,(0,38):C.GC_1310,(0,4):C.GC_2582,(0,10):C.GC_2585,(0,18):C.GC_2560,(0,25):C.GC_2557,(0,34):C.GC_1313,(0,39):C.GC_1310,(0,5):C.GC_1313,(0,21):C.GC_1313,(0,35):C.GC_1310,(0,36):C.GC_1310,(0,12):C.GC_1310,(0,28):C.GC_1310,(0,42):C.GC_1313,(0,43):C.GC_1313,(0,6):C.GC_2582,(0,11):C.GC_2661,(0,20):C.GC_2585,(0,40):C.GC_2658,(0,13):C.GC_2585,(0,15):C.GC_2658,(0,27):C.GC_2582,(0,44):C.GC_2661,(0,7):C.GC_2585,(0,22):C.GC_2582,(0,26):C.GC_2661,(0,41):C.GC_2658,(0,14):C.GC_2582,(0,29):C.GC_2585,(0,30):C.GC_2658,(0,45):C.GC_2661})

V_271 = Vertex(name = 'V_271',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6771,(0,1):C.GC_6771,(0,2):C.GC_6771,(0,3):C.GC_6771,(0,4):C.GC_5372,(0,5):C.GC_5372})

V_272 = Vertex(name = 'V_272',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6823,(0,1):C.GC_6823,(0,2):C.GC_6823,(0,3):C.GC_6823,(0,4):C.GC_5401,(0,5):C.GC_5401})

V_273 = Vertex(name = 'V_273',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS100, L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS109, L.VVVVS11, L.VVVVS110, L.VVVVS112, L.VVVVS113, L.VVVVS115, L.VVVVS117, L.VVVVS118, L.VVVVS12, L.VVVVS120, L.VVVVS123, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS13, L.VVVVS130, L.VVVVS131, L.VVVVS133, L.VVVVS134, L.VVVVS141, L.VVVVS142, L.VVVVS144, L.VVVVS145, L.VVVVS148, L.VVVVS151, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS160, L.VVVVS163, L.VVVVS164, L.VVVVS165, L.VVVVS167, L.VVVVS169, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS18, L.VVVVS180, L.VVVVS182, L.VVVVS184, L.VVVVS187, L.VVVVS188, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS198, L.VVVVS2, L.VVVVS201, L.VVVVS202, L.VVVVS203, L.VVVVS205, L.VVVVS207, L.VVVVS209, L.VVVVS21, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS233, L.VVVVS234, L.VVVVS237, L.VVVVS239, L.VVVVS242, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS252, L.VVVVS253, L.VVVVS255, L.VVVVS256, L.VVVVS257, L.VVVVS259, L.VVVVS261, L.VVVVS263, L.VVVVS264, L.VVVVS27, L.VVVVS28, L.VVVVS3, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS35, L.VVVVS36, L.VVVVS37, L.VVVVS38, L.VVVVS39, L.VVVVS4, L.VVVVS40, L.VVVVS5, L.VVVVS50, L.VVVVS51, L.VVVVS54, L.VVVVS55, L.VVVVS59, L.VVVVS60, L.VVVVS63, L.VVVVS64, L.VVVVS65, L.VVVVS66, L.VVVVS68, L.VVVVS70, L.VVVVS72, L.VVVVS75, L.VVVVS78, L.VVVVS79, L.VVVVS8, L.VVVVS81, L.VVVVS82, L.VVVVS88, L.VVVVS89, L.VVVVS91, L.VVVVS93, L.VVVVS95, L.VVVVS98 ],
               couplings = {(0,97):C.GC_5989,(0,107):C.GC_5989,(0,0):C.GC_5013,(0,62):C.GC_5013,(0,9):C.GC_5984,(0,16):C.GC_5982,(0,109):C.GC_5984,(0,126):C.GC_5982,(0,69):C.GC_5979,(0,73):C.GC_5982,(0,23):C.GC_5979,(0,50):C.GC_5982,(0,110):C.GC_5581,(0,111):C.GC_5581,(0,112):C.GC_5982,(0,113):C.GC_5982,(0,114):C.GC_5981,(0,116):C.GC_5981,(0,95):C.GC_5984,(0,96):C.GC_5979,(0,98):C.GC_5979,(0,99):C.GC_5984,(0,100):C.GC_5958,(0,101):C.GC_5980,(0,102):C.GC_5979,(0,103):C.GC_5007,(0,104):C.GC_5958,(0,105):C.GC_5980,(0,106):C.GC_5007,(0,108):C.GC_5979,(0,118):C.GC_4794,(0,119):C.GC_4794,(0,121):C.GC_5979,(0,120):C.GC_5973,(0,123):C.GC_5984,(0,122):C.GC_5973,(0,124):C.GC_5970,(0,125):C.GC_5974,(0,127):C.GC_5970,(0,128):C.GC_5974,(0,130):C.GC_5986,(0,129):C.GC_4795,(0,132):C.GC_5984,(0,131):C.GC_5976,(0,134):C.GC_5008,(0,1):C.GC_5009,(0,133):C.GC_5011,(0,7):C.GC_5584,(0,8):C.GC_5981,(0,10):C.GC_5982,(0,2):C.GC_5975,(0,3):C.GC_5973,(0,4):C.GC_5967,(0,5):C.GC_5011,(0,6):C.GC_5976,(0,12):C.GC_5986,(0,11):C.GC_4795,(0,14):C.GC_5008,(0,15):C.GC_5009,(0,13):C.GC_5011,(0,18):C.GC_5984,(0,17):C.GC_5976,(0,25):C.GC_5584,(0,26):C.GC_5981,(0,27):C.GC_5982,(0,19):C.GC_5975,(0,20):C.GC_5973,(0,21):C.GC_5967,(0,22):C.GC_5976,(0,24):C.GC_5011,(0,29):C.GC_5013,(0,28):C.GC_4795,(0,30):C.GC_5972,(0,31):C.GC_5975,(0,33):C.GC_5982,(0,32):C.GC_5976,(0,39):C.GC_5982,(0,40):C.GC_5981,(0,34):C.GC_5963,(0,35):C.GC_5975,(0,36):C.GC_5977,(0,37):C.GC_5010,(0,38):C.GC_5972,(0,41):C.GC_7120,(0,51):C.GC_5013,(0,49):C.GC_4795,(0,53):C.GC_5982,(0,52):C.GC_5976,(0,54):C.GC_5972,(0,55):C.GC_5975,(0,61):C.GC_5982,(0,63):C.GC_5981,(0,56):C.GC_5963,(0,57):C.GC_5975,(0,58):C.GC_5977,(0,59):C.GC_5972,(0,60):C.GC_5010,(0,64):C.GC_7120,(0,75):C.GC_4790,(0,74):C.GC_4793,(0,77):C.GC_5981,(0,76):C.GC_5973,(0,79):C.GC_5981,(0,78):C.GC_5973,(0,86):C.GC_5982,(0,87):C.GC_5982,(0,88):C.GC_5988,(0,80):C.GC_5960,(0,81):C.GC_5973,(0,82):C.GC_5973,(0,83):C.GC_5971,(0,84):C.GC_5975,(0,85):C.GC_5975,(0,89):C.GC_5438,(0,42):C.GC_4794,(0,65):C.GC_4794,(0,90):C.GC_4792,(0,45):C.GC_5962,(0,68):C.GC_5962,(0,93):C.GC_5965,(0,43):C.GC_5010,(0,66):C.GC_5972,(0,91):C.GC_5975,(0,44):C.GC_5972,(0,67):C.GC_5010,(0,92):C.GC_5975,(0,46):C.GC_5973,(0,70):C.GC_5973,(0,94):C.GC_5978,(0,115):C.GC_5984,(0,47):C.GC_5972,(0,71):C.GC_5976,(0,117):C.GC_5979,(0,48):C.GC_5976,(0,72):C.GC_5972})

V_274 = Vertex(name = 'V_274',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS112, L.VVVVS115, L.VVVVS120, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS130, L.VVVVS141, L.VVVVS144, L.VVVVS145, L.VVVVS148, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS164, L.VVVVS165, L.VVVVS167, L.VVVVS169, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS182, L.VVVVS187, L.VVVVS188, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS202, L.VVVVS203, L.VVVVS205, L.VVVVS207, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS237, L.VVVVS242, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS257, L.VVVVS259, L.VVVVS261, L.VVVVS263, L.VVVVS264, L.VVVVS65, L.VVVVS66, L.VVVVS68, L.VVVVS72, L.VVVVS78, L.VVVVS79, L.VVVVS81, L.VVVVS82, L.VVVVS88, L.VVVVS91, L.VVVVS95 ],
               couplings = {(0,62):C.GC_4919,(0,63):C.GC_4919,(0,64):C.GC_6105,(0,65):C.GC_6105,(0,66):C.GC_6103,(0,67):C.GC_6058,(0,68):C.GC_6103,(0,69):C.GC_6058,(0,70):C.GC_4920,(0,71):C.GC_5122,(0,72):C.GC_5115,(0,0):C.GC_6098,(0,1):C.GC_6105,(0,2):C.GC_6101,(0,3):C.GC_5115,(0,4):C.GC_5122,(0,5):C.GC_4920,(0,6):C.GC_5115,(0,7):C.GC_5122,(0,8):C.GC_6098,(0,9):C.GC_6105,(0,10):C.GC_6101,(0,11):C.GC_5122,(0,12):C.GC_5115,(0,13):C.GC_4920,(0,14):C.GC_5123,(0,15):C.GC_6098,(0,16):C.GC_5122,(0,17):C.GC_6102,(0,18):C.GC_6098,(0,19):C.GC_6057,(0,20):C.GC_5114,(0,21):C.GC_5123,(0,22):C.GC_7123,(0,30):C.GC_4920,(0,31):C.GC_5122,(0,32):C.GC_5123,(0,33):C.GC_6098,(0,34):C.GC_6102,(0,35):C.GC_6098,(0,36):C.GC_6057,(0,37):C.GC_5123,(0,38):C.GC_5114,(0,39):C.GC_7123,(0,47):C.GC_4913,(0,48):C.GC_6105,(0,49):C.GC_6105,(0,50):C.GC_6099,(0,51):C.GC_6105,(0,52):C.GC_6105,(0,53):C.GC_6106,(0,54):C.GC_6098,(0,55):C.GC_6098,(0,56):C.GC_5441,(0,23):C.GC_4919,(0,40):C.GC_4919,(0,57):C.GC_4912,(0,26):C.GC_6100,(0,43):C.GC_6100,(0,60):C.GC_6104,(0,24):C.GC_5114,(0,41):C.GC_5123,(0,58):C.GC_6098,(0,25):C.GC_5123,(0,42):C.GC_5114,(0,59):C.GC_6098,(0,27):C.GC_6105,(0,44):C.GC_6105,(0,61):C.GC_6097,(0,28):C.GC_5123,(0,45):C.GC_5122,(0,29):C.GC_5122,(0,46):C.GC_5123})

V_275 = Vertex(name = 'V_275',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS100, L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS106, L.VVVVS107, L.VVVVS108, L.VVVVS109, L.VVVVS11, L.VVVVS110, L.VVVVS114, L.VVVVS115, L.VVVVS116, L.VVVVS117, L.VVVVS118, L.VVVVS119, L.VVVVS12, L.VVVVS120, L.VVVVS121, L.VVVVS123, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS13, L.VVVVS131, L.VVVVS132, L.VVVVS133, L.VVVVS134, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS146, L.VVVVS147, L.VVVVS148, L.VVVVS15, L.VVVVS150, L.VVVVS151, L.VVVVS153, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS159, L.VVVVS160, L.VVVVS161, L.VVVVS162, L.VVVVS163, L.VVVVS164, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS17, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS18, L.VVVVS181, L.VVVVS182, L.VVVVS183, L.VVVVS184, L.VVVVS185, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS19, L.VVVVS190, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS198, L.VVVVS199, L.VVVVS20, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS209, L.VVVVS21, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS239, L.VVVVS240, L.VVVVS242, L.VVVVS244, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS254, L.VVVVS255, L.VVVVS256, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS27, L.VVVVS28, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS37, L.VVVVS38, L.VVVVS5, L.VVVVS50, L.VVVVS51, L.VVVVS54, L.VVVVS55, L.VVVVS57, L.VVVVS58, L.VVVVS6, L.VVVVS61, L.VVVVS62, L.VVVVS67, L.VVVVS68, L.VVVVS69, L.VVVVS7, L.VVVVS70, L.VVVVS71, L.VVVVS72, L.VVVVS74, L.VVVVS75, L.VVVVS78, L.VVVVS79, L.VVVVS8, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS86, L.VVVVS87, L.VVVVS9, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS93, L.VVVVS94, L.VVVVS95, L.VVVVS97, L.VVVVS98 ],
               couplings = {(0,150):C.GC_5567,(0,0):C.GC_5569,(0,9):C.GC_5567,(0,17):C.GC_5566,(0,122):C.GC_5567,(0,129):C.GC_5567,(0,135):C.GC_5569,(0,143):C.GC_5566,(0,67):C.GC_5568,(0,75):C.GC_5569,(0,84):C.GC_5568,(0,88):C.GC_5566,(0,25):C.GC_5568,(0,36):C.GC_5568,(0,53):C.GC_5569,(0,58):C.GC_5566,(0,123):C.GC_5569,(0,124):C.GC_5569,(0,125):C.GC_5566,(0,126):C.GC_5566,(0,127):C.GC_5567,(0,128):C.GC_5567,(0,130):C.GC_5568,(0,131):C.GC_5568,(0,114):C.GC_5569,(0,115):C.GC_5566,(0,116):C.GC_5569,(0,117):C.GC_5566,(0,118):C.GC_5567,(0,119):C.GC_5568,(0,120):C.GC_5567,(0,121):C.GC_5568,(0,134):C.GC_5568,(0,136):C.GC_5568,(0,132):C.GC_5561,(0,133):C.GC_5561,(0,139):C.GC_5567,(0,140):C.GC_5567,(0,137):C.GC_5561,(0,138):C.GC_5561,(0,148):C.GC_5570,(0,149):C.GC_5565,(0,141):C.GC_4768,(0,142):C.GC_4768,(0,144):C.GC_4770,(0,145):C.GC_4768,(0,146):C.GC_4768,(0,147):C.GC_4770,(0,154):C.GC_5567,(0,151):C.GC_5560,(0,152):C.GC_5563,(0,153):C.GC_5562,(0,157):C.GC_5566,(0,158):C.GC_4763,(0,1):C.GC_4764,(0,155):C.GC_5563,(0,156):C.GC_4767,(0,6):C.GC_5566,(0,7):C.GC_5567,(0,8):C.GC_5569,(0,10):C.GC_5568,(0,2):C.GC_4769,(0,3):C.GC_4769,(0,4):C.GC_4769,(0,5):C.GC_4769,(0,13):C.GC_5566,(0,14):C.GC_4763,(0,15):C.GC_4764,(0,11):C.GC_5563,(0,12):C.GC_4767,(0,20):C.GC_5567,(0,16):C.GC_5560,(0,18):C.GC_5563,(0,19):C.GC_5562,(0,26):C.GC_5566,(0,27):C.GC_5567,(0,28):C.GC_5569,(0,29):C.GC_5568,(0,21):C.GC_4769,(0,22):C.GC_4769,(0,23):C.GC_4769,(0,24):C.GC_4769,(0,33):C.GC_5567,(0,30):C.GC_5563,(0,31):C.GC_5560,(0,32):C.GC_5562,(0,37):C.GC_4763,(0,38):C.GC_5566,(0,39):C.GC_4764,(0,34):C.GC_4767,(0,35):C.GC_5563,(0,44):C.GC_5566,(0,45):C.GC_5567,(0,46):C.GC_5569,(0,47):C.GC_5568,(0,40):C.GC_4769,(0,41):C.GC_4769,(0,42):C.GC_4769,(0,43):C.GC_4769,(0,48):C.GC_7116,(0,61):C.GC_4763,(0,62):C.GC_5566,(0,63):C.GC_4764,(0,59):C.GC_4767,(0,60):C.GC_5563,(0,68):C.GC_5567,(0,64):C.GC_5563,(0,65):C.GC_5560,(0,66):C.GC_5562,(0,73):C.GC_5566,(0,74):C.GC_5567,(0,76):C.GC_5569,(0,77):C.GC_5568,(0,69):C.GC_4769,(0,70):C.GC_4769,(0,71):C.GC_4769,(0,72):C.GC_4769,(0,78):C.GC_7116,(0,91):C.GC_5566,(0,92):C.GC_5569,(0,89):C.GC_5561,(0,90):C.GC_5561,(0,95):C.GC_5566,(0,96):C.GC_5569,(0,93):C.GC_5561,(0,94):C.GC_5561,(0,103):C.GC_5564,(0,104):C.GC_5571,(0,97):C.GC_4770,(0,98):C.GC_4768,(0,99):C.GC_4768,(0,100):C.GC_4770,(0,101):C.GC_4768,(0,102):C.GC_4768,(0,105):C.GC_5434,(0,49):C.GC_5560,(0,79):C.GC_4766,(0,106):C.GC_5562,(0,51):C.GC_4766,(0,81):C.GC_5560,(0,108):C.GC_5562,(0,54):C.GC_4768,(0,83):C.GC_4768,(0,110):C.GC_4771,(0,50):C.GC_4766,(0,80):C.GC_5560,(0,107):C.GC_5562,(0,52):C.GC_5560,(0,82):C.GC_4766,(0,109):C.GC_5562,(0,55):C.GC_4768,(0,85):C.GC_4768,(0,111):C.GC_4771,(0,56):C.GC_4768,(0,86):C.GC_4768,(0,112):C.GC_4771,(0,57):C.GC_4768,(0,87):C.GC_4768,(0,113):C.GC_4771})

V_276 = Vertex(name = 'V_276',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS106, L.VVVVS114, L.VVVVS115, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS147, L.VVVVS148, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS159, L.VVVVS164, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS181, L.VVVVS182, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS202, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS236, L.VVVVS237, L.VVVVS240, L.VVVVS242, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS67, L.VVVVS68, L.VVVVS71, L.VVVVS72, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS94, L.VVVVS95 ],
               couplings = {(0,68):C.GC_5757,(0,69):C.GC_5757,(0,70):C.GC_5757,(0,71):C.GC_5757,(0,72):C.GC_4929,(0,73):C.GC_4929,(0,74):C.GC_4931,(0,75):C.GC_4929,(0,76):C.GC_4929,(0,77):C.GC_4931,(0,78):C.GC_4903,(0,79):C.GC_4902,(0,80):C.GC_5756,(0,81):C.GC_4902,(0,82):C.GC_4895,(0,0):C.GC_4928,(0,1):C.GC_4928,(0,2):C.GC_4928,(0,3):C.GC_4928,(0,4):C.GC_4902,(0,5):C.GC_4895,(0,6):C.GC_4903,(0,7):C.GC_4902,(0,8):C.GC_5756,(0,9):C.GC_4928,(0,10):C.GC_4928,(0,11):C.GC_4928,(0,12):C.GC_4928,(0,13):C.GC_4902,(0,14):C.GC_4903,(0,15):C.GC_5756,(0,16):C.GC_4895,(0,17):C.GC_4902,(0,18):C.GC_4928,(0,19):C.GC_4928,(0,20):C.GC_4928,(0,21):C.GC_4928,(0,22):C.GC_7117,(0,31):C.GC_4895,(0,32):C.GC_4902,(0,33):C.GC_4902,(0,34):C.GC_4903,(0,35):C.GC_5756,(0,36):C.GC_4928,(0,37):C.GC_4928,(0,38):C.GC_4928,(0,39):C.GC_4928,(0,40):C.GC_7117,(0,49):C.GC_5757,(0,50):C.GC_5757,(0,51):C.GC_5757,(0,52):C.GC_5757,(0,53):C.GC_4931,(0,54):C.GC_4929,(0,55):C.GC_4929,(0,56):C.GC_4931,(0,57):C.GC_4929,(0,58):C.GC_4929,(0,59):C.GC_5435,(0,23):C.GC_4903,(0,41):C.GC_4894,(0,60):C.GC_5756,(0,25):C.GC_4894,(0,43):C.GC_4903,(0,62):C.GC_5756,(0,27):C.GC_4929,(0,45):C.GC_4929,(0,64):C.GC_4930,(0,24):C.GC_4894,(0,42):C.GC_4903,(0,61):C.GC_5756,(0,26):C.GC_4903,(0,44):C.GC_4894,(0,63):C.GC_5756,(0,28):C.GC_4929,(0,46):C.GC_4929,(0,65):C.GC_4930,(0,29):C.GC_4929,(0,47):C.GC_4929,(0,66):C.GC_4930,(0,30):C.GC_4929,(0,48):C.GC_4929,(0,67):C.GC_4930})

V_277 = Vertex(name = 'V_277',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3495,(0,6):C.GC_3488,(0,4):C.GC_3495,(0,7):C.GC_3488,(0,9):C.GC_3474,(0,11):C.GC_3474,(0,5):C.GC_3495,(0,8):C.GC_3488,(0,10):C.GC_3474,(0,1):C.GC_3474,(0,2):C.GC_3474,(0,3):C.GC_3474})

V_278 = Vertex(name = 'V_278',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3775,(0,6):C.GC_3763,(0,4):C.GC_3775,(0,7):C.GC_3763,(0,9):C.GC_3739,(0,11):C.GC_3739,(0,5):C.GC_3775,(0,8):C.GC_3763,(0,10):C.GC_3739,(0,1):C.GC_3739,(0,2):C.GC_3739,(0,3):C.GC_3739})

V_279 = Vertex(name = 'V_279',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_6281,(0,1):C.GC_6279,(0,2):C.GC_6280,(0,3):C.GC_6276,(0,4):C.GC_6279,(0,5):C.GC_6276})

V_280 = Vertex(name = 'V_280',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_6385,(0,1):C.GC_6401,(0,2):C.GC_6384,(0,3):C.GC_6398,(0,4):C.GC_6401,(0,5):C.GC_6398})

V_281 = Vertex(name = 'V_281',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3489,(0,4):C.GC_3491,(0,2):C.GC_3477,(0,5):C.GC_3478,(0,7):C.GC_3480,(0,9):C.GC_3479,(0,3):C.GC_3477,(0,6):C.GC_3478,(0,8):C.GC_3480,(0,1):C.GC_3479})

V_282 = Vertex(name = 'V_282',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3747,(0,4):C.GC_3748,(0,2):C.GC_3766,(0,5):C.GC_3768,(0,7):C.GC_3769,(0,9):C.GC_3767,(0,3):C.GC_3766,(0,6):C.GC_3768,(0,8):C.GC_3769,(0,1):C.GC_3767})

V_283 = Vertex(name = 'V_283',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8 ],
               couplings = {(0,0):C.GC_3484,(0,6):C.GC_3483,(0,4):C.GC_3484,(0,7):C.GC_3483,(0,5):C.GC_3493,(0,8):C.GC_3486,(0,9):C.GC_3476,(0,1):C.GC_3475,(0,2):C.GC_3476,(0,3):C.GC_3475})

V_284 = Vertex(name = 'V_284',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS8 ],
               couplings = {(0,0):C.GC_3773,(0,6):C.GC_3765,(0,4):C.GC_3773,(0,7):C.GC_3765,(0,5):C.GC_3749,(0,8):C.GC_3746,(0,9):C.GC_3772,(0,1):C.GC_3764,(0,2):C.GC_3772,(0,3):C.GC_3764})

V_285 = Vertex(name = 'V_285',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3481,(0,6):C.GC_3481,(0,4):C.GC_3490,(0,7):C.GC_3492,(0,9):C.GC_3490,(0,11):C.GC_3492,(0,5):C.GC_3490,(0,8):C.GC_3492,(0,10):C.GC_3490,(0,1):C.GC_3492,(0,2):C.GC_3482,(0,3):C.GC_3482})

V_286 = Vertex(name = 'V_286',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3740,(0,6):C.GC_3740,(0,4):C.GC_3770,(0,7):C.GC_3771,(0,9):C.GC_3770,(0,11):C.GC_3771,(0,5):C.GC_3770,(0,8):C.GC_3771,(0,10):C.GC_3770,(0,1):C.GC_3771,(0,2):C.GC_3741,(0,3):C.GC_3741})

V_287 = Vertex(name = 'V_287',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS4, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6278,(0,1):C.GC_6278,(0,2):C.GC_6277,(0,3):C.GC_6277})

V_288 = Vertex(name = 'V_288',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS4, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6399,(0,1):C.GC_6399,(0,2):C.GC_6400,(0,3):C.GC_6400})

V_289 = Vertex(name = 'V_289',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,3):C.GC_3478,(0,5):C.GC_3477,(0,7):C.GC_3478,(0,9):C.GC_3477,(0,4):C.GC_3479,(0,6):C.GC_3480,(0,8):C.GC_3479,(0,0):C.GC_3480,(0,1):C.GC_3489,(0,2):C.GC_3491})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,3):C.GC_3768,(0,5):C.GC_3766,(0,7):C.GC_3768,(0,9):C.GC_3766,(0,4):C.GC_3767,(0,6):C.GC_3769,(0,8):C.GC_3767,(0,0):C.GC_3769,(0,1):C.GC_3747,(0,2):C.GC_3748})

V_291 = Vertex(name = 'V_291',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3485,(0,6):C.GC_3485,(0,4):C.GC_3485,(0,7):C.GC_3485,(0,9):C.GC_3485,(0,11):C.GC_3485,(0,5):C.GC_3494,(0,8):C.GC_3487,(0,10):C.GC_3494,(0,1):C.GC_3487,(0,2):C.GC_3494,(0,3):C.GC_3487})

V_292 = Vertex(name = 'V_292',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS10, L.VSSSS11, L.VSSSS12, L.VSSSS2, L.VSSSS3, L.VSSSS4, L.VSSSS5, L.VSSSS6, L.VSSSS7, L.VSSSS8, L.VSSSS9 ],
               couplings = {(0,0):C.GC_3742,(0,6):C.GC_3742,(0,4):C.GC_3742,(0,7):C.GC_3742,(0,9):C.GC_3742,(0,11):C.GC_3742,(0,5):C.GC_3774,(0,8):C.GC_3762,(0,10):C.GC_3774,(0,1):C.GC_3762,(0,2):C.GC_3774,(0,3):C.GC_3762})

V_293 = Vertex(name = 'V_293',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS107, L.VVVSS108, L.VVVSS11, L.VVVSS111, L.VVVSS112, L.VVVSS113, L.VVVSS114, L.VVVSS116, L.VVVSS118, L.VVVSS119, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS14, L.VVVSS141, L.VVVSS143, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS157, L.VVVSS158, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS38, L.VVVSS4, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS52, L.VVVSS54, L.VVVSS55, L.VVVSS58, L.VVVSS60, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS65, L.VVVSS67, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS89, L.VVVSS9, L.VVVSS91, L.VVVSS93, L.VVVSS94, L.VVVSS96, L.VVVSS97, L.VVVSS99 ],
               couplings = {(0,90):C.GC_4054,(0,89):C.GC_4051,(0,94):C.GC_1152,(0,95):C.GC_434,(0,92):C.GC_3374,(0,93):C.GC_3369,(0,77):C.GC_4019,(0,0):C.GC_3997,(0,108):C.GC_1153,(0,121):C.GC_2797,(0,91):C.GC_3398,(0,100):C.GC_2800,(0,131):C.GC_4046,(0,126):C.GC_3991,(0,14):C.GC_1140,(0,24):C.GC_433,(0,32):C.GC_3339,(0,1):C.GC_3355,(0,6):C.GC_3404,(0,48):C.GC_3340,(0,39):C.GC_3350,(0,78):C.GC_3370,(0,82):C.GC_3377,(0,61):C.GC_3400,(0,71):C.GC_3401,(0,132):C.GC_1161,(0,133):C.GC_3377,(0,3):C.GC_4018,(0,2):C.GC_4017,(0,5):C.GC_1153,(0,4):C.GC_3370,(0,7):C.GC_428,(0,8):C.GC_428,(0,9):C.GC_433,(0,10):C.GC_433,(0,97):C.GC_4055,(0,96):C.GC_4001,(0,99):C.GC_1152,(0,98):C.GC_3399,(0,104):C.GC_1159,(0,105):C.GC_427,(0,101):C.GC_1177,(0,102):C.GC_1174,(0,103):C.GC_3408,(0,107):C.GC_4012,(0,106):C.GC_3995,(0,110):C.GC_1141,(0,111):C.GC_3338,(0,109):C.GC_3354,(0,114):C.GC_427,(0,115):C.GC_434,(0,112):C.GC_1178,(0,113):C.GC_3401,(0,117):C.GC_3336,(0,116):C.GC_3356,(0,119):C.GC_3369,(0,118):C.GC_3397,(0,124):C.GC_3375,(0,125):C.GC_434,(0,120):C.GC_1173,(0,122):C.GC_3405,(0,123):C.GC_3404,(0,22):C.GC_1151,(0,23):C.GC_427,(0,13):C.GC_6776,(0,34):C.GC_1150,(0,44):C.GC_4014,(0,45):C.GC_3374,(0,35):C.GC_6773,(0,58):C.GC_4050,(0,68):C.GC_4051,(0,69):C.GC_3369,(0,59):C.GC_6773,(0,80):C.GC_4017,(0,81):C.GC_3370,(0,15):C.GC_3353,(0,25):C.GC_3349,(0,36):C.GC_4000,(0,46):C.GC_3996,(0,60):C.GC_3994,(0,70):C.GC_3990,(0,16):C.GC_3393,(0,26):C.GC_3396,(0,37):C.GC_3351,(0,47):C.GC_3352,(0,62):C.GC_3395,(0,72):C.GC_3394,(0,84):C.GC_4049,(0,87):C.GC_1150,(0,11):C.GC_1154,(0,18):C.GC_3994,(0,27):C.GC_1178,(0,41):C.GC_3395,(0,49):C.GC_1173,(0,64):C.GC_3997,(0,65):C.GC_3398,(0,128):C.GC_4013,(0,130):C.GC_1151,(0,136):C.GC_1156,(0,28):C.GC_3990,(0,31):C.GC_1177,(0,52):C.GC_3394,(0,54):C.GC_1174,(0,74):C.GC_4001,(0,75):C.GC_3399,(0,17):C.GC_3408,(0,38):C.GC_3405,(0,63):C.GC_2801,(0,83):C.GC_4046,(0,88):C.GC_433,(0,19):C.GC_4000,(0,40):C.GC_3991,(0,42):C.GC_3404,(0,66):C.GC_3405,(0,127):C.GC_4012,(0,29):C.GC_3996,(0,51):C.GC_3995,(0,85):C.GC_3367,(0,86):C.GC_3372,(0,12):C.GC_3372,(0,20):C.GC_3400,(0,21):C.GC_3401,(0,43):C.GC_3393,(0,50):C.GC_3408,(0,67):C.GC_3408,(0,73):C.GC_3401,(0,129):C.GC_3368,(0,137):C.GC_3374,(0,30):C.GC_3397,(0,53):C.GC_3396,(0,55):C.GC_3405,(0,76):C.GC_3404,(0,134):C.GC_2245,(0,135):C.GC_2797,(0,33):C.GC_2249,(0,56):C.GC_2248,(0,57):C.GC_2801,(0,79):C.GC_2800})

V_294 = Vertex(name = 'V_294',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS141, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS157, L.VVVSS158, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS199, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS4, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS55, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4220,(0,56):C.GC_3700,(0,59):C.GC_2988,(0,72):C.GC_4224,(0,1):C.GC_3675,(0,2):C.GC_3701,(0,23):C.GC_3671,(0,41):C.GC_3700,(0,49):C.GC_3702,(0,57):C.GC_4222,(0,58):C.GC_3699,(0,60):C.GC_1301,(0,61):C.GC_1300,(0,62):C.GC_3703,(0,63):C.GC_4226,(0,64):C.GC_3676,(0,65):C.GC_1302,(0,66):C.GC_3702,(0,67):C.GC_3677,(0,68):C.GC_3699,(0,69):C.GC_1299,(0,70):C.GC_3704,(0,71):C.GC_3701,(0,3):C.GC_6811,(0,19):C.GC_6825,(0,39):C.GC_6825,(0,4):C.GC_3674,(0,11):C.GC_3670,(0,20):C.GC_4221,(0,28):C.GC_4219,(0,40):C.GC_4225,(0,48):C.GC_4223,(0,5):C.GC_3697,(0,12):C.GC_3698,(0,21):C.GC_3673,(0,29):C.GC_3672,(0,42):C.GC_3697,(0,50):C.GC_3698,(0,7):C.GC_4225,(0,13):C.GC_1302,(0,25):C.GC_3697,(0,30):C.GC_1299,(0,44):C.GC_4220,(0,45):C.GC_3700,(0,14):C.GC_4223,(0,17):C.GC_1301,(0,33):C.GC_3698,(0,35):C.GC_1300,(0,52):C.GC_4222,(0,53):C.GC_3699,(0,6):C.GC_3703,(0,22):C.GC_3704,(0,43):C.GC_2989,(0,8):C.GC_4221,(0,24):C.GC_4224,(0,26):C.GC_3701,(0,46):C.GC_3704,(0,15):C.GC_4219,(0,32):C.GC_4226,(0,9):C.GC_3700,(0,10):C.GC_3702,(0,27):C.GC_3697,(0,31):C.GC_3703,(0,47):C.GC_3703,(0,51):C.GC_3702,(0,16):C.GC_3699,(0,34):C.GC_3698,(0,36):C.GC_3704,(0,54):C.GC_3701,(0,18):C.GC_2616,(0,37):C.GC_2615,(0,38):C.GC_2989,(0,55):C.GC_2988})

V_295 = Vertex(name = 'V_295',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5647,(0,1):C.GC_5647,(0,2):C.GC_5652,(0,3):C.GC_5652,(0,4):C.GC_5626,(0,5):C.GC_5626,(0,6):C.GC_5631,(0,7):C.GC_5639,(0,8):C.GC_5639})

V_296 = Vertex(name = 'V_296',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5816,(0,1):C.GC_5816,(0,2):C.GC_5795,(0,3):C.GC_5795,(0,4):C.GC_5824,(0,5):C.GC_5824,(0,6):C.GC_5809,(0,7):C.GC_5784,(0,8):C.GC_5784})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5651,(0,1):C.GC_5635,(0,2):C.GC_5650,(0,3):C.GC_5625,(0,4):C.GC_5637,(0,5):C.GC_5649,(0,6):C.GC_5635,(0,7):C.GC_5636,(0,8):C.GC_5636})

V_298 = Vertex(name = 'V_298',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5794,(0,1):C.GC_5818,(0,2):C.GC_5820,(0,3):C.GC_5819,(0,4):C.GC_5817,(0,5):C.GC_5793,(0,6):C.GC_5818,(0,7):C.GC_5783,(0,8):C.GC_5783})

V_299 = Vertex(name = 'V_299',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5654,(0,1):C.GC_5644,(0,2):C.GC_5654,(0,3):C.GC_5646,(0,4):C.GC_5644,(0,5):C.GC_5646,(0,6):C.GC_5627,(0,7):C.GC_5627,(0,8):C.GC_5628})

V_300 = Vertex(name = 'V_300',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5830,(0,1):C.GC_5812,(0,2):C.GC_5830,(0,3):C.GC_5813,(0,4):C.GC_5812,(0,5):C.GC_5813,(0,6):C.GC_5823,(0,7):C.GC_5823,(0,8):C.GC_5781})

V_301 = Vertex(name = 'V_301',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS111, L.VVVSS112, L.VVVSS113, L.VVVSS114, L.VVVSS116, L.VVVSS118, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS127, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS141, L.VVVSS143, L.VVVSS144, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS154, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS171, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS191, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS26, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS31, L.VVVSS32, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS40, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS52, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS58, L.VVVSS60, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS91, L.VVVSS93, L.VVVSS94, L.VVVSS96, L.VVVSS97, L.VVVSS99 ],
               couplings = {(0,85):C.GC_4042,(0,84):C.GC_4041,(0,88):C.GC_1162,(0,87):C.GC_3379,(0,75):C.GC_4033,(0,0):C.GC_4011,(0,102):C.GC_1163,(0,86):C.GC_3409,(0,129):C.GC_4035,(0,123):C.GC_3985,(0,14):C.GC_1143,(0,30):C.GC_3342,(0,1):C.GC_3358,(0,45):C.GC_3333,(0,36):C.GC_3360,(0,76):C.GC_3380,(0,59):C.GC_3411,(0,131):C.GC_1166,(0,132):C.GC_3384,(0,3):C.GC_4032,(0,2):C.GC_4029,(0,6):C.GC_1163,(0,7):C.GC_430,(0,4):C.GC_3361,(0,5):C.GC_3380,(0,8):C.GC_431,(0,9):C.GC_431,(0,10):C.GC_430,(0,11):C.GC_430,(0,90):C.GC_4043,(0,89):C.GC_4007,(0,93):C.GC_1162,(0,94):C.GC_2796,(0,91):C.GC_3412,(0,92):C.GC_2799,(0,98):C.GC_1164,(0,99):C.GC_432,(0,95):C.GC_1180,(0,96):C.GC_1171,(0,97):C.GC_3415,(0,101):C.GC_4023,(0,100):C.GC_3981,(0,105):C.GC_1142,(0,106):C.GC_429,(0,107):C.GC_3343,(0,103):C.GC_3359,(0,104):C.GC_3386,(0,110):C.GC_432,(0,111):C.GC_429,(0,108):C.GC_1183,(0,109):C.GC_3386,(0,113):C.GC_3344,(0,112):C.GC_3346,(0,116):C.GC_3379,(0,117):C.GC_3382,(0,114):C.GC_3410,(0,115):C.GC_3387,(0,121):C.GC_3382,(0,122):C.GC_429,(0,118):C.GC_1168,(0,119):C.GC_3414,(0,120):C.GC_3387,(0,20):C.GC_1149,(0,32):C.GC_1148,(0,33):C.GC_431,(0,40):C.GC_4027,(0,56):C.GC_4037,(0,57):C.GC_3361,(0,41):C.GC_6772,(0,63):C.GC_4041,(0,64):C.GC_3379,(0,78):C.GC_4029,(0,79):C.GC_3380,(0,65):C.GC_6775,(0,15):C.GC_3345,(0,21):C.GC_3357,(0,34):C.GC_4006,(0,42):C.GC_4010,(0,58):C.GC_3980,(0,66):C.GC_3984,(0,16):C.GC_3390,(0,22):C.GC_3391,(0,35):C.GC_3348,(0,43):C.GC_3347,(0,60):C.GC_3392,(0,67):C.GC_3389,(0,81):C.GC_4036,(0,83):C.GC_1148,(0,12):C.GC_1145,(0,17):C.GC_3980,(0,24):C.GC_1183,(0,38):C.GC_3392,(0,46):C.GC_1168,(0,61):C.GC_4011,(0,62):C.GC_3409,(0,125):C.GC_4026,(0,128):C.GC_1149,(0,135):C.GC_1147,(0,25):C.GC_3984,(0,29):C.GC_1180,(0,49):C.GC_3389,(0,52):C.GC_1171,(0,70):C.GC_4007,(0,71):C.GC_3412,(0,23):C.GC_3414,(0,44):C.GC_3415,(0,68):C.GC_2802,(0,80):C.GC_4035,(0,18):C.GC_4006,(0,37):C.GC_3985,(0,124):C.GC_4023,(0,130):C.GC_429,(0,26):C.GC_4010,(0,48):C.GC_3981,(0,50):C.GC_3386,(0,72):C.GC_3415,(0,82):C.GC_3365,(0,13):C.GC_3361,(0,19):C.GC_3411,(0,39):C.GC_3390,(0,47):C.GC_3415,(0,69):C.GC_3386,(0,126):C.GC_3366,(0,127):C.GC_3363,(0,136):C.GC_3363,(0,27):C.GC_3410,(0,28):C.GC_3387,(0,51):C.GC_3391,(0,53):C.GC_3414,(0,73):C.GC_3414,(0,74):C.GC_3387,(0,133):C.GC_2244,(0,134):C.GC_2796,(0,31):C.GC_2250,(0,54):C.GC_2247,(0,55):C.GC_2802,(0,77):C.GC_2799})

V_302 = Vertex(name = 'V_302',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS141, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS191, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS199, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4218,(0,53):C.GC_3705,(0,71):C.GC_4230,(0,1):C.GC_3680,(0,19):C.GC_3681,(0,38):C.GC_3705,(0,54):C.GC_4216,(0,55):C.GC_3706,(0,56):C.GC_2987,(0,57):C.GC_1304,(0,58):C.GC_1297,(0,59):C.GC_3708,(0,60):C.GC_4228,(0,61):C.GC_3679,(0,62):C.GC_3693,(0,63):C.GC_1303,(0,64):C.GC_3693,(0,65):C.GC_3667,(0,66):C.GC_3706,(0,67):C.GC_3694,(0,68):C.GC_1298,(0,69):C.GC_3707,(0,70):C.GC_3694,(0,23):C.GC_6827,(0,42):C.GC_6824,(0,2):C.GC_3666,(0,7):C.GC_3678,(0,17):C.GC_4215,(0,24):C.GC_4217,(0,37):C.GC_4227,(0,43):C.GC_4229,(0,3):C.GC_3696,(0,8):C.GC_3695,(0,18):C.GC_3668,(0,25):C.GC_3669,(0,39):C.GC_3696,(0,44):C.GC_3695,(0,4):C.GC_4227,(0,10):C.GC_1303,(0,21):C.GC_3696,(0,27):C.GC_1298,(0,40):C.GC_4218,(0,41):C.GC_3705,(0,11):C.GC_4229,(0,15):C.GC_1304,(0,30):C.GC_3695,(0,33):C.GC_1297,(0,47):C.GC_4216,(0,48):C.GC_3706,(0,9):C.GC_3707,(0,26):C.GC_3708,(0,45):C.GC_2990,(0,5):C.GC_4215,(0,20):C.GC_4230,(0,12):C.GC_4217,(0,29):C.GC_4228,(0,31):C.GC_3693,(0,49):C.GC_3708,(0,6):C.GC_3705,(0,22):C.GC_3696,(0,28):C.GC_3708,(0,46):C.GC_3693,(0,13):C.GC_3706,(0,14):C.GC_3694,(0,32):C.GC_3695,(0,34):C.GC_3707,(0,50):C.GC_3707,(0,51):C.GC_3694,(0,16):C.GC_2617,(0,35):C.GC_2614,(0,36):C.GC_2990,(0,52):C.GC_2987})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS3, L.VVSSS4, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5632,(0,1):C.GC_5632,(0,2):C.GC_5634,(0,3):C.GC_5634,(0,4):C.GC_5640,(0,5):C.GC_5640,(0,6):C.GC_5641})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS3, L.VVSSS4, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5826,(0,1):C.GC_5826,(0,2):C.GC_5821,(0,3):C.GC_5821,(0,4):C.GC_5810,(0,5):C.GC_5810,(0,6):C.GC_5811})

V_305 = Vertex(name = 'V_305',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6870,(0,1):C.GC_6870,(0,2):C.GC_6878,(0,3):C.GC_6878,(0,4):C.GC_6878,(0,5):C.GC_6878})

V_306 = Vertex(name = 'V_306',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6914,(0,1):C.GC_6914,(0,2):C.GC_6910,(0,3):C.GC_6910,(0,4):C.GC_6910,(0,5):C.GC_6910})

V_307 = Vertex(name = 'V_307',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS107, L.VVVSS108, L.VVVSS11, L.VVVSS111, L.VVVSS112, L.VVVSS113, L.VVVSS114, L.VVVSS116, L.VVVSS118, L.VVVSS119, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS14, L.VVVSS141, L.VVVSS143, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS157, L.VVVSS158, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS38, L.VVVSS4, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS52, L.VVVSS54, L.VVVSS55, L.VVVSS58, L.VVVSS60, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS65, L.VVVSS67, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS89, L.VVVSS9, L.VVVSS91, L.VVVSS93, L.VVVSS94, L.VVVSS96, L.VVVSS97, L.VVVSS99 ],
               couplings = {(0,90):C.GC_4048,(0,89):C.GC_4046,(0,94):C.GC_1150,(0,95):C.GC_433,(0,92):C.GC_3378,(0,93):C.GC_3367,(0,77):C.GC_4015,(0,0):C.GC_3992,(0,108):C.GC_1151,(0,121):C.GC_2798,(0,91):C.GC_3393,(0,100):C.GC_2801,(0,131):C.GC_4051,(0,126):C.GC_4002,(0,14):C.GC_1139,(0,24):C.GC_434,(0,32):C.GC_3334,(0,1):C.GC_3351,(0,6):C.GC_3407,(0,48):C.GC_3337,(0,39):C.GC_3353,(0,78):C.GC_3368,(0,82):C.GC_3373,(0,61):C.GC_3395,(0,71):C.GC_3406,(0,132):C.GC_1157,(0,133):C.GC_3373,(0,3):C.GC_4016,(0,2):C.GC_4012,(0,5):C.GC_1151,(0,4):C.GC_3368,(0,7):C.GC_427,(0,8):C.GC_427,(0,9):C.GC_434,(0,10):C.GC_434,(0,97):C.GC_4047,(0,96):C.GC_3988,(0,99):C.GC_1150,(0,98):C.GC_3396,(0,104):C.GC_1155,(0,105):C.GC_428,(0,101):C.GC_1172,(0,102):C.GC_1179,(0,103):C.GC_3403,(0,107):C.GC_4017,(0,106):C.GC_3998,(0,110):C.GC_1138,(0,111):C.GC_3335,(0,109):C.GC_3352,(0,114):C.GC_428,(0,115):C.GC_433,(0,112):C.GC_1175,(0,113):C.GC_3406,(0,117):C.GC_3341,(0,116):C.GC_3349,(0,119):C.GC_3367,(0,118):C.GC_3394,(0,124):C.GC_3371,(0,125):C.GC_433,(0,120):C.GC_1176,(0,122):C.GC_3402,(0,123):C.GC_3407,(0,22):C.GC_1153,(0,23):C.GC_428,(0,13):C.GC_6777,(0,34):C.GC_1152,(0,44):C.GC_4020,(0,45):C.GC_3378,(0,35):C.GC_6774,(0,58):C.GC_4052,(0,68):C.GC_4046,(0,69):C.GC_3367,(0,59):C.GC_6774,(0,80):C.GC_4012,(0,81):C.GC_3368,(0,15):C.GC_3350,(0,25):C.GC_3356,(0,36):C.GC_3989,(0,46):C.GC_3993,(0,60):C.GC_3999,(0,70):C.GC_4003,(0,16):C.GC_3398,(0,26):C.GC_3399,(0,37):C.GC_3355,(0,47):C.GC_3354,(0,62):C.GC_3400,(0,72):C.GC_3397,(0,84):C.GC_4053,(0,87):C.GC_1152,(0,11):C.GC_1158,(0,18):C.GC_3999,(0,27):C.GC_1175,(0,41):C.GC_3400,(0,49):C.GC_1176,(0,64):C.GC_3992,(0,65):C.GC_3393,(0,128):C.GC_4021,(0,130):C.GC_1153,(0,136):C.GC_1160,(0,28):C.GC_4003,(0,31):C.GC_1172,(0,52):C.GC_3397,(0,54):C.GC_1179,(0,74):C.GC_3988,(0,75):C.GC_3396,(0,17):C.GC_3403,(0,38):C.GC_3402,(0,63):C.GC_2800,(0,83):C.GC_4051,(0,88):C.GC_434,(0,19):C.GC_3989,(0,40):C.GC_4002,(0,42):C.GC_3407,(0,66):C.GC_3402,(0,127):C.GC_4017,(0,29):C.GC_3993,(0,51):C.GC_3998,(0,85):C.GC_3369,(0,86):C.GC_3376,(0,12):C.GC_3376,(0,20):C.GC_3395,(0,21):C.GC_3406,(0,43):C.GC_3398,(0,50):C.GC_3403,(0,67):C.GC_3403,(0,73):C.GC_3406,(0,129):C.GC_3370,(0,137):C.GC_3378,(0,30):C.GC_3394,(0,53):C.GC_3399,(0,55):C.GC_3402,(0,76):C.GC_3407,(0,134):C.GC_2246,(0,135):C.GC_2798,(0,33):C.GC_2248,(0,56):C.GC_2249,(0,57):C.GC_2800,(0,79):C.GC_2801})

V_308 = Vertex(name = 'V_308',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS141, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS157, L.VVVSS158, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS199, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS4, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS55, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4225,(0,56):C.GC_3697,(0,59):C.GC_2989,(0,72):C.GC_4221,(0,1):C.GC_3673,(0,2):C.GC_3704,(0,23):C.GC_3674,(0,41):C.GC_3697,(0,49):C.GC_3703,(0,57):C.GC_4223,(0,58):C.GC_3698,(0,60):C.GC_1300,(0,61):C.GC_1301,(0,62):C.GC_3702,(0,63):C.GC_4219,(0,64):C.GC_3672,(0,65):C.GC_1299,(0,66):C.GC_3703,(0,67):C.GC_3670,(0,68):C.GC_3698,(0,69):C.GC_1302,(0,70):C.GC_3701,(0,71):C.GC_3704,(0,3):C.GC_6812,(0,19):C.GC_6826,(0,39):C.GC_6826,(0,4):C.GC_3671,(0,11):C.GC_3677,(0,20):C.GC_4224,(0,28):C.GC_4226,(0,40):C.GC_4220,(0,48):C.GC_4222,(0,5):C.GC_3700,(0,12):C.GC_3699,(0,21):C.GC_3675,(0,29):C.GC_3676,(0,42):C.GC_3700,(0,50):C.GC_3699,(0,7):C.GC_4220,(0,13):C.GC_1299,(0,25):C.GC_3700,(0,30):C.GC_1302,(0,44):C.GC_4225,(0,45):C.GC_3697,(0,14):C.GC_4222,(0,17):C.GC_1300,(0,33):C.GC_3699,(0,35):C.GC_1301,(0,52):C.GC_4223,(0,53):C.GC_3698,(0,6):C.GC_3702,(0,22):C.GC_3701,(0,43):C.GC_2988,(0,8):C.GC_4224,(0,24):C.GC_4221,(0,26):C.GC_3704,(0,46):C.GC_3701,(0,15):C.GC_4226,(0,32):C.GC_4219,(0,9):C.GC_3697,(0,10):C.GC_3703,(0,27):C.GC_3700,(0,31):C.GC_3702,(0,47):C.GC_3702,(0,51):C.GC_3703,(0,16):C.GC_3698,(0,34):C.GC_3699,(0,36):C.GC_3701,(0,54):C.GC_3704,(0,18):C.GC_2615,(0,37):C.GC_2616,(0,38):C.GC_2988,(0,55):C.GC_2989})

V_309 = Vertex(name = 'V_309',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5655,(0,1):C.GC_5655,(0,2):C.GC_5645,(0,3):C.GC_5645,(0,4):C.GC_5623,(0,5):C.GC_5623,(0,6):C.GC_5642,(0,7):C.GC_5630,(0,8):C.GC_5630})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5822,(0,1):C.GC_5822,(0,2):C.GC_5792,(0,3):C.GC_5792,(0,4):C.GC_5807,(0,5):C.GC_5807,(0,6):C.GC_5828,(0,7):C.GC_5782,(0,8):C.GC_5782})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5651,(0,1):C.GC_5635,(0,2):C.GC_5650,(0,3):C.GC_5625,(0,4):C.GC_5637,(0,5):C.GC_5649,(0,6):C.GC_5635,(0,7):C.GC_5636,(0,8):C.GC_5636})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5794,(0,1):C.GC_5818,(0,2):C.GC_5820,(0,3):C.GC_5819,(0,4):C.GC_5817,(0,5):C.GC_5793,(0,6):C.GC_5818,(0,7):C.GC_5783,(0,8):C.GC_5783})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5653,(0,1):C.GC_5653,(0,2):C.GC_5629,(0,3):C.GC_5629,(0,4):C.GC_5648,(0,5):C.GC_5648,(0,6):C.GC_5643,(0,7):C.GC_5624,(0,8):C.GC_5624})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5829,(0,1):C.GC_5829,(0,2):C.GC_5825,(0,3):C.GC_5825,(0,4):C.GC_5814,(0,5):C.GC_5814,(0,6):C.GC_5785,(0,7):C.GC_5808,(0,8):C.GC_5808})

V_315 = Vertex(name = 'V_315',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS111, L.VVVSS112, L.VVVSS113, L.VVVSS114, L.VVVSS116, L.VVVSS118, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS127, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS141, L.VVVSS143, L.VVVSS144, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS154, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS171, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS191, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS26, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS31, L.VVVSS32, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS40, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS52, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS58, L.VVVSS60, L.VVVSS61, L.VVVSS62, L.VVVSS63, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS91, L.VVVSS93, L.VVVSS94, L.VVVSS96, L.VVVSS97, L.VVVSS99 ],
               couplings = {(0,85):C.GC_4030,(0,84):C.GC_4028,(0,88):C.GC_1163,(0,87):C.GC_3380,(0,75):C.GC_4045,(0,0):C.GC_4009,(0,102):C.GC_1162,(0,86):C.GC_3411,(0,129):C.GC_4022,(0,123):C.GC_3987,(0,14):C.GC_1143,(0,30):C.GC_3342,(0,1):C.GC_3358,(0,45):C.GC_3333,(0,36):C.GC_3360,(0,76):C.GC_3379,(0,59):C.GC_3409,(0,131):C.GC_1165,(0,132):C.GC_3381,(0,3):C.GC_4044,(0,2):C.GC_4040,(0,6):C.GC_1162,(0,7):C.GC_432,(0,4):C.GC_3364,(0,5):C.GC_3379,(0,8):C.GC_429,(0,9):C.GC_429,(0,10):C.GC_432,(0,11):C.GC_432,(0,90):C.GC_4031,(0,89):C.GC_4005,(0,93):C.GC_1163,(0,94):C.GC_2796,(0,91):C.GC_3410,(0,92):C.GC_2799,(0,98):C.GC_1167,(0,99):C.GC_430,(0,95):C.GC_1182,(0,96):C.GC_1169,(0,97):C.GC_3413,(0,101):C.GC_4034,(0,100):C.GC_3983,(0,105):C.GC_1142,(0,106):C.GC_431,(0,107):C.GC_3343,(0,103):C.GC_3359,(0,104):C.GC_3388,(0,110):C.GC_430,(0,111):C.GC_431,(0,108):C.GC_1181,(0,109):C.GC_3388,(0,113):C.GC_3344,(0,112):C.GC_3346,(0,116):C.GC_3380,(0,117):C.GC_3383,(0,114):C.GC_3412,(0,115):C.GC_3385,(0,121):C.GC_3383,(0,122):C.GC_431,(0,118):C.GC_1170,(0,119):C.GC_3416,(0,120):C.GC_3385,(0,20):C.GC_1148,(0,32):C.GC_1149,(0,33):C.GC_429,(0,40):C.GC_4039,(0,56):C.GC_4025,(0,57):C.GC_3364,(0,41):C.GC_6772,(0,63):C.GC_4028,(0,64):C.GC_3380,(0,78):C.GC_4040,(0,79):C.GC_3379,(0,65):C.GC_6775,(0,15):C.GC_3345,(0,21):C.GC_3357,(0,34):C.GC_4004,(0,42):C.GC_4008,(0,58):C.GC_3982,(0,66):C.GC_3986,(0,16):C.GC_3392,(0,22):C.GC_3389,(0,35):C.GC_3348,(0,43):C.GC_3347,(0,60):C.GC_3390,(0,67):C.GC_3391,(0,81):C.GC_4024,(0,83):C.GC_1149,(0,12):C.GC_1146,(0,17):C.GC_3982,(0,24):C.GC_1181,(0,38):C.GC_3390,(0,46):C.GC_1170,(0,61):C.GC_4009,(0,62):C.GC_3411,(0,125):C.GC_4038,(0,128):C.GC_1148,(0,135):C.GC_1144,(0,25):C.GC_3986,(0,29):C.GC_1182,(0,49):C.GC_3391,(0,52):C.GC_1169,(0,70):C.GC_4005,(0,71):C.GC_3410,(0,23):C.GC_3416,(0,44):C.GC_3413,(0,68):C.GC_2802,(0,80):C.GC_4022,(0,18):C.GC_4004,(0,37):C.GC_3987,(0,124):C.GC_4034,(0,130):C.GC_431,(0,26):C.GC_4008,(0,48):C.GC_3983,(0,50):C.GC_3388,(0,72):C.GC_3413,(0,82):C.GC_3366,(0,13):C.GC_3364,(0,19):C.GC_3409,(0,39):C.GC_3392,(0,47):C.GC_3413,(0,69):C.GC_3388,(0,126):C.GC_3365,(0,127):C.GC_3362,(0,136):C.GC_3362,(0,27):C.GC_3412,(0,28):C.GC_3385,(0,51):C.GC_3389,(0,53):C.GC_3416,(0,73):C.GC_3416,(0,74):C.GC_3385,(0,133):C.GC_2244,(0,134):C.GC_2796,(0,31):C.GC_2250,(0,54):C.GC_2247,(0,55):C.GC_2802,(0,77):C.GC_2799})

V_316 = Vertex(name = 'V_316',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS120, L.VVVSS121, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS141, L.VVVSS147, L.VVVSS148, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS182, L.VVVSS183, L.VVVSS188, L.VVVSS189, L.VVVSS190, L.VVVSS191, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS199, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS41, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS70, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4218,(0,53):C.GC_3705,(0,71):C.GC_4230,(0,1):C.GC_3680,(0,19):C.GC_3681,(0,38):C.GC_3705,(0,54):C.GC_4216,(0,55):C.GC_3706,(0,56):C.GC_2987,(0,57):C.GC_1304,(0,58):C.GC_1297,(0,59):C.GC_3708,(0,60):C.GC_4228,(0,61):C.GC_3679,(0,62):C.GC_3693,(0,63):C.GC_1303,(0,64):C.GC_3693,(0,65):C.GC_3667,(0,66):C.GC_3706,(0,67):C.GC_3694,(0,68):C.GC_1298,(0,69):C.GC_3707,(0,70):C.GC_3694,(0,23):C.GC_6827,(0,42):C.GC_6824,(0,2):C.GC_3666,(0,7):C.GC_3678,(0,17):C.GC_4215,(0,24):C.GC_4217,(0,37):C.GC_4227,(0,43):C.GC_4229,(0,3):C.GC_3696,(0,8):C.GC_3695,(0,18):C.GC_3668,(0,25):C.GC_3669,(0,39):C.GC_3696,(0,44):C.GC_3695,(0,4):C.GC_4227,(0,10):C.GC_1303,(0,21):C.GC_3696,(0,27):C.GC_1298,(0,40):C.GC_4218,(0,41):C.GC_3705,(0,11):C.GC_4229,(0,15):C.GC_1304,(0,30):C.GC_3695,(0,33):C.GC_1297,(0,47):C.GC_4216,(0,48):C.GC_3706,(0,9):C.GC_3707,(0,26):C.GC_3708,(0,45):C.GC_2990,(0,5):C.GC_4215,(0,20):C.GC_4230,(0,12):C.GC_4217,(0,29):C.GC_4228,(0,31):C.GC_3693,(0,49):C.GC_3708,(0,6):C.GC_3705,(0,22):C.GC_3696,(0,28):C.GC_3708,(0,46):C.GC_3693,(0,13):C.GC_3706,(0,14):C.GC_3694,(0,32):C.GC_3695,(0,34):C.GC_3707,(0,50):C.GC_3707,(0,51):C.GC_3694,(0,16):C.GC_2617,(0,35):C.GC_2614,(0,36):C.GC_2990,(0,52):C.GC_2987})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS3, L.VVSSS4, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5640,(0,1):C.GC_5640,(0,2):C.GC_5638,(0,3):C.GC_5638,(0,4):C.GC_5632,(0,5):C.GC_5632,(0,6):C.GC_5633})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS3, L.VVSSS4, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_5810,(0,1):C.GC_5810,(0,2):C.GC_5815,(0,3):C.GC_5815,(0,4):C.GC_5826,(0,5):C.GC_5826,(0,6):C.GC_5827})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS118, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS13, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS46, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS60, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS93, L.VVVSS94, L.VVVSS95, L.VVVSS96, L.VVVSS97, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,104):C.GC_3457,(0,103):C.GC_3457,(0,108):C.GC_1110,(0,109):C.GC_1113,(0,106):C.GC_1114,(0,107):C.GC_1112,(0,90):C.GC_3457,(0,0):C.GC_3465,(0,125):C.GC_1113,(0,141):C.GC_73,(0,105):C.GC_1084,(0,115):C.GC_79,(0,154):C.GC_3456,(0,148):C.GC_3462,(0,24):C.GC_1110,(0,34):C.GC_74,(0,1):C.GC_80,(0,8):C.GC_1086,(0,91):C.GC_1115,(0,96):C.GC_1131,(0,68):C.GC_1089,(0,79):C.GC_1083,(0,156):C.GC_2236,(0,157):C.GC_2236,(0,158):C.GC_89,(0,3):C.GC_3457,(0,2):C.GC_3457,(0,6):C.GC_1110,(0,7):C.GC_1113,(0,4):C.GC_1114,(0,5):C.GC_1112,(0,9):C.GC_2237,(0,10):C.GC_2237,(0,11):C.GC_2236,(0,12):C.GC_2237,(0,111):C.GC_3457,(0,110):C.GC_3465,(0,114):C.GC_1113,(0,116):C.GC_73,(0,112):C.GC_1084,(0,113):C.GC_79,(0,121):C.GC_2236,(0,122):C.GC_2237,(0,117):C.GC_2229,(0,118):C.GC_2228,(0,119):C.GC_2228,(0,120):C.GC_1073,(0,124):C.GC_3456,(0,123):C.GC_3462,(0,128):C.GC_1110,(0,129):C.GC_74,(0,126):C.GC_80,(0,127):C.GC_1086,(0,134):C.GC_2236,(0,135):C.GC_2237,(0,130):C.GC_2229,(0,131):C.GC_2228,(0,132):C.GC_2229,(0,133):C.GC_1068,(0,138):C.GC_1115,(0,139):C.GC_1131,(0,136):C.GC_1089,(0,137):C.GC_1083,(0,145):C.GC_89,(0,146):C.GC_2236,(0,147):C.GC_2237,(0,140):C.GC_2228,(0,142):C.GC_1073,(0,143):C.GC_2229,(0,144):C.GC_1068,(0,22):C.GC_1130,(0,23):C.GC_1128,(0,38):C.GC_1130,(0,39):C.GC_1128,(0,48):C.GC_3456,(0,49):C.GC_1114,(0,40):C.GC_6863,(0,64):C.GC_3456,(0,65):C.GC_1114,(0,50):C.GC_6863,(0,75):C.GC_3457,(0,76):C.GC_1112,(0,66):C.GC_6864,(0,94):C.GC_3457,(0,95):C.GC_1112,(0,77):C.GC_6864,(0,41):C.GC_3465,(0,51):C.GC_3465,(0,67):C.GC_3462,(0,78):C.GC_3462,(0,16):C.GC_1082,(0,25):C.GC_1082,(0,42):C.GC_79,(0,52):C.GC_79,(0,69):C.GC_1087,(0,80):C.GC_1087,(0,98):C.GC_3456,(0,101):C.GC_1128,(0,13):C.GC_2237,(0,18):C.GC_3462,(0,27):C.GC_2229,(0,45):C.GC_1087,(0,54):C.GC_2228,(0,71):C.GC_3465,(0,72):C.GC_1084,(0,150):C.GC_3456,(0,153):C.GC_1128,(0,162):C.GC_2237,(0,29):C.GC_3462,(0,33):C.GC_2229,(0,57):C.GC_1087,(0,60):C.GC_2228,(0,84):C.GC_3465,(0,85):C.GC_1084,(0,17):C.GC_1088,(0,26):C.GC_1088,(0,43):C.GC_1085,(0,53):C.GC_1085,(0,70):C.GC_80,(0,81):C.GC_80,(0,97):C.GC_3456,(0,102):C.GC_1110,(0,14):C.GC_2236,(0,19):C.GC_3465,(0,28):C.GC_2228,(0,44):C.GC_3462,(0,46):C.GC_1086,(0,73):C.GC_1085,(0,82):C.GC_2229,(0,149):C.GC_3456,(0,155):C.GC_1110,(0,163):C.GC_2236,(0,30):C.GC_3465,(0,35):C.GC_2228,(0,56):C.GC_3462,(0,58):C.GC_1086,(0,86):C.GC_1085,(0,88):C.GC_2229,(0,99):C.GC_1129,(0,100):C.GC_1111,(0,15):C.GC_88,(0,20):C.GC_1089,(0,21):C.GC_1083,(0,47):C.GC_1082,(0,55):C.GC_1073,(0,74):C.GC_1088,(0,83):C.GC_1068,(0,151):C.GC_1129,(0,152):C.GC_1111,(0,164):C.GC_88,(0,31):C.GC_1089,(0,32):C.GC_1083,(0,59):C.GC_1082,(0,61):C.GC_1073,(0,87):C.GC_1088,(0,89):C.GC_1068,(0,159):C.GC_2227,(0,160):C.GC_2227,(0,161):C.GC_1066,(0,36):C.GC_2233,(0,37):C.GC_2232,(0,62):C.GC_2232,(0,63):C.GC_1077,(0,92):C.GC_2233,(0,93):C.GC_1074})

V_320 = Vertex(name = 'V_320',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_3721,(0,67):C.GC_1319,(0,71):C.GC_507,(0,89):C.GC_3722,(0,1):C.GC_508,(0,2):C.GC_1316,(0,45):C.GC_1317,(0,54):C.GC_1318,(0,68):C.GC_3721,(0,69):C.GC_1319,(0,70):C.GC_507,(0,72):C.GC_1327,(0,73):C.GC_1322,(0,74):C.GC_1322,(0,75):C.GC_1329,(0,76):C.GC_3722,(0,77):C.GC_508,(0,78):C.GC_1316,(0,79):C.GC_1327,(0,80):C.GC_1322,(0,81):C.GC_1327,(0,82):C.GC_1323,(0,83):C.GC_1317,(0,84):C.GC_1318,(0,85):C.GC_1322,(0,86):C.GC_1329,(0,87):C.GC_1327,(0,88):C.GC_1323,(0,21):C.GC_6902,(0,29):C.GC_6902,(0,43):C.GC_6901,(0,52):C.GC_6901,(0,22):C.GC_3721,(0,30):C.GC_3721,(0,44):C.GC_3722,(0,53):C.GC_3722,(0,3):C.GC_1318,(0,9):C.GC_1318,(0,23):C.GC_507,(0,31):C.GC_507,(0,46):C.GC_1316,(0,55):C.GC_1316,(0,5):C.GC_3722,(0,11):C.GC_1327,(0,26):C.GC_1316,(0,33):C.GC_1322,(0,48):C.GC_3721,(0,49):C.GC_1319,(0,13):C.GC_3722,(0,17):C.GC_1327,(0,36):C.GC_1316,(0,39):C.GC_1322,(0,59):C.GC_3721,(0,60):C.GC_1319,(0,4):C.GC_1317,(0,10):C.GC_1317,(0,24):C.GC_1319,(0,32):C.GC_1319,(0,47):C.GC_508,(0,56):C.GC_508,(0,6):C.GC_3721,(0,12):C.GC_1322,(0,25):C.GC_3722,(0,27):C.GC_1316,(0,50):C.GC_1319,(0,57):C.GC_1327,(0,14):C.GC_3721,(0,18):C.GC_1322,(0,35):C.GC_3722,(0,37):C.GC_1316,(0,61):C.GC_1319,(0,63):C.GC_1327,(0,7):C.GC_1317,(0,8):C.GC_1318,(0,28):C.GC_1318,(0,34):C.GC_1329,(0,51):C.GC_1317,(0,58):C.GC_1323,(0,15):C.GC_1317,(0,16):C.GC_1318,(0,38):C.GC_1318,(0,40):C.GC_1329,(0,62):C.GC_1317,(0,64):C.GC_1323,(0,19):C.GC_2562,(0,20):C.GC_2561,(0,41):C.GC_2561,(0,42):C.GC_1287,(0,65):C.GC_2562,(0,66):C.GC_1284})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS140, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS46, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS60, L.VVVSS62, L.VVVSS63, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS93, L.VVVSS97, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,105):C.GC_3471,(0,104):C.GC_3471,(0,109):C.GC_1119,(0,110):C.GC_1125,(0,107):C.GC_1126,(0,108):C.GC_1120,(0,93):C.GC_3470,(0,0):C.GC_3454,(0,126):C.GC_1116,(0,145):C.GC_72,(0,106):C.GC_1102,(0,116):C.GC_78,(0,158):C.GC_3471,(0,152):C.GC_3454,(0,27):C.GC_1122,(0,38):C.GC_72,(0,1):C.GC_78,(0,8):C.GC_1103,(0,57):C.GC_3453,(0,66):C.GC_3450,(0,46):C.GC_3458,(0,94):C.GC_1117,(0,97):C.GC_1121,(0,71):C.GC_1079,(0,82):C.GC_1078,(0,160):C.GC_2230,(0,161):C.GC_2230,(0,162):C.GC_87,(0,3):C.GC_3470,(0,2):C.GC_3470,(0,6):C.GC_1122,(0,7):C.GC_1116,(0,4):C.GC_1118,(0,5):C.GC_1124,(0,9):C.GC_2231,(0,10):C.GC_2231,(0,11):C.GC_2230,(0,12):C.GC_2231,(0,112):C.GC_3471,(0,111):C.GC_3455,(0,115):C.GC_1125,(0,117):C.GC_77,(0,113):C.GC_1081,(0,114):C.GC_83,(0,122):C.GC_2231,(0,123):C.GC_2230,(0,118):C.GC_2235,(0,119):C.GC_2234,(0,120):C.GC_2234,(0,121):C.GC_85,(0,125):C.GC_3470,(0,124):C.GC_3455,(0,129):C.GC_1119,(0,130):C.GC_77,(0,127):C.GC_83,(0,128):C.GC_1080,(0,135):C.GC_2231,(0,136):C.GC_2230,(0,131):C.GC_2234,(0,132):C.GC_2235,(0,133):C.GC_2234,(0,134):C.GC_84,(0,138):C.GC_3450,(0,139):C.GC_3453,(0,137):C.GC_3461,(0,142):C.GC_1127,(0,143):C.GC_1123,(0,140):C.GC_1104,(0,141):C.GC_1105,(0,149):C.GC_86,(0,150):C.GC_2231,(0,151):C.GC_2230,(0,144):C.GC_2235,(0,146):C.GC_84,(0,147):C.GC_2235,(0,148):C.GC_85,(0,24):C.GC_1122,(0,25):C.GC_1116,(0,16):C.GC_6872,(0,40):C.GC_1119,(0,41):C.GC_1125,(0,26):C.GC_6879,(0,51):C.GC_3470,(0,52):C.GC_1126,(0,42):C.GC_6862,(0,67):C.GC_3471,(0,68):C.GC_1118,(0,53):C.GC_6871,(0,78):C.GC_3471,(0,79):C.GC_1120,(0,69):C.GC_6862,(0,95):C.GC_3470,(0,96):C.GC_1124,(0,80):C.GC_6871,(0,17):C.GC_3461,(0,28):C.GC_3458,(0,43):C.GC_3455,(0,54):C.GC_3454,(0,70):C.GC_3455,(0,81):C.GC_3454,(0,18):C.GC_1104,(0,29):C.GC_1079,(0,44):C.GC_83,(0,55):C.GC_78,(0,72):C.GC_1081,(0,83):C.GC_1102,(0,99):C.GC_3471,(0,102):C.GC_1125,(0,13):C.GC_2231,(0,20):C.GC_3455,(0,31):C.GC_2234,(0,48):C.GC_1081,(0,58):C.GC_2235,(0,74):C.GC_3454,(0,75):C.GC_1102,(0,154):C.GC_3470,(0,157):C.GC_1116,(0,163):C.GC_2230,(0,33):C.GC_3454,(0,37):C.GC_2235,(0,61):C.GC_1102,(0,64):C.GC_2234,(0,87):C.GC_3455,(0,88):C.GC_1081,(0,19):C.GC_1105,(0,30):C.GC_1078,(0,45):C.GC_1080,(0,56):C.GC_1103,(0,73):C.GC_83,(0,84):C.GC_78,(0,98):C.GC_3471,(0,103):C.GC_1122,(0,14):C.GC_2230,(0,21):C.GC_3455,(0,32):C.GC_2234,(0,47):C.GC_3454,(0,49):C.GC_1103,(0,76):C.GC_1080,(0,85):C.GC_2235,(0,153):C.GC_3470,(0,159):C.GC_1119,(0,164):C.GC_2231,(0,34):C.GC_3454,(0,39):C.GC_2235,(0,60):C.GC_3455,(0,62):C.GC_1080,(0,89):C.GC_1103,(0,91):C.GC_2234,(0,100):C.GC_1127,(0,101):C.GC_1123,(0,15):C.GC_86,(0,22):C.GC_1079,(0,23):C.GC_1078,(0,50):C.GC_1104,(0,59):C.GC_85,(0,77):C.GC_1105,(0,86):C.GC_84,(0,155):C.GC_1117,(0,156):C.GC_1121,(0,165):C.GC_87,(0,35):C.GC_1104,(0,36):C.GC_1105,(0,63):C.GC_1079,(0,65):C.GC_84,(0,90):C.GC_1078,(0,92):C.GC_85})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS71, L.VVVSS8 ],
               couplings = {(0,0):C.GC_3720,(0,62):C.GC_1314,(0,66):C.GC_506,(0,81):C.GC_3720,(0,1):C.GC_506,(0,2):C.GC_1314,(0,27):C.GC_3629,(0,44):C.GC_1332,(0,53):C.GC_1332,(0,63):C.GC_3725,(0,64):C.GC_1333,(0,65):C.GC_511,(0,67):C.GC_2662,(0,68):C.GC_2663,(0,69):C.GC_2663,(0,70):C.GC_3725,(0,71):C.GC_511,(0,72):C.GC_1333,(0,73):C.GC_2663,(0,74):C.GC_2662,(0,75):C.GC_2663,(0,76):C.GC_3632,(0,77):C.GC_1315,(0,78):C.GC_1315,(0,79):C.GC_2662,(0,80):C.GC_2662,(0,3):C.GC_6898,(0,11):C.GC_6899,(0,23):C.GC_6900,(0,32):C.GC_6915,(0,42):C.GC_6900,(0,51):C.GC_6915,(0,4):C.GC_3632,(0,12):C.GC_3629,(0,24):C.GC_3725,(0,33):C.GC_3720,(0,43):C.GC_3725,(0,52):C.GC_3720,(0,5):C.GC_1315,(0,13):C.GC_1332,(0,25):C.GC_511,(0,34):C.GC_506,(0,45):C.GC_1333,(0,54):C.GC_1314,(0,7):C.GC_3725,(0,15):C.GC_2663,(0,29):C.GC_1333,(0,36):C.GC_2662,(0,47):C.GC_3720,(0,48):C.GC_1314,(0,17):C.GC_3720,(0,21):C.GC_2662,(0,38):C.GC_1314,(0,41):C.GC_2663,(0,57):C.GC_3725,(0,58):C.GC_1333,(0,6):C.GC_1315,(0,14):C.GC_1332,(0,26):C.GC_1333,(0,35):C.GC_1314,(0,46):C.GC_511,(0,55):C.GC_506,(0,8):C.GC_3725,(0,16):C.GC_2663,(0,28):C.GC_3720,(0,30):C.GC_1314,(0,49):C.GC_1333,(0,56):C.GC_2662,(0,18):C.GC_3720,(0,22):C.GC_2662,(0,37):C.GC_3725,(0,39):C.GC_1333,(0,59):C.GC_1314,(0,61):C.GC_2663,(0,9):C.GC_1332,(0,10):C.GC_1332,(0,31):C.GC_1315,(0,50):C.GC_1315,(0,19):C.GC_1315,(0,20):C.GC_1315,(0,40):C.GC_1332,(0,60):C.GC_1332})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS104, L.VVVSS105, L.VVVSS107, L.VVVSS108, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS126, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS143, L.VVVSS146, L.VVVSS147, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS152, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS16, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS17, L.VVVSS170, L.VVVSS178, L.VVVSS179, L.VVVSS181, L.VVVSS182, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS25, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS30, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS38, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS46, L.VVVSS48, L.VVVSS49, L.VVVSS50, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS60, L.VVVSS62, L.VVVSS63, L.VVVSS64, L.VVVSS65, L.VVVSS67, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS89, L.VVVSS9, L.VVVSS91, L.VVVSS92, L.VVVSS93, L.VVVSS94, L.VVVSS95, L.VVVSS96, L.VVVSS97, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,85):C.GC_3468,(0,84):C.GC_3468,(0,87):C.GC_1135,(0,86):C.GC_1137,(0,74):C.GC_3472,(0,0):C.GC_3464,(0,115):C.GC_76,(0,92):C.GC_82,(0,127):C.GC_3469,(0,122):C.GC_3467,(0,21):C.GC_1132,(0,5):C.GC_1098,(0,45):C.GC_3451,(0,55):C.GC_3452,(0,37):C.GC_3460,(0,79):C.GC_1109,(0,66):C.GC_1093,(0,128):C.GC_1132,(0,129):C.GC_1132,(0,130):C.GC_401,(0,2):C.GC_3472,(0,1):C.GC_3472,(0,4):C.GC_1132,(0,3):C.GC_1133,(0,6):C.GC_1108,(0,7):C.GC_1108,(0,8):C.GC_1132,(0,9):C.GC_1108,(0,89):C.GC_3468,(0,88):C.GC_3463,(0,91):C.GC_1135,(0,90):C.GC_1090,(0,97):C.GC_1135,(0,98):C.GC_1106,(0,93):C.GC_1101,(0,94):C.GC_1094,(0,95):C.GC_1094,(0,96):C.GC_1071,(0,100):C.GC_3473,(0,99):C.GC_3466,(0,102):C.GC_75,(0,101):C.GC_81,(0,107):C.GC_1135,(0,108):C.GC_1106,(0,103):C.GC_1095,(0,104):C.GC_1100,(0,105):C.GC_1095,(0,106):C.GC_1070,(0,110):C.GC_3452,(0,111):C.GC_3451,(0,109):C.GC_3459,(0,113):C.GC_1136,(0,112):C.GC_1097,(0,119):C.GC_402,(0,120):C.GC_1135,(0,121):C.GC_1106,(0,114):C.GC_1100,(0,116):C.GC_1072,(0,117):C.GC_1101,(0,118):C.GC_1069,(0,19):C.GC_1106,(0,13):C.GC_6874,(0,33):C.GC_1108,(0,20):C.GC_6873,(0,40):C.GC_3473,(0,41):C.GC_1137,(0,34):C.GC_6877,(0,56):C.GC_3469,(0,42):C.GC_6867,(0,63):C.GC_3468,(0,57):C.GC_6869,(0,77):C.GC_3472,(0,78):C.GC_1133,(0,64):C.GC_6875,(0,14):C.GC_3459,(0,22):C.GC_3460,(0,35):C.GC_3463,(0,43):C.GC_3464,(0,58):C.GC_3466,(0,65):C.GC_3467,(0,23):C.GC_1092,(0,44):C.GC_82,(0,67):C.GC_1099,(0,81):C.GC_3469,(0,10):C.GC_1108,(0,16):C.GC_3466,(0,24):C.GC_1095,(0,46):C.GC_1100,(0,60):C.GC_3464,(0,124):C.GC_3473,(0,126):C.GC_1106,(0,134):C.GC_1106,(0,26):C.GC_3467,(0,29):C.GC_1101,(0,49):C.GC_1099,(0,51):C.GC_1094,(0,70):C.GC_3463,(0,71):C.GC_1090,(0,15):C.GC_1096,(0,36):C.GC_1091,(0,59):C.GC_81,(0,80):C.GC_3469,(0,83):C.GC_1132,(0,11):C.GC_1132,(0,17):C.GC_3463,(0,25):C.GC_1094,(0,38):C.GC_3467,(0,39):C.GC_1098,(0,61):C.GC_1091,(0,68):C.GC_1101,(0,123):C.GC_3473,(0,135):C.GC_1135,(0,27):C.GC_3464,(0,30):C.GC_1100,(0,48):C.GC_3466,(0,72):C.GC_1095,(0,82):C.GC_1134,(0,12):C.GC_404,(0,18):C.GC_1093,(0,47):C.GC_1071,(0,62):C.GC_1096,(0,69):C.GC_1070,(0,125):C.GC_1107,(0,136):C.GC_403,(0,28):C.GC_1097,(0,50):C.GC_1092,(0,52):C.GC_1072,(0,73):C.GC_1069,(0,131):C.GC_2227,(0,132):C.GC_2227,(0,133):C.GC_1067,(0,31):C.GC_2233,(0,32):C.GC_2232,(0,53):C.GC_2232,(0,54):C.GC_1076,(0,75):C.GC_2233,(0,76):C.GC_1075})

V_324 = Vertex(name = 'V_324',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS152, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS181, L.VVVSS182, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS34, L.VVVSS36, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS69, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_3724,(0,58):C.GC_510,(0,75):C.GC_3642,(0,1):C.GC_1321,(0,23):C.GC_3631,(0,46):C.GC_1326,(0,56):C.GC_3643,(0,57):C.GC_1325,(0,59):C.GC_2586,(0,60):C.GC_2587,(0,61):C.GC_2587,(0,62):C.GC_1328,(0,63):C.GC_3723,(0,64):C.GC_509,(0,65):C.GC_1331,(0,66):C.GC_1330,(0,67):C.GC_1331,(0,68):C.GC_1324,(0,69):C.GC_3630,(0,70):C.GC_1320,(0,71):C.GC_1330,(0,72):C.GC_1328,(0,73):C.GC_2586,(0,74):C.GC_1324,(0,2):C.GC_6908,(0,8):C.GC_6904,(0,20):C.GC_6909,(0,26):C.GC_6903,(0,38):C.GC_6907,(0,44):C.GC_6905,(0,3):C.GC_3630,(0,9):C.GC_3631,(0,21):C.GC_3643,(0,27):C.GC_3724,(0,39):C.GC_3723,(0,45):C.GC_3642,(0,10):C.GC_1326,(0,28):C.GC_510,(0,47):C.GC_1321,(0,5):C.GC_3723,(0,11):C.GC_1331,(0,29):C.GC_1330,(0,41):C.GC_3724,(0,13):C.GC_3642,(0,16):C.GC_2586,(0,32):C.GC_1321,(0,34):C.GC_2587,(0,50):C.GC_3643,(0,51):C.GC_1325,(0,4):C.GC_1320,(0,22):C.GC_1325,(0,40):C.GC_509,(0,6):C.GC_3643,(0,12):C.GC_2587,(0,24):C.GC_3642,(0,25):C.GC_1321,(0,42):C.GC_1325,(0,48):C.GC_2586,(0,14):C.GC_3724,(0,17):C.GC_1330,(0,31):C.GC_3723,(0,52):C.GC_1331,(0,7):C.GC_1326,(0,30):C.GC_1328,(0,43):C.GC_1320,(0,49):C.GC_1324,(0,15):C.GC_1320,(0,33):C.GC_1326,(0,35):C.GC_1328,(0,53):C.GC_1324,(0,18):C.GC_2562,(0,19):C.GC_2561,(0,36):C.GC_2561,(0,37):C.GC_1286,(0,54):C.GC_2562,(0,55):C.GC_1285})

V_325 = Vertex(name = 'V_325',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS112, L.VVVSS114, L.VVVSS115, L.VVVSS116, L.VVVSS117, L.VVVSS118, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS13, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS14, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS4, L.VVVSS40, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS45, L.VVVSS46, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS60, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS69, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS74, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS91, L.VVVSS92, L.VVVSS93, L.VVVSS94, L.VVVSS95, L.VVVSS96, L.VVVSS97, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,104):C.GC_3457,(0,103):C.GC_3457,(0,108):C.GC_1110,(0,109):C.GC_1113,(0,106):C.GC_1114,(0,107):C.GC_1112,(0,90):C.GC_3457,(0,0):C.GC_3465,(0,125):C.GC_1113,(0,141):C.GC_73,(0,105):C.GC_1084,(0,115):C.GC_79,(0,154):C.GC_3456,(0,148):C.GC_3462,(0,24):C.GC_1110,(0,34):C.GC_74,(0,1):C.GC_80,(0,8):C.GC_1086,(0,91):C.GC_1115,(0,96):C.GC_1131,(0,68):C.GC_1089,(0,79):C.GC_1083,(0,156):C.GC_2236,(0,157):C.GC_2236,(0,158):C.GC_89,(0,3):C.GC_3457,(0,2):C.GC_3457,(0,6):C.GC_1110,(0,7):C.GC_1113,(0,4):C.GC_1114,(0,5):C.GC_1112,(0,9):C.GC_2237,(0,10):C.GC_2237,(0,11):C.GC_2236,(0,12):C.GC_2237,(0,111):C.GC_3457,(0,110):C.GC_3465,(0,114):C.GC_1113,(0,116):C.GC_73,(0,112):C.GC_1084,(0,113):C.GC_79,(0,121):C.GC_2236,(0,122):C.GC_2237,(0,117):C.GC_2229,(0,118):C.GC_2228,(0,119):C.GC_2228,(0,120):C.GC_1073,(0,124):C.GC_3456,(0,123):C.GC_3462,(0,128):C.GC_1110,(0,129):C.GC_74,(0,126):C.GC_80,(0,127):C.GC_1086,(0,134):C.GC_2236,(0,135):C.GC_2237,(0,130):C.GC_2229,(0,131):C.GC_2228,(0,132):C.GC_2229,(0,133):C.GC_1068,(0,138):C.GC_1115,(0,139):C.GC_1131,(0,136):C.GC_1089,(0,137):C.GC_1083,(0,145):C.GC_89,(0,146):C.GC_2236,(0,147):C.GC_2237,(0,140):C.GC_2228,(0,142):C.GC_1073,(0,143):C.GC_2229,(0,144):C.GC_1068,(0,22):C.GC_1130,(0,23):C.GC_1128,(0,38):C.GC_1130,(0,39):C.GC_1128,(0,48):C.GC_3456,(0,49):C.GC_1114,(0,40):C.GC_6865,(0,64):C.GC_3456,(0,65):C.GC_1114,(0,50):C.GC_6865,(0,75):C.GC_3457,(0,76):C.GC_1112,(0,66):C.GC_6866,(0,94):C.GC_3457,(0,95):C.GC_1112,(0,77):C.GC_6866,(0,41):C.GC_3465,(0,51):C.GC_3465,(0,67):C.GC_3462,(0,78):C.GC_3462,(0,16):C.GC_1082,(0,25):C.GC_1082,(0,42):C.GC_79,(0,52):C.GC_79,(0,69):C.GC_1087,(0,80):C.GC_1087,(0,98):C.GC_3456,(0,101):C.GC_1128,(0,13):C.GC_2237,(0,18):C.GC_3462,(0,27):C.GC_2229,(0,45):C.GC_1087,(0,54):C.GC_2228,(0,71):C.GC_3465,(0,72):C.GC_1084,(0,150):C.GC_3456,(0,153):C.GC_1128,(0,162):C.GC_2237,(0,29):C.GC_3462,(0,33):C.GC_2229,(0,57):C.GC_1087,(0,60):C.GC_2228,(0,84):C.GC_3465,(0,85):C.GC_1084,(0,17):C.GC_1088,(0,26):C.GC_1088,(0,43):C.GC_1085,(0,53):C.GC_1085,(0,70):C.GC_80,(0,81):C.GC_80,(0,97):C.GC_3456,(0,102):C.GC_1110,(0,14):C.GC_2236,(0,19):C.GC_3465,(0,28):C.GC_2228,(0,44):C.GC_3462,(0,46):C.GC_1086,(0,73):C.GC_1085,(0,82):C.GC_2229,(0,149):C.GC_3456,(0,155):C.GC_1110,(0,163):C.GC_2236,(0,30):C.GC_3465,(0,35):C.GC_2228,(0,56):C.GC_3462,(0,58):C.GC_1086,(0,86):C.GC_1085,(0,88):C.GC_2229,(0,99):C.GC_1129,(0,100):C.GC_1111,(0,15):C.GC_88,(0,20):C.GC_1089,(0,21):C.GC_1083,(0,47):C.GC_1082,(0,55):C.GC_1073,(0,74):C.GC_1088,(0,83):C.GC_1068,(0,151):C.GC_1129,(0,152):C.GC_1111,(0,164):C.GC_88,(0,31):C.GC_1089,(0,32):C.GC_1083,(0,59):C.GC_1082,(0,61):C.GC_1073,(0,87):C.GC_1088,(0,89):C.GC_1068,(0,159):C.GC_2227,(0,160):C.GC_2227,(0,161):C.GC_1066,(0,36):C.GC_2233,(0,37):C.GC_2232,(0,62):C.GC_2232,(0,63):C.GC_1077,(0,92):C.GC_2233,(0,93):C.GC_1074})

V_326 = Vertex(name = 'V_326',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS131, L.VVVSS132, L.VVVSS133, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS139, L.VVVSS140, L.VVVSS141, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS160, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS166, L.VVVSS167, L.VVVSS168, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS41, L.VVVSS42, L.VVVSS43, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS55, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS65, L.VVVSS66, L.VVVSS69, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_3721,(0,67):C.GC_1319,(0,71):C.GC_507,(0,89):C.GC_3722,(0,1):C.GC_508,(0,2):C.GC_1316,(0,45):C.GC_1317,(0,54):C.GC_1318,(0,68):C.GC_3721,(0,69):C.GC_1319,(0,70):C.GC_507,(0,72):C.GC_1327,(0,73):C.GC_1322,(0,74):C.GC_1322,(0,75):C.GC_1329,(0,76):C.GC_3722,(0,77):C.GC_508,(0,78):C.GC_1316,(0,79):C.GC_1327,(0,80):C.GC_1322,(0,81):C.GC_1327,(0,82):C.GC_1323,(0,83):C.GC_1317,(0,84):C.GC_1318,(0,85):C.GC_1322,(0,86):C.GC_1329,(0,87):C.GC_1327,(0,88):C.GC_1323,(0,21):C.GC_6912,(0,29):C.GC_6912,(0,43):C.GC_6911,(0,52):C.GC_6911,(0,22):C.GC_3721,(0,30):C.GC_3721,(0,44):C.GC_3722,(0,53):C.GC_3722,(0,3):C.GC_1318,(0,9):C.GC_1318,(0,23):C.GC_507,(0,31):C.GC_507,(0,46):C.GC_1316,(0,55):C.GC_1316,(0,5):C.GC_3722,(0,11):C.GC_1327,(0,26):C.GC_1316,(0,33):C.GC_1322,(0,48):C.GC_3721,(0,49):C.GC_1319,(0,13):C.GC_3722,(0,17):C.GC_1327,(0,36):C.GC_1316,(0,39):C.GC_1322,(0,59):C.GC_3721,(0,60):C.GC_1319,(0,4):C.GC_1317,(0,10):C.GC_1317,(0,24):C.GC_1319,(0,32):C.GC_1319,(0,47):C.GC_508,(0,56):C.GC_508,(0,6):C.GC_3721,(0,12):C.GC_1322,(0,25):C.GC_3722,(0,27):C.GC_1316,(0,50):C.GC_1319,(0,57):C.GC_1327,(0,14):C.GC_3721,(0,18):C.GC_1322,(0,35):C.GC_3722,(0,37):C.GC_1316,(0,61):C.GC_1319,(0,63):C.GC_1327,(0,7):C.GC_1317,(0,8):C.GC_1318,(0,28):C.GC_1318,(0,34):C.GC_1329,(0,51):C.GC_1317,(0,58):C.GC_1323,(0,15):C.GC_1317,(0,16):C.GC_1318,(0,38):C.GC_1318,(0,40):C.GC_1329,(0,62):C.GC_1317,(0,64):C.GC_1323,(0,19):C.GC_2562,(0,20):C.GC_2561,(0,41):C.GC_2561,(0,42):C.GC_1287,(0,65):C.GC_2562,(0,66):C.GC_1284})

V_327 = Vertex(name = 'V_327',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS106, L.VVVVS108, L.VVVVS109, L.VVVVS11, L.VVVVS114, L.VVVVS115, L.VVVVS116, L.VVVVS117, L.VVVVS118, L.VVVVS12, L.VVVVS122, L.VVVVS124, L.VVVVS125, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS131, L.VVVVS132, L.VVVVS133, L.VVVVS134, L.VVVVS14, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS146, L.VVVVS149, L.VVVVS152, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS159, L.VVVVS16, L.VVVVS161, L.VVVVS162, L.VVVVS164, L.VVVVS166, L.VVVVS167, L.VVVVS170, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS181, L.VVVVS182, L.VVVVS183, L.VVVVS184, L.VVVVS185, L.VVVVS189, L.VVVVS191, L.VVVVS192, L.VVVVS193, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS198, L.VVVVS199, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS204, L.VVVVS205, L.VVVVS208, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS23, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS239, L.VVVVS24, L.VVVVS241, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS25, L.VVVVS250, L.VVVVS251, L.VVVVS254, L.VVVVS255, L.VVVVS256, L.VVVVS258, L.VVVVS259, L.VVVVS26, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS27, L.VVVVS28, L.VVVVS29, L.VVVVS30, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS37, L.VVVVS38, L.VVVVS49, L.VVVVS5, L.VVVVS51, L.VVVVS52, L.VVVVS53, L.VVVVS55, L.VVVVS56, L.VVVVS57, L.VVVVS58, L.VVVVS6, L.VVVVS61, L.VVVVS62, L.VVVVS67, L.VVVVS68, L.VVVVS69, L.VVVVS7, L.VVVVS70, L.VVVVS73, L.VVVVS77, L.VVVVS78, L.VVVVS79, L.VVVVS8, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS84, L.VVVVS85, L.VVVVS86, L.VVVVS9, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS93, L.VVVVS96, L.VVVVS99 ],
               couplings = {(0,138):C.GC_5602,(0,0):C.GC_5610,(0,8):C.GC_5602,(0,14):C.GC_5601,(0,110):C.GC_5602,(0,118):C.GC_5602,(0,124):C.GC_5610,(0,130):C.GC_5601,(0,73):C.GC_4796,(0,78):C.GC_4796,(0,26):C.GC_5944,(0,38):C.GC_5944,(0,109):C.GC_5615,(0,111):C.GC_5616,(0,113):C.GC_5615,(0,114):C.GC_5604,(0,116):C.GC_5603,(0,117):C.GC_5603,(0,119):C.GC_5942,(0,120):C.GC_5942,(0,85):C.GC_5620,(0,93):C.GC_5614,(0,99):C.GC_5613,(0,100):C.GC_5937,(0,101):C.GC_5614,(0,102):C.GC_5620,(0,103):C.GC_5613,(0,104):C.GC_5937,(0,105):C.GC_5618,(0,106):C.GC_5620,(0,107):C.GC_5611,(0,108):C.GC_5607,(0,123):C.GC_5609,(0,125):C.GC_5609,(0,121):C.GC_5456,(0,122):C.GC_5456,(0,127):C.GC_5002,(0,126):C.GC_5004,(0,135):C.GC_5603,(0,136):C.GC_5603,(0,137):C.GC_5621,(0,128):C.GC_5587,(0,129):C.GC_5587,(0,131):C.GC_5599,(0,132):C.GC_5595,(0,133):C.GC_5595,(0,134):C.GC_5946,(0,142):C.GC_5602,(0,139):C.GC_5455,(0,140):C.GC_5458,(0,141):C.GC_5457,(0,144):C.GC_4796,(0,143):C.GC_5006,(0,6):C.GC_5603,(0,7):C.GC_5615,(0,1):C.GC_5597,(0,2):C.GC_5596,(0,3):C.GC_5593,(0,4):C.GC_5591,(0,5):C.GC_5954,(0,11):C.GC_5601,(0,12):C.GC_4503,(0,13):C.GC_4504,(0,9):C.GC_5458,(0,10):C.GC_4506,(0,16):C.GC_5939,(0,15):C.GC_5006,(0,22):C.GC_5604,(0,23):C.GC_5941,(0,24):C.GC_5460,(0,25):C.GC_5615,(0,17):C.GC_5592,(0,18):C.GC_5585,(0,19):C.GC_5951,(0,20):C.GC_5600,(0,21):C.GC_5591,(0,30):C.GC_5602,(0,27):C.GC_5458,(0,28):C.GC_5455,(0,29):C.GC_5457,(0,32):C.GC_4796,(0,31):C.GC_5006,(0,39):C.GC_5603,(0,40):C.GC_5615,(0,33):C.GC_5596,(0,34):C.GC_5597,(0,35):C.GC_5593,(0,36):C.GC_5591,(0,37):C.GC_5954,(0,41):C.GC_7129,(0,51):C.GC_4503,(0,52):C.GC_5601,(0,53):C.GC_4504,(0,49):C.GC_4506,(0,50):C.GC_5458,(0,55):C.GC_5939,(0,54):C.GC_5006,(0,61):C.GC_5604,(0,62):C.GC_5941,(0,63):C.GC_5460,(0,64):C.GC_5615,(0,56):C.GC_5585,(0,57):C.GC_5592,(0,58):C.GC_5951,(0,59):C.GC_5600,(0,60):C.GC_5591,(0,65):C.GC_7129,(0,76):C.GC_5601,(0,77):C.GC_5610,(0,74):C.GC_5456,(0,75):C.GC_5456,(0,79):C.GC_5005,(0,80):C.GC_5005,(0,88):C.GC_5604,(0,89):C.GC_5616,(0,81):C.GC_5589,(0,82):C.GC_5598,(0,83):C.GC_5953,(0,84):C.GC_5589,(0,86):C.GC_5598,(0,87):C.GC_5953,(0,90):C.GC_7127,(0,42):C.GC_5455,(0,66):C.GC_4505,(0,91):C.GC_5457,(0,112):C.GC_5618,(0,45):C.GC_5590,(0,69):C.GC_5586,(0,95):C.GC_5594,(0,43):C.GC_4505,(0,67):C.GC_5455,(0,92):C.GC_5457,(0,115):C.GC_5620,(0,46):C.GC_5586,(0,70):C.GC_5590,(0,96):C.GC_5594,(0,44):C.GC_5005,(0,68):C.GC_5005,(0,94):C.GC_5003,(0,47):C.GC_5595,(0,71):C.GC_5595,(0,97):C.GC_5588,(0,48):C.GC_5948,(0,72):C.GC_5948,(0,98):C.GC_5957})

V_328 = Vertex(name = 'V_328',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS106, L.VVVVS114, L.VVVVS115, L.VVVVS122, L.VVVVS125, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS149, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS159, L.VVVVS164, L.VVVVS166, L.VVVVS167, L.VVVVS170, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS181, L.VVVVS182, L.VVVVS189, L.VVVVS192, L.VVVVS193, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS202, L.VVVVS204, L.VVVVS205, L.VVVVS208, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS236, L.VVVVS237, L.VVVVS241, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS258, L.VVVVS259, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS67, L.VVVVS68, L.VVVVS73, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS96 ],
               couplings = {(0,64):C.GC_5473,(0,65):C.GC_5473,(0,66):C.GC_5133,(0,67):C.GC_5768,(0,68):C.GC_5768,(0,69):C.GC_5758,(0,70):C.GC_5760,(0,71):C.GC_5760,(0,72):C.GC_6071,(0,73):C.GC_4570,(0,74):C.GC_4569,(0,75):C.GC_5472,(0,76):C.GC_5144,(0,0):C.GC_5762,(0,1):C.GC_4904,(0,2):C.GC_5746,(0,3):C.GC_5767,(0,4):C.GC_6074,(0,5):C.GC_4569,(0,6):C.GC_4562,(0,7):C.GC_5144,(0,8):C.GC_5765,(0,9):C.GC_5763,(0,10):C.GC_6073,(0,11):C.GC_5759,(0,12):C.GC_5767,(0,13):C.GC_4569,(0,14):C.GC_4570,(0,15):C.GC_5472,(0,16):C.GC_5144,(0,17):C.GC_4904,(0,18):C.GC_5762,(0,19):C.GC_5746,(0,20):C.GC_5767,(0,21):C.GC_6074,(0,22):C.GC_7134,(0,30):C.GC_4562,(0,31):C.GC_4569,(0,32):C.GC_5144,(0,33):C.GC_5763,(0,34):C.GC_5765,(0,35):C.GC_6073,(0,36):C.GC_5759,(0,37):C.GC_5767,(0,38):C.GC_7134,(0,46):C.GC_5473,(0,47):C.GC_5473,(0,48):C.GC_5143,(0,49):C.GC_5143,(0,50):C.GC_5764,(0,51):C.GC_5745,(0,52):C.GC_6075,(0,53):C.GC_5764,(0,54):C.GC_5745,(0,55):C.GC_6075,(0,56):C.GC_7135,(0,23):C.GC_4570,(0,39):C.GC_4561,(0,57):C.GC_5472,(0,26):C.GC_4905,(0,42):C.GC_5766,(0,60):C.GC_5761,(0,24):C.GC_4561,(0,40):C.GC_4570,(0,58):C.GC_5472,(0,27):C.GC_5766,(0,43):C.GC_4905,(0,61):C.GC_5761,(0,25):C.GC_5143,(0,41):C.GC_5143,(0,59):C.GC_5132,(0,28):C.GC_5760,(0,44):C.GC_5760,(0,62):C.GC_5769,(0,29):C.GC_6072,(0,45):C.GC_6072,(0,63):C.GC_6076})

V_329 = Vertex(name = 'V_329',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6868,(0,1):C.GC_6868,(0,2):C.GC_6876,(0,3):C.GC_6876,(0,4):C.GC_6876,(0,5):C.GC_6876})

V_330 = Vertex(name = 'V_330',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS129, L.VVVSS146, L.VVVSS156, L.VVVSS178, L.VVVSS188 ],
               couplings = {(0,0):C.GC_6913,(0,1):C.GC_6913,(0,2):C.GC_6906,(0,3):C.GC_6906,(0,4):C.GC_6906,(0,5):C.GC_6906})

V_331 = Vertex(name = 'V_331',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS109, L.VVVVS112, L.VVVVS113, L.VVVVS114, L.VVVVS116, L.VVVVS119, L.VVVVS121, L.VVVVS125, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS130, L.VVVVS133, L.VVVVS134, L.VVVVS141, L.VVVVS142, L.VVVVS143, L.VVVVS146, L.VVVVS147, L.VVVVS15, L.VVVVS153, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS160, L.VVVVS161, L.VVVVS162, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS168, L.VVVVS17, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS180, L.VVVVS181, L.VVVVS183, L.VVVVS185, L.VVVVS186, L.VVVVS19, L.VVVVS190, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS198, L.VVVVS199, L.VVVVS2, L.VVVVS20, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS206, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS234, L.VVVVS235, L.VVVVS236, L.VVVVS238, L.VVVVS240, L.VVVVS244, L.VVVVS246, L.VVVVS247, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS252, L.VVVVS253, L.VVVVS254, L.VVVVS255, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS26, L.VVVVS260, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS27, L.VVVVS29, L.VVVVS3, L.VVVVS30, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS35, L.VVVVS36, L.VVVVS38, L.VVVVS39, L.VVVVS4, L.VVVVS49, L.VVVVS50, L.VVVVS54, L.VVVVS55, L.VVVVS56, L.VVVVS58, L.VVVVS59, L.VVVVS6, L.VVVVS60, L.VVVVS62, L.VVVVS63, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS69, L.VVVVS7, L.VVVVS71, L.VVVVS74, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS82, L.VVVVS83, L.VVVVS84, L.VVVVS86, L.VVVVS88, L.VVVVS89, L.VVVVS9, L.VVVVS90, L.VVVVS92, L.VVVVS94, L.VVVVS97 ],
               couplings = {(0,102):C.GC_5610,(0,112):C.GC_5609,(0,0):C.GC_5610,(0,63):C.GC_5609,(0,140):C.GC_5610,(0,1):C.GC_5602,(0,120):C.GC_5610,(0,128):C.GC_5602,(0,54):C.GC_4797,(0,64):C.GC_4797,(0,28):C.GC_5945,(0,43):C.GC_5945,(0,113):C.GC_5611,(0,114):C.GC_5611,(0,115):C.GC_5607,(0,116):C.GC_5612,(0,118):C.GC_5607,(0,119):C.GC_5608,(0,122):C.GC_5943,(0,123):C.GC_5943,(0,94):C.GC_5617,(0,100):C.GC_5622,(0,101):C.GC_5605,(0,103):C.GC_5617,(0,104):C.GC_5606,(0,105):C.GC_5937,(0,106):C.GC_5605,(0,107):C.GC_5606,(0,108):C.GC_5617,(0,109):C.GC_5937,(0,110):C.GC_5615,(0,111):C.GC_5603,(0,124):C.GC_5456,(0,125):C.GC_5458,(0,127):C.GC_5601,(0,126):C.GC_5455,(0,130):C.GC_4796,(0,129):C.GC_5005,(0,136):C.GC_5607,(0,137):C.GC_5611,(0,131):C.GC_5598,(0,132):C.GC_5592,(0,133):C.GC_5590,(0,134):C.GC_5595,(0,135):C.GC_5950,(0,139):C.GC_5601,(0,138):C.GC_5455,(0,141):C.GC_5456,(0,142):C.GC_5458,(0,144):C.GC_4796,(0,143):C.GC_5005,(0,7):C.GC_5607,(0,8):C.GC_5611,(0,2):C.GC_5598,(0,3):C.GC_5590,(0,4):C.GC_5592,(0,5):C.GC_5595,(0,6):C.GC_5950,(0,10):C.GC_5602,(0,9):C.GC_5457,(0,12):C.GC_5609,(0,11):C.GC_5457,(0,13):C.GC_5006,(0,14):C.GC_5006,(0,21):C.GC_5608,(0,22):C.GC_5612,(0,15):C.GC_5593,(0,16):C.GC_5594,(0,17):C.GC_5949,(0,18):C.GC_5593,(0,19):C.GC_5594,(0,20):C.GC_5949,(0,24):C.GC_5610,(0,23):C.GC_5457,(0,26):C.GC_5610,(0,25):C.GC_5457,(0,29):C.GC_5001,(0,27):C.GC_5003,(0,36):C.GC_5607,(0,37):C.GC_5607,(0,38):C.GC_5619,(0,30):C.GC_5588,(0,31):C.GC_5600,(0,32):C.GC_5600,(0,33):C.GC_5591,(0,34):C.GC_5591,(0,35):C.GC_5956,(0,39):C.GC_7126,(0,49):C.GC_5609,(0,48):C.GC_5455,(0,51):C.GC_4504,(0,52):C.GC_4503,(0,50):C.GC_4505,(0,55):C.GC_5938,(0,53):C.GC_5005,(0,61):C.GC_5612,(0,62):C.GC_5940,(0,65):C.GC_5607,(0,66):C.GC_5459,(0,56):C.GC_5595,(0,57):C.GC_5587,(0,58):C.GC_5597,(0,59):C.GC_5586,(0,60):C.GC_5955,(0,67):C.GC_7128,(0,76):C.GC_4504,(0,77):C.GC_4503,(0,75):C.GC_4505,(0,79):C.GC_5609,(0,78):C.GC_5455,(0,81):C.GC_5938,(0,80):C.GC_5005,(0,87):C.GC_5612,(0,88):C.GC_5940,(0,89):C.GC_5607,(0,90):C.GC_5459,(0,82):C.GC_5595,(0,83):C.GC_5587,(0,84):C.GC_5586,(0,85):C.GC_5597,(0,86):C.GC_5955,(0,91):C.GC_7128,(0,40):C.GC_5456,(0,68):C.GC_5458,(0,92):C.GC_4506,(0,41):C.GC_5456,(0,69):C.GC_4506,(0,93):C.GC_5458,(0,42):C.GC_5004,(0,70):C.GC_5006,(0,95):C.GC_5006,(0,44):C.GC_5599,(0,71):C.GC_5591,(0,96):C.GC_5591,(0,117):C.GC_5617,(0,45):C.GC_5589,(0,72):C.GC_5596,(0,97):C.GC_5585,(0,121):C.GC_5622,(0,46):C.GC_5589,(0,73):C.GC_5585,(0,98):C.GC_5596,(0,47):C.GC_5947,(0,74):C.GC_5952,(0,99):C.GC_5952})

V_332 = Vertex(name = 'V_332',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS101, L.VVVVS102, L.VVVVS103, L.VVVVS105, L.VVVVS106, L.VVVVS112, L.VVVVS114, L.VVVVS119, L.VVVVS121, L.VVVVS125, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS130, L.VVVVS141, L.VVVVS143, L.VVVVS147, L.VVVVS154, L.VVVVS155, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS168, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS181, L.VVVVS186, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS206, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS236, L.VVVVS240, L.VVVVS246, L.VVVVS247, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS260, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS71, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS82, L.VVVVS83, L.VVVVS88, L.VVVVS90, L.VVVVS92, L.VVVVS94 ],
               couplings = {(0,64):C.GC_5473,(0,65):C.GC_4569,(0,66):C.GC_4570,(0,67):C.GC_5143,(0,68):C.GC_5745,(0,69):C.GC_5765,(0,70):C.GC_4905,(0,71):C.GC_5760,(0,72):C.GC_6072,(0,73):C.GC_4570,(0,74):C.GC_5473,(0,75):C.GC_4569,(0,76):C.GC_5143,(0,0):C.GC_5745,(0,1):C.GC_4905,(0,2):C.GC_5765,(0,3):C.GC_5760,(0,4):C.GC_6072,(0,5):C.GC_5472,(0,6):C.GC_5472,(0,7):C.GC_5144,(0,8):C.GC_5144,(0,9):C.GC_5746,(0,10):C.GC_5761,(0,11):C.GC_6073,(0,12):C.GC_5746,(0,13):C.GC_5761,(0,14):C.GC_6073,(0,15):C.GC_5472,(0,16):C.GC_5472,(0,17):C.GC_5132,(0,18):C.GC_5769,(0,19):C.GC_5759,(0,20):C.GC_5759,(0,21):C.GC_5767,(0,22):C.GC_5767,(0,23):C.GC_6076,(0,24):C.GC_7132,(0,32):C.GC_4570,(0,33):C.GC_4561,(0,34):C.GC_5143,(0,35):C.GC_5760,(0,36):C.GC_5768,(0,37):C.GC_5762,(0,38):C.GC_5766,(0,39):C.GC_6075,(0,40):C.GC_7133,(0,48):C.GC_4561,(0,49):C.GC_4570,(0,50):C.GC_5143,(0,51):C.GC_5760,(0,52):C.GC_5768,(0,53):C.GC_5766,(0,54):C.GC_5762,(0,55):C.GC_6075,(0,56):C.GC_7133,(0,25):C.GC_5473,(0,41):C.GC_4569,(0,57):C.GC_4562,(0,26):C.GC_5473,(0,42):C.GC_4562,(0,58):C.GC_4569,(0,27):C.GC_5133,(0,43):C.GC_5144,(0,59):C.GC_5144,(0,28):C.GC_5758,(0,44):C.GC_5767,(0,60):C.GC_5767,(0,29):C.GC_5764,(0,45):C.GC_4904,(0,61):C.GC_5763,(0,30):C.GC_5764,(0,46):C.GC_5763,(0,62):C.GC_4904,(0,31):C.GC_6071,(0,47):C.GC_6074,(0,63):C.GC_6074})

V_333 = Vertex(name = 'V_333',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6477,(0,1):C.GC_6477,(0,2):C.GC_6475,(0,3):C.GC_6475,(0,4):C.GC_6475,(0,5):C.GC_6475,(0,6):C.GC_6477,(0,7):C.GC_6472,(0,8):C.GC_6472})

V_334 = Vertex(name = 'V_334',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6600,(0,1):C.GC_6600,(0,2):C.GC_6599,(0,3):C.GC_6599,(0,4):C.GC_6599,(0,5):C.GC_6599,(0,6):C.GC_6600,(0,7):C.GC_6589,(0,8):C.GC_6589})

V_335 = Vertex(name = 'V_335',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_6474,(0,1):C.GC_6474,(0,2):C.GC_6479,(0,3):C.GC_6479,(0,4):C.GC_6467,(0,5):C.GC_6473})

V_336 = Vertex(name = 'V_336',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS5, L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_6595,(0,1):C.GC_6595,(0,2):C.GC_6602,(0,3):C.GC_6602,(0,4):C.GC_6594,(0,5):C.GC_6603})

V_337 = Vertex(name = 'V_337',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6469,(0,1):C.GC_6469,(0,2):C.GC_6468,(0,3):C.GC_6468,(0,4):C.GC_6468,(0,5):C.GC_6468,(0,6):C.GC_6476,(0,7):C.GC_6470,(0,8):C.GC_6470})

V_338 = Vertex(name = 'V_338',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6597,(0,1):C.GC_6597,(0,2):C.GC_6596,(0,3):C.GC_6596,(0,4):C.GC_6596,(0,5):C.GC_6596,(0,6):C.GC_6590,(0,7):C.GC_6598,(0,8):C.GC_6598})

V_339 = Vertex(name = 'V_339',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6471,(0,1):C.GC_6471,(0,2):C.GC_6471,(0,3):C.GC_6471,(0,4):C.GC_6471,(0,5):C.GC_6471,(0,6):C.GC_6478,(0,7):C.GC_6478,(0,8):C.GC_6478})

V_340 = Vertex(name = 'V_340',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS3, L.VVSSS4, L.VVSSS5, L.VVSSS6, L.VVSSS7, L.VVSSS8, L.VVSSS9 ],
               couplings = {(0,0):C.GC_6588,(0,1):C.GC_6588,(0,2):C.GC_6588,(0,3):C.GC_6588,(0,4):C.GC_6588,(0,5):C.GC_6588,(0,6):C.GC_6601,(0,7):C.GC_6601,(0,8):C.GC_6601})

V_341 = Vertex(name = 'V_341',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS14, L.VVVSS140, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS6, L.VVVSS61, L.VVVSS62, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS92, L.VVVSS93, L.VVVSS95, L.VVVSS96, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,103):C.GC_3431,(0,102):C.GC_3937,(0,107):C.GC_3431,(0,108):C.GC_422,(0,105):C.GC_423,(0,106):C.GC_3937,(0,89):C.GC_3442,(0,0):C.GC_3965,(0,123):C.GC_3433,(0,132):C.GC_3319,(0,140):C.GC_3322,(0,104):C.GC_3965,(0,115):C.GC_3330,(0,152):C.GC_3940,(0,146):C.GC_3970,(0,26):C.GC_421,(0,35):C.GC_3913,(0,1):C.GC_3920,(0,8):C.GC_3314,(0,62):C.GC_3913,(0,44):C.GC_3920,(0,90):C.GC_3940,(0,95):C.GC_421,(0,67):C.GC_3970,(0,78):C.GC_3314,(0,154):C.GC_1219,(0,155):C.GC_1219,(0,3):C.GC_3443,(0,2):C.GC_3933,(0,6):C.GC_3443,(0,7):C.GC_421,(0,4):C.GC_424,(0,5):C.GC_3933,(0,9):C.GC_1203,(0,10):C.GC_1218,(0,11):C.GC_1203,(0,12):C.GC_1203,(0,110):C.GC_3430,(0,109):C.GC_3956,(0,113):C.GC_3445,(0,114):C.GC_3321,(0,116):C.GC_3320,(0,111):C.GC_3956,(0,112):C.GC_3328,(0,119):C.GC_1200,(0,120):C.GC_1221,(0,117):C.GC_1188,(0,118):C.GC_1188,(0,122):C.GC_3935,(0,121):C.GC_3963,(0,126):C.GC_422,(0,127):C.GC_3911,(0,124):C.GC_3918,(0,125):C.GC_3312,(0,131):C.GC_1222,(0,133):C.GC_1200,(0,128):C.GC_1193,(0,129):C.GC_1190,(0,130):C.GC_1195,(0,135):C.GC_3911,(0,134):C.GC_3918,(0,138):C.GC_3935,(0,139):C.GC_422,(0,136):C.GC_3963,(0,137):C.GC_3312,(0,144):C.GC_1222,(0,145):C.GC_1200,(0,141):C.GC_1193,(0,142):C.GC_1195,(0,143):C.GC_1190,(0,23):C.GC_3444,(0,24):C.GC_423,(0,15):C.GC_6967,(0,38):C.GC_3432,(0,39):C.GC_424,(0,25):C.GC_6958,(0,49):C.GC_3444,(0,50):C.GC_423,(0,40):C.GC_6967,(0,63):C.GC_3432,(0,64):C.GC_424,(0,51):C.GC_6958,(0,74):C.GC_3937,(0,75):C.GC_3937,(0,65):C.GC_6965,(0,93):C.GC_3933,(0,94):C.GC_3933,(0,76):C.GC_6962,(0,16):C.GC_3919,(0,27):C.GC_3921,(0,41):C.GC_3957,(0,52):C.GC_3964,(0,66):C.GC_3962,(0,77):C.GC_3971,(0,17):C.GC_3957,(0,28):C.GC_3964,(0,42):C.GC_3919,(0,53):C.GC_3921,(0,68):C.GC_3962,(0,79):C.GC_3971,(0,97):C.GC_3433,(0,100):C.GC_3442,(0,19):C.GC_3962,(0,46):C.GC_3962,(0,70):C.GC_3965,(0,71):C.GC_3965,(0,148):C.GC_3445,(0,151):C.GC_3430,(0,31):C.GC_3971,(0,57):C.GC_3971,(0,83):C.GC_3956,(0,84):C.GC_3956,(0,18):C.GC_3311,(0,29):C.GC_3313,(0,43):C.GC_3311,(0,54):C.GC_3313,(0,69):C.GC_3327,(0,80):C.GC_3329,(0,96):C.GC_3940,(0,101):C.GC_421,(0,13):C.GC_1219,(0,20):C.GC_3957,(0,30):C.GC_1188,(0,45):C.GC_3970,(0,47):C.GC_3314,(0,72):C.GC_3311,(0,81):C.GC_1195,(0,147):C.GC_3935,(0,153):C.GC_422,(0,158):C.GC_1222,(0,32):C.GC_3964,(0,36):C.GC_1193,(0,56):C.GC_3963,(0,58):C.GC_3312,(0,85):C.GC_3313,(0,87):C.GC_1190,(0,98):C.GC_3932,(0,99):C.GC_424,(0,14):C.GC_1205,(0,21):C.GC_3970,(0,22):C.GC_3314,(0,48):C.GC_3957,(0,55):C.GC_1188,(0,73):C.GC_3311,(0,82):C.GC_1195,(0,149):C.GC_3936,(0,150):C.GC_423,(0,159):C.GC_1202,(0,33):C.GC_3963,(0,34):C.GC_3312,(0,59):C.GC_3964,(0,60):C.GC_1193,(0,86):C.GC_3313,(0,88):C.GC_1190,(0,156):C.GC_113,(0,157):C.GC_114,(0,37):C.GC_118,(0,61):C.GC_118,(0,91):C.GC_119,(0,92):C.GC_119})

V_342 = Vertex(name = 'V_342',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS140, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4199,(0,66):C.GC_4199,(0,70):C.GC_3652,(0,85):C.GC_4198,(0,1):C.GC_4178,(0,2):C.GC_3661,(0,26):C.GC_4178,(0,44):C.GC_4198,(0,53):C.GC_3661,(0,67):C.GC_4196,(0,68):C.GC_4196,(0,69):C.GC_3650,(0,71):C.GC_1338,(0,72):C.GC_1338,(0,73):C.GC_4193,(0,74):C.GC_4176,(0,75):C.GC_3663,(0,76):C.GC_1336,(0,77):C.GC_1339,(0,78):C.GC_1337,(0,79):C.GC_4176,(0,80):C.GC_4193,(0,81):C.GC_3663,(0,82):C.GC_1336,(0,83):C.GC_1337,(0,84):C.GC_1339,(0,3):C.GC_7010,(0,11):C.GC_7007,(0,22):C.GC_7010,(0,31):C.GC_7007,(0,42):C.GC_7012,(0,51):C.GC_7000,(0,4):C.GC_4177,(0,12):C.GC_4179,(0,23):C.GC_4195,(0,32):C.GC_4200,(0,43):C.GC_4194,(0,52):C.GC_4197,(0,5):C.GC_4195,(0,13):C.GC_4200,(0,24):C.GC_4177,(0,33):C.GC_4179,(0,45):C.GC_4194,(0,54):C.GC_4197,(0,7):C.GC_4194,(0,28):C.GC_4194,(0,47):C.GC_4199,(0,48):C.GC_4199,(0,16):C.GC_4197,(0,37):C.GC_4197,(0,58):C.GC_4196,(0,59):C.GC_4196,(0,6):C.GC_3662,(0,14):C.GC_3660,(0,25):C.GC_3662,(0,34):C.GC_3660,(0,46):C.GC_3649,(0,55):C.GC_3651,(0,8):C.GC_4195,(0,15):C.GC_1338,(0,27):C.GC_4198,(0,29):C.GC_3661,(0,49):C.GC_3662,(0,56):C.GC_1337,(0,17):C.GC_4200,(0,20):C.GC_1336,(0,36):C.GC_4193,(0,38):C.GC_3663,(0,60):C.GC_3660,(0,62):C.GC_1339,(0,9):C.GC_4198,(0,10):C.GC_3661,(0,30):C.GC_4195,(0,35):C.GC_1338,(0,50):C.GC_3662,(0,57):C.GC_1337,(0,18):C.GC_4193,(0,19):C.GC_3663,(0,39):C.GC_4200,(0,40):C.GC_1336,(0,61):C.GC_3660,(0,63):C.GC_1339,(0,21):C.GC_513,(0,41):C.GC_513,(0,64):C.GC_514,(0,65):C.GC_514})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS14, L.VVVSS140, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS6, L.VVVSS61, L.VVVSS62, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS92, L.VVVSS93, L.VVVSS95, L.VVVSS96, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,103):C.GC_3434,(0,102):C.GC_3927,(0,107):C.GC_3434,(0,108):C.GC_420,(0,105):C.GC_425,(0,106):C.GC_3927,(0,89):C.GC_3439,(0,0):C.GC_3952,(0,123):C.GC_3436,(0,132):C.GC_3323,(0,140):C.GC_3318,(0,104):C.GC_3952,(0,115):C.GC_3326,(0,152):C.GC_3924,(0,146):C.GC_3951,(0,26):C.GC_419,(0,35):C.GC_3910,(0,1):C.GC_3916,(0,8):C.GC_3310,(0,62):C.GC_3910,(0,44):C.GC_3916,(0,90):C.GC_3924,(0,95):C.GC_419,(0,67):C.GC_3951,(0,78):C.GC_3310,(0,154):C.GC_1210,(0,155):C.GC_1210,(0,3):C.GC_3438,(0,2):C.GC_3946,(0,6):C.GC_3438,(0,7):C.GC_419,(0,4):C.GC_426,(0,5):C.GC_3946,(0,9):C.GC_1212,(0,10):C.GC_1209,(0,11):C.GC_1212,(0,12):C.GC_1212,(0,110):C.GC_3435,(0,109):C.GC_3977,(0,113):C.GC_3440,(0,114):C.GC_3317,(0,116):C.GC_3324,(0,111):C.GC_3977,(0,112):C.GC_3332,(0,119):C.GC_1215,(0,120):C.GC_1206,(0,117):C.GC_1196,(0,118):C.GC_1196,(0,122):C.GC_3944,(0,121):C.GC_3974,(0,126):C.GC_420,(0,127):C.GC_3915,(0,124):C.GC_3922,(0,125):C.GC_3316,(0,131):C.GC_1207,(0,133):C.GC_1215,(0,128):C.GC_1185,(0,129):C.GC_1198,(0,130):C.GC_1187,(0,135):C.GC_3915,(0,134):C.GC_3922,(0,138):C.GC_3944,(0,139):C.GC_420,(0,136):C.GC_3974,(0,137):C.GC_3316,(0,144):C.GC_1207,(0,145):C.GC_1215,(0,141):C.GC_1185,(0,142):C.GC_1187,(0,143):C.GC_1198,(0,23):C.GC_3441,(0,24):C.GC_425,(0,15):C.GC_6957,(0,38):C.GC_3437,(0,39):C.GC_426,(0,25):C.GC_6960,(0,49):C.GC_3441,(0,50):C.GC_425,(0,40):C.GC_6957,(0,63):C.GC_3437,(0,64):C.GC_426,(0,51):C.GC_6960,(0,74):C.GC_3927,(0,75):C.GC_3927,(0,65):C.GC_6961,(0,93):C.GC_3946,(0,94):C.GC_3946,(0,76):C.GC_6968,(0,16):C.GC_3923,(0,27):C.GC_3917,(0,41):C.GC_3976,(0,52):C.GC_3953,(0,66):C.GC_3975,(0,77):C.GC_3950,(0,17):C.GC_3976,(0,28):C.GC_3953,(0,42):C.GC_3923,(0,53):C.GC_3917,(0,68):C.GC_3975,(0,79):C.GC_3950,(0,97):C.GC_3436,(0,100):C.GC_3439,(0,19):C.GC_3975,(0,46):C.GC_3975,(0,70):C.GC_3952,(0,71):C.GC_3952,(0,148):C.GC_3440,(0,151):C.GC_3435,(0,31):C.GC_3950,(0,57):C.GC_3950,(0,83):C.GC_3977,(0,84):C.GC_3977,(0,18):C.GC_3315,(0,29):C.GC_3309,(0,43):C.GC_3315,(0,54):C.GC_3309,(0,69):C.GC_3331,(0,80):C.GC_3325,(0,96):C.GC_3924,(0,101):C.GC_419,(0,13):C.GC_1210,(0,20):C.GC_3976,(0,30):C.GC_1196,(0,45):C.GC_3951,(0,47):C.GC_3310,(0,72):C.GC_3315,(0,81):C.GC_1187,(0,147):C.GC_3944,(0,153):C.GC_420,(0,158):C.GC_1207,(0,32):C.GC_3953,(0,36):C.GC_1185,(0,56):C.GC_3974,(0,58):C.GC_3316,(0,85):C.GC_3309,(0,87):C.GC_1198,(0,98):C.GC_3947,(0,99):C.GC_426,(0,14):C.GC_1214,(0,21):C.GC_3951,(0,22):C.GC_3310,(0,48):C.GC_3976,(0,55):C.GC_1196,(0,73):C.GC_3315,(0,82):C.GC_1187,(0,149):C.GC_3928,(0,150):C.GC_425,(0,159):C.GC_1217,(0,33):C.GC_3974,(0,34):C.GC_3316,(0,59):C.GC_3953,(0,60):C.GC_1185,(0,86):C.GC_3309,(0,88):C.GC_1198,(0,156):C.GC_112,(0,157):C.GC_116,(0,37):C.GC_117,(0,61):C.GC_117,(0,91):C.GC_120,(0,92):C.GC_120})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS140, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4192,(0,66):C.GC_4192,(0,70):C.GC_3648,(0,85):C.GC_4189,(0,1):C.GC_4174,(0,2):C.GC_3665,(0,26):C.GC_4174,(0,44):C.GC_4189,(0,53):C.GC_3665,(0,67):C.GC_4203,(0,68):C.GC_4203,(0,69):C.GC_3654,(0,71):C.GC_1334,(0,72):C.GC_1334,(0,73):C.GC_4202,(0,74):C.GC_4180,(0,75):C.GC_3659,(0,76):C.GC_1340,(0,77):C.GC_1335,(0,78):C.GC_1341,(0,79):C.GC_4180,(0,80):C.GC_4202,(0,81):C.GC_3659,(0,82):C.GC_1340,(0,83):C.GC_1341,(0,84):C.GC_1335,(0,3):C.GC_7006,(0,11):C.GC_7013,(0,22):C.GC_7006,(0,31):C.GC_7013,(0,42):C.GC_6999,(0,51):C.GC_7002,(0,4):C.GC_4181,(0,12):C.GC_4175,(0,23):C.GC_4204,(0,32):C.GC_4191,(0,43):C.GC_4201,(0,52):C.GC_4190,(0,5):C.GC_4204,(0,13):C.GC_4191,(0,24):C.GC_4181,(0,33):C.GC_4175,(0,45):C.GC_4201,(0,54):C.GC_4190,(0,7):C.GC_4201,(0,28):C.GC_4201,(0,47):C.GC_4192,(0,48):C.GC_4192,(0,16):C.GC_4190,(0,37):C.GC_4190,(0,58):C.GC_4203,(0,59):C.GC_4203,(0,6):C.GC_3658,(0,14):C.GC_3664,(0,25):C.GC_3658,(0,34):C.GC_3664,(0,46):C.GC_3653,(0,55):C.GC_3647,(0,8):C.GC_4204,(0,15):C.GC_1334,(0,27):C.GC_4189,(0,29):C.GC_3665,(0,49):C.GC_3658,(0,56):C.GC_1341,(0,17):C.GC_4191,(0,20):C.GC_1340,(0,36):C.GC_4202,(0,38):C.GC_3659,(0,60):C.GC_3664,(0,62):C.GC_1335,(0,9):C.GC_4189,(0,10):C.GC_3665,(0,30):C.GC_4204,(0,35):C.GC_1334,(0,50):C.GC_3658,(0,57):C.GC_1341,(0,18):C.GC_4202,(0,19):C.GC_3659,(0,39):C.GC_4191,(0,40):C.GC_1340,(0,61):C.GC_3664,(0,63):C.GC_1335,(0,21):C.GC_512,(0,41):C.GC_512,(0,64):C.GC_515,(0,65):C.GC_515})

V_345 = Vertex(name = 'V_345',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS14, L.VVVSS140, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS6, L.VVVSS61, L.VVVSS62, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS92, L.VVVSS93, L.VVVSS95, L.VVVSS96, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,103):C.GC_3433,(0,102):C.GC_3931,(0,107):C.GC_3433,(0,108):C.GC_424,(0,105):C.GC_421,(0,106):C.GC_3931,(0,89):C.GC_3444,(0,0):C.GC_3958,(0,123):C.GC_3431,(0,132):C.GC_3322,(0,140):C.GC_3319,(0,104):C.GC_3958,(0,115):C.GC_3327,(0,152):C.GC_3934,(0,146):C.GC_3961,(0,26):C.GC_423,(0,35):C.GC_3912,(0,1):C.GC_3919,(0,8):C.GC_3311,(0,62):C.GC_3912,(0,44):C.GC_3919,(0,90):C.GC_3934,(0,95):C.GC_423,(0,67):C.GC_3961,(0,78):C.GC_3311,(0,154):C.GC_1223,(0,155):C.GC_1223,(0,3):C.GC_3445,(0,2):C.GC_3939,(0,6):C.GC_3445,(0,7):C.GC_423,(0,4):C.GC_422,(0,5):C.GC_3939,(0,9):C.GC_1200,(0,10):C.GC_1221,(0,11):C.GC_1200,(0,12):C.GC_1200,(0,110):C.GC_3432,(0,109):C.GC_3967,(0,113):C.GC_3443,(0,114):C.GC_3320,(0,116):C.GC_3321,(0,111):C.GC_3967,(0,112):C.GC_3329,(0,119):C.GC_1203,(0,120):C.GC_1218,(0,117):C.GC_1194,(0,118):C.GC_1194,(0,122):C.GC_3941,(0,121):C.GC_3968,(0,126):C.GC_424,(0,127):C.GC_3914,(0,124):C.GC_3921,(0,125):C.GC_3313,(0,131):C.GC_1220,(0,133):C.GC_1203,(0,128):C.GC_1191,(0,129):C.GC_1192,(0,130):C.GC_1189,(0,135):C.GC_3914,(0,134):C.GC_3921,(0,138):C.GC_3941,(0,139):C.GC_424,(0,136):C.GC_3968,(0,137):C.GC_3313,(0,144):C.GC_1220,(0,145):C.GC_1203,(0,141):C.GC_1191,(0,142):C.GC_1189,(0,143):C.GC_1192,(0,23):C.GC_3442,(0,24):C.GC_421,(0,15):C.GC_6966,(0,38):C.GC_3430,(0,39):C.GC_422,(0,25):C.GC_6959,(0,49):C.GC_3442,(0,50):C.GC_421,(0,40):C.GC_6966,(0,63):C.GC_3430,(0,64):C.GC_422,(0,51):C.GC_6959,(0,74):C.GC_3931,(0,75):C.GC_3931,(0,65):C.GC_6963,(0,93):C.GC_3939,(0,94):C.GC_3939,(0,76):C.GC_6964,(0,16):C.GC_3920,(0,27):C.GC_3918,(0,41):C.GC_3966,(0,52):C.GC_3959,(0,66):C.GC_3969,(0,77):C.GC_3960,(0,17):C.GC_3966,(0,28):C.GC_3959,(0,42):C.GC_3920,(0,53):C.GC_3918,(0,68):C.GC_3969,(0,79):C.GC_3960,(0,97):C.GC_3431,(0,100):C.GC_3444,(0,19):C.GC_3969,(0,46):C.GC_3969,(0,70):C.GC_3958,(0,71):C.GC_3958,(0,148):C.GC_3443,(0,151):C.GC_3432,(0,31):C.GC_3960,(0,57):C.GC_3960,(0,83):C.GC_3967,(0,84):C.GC_3967,(0,18):C.GC_3314,(0,29):C.GC_3312,(0,43):C.GC_3314,(0,54):C.GC_3312,(0,69):C.GC_3330,(0,80):C.GC_3328,(0,96):C.GC_3934,(0,101):C.GC_423,(0,13):C.GC_1223,(0,20):C.GC_3966,(0,30):C.GC_1194,(0,45):C.GC_3961,(0,47):C.GC_3311,(0,72):C.GC_3314,(0,81):C.GC_1189,(0,147):C.GC_3941,(0,153):C.GC_424,(0,158):C.GC_1220,(0,32):C.GC_3959,(0,36):C.GC_1191,(0,56):C.GC_3968,(0,58):C.GC_3313,(0,85):C.GC_3312,(0,87):C.GC_1192,(0,98):C.GC_3938,(0,99):C.GC_422,(0,14):C.GC_1201,(0,21):C.GC_3961,(0,22):C.GC_3311,(0,48):C.GC_3966,(0,55):C.GC_1194,(0,73):C.GC_3314,(0,82):C.GC_1189,(0,149):C.GC_3930,(0,150):C.GC_421,(0,159):C.GC_1204,(0,33):C.GC_3968,(0,34):C.GC_3313,(0,59):C.GC_3959,(0,60):C.GC_1191,(0,86):C.GC_3312,(0,88):C.GC_1192,(0,156):C.GC_114,(0,157):C.GC_113,(0,37):C.GC_119,(0,61):C.GC_119,(0,91):C.GC_118,(0,92):C.GC_118})

V_346 = Vertex(name = 'V_346',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS140, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4194,(0,66):C.GC_4194,(0,70):C.GC_3649,(0,85):C.GC_4195,(0,1):C.GC_4177,(0,2):C.GC_3662,(0,26):C.GC_4177,(0,44):C.GC_4195,(0,53):C.GC_3662,(0,67):C.GC_4197,(0,68):C.GC_4197,(0,69):C.GC_3651,(0,71):C.GC_1337,(0,72):C.GC_1337,(0,73):C.GC_4200,(0,74):C.GC_4179,(0,75):C.GC_3660,(0,76):C.GC_1339,(0,77):C.GC_1336,(0,78):C.GC_1338,(0,79):C.GC_4179,(0,80):C.GC_4200,(0,81):C.GC_3660,(0,82):C.GC_1339,(0,83):C.GC_1338,(0,84):C.GC_1336,(0,3):C.GC_7009,(0,11):C.GC_7008,(0,22):C.GC_7009,(0,31):C.GC_7008,(0,42):C.GC_7011,(0,51):C.GC_7001,(0,4):C.GC_4178,(0,12):C.GC_4176,(0,23):C.GC_4198,(0,32):C.GC_4193,(0,43):C.GC_4199,(0,52):C.GC_4196,(0,5):C.GC_4198,(0,13):C.GC_4193,(0,24):C.GC_4178,(0,33):C.GC_4176,(0,45):C.GC_4199,(0,54):C.GC_4196,(0,7):C.GC_4199,(0,28):C.GC_4199,(0,47):C.GC_4194,(0,48):C.GC_4194,(0,16):C.GC_4196,(0,37):C.GC_4196,(0,58):C.GC_4197,(0,59):C.GC_4197,(0,6):C.GC_3661,(0,14):C.GC_3663,(0,25):C.GC_3661,(0,34):C.GC_3663,(0,46):C.GC_3652,(0,55):C.GC_3650,(0,8):C.GC_4198,(0,15):C.GC_1337,(0,27):C.GC_4195,(0,29):C.GC_3662,(0,49):C.GC_3661,(0,56):C.GC_1338,(0,17):C.GC_4193,(0,20):C.GC_1339,(0,36):C.GC_4200,(0,38):C.GC_3660,(0,60):C.GC_3663,(0,62):C.GC_1336,(0,9):C.GC_4195,(0,10):C.GC_3662,(0,30):C.GC_4198,(0,35):C.GC_1337,(0,50):C.GC_3661,(0,57):C.GC_1338,(0,18):C.GC_4200,(0,19):C.GC_3660,(0,39):C.GC_4193,(0,40):C.GC_1339,(0,61):C.GC_3663,(0,63):C.GC_1336,(0,21):C.GC_514,(0,41):C.GC_514,(0,64):C.GC_513,(0,65):C.GC_513})

V_347 = Vertex(name = 'V_347',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS110, L.VVVSS111, L.VVVSS113, L.VVVSS115, L.VVVSS117, L.VVVSS118, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS14, L.VVVSS140, L.VVVSS142, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS2, L.VVVSS20, L.VVVSS200, L.VVVSS201, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS42, L.VVVSS44, L.VVVSS46, L.VVVSS47, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS53, L.VVVSS54, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS59, L.VVVSS6, L.VVVSS61, L.VVVSS62, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS7, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS73, L.VVVSS75, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90, L.VVVSS92, L.VVVSS93, L.VVVSS95, L.VVVSS96, L.VVVSS98, L.VVVSS99 ],
               couplings = {(0,103):C.GC_3439,(0,102):C.GC_3926,(0,107):C.GC_3439,(0,108):C.GC_419,(0,105):C.GC_426,(0,106):C.GC_3926,(0,89):C.GC_3434,(0,0):C.GC_3948,(0,123):C.GC_3441,(0,132):C.GC_3323,(0,140):C.GC_3318,(0,104):C.GC_3948,(0,115):C.GC_3326,(0,152):C.GC_3929,(0,146):C.GC_3955,(0,26):C.GC_420,(0,35):C.GC_3910,(0,1):C.GC_3916,(0,8):C.GC_3310,(0,62):C.GC_3910,(0,44):C.GC_3916,(0,90):C.GC_3929,(0,95):C.GC_420,(0,67):C.GC_3955,(0,78):C.GC_3310,(0,154):C.GC_1216,(0,155):C.GC_1216,(0,3):C.GC_3435,(0,2):C.GC_3943,(0,6):C.GC_3435,(0,7):C.GC_420,(0,4):C.GC_425,(0,5):C.GC_3943,(0,9):C.GC_1206,(0,10):C.GC_1215,(0,11):C.GC_1206,(0,12):C.GC_1206,(0,110):C.GC_3438,(0,109):C.GC_3973,(0,113):C.GC_3437,(0,114):C.GC_3317,(0,116):C.GC_3324,(0,111):C.GC_3973,(0,112):C.GC_3332,(0,119):C.GC_1209,(0,120):C.GC_1212,(0,117):C.GC_1197,(0,118):C.GC_1197,(0,122):C.GC_3945,(0,121):C.GC_3978,(0,126):C.GC_419,(0,127):C.GC_3915,(0,124):C.GC_3922,(0,125):C.GC_3316,(0,131):C.GC_1213,(0,133):C.GC_1209,(0,128):C.GC_1184,(0,129):C.GC_1199,(0,130):C.GC_1186,(0,135):C.GC_3915,(0,134):C.GC_3922,(0,138):C.GC_3945,(0,139):C.GC_419,(0,136):C.GC_3978,(0,137):C.GC_3316,(0,144):C.GC_1213,(0,145):C.GC_1209,(0,141):C.GC_1184,(0,142):C.GC_1186,(0,143):C.GC_1199,(0,23):C.GC_3436,(0,24):C.GC_426,(0,15):C.GC_6957,(0,38):C.GC_3440,(0,39):C.GC_425,(0,25):C.GC_6960,(0,49):C.GC_3436,(0,50):C.GC_426,(0,40):C.GC_6957,(0,63):C.GC_3440,(0,64):C.GC_425,(0,51):C.GC_6960,(0,74):C.GC_3926,(0,75):C.GC_3926,(0,65):C.GC_6961,(0,93):C.GC_3943,(0,94):C.GC_3943,(0,76):C.GC_6968,(0,16):C.GC_3923,(0,27):C.GC_3917,(0,41):C.GC_3972,(0,52):C.GC_3949,(0,66):C.GC_3979,(0,77):C.GC_3954,(0,17):C.GC_3972,(0,28):C.GC_3949,(0,42):C.GC_3923,(0,53):C.GC_3917,(0,68):C.GC_3979,(0,79):C.GC_3954,(0,97):C.GC_3441,(0,100):C.GC_3434,(0,19):C.GC_3979,(0,46):C.GC_3979,(0,70):C.GC_3948,(0,71):C.GC_3948,(0,148):C.GC_3437,(0,151):C.GC_3438,(0,31):C.GC_3954,(0,57):C.GC_3954,(0,83):C.GC_3973,(0,84):C.GC_3973,(0,18):C.GC_3315,(0,29):C.GC_3309,(0,43):C.GC_3315,(0,54):C.GC_3309,(0,69):C.GC_3331,(0,80):C.GC_3325,(0,96):C.GC_3929,(0,101):C.GC_420,(0,13):C.GC_1216,(0,20):C.GC_3972,(0,30):C.GC_1197,(0,45):C.GC_3955,(0,47):C.GC_3310,(0,72):C.GC_3315,(0,81):C.GC_1186,(0,147):C.GC_3945,(0,153):C.GC_419,(0,158):C.GC_1213,(0,32):C.GC_3949,(0,36):C.GC_1184,(0,56):C.GC_3978,(0,58):C.GC_3316,(0,85):C.GC_3309,(0,87):C.GC_1199,(0,98):C.GC_3942,(0,99):C.GC_425,(0,14):C.GC_1208,(0,21):C.GC_3955,(0,22):C.GC_3310,(0,48):C.GC_3972,(0,55):C.GC_1197,(0,73):C.GC_3315,(0,82):C.GC_1186,(0,149):C.GC_3925,(0,150):C.GC_426,(0,159):C.GC_1211,(0,33):C.GC_3978,(0,34):C.GC_3316,(0,59):C.GC_3949,(0,60):C.GC_1184,(0,86):C.GC_3309,(0,88):C.GC_1199,(0,156):C.GC_112,(0,157):C.GC_116,(0,37):C.GC_117,(0,61):C.GC_117,(0,91):C.GC_120,(0,92):C.GC_120})

V_348 = Vertex(name = 'V_348',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS134, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS140, L.VVVSS142, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS161, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS167, L.VVVSS169, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS198, L.VVVSS199, L.VVVSS200, L.VVVSS201, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS42, L.VVVSS44, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS56, L.VVVSS57, L.VVVSS58, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS70, L.VVVSS71, L.VVVSS72, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4192,(0,66):C.GC_4192,(0,70):C.GC_3648,(0,85):C.GC_4189,(0,1):C.GC_4174,(0,2):C.GC_3665,(0,26):C.GC_4174,(0,44):C.GC_4189,(0,53):C.GC_3665,(0,67):C.GC_4203,(0,68):C.GC_4203,(0,69):C.GC_3654,(0,71):C.GC_1334,(0,72):C.GC_1334,(0,73):C.GC_4202,(0,74):C.GC_4180,(0,75):C.GC_3659,(0,76):C.GC_1340,(0,77):C.GC_1335,(0,78):C.GC_1341,(0,79):C.GC_4180,(0,80):C.GC_4202,(0,81):C.GC_3659,(0,82):C.GC_1340,(0,83):C.GC_1341,(0,84):C.GC_1335,(0,3):C.GC_7006,(0,11):C.GC_7013,(0,22):C.GC_7006,(0,31):C.GC_7013,(0,42):C.GC_6999,(0,51):C.GC_7002,(0,4):C.GC_4181,(0,12):C.GC_4175,(0,23):C.GC_4204,(0,32):C.GC_4191,(0,43):C.GC_4201,(0,52):C.GC_4190,(0,5):C.GC_4204,(0,13):C.GC_4191,(0,24):C.GC_4181,(0,33):C.GC_4175,(0,45):C.GC_4201,(0,54):C.GC_4190,(0,7):C.GC_4201,(0,28):C.GC_4201,(0,47):C.GC_4192,(0,48):C.GC_4192,(0,16):C.GC_4190,(0,37):C.GC_4190,(0,58):C.GC_4203,(0,59):C.GC_4203,(0,6):C.GC_3658,(0,14):C.GC_3664,(0,25):C.GC_3658,(0,34):C.GC_3664,(0,46):C.GC_3653,(0,55):C.GC_3647,(0,8):C.GC_4204,(0,15):C.GC_1334,(0,27):C.GC_4189,(0,29):C.GC_3665,(0,49):C.GC_3658,(0,56):C.GC_1341,(0,17):C.GC_4191,(0,20):C.GC_1340,(0,36):C.GC_4202,(0,38):C.GC_3659,(0,60):C.GC_3664,(0,62):C.GC_1335,(0,9):C.GC_4189,(0,10):C.GC_3665,(0,30):C.GC_4204,(0,35):C.GC_1334,(0,50):C.GC_3658,(0,57):C.GC_1341,(0,18):C.GC_4202,(0,19):C.GC_3659,(0,39):C.GC_4191,(0,40):C.GC_1340,(0,61):C.GC_3664,(0,63):C.GC_1335,(0,21):C.GC_512,(0,41):C.GC_512,(0,64):C.GC_515,(0,65):C.GC_515})

V_349 = Vertex(name = 'V_349',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS104, L.VVVSS105, L.VVVSS106, L.VVVSS107, L.VVVSS108, L.VVVSS109, L.VVVSS11, L.VVVSS119, L.VVVSS12, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS127, L.VVVSS128, L.VVVSS129, L.VVVSS13, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS14, L.VVVSS143, L.VVVSS144, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS154, L.VVVSS155, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS16, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS17, L.VVVSS170, L.VVVSS171, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS186, L.VVVSS187, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS2, L.VVVSS20, L.VVVSS202, L.VVVSS203, L.VVVSS21, L.VVVSS22, L.VVVSS23, L.VVVSS24, L.VVVSS25, L.VVVSS26, L.VVVSS27, L.VVVSS28, L.VVVSS29, L.VVVSS3, L.VVVSS30, L.VVVSS31, L.VVVSS32, L.VVVSS33, L.VVVSS34, L.VVVSS35, L.VVVSS36, L.VVVSS37, L.VVVSS38, L.VVVSS39, L.VVVSS4, L.VVVSS40, L.VVVSS48, L.VVVSS49, L.VVVSS5, L.VVVSS50, L.VVVSS51, L.VVVSS52, L.VVVSS53, L.VVVSS54, L.VVVSS6, L.VVVSS62, L.VVVSS63, L.VVVSS64, L.VVVSS65, L.VVVSS66, L.VVVSS67, L.VVVSS68, L.VVVSS7, L.VVVSS8, L.VVVSS85, L.VVVSS86, L.VVVSS87, L.VVVSS88, L.VVVSS89, L.VVVSS9, L.VVVSS90 ],
               couplings = {(0,87):C.GC_3497,(0,86):C.GC_4328,(0,91):C.GC_3497,(0,92):C.GC_3501,(0,89):C.GC_3502,(0,90):C.GC_4328,(0,75):C.GC_3499,(0,0):C.GC_4333,(0,103):C.GC_3496,(0,109):C.GC_3889,(0,117):C.GC_3888,(0,88):C.GC_4333,(0,99):C.GC_3890,(0,124):C.GC_4327,(0,118):C.GC_4332,(0,10):C.GC_3901,(0,21):C.GC_3500,(0,29):C.GC_4321,(0,1):C.GC_4324,(0,8):C.GC_3886,(0,47):C.GC_3901,(0,52):C.GC_4321,(0,36):C.GC_4324,(0,76):C.GC_4327,(0,79):C.GC_3500,(0,57):C.GC_4332,(0,68):C.GC_3886,(0,3):C.GC_3499,(0,2):C.GC_4330,(0,6):C.GC_3499,(0,7):C.GC_3503,(0,4):C.GC_3500,(0,5):C.GC_4330,(0,94):C.GC_3497,(0,93):C.GC_4335,(0,97):C.GC_3498,(0,98):C.GC_3888,(0,100):C.GC_3889,(0,95):C.GC_4335,(0,96):C.GC_3891,(0,102):C.GC_4329,(0,101):C.GC_4334,(0,106):C.GC_3902,(0,107):C.GC_3502,(0,108):C.GC_4322,(0,104):C.GC_4325,(0,105):C.GC_3887,(0,111):C.GC_3902,(0,112):C.GC_4322,(0,110):C.GC_4325,(0,115):C.GC_4329,(0,116):C.GC_3502,(0,113):C.GC_4334,(0,114):C.GC_3887,(0,18):C.GC_3498,(0,19):C.GC_3502,(0,9):C.GC_7036,(0,30):C.GC_3496,(0,31):C.GC_3500,(0,20):C.GC_7037,(0,41):C.GC_3498,(0,42):C.GC_3502,(0,32):C.GC_7036,(0,53):C.GC_3496,(0,54):C.GC_3500,(0,43):C.GC_7037,(0,64):C.GC_4328,(0,65):C.GC_4328,(0,55):C.GC_7038,(0,77):C.GC_4330,(0,78):C.GC_4330,(0,66):C.GC_7039,(0,11):C.GC_4325,(0,22):C.GC_4324,(0,33):C.GC_4335,(0,44):C.GC_4333,(0,56):C.GC_4334,(0,67):C.GC_4332,(0,12):C.GC_4335,(0,23):C.GC_4333,(0,34):C.GC_4325,(0,45):C.GC_4324,(0,58):C.GC_4334,(0,69):C.GC_4332,(0,81):C.GC_3496,(0,84):C.GC_3499,(0,14):C.GC_4334,(0,38):C.GC_4334,(0,60):C.GC_4333,(0,61):C.GC_4333,(0,120):C.GC_3498,(0,123):C.GC_3497,(0,25):C.GC_4332,(0,49):C.GC_4332,(0,71):C.GC_4335,(0,72):C.GC_4335,(0,13):C.GC_3887,(0,24):C.GC_3886,(0,35):C.GC_3887,(0,46):C.GC_3886,(0,59):C.GC_3891,(0,70):C.GC_3890,(0,80):C.GC_4327,(0,85):C.GC_3500,(0,15):C.GC_4335,(0,37):C.GC_4332,(0,39):C.GC_3886,(0,62):C.GC_3887,(0,119):C.GC_4329,(0,125):C.GC_3502,(0,26):C.GC_4333,(0,48):C.GC_4334,(0,50):C.GC_3887,(0,73):C.GC_3886,(0,82):C.GC_4330,(0,83):C.GC_3503,(0,16):C.GC_4332,(0,17):C.GC_3886,(0,40):C.GC_4335,(0,63):C.GC_3887,(0,121):C.GC_4328,(0,122):C.GC_3501,(0,27):C.GC_4334,(0,28):C.GC_3887,(0,51):C.GC_4333,(0,74):C.GC_3886})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS10, L.VVVSS11, L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS125, L.VVVSS126, L.VVVSS129, L.VVVSS130, L.VVVSS131, L.VVVSS132, L.VVVSS135, L.VVVSS136, L.VVVSS137, L.VVVSS138, L.VVVSS146, L.VVVSS147, L.VVVSS148, L.VVVSS149, L.VVVSS15, L.VVVSS150, L.VVVSS151, L.VVVSS152, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS158, L.VVVSS159, L.VVVSS162, L.VVVSS163, L.VVVSS164, L.VVVSS165, L.VVVSS178, L.VVVSS179, L.VVVSS18, L.VVVSS180, L.VVVSS181, L.VVVSS182, L.VVVSS183, L.VVVSS184, L.VVVSS185, L.VVVSS188, L.VVVSS189, L.VVVSS19, L.VVVSS190, L.VVVSS191, L.VVVSS194, L.VVVSS195, L.VVVSS196, L.VVVSS197, L.VVVSS3, L.VVVSS34, L.VVVSS36, L.VVVSS37, L.VVVSS4, L.VVVSS48, L.VVVSS50, L.VVVSS51, L.VVVSS62, L.VVVSS65, L.VVVSS66, L.VVVSS8 ],
               couplings = {(0,0):C.GC_4380,(0,54):C.GC_4380,(0,58):C.GC_4153,(0,65):C.GC_4380,(0,1):C.GC_4376,(0,2):C.GC_4164,(0,23):C.GC_4376,(0,38):C.GC_4380,(0,47):C.GC_4164,(0,55):C.GC_4381,(0,56):C.GC_4381,(0,57):C.GC_4154,(0,59):C.GC_4381,(0,60):C.GC_4377,(0,61):C.GC_4163,(0,62):C.GC_4377,(0,63):C.GC_4381,(0,64):C.GC_4163,(0,3):C.GC_7064,(0,11):C.GC_7065,(0,19):C.GC_7064,(0,28):C.GC_7065,(0,36):C.GC_7058,(0,45):C.GC_7059,(0,4):C.GC_4377,(0,12):C.GC_4376,(0,20):C.GC_4381,(0,29):C.GC_4380,(0,37):C.GC_4381,(0,46):C.GC_4380,(0,5):C.GC_4381,(0,13):C.GC_4380,(0,21):C.GC_4377,(0,30):C.GC_4376,(0,39):C.GC_4381,(0,48):C.GC_4380,(0,7):C.GC_4381,(0,25):C.GC_4381,(0,41):C.GC_4380,(0,42):C.GC_4380,(0,15):C.GC_4380,(0,33):C.GC_4380,(0,50):C.GC_4381,(0,51):C.GC_4381,(0,6):C.GC_4163,(0,14):C.GC_4164,(0,22):C.GC_4163,(0,31):C.GC_4164,(0,40):C.GC_4154,(0,49):C.GC_4153,(0,8):C.GC_4381,(0,24):C.GC_4380,(0,26):C.GC_4164,(0,43):C.GC_4163,(0,16):C.GC_4380,(0,32):C.GC_4381,(0,34):C.GC_4163,(0,52):C.GC_4164,(0,9):C.GC_4380,(0,10):C.GC_4164,(0,27):C.GC_4381,(0,44):C.GC_4163,(0,17):C.GC_4381,(0,18):C.GC_4163,(0,35):C.GC_4380,(0,53):C.GC_4164})

V_351 = Vertex(name = 'V_351',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS100, L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS11, L.VVVVS110, L.VVVVS112, L.VVVVS113, L.VVVVS114, L.VVVVS115, L.VVVVS116, L.VVVVS118, L.VVVVS119, L.VVVVS12, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS123, L.VVVVS124, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS13, L.VVVVS130, L.VVVVS131, L.VVVVS134, L.VVVVS14, L.VVVVS141, L.VVVVS142, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS146, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS15, L.VVVVS150, L.VVVVS151, L.VVVVS152, L.VVVVS153, L.VVVVS154, L.VVVVS156, L.VVVVS158, L.VVVVS159, L.VVVVS16, L.VVVVS162, L.VVVVS163, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS17, L.VVVVS170, L.VVVVS171, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS18, L.VVVVS180, L.VVVVS181, L.VVVVS182, L.VVVVS183, L.VVVVS184, L.VVVVS185, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS19, L.VVVVS190, L.VVVVS191, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS197, L.VVVVS2, L.VVVVS20, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS21, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS23, L.VVVVS233, L.VVVVS234, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS239, L.VVVVS24, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS244, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS250, L.VVVVS251, L.VVVVS252, L.VVVVS253, L.VVVVS254, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS27, L.VVVVS28, L.VVVVS3, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS35, L.VVVVS36, L.VVVVS37, L.VVVVS39, L.VVVVS4, L.VVVVS40, L.VVVVS5, L.VVVVS50, L.VVVVS51, L.VVVVS59, L.VVVVS6, L.VVVVS60, L.VVVVS63, L.VVVVS64, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS69, L.VVVVS7, L.VVVVS70, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS74, L.VVVVS75, L.VVVVS76, L.VVVVS77, L.VVVVS78, L.VVVVS8, L.VVVVS81, L.VVVVS88, L.VVVVS89, L.VVVVS9, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS93, L.VVVVS94, L.VVVVS95, L.VVVVS96, L.VVVVS97, L.VVVVS99 ],
               couplings = {(0,130):C.GC_6639,(0,138):C.GC_6639,(0,0):C.GC_6637,(0,82):C.GC_6637,(0,167):C.GC_5680,(0,1):C.GC_5678,(0,8):C.GC_6233,(0,17):C.GC_6230,(0,140):C.GC_6502,(0,144):C.GC_6501,(0,153):C.GC_6500,(0,163):C.GC_6504,(0,75):C.GC_5677,(0,83):C.GC_5678,(0,94):C.GC_6236,(0,97):C.GC_6230,(0,98):C.GC_5461,(0,105):C.GC_5462,(0,26):C.GC_6509,(0,30):C.GC_5464,(0,40):C.GC_6498,(0,49):C.GC_5463,(0,58):C.GC_6500,(0,64):C.GC_6504,(0,141):C.GC_6239,(0,142):C.GC_6239,(0,143):C.GC_6504,(0,146):C.GC_6504,(0,128):C.GC_6236,(0,129):C.GC_6233,(0,131):C.GC_6233,(0,132):C.GC_6236,(0,133):C.GC_6234,(0,134):C.GC_6502,(0,135):C.GC_6486,(0,136):C.GC_6234,(0,137):C.GC_6486,(0,139):C.GC_6502,(0,148):C.GC_6515,(0,149):C.GC_6515,(0,152):C.GC_5677,(0,154):C.GC_6236,(0,150):C.GC_6495,(0,151):C.GC_6513,(0,158):C.GC_5680,(0,159):C.GC_6233,(0,160):C.GC_6198,(0,161):C.GC_6197,(0,155):C.GC_6495,(0,156):C.GC_6513,(0,157):C.GC_6199,(0,162):C.GC_6222,(0,164):C.GC_6222,(0,166):C.GC_6640,(0,165):C.GC_6510,(0,171):C.GC_6502,(0,168):C.GC_6494,(0,169):C.GC_6512,(0,170):C.GC_6496,(0,175):C.GC_5679,(0,176):C.GC_5461,(0,2):C.GC_6486,(0,172):C.GC_6497,(0,173):C.GC_6490,(0,174):C.GC_6195,(0,7):C.GC_6232,(0,9):C.GC_6238,(0,3):C.GC_6517,(0,4):C.GC_6225,(0,5):C.GC_6492,(0,6):C.GC_6518,(0,11):C.GC_6640,(0,10):C.GC_6510,(0,14):C.GC_5679,(0,15):C.GC_6486,(0,12):C.GC_6497,(0,13):C.GC_6490,(0,21):C.GC_6502,(0,22):C.GC_5461,(0,16):C.GC_6494,(0,18):C.GC_6512,(0,19):C.GC_6496,(0,20):C.GC_6195,(0,28):C.GC_6232,(0,29):C.GC_6238,(0,23):C.GC_6517,(0,24):C.GC_6225,(0,25):C.GC_6518,(0,27):C.GC_6492,(0,32):C.GC_6637,(0,31):C.GC_6510,(0,36):C.GC_6501,(0,33):C.GC_6497,(0,34):C.GC_6518,(0,35):C.GC_6517,(0,41):C.GC_6208,(0,42):C.GC_6230,(0,43):C.GC_5462,(0,44):C.GC_6210,(0,37):C.GC_6217,(0,38):C.GC_6512,(0,39):C.GC_6195,(0,50):C.GC_6238,(0,51):C.GC_6230,(0,45):C.GC_6227,(0,46):C.GC_6513,(0,47):C.GC_6490,(0,48):C.GC_6512,(0,52):C.GC_7146,(0,65):C.GC_6637,(0,63):C.GC_6510,(0,68):C.GC_6208,(0,69):C.GC_6230,(0,70):C.GC_6210,(0,66):C.GC_6217,(0,67):C.GC_6512,(0,76):C.GC_6501,(0,77):C.GC_5462,(0,71):C.GC_6497,(0,72):C.GC_6518,(0,73):C.GC_6517,(0,74):C.GC_6195,(0,84):C.GC_6238,(0,85):C.GC_6230,(0,78):C.GC_6227,(0,79):C.GC_6513,(0,80):C.GC_6512,(0,81):C.GC_6490,(0,86):C.GC_7146,(0,100):C.GC_6489,(0,99):C.GC_6491,(0,103):C.GC_6499,(0,104):C.GC_6507,(0,101):C.GC_6495,(0,102):C.GC_6513,(0,110):C.GC_6499,(0,111):C.GC_6507,(0,106):C.GC_6495,(0,107):C.GC_6196,(0,108):C.GC_6513,(0,109):C.GC_6196,(0,117):C.GC_6507,(0,118):C.GC_6507,(0,119):C.GC_6240,(0,112):C.GC_6218,(0,113):C.GC_6517,(0,114):C.GC_6517,(0,115):C.GC_6513,(0,116):C.GC_6513,(0,120):C.GC_7148,(0,53):C.GC_6515,(0,87):C.GC_6515,(0,121):C.GC_6493,(0,54):C.GC_6494,(0,88):C.GC_6215,(0,122):C.GC_6496,(0,56):C.GC_6215,(0,90):C.GC_6494,(0,124):C.GC_6496,(0,60):C.GC_6220,(0,93):C.GC_6220,(0,127):C.GC_6229,(0,55):C.GC_6492,(0,89):C.GC_6518,(0,123):C.GC_6517,(0,57):C.GC_6518,(0,91):C.GC_6492,(0,125):C.GC_6517,(0,59):C.GC_6196,(0,92):C.GC_6196,(0,126):C.GC_6200,(0,145):C.GC_6509,(0,61):C.GC_6512,(0,95):C.GC_6518,(0,147):C.GC_6502,(0,62):C.GC_6518,(0,96):C.GC_6512})

V_352 = Vertex(name = 'V_352',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS112, L.VVVVS114, L.VVVVS115, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS130, L.VVVVS141, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS154, L.VVVVS156, L.VVVVS158, L.VVVVS159, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS170, L.VVVVS171, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS181, L.VVVVS182, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS197, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS236, L.VVVVS237, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS78, L.VVVVS81, L.VVVVS88, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS94, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,77):C.GC_6575,(0,78):C.GC_6575,(0,79):C.GC_6374,(0,80):C.GC_6574,(0,81):C.GC_6374,(0,82):C.GC_6574,(0,83):C.GC_6338,(0,84):C.GC_6372,(0,85):C.GC_6372,(0,86):C.GC_6572,(0,87):C.GC_6370,(0,88):C.GC_6573,(0,89):C.GC_6370,(0,90):C.GC_6374,(0,91):C.GC_6564,(0,92):C.GC_6345,(0,0):C.GC_6576,(0,1):C.GC_6367,(0,2):C.GC_6566,(0,3):C.GC_6577,(0,4):C.GC_6572,(0,5):C.GC_6374,(0,6):C.GC_6564,(0,7):C.GC_6370,(0,8):C.GC_6573,(0,9):C.GC_6370,(0,10):C.GC_6345,(0,11):C.GC_6576,(0,12):C.GC_6367,(0,13):C.GC_6577,(0,14):C.GC_6566,(0,15):C.GC_6572,(0,16):C.GC_6374,(0,17):C.GC_6577,(0,18):C.GC_6576,(0,19):C.GC_6339,(0,20):C.GC_6573,(0,21):C.GC_6345,(0,22):C.GC_6368,(0,23):C.GC_6574,(0,24):C.GC_6564,(0,25):C.GC_6573,(0,26):C.GC_7154,(0,36):C.GC_6572,(0,37):C.GC_6339,(0,38):C.GC_6573,(0,39):C.GC_6374,(0,40):C.GC_6577,(0,41):C.GC_6576,(0,42):C.GC_6345,(0,43):C.GC_6368,(0,44):C.GC_6574,(0,45):C.GC_6573,(0,46):C.GC_6564,(0,47):C.GC_7154,(0,57):C.GC_6565,(0,58):C.GC_6374,(0,59):C.GC_6574,(0,60):C.GC_6374,(0,61):C.GC_6344,(0,62):C.GC_6574,(0,63):C.GC_6344,(0,64):C.GC_6375,(0,65):C.GC_6576,(0,66):C.GC_6576,(0,67):C.GC_6574,(0,68):C.GC_6574,(0,69):C.GC_7151,(0,27):C.GC_6575,(0,48):C.GC_6575,(0,70):C.GC_6567,(0,28):C.GC_6370,(0,49):C.GC_6341,(0,71):C.GC_6370,(0,30):C.GC_6341,(0,51):C.GC_6370,(0,73):C.GC_6370,(0,33):C.GC_6371,(0,54):C.GC_6371,(0,76):C.GC_6366,(0,29):C.GC_6566,(0,50):C.GC_6577,(0,72):C.GC_6576,(0,31):C.GC_6577,(0,52):C.GC_6566,(0,74):C.GC_6576,(0,32):C.GC_6344,(0,53):C.GC_6344,(0,75):C.GC_6340,(0,34):C.GC_6573,(0,55):C.GC_6577,(0,35):C.GC_6577,(0,56):C.GC_6573})

V_353 = Vertex(name = 'V_353',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS100, L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS11, L.VVVVS110, L.VVVVS112, L.VVVVS113, L.VVVVS114, L.VVVVS115, L.VVVVS116, L.VVVVS118, L.VVVVS119, L.VVVVS12, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS123, L.VVVVS124, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS13, L.VVVVS130, L.VVVVS131, L.VVVVS134, L.VVVVS14, L.VVVVS141, L.VVVVS142, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS146, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS15, L.VVVVS150, L.VVVVS151, L.VVVVS152, L.VVVVS153, L.VVVVS154, L.VVVVS156, L.VVVVS158, L.VVVVS159, L.VVVVS16, L.VVVVS162, L.VVVVS163, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS17, L.VVVVS170, L.VVVVS171, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS18, L.VVVVS180, L.VVVVS181, L.VVVVS182, L.VVVVS183, L.VVVVS184, L.VVVVS185, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS19, L.VVVVS190, L.VVVVS191, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS197, L.VVVVS2, L.VVVVS20, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS21, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS23, L.VVVVS233, L.VVVVS234, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS239, L.VVVVS24, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS244, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS250, L.VVVVS251, L.VVVVS252, L.VVVVS253, L.VVVVS254, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS27, L.VVVVS28, L.VVVVS3, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS35, L.VVVVS36, L.VVVVS37, L.VVVVS39, L.VVVVS4, L.VVVVS40, L.VVVVS5, L.VVVVS50, L.VVVVS51, L.VVVVS59, L.VVVVS6, L.VVVVS60, L.VVVVS63, L.VVVVS64, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS69, L.VVVVS7, L.VVVVS70, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS74, L.VVVVS75, L.VVVVS76, L.VVVVS77, L.VVVVS78, L.VVVVS8, L.VVVVS81, L.VVVVS88, L.VVVVS89, L.VVVVS9, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS93, L.VVVVS94, L.VVVVS95, L.VVVVS96, L.VVVVS97, L.VVVVS99 ],
               couplings = {(0,130):C.GC_6638,(0,138):C.GC_6638,(0,0):C.GC_6637,(0,82):C.GC_6637,(0,167):C.GC_5678,(0,1):C.GC_5680,(0,8):C.GC_6230,(0,17):C.GC_6233,(0,140):C.GC_6506,(0,144):C.GC_6500,(0,153):C.GC_6501,(0,163):C.GC_6508,(0,75):C.GC_5679,(0,83):C.GC_5680,(0,94):C.GC_6238,(0,97):C.GC_6233,(0,98):C.GC_5463,(0,105):C.GC_5464,(0,26):C.GC_6505,(0,30):C.GC_5462,(0,40):C.GC_6499,(0,49):C.GC_5461,(0,58):C.GC_6501,(0,64):C.GC_6508,(0,141):C.GC_6237,(0,142):C.GC_6237,(0,143):C.GC_6508,(0,146):C.GC_6508,(0,128):C.GC_6238,(0,129):C.GC_6230,(0,131):C.GC_6230,(0,132):C.GC_6238,(0,133):C.GC_6231,(0,134):C.GC_6506,(0,135):C.GC_6488,(0,136):C.GC_6231,(0,137):C.GC_6488,(0,139):C.GC_6506,(0,148):C.GC_6510,(0,149):C.GC_6510,(0,152):C.GC_5679,(0,154):C.GC_6238,(0,150):C.GC_6494,(0,151):C.GC_6519,(0,158):C.GC_5678,(0,159):C.GC_6230,(0,160):C.GC_6197,(0,161):C.GC_6198,(0,155):C.GC_6494,(0,156):C.GC_6519,(0,157):C.GC_6200,(0,162):C.GC_6224,(0,164):C.GC_6224,(0,166):C.GC_6641,(0,165):C.GC_6515,(0,171):C.GC_6506,(0,168):C.GC_6495,(0,169):C.GC_6516,(0,170):C.GC_6497,(0,175):C.GC_5677,(0,176):C.GC_5463,(0,2):C.GC_6488,(0,172):C.GC_6496,(0,173):C.GC_6492,(0,174):C.GC_6196,(0,7):C.GC_6235,(0,9):C.GC_6236,(0,3):C.GC_6511,(0,4):C.GC_6223,(0,5):C.GC_6490,(0,6):C.GC_6514,(0,11):C.GC_6641,(0,10):C.GC_6515,(0,14):C.GC_5677,(0,15):C.GC_6488,(0,12):C.GC_6496,(0,13):C.GC_6492,(0,21):C.GC_6506,(0,22):C.GC_5463,(0,16):C.GC_6495,(0,18):C.GC_6516,(0,19):C.GC_6497,(0,20):C.GC_6196,(0,28):C.GC_6235,(0,29):C.GC_6236,(0,23):C.GC_6511,(0,24):C.GC_6223,(0,25):C.GC_6514,(0,27):C.GC_6490,(0,32):C.GC_6637,(0,31):C.GC_6515,(0,36):C.GC_6500,(0,33):C.GC_6496,(0,34):C.GC_6514,(0,35):C.GC_6511,(0,41):C.GC_6211,(0,42):C.GC_6233,(0,43):C.GC_5464,(0,44):C.GC_6207,(0,37):C.GC_6215,(0,38):C.GC_6516,(0,39):C.GC_6196,(0,50):C.GC_6236,(0,51):C.GC_6233,(0,45):C.GC_6221,(0,46):C.GC_6519,(0,47):C.GC_6492,(0,48):C.GC_6516,(0,52):C.GC_7147,(0,65):C.GC_6637,(0,63):C.GC_6515,(0,68):C.GC_6211,(0,69):C.GC_6233,(0,70):C.GC_6207,(0,66):C.GC_6215,(0,67):C.GC_6516,(0,76):C.GC_6500,(0,77):C.GC_5464,(0,71):C.GC_6496,(0,72):C.GC_6514,(0,73):C.GC_6511,(0,74):C.GC_6196,(0,84):C.GC_6236,(0,85):C.GC_6233,(0,78):C.GC_6221,(0,79):C.GC_6519,(0,80):C.GC_6516,(0,81):C.GC_6492,(0,86):C.GC_7147,(0,100):C.GC_6487,(0,99):C.GC_6493,(0,103):C.GC_6498,(0,104):C.GC_6503,(0,101):C.GC_6494,(0,102):C.GC_6519,(0,110):C.GC_6498,(0,111):C.GC_6503,(0,106):C.GC_6494,(0,107):C.GC_6195,(0,108):C.GC_6519,(0,109):C.GC_6195,(0,117):C.GC_6503,(0,118):C.GC_6503,(0,119):C.GC_6241,(0,112):C.GC_6228,(0,113):C.GC_6511,(0,114):C.GC_6511,(0,115):C.GC_6519,(0,116):C.GC_6519,(0,120):C.GC_7149,(0,53):C.GC_6510,(0,87):C.GC_6510,(0,121):C.GC_6491,(0,54):C.GC_6495,(0,88):C.GC_6217,(0,122):C.GC_6497,(0,56):C.GC_6217,(0,90):C.GC_6495,(0,124):C.GC_6497,(0,60):C.GC_6226,(0,93):C.GC_6226,(0,127):C.GC_6219,(0,55):C.GC_6490,(0,89):C.GC_6514,(0,123):C.GC_6511,(0,57):C.GC_6514,(0,91):C.GC_6490,(0,125):C.GC_6511,(0,59):C.GC_6195,(0,92):C.GC_6195,(0,126):C.GC_6199,(0,145):C.GC_6505,(0,61):C.GC_6516,(0,95):C.GC_6514,(0,147):C.GC_6506,(0,62):C.GC_6514,(0,96):C.GC_6516})

V_354 = Vertex(name = 'V_354',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS112, L.VVVVS114, L.VVVVS115, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS130, L.VVVVS141, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS154, L.VVVVS156, L.VVVVS158, L.VVVVS159, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS170, L.VVVVS171, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS181, L.VVVVS182, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS197, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS236, L.VVVVS237, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS78, L.VVVVS81, L.VVVVS88, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS94, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,77):C.GC_6572,(0,78):C.GC_6572,(0,79):C.GC_6370,(0,80):C.GC_6576,(0,81):C.GC_6370,(0,82):C.GC_6576,(0,83):C.GC_6340,(0,84):C.GC_6367,(0,85):C.GC_6367,(0,86):C.GC_6575,(0,87):C.GC_6374,(0,88):C.GC_6577,(0,89):C.GC_6374,(0,90):C.GC_6370,(0,91):C.GC_6566,(0,92):C.GC_6344,(0,0):C.GC_6574,(0,1):C.GC_6372,(0,2):C.GC_6564,(0,3):C.GC_6573,(0,4):C.GC_6575,(0,5):C.GC_6370,(0,6):C.GC_6566,(0,7):C.GC_6374,(0,8):C.GC_6577,(0,9):C.GC_6374,(0,10):C.GC_6344,(0,11):C.GC_6574,(0,12):C.GC_6372,(0,13):C.GC_6573,(0,14):C.GC_6564,(0,15):C.GC_6575,(0,16):C.GC_6370,(0,17):C.GC_6573,(0,18):C.GC_6574,(0,19):C.GC_6341,(0,20):C.GC_6577,(0,21):C.GC_6344,(0,22):C.GC_6371,(0,23):C.GC_6576,(0,24):C.GC_6566,(0,25):C.GC_6577,(0,26):C.GC_7155,(0,36):C.GC_6575,(0,37):C.GC_6341,(0,38):C.GC_6577,(0,39):C.GC_6370,(0,40):C.GC_6573,(0,41):C.GC_6574,(0,42):C.GC_6344,(0,43):C.GC_6371,(0,44):C.GC_6576,(0,45):C.GC_6577,(0,46):C.GC_6566,(0,47):C.GC_7155,(0,57):C.GC_6567,(0,58):C.GC_6370,(0,59):C.GC_6576,(0,60):C.GC_6370,(0,61):C.GC_6345,(0,62):C.GC_6576,(0,63):C.GC_6345,(0,64):C.GC_6366,(0,65):C.GC_6574,(0,66):C.GC_6574,(0,67):C.GC_6576,(0,68):C.GC_6576,(0,69):C.GC_7152,(0,27):C.GC_6572,(0,48):C.GC_6572,(0,70):C.GC_6565,(0,28):C.GC_6374,(0,49):C.GC_6339,(0,71):C.GC_6374,(0,30):C.GC_6339,(0,51):C.GC_6374,(0,73):C.GC_6374,(0,33):C.GC_6368,(0,54):C.GC_6368,(0,76):C.GC_6375,(0,29):C.GC_6564,(0,50):C.GC_6573,(0,72):C.GC_6574,(0,31):C.GC_6573,(0,52):C.GC_6564,(0,74):C.GC_6574,(0,32):C.GC_6345,(0,53):C.GC_6345,(0,75):C.GC_6338,(0,34):C.GC_6577,(0,55):C.GC_6573,(0,35):C.GC_6573,(0,56):C.GC_6577})

V_355 = Vertex(name = 'V_355',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS100, L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS105, L.VVVVS106, L.VVVVS107, L.VVVVS108, L.VVVVS109, L.VVVVS11, L.VVVVS110, L.VVVVS112, L.VVVVS113, L.VVVVS114, L.VVVVS115, L.VVVVS116, L.VVVVS118, L.VVVVS119, L.VVVVS12, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS123, L.VVVVS124, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS13, L.VVVVS130, L.VVVVS131, L.VVVVS132, L.VVVVS133, L.VVVVS134, L.VVVVS14, L.VVVVS141, L.VVVVS142, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS146, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS15, L.VVVVS151, L.VVVVS152, L.VVVVS153, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS158, L.VVVVS159, L.VVVVS16, L.VVVVS160, L.VVVVS161, L.VVVVS162, L.VVVVS163, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS17, L.VVVVS170, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS18, L.VVVVS180, L.VVVVS181, L.VVVVS182, L.VVVVS184, L.VVVVS185, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS19, L.VVVVS190, L.VVVVS191, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS197, L.VVVVS198, L.VVVVS199, L.VVVVS2, L.VVVVS20, L.VVVVS200, L.VVVVS201, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS21, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS22, L.VVVVS23, L.VVVVS233, L.VVVVS234, L.VVVVS235, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS239, L.VVVVS24, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS244, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS252, L.VVVVS253, L.VVVVS254, L.VVVVS255, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS27, L.VVVVS28, L.VVVVS3, L.VVVVS31, L.VVVVS32, L.VVVVS33, L.VVVVS34, L.VVVVS35, L.VVVVS36, L.VVVVS37, L.VVVVS38, L.VVVVS39, L.VVVVS4, L.VVVVS40, L.VVVVS5, L.VVVVS50, L.VVVVS51, L.VVVVS54, L.VVVVS55, L.VVVVS57, L.VVVVS58, L.VVVVS59, L.VVVVS6, L.VVVVS60, L.VVVVS61, L.VVVVS62, L.VVVVS63, L.VVVVS64, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS69, L.VVVVS7, L.VVVVS70, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS74, L.VVVVS75, L.VVVVS76, L.VVVVS77, L.VVVVS78, L.VVVVS79, L.VVVVS8, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS86, L.VVVVS87, L.VVVVS88, L.VVVVS89, L.VVVVS9, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS93, L.VVVVS94, L.VVVVS95, L.VVVVS96, L.VVVVS97, L.VVVVS99 ],
               couplings = {(0,148):C.GC_6466,(0,158):C.GC_6466,(0,0):C.GC_6466,(0,93):C.GC_6466,(0,199):C.GC_5671,(0,1):C.GC_5674,(0,11):C.GC_5674,(0,20):C.GC_5676,(0,160):C.GC_6264,(0,168):C.GC_6261,(0,179):C.GC_6258,(0,190):C.GC_6262,(0,83):C.GC_5676,(0,94):C.GC_5674,(0,105):C.GC_5673,(0,109):C.GC_5676,(0,110):C.GC_6011,(0,118):C.GC_6009,(0,30):C.GC_6257,(0,36):C.GC_6005,(0,46):C.GC_6260,(0,55):C.GC_6007,(0,66):C.GC_6258,(0,73):C.GC_6262,(0,161):C.GC_5662,(0,162):C.GC_5662,(0,163):C.GC_5663,(0,164):C.GC_5663,(0,165):C.GC_6012,(0,166):C.GC_6010,(0,167):C.GC_6254,(0,170):C.GC_6006,(0,171):C.GC_6008,(0,172):C.GC_6254,(0,146):C.GC_6002,(0,147):C.GC_5998,(0,149):C.GC_6001,(0,150):C.GC_5999,(0,151):C.GC_5662,(0,152):C.GC_5663,(0,153):C.GC_6256,(0,154):C.GC_4812,(0,155):C.GC_5662,(0,156):C.GC_5663,(0,157):C.GC_4812,(0,159):C.GC_6256,(0,174):C.GC_6461,(0,175):C.GC_6461,(0,178):C.GC_5676,(0,180):C.GC_5673,(0,176):C.GC_6272,(0,177):C.GC_6270,(0,184):C.GC_5671,(0,185):C.GC_5674,(0,186):C.GC_6000,(0,187):C.GC_5997,(0,181):C.GC_6272,(0,182):C.GC_6270,(0,183):C.GC_6003,(0,195):C.GC_4810,(0,196):C.GC_4809,(0,188):C.GC_5668,(0,189):C.GC_5668,(0,191):C.GC_6016,(0,192):C.GC_5668,(0,193):C.GC_5668,(0,194):C.GC_6016,(0,198):C.GC_6465,(0,197):C.GC_6462,(0,203):C.GC_6264,(0,200):C.GC_6268,(0,201):C.GC_6271,(0,202):C.GC_6265,(0,207):C.GC_5673,(0,208):C.GC_6011,(0,2):C.GC_6242,(0,204):C.GC_6269,(0,205):C.GC_6244,(0,206):C.GC_6013,(0,8):C.GC_5663,(0,9):C.GC_6012,(0,10):C.GC_5662,(0,12):C.GC_5672,(0,3):C.GC_5667,(0,4):C.GC_6252,(0,5):C.GC_5667,(0,6):C.GC_5023,(0,7):C.GC_6245,(0,14):C.GC_6465,(0,13):C.GC_6462,(0,17):C.GC_5673,(0,18):C.GC_6242,(0,15):C.GC_6269,(0,16):C.GC_6244,(0,24):C.GC_6264,(0,25):C.GC_6011,(0,19):C.GC_6268,(0,21):C.GC_6271,(0,22):C.GC_6265,(0,23):C.GC_6013,(0,32):C.GC_5663,(0,33):C.GC_6012,(0,34):C.GC_5662,(0,35):C.GC_5672,(0,26):C.GC_5667,(0,27):C.GC_6252,(0,28):C.GC_5667,(0,29):C.GC_6245,(0,31):C.GC_5023,(0,38):C.GC_6466,(0,37):C.GC_6462,(0,42):C.GC_6261,(0,39):C.GC_6269,(0,40):C.GC_6266,(0,41):C.GC_6267,(0,47):C.GC_5676,(0,48):C.GC_6009,(0,49):C.GC_6242,(0,43):C.GC_6244,(0,44):C.GC_6271,(0,45):C.GC_6013,(0,56):C.GC_5663,(0,57):C.GC_6010,(0,58):C.GC_5662,(0,59):C.GC_5675,(0,50):C.GC_5667,(0,51):C.GC_6248,(0,52):C.GC_5667,(0,53):C.GC_5027,(0,54):C.GC_6249,(0,60):C.GC_7124,(0,74):C.GC_6466,(0,72):C.GC_6462,(0,77):C.GC_5676,(0,78):C.GC_6242,(0,75):C.GC_6244,(0,76):C.GC_6271,(0,84):C.GC_6261,(0,85):C.GC_6009,(0,79):C.GC_6269,(0,80):C.GC_6266,(0,81):C.GC_6267,(0,82):C.GC_6013,(0,91):C.GC_5663,(0,92):C.GC_6010,(0,95):C.GC_5662,(0,96):C.GC_5675,(0,86):C.GC_5667,(0,87):C.GC_6248,(0,88):C.GC_5667,(0,89):C.GC_6249,(0,90):C.GC_5027,(0,97):C.GC_7124,(0,112):C.GC_6459,(0,113):C.GC_6460,(0,111):C.GC_6464,(0,116):C.GC_6263,(0,117):C.GC_6259,(0,114):C.GC_6272,(0,115):C.GC_6270,(0,123):C.GC_6263,(0,124):C.GC_6259,(0,119):C.GC_6272,(0,120):C.GC_6015,(0,121):C.GC_6270,(0,122):C.GC_6015,(0,131):C.GC_6255,(0,132):C.GC_6255,(0,133):C.GC_5665,(0,134):C.GC_5664,(0,125):C.GC_5670,(0,126):C.GC_6250,(0,127):C.GC_6250,(0,128):C.GC_5670,(0,129):C.GC_6246,(0,130):C.GC_6246,(0,135):C.GC_7125,(0,61):C.GC_6461,(0,98):C.GC_6461,(0,136):C.GC_6463,(0,62):C.GC_6268,(0,99):C.GC_6243,(0,137):C.GC_6265,(0,64):C.GC_6243,(0,101):C.GC_6268,(0,139):C.GC_6265,(0,68):C.GC_5668,(0,104):C.GC_5668,(0,142):C.GC_5669,(0,63):C.GC_6243,(0,100):C.GC_6266,(0,138):C.GC_6267,(0,65):C.GC_6266,(0,102):C.GC_6243,(0,140):C.GC_6267,(0,69):C.GC_5668,(0,106):C.GC_5668,(0,143):C.GC_5669,(0,67):C.GC_6015,(0,103):C.GC_6015,(0,141):C.GC_6004,(0,169):C.GC_6253,(0,70):C.GC_6251,(0,107):C.GC_6247,(0,144):C.GC_6014,(0,173):C.GC_6256,(0,71):C.GC_6247,(0,108):C.GC_6251,(0,145):C.GC_6014})

V_356 = Vertex(name = 'V_356',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS104, L.VVVVS106, L.VVVVS112, L.VVVVS114, L.VVVVS115, L.VVVVS119, L.VVVVS120, L.VVVVS121, L.VVVVS122, L.VVVVS126, L.VVVVS127, L.VVVVS128, L.VVVVS129, L.VVVVS141, L.VVVVS143, L.VVVVS144, L.VVVVS145, L.VVVVS147, L.VVVVS148, L.VVVVS149, L.VVVVS154, L.VVVVS156, L.VVVVS157, L.VVVVS159, L.VVVVS164, L.VVVVS165, L.VVVVS166, L.VVVVS167, L.VVVVS168, L.VVVVS169, L.VVVVS170, L.VVVVS171, L.VVVVS172, L.VVVVS173, L.VVVVS174, L.VVVVS179, L.VVVVS181, L.VVVVS182, L.VVVVS186, L.VVVVS187, L.VVVVS188, L.VVVVS189, L.VVVVS192, L.VVVVS194, L.VVVVS195, L.VVVVS196, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS208, L.VVVVS209, L.VVVVS210, L.VVVVS211, L.VVVVS212, L.VVVVS233, L.VVVVS236, L.VVVVS237, L.VVVVS240, L.VVVVS241, L.VVVVS242, L.VVVVS243, L.VVVVS246, L.VVVVS247, L.VVVVS248, L.VVVVS249, L.VVVVS250, L.VVVVS251, L.VVVVS256, L.VVVVS257, L.VVVVS258, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS262, L.VVVVS263, L.VVVVS264, L.VVVVS265, L.VVVVS266, L.VVVVS65, L.VVVVS66, L.VVVVS67, L.VVVVS68, L.VVVVS71, L.VVVVS72, L.VVVVS73, L.VVVVS78, L.VVVVS79, L.VVVVS80, L.VVVVS81, L.VVVVS82, L.VVVVS83, L.VVVVS88, L.VVVVS90, L.VVVVS91, L.VVVVS92, L.VVVVS94, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,83):C.GC_6583,(0,84):C.GC_6583,(0,85):C.GC_6357,(0,86):C.GC_6357,(0,87):C.GC_6357,(0,88):C.GC_6357,(0,89):C.GC_6061,(0,90):C.GC_5770,(0,91):C.GC_5770,(0,92):C.GC_6084,(0,93):C.GC_5770,(0,94):C.GC_5770,(0,95):C.GC_6084,(0,96):C.GC_6584,(0,97):C.GC_6355,(0,98):C.GC_6358,(0,99):C.GC_6356,(0,100):C.GC_6358,(0,101):C.GC_6351,(0,102):C.GC_6081,(0,0):C.GC_5771,(0,1):C.GC_6080,(0,2):C.GC_5771,(0,3):C.GC_6077,(0,4):C.GC_6584,(0,5):C.GC_6358,(0,6):C.GC_6351,(0,7):C.GC_6355,(0,8):C.GC_6358,(0,9):C.GC_6356,(0,10):C.GC_6081,(0,11):C.GC_5771,(0,12):C.GC_6080,(0,13):C.GC_5771,(0,14):C.GC_6077,(0,15):C.GC_6584,(0,16):C.GC_6358,(0,17):C.GC_6355,(0,18):C.GC_6356,(0,19):C.GC_6351,(0,20):C.GC_6358,(0,21):C.GC_6081,(0,22):C.GC_5771,(0,23):C.GC_6080,(0,24):C.GC_5771,(0,25):C.GC_6077,(0,26):C.GC_7131,(0,37):C.GC_6584,(0,38):C.GC_6351,(0,39):C.GC_6358,(0,40):C.GC_6358,(0,41):C.GC_6355,(0,42):C.GC_6356,(0,43):C.GC_6081,(0,44):C.GC_5771,(0,45):C.GC_6080,(0,46):C.GC_5771,(0,47):C.GC_6077,(0,48):C.GC_7131,(0,59):C.GC_6555,(0,60):C.GC_6357,(0,61):C.GC_6357,(0,62):C.GC_6357,(0,63):C.GC_6083,(0,64):C.GC_6357,(0,65):C.GC_6083,(0,66):C.GC_5772,(0,67):C.GC_6078,(0,68):C.GC_6078,(0,69):C.GC_5772,(0,70):C.GC_6078,(0,71):C.GC_6078,(0,72):C.GC_7130,(0,27):C.GC_6583,(0,49):C.GC_6583,(0,73):C.GC_6554,(0,28):C.GC_6355,(0,50):C.GC_6350,(0,74):C.GC_6356,(0,30):C.GC_6350,(0,52):C.GC_6355,(0,76):C.GC_6356,(0,33):C.GC_5770,(0,55):C.GC_5770,(0,79):C.GC_5773,(0,29):C.GC_6350,(0,51):C.GC_6355,(0,75):C.GC_6356,(0,31):C.GC_6355,(0,53):C.GC_6350,(0,77):C.GC_6356,(0,34):C.GC_5770,(0,56):C.GC_5770,(0,80):C.GC_5773,(0,32):C.GC_6083,(0,54):C.GC_6083,(0,78):C.GC_6062,(0,35):C.GC_6079,(0,57):C.GC_6079,(0,81):C.GC_6082,(0,36):C.GC_6079,(0,58):C.GC_6079,(0,82):C.GC_6082})

V_357 = Vertex(name = 'V_357',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS207, L.VVVSS209, L.VVVSS217, L.VVVSS248, L.VVVSS84 ],
               couplings = {(0,3):C.GC_3899,(0,2):C.GC_4315,(0,4):C.GC_4318,(0,1):C.GC_4319,(0,0):C.GC_7073})

V_358 = Vertex(name = 'V_358',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS207, L.VVVSS209, L.VVVSS217 ],
               couplings = {(0,2):C.GC_4373,(0,1):C.GC_4369,(0,0):C.GC_7076})

V_359 = Vertex(name = 'V_359',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS206, L.VVVSS209, L.VVVSS217, L.VVVSS240, L.VVVSS248, L.VVVSS84 ],
               couplings = {(0,3):C.GC_3895,(0,4):C.GC_3898,(0,2):C.GC_4316,(0,5):C.GC_4317,(0,1):C.GC_4320,(0,0):C.GC_7074})

V_360 = Vertex(name = 'V_360',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS206, L.VVVSS209, L.VVVSS217 ],
               couplings = {(0,2):C.GC_4372,(0,1):C.GC_4370,(0,0):C.GC_7077})

V_361 = Vertex(name = 'V_361',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS137, L.VVVVS278, L.VVVVS279, L.VVVVS285, L.VVVVS286, L.VVVVS292, L.VVVVS300, L.VVVVS303, L.VVVVS304, L.VVVVS307, L.VVVVS308, L.VVVVS309, L.VVVVS320, L.VVVVS325, L.VVVVS332, L.VVVVS333, L.VVVVS337, L.VVVVS339, L.VVVVS362, L.VVVVS365, L.VVVVS366, L.VVVVS367, L.VVVVS45 ],
               couplings = {(0,11):C.GC_4814,(0,4):C.GC_5254,(0,8):C.GC_5049,(0,3):C.GC_5283,(0,6):C.GC_5197,(0,9):C.GC_5681,(0,10):C.GC_4522,(0,7):C.GC_6204,(0,2):C.GC_5042,(0,22):C.GC_5193,(0,20):C.GC_5053,(0,14):C.GC_5284,(0,15):C.GC_6481,(0,21):C.GC_4594,(0,0):C.GC_6482,(0,16):C.GC_6485,(0,17):C.GC_5047,(0,19):C.GC_6202,(0,5):C.GC_5195,(0,18):C.GC_5201,(0,1):C.GC_5279,(0,13):C.GC_5281,(0,12):C.GC_7157})

V_362 = Vertex(name = 'V_362',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS292, L.VVVVS320, L.VVVVS325, L.VVVVS332, L.VVVVS333, L.VVVVS337, L.VVVVS339, L.VVVVS362, L.VVVVS365, L.VVVVS366 ],
               couplings = {(0,9):C.GC_5149,(0,3):C.GC_5294,(0,4):C.GC_6560,(0,5):C.GC_6559,(0,6):C.GC_5139,(0,8):C.GC_4934,(0,0):C.GC_5229,(0,7):C.GC_5234,(0,2):C.GC_5292,(0,1):C.GC_7159})

V_363 = Vertex(name = 'V_363',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS137, L.VVVVS278, L.VVVVS279, L.VVVVS285, L.VVVVS286, L.VVVVS292, L.VVVVS300, L.VVVVS303, L.VVVVS304, L.VVVVS307, L.VVVVS308, L.VVVVS309, L.VVVVS320, L.VVVVS325, L.VVVVS332, L.VVVVS333, L.VVVVS337, L.VVVVS339, L.VVVVS362, L.VVVVS365, L.VVVVS366, L.VVVVS367, L.VVVVS45 ],
               couplings = {(0,11):C.GC_4814,(0,4):C.GC_5254,(0,8):C.GC_5050,(0,3):C.GC_5282,(0,6):C.GC_5197,(0,9):C.GC_5682,(0,10):C.GC_4522,(0,7):C.GC_6205,(0,2):C.GC_5043,(0,22):C.GC_5194,(0,20):C.GC_5052,(0,14):C.GC_5285,(0,15):C.GC_6480,(0,21):C.GC_4593,(0,0):C.GC_6483,(0,16):C.GC_6484,(0,17):C.GC_5044,(0,19):C.GC_6203,(0,5):C.GC_5196,(0,18):C.GC_5202,(0,1):C.GC_5278,(0,13):C.GC_5280,(0,12):C.GC_7156})

V_364 = Vertex(name = 'V_364',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS292, L.VVVVS320, L.VVVVS325, L.VVVVS332, L.VVVVS333, L.VVVVS337, L.VVVVS339, L.VVVVS362, L.VVVVS365, L.VVVVS366 ],
               couplings = {(0,9):C.GC_5148,(0,3):C.GC_5295,(0,4):C.GC_6561,(0,5):C.GC_6558,(0,6):C.GC_5136,(0,8):C.GC_4933,(0,0):C.GC_5230,(0,7):C.GC_5235,(0,2):C.GC_5291,(0,1):C.GC_7158})

V_365 = Vertex(name = 'V_365',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS276, L.VVVVS290, L.VVVVS320, L.VVVVS336, L.VVVVS338 ],
               couplings = {(0,1):C.GC_6642,(0,3):C.GC_6669,(0,0):C.GC_6670,(0,4):C.GC_6671,(0,2):C.GC_7162})

V_366 = Vertex(name = 'V_366',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS320, L.VVVVS336, L.VVVVS338 ],
               couplings = {(0,1):C.GC_6682,(0,2):C.GC_6681,(0,0):C.GC_7163})

V_367 = Vertex(name = 'V_367',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS209, L.VVVSS217, L.VVVSS240, L.VVVSS248, L.VVVSS84 ],
               couplings = {(0,2):C.GC_2813,(0,3):C.GC_2816,(0,1):C.GC_3905,(0,4):C.GC_3903,(0,0):C.GC_3906})

V_368 = Vertex(name = 'V_368',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS209, L.VVVSS217 ],
               couplings = {(0,1):C.GC_4214,(0,0):C.GC_4144})

V_369 = Vertex(name = 'V_369',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS208, L.VVVSS209, L.VVVSS210, L.VVVSS216, L.VVVSS217, L.VVVSS218, L.VVVSS233, L.VVVSS238, L.VVVSS239, L.VVVSS252, L.VVVSS79, L.VVVSS80, L.VVVSS81, L.VVVSS82 ],
               couplings = {(0,7):C.GC_131,(0,8):C.GC_132,(0,9):C.GC_3051,(0,10):C.GC_3052,(0,5):C.GC_3900,(0,3):C.GC_4339,(0,6):C.GC_3505,(0,12):C.GC_130,(0,13):C.GC_3504,(0,11):C.GC_3050,(0,4):C.GC_3893,(0,2):C.GC_3892,(0,1):C.GC_3506,(0,14):C.GC_4336,(0,0):C.GC_4341})

V_370 = Vertex(name = 'V_370',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS208, L.VVVSS209, L.VVVSS210, L.VVVSS217, L.VVVSS218 ],
               couplings = {(0,4):C.GC_4188,(0,3):C.GC_4384,(0,5):C.GC_3726,(0,2):C.GC_4173,(0,1):C.GC_3655,(0,0):C.GC_4367})

V_371 = Vertex(name = 'V_371',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS102, L.VVVSS145, L.VVVSS204, L.VVVSS205, L.VVVSS210, L.VVVSS219, L.VVVSS221, L.VVVSS222, L.VVVSS229, L.VVVSS232, L.VVVSS236, L.VVVSS82 ],
               couplings = {(0,10):C.GC_121,(0,9):C.GC_125,(0,2):C.GC_2804,(0,3):C.GC_2806,(0,7):C.GC_128,(0,4):C.GC_3422,(0,5):C.GC_3015,(0,0):C.GC_113,(0,6):C.GC_3428,(0,8):C.GC_119,(0,11):C.GC_3417,(0,1):C.GC_3425})

V_372 = Vertex(name = 'V_372',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210, L.VVVSS222, L.VVVSS229 ],
               couplings = {(0,2):C.GC_528,(0,1):C.GC_3639,(0,3):C.GC_514,(0,0):C.GC_3628})

V_373 = Vertex(name = 'V_373',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS145, L.VVVSS210, L.VVVSS220, L.VVVSS223, L.VVVSS224, L.VVVSS228, L.VVVSS234, L.VVVSS237, L.VVVSS245, L.VVVSS246, L.VVVSS82 ],
               couplings = {(0,8):C.GC_122,(0,7):C.GC_126,(0,4):C.GC_127,(0,2):C.GC_3420,(0,3):C.GC_3013,(0,0):C.GC_115,(0,11):C.GC_3419,(0,6):C.GC_117,(0,1):C.GC_3423,(0,9):C.GC_2803,(0,10):C.GC_2808,(0,5):C.GC_3426})

V_374 = Vertex(name = 'V_374',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210, L.VVVSS223, L.VVVSS228 ],
               couplings = {(0,2):C.GC_527,(0,1):C.GC_3641,(0,3):C.GC_512,(0,0):C.GC_3626})

V_375 = Vertex(name = 'V_375',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS274, L.VVVVS282, L.VVVVS283, L.VVVVS324, L.VVVVS329 ],
               couplings = {(0,1):C.GC_4513,(0,2):C.GC_4515,(0,4):C.GC_6213,(0,0):C.GC_6209,(0,3):C.GC_6214})

V_376 = Vertex(name = 'V_376',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS324, L.VVVVS329 ],
               couplings = {(0,1):C.GC_6373,(0,0):C.GC_6331})

V_377 = Vertex(name = 'V_377',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS176, L.VVVVS214, L.VVVVS220, L.VVVVS221, L.VVVVS228, L.VVVVS229, L.VVVVS230, L.VVVVS270, L.VVVVS272, L.VVVVS273, L.VVVVS288, L.VVVVS289, L.VVVVS311, L.VVVVS313, L.VVVVS322, L.VVVVS323, L.VVVVS327, L.VVVVS334, L.VVVVS335, L.VVVVS348, L.VVVVS349, L.VVVVS350, L.VVVVS351, L.VVVVS352, L.VVVVS354 ],
               couplings = {(0,3):C.GC_5050,(0,11):C.GC_5198,(0,13):C.GC_6520,(0,12):C.GC_6524,(0,2):C.GC_5048,(0,10):C.GC_5199,(0,9):C.GC_5043,(0,1):C.GC_5194,(0,18):C.GC_4507,(0,24):C.GC_5054,(0,4):C.GC_5250,(0,20):C.GC_5276,(0,19):C.GC_6523,(0,22):C.GC_4593,(0,23):C.GC_6201,(0,21):C.GC_5202,(0,17):C.GC_4518,(0,14):C.GC_5045,(0,6):C.GC_5195,(0,8):C.GC_4509,(0,0):C.GC_4517,(0,16):C.GC_4512,(0,5):C.GC_4520,(0,7):C.GC_5248,(0,15):C.GC_5253})

V_378 = Vertex(name = 'V_378',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS228, L.VVVVS229, L.VVVVS230, L.VVVVS322, L.VVVVS323, L.VVVVS327, L.VVVVS334, L.VVVVS335, L.VVVVS350, L.VVVVS354 ],
               couplings = {(0,7):C.GC_4580,(0,9):C.GC_5150,(0,0):C.GC_5271,(0,8):C.GC_5235,(0,6):C.GC_4572,(0,3):C.GC_5137,(0,2):C.GC_5229,(0,5):C.GC_4578,(0,1):C.GC_4563,(0,4):C.GC_5269})

V_379 = Vertex(name = 'V_379',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS274, L.VVVVS282, L.VVVVS283, L.VVVVS324, L.VVVVS329 ],
               couplings = {(0,1):C.GC_4513,(0,2):C.GC_4514,(0,4):C.GC_6212,(0,0):C.GC_6206,(0,3):C.GC_6216})

V_380 = Vertex(name = 'V_380',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS324, L.VVVVS329 ],
               couplings = {(0,1):C.GC_6369,(0,0):C.GC_6332})

V_381 = Vertex(name = 'V_381',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS102, L.VVVSS145, L.VVVSS204, L.VVVSS205, L.VVVSS210, L.VVVSS219, L.VVVSS221, L.VVVSS222, L.VVVSS229, L.VVVSS232, L.VVVSS236, L.VVVSS82 ],
               couplings = {(0,10):C.GC_121,(0,9):C.GC_124,(0,2):C.GC_2805,(0,3):C.GC_2806,(0,7):C.GC_129,(0,4):C.GC_3421,(0,5):C.GC_3014,(0,0):C.GC_114,(0,6):C.GC_3429,(0,8):C.GC_118,(0,11):C.GC_3418,(0,1):C.GC_3424})

V_382 = Vertex(name = 'V_382',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210, L.VVVSS222, L.VVVSS229 ],
               couplings = {(0,2):C.GC_529,(0,1):C.GC_3640,(0,3):C.GC_513,(0,0):C.GC_3627})

V_383 = Vertex(name = 'V_383',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS145, L.VVVSS210, L.VVVSS220, L.VVVSS223, L.VVVSS224, L.VVVSS228, L.VVVSS234, L.VVVSS237, L.VVVSS245, L.VVVSS246, L.VVVSS82 ],
               couplings = {(0,8):C.GC_123,(0,7):C.GC_126,(0,4):C.GC_127,(0,2):C.GC_3420,(0,3):C.GC_3013,(0,0):C.GC_115,(0,11):C.GC_3419,(0,6):C.GC_117,(0,1):C.GC_3423,(0,9):C.GC_2803,(0,10):C.GC_2807,(0,5):C.GC_3427})

V_384 = Vertex(name = 'V_384',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210, L.VVVSS223, L.VVVSS228 ],
               couplings = {(0,2):C.GC_527,(0,1):C.GC_3641,(0,3):C.GC_512,(0,0):C.GC_3626})

V_385 = Vertex(name = 'V_385',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS176, L.VVVVS214, L.VVVVS220, L.VVVVS221, L.VVVVS228, L.VVVVS229, L.VVVVS230, L.VVVVS270, L.VVVVS272, L.VVVVS273, L.VVVVS288, L.VVVVS289, L.VVVVS311, L.VVVVS313, L.VVVVS322, L.VVVVS323, L.VVVVS327, L.VVVVS334, L.VVVVS335, L.VVVVS348, L.VVVVS349, L.VVVVS350, L.VVVVS351, L.VVVVS352, L.VVVVS354 ],
               couplings = {(0,3):C.GC_5049,(0,11):C.GC_5198,(0,13):C.GC_6521,(0,12):C.GC_6524,(0,2):C.GC_5048,(0,10):C.GC_5200,(0,9):C.GC_5042,(0,1):C.GC_5193,(0,18):C.GC_4508,(0,24):C.GC_5051,(0,4):C.GC_5251,(0,20):C.GC_5277,(0,19):C.GC_6522,(0,22):C.GC_4594,(0,23):C.GC_6201,(0,21):C.GC_5201,(0,17):C.GC_4519,(0,14):C.GC_5046,(0,6):C.GC_5196,(0,8):C.GC_4510,(0,0):C.GC_4516,(0,16):C.GC_4511,(0,5):C.GC_4521,(0,7):C.GC_5249,(0,15):C.GC_5252})

V_386 = Vertex(name = 'V_386',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS228, L.VVVVS229, L.VVVVS230, L.VVVVS322, L.VVVVS323, L.VVVVS327, L.VVVVS334, L.VVVVS335, L.VVVVS350, L.VVVVS354 ],
               couplings = {(0,7):C.GC_4579,(0,9):C.GC_5147,(0,0):C.GC_5270,(0,8):C.GC_5234,(0,6):C.GC_4571,(0,3):C.GC_5138,(0,2):C.GC_5230,(0,5):C.GC_4577,(0,1):C.GC_4564,(0,4):C.GC_5268})

V_387 = Vertex(name = 'V_387',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS219, L.VVVVS223, L.VVVVS225, L.VVVVS228, L.VVVVS231, L.VVVVS270, L.VVVVS271, L.VVVVS316, L.VVVVS321, L.VVVVS323, L.VVVVS342, L.VVVVS343, L.VVVVS347 ],
               couplings = {(0,1):C.GC_5028,(0,0):C.GC_5032,(0,7):C.GC_4498,(0,2):C.GC_4502,(0,6):C.GC_5019,(0,3):C.GC_5656,(0,11):C.GC_4591,(0,12):C.GC_5035,(0,10):C.GC_4500,(0,8):C.GC_5021,(0,4):C.GC_5024,(0,5):C.GC_5657,(0,9):C.GC_5658})

V_388 = Vertex(name = 'V_388',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS228, L.VVVVS321, L.VVVVS323, L.VVVVS347 ],
               couplings = {(0,0):C.GC_5750,(0,3):C.GC_5146,(0,1):C.GC_5134,(0,2):C.GC_5749})

V_389 = Vertex(name = 'V_389',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS136, L.VVVVS140, L.VVVVS175, L.VVVVS178, L.VVVVS267, L.VVVVS269, L.VVVVS281, L.VVVVS297, L.VVVVS298, L.VVVVS305, L.VVVVS312, L.VVVVS315, L.VVVVS326, L.VVVVS328, L.VVVVS330, L.VVVVS331, L.VVVVS341, L.VVVVS346, L.VVVVS358, L.VVVVS359, L.VVVVS360, L.VVVVS364 ],
               couplings = {(0,8):C.GC_4491,(0,7):C.GC_4493,(0,1):C.GC_4803,(0,0):C.GC_4805,(0,11):C.GC_5036,(0,9):C.GC_5041,(0,10):C.GC_5207,(0,6):C.GC_5210,(0,4):C.GC_4798,(0,5):C.GC_4485,(0,18):C.GC_4490,(0,21):C.GC_4496,(0,15):C.GC_4802,(0,16):C.GC_4807,(0,19):C.GC_5039,(0,20):C.GC_5154,(0,17):C.GC_5208,(0,14):C.GC_6019,(0,12):C.GC_4800,(0,13):C.GC_4488,(0,2):C.GC_6018,(0,3):C.GC_6020})

V_390 = Vertex(name = 'V_390',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS178, L.VVVVS326, L.VVVVS328, L.VVVVS330, L.VVVVS341, L.VVVVS346, L.VVVVS364 ],
               couplings = {(0,6):C.GC_4589,(0,4):C.GC_4921,(0,5):C.GC_5239,(0,3):C.GC_6060,(0,1):C.GC_4914,(0,2):C.GC_4586,(0,0):C.GC_6059})

V_391 = Vertex(name = 'V_391',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210, L.VVVSS235, L.VVVSS82 ],
               couplings = {(0,2):C.GC_3897,(0,1):C.GC_4338,(0,3):C.GC_4337,(0,0):C.GC_4340})

V_392 = Vertex(name = 'V_392',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS145, L.VVVSS210 ],
               couplings = {(0,1):C.GC_4383,(0,0):C.GC_4366})

V_393 = Vertex(name = 'V_393',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172, L.VVVSS177, L.VVVSS211, L.VVVSS241, L.VVVSS242, L.VVVSS76, L.VVVSS77, L.VVVSS78, L.VVVSS83 ],
               couplings = {(0,1):C.GC_2253,(0,4):C.GC_2815,(0,3):C.GC_3182,(0,2):C.GC_4331,(0,8):C.GC_3904,(0,5):C.GC_2251,(0,7):C.GC_2812,(0,6):C.GC_3180,(0,0):C.GC_4323})

V_394 = Vertex(name = 'V_394',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172, L.VVVSS211 ],
               couplings = {(0,1):C.GC_4379,(0,0):C.GC_4375})

V_395 = Vertex(name = 'V_395',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS213, L.VVVVS228, L.VVVVS270, L.VVVVS323 ],
               couplings = {(0,0):C.GC_6643,(0,1):C.GC_6675,(0,2):C.GC_6674,(0,3):C.GC_6676})

V_396 = Vertex(name = 'V_396',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS228, L.VVVVS323 ],
               couplings = {(0,0):C.GC_6685,(0,1):C.GC_6680})

V_397 = Vertex(name = 'V_397',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS135, L.VVVVS268, L.VVVVS275, L.VVVVS277, L.VVVVS278, L.VVVVS280, L.VVVVS284, L.VVVVS285, L.VVVVS287, L.VVVVS325, L.VVVVS332 ],
               couplings = {(0,6):C.GC_4524,(0,0):C.GC_4816,(0,8):C.GC_5247,(0,7):C.GC_5298,(0,10):C.GC_6673,(0,3):C.GC_4523,(0,1):C.GC_4815,(0,2):C.GC_6644,(0,5):C.GC_5246,(0,4):C.GC_5297,(0,9):C.GC_6672})

V_398 = Vertex(name = 'V_398',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS325, L.VVVVS332 ],
               couplings = {(0,1):C.GC_6684,(0,0):C.GC_6683})

V_399 = Vertex(name = 'V_399',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS103, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS212, L.VVVSS213, L.VVVSS215, L.VVVSS226, L.VVVSS227, L.VVVSS230, L.VVVSS244, L.VVVSS251 ],
               couplings = {(0,11):C.GC_95,(0,12):C.GC_101,(0,3):C.GC_2221,(0,4):C.GC_2224,(0,5):C.GC_99,(0,9):C.GC_549,(0,7):C.GC_2219,(0,6):C.GC_2225,(0,0):C.GC_2212,(0,2):C.GC_2215,(0,8):C.GC_93,(0,1):C.GC_92,(0,10):C.GC_97})

V_400 = Vertex(name = 'V_400',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS173, L.VVVSS213, L.VVVSS226, L.VVVSS230 ],
               couplings = {(0,1):C.GC_2637,(0,0):C.GC_2610,(0,2):C.GC_474,(0,3):C.GC_453})

V_401 = Vertex(name = 'V_401',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172, L.VVVSS176, L.VVVSS177, L.VVVSS211, L.VVVSS214, L.VVVSS225, L.VVVSS243, L.VVVSS247, L.VVVSS76 ],
               couplings = {(0,6):C.GC_94,(0,7):C.GC_100,(0,1):C.GC_2222,(0,2):C.GC_2223,(0,5):C.GC_98,(0,4):C.GC_2220,(0,3):C.GC_2226,(0,8):C.GC_2211,(0,0):C.GC_2218})

V_402 = Vertex(name = 'V_402',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172, L.VVVSS211, L.VVVSS225 ],
               couplings = {(0,2):C.GC_550,(0,1):C.GC_2638,(0,0):C.GC_2613})

V_403 = Vertex(name = 'V_403',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS103, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS212, L.VVVSS213, L.VVVSS215, L.VVVSS226, L.VVVSS227, L.VVVSS230, L.VVVSS244, L.VVVSS251 ],
               couplings = {(0,11):C.GC_95,(0,12):C.GC_101,(0,3):C.GC_2221,(0,4):C.GC_2224,(0,5):C.GC_99,(0,9):C.GC_549,(0,7):C.GC_2219,(0,6):C.GC_2225,(0,0):C.GC_2212,(0,2):C.GC_2215,(0,8):C.GC_93,(0,1):C.GC_92,(0,10):C.GC_97})

V_404 = Vertex(name = 'V_404',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS173, L.VVVSS213, L.VVVSS226, L.VVVSS230 ],
               couplings = {(0,1):C.GC_2637,(0,0):C.GC_2610,(0,2):C.GC_474,(0,3):C.GC_453})

V_405 = Vertex(name = 'V_405',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS215, L.VVVVS218, L.VVVVS222, L.VVVVS226, L.VVVVS231, L.VVVVS232, L.VVVVS317, L.VVVVS342, L.VVVVS43 ],
               couplings = {(0,3):C.GC_4497,(0,6):C.GC_4501,(0,1):C.GC_5030,(0,2):C.GC_5031,(0,8):C.GC_5018,(0,4):C.GC_4499,(0,0):C.GC_5022,(0,7):C.GC_5025,(0,5):C.GC_5034})

V_406 = Vertex(name = 'V_406',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS215, L.VVVVS231, L.VVVVS232 ],
               couplings = {(0,1):C.GC_4592,(0,0):C.GC_5135,(0,2):C.GC_5145})

V_407 = Vertex(name = 'V_407',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS111, L.VVVVS138, L.VVVVS139, L.VVVVS177, L.VVVVS291, L.VVVVS296, L.VVVVS301, L.VVVVS306, L.VVVVS310, L.VVVVS314, L.VVVVS340, L.VVVVS353, L.VVVVS355, L.VVVVS356, L.VVVVS357, L.VVVVS363, L.VVVVS41, L.VVVVS42, L.VVVVS47 ],
               couplings = {(0,0):C.GC_4804,(0,2):C.GC_4806,(0,7):C.GC_5037,(0,9):C.GC_5040,(0,6):C.GC_4494,(0,8):C.GC_5209,(0,5):C.GC_4492,(0,16):C.GC_4799,(0,17):C.GC_4486,(0,18):C.GC_6273,(0,14):C.GC_4495,(0,1):C.GC_5659,(0,10):C.GC_4801,(0,11):C.GC_6274,(0,13):C.GC_5038,(0,15):C.GC_5155,(0,4):C.GC_4487,(0,3):C.GC_6275,(0,12):C.GC_4489})

V_408 = Vertex(name = 'V_408',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS138, L.VVVVS177, L.VVVVS291, L.VVVVS353, L.VVVVS357 ],
               couplings = {(0,4):C.GC_4588,(0,0):C.GC_5752,(0,3):C.GC_6376,(0,2):C.GC_4585,(0,1):C.GC_6333})

V_409 = Vertex(name = 'V_409',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV135, L.VVVVV136, L.VVVVV137, L.VVVVV152, L.VVVVV153, L.VVVVV159, L.VVVVV17, L.VVVVV40, L.VVVVV42, L.VVVVV50, L.VVVVV51, L.VVVVV54, L.VVVVV59, L.VVVVV76, L.VVVVV77, L.VVVVV8, L.VVVVV99 ],
               couplings = {(0,14):C.GC_5367,(0,13):C.GC_5370,(0,6):C.GC_106,(0,16):C.GC_108,(0,15):C.GC_110,(0,9):C.GC_107,(0,3):C.GC_667,(0,4):C.GC_675,(0,12):C.GC_109,(0,5):C.GC_111,(0,2):C.GC_5366,(0,1):C.GC_5369,(0,0):C.GC_5395,(0,7):C.GC_5323,(0,8):C.GC_5365,(0,10):C.GC_6724,(0,11):C.GC_5368})

V_410 = Vertex(name = 'V_410',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV137, L.VVVVV159, L.VVVVV51, L.VVVVV54, L.VVVVV59 ],
               couplings = {(0,4):C.GC_652,(0,1):C.GC_662,(0,0):C.GC_5391,(0,2):C.GC_6730,(0,3):C.GC_5387})

V_411 = Vertex(name = 'V_411',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV12, L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV134, L.VVVVV138, L.VVVVV145, L.VVVVV146, L.VVVVV15, L.VVVVV157, L.VVVVV29, L.VVVVV30, L.VVVVV37, L.VVVVV65, L.VVVVV70, L.VVVVV78, L.VVVVV90 ],
               couplings = {(0,15):C.GC_6860,(0,13):C.GC_5327,(0,14):C.GC_5408,(0,9):C.GC_2238,(0,0):C.GC_2242,(0,17):C.GC_2240,(0,16):C.GC_2239,(0,7):C.GC_2765,(0,8):C.GC_2770,(0,10):C.GC_2243,(0,12):C.GC_5324,(0,6):C.GC_2241,(0,11):C.GC_5364,(0,2):C.GC_5325,(0,4):C.GC_5326,(0,1):C.GC_6861,(0,5):C.GC_5345,(0,3):C.GC_6769})

V_412 = Vertex(name = 'V_412',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV138, L.VVVVV157 ],
               couplings = {(0,5):C.GC_2763,(0,4):C.GC_2758,(0,1):C.GC_5341,(0,3):C.GC_5339,(0,0):C.GC_5417,(0,2):C.GC_6805})

V_413 = Vertex(name = 'V_413',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV100, L.VVVVV101, L.VVVVV115, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV14, L.VVVVV140, L.VVVVV142, L.VVVVV143, L.VVVVV147, L.VVVVV148, L.VVVVV155, L.VVVVV156, L.VVVVV16, L.VVVVV23, L.VVVVV28, L.VVVVV3, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV38, L.VVVVV39, L.VVVVV6, L.VVVVV64, L.VVVVV68, L.VVVVV69, L.VVVVV7, L.VVVVV79, L.VVVVV81, L.VVVVV91, L.VVVVV92 ],
               couplings = {(0,17):C.GC_6781,(0,19):C.GC_6782,(0,29):C.GC_6973,(0,27):C.GC_6976,(0,0):C.GC_2262,(0,15):C.GC_2817,(0,16):C.GC_2257,(0,31):C.GC_2827,(0,18):C.GC_2258,(0,30):C.GC_2831,(0,20):C.GC_2259,(0,34):C.GC_2829,(0,26):C.GC_2823,(0,33):C.GC_2825,(0,7):C.GC_2828,(0,21):C.GC_2821,(0,8):C.GC_2778,(0,11):C.GC_3033,(0,10):C.GC_3035,(0,9):C.GC_3036,(0,12):C.GC_3041,(0,14):C.GC_2826,(0,13):C.GC_2832,(0,22):C.GC_2772,(0,23):C.GC_2260,(0,24):C.GC_2818,(0,25):C.GC_2820,(0,2):C.GC_2830,(0,3):C.GC_6780,(0,6):C.GC_6783,(0,4):C.GC_6975,(0,32):C.GC_2255,(0,1):C.GC_2256,(0,28):C.GC_6778,(0,5):C.GC_6779})

V_414 = Vertex(name = 'V_414',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV100, L.VVVVV101, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV155, L.VVVVV156, L.VVVVV36, L.VVVVV39 ],
               couplings = {(0,6):C.GC_3040,(0,5):C.GC_3032,(0,7):C.GC_2777,(0,8):C.GC_3037,(0,1):C.GC_3030,(0,4):C.GC_6806,(0,2):C.GC_6996,(0,0):C.GC_2773,(0,3):C.GC_6804})

V_415 = Vertex(name = 'V_415',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV10, L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV106, L.VVVVV107, L.VVVVV108, L.VVVVV109, L.VVVVV11, L.VVVVV110, L.VVVVV111, L.VVVVV112, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV125, L.VVVVV13, L.VVVVV141, L.VVVVV150, L.VVVVV151, L.VVVVV160, L.VVVVV161, L.VVVVV18, L.VVVVV19, L.VVVVV24, L.VVVVV25, L.VVVVV27, L.VVVVV41, L.VVVVV43, L.VVVVV44, L.VVVVV45, L.VVVVV46, L.VVVVV49, L.VVVVV52, L.VVVVV53, L.VVVVV57, L.VVVVV58, L.VVVVV60, L.VVVVV61, L.VVVVV62, L.VVVVV74, L.VVVVV84, L.VVVVV86, L.VVVVV87, L.VVVVV88, L.VVVVV89, L.VVVVV9, L.VVVVV93, L.VVVVV94 ],
               couplings = {(0,42):C.GC_6784,(0,25):C.GC_5330,(0,43):C.GC_5411,(0,44):C.GC_5423,(0,32):C.GC_5300,(0,31):C.GC_5376,(0,28):C.GC_5431,(0,9):C.GC_139,(0,24):C.GC_147,(0,45):C.GC_140,(0,46):C.GC_145,(0,0):C.GC_133,(0,47):C.GC_144,(0,26):C.GC_137,(0,49):C.GC_143,(0,30):C.GC_6970,(0,17):C.GC_3061,(0,33):C.GC_3058,(0,23):C.GC_3057,(0,48):C.GC_3056,(0,12):C.GC_676,(0,11):C.GC_681,(0,20):C.GC_668,(0,18):C.GC_688,(0,13):C.GC_142,(0,14):C.GC_148,(0,27):C.GC_3054,(0,19):C.GC_3178,(0,22):C.GC_146,(0,21):C.GC_3055,(0,36):C.GC_3174,(0,37):C.GC_3059,(0,29):C.GC_134,(0,34):C.GC_136,(0,35):C.GC_7034,(0,6):C.GC_5302,(0,5):C.GC_5396,(0,16):C.GC_6969,(0,38):C.GC_5328,(0,40):C.GC_5409,(0,39):C.GC_5421,(0,8):C.GC_6785,(0,3):C.GC_5329,(0,1):C.GC_5331,(0,2):C.GC_5410,(0,7):C.GC_5412,(0,10):C.GC_5424,(0,4):C.GC_5422,(0,41):C.GC_7033,(0,15):C.GC_7035})

V_416 = Vertex(name = 'V_416',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV108, L.VVVVV110, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV160, L.VVVVV161, L.VVVVV52, L.VVVVV53, L.VVVVV58 ],
               couplings = {(0,6):C.GC_685,(0,7):C.GC_663,(0,10):C.GC_653,(0,9):C.GC_3175,(0,13):C.GC_3177,(0,11):C.GC_682,(0,12):C.GC_7054,(0,2):C.GC_5343,(0,0):C.GC_5344,(0,1):C.GC_5415,(0,4):C.GC_5416,(0,5):C.GC_5427,(0,3):C.GC_5426,(0,8):C.GC_7050})

V_417 = Vertex(name = 'V_417',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS216, L.VVVVS217, L.VVVVS224, L.VVVVS227, L.VVVVS293, L.VVVVS294, L.VVVVS295, L.VVVVS299, L.VVVVS302, L.VVVVS317, L.VVVVS318, L.VVVVS344, L.VVVVS345, L.VVVVS361, L.VVVVS44, L.VVVVS46, L.VVVVS48 ],
               couplings = {(0,9):C.GC_4501,(0,10):C.GC_4813,(0,3):C.GC_4808,(0,2):C.GC_5029,(0,8):C.GC_5033,(0,7):C.GC_5205,(0,14):C.GC_5020,(0,16):C.GC_5660,(0,15):C.GC_5203,(0,12):C.GC_5661,(0,1):C.GC_5666,(0,11):C.GC_4932,(0,13):C.GC_5026,(0,6):C.GC_4811,(0,4):C.GC_6017,(0,5):C.GC_5206,(0,0):C.GC_5204})

V_418 = Vertex(name = 'V_418',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS216, L.VVVVS217, L.VVVVS293, L.VVVVS294, L.VVVVS345 ],
               couplings = {(0,4):C.GC_5747,(0,1):C.GC_5742,(0,2):C.GC_6085,(0,3):C.GC_5236,(0,0):C.GC_5231})

V_419 = Vertex(name = 'V_419',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV131, L.VVVVV132, L.VVVVV133, L.VVVVV149, L.VVVVV154, L.VVVVV158, L.VVVVV162, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV32, L.VVVVV63, L.VVVVV66, L.VVVVV67, L.VVVVV71, L.VVVVV72, L.VVVVV73, L.VVVVV75, L.VVVVV83, L.VVVVV85, L.VVVVV95, L.VVVVV96, L.VVVVV97, L.VVVVV98 ],
               couplings = {(0,24):C.GC_7032,(0,25):C.GC_6880,(0,14):C.GC_3508,(0,29):C.GC_2263,(0,28):C.GC_2824,(0,15):C.GC_2254,(0,13):C.GC_2828,(0,27):C.GC_2261,(0,26):C.GC_2822,(0,16):C.GC_2819,(0,12):C.GC_3507,(0,10):C.GC_3815,(0,20):C.GC_5299,(0,19):C.GC_5332,(0,21):C.GC_5373,(0,17):C.GC_5413,(0,9):C.GC_3805,(0,11):C.GC_3509,(0,5):C.GC_6881,(0,3):C.GC_6972,(0,6):C.GC_5346,(0,7):C.GC_5374,(0,4):C.GC_5375,(0,8):C.GC_5418,(0,2):C.GC_5430,(0,23):C.GC_6971,(0,18):C.GC_5425,(0,22):C.GC_5428,(0,1):C.GC_6974,(0,0):C.GC_5429})

V_420 = Vertex(name = 'V_420',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV132, L.VVVVV158, L.VVVVV162 ],
               couplings = {(0,8):C.GC_3808,(0,7):C.GC_3811,(0,5):C.GC_6695,(0,3):C.GC_6997,(0,6):C.GC_5393,(0,4):C.GC_5394,(0,2):C.GC_5433,(0,1):C.GC_6985,(0,0):C.GC_5432})

V_421 = Vertex(name = 'V_421',
               particles = [ P.a, P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS231 ],
               couplings = {(0,0):C.GC_3894})

V_422 = Vertex(name = 'V_422',
               particles = [ P.a, P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS231 ],
               couplings = {(0,0):C.GC_3894})

V_423 = Vertex(name = 'V_423',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS174, L.VVVSS215, L.VVVSS249, L.VVVSS250 ],
               couplings = {(0,0):C.GC_2252,(0,3):C.GC_2814,(0,2):C.GC_3181,(0,1):C.GC_4326})

V_424 = Vertex(name = 'V_424',
               particles = [ P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS174, L.VVVSS215, L.VVVSS249, L.VVVSS250 ],
               couplings = {(0,0):C.GC_2252,(0,3):C.GC_2814,(0,2):C.GC_3181,(0,1):C.GC_4326})

V_425 = Vertex(name = 'V_425',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS240 ],
               couplings = {(0,0):C.GC_3896})

V_426 = Vertex(name = 'V_426',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS240 ],
               couplings = {(0,0):C.GC_3896})

V_427 = Vertex(name = 'V_427',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS318, L.VVVVS319, L.VVVVS368 ],
               couplings = {(0,1):C.GC_4765,(0,0):C.GC_4773,(0,2):C.GC_4772})

V_428 = Vertex(name = 'V_428',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS368 ],
               couplings = {(0,0):C.GC_4927})

V_429 = Vertex(name = 'V_429',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV144, L.VVVVV2, L.VVVVV26, L.VVVVV4, L.VVVVV47, L.VVVVV48, L.VVVVV5, L.VVVVV55, L.VVVVV56, L.VVVVV80, L.VVVVV82 ],
               couplings = {(0,4):C.GC_3908,(0,2):C.GC_144,(0,7):C.GC_3053,(0,3):C.GC_138,(0,5):C.GC_141,(0,10):C.GC_3060,(0,6):C.GC_3062,(0,8):C.GC_4280,(0,1):C.GC_4276,(0,9):C.GC_3909,(0,11):C.GC_135,(0,0):C.GC_3907})

V_430 = Vertex(name = 'V_430',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV56 ],
               couplings = {(0,1):C.GC_4273,(0,0):C.GC_4269})

V_431 = Vertex(name = 'V_431',
               particles = [ P.a, P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1, L.VVSSSS28 ],
               couplings = {(0,0):C.GC_437,(0,1):C.GC_192})

V_432 = Vertex(name = 'V_432',
               particles = [ P.a, P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1, L.VVSSSS28 ],
               couplings = {(0,0):C.GC_640,(0,1):C.GC_598})

V_433 = Vertex(name = 'V_433',
               particles = [ P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_438,(0,1):C.GC_189})

V_434 = Vertex(name = 'V_434',
               particles = [ P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_641,(0,1):C.GC_581})

V_435 = Vertex(name = 'V_435',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS16, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_437,(0,1):C.GC_192})

V_436 = Vertex(name = 'V_436',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS16, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_640,(0,1):C.GC_598})

V_437 = Vertex(name = 'V_437',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_1225,(0,1):C.GC_2317})

V_438 = Vertex(name = 'V_438',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_1371,(0,1):C.GC_2717})

V_439 = Vertex(name = 'V_439',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_2307,(0,0):C.GC_2314,(0,1):C.GC_2319})

V_440 = Vertex(name = 'V_440',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_2744,(0,0):C.GC_2701,(0,1):C.GC_2719})

V_441 = Vertex(name = 'V_441',
               particles = [ P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS52, L.VVSSSS54, L.VVSSSS68 ],
               couplings = {(0,0):C.GC_2318,(0,1):C.GC_2306,(0,2):C.GC_2313})

V_442 = Vertex(name = 'V_442',
               particles = [ P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS52, L.VVSSSS54, L.VVSSSS68 ],
               couplings = {(0,0):C.GC_2718,(0,1):C.GC_2743,(0,2):C.GC_2700})

V_443 = Vertex(name = 'V_443',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS81, L.VVVSSS92 ],
               couplings = {(0,0):C.GC_5085,(0,1):C.GC_6021})

V_444 = Vertex(name = 'V_444',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS81, L.VVVSSS92 ],
               couplings = {(0,0):C.GC_5173,(0,1):C.GC_6123})

V_445 = Vertex(name = 'V_445',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS31, L.VVSSSS41, L.VVSSSS96 ],
               couplings = {(0,1):C.GC_2315,(0,2):C.GC_2308,(0,0):C.GC_2319})

V_446 = Vertex(name = 'V_446',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS31, L.VVSSSS41, L.VVSSSS96 ],
               couplings = {(0,1):C.GC_2702,(0,2):C.GC_2745,(0,0):C.GC_2719})

V_447 = Vertex(name = 'V_447',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_2304,(0,1):C.GC_2311,(0,2):C.GC_2317})

V_448 = Vertex(name = 'V_448',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_2741,(0,1):C.GC_2698,(0,2):C.GC_2717})

V_449 = Vertex(name = 'V_449',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_1226,(0,1):C.GC_2319})

V_450 = Vertex(name = 'V_450',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_1372,(0,1):C.GC_2719})

V_451 = Vertex(name = 'V_451',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_4829,(0,0):C.GC_4834,(0,1):C.GC_4828})

V_452 = Vertex(name = 'V_452',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_4950,(0,0):C.GC_4964,(0,1):C.GC_4986})

V_453 = Vertex(name = 'V_453',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1694,(0,0):C.GC_1706,(0,2):C.GC_1697})

V_454 = Vertex(name = 'V_454',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_2150,(0,0):C.GC_2118,(0,2):C.GC_2089})

V_455 = Vertex(name = 'V_455',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_1696,(0,0):C.GC_1703,(0,2):C.GC_1695})

V_456 = Vertex(name = 'V_456',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_2088,(0,0):C.GC_2115,(0,2):C.GC_2151})

V_457 = Vertex(name = 'V_457',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_4826,(0,0):C.GC_4835,(0,1):C.GC_4831})

V_458 = Vertex(name = 'V_458',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_4984,(0,0):C.GC_4965,(0,1):C.GC_4952})

V_459 = Vertex(name = 'V_459',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1693,(0,0):C.GC_1705,(0,2):C.GC_1698})

V_460 = Vertex(name = 'V_460',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_2149,(0,0):C.GC_2117,(0,2):C.GC_2090})

V_461 = Vertex(name = 'V_461',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_6792,(0,1):C.GC_5381})

V_462 = Vertex(name = 'V_462',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_6830,(0,1):C.GC_5403})

V_463 = Vertex(name = 'V_463',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_1225,(0,1):C.GC_2317})

V_464 = Vertex(name = 'V_464',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_1371,(0,1):C.GC_2717})

V_465 = Vertex(name = 'V_465',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_2303,(0,0):C.GC_2310,(0,1):C.GC_2316})

V_466 = Vertex(name = 'V_466',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_2740,(0,0):C.GC_2697,(0,1):C.GC_2716})

V_467 = Vertex(name = 'V_467',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS45, L.VVVSSS76 ],
               couplings = {(0,1):C.GC_6021,(0,0):C.GC_5085})

V_468 = Vertex(name = 'V_468',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS45, L.VVVSSS76 ],
               couplings = {(0,1):C.GC_6123,(0,0):C.GC_5173})

V_469 = Vertex(name = 'V_469',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS40, L.VVSSSS73, L.VVSSSS95 ],
               couplings = {(0,2):C.GC_2317,(0,0):C.GC_2312,(0,1):C.GC_2305})

V_470 = Vertex(name = 'V_470',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS40, L.VVSSSS73, L.VVSSSS95 ],
               couplings = {(0,2):C.GC_2717,(0,0):C.GC_2699,(0,1):C.GC_2742})

V_471 = Vertex(name = 'V_471',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS34, L.VVSSSS44, L.VVSSSS67 ],
               couplings = {(0,1):C.GC_2308,(0,0):C.GC_2319,(0,2):C.GC_2309})

V_472 = Vertex(name = 'V_472',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS34, L.VVSSSS44, L.VVSSSS67 ],
               couplings = {(0,1):C.GC_2745,(0,0):C.GC_2719,(0,2):C.GC_2696})

V_473 = Vertex(name = 'V_473',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_2304,(0,1):C.GC_2311,(0,2):C.GC_2317})

V_474 = Vertex(name = 'V_474',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_2741,(0,1):C.GC_2698,(0,2):C.GC_2717})

V_475 = Vertex(name = 'V_475',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_1224,(0,1):C.GC_2316})

V_476 = Vertex(name = 'V_476',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_1370,(0,1):C.GC_2716})

V_477 = Vertex(name = 'V_477',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS118, L.VVVVSS121, L.VVVVSS221, L.VVVVSS236, L.VVVVSS253, L.VVVVSS259, L.VVVVSS270, L.VVVVSS350, L.VVVVSS353, L.VVVVSS376, L.VVVVSS380, L.VVVVSS392, L.VVVVSS432, L.VVVVSS59, L.VVVVSS68, L.VVVVSS75, L.VVVVSS76, L.VVVVSS98 ],
               couplings = {(0,14):C.GC_2339,(0,13):C.GC_2345,(0,3):C.GC_177,(0,2):C.GC_185,(0,0):C.GC_171,(0,1):C.GC_2328,(0,10):C.GC_172,(0,9):C.GC_551,(0,16):C.GC_1767,(0,7):C.GC_2351,(0,11):C.GC_184,(0,8):C.GC_2334,(0,12):C.GC_180,(0,6):C.GC_2331,(0,4):C.GC_6791,(0,15):C.GC_5380,(0,17):C.GC_1768,(0,5):C.GC_1769})

V_478 = Vertex(name = 'V_478',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS253, L.VVVVSS259, L.VVVVSS270, L.VVVVSS350, L.VVVVSS380, L.VVVVSS432, L.VVVVSS75, L.VVVVSS76 ],
               couplings = {(0,4):C.GC_476,(0,7):C.GC_2024,(0,3):C.GC_2646,(0,5):C.GC_456,(0,2):C.GC_2623,(0,0):C.GC_6829,(0,6):C.GC_5402,(0,1):C.GC_2023})

V_479 = Vertex(name = 'V_479',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS101, L.VVSSSS103, L.VVSSSS57 ],
               couplings = {(0,1):C.GC_1692,(0,2):C.GC_1699,(0,0):C.GC_1704})

V_480 = Vertex(name = 'V_480',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS101, L.VVSSSS103, L.VVSSSS57 ],
               couplings = {(0,1):C.GC_2148,(0,2):C.GC_2091,(0,0):C.GC_2116})

V_481 = Vertex(name = 'V_481',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS42, L.VVVSSS43, L.VVVSSS9 ],
               couplings = {(0,0):C.GC_4826,(0,1):C.GC_4835,(0,2):C.GC_4832})

V_482 = Vertex(name = 'V_482',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS42, L.VVVSSS43, L.VVVSSS9 ],
               couplings = {(0,0):C.GC_4984,(0,1):C.GC_4965,(0,2):C.GC_4953})

V_483 = Vertex(name = 'V_483',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS58, L.VVSSSS86, L.VVSSSS88 ],
               couplings = {(0,1):C.GC_1693,(0,2):C.GC_1705,(0,0):C.GC_1700})

V_484 = Vertex(name = 'V_484',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS58, L.VVSSSS86, L.VVSSSS88 ],
               couplings = {(0,1):C.GC_2149,(0,2):C.GC_2117,(0,0):C.GC_2092})

V_485 = Vertex(name = 'V_485',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS21 ],
               couplings = {(0,0):C.GC_5684,(0,1):C.GC_4833})

V_486 = Vertex(name = 'V_486',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS21 ],
               couplings = {(0,0):C.GC_5831,(0,1):C.GC_4954})

V_487 = Vertex(name = 'V_487',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_814,(0,0):C.GC_1705})

V_488 = Vertex(name = 'V_488',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_954,(0,0):C.GC_2117})

V_489 = Vertex(name = 'V_489',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS17, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_814,(0,1):C.GC_1705})

V_490 = Vertex(name = 'V_490',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS17, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_954,(0,1):C.GC_2117})

V_491 = Vertex(name = 'V_491',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS18, L.VVSSSS8, L.VVSSSS81 ],
               couplings = {(0,1):C.GC_1691,(0,0):C.GC_1703,(0,2):C.GC_1702})

V_492 = Vertex(name = 'V_492',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS18, L.VVSSSS8, L.VVSSSS81 ],
               couplings = {(0,1):C.GC_2147,(0,0):C.GC_2115,(0,2):C.GC_2094})

V_493 = Vertex(name = 'V_493',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS60, L.VVSSSS9 ],
               couplings = {(0,0):C.GC_1699,(0,2):C.GC_1693,(0,1):C.GC_1705})

V_494 = Vertex(name = 'V_494',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS60, L.VVSSSS9 ],
               couplings = {(0,0):C.GC_2091,(0,2):C.GC_2149,(0,1):C.GC_2117})

V_495 = Vertex(name = 'V_495',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS13 ],
               couplings = {(0,0):C.GC_813})

V_496 = Vertex(name = 'V_496',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS13 ],
               couplings = {(0,0):C.GC_955})

V_497 = Vertex(name = 'V_497',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS6 ],
               couplings = {(0,0):C.GC_813})

V_498 = Vertex(name = 'V_498',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS6 ],
               couplings = {(0,0):C.GC_955})

V_499 = Vertex(name = 'V_499',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_814,(0,0):C.GC_1705})

V_500 = Vertex(name = 'V_500',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_954,(0,0):C.GC_2117})

V_501 = Vertex(name = 'V_501',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS13, L.VVVVSS15, L.VVVVSS16, L.VVVVSS223, L.VVVVSS228, L.VVVVSS251, L.VVVVSS308, L.VVVVSS31, L.VVVVSS32, L.VVVVSS332, L.VVVVSS333, L.VVVVSS40, L.VVVVSS400, L.VVVVSS416, L.VVVVSS422 ],
               couplings = {(0,1):C.GC_1726,(0,3):C.GC_2302,(0,4):C.GC_2291,(0,2):C.GC_1724,(0,8):C.GC_1714,(0,0):C.GC_2286,(0,9):C.GC_1729,(0,13):C.GC_2288,(0,12):C.GC_2298,(0,6):C.GC_2294,(0,11):C.GC_1717,(0,10):C.GC_1719,(0,14):C.GC_2664,(0,7):C.GC_5334,(0,5):C.GC_6726})

V_502 = Vertex(name = 'V_502',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS251, L.VVVVSS308, L.VVVVSS31, L.VVVVSS332, L.VVVVSS40, L.VVVVSS416 ],
               couplings = {(0,3):C.GC_2043,(0,5):C.GC_2589,(0,1):C.GC_2564,(0,4):C.GC_2026,(0,2):C.GC_5352,(0,0):C.GC_6738})

V_503 = Vertex(name = 'V_503',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS14, L.VVVVSS15, L.VVVVSS16, L.VVVVSS212, L.VVVVSS224, L.VVVVSS251, L.VVVVSS305, L.VVVVSS31, L.VVVVSS32, L.VVVVSS332, L.VVVVSS333, L.VVVVSS40, L.VVVVSS403, L.VVVVSS413, L.VVVVSS425 ],
               couplings = {(0,1):C.GC_1725,(0,4):C.GC_2300,(0,3):C.GC_2290,(0,2):C.GC_1723,(0,8):C.GC_1713,(0,0):C.GC_2284,(0,9):C.GC_1728,(0,12):C.GC_2287,(0,13):C.GC_2297,(0,6):C.GC_2293,(0,11):C.GC_1718,(0,10):C.GC_1720,(0,14):C.GC_2666,(0,7):C.GC_5333,(0,5):C.GC_6725})

V_504 = Vertex(name = 'V_504',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS251, L.VVVVSS305, L.VVVVSS31, L.VVVVSS332, L.VVVVSS40, L.VVVVSS403 ],
               couplings = {(0,3):C.GC_2042,(0,5):C.GC_2590,(0,1):C.GC_2563,(0,4):C.GC_2027,(0,2):C.GC_5351,(0,0):C.GC_6737})

V_505 = Vertex(name = 'V_505',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS2, L.VVVSSS95 ],
               couplings = {(0,0):C.GC_4631,(0,1):C.GC_5513})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS2, L.VVVSSS95 ],
               couplings = {(0,0):C.GC_4723,(0,1):C.GC_5544})

V_507 = Vertex(name = 'V_507',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS28, L.VVVSSS39, L.VVVSSS44 ],
               couplings = {(0,2):C.GC_4628,(0,0):C.GC_4633,(0,1):C.GC_4637})

V_508 = Vertex(name = 'V_508',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS28, L.VVVSSS39, L.VVVSSS44 ],
               couplings = {(0,2):C.GC_4752,(0,0):C.GC_4725,(0,1):C.GC_4742})

V_509 = Vertex(name = 'V_509',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS26, L.VVVSSS89, L.VVVSSS91 ],
               couplings = {(0,2):C.GC_4630,(0,0):C.GC_4629,(0,1):C.GC_4635})

V_510 = Vertex(name = 'V_510',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS26, L.VVVSSS89, L.VVVSSS91 ],
               couplings = {(0,2):C.GC_4722,(0,0):C.GC_4753,(0,1):C.GC_4740})

V_511 = Vertex(name = 'V_511',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS100, L.VVVSSS7 ],
               couplings = {(0,1):C.GC_4626,(0,0):C.GC_5514})

V_512 = Vertex(name = 'V_512',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS100, L.VVVSSS7 ],
               couplings = {(0,1):C.GC_4750,(0,0):C.GC_5541})

V_513 = Vertex(name = 'V_513',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_4829,(0,0):C.GC_4834,(0,1):C.GC_4828})

V_514 = Vertex(name = 'V_514',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_4950,(0,0):C.GC_4964,(0,1):C.GC_4986})

V_515 = Vertex(name = 'V_515',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1694,(0,0):C.GC_1706,(0,2):C.GC_1697})

V_516 = Vertex(name = 'V_516',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_2150,(0,0):C.GC_2118,(0,2):C.GC_2089})

V_517 = Vertex(name = 'V_517',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_1701,(0,0):C.GC_1707,(0,2):C.GC_1690})

V_518 = Vertex(name = 'V_518',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_2093,(0,0):C.GC_2119,(0,2):C.GC_2146})

V_519 = Vertex(name = 'V_519',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_4827,(0,0):C.GC_4836,(0,1):C.GC_4830})

V_520 = Vertex(name = 'V_520',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_4985,(0,0):C.GC_4966,(0,1):C.GC_4951})

V_521 = Vertex(name = 'V_521',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1693,(0,0):C.GC_1705,(0,2):C.GC_1698})

V_522 = Vertex(name = 'V_522',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_2149,(0,0):C.GC_2117,(0,2):C.GC_2090})

V_523 = Vertex(name = 'V_523',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS24, L.VVVSSS34 ],
               couplings = {(0,2):C.GC_4632,(0,0):C.GC_4636,(0,1):C.GC_4627})

V_524 = Vertex(name = 'V_524',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS24, L.VVVSSS34 ],
               couplings = {(0,2):C.GC_4724,(0,0):C.GC_4741,(0,1):C.GC_4751})

V_525 = Vertex(name = 'V_525',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS13, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_5514,(0,1):C.GC_4626})

V_526 = Vertex(name = 'V_526',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS13, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_5541,(0,1):C.GC_4750})

V_527 = Vertex(name = 'V_527',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS23, L.VVVSSS80 ],
               couplings = {(0,2):C.GC_4625,(0,0):C.GC_4635,(0,1):C.GC_4634})

V_528 = Vertex(name = 'V_528',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS23, L.VVVSSS80 ],
               couplings = {(0,2):C.GC_4749,(0,0):C.GC_4740,(0,1):C.GC_4726})

V_529 = Vertex(name = 'V_529',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS201, L.VVVVSS245, L.VVVVSS287, L.VVVVSS336, L.VVVVSS342, L.VVVVSS435, L.VVVVSS51, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,1):C.GC_1683,(0,0):C.GC_1689,(0,2):C.GC_1681,(0,3):C.GC_1685,(0,4):C.GC_2061,(0,6):C.GC_1680,(0,5):C.GC_1684,(0,7):C.GC_6700,(0,8):C.GC_5304})

V_530 = Vertex(name = 'V_530',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS287, L.VVVVSS435, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_2007,(0,1):C.GC_1992,(0,2):C.GC_6709,(0,3):C.GC_5316})

V_531 = Vertex(name = 'V_531',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_6792,(0,1):C.GC_5381})

V_532 = Vertex(name = 'V_532',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_6830,(0,1):C.GC_5403})

V_533 = Vertex(name = 'V_533',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS211, L.VVVVSS22, L.VVVVSS240, L.VVVVSS25, L.VVVVSS254, L.VVVVSS27, L.VVVVSS327, L.VVVVSS334, L.VVVVSS338, L.VVVVSS343, L.VVVVSS345, L.VVVVSS75, L.VVVVSS83, L.VVVVSS87, L.VVVVSS96 ],
               couplings = {(0,3):C.GC_1727,(0,0):C.GC_2302,(0,2):C.GC_2291,(0,5):C.GC_1724,(0,14):C.GC_1715,(0,1):C.GC_2285,(0,6):C.GC_1730,(0,10):C.GC_2288,(0,8):C.GC_2299,(0,9):C.GC_2665,(0,4):C.GC_1716,(0,7):C.GC_1719,(0,12):C.GC_2295,(0,11):C.GC_6726,(0,13):C.GC_5334})

V_534 = Vertex(name = 'V_534',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS254, L.VVVVSS327, L.VVVVSS345, L.VVVVSS75, L.VVVVSS83, L.VVVVSS87 ],
               couplings = {(0,1):C.GC_2044,(0,2):C.GC_2589,(0,0):C.GC_2025,(0,4):C.GC_2565,(0,3):C.GC_6738,(0,5):C.GC_5352})

V_535 = Vertex(name = 'V_535',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS204, L.VVVVSS21, L.VVVVSS210, L.VVVVSS25, L.VVVVSS254, L.VVVVSS27, L.VVVVSS327, L.VVVVSS334, L.VVVVSS368, L.VVVVSS393, L.VVVVSS402, L.VVVVSS75, L.VVVVSS80, L.VVVVSS87, L.VVVVSS96 ],
               couplings = {(0,3):C.GC_1725,(0,2):C.GC_2301,(0,0):C.GC_2292,(0,5):C.GC_1722,(0,14):C.GC_1713,(0,1):C.GC_2284,(0,6):C.GC_1728,(0,8):C.GC_2289,(0,9):C.GC_2297,(0,10):C.GC_2667,(0,4):C.GC_1718,(0,7):C.GC_1721,(0,12):C.GC_2296,(0,11):C.GC_6727,(0,13):C.GC_5335})

V_536 = Vertex(name = 'V_536',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS254, L.VVVVSS327, L.VVVVSS368, L.VVVVSS75, L.VVVVSS80, L.VVVVSS87 ],
               couplings = {(0,1):C.GC_2042,(0,2):C.GC_2588,(0,0):C.GC_2027,(0,4):C.GC_2566,(0,3):C.GC_6739,(0,5):C.GC_5353})

V_537 = Vertex(name = 'V_537',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS19, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_5513,(0,1):C.GC_4631})

V_538 = Vertex(name = 'V_538',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS19, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_5544,(0,1):C.GC_4723})

V_539 = Vertex(name = 'V_539',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS205, L.VVVVSS244, L.VVVVSS287, L.VVVVSS389, L.VVVVSS399, L.VVVVSS435, L.VVVVSS51, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,1):C.GC_1683,(0,0):C.GC_1687,(0,2):C.GC_1681,(0,3):C.GC_1685,(0,4):C.GC_2061,(0,6):C.GC_1680,(0,5):C.GC_1684,(0,7):C.GC_6699,(0,8):C.GC_5305})

V_540 = Vertex(name = 'V_540',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS287, L.VVVVSS435, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_2007,(0,1):C.GC_1992,(0,2):C.GC_6710,(0,3):C.GC_5313})

V_541 = Vertex(name = 'V_541',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS205, L.VVVVSS244, L.VVVVSS287, L.VVVVSS389, L.VVVVSS399, L.VVVVSS435, L.VVVVSS51, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,1):C.GC_1683,(0,0):C.GC_1687,(0,2):C.GC_1681,(0,3):C.GC_1685,(0,4):C.GC_2061,(0,6):C.GC_1680,(0,5):C.GC_1684,(0,7):C.GC_6701,(0,8):C.GC_5306})

V_542 = Vertex(name = 'V_542',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS287, L.VVVVSS435, L.VVVVSS75, L.VVVVSS87 ],
               couplings = {(0,0):C.GC_2007,(0,1):C.GC_1992,(0,2):C.GC_6711,(0,3):C.GC_5314})

V_543 = Vertex(name = 'V_543',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS29 ],
               couplings = {(0,0):C.GC_6310,(0,1):C.GC_6309})

V_544 = Vertex(name = 'V_544',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS29 ],
               couplings = {(0,0):C.GC_6387,(0,1):C.GC_6408})

V_545 = Vertex(name = 'V_545',
               particles = [ P.a, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS28, L.VVSSSS53, L.VVSSSS59 ],
               couplings = {(0,1):C.GC_3537,(0,2):C.GC_3535,(0,0):C.GC_3541})

V_546 = Vertex(name = 'V_546',
               particles = [ P.a, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS28, L.VVSSSS53, L.VVSSSS59 ],
               couplings = {(0,1):C.GC_3744,(0,2):C.GC_3777,(0,0):C.GC_3750})

V_547 = Vertex(name = 'V_547',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS20, L.VVSSSS91 ],
               couplings = {(0,0):C.GC_3542,(0,1):C.GC_3539})

V_548 = Vertex(name = 'V_548',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS20, L.VVSSSS91 ],
               couplings = {(0,0):C.GC_3751,(0,1):C.GC_3779})

V_549 = Vertex(name = 'V_549',
               particles = [ P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_3540,(0,1):C.GC_3538})

V_550 = Vertex(name = 'V_550',
               particles = [ P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_3778,(0,1):C.GC_3745})

V_551 = Vertex(name = 'V_551',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS29, L.VVSSSS45, L.VVSSSS51 ],
               couplings = {(0,2):C.GC_3536,(0,1):C.GC_3534,(0,0):C.GC_3541})

V_552 = Vertex(name = 'V_552',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS29, L.VVSSSS45, L.VVSSSS51 ],
               couplings = {(0,2):C.GC_3743,(0,1):C.GC_3776,(0,0):C.GC_3750})

V_553 = Vertex(name = 'V_553',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_5696,(0,0):C.GC_5689,(0,2):C.GC_5693})

V_554 = Vertex(name = 'V_554',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_5796,(0,0):C.GC_5832,(0,2):C.GC_5786})

V_555 = Vertex(name = 'V_555',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_224,(0,3):C.GC_233,(0,2):C.GC_816,(0,1):C.GC_240})

V_556 = Vertex(name = 'V_556',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_621,(0,3):C.GC_585,(0,2):C.GC_957,(0,1):C.GC_602})

V_557 = Vertex(name = 'V_557',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_222,(0,5):C.GC_230,(0,3):C.GC_238,(0,0):C.GC_1750,(0,1):C.GC_1757,(0,2):C.GC_1761})

V_558 = Vertex(name = 'V_558',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_619,(0,5):C.GC_582,(0,3):C.GC_600,(0,0):C.GC_2152,(0,1):C.GC_2097,(0,2):C.GC_2120})

V_559 = Vertex(name = 'V_559',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS15, L.VVVSSS67, L.VVVSSS74, L.VVVSSS85, L.VVVSSS86, L.VVVSSS99 ],
               couplings = {(0,4):C.GC_4539,(0,1):C.GC_4541,(0,2):C.GC_4543,(0,3):C.GC_4859,(0,5):C.GC_4860,(0,0):C.GC_4862})

V_560 = Vertex(name = 'V_560',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS15, L.VVVSSS67, L.VVVSSS74, L.VVVSSS85, L.VVVSSS86, L.VVVSSS99 ],
               couplings = {(0,4):C.GC_4607,(0,1):C.GC_4600,(0,2):C.GC_4602,(0,3):C.GC_4987,(0,5):C.GC_4955,(0,0):C.GC_4968})

V_561 = Vertex(name = 'V_561',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS14, L.VVSSSS43, L.VVSSSS55, L.VVSSSS56, L.VVSSSS64, L.VVSSSS65 ],
               couplings = {(0,2):C.GC_227,(0,3):C.GC_1752,(0,1):C.GC_241,(0,0):C.GC_1763,(0,5):C.GC_232,(0,4):C.GC_1759})

V_562 = Vertex(name = 'V_562',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS14, L.VVSSSS43, L.VVSSSS55, L.VVSSSS56, L.VVSSSS64, L.VVSSSS65 ],
               couplings = {(0,2):C.GC_624,(0,3):C.GC_2154,(0,1):C.GC_603,(0,0):C.GC_2122,(0,5):C.GC_584,(0,4):C.GC_2099})

V_563 = Vertex(name = 'V_563',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_240,(0,0):C.GC_1763,(0,3):C.GC_225,(0,5):C.GC_232,(0,2):C.GC_1751,(0,4):C.GC_1758})

V_564 = Vertex(name = 'V_564',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_602,(0,0):C.GC_2122,(0,3):C.GC_622,(0,5):C.GC_584,(0,2):C.GC_2153,(0,4):C.GC_2098})

V_565 = Vertex(name = 'V_565',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS32, L.VVSSSS38, L.VVSSSS4, L.VVSSSS42, L.VVSSSS97, L.VVSSSS98 ],
               couplings = {(0,5):C.GC_223,(0,1):C.GC_231,(0,0):C.GC_238,(0,4):C.GC_1754,(0,3):C.GC_1756,(0,2):C.GC_1764})

V_566 = Vertex(name = 'V_566',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS32, L.VVSSSS38, L.VVSSSS4, L.VVSSSS42, L.VVSSSS97, L.VVSSSS98 ],
               couplings = {(0,5):C.GC_620,(0,1):C.GC_583,(0,0):C.GC_600,(0,4):C.GC_2156,(0,3):C.GC_2096,(0,2):C.GC_2123})

V_567 = Vertex(name = 'V_567',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_5692})

V_568 = Vertex(name = 'V_568',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_5835})

V_569 = Vertex(name = 'V_569',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_228,(0,2):C.GC_231,(0,1):C.GC_815,(0,3):C.GC_237})

V_570 = Vertex(name = 'V_570',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_625,(0,2):C.GC_583,(0,1):C.GC_958,(0,3):C.GC_599})

V_571 = Vertex(name = 'V_571',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_5698,(0,0):C.GC_5691,(0,2):C.GC_5695})

V_572 = Vertex(name = 'V_572',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_5798,(0,0):C.GC_5834,(0,2):C.GC_5788})

V_573 = Vertex(name = 'V_573',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS249, L.VVVVSS250, L.VVVVSS251 ],
               couplings = {(0,0):C.GC_6728,(0,1):C.GC_6884,(0,2):C.GC_5414})

V_574 = Vertex(name = 'V_574',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS249, L.VVVVSS250, L.VVVVSS251 ],
               couplings = {(0,0):C.GC_6741,(0,1):C.GC_6917,(0,2):C.GC_5420})

V_575 = Vertex(name = 'V_575',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_5518,(0,2):C.GC_6033,(0,0):C.GC_5096})

V_576 = Vertex(name = 'V_576',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_5545,(0,2):C.GC_6133,(0,0):C.GC_5184})

V_577 = Vertex(name = 'V_577',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_5516,(0,2):C.GC_6032,(0,0):C.GC_5095})

V_578 = Vertex(name = 'V_578',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_5548,(0,2):C.GC_6132,(0,0):C.GC_5183})

V_579 = Vertex(name = 'V_579',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_5697,(0,0):C.GC_5690,(0,2):C.GC_5694})

V_580 = Vertex(name = 'V_580',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_5797,(0,0):C.GC_5833,(0,2):C.GC_5787})

V_581 = Vertex(name = 'V_581',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_224,(0,3):C.GC_233,(0,2):C.GC_816,(0,1):C.GC_240})

V_582 = Vertex(name = 'V_582',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_621,(0,3):C.GC_585,(0,2):C.GC_957,(0,1):C.GC_602})

V_583 = Vertex(name = 'V_583',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_229,(0,5):C.GC_235,(0,3):C.GC_242,(0,0):C.GC_1753,(0,1):C.GC_1760,(0,2):C.GC_1764})

V_584 = Vertex(name = 'V_584',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_626,(0,5):C.GC_587,(0,3):C.GC_604,(0,0):C.GC_2155,(0,1):C.GC_2100,(0,2):C.GC_2123})

V_585 = Vertex(name = 'V_585',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS14, L.VVVSSS48, L.VVVSSS49, L.VVVSSS54, L.VVVSSS77, L.VVVSSS97 ],
               couplings = {(0,4):C.GC_4540,(0,2):C.GC_4542,(0,3):C.GC_4544,(0,1):C.GC_4860,(0,0):C.GC_4861,(0,5):C.GC_4859})

V_586 = Vertex(name = 'V_586',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS14, L.VVVSSS48, L.VVVSSS49, L.VVVSSS54, L.VVVSSS77, L.VVVSSS97 ],
               couplings = {(0,4):C.GC_4608,(0,2):C.GC_4601,(0,3):C.GC_4603,(0,1):C.GC_4955,(0,0):C.GC_4967,(0,5):C.GC_4987})

V_587 = Vertex(name = 'V_587',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS106, L.VVSSSS24, L.VVSSSS37, L.VVSSSS39, L.VVSSSS74, L.VVSSSS75 ],
               couplings = {(0,3):C.GC_232,(0,2):C.GC_1759,(0,0):C.GC_239,(0,1):C.GC_1762,(0,4):C.GC_226,(0,5):C.GC_1751})

V_588 = Vertex(name = 'V_588',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS106, L.VVSSSS24, L.VVSSSS37, L.VVSSSS39, L.VVSSSS74, L.VVSSSS75 ],
               couplings = {(0,3):C.GC_584,(0,2):C.GC_2099,(0,0):C.GC_601,(0,1):C.GC_2121,(0,4):C.GC_623,(0,5):C.GC_2153})

V_589 = Vertex(name = 'V_589',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_240,(0,0):C.GC_1763,(0,3):C.GC_225,(0,5):C.GC_232,(0,2):C.GC_1751,(0,4):C.GC_1758})

V_590 = Vertex(name = 'V_590',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_602,(0,0):C.GC_2122,(0,3):C.GC_622,(0,5):C.GC_584,(0,2):C.GC_2153,(0,4):C.GC_2098})

V_591 = Vertex(name = 'V_591',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS33, L.VVSSSS49, L.VVSSSS5, L.VVSSSS50, L.VVSSSS69, L.VVSSSS70 ],
               couplings = {(0,1):C.GC_223,(0,0):C.GC_238,(0,3):C.GC_1754,(0,2):C.GC_1764,(0,5):C.GC_236,(0,4):C.GC_1755})

V_592 = Vertex(name = 'V_592',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS33, L.VVSSSS49, L.VVSSSS5, L.VVSSSS50, L.VVSSSS69, L.VVSSSS70 ],
               couplings = {(0,1):C.GC_620,(0,0):C.GC_600,(0,3):C.GC_2156,(0,2):C.GC_2123,(0,5):C.GC_588,(0,4):C.GC_2095})

V_593 = Vertex(name = 'V_593',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_5692})

V_594 = Vertex(name = 'V_594',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_5835})

V_595 = Vertex(name = 'V_595',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_223,(0,2):C.GC_234,(0,1):C.GC_817,(0,3):C.GC_243})

V_596 = Vertex(name = 'V_596',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_620,(0,2):C.GC_586,(0,1):C.GC_956,(0,3):C.GC_605})

V_597 = Vertex(name = 'V_597',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS188, L.VVVVSS189, L.VVVVSS19, L.VVVVSS226, L.VVVVSS227, L.VVVVSS229, L.VVVVSS230, L.VVVVSS247, L.VVVVSS252, L.VVVVSS263, L.VVVVSS277, L.VVVVSS28, L.VVVVSS29, L.VVVVSS31, L.VVVVSS315, L.VVVVSS328, L.VVVVSS330, L.VVVVSS331, L.VVVVSS34, L.VVVVSS346, L.VVVVSS36, L.VVVVSS363, L.VVVVSS370, L.VVVVSS38, L.VVVVSS381, L.VVVVSS382, L.VVVVSS39, L.VVVVSS414, L.VVVVSS423, L.VVVVSS434, L.VVVVSS89, L.VVVVSS90 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_166,(0,12):C.GC_1777,(0,11):C.GC_1779,(0,6):C.GC_2355,(0,5):C.GC_2360,(0,4):C.GC_2901,(0,3):C.GC_2907,(0,20):C.GC_2352,(0,31):C.GC_155,(0,30):C.GC_1771,(0,2):C.GC_2899,(0,25):C.GC_160,(0,24):C.GC_169,(0,16):C.GC_1776,(0,15):C.GC_1782,(0,22):C.GC_2359,(0,28):C.GC_2668,(0,19):C.GC_2905,(0,17):C.GC_3019,(0,27):C.GC_2354,(0,21):C.GC_2900,(0,10):C.GC_2322,(0,14):C.GC_159,(0,9):C.GC_1774,(0,29):C.GC_2357,(0,23):C.GC_2903,(0,18):C.GC_2323,(0,26):C.GC_2324,(0,13):C.GC_6729,(0,7):C.GC_5338,(0,8):C.GC_6885})

V_598 = Vertex(name = 'V_598',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS247, L.VVVVSS252, L.VVVVSS263, L.VVVVSS277, L.VVVVSS31, L.VVVVSS315, L.VVVVSS328, L.VVVVSS363, L.VVVVSS38, L.VVVVSS381, L.VVVVSS39, L.VVVVSS414, L.VVVVSS434 ],
               couplings = {(0,9):C.GC_531,(0,6):C.GC_2045,(0,11):C.GC_2592,(0,7):C.GC_2975,(0,3):C.GC_2609,(0,5):C.GC_518,(0,2):C.GC_2029,(0,12):C.GC_2567,(0,8):C.GC_2970,(0,10):C.GC_2608,(0,4):C.GC_6740,(0,0):C.GC_5354,(0,1):C.GC_6916})

V_599 = Vertex(name = 'V_599',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS101, L.VVVSSS8 ],
               couplings = {(0,1):C.GC_6035,(0,0):C.GC_6028})

V_600 = Vertex(name = 'V_600',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS101, L.VVVSSS8 ],
               couplings = {(0,1):C.GC_6112,(0,0):C.GC_6128})

V_601 = Vertex(name = 'V_601',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_6029})

V_602 = Vertex(name = 'V_602',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_6129})

V_603 = Vertex(name = 'V_603',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS6, L.VVVSSS89 ],
               couplings = {(0,0):C.GC_6034,(0,1):C.GC_6027})

V_604 = Vertex(name = 'V_604',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS6, L.VVVSSS89 ],
               couplings = {(0,0):C.GC_6111,(0,1):C.GC_6126})

V_605 = Vertex(name = 'V_605',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS27, L.VVVSSS30 ],
               couplings = {(0,0):C.GC_5519,(0,1):C.GC_4648,(0,2):C.GC_6036})

V_606 = Vertex(name = 'V_606',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS27, L.VVVSSS30 ],
               couplings = {(0,0):C.GC_5546,(0,1):C.GC_4728,(0,2):C.GC_6127})

V_607 = Vertex(name = 'V_607',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS3, L.VVVSSS40, L.VVVSSS62, L.VVVSSS65, L.VVVSSS72, L.VVVSSS96 ],
               couplings = {(0,4):C.GC_4646,(0,2):C.GC_4647,(0,0):C.GC_4649,(0,1):C.GC_5091,(0,3):C.GC_5092,(0,5):C.GC_5093})

V_608 = Vertex(name = 'V_608',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS3, L.VVVSSS40, L.VVVSSS62, L.VVVSSS65, L.VVVSSS72, L.VVVSSS96 ],
               couplings = {(0,4):C.GC_4754,(0,2):C.GC_4727,(0,0):C.GC_4743,(0,1):C.GC_5192,(0,3):C.GC_5174,(0,5):C.GC_5181})

V_609 = Vertex(name = 'V_609',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_6030})

V_610 = Vertex(name = 'V_610',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_6130})

V_611 = Vertex(name = 'V_611',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS12, L.VVVVSS159, L.VVVVSS215, L.VVVVSS216, L.VVVVSS217, L.VVVVSS235, L.VVVVSS246, L.VVVVSS253, L.VVVVSS275, L.VVVVSS306, L.VVVVSS348, L.VVVVSS360, L.VVVVSS372, L.VVVVSS395, L.VVVVSS406, L.VVVVSS408, L.VVVVSS424, L.VVVVSS48, L.VVVVSS70, L.VVVVSS71, L.VVVVSS75, L.VVVVSS77 ],
               couplings = {(0,6):C.GC_211,(0,3):C.GC_1749,(0,19):C.GC_2279,(0,5):C.GC_1738,(0,4):C.GC_221,(0,20):C.GC_2275,(0,0):C.GC_1733,(0,1):C.GC_2265,(0,9):C.GC_208,(0,11):C.GC_217,(0,12):C.GC_556,(0,10):C.GC_2269,(0,17):C.GC_1734,(0,13):C.GC_1745,(0,15):C.GC_2063,(0,16):C.GC_2271,(0,14):C.GC_2282,(0,2):C.GC_1740,(0,18):C.GC_205,(0,22):C.GC_214,(0,7):C.GC_6702,(0,8):C.GC_6796,(0,21):C.GC_5383})

V_612 = Vertex(name = 'V_612',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS159, L.VVVVSS246, L.VVVVSS253, L.VVVVSS275, L.VVVVSS306, L.VVVVSS395, L.VVVVSS424, L.VVVVSS75, L.VVVVSS77 ],
               couplings = {(0,3):C.GC_479,(0,4):C.GC_2620,(0,6):C.GC_2010,(0,5):C.GC_2640,(0,0):C.GC_1993,(0,8):C.GC_458,(0,1):C.GC_6714,(0,2):C.GC_6833,(0,7):C.GC_5406})

V_613 = Vertex(name = 'V_613',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS12, L.VVVVSS159, L.VVVVSS215, L.VVVVSS216, L.VVVVSS217, L.VVVVSS235, L.VVVVSS246, L.VVVVSS253, L.VVVVSS275, L.VVVVSS306, L.VVVVSS348, L.VVVVSS360, L.VVVVSS372, L.VVVVSS395, L.VVVVSS406, L.VVVVSS408, L.VVVVSS424, L.VVVVSS48, L.VVVVSS70, L.VVVVSS71, L.VVVVSS75, L.VVVVSS77 ],
               couplings = {(0,6):C.GC_212,(0,3):C.GC_1747,(0,19):C.GC_2280,(0,5):C.GC_1739,(0,4):C.GC_220,(0,20):C.GC_2276,(0,0):C.GC_1731,(0,1):C.GC_2266,(0,9):C.GC_209,(0,11):C.GC_216,(0,12):C.GC_557,(0,10):C.GC_2270,(0,17):C.GC_1736,(0,13):C.GC_1743,(0,15):C.GC_2065,(0,16):C.GC_2274,(0,14):C.GC_2281,(0,2):C.GC_1742,(0,18):C.GC_204,(0,22):C.GC_215,(0,7):C.GC_6704,(0,8):C.GC_6798,(0,21):C.GC_5384})

V_614 = Vertex(name = 'V_614',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS159, L.VVVVSS246, L.VVVVSS253, L.VVVVSS275, L.VVVVSS306, L.VVVVSS395, L.VVVVSS424, L.VVVVSS75, L.VVVVSS77 ],
               couplings = {(0,3):C.GC_478,(0,4):C.GC_2621,(0,6):C.GC_2008,(0,5):C.GC_2639,(0,0):C.GC_1995,(0,8):C.GC_459,(0,1):C.GC_6713,(0,2):C.GC_6835,(0,7):C.GC_5407})

V_615 = Vertex(name = 'V_615',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_5698,(0,0):C.GC_5691,(0,2):C.GC_5695})

V_616 = Vertex(name = 'V_616',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_5798,(0,0):C.GC_5834,(0,2):C.GC_5788})

V_617 = Vertex(name = 'V_617',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS249, L.VVVVSS250, L.VVVVSS251 ],
               couplings = {(0,0):C.GC_6728,(0,1):C.GC_6884,(0,2):C.GC_5414})

V_618 = Vertex(name = 'V_618',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS249, L.VVVVSS250, L.VVVVSS251 ],
               couplings = {(0,0):C.GC_6741,(0,1):C.GC_6917,(0,2):C.GC_5420})

V_619 = Vertex(name = 'V_619',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_5518,(0,2):C.GC_6033,(0,0):C.GC_5096})

V_620 = Vertex(name = 'V_620',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_5545,(0,2):C.GC_6133,(0,0):C.GC_5184})

V_621 = Vertex(name = 'V_621',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_5517,(0,2):C.GC_6031,(0,0):C.GC_5094})

V_622 = Vertex(name = 'V_622',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_5547,(0,2):C.GC_6131,(0,0):C.GC_5182})

V_623 = Vertex(name = 'V_623',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS104, L.VVVVSS156, L.VVVVSS158, L.VVVVSS179, L.VVVVSS180, L.VVVVSS195, L.VVVVSS198, L.VVVVSS2, L.VVVVSS225, L.VVVVSS227, L.VVVVSS249, L.VVVVSS250, L.VVVVSS251, L.VVVVSS260, L.VVVVSS274, L.VVVVSS33, L.VVVVSS346, L.VVVVSS359, L.VVVVSS371, L.VVVVSS404, L.VVVVSS407, L.VVVVSS412, L.VVVVSS415 ],
               couplings = {(0,9):C.GC_210,(0,5):C.GC_1749,(0,3):C.GC_2278,(0,6):C.GC_1738,(0,8):C.GC_219,(0,4):C.GC_2275,(0,7):C.GC_1732,(0,15):C.GC_2264,(0,14):C.GC_207,(0,16):C.GC_218,(0,17):C.GC_555,(0,19):C.GC_2283,(0,22):C.GC_1735,(0,2):C.GC_1741,(0,18):C.GC_1744,(0,21):C.GC_2062,(0,20):C.GC_2272,(0,1):C.GC_2268,(0,10):C.GC_6703,(0,11):C.GC_6797,(0,0):C.GC_205,(0,13):C.GC_214,(0,12):C.GC_5383})

V_624 = Vertex(name = 'V_624',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS156, L.VVVVSS158, L.VVVVSS249, L.VVVVSS250, L.VVVVSS251, L.VVVVSS260, L.VVVVSS274, L.VVVVSS404, L.VVVVSS415 ],
               couplings = {(0,6):C.GC_480,(0,7):C.GC_2641,(0,8):C.GC_2009,(0,1):C.GC_1994,(0,0):C.GC_2619,(0,2):C.GC_6715,(0,3):C.GC_6834,(0,5):C.GC_458,(0,4):C.GC_5406})

V_625 = Vertex(name = 'V_625',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS104, L.VVVVSS156, L.VVVVSS158, L.VVVVSS179, L.VVVVSS180, L.VVVVSS195, L.VVVVSS198, L.VVVVSS2, L.VVVVSS225, L.VVVVSS227, L.VVVVSS249, L.VVVVSS250, L.VVVVSS251, L.VVVVSS260, L.VVVVSS274, L.VVVVSS33, L.VVVVSS346, L.VVVVSS359, L.VVVVSS371, L.VVVVSS404, L.VVVVSS407, L.VVVVSS412, L.VVVVSS415 ],
               couplings = {(0,9):C.GC_212,(0,5):C.GC_1748,(0,3):C.GC_2280,(0,6):C.GC_1737,(0,8):C.GC_220,(0,4):C.GC_2277,(0,7):C.GC_1731,(0,15):C.GC_2266,(0,14):C.GC_209,(0,16):C.GC_216,(0,17):C.GC_557,(0,19):C.GC_2281,(0,22):C.GC_1736,(0,2):C.GC_1742,(0,18):C.GC_1746,(0,21):C.GC_2064,(0,20):C.GC_2273,(0,1):C.GC_2267,(0,10):C.GC_6705,(0,11):C.GC_6795,(0,0):C.GC_206,(0,13):C.GC_213,(0,12):C.GC_5382})

V_626 = Vertex(name = 'V_626',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS156, L.VVVVSS158, L.VVVVSS249, L.VVVVSS250, L.VVVVSS251, L.VVVVSS260, L.VVVVSS274, L.VVVVSS404, L.VVVVSS415 ],
               couplings = {(0,6):C.GC_478,(0,7):C.GC_2639,(0,8):C.GC_2008,(0,1):C.GC_1995,(0,0):C.GC_2618,(0,2):C.GC_6712,(0,3):C.GC_6832,(0,5):C.GC_457,(0,4):C.GC_5405})

V_627 = Vertex(name = 'V_627',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS33 ],
               couplings = {(0,1):C.GC_6530,(0,0):C.GC_6532})

V_628 = Vertex(name = 'V_628',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS33 ],
               couplings = {(0,1):C.GC_6605,(0,0):C.GC_6592})

V_629 = Vertex(name = 'V_629',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_4079,(0,0):C.GC_4083})

V_630 = Vertex(name = 'V_630',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_4242,(0,0):C.GC_4251})

V_631 = Vertex(name = 'V_631',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS89, L.VVSSSS93 ],
               couplings = {(0,0):C.GC_4083,(0,1):C.GC_4079})

V_632 = Vertex(name = 'V_632',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS89, L.VVSSSS93 ],
               couplings = {(0,0):C.GC_4251,(0,1):C.GC_4242})

V_633 = Vertex(name = 'V_633',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_436,(0,1):C.GC_4078,(0,2):C.GC_4076,(0,3):C.GC_191,(0,4):C.GC_4082})

V_634 = Vertex(name = 'V_634',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_639,(0,1):C.GC_4241,(0,2):C.GC_4250,(0,3):C.GC_597,(0,4):C.GC_4245})

V_635 = Vertex(name = 'V_635',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS104, L.VVSSSS21 ],
               couplings = {(0,0):C.GC_4077,(0,1):C.GC_4081})

V_636 = Vertex(name = 'V_636',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS104, L.VVSSSS21 ],
               couplings = {(0,0):C.GC_4249,(0,1):C.GC_4244})

V_637 = Vertex(name = 'V_637',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_4084,(0,1):C.GC_4080})

V_638 = Vertex(name = 'V_638',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_4252,(0,1):C.GC_4243})

V_639 = Vertex(name = 'V_639',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_435,(0,1):C.GC_4078,(0,2):C.GC_4076,(0,3):C.GC_190,(0,4):C.GC_4082})

V_640 = Vertex(name = 'V_640',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_638,(0,1):C.GC_4241,(0,2):C.GC_4250,(0,3):C.GC_596,(0,4):C.GC_4245})

V_641 = Vertex(name = 'V_641',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_4079,(0,0):C.GC_4083})

V_642 = Vertex(name = 'V_642',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_4242,(0,0):C.GC_4251})

V_643 = Vertex(name = 'V_643',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_4664,(0,3):C.GC_4672,(0,1):C.GC_5077,(0,0):C.GC_5086,(0,6):C.GC_6293,(0,7):C.GC_5218,(0,5):C.GC_5081,(0,2):C.GC_4673})

V_644 = Vertex(name = 'V_644',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_4756,(0,3):C.GC_4733,(0,1):C.GC_5189,(0,0):C.GC_5178,(0,6):C.GC_6404,(0,7):C.GC_5240,(0,5):C.GC_5169,(0,2):C.GC_4744})

V_645 = Vertex(name = 'V_645',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_4666,(0,5):C.GC_4671,(0,1):C.GC_5079,(0,6):C.GC_5083,(0,3):C.GC_5088,(0,7):C.GC_6295,(0,4):C.GC_5220,(0,2):C.GC_4675})

V_646 = Vertex(name = 'V_646',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_4758,(0,5):C.GC_4732,(0,1):C.GC_5191,(0,6):C.GC_5171,(0,3):C.GC_5180,(0,7):C.GC_6406,(0,4):C.GC_5242,(0,2):C.GC_4746})

V_647 = Vertex(name = 'V_647',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS66, L.VVVSSS69, L.VVVSSS70, L.VVVSSS75, L.VVVSSS82, L.VVVSSS98 ],
               couplings = {(0,2):C.GC_4667,(0,3):C.GC_4669,(0,1):C.GC_6022,(0,4):C.GC_6296,(0,5):C.GC_5221,(0,0):C.GC_5084,(0,6):C.GC_4673})

V_648 = Vertex(name = 'V_648',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS66, L.VVVSSS69, L.VVVSSS70, L.VVVSSS75, L.VVVSSS82, L.VVVSSS98 ],
               couplings = {(0,2):C.GC_4759,(0,3):C.GC_4730,(0,1):C.GC_6124,(0,4):C.GC_6407,(0,5):C.GC_5243,(0,0):C.GC_5172,(0,6):C.GC_4744})

V_649 = Vertex(name = 'V_649',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_4663,(0,0):C.GC_4668,(0,3):C.GC_5076,(0,5):C.GC_5080,(0,1):C.GC_6291,(0,4):C.GC_6297})

V_650 = Vertex(name = 'V_650',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_4755,(0,0):C.GC_4729,(0,3):C.GC_5188,(0,5):C.GC_5168,(0,1):C.GC_6402,(0,4):C.GC_6386})

V_651 = Vertex(name = 'V_651',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS246, L.VVVVSS253, L.VVVVSS75 ],
               couplings = {(0,1):C.GC_6693,(0,2):C.GC_5301,(0,0):C.GC_6706})

V_652 = Vertex(name = 'V_652',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS246, L.VVVVSS253, L.VVVVSS75 ],
               couplings = {(0,1):C.GC_6696,(0,2):C.GC_5303,(0,0):C.GC_6716})

V_653 = Vertex(name = 'V_653',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_4664,(0,3):C.GC_4672,(0,1):C.GC_5077,(0,0):C.GC_5086,(0,6):C.GC_6293,(0,7):C.GC_5218,(0,5):C.GC_5081,(0,2):C.GC_4673})

V_654 = Vertex(name = 'V_654',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_4756,(0,3):C.GC_4733,(0,1):C.GC_5189,(0,0):C.GC_5178,(0,6):C.GC_6404,(0,7):C.GC_5240,(0,5):C.GC_5169,(0,2):C.GC_4744})

V_655 = Vertex(name = 'V_655',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_4665,(0,5):C.GC_4670,(0,1):C.GC_5078,(0,6):C.GC_5082,(0,3):C.GC_5087,(0,7):C.GC_6294,(0,4):C.GC_5219,(0,2):C.GC_4674})

V_656 = Vertex(name = 'V_656',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_4757,(0,5):C.GC_4731,(0,1):C.GC_5190,(0,6):C.GC_5170,(0,3):C.GC_5179,(0,7):C.GC_6405,(0,4):C.GC_5241,(0,2):C.GC_4745})

V_657 = Vertex(name = 'V_657',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS47, L.VVVSSS50, L.VVVSSS51, L.VVVSSS55, L.VVVSSS58, L.VVVSSS59, L.VVVSSS60 ],
               couplings = {(0,5):C.GC_4669,(0,2):C.GC_6023,(0,3):C.GC_5084,(0,6):C.GC_6292,(0,1):C.GC_5218,(0,4):C.GC_4667,(0,0):C.GC_4673})

V_658 = Vertex(name = 'V_658',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS47, L.VVVSSS50, L.VVVSSS51, L.VVVSSS55, L.VVVSSS58, L.VVVSSS59, L.VVVSSS60 ],
               couplings = {(0,5):C.GC_4730,(0,2):C.GC_6125,(0,3):C.GC_5172,(0,6):C.GC_6403,(0,1):C.GC_5240,(0,4):C.GC_4759,(0,0):C.GC_4744})

V_659 = Vertex(name = 'V_659',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_4663,(0,0):C.GC_4668,(0,3):C.GC_5076,(0,5):C.GC_5080,(0,1):C.GC_6291,(0,4):C.GC_6297})

V_660 = Vertex(name = 'V_660',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_4755,(0,0):C.GC_4729,(0,3):C.GC_5188,(0,5):C.GC_5168,(0,1):C.GC_6402,(0,4):C.GC_6386})

V_661 = Vertex(name = 'V_661',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS100, L.VVVVSS109, L.VVVVSS11, L.VVVVSS134, L.VVVVSS176, L.VVVVSS177, L.VVVVSS184, L.VVVVSS185, L.VVVVSS209, L.VVVVSS220, L.VVVVSS242, L.VVVVSS243, L.VVVVSS248, L.VVVVSS252, L.VVVVSS256, L.VVVVSS259, L.VVVVSS286, L.VVVVSS291, L.VVVVSS300, L.VVVVSS309, L.VVVVSS337, L.VVVVSS341, L.VVVVSS344, L.VVVVSS358, L.VVVVSS384, L.VVVVSS385, L.VVVVSS388, L.VVVVSS390, L.VVVVSS42, L.VVVVSS431, L.VVVVSS46, L.VVVVSS53, L.VVVVSS76, L.VVVVSS82, L.VVVVSS87, L.VVVVSS98 ],
               couplings = {(0,9):C.GC_188,(0,8):C.GC_1792,(0,28):C.GC_3077,(0,10):C.GC_176,(0,11):C.GC_1788,(0,7):C.GC_2342,(0,5):C.GC_2344,(0,6):C.GC_2893,(0,4):C.GC_2896,(0,31):C.GC_2328,(0,0):C.GC_170,(0,1):C.GC_1785,(0,30):C.GC_2887,(0,23):C.GC_173,(0,20):C.GC_553,(0,22):C.GC_1786,(0,26):C.GC_2066,(0,32):C.GC_3075,(0,21):C.GC_182,(0,27):C.GC_1791,(0,25):C.GC_2338,(0,24):C.GC_2348,(0,17):C.GC_2891,(0,16):C.GC_2897,(0,2):C.GC_152,(0,18):C.GC_153,(0,29):C.GC_1789,(0,19):C.GC_2332,(0,14):C.GC_178,(0,33):C.GC_2889,(0,3):C.GC_151,(0,13):C.GC_6694,(0,12):C.GC_5309,(0,35):C.GC_3074,(0,15):C.GC_3076,(0,34):C.GC_6707})

V_662 = Vertex(name = 'V_662',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS248, L.VVVVSS252, L.VVVVSS256, L.VVVVSS259, L.VVVVSS286, L.VVVVSS300, L.VVVVSS309, L.VVVVSS344, L.VVVVSS358, L.VVVVSS384, L.VVVVSS431, L.VVVVSS76, L.VVVVSS82, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_477,(0,8):C.GC_2011,(0,12):C.GC_4232,(0,10):C.GC_2643,(0,5):C.GC_3005,(0,6):C.GC_494,(0,11):C.GC_1996,(0,7):C.GC_2624,(0,3):C.GC_454,(0,13):C.GC_2994,(0,0):C.GC_498,(0,2):C.GC_6697,(0,1):C.GC_5315,(0,4):C.GC_3146,(0,14):C.GC_6717})

V_663 = Vertex(name = 'V_663',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS246, L.VVVVSS253, L.VVVVSS75 ],
               couplings = {(0,1):C.GC_6693,(0,2):C.GC_5301,(0,0):C.GC_6706})

V_664 = Vertex(name = 'V_664',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS246, L.VVVVSS253, L.VVVVSS75 ],
               couplings = {(0,1):C.GC_6696,(0,2):C.GC_5303,(0,0):C.GC_6716})

V_665 = Vertex(name = 'V_665',
               particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS107, L.VVVVSS110, L.VVVVSS116, L.VVVVSS119, L.VVVVSS123, L.VVVVSS148, L.VVVVSS151, L.VVVVSS259, L.VVVVSS269, L.VVVVSS293, L.VVVVSS295, L.VVVVSS299, L.VVVVSS314, L.VVVVSS316, L.VVVVSS45, L.VVVVSS75, L.VVVVSS76, L.VVVVSS87, L.VVVVSS98 ],
               couplings = {(0,14):C.GC_2419,(0,5):C.GC_2910,(0,6):C.GC_3199,(0,9):C.GC_4349,(0,11):C.GC_4056,(0,16):C.GC_4438,(0,10):C.GC_2912,(0,3):C.GC_4057,(0,2):C.GC_2908,(0,13):C.GC_4058,(0,12):C.GC_2909,(0,0):C.GC_4063,(0,1):C.GC_2418,(0,4):C.GC_3198,(0,8):C.GC_4345,(0,15):C.GC_7046,(0,18):C.GC_4436,(0,7):C.GC_4440,(0,17):C.GC_7047})

V_666 = Vertex(name = 'V_666',
               particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259, L.VVVVSS269, L.VVVVSS293, L.VVVVSS295, L.VVVVSS299, L.VVVVSS314, L.VVVVSS316, L.VVVVSS75, L.VVVVSS76, L.VVVVSS87 ],
               couplings = {(0,2):C.GC_4382,(0,4):C.GC_4165,(0,8):C.GC_4456,(0,3):C.GC_3007,(0,6):C.GC_4155,(0,5):C.GC_2996,(0,1):C.GC_4378,(0,7):C.GC_7069,(0,0):C.GC_4446,(0,9):C.GC_7060})

V_667 = Vertex(name = 'V_667',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS38 ],
               couplings = {(0,0):C.GC_6529,(0,1):C.GC_6531})

V_668 = Vertex(name = 'V_668',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS38 ],
               couplings = {(0,0):C.GC_6604,(0,1):C.GC_6591})

V_669 = Vertex(name = 'V_669',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS134, L.VVVVSS171, L.VVVVSS175, L.VVVVSS183, L.VVVVSS184, L.VVVVSS190, L.VVVVSS191, L.VVVVSS194, L.VVVVSS199, L.VVVVSS24, L.VVVVSS265, L.VVVVSS268, L.VVVVSS27, L.VVVVSS279, L.VVVVSS280, L.VVVVSS288, L.VVVVSS291, L.VVVVSS300, L.VVVVSS301, L.VVVVSS303, L.VVVVSS321, L.VVVVSS322, L.VVVVSS323, L.VVVVSS324, L.VVVVSS325, L.VVVVSS326, L.VVVVSS334, L.VVVVSS335, L.VVVVSS42, L.VVVVSS49, L.VVVVSS50, L.VVVVSS52, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87, L.VVVVSS91, L.VVVVSS92 ],
               couplings = {(0,10):C.GC_1819,(0,7):C.GC_2415,(0,4):C.GC_3092,(0,29):C.GC_3197,(0,3):C.GC_266,(0,8):C.GC_2407,(0,6):C.GC_2870,(0,9):C.GC_2884,(0,2):C.GC_270,(0,5):C.GC_3090,(0,13):C.GC_1817,(0,32):C.GC_255,(0,37):C.GC_1807,(0,36):C.GC_3080,(0,21):C.GC_1822,(0,16):C.GC_3095,(0,26):C.GC_265,(0,28):C.GC_275,(0,15):C.GC_2834,(0,14):C.GC_2866,(0,23):C.GC_3017,(0,17):C.GC_3087,(0,24):C.GC_2413,(0,25):C.GC_2671,(0,22):C.GC_2878,(0,0):C.GC_2401,(0,31):C.GC_2837,(0,20):C.GC_261,(0,18):C.GC_2410,(0,19):C.GC_2840,(0,11):C.GC_1810,(0,27):C.GC_1812,(0,12):C.GC_3083,(0,1):C.GC_2404,(0,30):C.GC_2863,(0,34):C.GC_2875,(0,33):C.GC_6978,(0,35):C.GC_6981})

V_670 = Vertex(name = 'V_670',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS265, L.VVVVSS268, L.VVVVSS279, L.VVVVSS280, L.VVVVSS288, L.VVVVSS300, L.VVVVSS301, L.VVVVSS303, L.VVVVSS321, L.VVVVSS335, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_2048,(0,5):C.GC_3164,(0,10):C.GC_534,(0,4):C.GC_2981,(0,3):C.GC_2973,(0,8):C.GC_521,(0,6):C.GC_2569,(0,7):C.GC_2978,(0,1):C.GC_2031,(0,2):C.GC_3156,(0,0):C.GC_2594,(0,12):C.GC_2968,(0,11):C.GC_7015,(0,13):C.GC_7004})

V_671 = Vertex(name = 'V_671',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS134, L.VVVVSS172, L.VVVVSS178, L.VVVVSS182, L.VVVVSS184, L.VVVVSS190, L.VVVVSS192, L.VVVVSS193, L.VVVVSS200, L.VVVVSS24, L.VVVVSS265, L.VVVVSS267, L.VVVVSS27, L.VVVVSS279, L.VVVVSS280, L.VVVVSS289, L.VVVVSS291, L.VVVVSS300, L.VVVVSS301, L.VVVVSS304, L.VVVVSS321, L.VVVVSS322, L.VVVVSS323, L.VVVVSS334, L.VVVVSS386, L.VVVVSS387, L.VVVVSS42, L.VVVVSS426, L.VVVVSS427, L.VVVVSS47, L.VVVVSS49, L.VVVVSS50, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87, L.VVVVSS88, L.VVVVSS92 ],
               couplings = {(0,10):C.GC_1818,(0,7):C.GC_2416,(0,3):C.GC_3093,(0,27):C.GC_3196,(0,4):C.GC_267,(0,9):C.GC_2408,(0,6):C.GC_2872,(0,8):C.GC_2882,(0,2):C.GC_269,(0,5):C.GC_3089,(0,13):C.GC_1816,(0,30):C.GC_254,(0,37):C.GC_1806,(0,36):C.GC_3079,(0,21):C.GC_1821,(0,16):C.GC_3096,(0,28):C.GC_264,(0,29):C.GC_277,(0,15):C.GC_2833,(0,14):C.GC_2867,(0,23):C.GC_3018,(0,17):C.GC_3086,(0,25):C.GC_2412,(0,26):C.GC_2672,(0,22):C.GC_2877,(0,0):C.GC_2402,(0,32):C.GC_2838,(0,20):C.GC_262,(0,18):C.GC_2409,(0,19):C.GC_2839,(0,11):C.GC_1811,(0,24):C.GC_1813,(0,12):C.GC_3082,(0,1):C.GC_2403,(0,31):C.GC_2862,(0,34):C.GC_2876,(0,33):C.GC_6977,(0,35):C.GC_6980})

V_672 = Vertex(name = 'V_672',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS265, L.VVVVSS267, L.VVVVSS279, L.VVVVSS280, L.VVVVSS289, L.VVVVSS300, L.VVVVSS301, L.VVVVSS304, L.VVVVSS321, L.VVVVSS427, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_2047,(0,5):C.GC_3165,(0,10):C.GC_536,(0,4):C.GC_2982,(0,3):C.GC_2972,(0,8):C.GC_522,(0,6):C.GC_2568,(0,7):C.GC_2977,(0,1):C.GC_2032,(0,2):C.GC_3155,(0,0):C.GC_2595,(0,12):C.GC_2969,(0,11):C.GC_7014,(0,13):C.GC_7003})

V_673 = Vertex(name = 'V_673',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS134, L.VVVVSS171, L.VVVVSS175, L.VVVVSS183, L.VVVVSS184, L.VVVVSS190, L.VVVVSS191, L.VVVVSS194, L.VVVVSS199, L.VVVVSS24, L.VVVVSS265, L.VVVVSS268, L.VVVVSS27, L.VVVVSS279, L.VVVVSS280, L.VVVVSS288, L.VVVVSS291, L.VVVVSS300, L.VVVVSS301, L.VVVVSS303, L.VVVVSS321, L.VVVVSS322, L.VVVVSS323, L.VVVVSS324, L.VVVVSS325, L.VVVVSS326, L.VVVVSS334, L.VVVVSS335, L.VVVVSS42, L.VVVVSS49, L.VVVVSS50, L.VVVVSS52, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87, L.VVVVSS91, L.VVVVSS92 ],
               couplings = {(0,10):C.GC_1819,(0,7):C.GC_2417,(0,4):C.GC_3092,(0,29):C.GC_3195,(0,3):C.GC_268,(0,8):C.GC_2407,(0,6):C.GC_2870,(0,9):C.GC_2881,(0,2):C.GC_270,(0,5):C.GC_3088,(0,13):C.GC_1815,(0,32):C.GC_255,(0,37):C.GC_1807,(0,36):C.GC_3080,(0,21):C.GC_1822,(0,16):C.GC_3095,(0,26):C.GC_263,(0,28):C.GC_275,(0,15):C.GC_2834,(0,14):C.GC_2866,(0,23):C.GC_3017,(0,17):C.GC_3085,(0,24):C.GC_2413,(0,25):C.GC_2671,(0,22):C.GC_2878,(0,0):C.GC_2401,(0,31):C.GC_2837,(0,20):C.GC_261,(0,18):C.GC_2410,(0,19):C.GC_2840,(0,11):C.GC_1810,(0,27):C.GC_1814,(0,12):C.GC_3083,(0,1):C.GC_2404,(0,30):C.GC_2863,(0,34):C.GC_2875,(0,33):C.GC_6978,(0,35):C.GC_6981})

V_674 = Vertex(name = 'V_674',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS265, L.VVVVSS268, L.VVVVSS279, L.VVVVSS280, L.VVVVSS288, L.VVVVSS300, L.VVVVSS301, L.VVVVSS303, L.VVVVSS321, L.VVVVSS335, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_2048,(0,5):C.GC_3164,(0,10):C.GC_534,(0,4):C.GC_2981,(0,3):C.GC_2973,(0,8):C.GC_521,(0,6):C.GC_2569,(0,7):C.GC_2978,(0,1):C.GC_2031,(0,2):C.GC_3156,(0,0):C.GC_2594,(0,12):C.GC_2968,(0,11):C.GC_7015,(0,13):C.GC_7004})

V_675 = Vertex(name = 'V_675',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS134, L.VVVVSS172, L.VVVVSS178, L.VVVVSS182, L.VVVVSS184, L.VVVVSS190, L.VVVVSS192, L.VVVVSS193, L.VVVVSS200, L.VVVVSS24, L.VVVVSS265, L.VVVVSS267, L.VVVVSS27, L.VVVVSS279, L.VVVVSS280, L.VVVVSS289, L.VVVVSS291, L.VVVVSS300, L.VVVVSS301, L.VVVVSS304, L.VVVVSS321, L.VVVVSS322, L.VVVVSS323, L.VVVVSS334, L.VVVVSS386, L.VVVVSS387, L.VVVVSS42, L.VVVVSS426, L.VVVVSS427, L.VVVVSS47, L.VVVVSS49, L.VVVVSS50, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87, L.VVVVSS88, L.VVVVSS92 ],
               couplings = {(0,10):C.GC_1820,(0,7):C.GC_2416,(0,3):C.GC_3091,(0,27):C.GC_3196,(0,4):C.GC_267,(0,9):C.GC_2406,(0,6):C.GC_2869,(0,8):C.GC_2882,(0,2):C.GC_272,(0,5):C.GC_3089,(0,13):C.GC_1816,(0,30):C.GC_257,(0,37):C.GC_1808,(0,36):C.GC_3081,(0,21):C.GC_1823,(0,16):C.GC_3094,(0,28):C.GC_264,(0,29):C.GC_274,(0,15):C.GC_2835,(0,14):C.GC_2865,(0,23):C.GC_3016,(0,17):C.GC_3086,(0,25):C.GC_2414,(0,26):C.GC_2670,(0,22):C.GC_2879,(0,0):C.GC_2400,(0,32):C.GC_2836,(0,20):C.GC_259,(0,18):C.GC_2411,(0,19):C.GC_2841,(0,11):C.GC_1809,(0,24):C.GC_1813,(0,12):C.GC_3084,(0,1):C.GC_2405,(0,31):C.GC_2864,(0,34):C.GC_2874,(0,33):C.GC_6979,(0,35):C.GC_6982})

V_676 = Vertex(name = 'V_676',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS265, L.VVVVSS267, L.VVVVSS279, L.VVVVSS280, L.VVVVSS289, L.VVVVSS300, L.VVVVSS301, L.VVVVSS304, L.VVVVSS321, L.VVVVSS427, L.VVVVSS75, L.VVVVSS78, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_2049,(0,5):C.GC_3163,(0,10):C.GC_533,(0,4):C.GC_2980,(0,3):C.GC_2974,(0,8):C.GC_519,(0,6):C.GC_2570,(0,7):C.GC_2979,(0,1):C.GC_2030,(0,2):C.GC_3157,(0,0):C.GC_2593,(0,12):C.GC_2967,(0,11):C.GC_7016,(0,13):C.GC_7005})

V_677 = Vertex(name = 'V_677',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS101, L.VVVVSS11, L.VVVVSS134, L.VVVVSS139, L.VVVVSS140, L.VVVVSS141, L.VVVVSS142, L.VVVVSS166, L.VVVVSS184, L.VVVVSS186, L.VVVVSS242, L.VVVVSS244, L.VVVVSS259, L.VVVVSS285, L.VVVVSS290, L.VVVVSS291, L.VVVVSS300, L.VVVVSS307, L.VVVVSS341, L.VVVVSS351, L.VVVVSS383, L.VVVVSS389, L.VVVVSS391, L.VVVVSS42, L.VVVVSS430, L.VVVVSS54, L.VVVVSS55, L.VVVVSS75, L.VVVVSS76, L.VVVVSS81, L.VVVVSS87, L.VVVVSS98 ],
               couplings = {(0,6):C.GC_188,(0,3):C.GC_1794,(0,23):C.GC_3078,(0,10):C.GC_175,(0,11):C.GC_1788,(0,9):C.GC_2342,(0,5):C.GC_2345,(0,8):C.GC_2894,(0,4):C.GC_2896,(0,26):C.GC_2327,(0,28):C.GC_4074,(0,19):C.GC_552,(0,7):C.GC_1786,(0,22):C.GC_2066,(0,18):C.GC_183,(0,21):C.GC_1791,(0,14):C.GC_2338,(0,20):C.GC_2349,(0,15):C.GC_2892,(0,13):C.GC_2897,(0,1):C.GC_152,(0,0):C.GC_1784,(0,16):C.GC_153,(0,24):C.GC_1789,(0,17):C.GC_2331,(0,25):C.GC_2888,(0,29):C.GC_2889,(0,2):C.GC_151,(0,27):C.GC_6789,(0,31):C.GC_4073,(0,12):C.GC_4075,(0,30):C.GC_6793})

V_678 = Vertex(name = 'V_678',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS166, L.VVVVSS259, L.VVVVSS285, L.VVVVSS300, L.VVVVSS307, L.VVVVSS383, L.VVVVSS430, L.VVVVSS75, L.VVVVSS76, L.VVVVSS81, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_4233,(0,1):C.GC_2011,(0,6):C.GC_2644,(0,3):C.GC_3005,(0,4):C.GC_494,(0,7):C.GC_1996,(0,5):C.GC_2623,(0,10):C.GC_2994,(0,0):C.GC_498,(0,8):C.GC_6828,(0,2):C.GC_4146,(0,11):C.GC_6813})

V_679 = Vertex(name = 'V_679',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS101, L.VVVVSS11, L.VVVVSS134, L.VVVVSS139, L.VVVVSS140, L.VVVVSS141, L.VVVVSS142, L.VVVVSS166, L.VVVVSS184, L.VVVVSS186, L.VVVVSS242, L.VVVVSS244, L.VVVVSS259, L.VVVVSS285, L.VVVVSS290, L.VVVVSS291, L.VVVVSS300, L.VVVVSS307, L.VVVVSS341, L.VVVVSS351, L.VVVVSS383, L.VVVVSS389, L.VVVVSS391, L.VVVVSS42, L.VVVVSS430, L.VVVVSS54, L.VVVVSS55, L.VVVVSS75, L.VVVVSS76, L.VVVVSS81, L.VVVVSS87, L.VVVVSS98 ],
               couplings = {(0,6):C.GC_188,(0,3):C.GC_1794,(0,23):C.GC_3078,(0,10):C.GC_175,(0,11):C.GC_1788,(0,9):C.GC_2342,(0,5):C.GC_2345,(0,8):C.GC_2894,(0,4):C.GC_2896,(0,26):C.GC_2327,(0,28):C.GC_4074,(0,19):C.GC_552,(0,7):C.GC_1786,(0,22):C.GC_2066,(0,18):C.GC_183,(0,21):C.GC_1791,(0,14):C.GC_2338,(0,20):C.GC_2349,(0,15):C.GC_2892,(0,13):C.GC_2897,(0,1):C.GC_152,(0,0):C.GC_1784,(0,16):C.GC_153,(0,24):C.GC_1789,(0,17):C.GC_2331,(0,25):C.GC_2888,(0,29):C.GC_2889,(0,2):C.GC_151,(0,27):C.GC_6790,(0,31):C.GC_4073,(0,12):C.GC_4075,(0,30):C.GC_6794})

V_680 = Vertex(name = 'V_680',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS134, L.VVVVSS166, L.VVVVSS259, L.VVVVSS285, L.VVVVSS300, L.VVVVSS307, L.VVVVSS383, L.VVVVSS430, L.VVVVSS75, L.VVVVSS76, L.VVVVSS81, L.VVVVSS87 ],
               couplings = {(0,9):C.GC_4233,(0,1):C.GC_2011,(0,6):C.GC_2644,(0,3):C.GC_3005,(0,4):C.GC_494,(0,7):C.GC_1996,(0,5):C.GC_2623,(0,10):C.GC_2994,(0,0):C.GC_498,(0,8):C.GC_6831,(0,2):C.GC_4146,(0,11):C.GC_6814})

V_681 = Vertex(name = 'V_681',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS106, L.VVVVSS108, L.VVVVSS115, L.VVVVSS117, L.VVVVSS125, L.VVVVSS136, L.VVVVSS149, L.VVVVSS152, L.VVVVSS17, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS294, L.VVVVSS296, L.VVVVSS297, L.VVVVSS310, L.VVVVSS311, L.VVVVSS313, L.VVVVSS94, L.VVVVSS97 ],
               couplings = {(0,6):C.GC_301,(0,8):C.GC_1832,(0,7):C.GC_3066,(0,5):C.GC_3226,(0,13):C.GC_4061,(0,11):C.GC_4435,(0,14):C.GC_4342,(0,12):C.GC_3546,(0,3):C.GC_298,(0,2):C.GC_4343,(0,1):C.GC_3543,(0,19):C.GC_3064,(0,16):C.GC_4060,(0,17):C.GC_4344,(0,15):C.GC_3547,(0,18):C.GC_1830,(0,0):C.GC_4350,(0,4):C.GC_3224,(0,10):C.GC_4432,(0,9):C.GC_7075})

V_682 = Vertex(name = 'V_682',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS294, L.VVVVSS296, L.VVVVSS297, L.VVVVSS310, L.VVVVSS311, L.VVVVSS313 ],
               couplings = {(0,4):C.GC_4205,(0,2):C.GC_4455,(0,5):C.GC_4374,(0,3):C.GC_3729,(0,7):C.GC_4183,(0,8):C.GC_4371,(0,6):C.GC_3656,(0,1):C.GC_4452,(0,0):C.GC_7078})

V_683 = Vertex(name = 'V_683',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS102 ],
               couplings = {(0,0):C.GC_6646})

V_684 = Vertex(name = 'V_684',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS102 ],
               couplings = {(0,0):C.GC_6665})

V_685 = Vertex(name = 'V_685',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS30 ],
               couplings = {(0,0):C.GC_6647})

V_686 = Vertex(name = 'V_686',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS30 ],
               couplings = {(0,0):C.GC_6666})

V_687 = Vertex(name = 'V_687',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS90 ],
               couplings = {(0,0):C.GC_6645})

V_688 = Vertex(name = 'V_688',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS90 ],
               couplings = {(0,0):C.GC_6664})

V_689 = Vertex(name = 'V_689',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS40 ],
               couplings = {(0,0):C.GC_6648})

V_690 = Vertex(name = 'V_690',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS40 ],
               couplings = {(0,0):C.GC_6667})

V_691 = Vertex(name = 'V_691',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS125, L.VVVVSS126, L.VVVVSS136, L.VVVVSS137, L.VVVVSS160, L.VVVVSS170, L.VVVVSS173, L.VVVVSS187, L.VVVVSS20, L.VVVVSS202, L.VVVVSS203, L.VVVVSS238, L.VVVVSS239, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS419, L.VVVVSS420, L.VVVVSS421 ],
               couplings = {(0,11):C.GC_1829,(0,4):C.GC_3112,(0,8):C.GC_2391,(0,3):C.GC_3190,(0,6):C.GC_2855,(0,10):C.GC_286,(0,12):C.GC_294,(0,13):C.GC_1825,(0,7):C.GC_3516,(0,2):C.GC_2375,(0,0):C.GC_2843,(0,23):C.GC_2396,(0,16):C.GC_3193,(0,17):C.GC_4086,(0,24):C.GC_560,(0,9):C.GC_4089,(0,18):C.GC_4092,(0,19):C.GC_2381,(0,22):C.GC_3510,(0,20):C.GC_1232,(0,5):C.GC_2847,(0,21):C.GC_2860,(0,1):C.GC_3184,(0,15):C.GC_3187,(0,14):C.GC_7041})

V_692 = Vertex(name = 'V_692',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS160, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS420 ],
               couplings = {(0,9):C.GC_2649,(0,3):C.GC_3219,(0,4):C.GC_4167,(0,5):C.GC_4157,(0,6):C.GC_2629,(0,7):C.GC_2069,(0,0):C.GC_2992,(0,8):C.GC_3003,(0,2):C.GC_3213,(0,1):C.GC_7067})

V_693 = Vertex(name = 'V_693',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS125, L.VVVVSS126, L.VVVVSS136, L.VVVVSS137, L.VVVVSS160, L.VVVVSS170, L.VVVVSS173, L.VVVVSS187, L.VVVVSS20, L.VVVVSS202, L.VVVVSS203, L.VVVVSS238, L.VVVVSS239, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS419, L.VVVVSS420, L.VVVVSS421 ],
               couplings = {(0,11):C.GC_1828,(0,4):C.GC_3113,(0,8):C.GC_2390,(0,3):C.GC_3191,(0,6):C.GC_2853,(0,10):C.GC_285,(0,12):C.GC_295,(0,13):C.GC_1824,(0,7):C.GC_3514,(0,2):C.GC_2374,(0,0):C.GC_2842,(0,23):C.GC_2398,(0,16):C.GC_3192,(0,17):C.GC_4087,(0,24):C.GC_561,(0,9):C.GC_4088,(0,18):C.GC_4093,(0,19):C.GC_2383,(0,22):C.GC_3511,(0,20):C.GC_1230,(0,5):C.GC_2846,(0,21):C.GC_2859,(0,1):C.GC_3185,(0,15):C.GC_3188,(0,14):C.GC_7042})

V_694 = Vertex(name = 'V_694',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS160, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS420 ],
               couplings = {(0,9):C.GC_2651,(0,3):C.GC_3218,(0,4):C.GC_4166,(0,5):C.GC_4158,(0,6):C.GC_2631,(0,7):C.GC_2070,(0,0):C.GC_2991,(0,8):C.GC_3002,(0,2):C.GC_3214,(0,1):C.GC_7068})

V_695 = Vertex(name = 'V_695',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS125, L.VVVVSS126, L.VVVVSS136, L.VVVVSS137, L.VVVVSS160, L.VVVVSS170, L.VVVVSS173, L.VVVVSS187, L.VVVVSS20, L.VVVVSS202, L.VVVVSS203, L.VVVVSS238, L.VVVVSS239, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS419, L.VVVVSS420, L.VVVVSS421 ],
               couplings = {(0,11):C.GC_1827,(0,4):C.GC_3114,(0,8):C.GC_2391,(0,3):C.GC_3190,(0,6):C.GC_2852,(0,10):C.GC_286,(0,12):C.GC_297,(0,13):C.GC_1825,(0,7):C.GC_3515,(0,2):C.GC_2375,(0,0):C.GC_2843,(0,23):C.GC_2396,(0,16):C.GC_3193,(0,17):C.GC_4086,(0,24):C.GC_560,(0,9):C.GC_4089,(0,18):C.GC_4092,(0,19):C.GC_2381,(0,22):C.GC_3513,(0,20):C.GC_1229,(0,5):C.GC_2847,(0,21):C.GC_2860,(0,1):C.GC_3184,(0,15):C.GC_3187,(0,14):C.GC_7041})

V_696 = Vertex(name = 'V_696',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS160, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS420 ],
               couplings = {(0,9):C.GC_2649,(0,3):C.GC_3219,(0,4):C.GC_4167,(0,5):C.GC_4157,(0,6):C.GC_2629,(0,7):C.GC_2069,(0,0):C.GC_2992,(0,8):C.GC_3003,(0,2):C.GC_3213,(0,1):C.GC_7067})

V_697 = Vertex(name = 'V_697',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS125, L.VVVVSS126, L.VVVVSS136, L.VVVVSS137, L.VVVVSS160, L.VVVVSS170, L.VVVVSS173, L.VVVVSS187, L.VVVVSS20, L.VVVVSS202, L.VVVVSS203, L.VVVVSS238, L.VVVVSS239, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS419, L.VVVVSS420, L.VVVVSS421 ],
               couplings = {(0,11):C.GC_1828,(0,4):C.GC_3113,(0,8):C.GC_2393,(0,3):C.GC_3189,(0,6):C.GC_2853,(0,10):C.GC_287,(0,12):C.GC_295,(0,13):C.GC_1826,(0,7):C.GC_3517,(0,2):C.GC_2377,(0,0):C.GC_2845,(0,23):C.GC_2395,(0,16):C.GC_3194,(0,17):C.GC_4085,(0,24):C.GC_558,(0,9):C.GC_4090,(0,18):C.GC_4091,(0,19):C.GC_2378,(0,22):C.GC_3512,(0,20):C.GC_1231,(0,5):C.GC_2848,(0,21):C.GC_2861,(0,1):C.GC_3183,(0,15):C.GC_3186,(0,14):C.GC_7040})

V_698 = Vertex(name = 'V_698',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS160, L.VVVVSS252, L.VVVVSS262, L.VVVVSS282, L.VVVVSS283, L.VVVVSS302, L.VVVVSS317, L.VVVVSS401, L.VVVVSS418, L.VVVVSS420 ],
               couplings = {(0,9):C.GC_2648,(0,3):C.GC_3220,(0,4):C.GC_4168,(0,5):C.GC_4156,(0,6):C.GC_2626,(0,7):C.GC_2068,(0,0):C.GC_2993,(0,8):C.GC_3004,(0,2):C.GC_3212,(0,1):C.GC_7066})

V_699 = Vertex(name = 'V_699',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS108, L.VVVVSS147, L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4346,(0,3):C.GC_4426,(0,0):C.GC_4428,(0,4):C.GC_4431,(0,2):C.GC_7099})

V_700 = Vertex(name = 'V_700',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4450,(0,2):C.GC_4449,(0,0):C.GC_7114})

V_701 = Vertex(name = 'V_701',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS108, L.VVVVSS147, L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4347,(0,3):C.GC_4427,(0,0):C.GC_4429,(0,4):C.GC_4430,(0,2):C.GC_7098})

V_702 = Vertex(name = 'V_702',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4451,(0,2):C.GC_4448,(0,0):C.GC_7113})

V_703 = Vertex(name = 'V_703',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS108, L.VVVVSS147, L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4346,(0,3):C.GC_4426,(0,0):C.GC_4428,(0,4):C.GC_4431,(0,2):C.GC_7100})

V_704 = Vertex(name = 'V_704',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS252, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_4450,(0,2):C.GC_4449,(0,0):C.GC_7115})

V_705 = Vertex(name = 'V_705',
               particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS108, L.VVVVSS147, L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_2911,(0,2):C.GC_4065,(0,0):C.GC_4064,(0,3):C.GC_4066})

V_706 = Vertex(name = 'V_706',
               particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS294, L.VVVVSS310 ],
               couplings = {(0,0):C.GC_4231,(0,1):C.GC_4145})

V_707 = Vertex(name = 'V_707',
               particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS113, L.VVVVSS114, L.VVVVSS122, L.VVVVSS131, L.VVVVSS150, L.VVVVSS261, L.VVVVSS276, L.VVVVSS294, L.VVVVSS298, L.VVVVSS310, L.VVVVSS312 ],
               couplings = {(0,4):C.GC_300,(0,5):C.GC_3068,(0,8):C.GC_4062,(0,7):C.GC_4353,(0,9):C.GC_3545,(0,1):C.GC_299,(0,2):C.GC_3544,(0,3):C.GC_3065,(0,10):C.GC_4059,(0,11):C.GC_3548,(0,0):C.GC_4352,(0,6):C.GC_4354})

V_708 = Vertex(name = 'V_708',
               particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS261, L.VVVVSS276, L.VVVVSS294, L.VVVVSS298, L.VVVVSS310, L.VVVVSS312 ],
               couplings = {(0,2):C.GC_4206,(0,1):C.GC_4385,(0,3):C.GC_3728,(0,4):C.GC_4182,(0,5):C.GC_3657,(0,0):C.GC_4368})

V_709 = Vertex(name = 'V_709',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS111, L.VVVVSS129, L.VVVVSS132, L.VVVVSS154, L.VVVVSS155, L.VVVVSS261, L.VVVVSS271, L.VVVVSS276, L.VVVVSS318, L.VVVVSS319, L.VVVVSS320 ],
               couplings = {(0,2):C.GC_266,(0,3):C.GC_271,(0,4):C.GC_2871,(0,5):C.GC_2885,(0,1):C.GC_256,(0,10):C.GC_276,(0,8):C.GC_3522,(0,11):C.GC_3017,(0,7):C.GC_260,(0,9):C.GC_3529,(0,0):C.GC_3519,(0,6):C.GC_3525})

V_710 = Vertex(name = 'V_710',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS261, L.VVVVSS271, L.VVVVSS276, L.VVVVSS319 ],
               couplings = {(0,3):C.GC_535,(0,2):C.GC_3645,(0,1):C.GC_520,(0,0):C.GC_3634})

V_711 = Vertex(name = 'V_711',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS112, L.VVVVSS130, L.VVVVSS133, L.VVVVSS231, L.VVVVSS232, L.VVVVSS261, L.VVVVSS272, L.VVVVSS276, L.VVVVSS373, L.VVVVSS374, L.VVVVSS375 ],
               couplings = {(0,2):C.GC_267,(0,3):C.GC_272,(0,4):C.GC_2873,(0,5):C.GC_2883,(0,1):C.GC_258,(0,10):C.GC_278,(0,8):C.GC_3523,(0,11):C.GC_3018,(0,7):C.GC_259,(0,9):C.GC_3527,(0,0):C.GC_3520,(0,6):C.GC_3524})

V_712 = Vertex(name = 'V_712',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS261, L.VVVVSS272, L.VVVVSS276, L.VVVVSS374 ],
               couplings = {(0,3):C.GC_537,(0,2):C.GC_3644,(0,1):C.GC_519,(0,0):C.GC_3633})

V_713 = Vertex(name = 'V_713',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS102, L.VVVVSS120, L.VVVVSS143, L.VVVVSS144, L.VVVVSS153, L.VVVVSS214, L.VVVVSS218, L.VVVVSS234, L.VVVVSS235, L.VVVVSS257, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS348, L.VVVVSS349, L.VVVVSS35, L.VVVVSS352, L.VVVVSS354, L.VVVVSS355, L.VVVVSS356, L.VVVVSS357, L.VVVVSS361, L.VVVVSS44, L.VVVVSS61, L.VVVVSS64, L.VVVVSS76, L.VVVVSS79, L.VVVVSS98 ],
               couplings = {(0,24):C.GC_2392,(0,3):C.GC_2852,(0,7):C.GC_286,(0,5):C.GC_294,(0,25):C.GC_2389,(0,2):C.GC_2857,(0,8):C.GC_3104,(0,6):C.GC_3112,(0,1):C.GC_2376,(0,23):C.GC_2844,(0,13):C.GC_245,(0,22):C.GC_2397,(0,26):C.GC_3101,(0,15):C.GC_3172,(0,18):C.GC_292,(0,20):C.GC_559,(0,17):C.GC_2384,(0,21):C.GC_2849,(0,19):C.GC_2860,(0,14):C.GC_3110,(0,12):C.GC_283,(0,9):C.GC_2380,(0,4):C.GC_2847,(0,0):C.GC_248,(0,16):C.GC_280,(0,11):C.GC_251,(0,27):C.GC_289,(0,28):C.GC_3098,(0,10):C.GC_3107})

V_714 = Vertex(name = 'V_714',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS153, L.VVVVSS257, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS355, L.VVVVSS361, L.VVVVSS76, L.VVVVSS79 ],
               couplings = {(0,5):C.GC_500,(0,7):C.GC_2650,(0,8):C.GC_3153,(0,6):C.GC_3003,(0,4):C.GC_482,(0,1):C.GC_2628,(0,0):C.GC_2992,(0,3):C.GC_496,(0,9):C.GC_461,(0,2):C.GC_3148})

V_715 = Vertex(name = 'V_715',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS102, L.VVVVSS103, L.VVVVSS145, L.VVVVSS146, L.VVVVSS163, L.VVVVSS213, L.VVVVSS219, L.VVVVSS233, L.VVVVSS235, L.VVVVSS258, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS348, L.VVVVSS349, L.VVVVSS35, L.VVVVSS362, L.VVVVSS365, L.VVVVSS377, L.VVVVSS378, L.VVVVSS379, L.VVVVSS428, L.VVVVSS43, L.VVVVSS62, L.VVVVSS66, L.VVVVSS76, L.VVVVSS79, L.VVVVSS98 ],
               couplings = {(0,24):C.GC_2393,(0,3):C.GC_2854,(0,6):C.GC_285,(0,5):C.GC_296,(0,25):C.GC_2388,(0,2):C.GC_2856,(0,8):C.GC_3103,(0,7):C.GC_3113,(0,1):C.GC_2377,(0,23):C.GC_2845,(0,13):C.GC_244,(0,17):C.GC_2399,(0,26):C.GC_3100,(0,15):C.GC_3171,(0,19):C.GC_293,(0,21):C.GC_558,(0,18):C.GC_2385,(0,22):C.GC_2850,(0,20):C.GC_2861,(0,14):C.GC_3111,(0,12):C.GC_282,(0,9):C.GC_2379,(0,4):C.GC_2846,(0,0):C.GC_247,(0,16):C.GC_281,(0,11):C.GC_252,(0,27):C.GC_288,(0,28):C.GC_3097,(0,10):C.GC_3108})

V_716 = Vertex(name = 'V_716',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS163, L.VVVVSS258, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS362, L.VVVVSS378, L.VVVVSS76, L.VVVVSS79 ],
               couplings = {(0,5):C.GC_501,(0,6):C.GC_2652,(0,8):C.GC_3154,(0,7):C.GC_3004,(0,4):C.GC_483,(0,1):C.GC_2627,(0,0):C.GC_2991,(0,3):C.GC_497,(0,9):C.GC_460,(0,2):C.GC_3149})

V_717 = Vertex(name = 'V_717',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS111, L.VVVVSS129, L.VVVVSS132, L.VVVVSS154, L.VVVVSS155, L.VVVVSS261, L.VVVVSS271, L.VVVVSS276, L.VVVVSS318, L.VVVVSS319, L.VVVVSS320 ],
               couplings = {(0,2):C.GC_268,(0,3):C.GC_271,(0,4):C.GC_2871,(0,5):C.GC_2880,(0,1):C.GC_256,(0,10):C.GC_276,(0,8):C.GC_3522,(0,11):C.GC_3017,(0,7):C.GC_260,(0,9):C.GC_3528,(0,0):C.GC_3519,(0,6):C.GC_3525})

V_718 = Vertex(name = 'V_718',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS261, L.VVVVSS271, L.VVVVSS276, L.VVVVSS319 ],
               couplings = {(0,3):C.GC_535,(0,2):C.GC_3645,(0,1):C.GC_520,(0,0):C.GC_3634})

V_719 = Vertex(name = 'V_719',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS112, L.VVVVSS130, L.VVVVSS133, L.VVVVSS231, L.VVVVSS232, L.VVVVSS261, L.VVVVSS272, L.VVVVSS276, L.VVVVSS373, L.VVVVSS374, L.VVVVSS375 ],
               couplings = {(0,2):C.GC_267,(0,3):C.GC_269,(0,4):C.GC_2868,(0,5):C.GC_2883,(0,1):C.GC_253,(0,10):C.GC_273,(0,8):C.GC_3521,(0,11):C.GC_3016,(0,7):C.GC_262,(0,9):C.GC_3530,(0,0):C.GC_3518,(0,6):C.GC_3526})

V_720 = Vertex(name = 'V_720',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS261, L.VVVVSS272, L.VVVVSS276, L.VVVVSS374 ],
               couplings = {(0,3):C.GC_532,(0,2):C.GC_3646,(0,1):C.GC_522,(0,0):C.GC_3635})

V_721 = Vertex(name = 'V_721',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS102, L.VVVVSS120, L.VVVVSS143, L.VVVVSS144, L.VVVVSS153, L.VVVVSS214, L.VVVVSS218, L.VVVVSS234, L.VVVVSS235, L.VVVVSS257, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS348, L.VVVVSS349, L.VVVVSS35, L.VVVVSS352, L.VVVVSS354, L.VVVVSS355, L.VVVVSS356, L.VVVVSS357, L.VVVVSS361, L.VVVVSS44, L.VVVVSS61, L.VVVVSS64, L.VVVVSS76, L.VVVVSS79, L.VVVVSS98 ],
               couplings = {(0,24):C.GC_2392,(0,3):C.GC_2855,(0,7):C.GC_286,(0,5):C.GC_297,(0,25):C.GC_2387,(0,2):C.GC_2857,(0,8):C.GC_3104,(0,6):C.GC_3114,(0,1):C.GC_2376,(0,23):C.GC_2844,(0,13):C.GC_245,(0,22):C.GC_2397,(0,26):C.GC_3101,(0,15):C.GC_3172,(0,18):C.GC_292,(0,20):C.GC_559,(0,17):C.GC_2386,(0,21):C.GC_2851,(0,19):C.GC_2860,(0,14):C.GC_3110,(0,12):C.GC_283,(0,9):C.GC_2380,(0,4):C.GC_2847,(0,0):C.GC_248,(0,16):C.GC_280,(0,11):C.GC_251,(0,27):C.GC_289,(0,28):C.GC_3098,(0,10):C.GC_3107})

V_722 = Vertex(name = 'V_722',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS153, L.VVVVSS257, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS355, L.VVVVSS361, L.VVVVSS76, L.VVVVSS79 ],
               couplings = {(0,5):C.GC_500,(0,7):C.GC_2650,(0,8):C.GC_3153,(0,6):C.GC_3003,(0,4):C.GC_482,(0,1):C.GC_2628,(0,0):C.GC_2992,(0,3):C.GC_496,(0,9):C.GC_461,(0,2):C.GC_3148})

V_723 = Vertex(name = 'V_723',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS102, L.VVVVSS103, L.VVVVSS145, L.VVVVSS146, L.VVVVSS163, L.VVVVSS213, L.VVVVSS219, L.VVVVSS233, L.VVVVSS235, L.VVVVSS258, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS348, L.VVVVSS349, L.VVVVSS35, L.VVVVSS362, L.VVVVSS365, L.VVVVSS377, L.VVVVSS378, L.VVVVSS379, L.VVVVSS428, L.VVVVSS43, L.VVVVSS62, L.VVVVSS66, L.VVVVSS76, L.VVVVSS79, L.VVVVSS98 ],
               couplings = {(0,24):C.GC_2390,(0,3):C.GC_2854,(0,6):C.GC_287,(0,5):C.GC_296,(0,25):C.GC_2388,(0,2):C.GC_2858,(0,8):C.GC_3105,(0,7):C.GC_3113,(0,1):C.GC_2374,(0,23):C.GC_2842,(0,13):C.GC_246,(0,17):C.GC_2394,(0,26):C.GC_3102,(0,15):C.GC_3173,(0,19):C.GC_291,(0,21):C.GC_561,(0,18):C.GC_2385,(0,22):C.GC_2850,(0,20):C.GC_2859,(0,14):C.GC_3109,(0,12):C.GC_284,(0,9):C.GC_2382,(0,4):C.GC_2848,(0,0):C.GC_249,(0,16):C.GC_279,(0,11):C.GC_250,(0,27):C.GC_290,(0,28):C.GC_3099,(0,10):C.GC_3106})

V_724 = Vertex(name = 'V_724',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS163, L.VVVVSS258, L.VVVVSS259, L.VVVVSS266, L.VVVVSS284, L.VVVVSS292, L.VVVVSS362, L.VVVVSS378, L.VVVVSS76, L.VVVVSS79 ],
               couplings = {(0,5):C.GC_499,(0,6):C.GC_2647,(0,8):C.GC_3152,(0,7):C.GC_3002,(0,4):C.GC_481,(0,1):C.GC_2630,(0,0):C.GC_2993,(0,3):C.GC_495,(0,9):C.GC_462,(0,2):C.GC_3147})

V_725 = Vertex(name = 'V_725',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS165, L.VVVVSS241, L.VVVVSS255, L.VVVVSS259, L.VVVVSS339, L.VVVVSS340, L.VVVVSS347, L.VVVVSS429, L.VVVVSS60, L.VVVVSS67, L.VVVVSS72, L.VVVVSS76, L.VVVVSS84, L.VVVVSS98, L.VVVVSS99 ],
               couplings = {(0,9):C.GC_2339,(0,8):C.GC_2344,(0,1):C.GC_175,(0,10):C.GC_187,(0,14):C.GC_2326,(0,0):C.GC_172,(0,5):C.GC_551,(0,11):C.GC_1767,(0,6):C.GC_2350,(0,4):C.GC_183,(0,2):C.GC_2330,(0,12):C.GC_2335,(0,13):C.GC_818,(0,7):C.GC_179,(0,3):C.GC_1769})

V_726 = Vertex(name = 'V_726',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS165, L.VVVVSS255, L.VVVVSS259, L.VVVVSS347, L.VVVVSS429, L.VVVVSS76 ],
               couplings = {(0,0):C.GC_476,(0,5):C.GC_2024,(0,3):C.GC_2645,(0,1):C.GC_2622,(0,4):C.GC_455,(0,2):C.GC_2023})

V_727 = Vertex(name = 'V_727',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS165, L.VVVVSS241, L.VVVVSS255, L.VVVVSS259, L.VVVVSS339, L.VVVVSS340, L.VVVVSS347, L.VVVVSS429, L.VVVVSS60, L.VVVVSS67, L.VVVVSS72, L.VVVVSS76, L.VVVVSS84, L.VVVVSS98, L.VVVVSS99 ],
               couplings = {(0,9):C.GC_2339,(0,8):C.GC_2344,(0,1):C.GC_175,(0,10):C.GC_187,(0,14):C.GC_2326,(0,0):C.GC_172,(0,5):C.GC_551,(0,11):C.GC_1767,(0,6):C.GC_2350,(0,4):C.GC_183,(0,2):C.GC_2330,(0,12):C.GC_2335,(0,13):C.GC_818,(0,7):C.GC_179,(0,3):C.GC_1769})

V_728 = Vertex(name = 'V_728',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS165, L.VVVVSS255, L.VVVVSS259, L.VVVVSS347, L.VVVVSS429, L.VVVVSS76 ],
               couplings = {(0,0):C.GC_476,(0,5):C.GC_2024,(0,3):C.GC_2645,(0,1):C.GC_2622,(0,4):C.GC_455,(0,2):C.GC_2023})

V_729 = Vertex(name = 'V_729',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS128, L.VVVVSS167, L.VVVVSS168, L.VVVVSS18, L.VVVVSS196, L.VVVVSS227, L.VVVVSS237, L.VVVVSS264, L.VVVVSS273, L.VVVVSS277, L.VVVVSS278, L.VVVVSS281, L.VVVVSS30, L.VVVVSS329, L.VVVVSS34, L.VVVVSS346, L.VVVVSS39, L.VVVVSS396, L.VVVVSS397, L.VVVVSS398, L.VVVVSS409, L.VVVVSS433, L.VVVVSS93, L.VVVVSS95 ],
               couplings = {(0,2):C.GC_163,(0,1):C.GC_166,(0,12):C.GC_1777,(0,3):C.GC_1780,(0,6):C.GC_2355,(0,4):C.GC_2362,(0,5):C.GC_2902,(0,0):C.GC_2907,(0,22):C.GC_1770,(0,23):C.GC_154,(0,17):C.GC_162,(0,20):C.GC_169,(0,11):C.GC_1776,(0,13):C.GC_1783,(0,18):C.GC_2359,(0,19):C.GC_2668,(0,15):C.GC_2904,(0,9):C.GC_2322,(0,10):C.GC_2353,(0,7):C.GC_1773,(0,8):C.GC_158,(0,14):C.GC_1228,(0,16):C.GC_2324,(0,21):C.GC_2357})

V_730 = Vertex(name = 'V_730',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS264, L.VVVVSS273, L.VVVVSS277, L.VVVVSS278, L.VVVVSS329, L.VVVVSS346, L.VVVVSS39, L.VVVVSS409, L.VVVVSS433 ],
               couplings = {(0,7):C.GC_531,(0,4):C.GC_2046,(0,5):C.GC_3020,(0,2):C.GC_2609,(0,3):C.GC_2591,(0,0):C.GC_2028,(0,1):C.GC_517,(0,6):C.GC_2608,(0,8):C.GC_2567})

V_731 = Vertex(name = 'V_731',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS128, L.VVVVSS167, L.VVVVSS168, L.VVVVSS18, L.VVVVSS196, L.VVVVSS227, L.VVVVSS237, L.VVVVSS264, L.VVVVSS273, L.VVVVSS277, L.VVVVSS278, L.VVVVSS281, L.VVVVSS30, L.VVVVSS329, L.VVVVSS34, L.VVVVSS346, L.VVVVSS39, L.VVVVSS396, L.VVVVSS397, L.VVVVSS398, L.VVVVSS409, L.VVVVSS433, L.VVVVSS93, L.VVVVSS95 ],
               couplings = {(0,2):C.GC_163,(0,1):C.GC_166,(0,12):C.GC_1777,(0,3):C.GC_1780,(0,6):C.GC_2355,(0,4):C.GC_2362,(0,5):C.GC_2902,(0,0):C.GC_2907,(0,22):C.GC_1770,(0,23):C.GC_154,(0,17):C.GC_162,(0,20):C.GC_169,(0,11):C.GC_1776,(0,13):C.GC_1783,(0,18):C.GC_2359,(0,19):C.GC_2668,(0,15):C.GC_2904,(0,9):C.GC_2322,(0,10):C.GC_2353,(0,7):C.GC_1773,(0,8):C.GC_158,(0,14):C.GC_1228,(0,16):C.GC_2324,(0,21):C.GC_2357})

V_732 = Vertex(name = 'V_732',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS264, L.VVVVSS273, L.VVVVSS277, L.VVVVSS278, L.VVVVSS329, L.VVVVSS346, L.VVVVSS39, L.VVVVSS409, L.VVVVSS433 ],
               couplings = {(0,7):C.GC_531,(0,4):C.GC_2046,(0,5):C.GC_3020,(0,2):C.GC_2609,(0,3):C.GC_2591,(0,0):C.GC_2028,(0,1):C.GC_517,(0,6):C.GC_2608,(0,8):C.GC_2567})

V_733 = Vertex(name = 'V_733',
               particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259, L.VVVVSS41, L.VVVVSS76, L.VVVVSS98 ],
               couplings = {(0,1):C.GC_4348,(0,2):C.GC_4439,(0,3):C.GC_4437,(0,0):C.GC_4441})

V_734 = Vertex(name = 'V_734',
               particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259, L.VVVVSS76 ],
               couplings = {(0,1):C.GC_4457,(0,0):C.GC_4447})

V_735 = Vertex(name = 'V_735',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259, L.VVVVSS41, L.VVVVSS76, L.VVVVSS98 ],
               couplings = {(0,1):C.GC_4348,(0,2):C.GC_4439,(0,3):C.GC_4437,(0,0):C.GC_4441})

V_736 = Vertex(name = 'V_736',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259, L.VVVVSS76 ],
               couplings = {(0,1):C.GC_4457,(0,0):C.GC_4447})

V_737 = Vertex(name = 'V_737',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS106, L.VVVVSS124, L.VVVVSS125, L.VVVVSS127, L.VVVVSS135, L.VVVVSS136, L.VVVVSS138, L.VVVVSS17, L.VVVVSS262, L.VVVVSS282, L.VVVVSS94 ],
               couplings = {(0,4):C.GC_301,(0,7):C.GC_1833,(0,6):C.GC_3067,(0,5):C.GC_3227,(0,9):C.GC_4434,(0,1):C.GC_298,(0,10):C.GC_1831,(0,0):C.GC_4351,(0,3):C.GC_3063,(0,2):C.GC_3225,(0,8):C.GC_4433})

V_738 = Vertex(name = 'V_738',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS262, L.VVVVSS282 ],
               couplings = {(0,1):C.GC_4454,(0,0):C.GC_4453})

V_739 = Vertex(name = 'V_739',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS106, L.VVVVSS124, L.VVVVSS125, L.VVVVSS127, L.VVVVSS135, L.VVVVSS136, L.VVVVSS138, L.VVVVSS17, L.VVVVSS262, L.VVVVSS282, L.VVVVSS94 ],
               couplings = {(0,4):C.GC_301,(0,7):C.GC_1833,(0,6):C.GC_3067,(0,5):C.GC_3227,(0,9):C.GC_4434,(0,1):C.GC_298,(0,10):C.GC_1831,(0,0):C.GC_4351,(0,3):C.GC_3063,(0,2):C.GC_3225,(0,8):C.GC_4433})

V_740 = Vertex(name = 'V_740',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS262, L.VVVVSS282 ],
               couplings = {(0,1):C.GC_4454,(0,0):C.GC_4453})

V_741 = Vertex(name = 'V_741',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS206, L.VVVVSS369, L.VVVVSS5, L.VVVVSS56, L.VVVVSS63, L.VVVVSS65, L.VVVVSS73, L.VVVVSS85, L.VVVVSS86 ],
               couplings = {(0,6):C.GC_174,(0,0):C.GC_186,(0,5):C.GC_2341,(0,4):C.GC_2343,(0,2):C.GC_2325,(0,8):C.GC_181,(0,3):C.GC_2333,(0,1):C.GC_2336,(0,7):C.GC_2347})

V_742 = Vertex(name = 'V_742',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS56, L.VVVVSS85, L.VVVVSS86 ],
               couplings = {(0,2):C.GC_554,(0,0):C.GC_2625,(0,1):C.GC_2642})

V_743 = Vertex(name = 'V_743',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS157, L.VVVVSS16, L.VVVVSS169, L.VVVVSS180, L.VVVVSS197, L.VVVVSS222, L.VVVVSS225, L.VVVVSS23, L.VVVVSS26, L.VVVVSS3, L.VVVVSS333, L.VVVVSS364, L.VVVVSS37, L.VVVVSS4, L.VVVVSS405, L.VVVVSS407, L.VVVVSS410, L.VVVVSS411, L.VVVVSS7 ],
               couplings = {(0,1):C.GC_1778,(0,8):C.GC_1781,(0,4):C.GC_2356,(0,5):C.GC_2361,(0,2):C.GC_167,(0,6):C.GC_2906,(0,3):C.GC_164,(0,9):C.GC_1772,(0,13):C.GC_156,(0,18):C.GC_3531,(0,16):C.GC_168,(0,7):C.GC_819,(0,10):C.GC_1775,(0,11):C.GC_3532,(0,17):C.GC_2358,(0,14):C.GC_2669,(0,0):C.GC_157,(0,12):C.GC_3533,(0,15):C.GC_161})

V_744 = Vertex(name = 'V_744',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS157, L.VVVVSS23, L.VVVVSS364, L.VVVVSS37, L.VVVVSS410 ],
               couplings = {(0,4):C.GC_530,(0,1):C.GC_925,(0,2):C.GC_3727,(0,0):C.GC_516,(0,3):C.GC_3636})

V_745 = Vertex(name = 'V_745',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS13, L.VVVVVS137, L.VVVVVS138, L.VVVVVS139, L.VVVVVS18, L.VVVVVS185, L.VVVVVS194, L.VVVVVS195, L.VVVVVS22, L.VVVVVS35, L.VVVVVS58, L.VVVVVS66 ],
               couplings = {(0,0):C.GC_5686,(0,9):C.GC_5075,(0,8):C.GC_5070,(0,11):C.GC_4839,(0,4):C.GC_5067,(0,1):C.GC_4841,(0,2):C.GC_4843,(0,3):C.GC_4846,(0,7):C.GC_5068,(0,10):C.GC_5071,(0,5):C.GC_5157,(0,6):C.GC_5074})

V_746 = Vertex(name = 'V_746',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS137, L.VVVVVS139, L.VVVVVS195, L.VVVVVS58 ],
               couplings = {(0,0):C.GC_4916,(0,1):C.GC_4924,(0,2):C.GC_5125,(0,3):C.GC_5116})

V_747 = Vertex(name = 'V_747',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS101, L.VVVVVS102, L.VVVVVS107, L.VVVVVS109, L.VVVVVS112, L.VVVVVS116, L.VVVVVS124, L.VVVVVS125, L.VVVVVS126, L.VVVVVS128, L.VVVVVS147, L.VVVVVS150, L.VVVVVS155, L.VVVVVS170, L.VVVVVS192, L.VVVVVS197, L.VVVVVS204, L.VVVVVS206, L.VVVVVS216, L.VVVVVS27, L.VVVVVS3, L.VVVVVS4, L.VVVVVS61, L.VVVVVS95 ],
               couplings = {(0,20):C.GC_4652,(0,2):C.GC_4858,(0,1):C.GC_5061,(0,4):C.GC_4533,(0,0):C.GC_4852,(0,5):C.GC_4538,(0,3):C.GC_5062,(0,21):C.GC_4849,(0,19):C.GC_5055,(0,11):C.GC_4531,(0,16):C.GC_4596,(0,6):C.GC_4655,(0,13):C.GC_5059,(0,15):C.GC_4536,(0,17):C.GC_4850,(0,9):C.GC_4854,(0,14):C.GC_4857,(0,18):C.GC_4937,(0,12):C.GC_5065,(0,8):C.GC_5057,(0,22):C.GC_4650,(0,7):C.GC_4651,(0,23):C.GC_4529,(0,10):C.GC_4535})

V_748 = Vertex(name = 'V_748',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS124, L.VVVVVS125, L.VVVVVS126, L.VVVVVS128, L.VVVVVS147, L.VVVVVS150, L.VVVVVS155, L.VVVVVS206 ],
               couplings = {(0,5):C.GC_4574,(0,0):C.GC_4712,(0,7):C.GC_4908,(0,3):C.GC_4897,(0,6):C.GC_5152,(0,2):C.GC_5140,(0,1):C.GC_4709,(0,4):C.GC_4566})

V_749 = Vertex(name = 'V_749',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS11, L.VVVVVS136, L.VVVVVS140, L.VVVVVS169, L.VVVVVS17, L.VVVVVS193, L.VVVVVS196, L.VVVVVS198, L.VVVVVS26, L.VVVVVS29, L.VVVVVS78, L.VVVVVS9 ],
               couplings = {(0,11):C.GC_5688,(0,10):C.GC_5075,(0,4):C.GC_5070,(0,8):C.GC_4838,(0,0):C.GC_5066,(0,9):C.GC_4842,(0,2):C.GC_4843,(0,1):C.GC_4845,(0,7):C.GC_5069,(0,3):C.GC_5072,(0,5):C.GC_5158,(0,6):C.GC_5073})

V_750 = Vertex(name = 'V_750',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS136, L.VVVVVS169, L.VVVVVS198, L.VVVVVS29 ],
               couplings = {(0,3):C.GC_4917,(0,0):C.GC_4923,(0,2):C.GC_5124,(0,1):C.GC_5117})

V_751 = Vertex(name = 'V_751',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1, L.VVVVVS134, L.VVVVVS152, L.VVVVVS156, L.VVVVVS157, L.VVVVVS171, L.VVVVVS2, L.VVVVVS205, L.VVVVVS211, L.VVVVVS212, L.VVVVVS213, L.VVVVVS214, L.VVVVVS30, L.VVVVVS39, L.VVVVVS41, L.VVVVVS45, L.VVVVVS49, L.VVVVVS50, L.VVVVVS55, L.VVVVVS7, L.VVVVVS87, L.VVVVVS88, L.VVVVVS93, L.VVVVVS99 ],
               couplings = {(0,0):C.GC_4653,(0,22):C.GC_4858,(0,14):C.GC_5061,(0,23):C.GC_4533,(0,20):C.GC_4537,(0,21):C.GC_4853,(0,15):C.GC_5063,(0,6):C.GC_4848,(0,19):C.GC_5056,(0,12):C.GC_4650,(0,2):C.GC_4532,(0,7):C.GC_4597,(0,16):C.GC_4651,(0,17):C.GC_4654,(0,5):C.GC_5060,(0,9):C.GC_4536,(0,10):C.GC_4851,(0,8):C.GC_4856,(0,11):C.GC_4938,(0,3):C.GC_5058,(0,4):C.GC_5064,(0,1):C.GC_4855,(0,13):C.GC_4530,(0,18):C.GC_4534})

V_752 = Vertex(name = 'V_752',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS134, L.VVVVVS152, L.VVVVVS156, L.VVVVVS157, L.VVVVVS213, L.VVVVVS49, L.VVVVVS50, L.VVVVVS55 ],
               couplings = {(0,1):C.GC_4573,(0,5):C.GC_4709,(0,6):C.GC_4711,(0,4):C.GC_4907,(0,2):C.GC_5141,(0,3):C.GC_5151,(0,0):C.GC_4898,(0,7):C.GC_4565})

V_753 = Vertex(name = 'V_753',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS100, L.VVVVVS182, L.VVVVVS183, L.VVVVVS184, L.VVVVVS31, L.VVVVVS40, L.VVVVVS48, L.VVVVVS59, L.VVVVVS97 ],
               couplings = {(0,0):C.GC_4820,(0,8):C.GC_4825,(0,3):C.GC_4819,(0,2):C.GC_4823,(0,1):C.GC_4935,(0,4):C.GC_4638,(0,5):C.GC_4818,(0,6):C.GC_5515,(0,7):C.GC_4821})

V_754 = Vertex(name = 'V_754',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS184, L.VVVVVS48, L.VVVVVS59 ],
               couplings = {(0,0):C.GC_4906,(0,1):C.GC_5536,(0,2):C.GC_4896})

V_755 = Vertex(name = 'V_755',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS10, L.VVVVVS11, L.VVVVVS151, L.VVVVVS153, L.VVVVVS154, L.VVVVVS168, L.VVVVVS181, L.VVVVVS25, L.VVVVVS71, L.VVVVVS79, L.VVVVVS80 ],
               couplings = {(0,10):C.GC_4641,(0,7):C.GC_4644,(0,9):C.GC_5089,(0,8):C.GC_5090,(0,1):C.GC_4639,(0,0):C.GC_4817,(0,3):C.GC_4640,(0,5):C.GC_4642,(0,2):C.GC_6026,(0,6):C.GC_4714,(0,4):C.GC_5683})

V_756 = Vertex(name = 'V_756',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS151, L.VVVVVS153, L.VVVVVS154, L.VVVVVS168 ],
               couplings = {(0,1):C.GC_4703,(0,3):C.GC_4698,(0,0):C.GC_5160,(0,2):C.GC_5753})

V_757 = Vertex(name = 'V_757',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS32, L.VVVVVS34, L.VVVVVS36, L.VVVVVS51, L.VVVVVS53, L.VVVVVS54, L.VVVVVS6 ],
               couplings = {(0,2):C.GC_6537,(0,1):C.GC_6541,(0,6):C.GC_6286,(0,0):C.GC_6282,(0,4):C.GC_6538,(0,5):C.GC_6288,(0,3):C.GC_6283})

V_758 = Vertex(name = 'V_758',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS51, L.VVVVVS53, L.VVVVVS54 ],
               couplings = {(0,1):C.GC_6586,(0,2):C.GC_6359,(0,0):C.GC_6352})

V_759 = Vertex(name = 'V_759',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS13, L.VVVVVS138, L.VVVVVS141, L.VVVVVS142, L.VVVVVS16, L.VVVVVS160, L.VVVVVS163, L.VVVVVS164, L.VVVVVS173, L.VVVVVS175, L.VVVVVS19, L.VVVVVS20, L.VVVVVS21, L.VVVVVS33, L.VVVVVS56, L.VVVVVS67, L.VVVVVS69, L.VVVVVS74, L.VVVVVS81, L.VVVVVS82 ],
               couplings = {(0,12):C.GC_4549,(0,11):C.GC_6535,(0,0):C.GC_4870,(0,18):C.GC_6289,(0,19):C.GC_5214,(0,13):C.GC_5289,(0,15):C.GC_5104,(0,10):C.GC_5264,(0,4):C.GC_4545,(0,17):C.GC_4867,(0,16):C.GC_5259,(0,14):C.GC_4546,(0,6):C.GC_4547,(0,7):C.GC_4551,(0,3):C.GC_5710,(0,1):C.GC_4868,(0,9):C.GC_6290,(0,8):C.GC_5265,(0,5):C.GC_5261,(0,2):C.GC_5260})

V_760 = Vertex(name = 'V_760',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141, L.VVVVVS142, L.VVVVVS164, L.VVVVVS173, L.VVVVVS175, L.VVVVVS56 ],
               couplings = {(0,5):C.GC_4587,(0,2):C.GC_4590,(0,1):C.GC_5755,(0,4):C.GC_6377,(0,3):C.GC_5275,(0,0):C.GC_5273})

V_761 = Vertex(name = 'V_761',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS14, L.VVVVVS140, L.VVVVVS143, L.VVVVVS144, L.VVVVVS203, L.VVVVVS70, L.VVVVVS75, L.VVVVVS76, L.VVVVVS9 ],
               couplings = {(0,8):C.GC_5702,(0,0):C.GC_5703,(0,7):C.GC_6303,(0,5):C.GC_6308,(0,1):C.GC_5701,(0,3):C.GC_5704,(0,4):C.GC_6306,(0,6):C.GC_5699,(0,2):C.GC_5700})

V_762 = Vertex(name = 'V_762',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS143, L.VVVVVS144, L.VVVVVS203 ],
               couplings = {(0,1):C.GC_5754,(0,2):C.GC_6378,(0,0):C.GC_5751})

V_763 = Vertex(name = 'V_763',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS108, L.VVVVVS110, L.VVVVVS113, L.VVVVVS119, L.VVVVVS120, L.VVVVVS122, L.VVVVVS123, L.VVVVVS129, L.VVVVVS130, L.VVVVVS132, L.VVVVVS133, L.VVVVVS135, L.VVVVVS146, L.VVVVVS161, L.VVVVVS37, L.VVVVVS42, L.VVVVVS43, L.VVVVVS44, L.VVVVVS5, L.VVVVVS52, L.VVVVVS62, L.VVVVVS64, L.VVVVVS65, L.VVVVVS94 ],
               couplings = {(0,2):C.GC_5706,(0,18):C.GC_4678,(0,0):C.GC_5099,(0,1):C.GC_5224,(0,17):C.GC_4526,(0,16):C.GC_4866,(0,14):C.GC_5258,(0,15):C.GC_6299,(0,19):C.GC_6527,(0,10):C.GC_4595,(0,9):C.GC_4939,(0,13):C.GC_6298,(0,20):C.GC_4676,(0,22):C.GC_5097,(0,21):C.GC_5222,(0,11):C.GC_5708,(0,5):C.GC_4677,(0,3):C.GC_4679,(0,4):C.GC_5098,(0,7):C.GC_5100,(0,8):C.GC_5225,(0,6):C.GC_5223,(0,23):C.GC_6526,(0,12):C.GC_6528})

V_764 = Vertex(name = 'V_764',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS119, L.VVVVVS120, L.VVVVVS122, L.VVVVVS123, L.VVVVVS129, L.VVVVVS130, L.VVVVVS146, L.VVVVVS52 ],
               couplings = {(0,7):C.GC_6585,(0,2):C.GC_4710,(0,0):C.GC_4713,(0,1):C.GC_5142,(0,4):C.GC_5153,(0,5):C.GC_5238,(0,3):C.GC_5233,(0,6):C.GC_6556})

V_765 = Vertex(name = 'V_765',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS32, L.VVVVVS34, L.VVVVVS36, L.VVVVVS51, L.VVVVVS53, L.VVVVVS54, L.VVVVVS6 ],
               couplings = {(0,2):C.GC_6537,(0,1):C.GC_6540,(0,6):C.GC_6287,(0,0):C.GC_6282,(0,4):C.GC_6539,(0,5):C.GC_6288,(0,3):C.GC_6283})

V_766 = Vertex(name = 'V_766',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS51, L.VVVVVS53, L.VVVVVS54 ],
               couplings = {(0,1):C.GC_6586,(0,2):C.GC_6359,(0,0):C.GC_6352})

V_767 = Vertex(name = 'V_767',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS13, L.VVVVVS138, L.VVVVVS141, L.VVVVVS142, L.VVVVVS16, L.VVVVVS160, L.VVVVVS163, L.VVVVVS164, L.VVVVVS173, L.VVVVVS175, L.VVVVVS19, L.VVVVVS20, L.VVVVVS21, L.VVVVVS33, L.VVVVVS56, L.VVVVVS67, L.VVVVVS69, L.VVVVVS74, L.VVVVVS81, L.VVVVVS82 ],
               couplings = {(0,12):C.GC_4550,(0,11):C.GC_6535,(0,0):C.GC_4871,(0,18):C.GC_6289,(0,19):C.GC_5215,(0,13):C.GC_5290,(0,15):C.GC_5103,(0,10):C.GC_5263,(0,4):C.GC_4545,(0,17):C.GC_4867,(0,16):C.GC_5259,(0,14):C.GC_4546,(0,6):C.GC_4548,(0,7):C.GC_4551,(0,3):C.GC_5710,(0,1):C.GC_4869,(0,9):C.GC_6290,(0,8):C.GC_5265,(0,5):C.GC_5262,(0,2):C.GC_5260})

V_768 = Vertex(name = 'V_768',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141, L.VVVVVS142, L.VVVVVS164, L.VVVVVS173, L.VVVVVS175, L.VVVVVS56 ],
               couplings = {(0,5):C.GC_4587,(0,2):C.GC_4590,(0,1):C.GC_5755,(0,4):C.GC_6377,(0,3):C.GC_5275,(0,0):C.GC_5273})

V_769 = Vertex(name = 'V_769',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS161, L.VVVVSS162, L.VVVVSS164, L.VVVVSS174, L.VVVVSS181, L.VVVVSS206, L.VVVVSS208, L.VVVVSS366, L.VVVVSS367, L.VVVVSS417, L.VVVVSS57, L.VVVVSS58, L.VVVVSS6, L.VVVVSS69, L.VVVVSS74, L.VVVVSS8, L.VVVVSS9 ],
               couplings = {(0,5):C.GC_186,(0,6):C.GC_1793,(0,14):C.GC_1787,(0,13):C.GC_2340,(0,3):C.GC_2346,(0,4):C.GC_2895,(0,16):C.GC_2329,(0,15):C.GC_820,(0,12):C.GC_2886,(0,7):C.GC_821,(0,11):C.GC_822,(0,8):C.GC_2067,(0,9):C.GC_2337,(0,2):C.GC_1790,(0,0):C.GC_1227,(0,1):C.GC_2898,(0,10):C.GC_2890})

V_770 = Vertex(name = 'V_770',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS161, L.VVVVSS162, L.VVVVSS366, L.VVVVSS57, L.VVVVSS58 ],
               couplings = {(0,2):C.GC_921,(0,4):C.GC_917,(0,0):C.GC_1305,(0,1):C.GC_3006,(0,3):C.GC_2995})

V_771 = Vertex(name = 'V_771',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS117, L.VVVVVS15, L.VVVVVS159, L.VVVVVS160, L.VVVVVS165, L.VVVVVS18, L.VVVVVS186, L.VVVVVS188, L.VVVVVS19, L.VVVVVS200, L.VVVVVS207, L.VVVVVS209, L.VVVVVS210, L.VVVVVS24, L.VVVVVS33, L.VVVVVS57, L.VVVVVS77, L.VVVVVS83 ],
               couplings = {(0,16):C.GC_4661,(0,17):C.GC_5070,(0,14):C.GC_5217,(0,8):C.GC_5685,(0,1):C.GC_4837,(0,5):C.GC_5067,(0,13):C.GC_5075,(0,4):C.GC_5068,(0,15):C.GC_5071,(0,12):C.GC_5073,(0,10):C.GC_5159,(0,3):C.GC_4527,(0,2):C.GC_4844,(0,11):C.GC_4656,(0,7):C.GC_4660,(0,9):C.GC_4716,(0,0):C.GC_4841,(0,6):C.GC_4658})

V_772 = Vertex(name = 'V_772',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS117, L.VVVVVS159, L.VVVVVS165, L.VVVVVS186, L.VVVVVS209, L.VVVVVS57 ],
               couplings = {(0,2):C.GC_5125,(0,5):C.GC_5116,(0,1):C.GC_4922,(0,4):C.GC_4705,(0,0):C.GC_4916,(0,3):C.GC_4699})

V_773 = Vertex(name = 'V_773',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS131, L.VVVVVS158, L.VVVVVS161, L.VVVVVS162, L.VVVVVS184, L.VVVVVS189, L.VVVVVS190, L.VVVVVS191, L.VVVVVS215, L.VVVVVS217, L.VVVVVS37, L.VVVVVS38, L.VVVVVS40, L.VVVVVS42, L.VVVVVS46, L.VVVVVS59, L.VVVVVS92, L.VVVVVS98 ],
               couplings = {(0,16):C.GC_4662,(0,17):C.GC_5070,(0,10):C.GC_5216,(0,13):C.GC_5687,(0,11):C.GC_4837,(0,4):C.GC_5068,(0,9):C.GC_5074,(0,8):C.GC_5156,(0,2):C.GC_4528,(0,1):C.GC_4840,(0,3):C.GC_4847,(0,5):C.GC_4657,(0,7):C.GC_4659,(0,6):C.GC_4717,(0,12):C.GC_5066,(0,14):C.GC_5075,(0,15):C.GC_5072,(0,0):C.GC_4658})

V_774 = Vertex(name = 'V_774',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS131, L.VVVVVS158, L.VVVVVS162, L.VVVVVS184, L.VVVVVS189, L.VVVVVS59 ],
               couplings = {(0,3):C.GC_5125,(0,1):C.GC_4915,(0,2):C.GC_4925,(0,4):C.GC_4704,(0,5):C.GC_5117,(0,0):C.GC_4699})

V_775 = Vertex(name = 'V_775',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS103, L.VVVVVS104, L.VVVVVS105, L.VVVVVS106, L.VVVVVS121, L.VVVVVS127, L.VVVVVS145, L.VVVVVS149, L.VVVVVS167, L.VVVVVS172, L.VVVVVS177, L.VVVVVS60, L.VVVVVS63, L.VVVVVS89, L.VVVVVS90, L.VVVVVS91 ],
               couplings = {(0,2):C.GC_5711,(0,3):C.GC_4552,(0,0):C.GC_6650,(0,1):C.GC_5266,(0,15):C.GC_4873,(0,14):C.GC_5102,(0,11):C.GC_5211,(0,10):C.GC_6285,(0,7):C.GC_6041,(0,5):C.GC_5212,(0,8):C.GC_5213,(0,9):C.GC_5288,(0,12):C.GC_4681,(0,13):C.GC_5286,(0,4):C.GC_5520,(0,6):C.GC_5287})

V_776 = Vertex(name = 'V_776',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS121, L.VVVVVS127, L.VVVVVS145, L.VVVVVS149, L.VVVVVS167, L.VVVVVS172, L.VVVVVS177 ],
               couplings = {(0,6):C.GC_5775,(0,3):C.GC_6086,(0,1):C.GC_5232,(0,4):C.GC_5237,(0,5):C.GC_5296,(0,0):C.GC_5537,(0,2):C.GC_5293})

V_777 = Vertex(name = 'V_777',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS103, L.VVVVVS104, L.VVVVVS105, L.VVVVVS106, L.VVVVVS121, L.VVVVVS127, L.VVVVVS145, L.VVVVVS149, L.VVVVVS167, L.VVVVVS172, L.VVVVVS177, L.VVVVVS60, L.VVVVVS63, L.VVVVVS89, L.VVVVVS90, L.VVVVVS91 ],
               couplings = {(0,2):C.GC_5711,(0,3):C.GC_4553,(0,0):C.GC_6649,(0,1):C.GC_5267,(0,15):C.GC_4872,(0,14):C.GC_5102,(0,11):C.GC_5211,(0,10):C.GC_6284,(0,7):C.GC_6041,(0,5):C.GC_5212,(0,8):C.GC_5213,(0,9):C.GC_5288,(0,12):C.GC_4681,(0,13):C.GC_5286,(0,4):C.GC_5520,(0,6):C.GC_5287})

V_778 = Vertex(name = 'V_778',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS121, L.VVVVVS127, L.VVVVVS145, L.VVVVVS149, L.VVVVVS167, L.VVVVVS172, L.VVVVVS177 ],
               couplings = {(0,6):C.GC_5775,(0,3):C.GC_6086,(0,1):C.GC_5232,(0,4):C.GC_5237,(0,5):C.GC_5296,(0,0):C.GC_5537,(0,2):C.GC_5293})

V_779 = Vertex(name = 'V_779',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS103, L.VVVVVS114, L.VVVVVS145, L.VVVVVS148, L.VVVVVS172, L.VVVVVS174, L.VVVVVS176, L.VVVVVS177, L.VVVVVS178, L.VVVVVS179, L.VVVVVS180, L.VVVVVS68, L.VVVVVS72, L.VVVVVS73, L.VVVVVS84, L.VVVVVS85, L.VVVVVS89, L.VVVVVS96 ],
               couplings = {(0,0):C.GC_6525,(0,1):C.GC_6037,(0,14):C.GC_4525,(0,13):C.GC_4680,(0,15):C.GC_4863,(0,11):C.GC_5101,(0,7):C.GC_6039,(0,5):C.GC_6301,(0,8):C.GC_4718,(0,9):C.GC_4864,(0,6):C.GC_4865,(0,10):C.GC_5161,(0,4):C.GC_5257,(0,17):C.GC_6300,(0,12):C.GC_5226,(0,16):C.GC_5255,(0,3):C.GC_6304,(0,2):C.GC_5256})

V_780 = Vertex(name = 'V_780',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS145, L.VVVVVS148, L.VVVVVS172, L.VVVVVS174, L.VVVVVS176, L.VVVVVS177, L.VVVVVS179 ],
               couplings = {(0,5):C.GC_5471,(0,3):C.GC_6379,(0,6):C.GC_4918,(0,4):C.GC_4926,(0,2):C.GC_5274,(0,1):C.GC_6334,(0,0):C.GC_5272})

V_781 = Vertex(name = 'V_781',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS166, L.VVVVVS86 ],
               couplings = {(0,1):C.GC_6533,(0,0):C.GC_6536})

V_782 = Vertex(name = 'V_782',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS166 ],
               couplings = {(0,0):C.GC_6578})

V_783 = Vertex(name = 'V_783',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS166, L.VVVVVS86 ],
               couplings = {(0,1):C.GC_6534,(0,0):C.GC_6536})

V_784 = Vertex(name = 'V_784',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS166 ],
               couplings = {(0,0):C.GC_6578})

V_785 = Vertex(name = 'V_785',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV11, L.VVVVVV114, L.VVVVVV115, L.VVVVVV128, L.VVVVVV15, L.VVVVVV23, L.VVVVVV24, L.VVVVVV40, L.VVVVVV65, L.VVVVVV66, L.VVVVVV71, L.VVVVVV72, L.VVVVVV84, L.VVVVVV85, L.VVVVVV86, L.VVVVVV98, L.VVVVVV99 ],
               couplings = {(0,1):C.GC_193,(0,5):C.GC_202,(0,0):C.GC_1801,(0,10):C.GC_200,(0,11):C.GC_198,(0,6):C.GC_1798,(0,17):C.GC_201,(0,4):C.GC_203,(0,3):C.GC_669,(0,2):C.GC_677,(0,7):C.GC_1799,(0,9):C.GC_2181,(0,14):C.GC_5377,(0,15):C.GC_5379,(0,13):C.GC_5397,(0,8):C.GC_5378,(0,12):C.GC_1796,(0,16):C.GC_1797})

V_786 = Vertex(name = 'V_786',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV128, L.VVVVVV24, L.VVVVVV40, L.VVVVVV85, L.VVVVVV98, L.VVVVVV99 ],
               couplings = {(0,5):C.GC_654,(0,0):C.GC_664,(0,1):C.GC_997,(0,3):C.GC_5392,(0,2):C.GC_5388,(0,4):C.GC_2179})

V_787 = Vertex(name = 'V_787',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS187, L.VVVVVS8 ],
               couplings = {(0,1):C.GC_4624,(0,0):C.GC_5512})

V_788 = Vertex(name = 'V_788',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS187 ],
               couplings = {(0,0):C.GC_5538})

V_789 = Vertex(name = 'V_789',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS118, L.VVVVVS72 ],
               couplings = {(0,0):C.GC_5512,(0,1):C.GC_4623})

V_790 = Vertex(name = 'V_790',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS118 ],
               couplings = {(0,0):C.GC_5538})

V_791 = Vertex(name = 'V_791',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV10, L.VVVVVV104, L.VVVVVV113, L.VVVVVV47, L.VVVVVV59, L.VVVVVV77, L.VVVVVV91 ],
               couplings = {(0,0):C.GC_1708,(0,3):C.GC_1710,(0,2):C.GC_2172,(0,5):C.GC_1712,(0,4):C.GC_1709,(0,1):C.GC_1711,(0,6):C.GC_6698})

V_792 = Vertex(name = 'V_792',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV104, L.VVVVVV77, L.VVVVVV91 ],
               couplings = {(0,1):C.GC_991,(0,0):C.GC_2165,(0,2):C.GC_6708})

V_793 = Vertex(name = 'V_793',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS202, L.VVVVVS23, L.VVVVVS28 ],
               couplings = {(0,1):C.GC_6307,(0,2):C.GC_6305,(0,0):C.GC_6302})

V_794 = Vertex(name = 'V_794',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS202, L.VVVVVS28 ],
               couplings = {(0,1):C.GC_6335,(0,0):C.GC_6380})

V_795 = Vertex(name = 'V_795',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV103, L.VVVVVV107, L.VVVVVV112, L.VVVVVV118, L.VVVVVV123, L.VVVVVV21, L.VVVVVV26, L.VVVVVV30, L.VVVVVV32, L.VVVVVV44, L.VVVVVV5, L.VVVVVV54, L.VVVVVV55, L.VVVVVV6, L.VVVVVV60, L.VVVVVV69, L.VVVVVV90, L.VVVVVV93, L.VVVVVV94 ],
               couplings = {(0,13):C.GC_2363,(0,5):C.GC_2372,(0,10):C.GC_2369,(0,11):C.GC_2368,(0,15):C.GC_2370,(0,9):C.GC_2366,(0,4):C.GC_2373,(0,3):C.GC_2766,(0,2):C.GC_2771,(0,1):C.GC_2779,(0,6):C.GC_6883,(0,0):C.GC_2371,(0,12):C.GC_2367,(0,7):C.GC_2364,(0,8):C.GC_2365,(0,14):C.GC_5336,(0,18):C.GC_5337,(0,17):C.GC_6882,(0,16):C.GC_5347})

V_796 = Vertex(name = 'V_796',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV103, L.VVVVVV123, L.VVVVVV32, L.VVVVVV55, L.VVVVVV60, L.VVVVVV93, L.VVVVVV94 ],
               couplings = {(0,1):C.GC_2764,(0,0):C.GC_2759,(0,3):C.GC_1397,(0,2):C.GC_2774,(0,4):C.GC_5342,(0,6):C.GC_5340,(0,5):C.GC_5419})

V_797 = Vertex(name = 'V_797',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS12, L.VVVVVS199, L.VVVVVS201, L.VVVVVS202, L.VVVVVS28 ],
               couplings = {(0,0):C.GC_4645,(0,4):C.GC_6025,(0,2):C.GC_4643,(0,1):C.GC_4715,(0,3):C.GC_6024})

V_798 = Vertex(name = 'V_798',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS202, L.VVVVVS28 ],
               couplings = {(0,1):C.GC_6056,(0,0):C.GC_6107})

V_799 = Vertex(name = 'V_799',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS111, L.VVVVVS208, L.VVVVVS47 ],
               couplings = {(0,0):C.GC_5709,(0,1):C.GC_5705,(0,2):C.GC_5707})

V_800 = Vertex(name = 'V_800',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS208, L.VVVVVS47 ],
               couplings = {(0,0):C.GC_5774,(0,1):C.GC_5743})

V_801 = Vertex(name = 'V_801',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV108, L.VVVVVV109, L.VVVVVV124, L.VVVVVV126, L.VVVVVV13, L.VVVVVV14, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV39, L.VVVVVV41, L.VVVVVV51, L.VVVVVV52, L.VVVVVV63, L.VVVVVV64, L.VVVVVV65, L.VVVVVV7, L.VVVVVV72, L.VVVVVV73, L.VVVVVV81, L.VVVVVV83, L.VVVVVV98 ],
               couplings = {(0,6):C.GC_302,(0,0):C.GC_1838,(0,21):C.GC_308,(0,5):C.GC_3073,(0,16):C.GC_305,(0,17):C.GC_309,(0,8):C.GC_1836,(0,7):C.GC_7045,(0,11):C.GC_3071,(0,18):C.GC_311,(0,9):C.GC_1837,(0,2):C.GC_670,(0,1):C.GC_690,(0,23):C.GC_307,(0,10):C.GC_3069,(0,4):C.GC_310,(0,3):C.GC_3070,(0,19):C.GC_306,(0,24):C.GC_3179,(0,14):C.GC_3072,(0,20):C.GC_2182,(0,12):C.GC_303,(0,13):C.GC_304,(0,15):C.GC_7043,(0,22):C.GC_1834,(0,26):C.GC_1835,(0,25):C.GC_7044})

V_802 = Vertex(name = 'V_802',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV124, L.VVVVVV126, L.VVVVVV24, L.VVVVVV37, L.VVVVVV39, L.VVVVVV41, L.VVVVVV63, L.VVVVVV64, L.VVVVVV83, L.VVVVVV98 ],
               couplings = {(0,6):C.GC_678,(0,2):C.GC_998,(0,1):C.GC_655,(0,0):C.GC_3176,(0,7):C.GC_687,(0,4):C.GC_4288,(0,3):C.GC_684,(0,5):C.GC_7055,(0,9):C.GC_2180,(0,8):C.GC_7051})

V_803 = Vertex(name = 'V_803',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV101, L.VVVVVV120, L.VVVVVV124, L.VVVVVV125, L.VVVVVV129, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV25, L.VVVVVV35, L.VVVVVV39, L.VVVVVV41, L.VVVVVV62, L.VVVVVV68, L.VVVVVV81, L.VVVVVV83, L.VVVVVV86, L.VVVVVV87, L.VVVVVV88, L.VVVVVV89, L.VVVVVV95 ],
               couplings = {(0,7):C.GC_1795,(0,6):C.GC_1804,(0,5):C.GC_199,(0,13):C.GC_1802,(0,12):C.GC_1800,(0,9):C.GC_196,(0,3):C.GC_1803,(0,4):C.GC_1805,(0,0):C.GC_2173,(0,1):C.GC_2178,(0,8):C.GC_194,(0,2):C.GC_195,(0,14):C.GC_689,(0,10):C.GC_197,(0,11):C.GC_6786,(0,18):C.GC_5307,(0,16):C.GC_6788,(0,17):C.GC_5312,(0,19):C.GC_5398,(0,20):C.GC_5308,(0,15):C.GC_6787})

V_804 = Vertex(name = 'V_804',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV124, L.VVVVVV125, L.VVVVVV129, L.VVVVVV39, L.VVVVVV41, L.VVVVVV83, L.VVVVVV88, L.VVVVVV95 ],
               couplings = {(0,1):C.GC_2166,(0,2):C.GC_2171,(0,0):C.GC_683,(0,3):C.GC_686,(0,4):C.GC_6801,(0,6):C.GC_5311,(0,7):C.GC_5310,(0,5):C.GC_6800})

V_805 = Vertex(name = 'V_805',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV106, L.VVVVVV116, L.VVVVVV117, L.VVVVVV121, L.VVVVVV122, L.VVVVVV19, L.VVVVVV20, L.VVVVVV28, L.VVVVVV4, L.VVVVVV42, L.VVVVVV45, L.VVVVVV49, L.VVVVVV50, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV61, L.VVVVVV78, L.VVVVVV79, L.VVVVVV92 ],
               couplings = {(0,6):C.GC_2420,(0,8):C.GC_2429,(0,5):C.GC_2922,(0,10):C.GC_2426,(0,11):C.GC_2431,(0,12):C.GC_2919,(0,1):C.GC_2767,(0,0):C.GC_2781,(0,2):C.GC_3043,(0,14):C.GC_2428,(0,7):C.GC_2915,(0,4):C.GC_2432,(0,3):C.GC_2917,(0,13):C.GC_2427,(0,17):C.GC_2433,(0,18):C.GC_2920,(0,15):C.GC_2421,(0,16):C.GC_2423,(0,9):C.GC_6984,(0,19):C.GC_6983})

V_806 = Vertex(name = 'V_806',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV121, L.VVVVVV122, L.VVVVVV56, L.VVVVVV61, L.VVVVVV78, L.VVVVVV79, L.VVVVVV92 ],
               couplings = {(0,1):C.GC_2760,(0,0):C.GC_3039,(0,2):C.GC_1398,(0,4):C.GC_1394,(0,5):C.GC_3812,(0,3):C.GC_2775,(0,6):C.GC_6998})

V_807 = Vertex(name = 'V_807',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS115, L.VVVVVS118 ],
               couplings = {(0,1):C.GC_6038,(0,0):C.GC_6040})

V_808 = Vertex(name = 'V_808',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS118 ],
               couplings = {(0,0):C.GC_6108})

V_809 = Vertex(name = 'V_809',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV119, L.VVVVVV12, L.VVVVVV127, L.VVVVVV43, L.VVVVVV53, L.VVVVVV80, L.VVVVVV82 ],
               couplings = {(0,1):C.GC_823,(0,3):C.GC_825,(0,5):C.GC_827,(0,0):C.GC_990,(0,4):C.GC_824,(0,2):C.GC_826,(0,6):C.GC_6799})

V_810 = Vertex(name = 'V_810',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV127, L.VVVVVV80, L.VVVVVV82 ],
               couplings = {(0,1):C.GC_992,(0,0):C.GC_989,(0,2):C.GC_6809})

V_811 = Vertex(name = 'V_811',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS207, L.VVVVSS208, L.VVVVSS394 ],
               couplings = {(0,0):C.GC_1682,(0,1):C.GC_1688,(0,2):C.GC_1686})

V_812 = Vertex(name = 'V_812',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS394 ],
               couplings = {(0,0):C.GC_2060})

V_813 = Vertex(name = 'V_813',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS191, L.VVVVVS46 ],
               couplings = {(0,0):C.GC_4822,(0,1):C.GC_4824})

V_814 = Vertex(name = 'V_814',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS191 ],
               couplings = {(0,0):C.GC_4936})

V_815 = Vertex(name = 'V_815',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV102, L.VVVVVV105, L.VVVVVV3, L.VVVVVV34, L.VVVVVV38, L.VVVVVV74 ],
               couplings = {(0,2):C.GC_4067,(0,3):C.GC_4069,(0,4):C.GC_4071,(0,0):C.GC_4277,(0,5):C.GC_4068,(0,1):C.GC_4070})

V_816 = Vertex(name = 'V_816',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV105, L.VVVVVV38 ],
               couplings = {(0,1):C.GC_4281,(0,0):C.GC_4270})

V_817 = Vertex(name = 'V_817',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV100, L.VVVVVV110, L.VVVVVV111, L.VVVVVV2, L.VVVVVV27, L.VVVVVV29, L.VVVVVV31, L.VVVVVV33, L.VVVVVV46, L.VVVVVV48, L.VVVVVV67, L.VVVVVV70, L.VVVVVV75, L.VVVVVV76, L.VVVVVV8, L.VVVVVV9, L.VVVVVV96, L.VVVVVV97 ],
               couplings = {(0,3):C.GC_2430,(0,15):C.GC_2913,(0,14):C.GC_2923,(0,4):C.GC_2425,(0,8):C.GC_2924,(0,9):C.GC_2918,(0,5):C.GC_2427,(0,12):C.GC_2926,(0,0):C.GC_2780,(0,1):C.GC_3034,(0,2):C.GC_3042,(0,13):C.GC_2920,(0,6):C.GC_2914,(0,10):C.GC_2921,(0,7):C.GC_2916,(0,16):C.GC_2925,(0,11):C.GC_2422,(0,17):C.GC_2424})

V_818 = Vertex(name = 'V_818',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV29, L.VVVVVV33, L.VVVVVV75, L.VVVVVV76, L.VVVVVV96, L.VVVVVV97 ],
               couplings = {(0,0):C.GC_1398,(0,2):C.GC_3802,(0,3):C.GC_3812,(0,1):C.GC_3038,(0,4):C.GC_3031,(0,5):C.GC_2776})

V_819 = Vertex(name = 'V_819',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS132 ],
               couplings = {(0,0):C.GC_439})

V_820 = Vertex(name = 'V_820',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS132 ],
               couplings = {(0,0):C.GC_642})

V_821 = Vertex(name = 'V_821',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS12 ],
               couplings = {(0,0):C.GC_6046})

V_822 = Vertex(name = 'V_822',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS12 ],
               couplings = {(0,0):C.GC_6134})

V_823 = Vertex(name = 'V_823',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS144, L.VVVSSSS156, L.VVVSSSS162 ],
               couplings = {(0,1):C.GC_2502,(0,0):C.GC_2492,(0,2):C.GC_2484})

V_824 = Vertex(name = 'V_824',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS144, L.VVVSSSS156, L.VVVSSSS162 ],
               couplings = {(0,1):C.GC_2727,(0,0):C.GC_2708,(0,2):C.GC_2754})

V_825 = Vertex(name = 'V_825',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS135, L.VVVSSSS159, L.VVVSSSS78 ],
               couplings = {(0,1):C.GC_2494,(0,0):C.GC_2476,(0,2):C.GC_2495})

V_826 = Vertex(name = 'V_826',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS135, L.VVVSSSS159, L.VVVSSSS78 ],
               couplings = {(0,1):C.GC_2710,(0,0):C.GC_2746,(0,2):C.GC_2720})

V_827 = Vertex(name = 'V_827',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_1858,(0,0):C.GC_1865,(0,1):C.GC_1854})

V_828 = Vertex(name = 'V_828',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_2102,(0,0):C.GC_2126,(0,1):C.GC_2159})

V_829 = Vertex(name = 'V_829',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS24, L.VVVSSSS55, L.VVVSSSS92 ],
               couplings = {(0,1):C.GC_1857,(0,0):C.GC_1863,(0,2):C.GC_1856})

V_830 = Vertex(name = 'V_830',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS24, L.VVVSSSS55, L.VVVSSSS92 ],
               couplings = {(0,1):C.GC_2101,(0,0):C.GC_2124,(0,2):C.GC_2161})

V_831 = Vertex(name = 'V_831',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_1853,(0,0):C.GC_1865,(0,1):C.GC_1859})

V_832 = Vertex(name = 'V_832',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_2158,(0,0):C.GC_2126,(0,1):C.GC_2103})

V_833 = Vertex(name = 'V_833',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5722,(0,1):C.GC_4880})

V_834 = Vertex(name = 'V_834',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5841,(0,1):C.GC_4959})

V_835 = Vertex(name = 'V_835',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5719,(0,1):C.GC_4879})

V_836 = Vertex(name = 'V_836',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5839,(0,1):C.GC_4958})

V_837 = Vertex(name = 'V_837',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS12 ],
               couplings = {(0,0):C.GC_6049})

V_838 = Vertex(name = 'V_838',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS12 ],
               couplings = {(0,0):C.GC_6137})

V_839 = Vertex(name = 'V_839',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS135, L.VVVSSSS161, L.VVVSSSS74 ],
               couplings = {(0,1):C.GC_2501,(0,0):C.GC_2485,(0,2):C.GC_2491})

V_840 = Vertex(name = 'V_840',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS135, L.VVVSSSS161, L.VVVSSSS74 ],
               couplings = {(0,1):C.GC_2726,(0,0):C.GC_2755,(0,2):C.GC_2707})

V_841 = Vertex(name = 'V_841',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS129, L.VVVSSSS158, L.VVVSSSS71 ],
               couplings = {(0,0):C.GC_2476,(0,2):C.GC_2495,(0,1):C.GC_2494})

V_842 = Vertex(name = 'V_842',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS129, L.VVVSSSS158, L.VVVSSSS71 ],
               couplings = {(0,0):C.GC_2746,(0,2):C.GC_2720,(0,1):C.GC_2710})

V_843 = Vertex(name = 'V_843',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5718,(0,1):C.GC_4878})

V_844 = Vertex(name = 'V_844',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5838,(0,1):C.GC_4957})

V_845 = Vertex(name = 'V_845',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS103, L.VVVSSSS12, L.VVVSSSS178 ],
               couplings = {(0,0):C.GC_1852,(0,2):C.GC_1864,(0,1):C.GC_1861})

V_846 = Vertex(name = 'V_846',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS103, L.VVVSSSS12, L.VVVSSSS178 ],
               couplings = {(0,0):C.GC_2157,(0,2):C.GC_2125,(0,1):C.GC_2105})

V_847 = Vertex(name = 'V_847',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS45, L.VVVSSSS46, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_1853,(0,1):C.GC_1865,(0,2):C.GC_1861})

V_848 = Vertex(name = 'V_848',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS45, L.VVVSSSS46, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_2158,(0,1):C.GC_2126,(0,2):C.GC_2105})

V_849 = Vertex(name = 'V_849',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS109, L.VVVSSSS18 ],
               couplings = {(0,1):C.GC_830,(0,0):C.GC_1862})

V_850 = Vertex(name = 'V_850',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS109, L.VVVSSSS18 ],
               couplings = {(0,1):C.GC_959,(0,0):C.GC_2106})

V_851 = Vertex(name = 'V_851',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS130, L.VVVSSSS19 ],
               couplings = {(0,2):C.GC_1860,(0,0):C.GC_1855,(0,1):C.GC_1867})

V_852 = Vertex(name = 'V_852',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS130, L.VVVSSSS19 ],
               couplings = {(0,2):C.GC_2104,(0,0):C.GC_2160,(0,1):C.GC_2128})

V_853 = Vertex(name = 'V_853',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4685,(0,1):C.GC_5525})

V_854 = Vertex(name = 'V_854',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4735,(0,1):C.GC_5550})

V_855 = Vertex(name = 'V_855',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4686,(0,1):C.GC_5526})

V_856 = Vertex(name = 'V_856',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4736,(0,1):C.GC_5551})

V_857 = Vertex(name = 'V_857',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4684,(0,1):C.GC_5523})

V_858 = Vertex(name = 'V_858',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4734,(0,1):C.GC_5549})

V_859 = Vertex(name = 'V_859',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS146, L.VVVSSSS155, L.VVVSSSS31 ],
               couplings = {(0,1):C.GC_1439,(0,2):C.GC_1429,(0,0):C.GC_1448})

V_860 = Vertex(name = 'V_860',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS146, L.VVVSSSS155, L.VVVSSSS31 ],
               couplings = {(0,1):C.GC_1613,(0,2):C.GC_1654,(0,0):C.GC_1640})

V_861 = Vertex(name = 'V_861',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS105, L.VVVSSSS77, L.VVVSSSS88 ],
               couplings = {(0,0):C.GC_1430,(0,1):C.GC_1440,(0,2):C.GC_1446})

V_862 = Vertex(name = 'V_862',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS105, L.VVVSSSS77, L.VVVSSSS88 ],
               couplings = {(0,0):C.GC_1655,(0,1):C.GC_1614,(0,2):C.GC_1638})

V_863 = Vertex(name = 'V_863',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS138, L.VVVSSSS143, L.VVVSSSS73 ],
               couplings = {(0,1):C.GC_1434,(0,2):C.GC_1432,(0,0):C.GC_1444})

V_864 = Vertex(name = 'V_864',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS138, L.VVVSSSS143, L.VVVSSSS73 ],
               couplings = {(0,1):C.GC_1608,(0,2):C.GC_1657,(0,0):C.GC_1636})

V_865 = Vertex(name = 'V_865',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS32, L.VVVSSSS42, L.VVVSSSS47 ],
               couplings = {(0,2):C.GC_1430,(0,0):C.GC_1438,(0,1):C.GC_1446})

V_866 = Vertex(name = 'V_866',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS32, L.VVVSSSS42, L.VVVSSSS47 ],
               couplings = {(0,2):C.GC_1655,(0,0):C.GC_1612,(0,1):C.GC_1638})

V_867 = Vertex(name = 'V_867',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS153, L.VVVSSSS157, L.VVVSSSS30 ],
               couplings = {(0,1):C.GC_1433,(0,2):C.GC_1432,(0,0):C.GC_1443})

V_868 = Vertex(name = 'V_868',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS153, L.VVVSSSS157, L.VVVSSSS30 ],
               couplings = {(0,1):C.GC_1607,(0,2):C.GC_1657,(0,0):C.GC_1635})

V_869 = Vertex(name = 'V_869',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS102, L.VVVSSSS107, L.VVVSSSS76 ],
               couplings = {(0,1):C.GC_1426,(0,2):C.GC_1442,(0,0):C.GC_1444})

V_870 = Vertex(name = 'V_870',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS102, L.VVVSSSS107, L.VVVSSSS76 ],
               couplings = {(0,1):C.GC_1651,(0,2):C.GC_1616,(0,0):C.GC_1636})

V_871 = Vertex(name = 'V_871',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4682,(0,1):C.GC_5524})

V_872 = Vertex(name = 'V_872',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS11 ],
               couplings = {(0,0):C.GC_4760,(0,1):C.GC_5542})

V_873 = Vertex(name = 'V_873',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_1859,(0,0):C.GC_1866,(0,1):C.GC_1853})

V_874 = Vertex(name = 'V_874',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_2103,(0,0):C.GC_2127,(0,1):C.GC_2158})

V_875 = Vertex(name = 'V_875',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS24, L.VVVSSSS55, L.VVVSSSS92 ],
               couplings = {(0,1):C.GC_1857,(0,0):C.GC_1863,(0,2):C.GC_1856})

V_876 = Vertex(name = 'V_876',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS24, L.VVVSSSS55, L.VVVSSSS92 ],
               couplings = {(0,1):C.GC_2101,(0,0):C.GC_2124,(0,2):C.GC_2161})

V_877 = Vertex(name = 'V_877',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_1854,(0,0):C.GC_1866,(0,1):C.GC_1858})

V_878 = Vertex(name = 'V_878',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS38, L.VVVSSSS98 ],
               couplings = {(0,2):C.GC_2159,(0,0):C.GC_2127,(0,1):C.GC_2102})

V_879 = Vertex(name = 'V_879',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5528,(0,1):C.GC_4683})

V_880 = Vertex(name = 'V_880',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5543,(0,1):C.GC_4761})

V_881 = Vertex(name = 'V_881',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS16, L.VVVSSSS72, L.VVVSSSS82 ],
               couplings = {(0,2):C.GC_1436,(0,0):C.GC_1445,(0,1):C.GC_1431})

V_882 = Vertex(name = 'V_882',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS16, L.VVVSSSS72, L.VVVSSSS82 ],
               couplings = {(0,2):C.GC_1610,(0,0):C.GC_1637,(0,1):C.GC_1656})

V_883 = Vertex(name = 'V_883',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS11, L.VVVSSSS28, L.VVVSSSS35 ],
               couplings = {(0,2):C.GC_1436,(0,0):C.GC_1445,(0,1):C.GC_1428})

V_884 = Vertex(name = 'V_884',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS11, L.VVVSSSS28, L.VVVSSSS35 ],
               couplings = {(0,2):C.GC_1610,(0,0):C.GC_1637,(0,1):C.GC_1653})

V_885 = Vertex(name = 'V_885',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS13, L.VVVSSSS27, L.VVVSSSS61 ],
               couplings = {(0,2):C.GC_1429,(0,0):C.GC_1447,(0,1):C.GC_1437})

V_886 = Vertex(name = 'V_886',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS13, L.VVVSSSS27, L.VVVSSSS61 ],
               couplings = {(0,2):C.GC_1654,(0,0):C.GC_1639,(0,1):C.GC_1611})

V_887 = Vertex(name = 'V_887',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS17, L.VVVSSSS39, L.VVVSSSS83 ],
               couplings = {(0,2):C.GC_1435,(0,0):C.GC_1444,(0,1):C.GC_1432})

V_888 = Vertex(name = 'V_888',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS17, L.VVVSSSS39, L.VVVSSSS83 ],
               couplings = {(0,2):C.GC_1609,(0,0):C.GC_1636,(0,1):C.GC_1657})

V_889 = Vertex(name = 'V_889',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS54, L.VVVSSSS90 ],
               couplings = {(0,2):C.GC_1427,(0,0):C.GC_1444,(0,1):C.GC_1441})

V_890 = Vertex(name = 'V_890',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS54, L.VVVSSSS90 ],
               couplings = {(0,2):C.GC_1652,(0,0):C.GC_1636,(0,1):C.GC_1615})

V_891 = Vertex(name = 'V_891',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS142, L.VVVSSSS23, L.VVVSSSS26 ],
               couplings = {(0,0):C.GC_1425,(0,1):C.GC_1443,(0,2):C.GC_1441})

V_892 = Vertex(name = 'V_892',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS142, L.VVVSSSS23, L.VVVSSSS26 ],
               couplings = {(0,0):C.GC_1650,(0,1):C.GC_1635,(0,2):C.GC_1615})

V_893 = Vertex(name = 'V_893',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5482,(0,1):C.GC_4610})

V_894 = Vertex(name = 'V_894',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5497,(0,1):C.GC_4622})

V_895 = Vertex(name = 'V_895',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5717,(0,1):C.GC_4877})

V_896 = Vertex(name = 'V_896',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5836,(0,1):C.GC_4956})

V_897 = Vertex(name = 'V_897',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5719,(0,1):C.GC_4879})

V_898 = Vertex(name = 'V_898',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5839,(0,1):C.GC_4958})

V_899 = Vertex(name = 'V_899',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5527,(0,1):C.GC_4687})

V_900 = Vertex(name = 'V_900',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5552,(0,1):C.GC_4737})

V_901 = Vertex(name = 'V_901',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5526,(0,1):C.GC_4686})

V_902 = Vertex(name = 'V_902',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5551,(0,1):C.GC_4736})

V_903 = Vertex(name = 'V_903',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5529,(0,1):C.GC_4688})

V_904 = Vertex(name = 'V_904',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5553,(0,1):C.GC_4738})

V_905 = Vertex(name = 'V_905',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5481,(0,1):C.GC_4611})

V_906 = Vertex(name = 'V_906',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5498,(0,1):C.GC_4619})

V_907 = Vertex(name = 'V_907',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5483,(0,1):C.GC_4612})

V_908 = Vertex(name = 'V_908',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_5499,(0,1):C.GC_4620})

V_909 = Vertex(name = 'V_909',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS110, L.VVVSSSS4 ],
               couplings = {(0,1):C.GC_3600,(0,0):C.GC_3599})

V_910 = Vertex(name = 'V_910',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS110, L.VVVSSSS4 ],
               couplings = {(0,1):C.GC_3755,(0,0):C.GC_3790})

V_911 = Vertex(name = 'V_911',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS132 ],
               couplings = {(0,0):C.GC_3601})

V_912 = Vertex(name = 'V_912',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS132 ],
               couplings = {(0,0):C.GC_3791})

V_913 = Vertex(name = 'V_913',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5470,(0,1):C.GC_5739,(0,2):C.GC_4892})

V_914 = Vertex(name = 'V_914',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5479,(0,1):C.GC_5850,(0,2):C.GC_4976})

V_915 = Vertex(name = 'V_915',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS65 ],
               couplings = {(0,0):C.GC_845})

V_916 = Vertex(name = 'V_916',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS65 ],
               couplings = {(0,0):C.GC_963})

V_917 = Vertex(name = 'V_917',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS119, L.VVVSSSS120, L.VVVSSSS133, L.VVVSSSS150, L.VVVSSSS151, L.VVVSSSS20 ],
               couplings = {(0,4):C.GC_357,(0,0):C.GC_361,(0,3):C.GC_1915,(0,1):C.GC_1919,(0,2):C.GC_366,(0,5):C.GC_1922})

V_918 = Vertex(name = 'V_918',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS119, L.VVVSSSS120, L.VVVSSSS133, L.VVVSSSS150, L.VVVSSSS151, L.VVVSSSS20 ],
               couplings = {(0,4):C.GC_628,(0,0):C.GC_590,(0,3):C.GC_2163,(0,1):C.GC_2109,(0,2):C.GC_608,(0,5):C.GC_2131})

V_919 = Vertex(name = 'V_919',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS117, L.VVVSSSS33, L.VVVSSSS7 ],
               couplings = {(0,2):C.GC_848,(0,1):C.GC_839,(0,0):C.GC_844})

V_920 = Vertex(name = 'V_920',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS117, L.VVVSSSS33, L.VVVSSSS7 ],
               couplings = {(0,2):C.GC_948,(0,1):C.GC_960,(0,0):C.GC_946})

V_921 = Vertex(name = 'V_921',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS140, L.VVVSSSS166, L.VVVSSSS169, L.VVVSSSS170, L.VVVSSSS25, L.VVVSSSS70 ],
               couplings = {(0,3):C.GC_356,(0,1):C.GC_360,(0,5):C.GC_364,(0,2):C.GC_1916,(0,0):C.GC_1917,(0,4):C.GC_1923})

V_922 = Vertex(name = 'V_922',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS140, L.VVVSSSS166, L.VVVSSSS169, L.VVVSSSS170, L.VVVSSSS25, L.VVVSSSS70 ],
               couplings = {(0,3):C.GC_627,(0,1):C.GC_589,(0,5):C.GC_606,(0,2):C.GC_2164,(0,0):C.GC_2107,(0,4):C.GC_2132})

V_923 = Vertex(name = 'V_923',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS108, L.VVVSSSS165, L.VVVSSSS3 ],
               couplings = {(0,2):C.GC_850,(0,0):C.GC_841,(0,1):C.GC_842})

V_924 = Vertex(name = 'V_924',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS108, L.VVVSSSS165, L.VVVSSSS3 ],
               couplings = {(0,2):C.GC_950,(0,0):C.GC_964,(0,1):C.GC_945})

V_925 = Vertex(name = 'V_925',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS124 ],
               couplings = {(0,0):C.GC_843})

V_926 = Vertex(name = 'V_926',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS124 ],
               couplings = {(0,0):C.GC_965})

V_927 = Vertex(name = 'V_927',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5532,(0,2):C.GC_6052,(0,0):C.GC_5109})

V_928 = Vertex(name = 'V_928',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5554,(0,2):C.GC_6138,(0,0):C.GC_5185})

V_929 = Vertex(name = 'V_929',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5531,(0,2):C.GC_6053,(0,0):C.GC_5110})

V_930 = Vertex(name = 'V_930',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5556,(0,2):C.GC_6140,(0,0):C.GC_5186})

V_931 = Vertex(name = 'V_931',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_749,(0,2):C.GC_1243,(0,0):C.GC_2514})

V_932 = Vertex(name = 'V_932',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_793,(0,2):C.GC_1380,(0,0):C.GC_2731})

V_933 = Vertex(name = 'V_933',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS148, L.VVVSSSS160, L.VVVSSSS167 ],
               couplings = {(0,0):C.GC_750,(0,1):C.GC_1244,(0,2):C.GC_2515})

V_934 = Vertex(name = 'V_934',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS148, L.VVVSSSS160, L.VVVSSSS167 ],
               couplings = {(0,0):C.GC_791,(0,1):C.GC_1381,(0,2):C.GC_2732})

V_935 = Vertex(name = 'V_935',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_748,(0,2):C.GC_1243,(0,0):C.GC_2514})

V_936 = Vertex(name = 'V_936',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_794,(0,2):C.GC_1380,(0,0):C.GC_2731})

V_937 = Vertex(name = 'V_937',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5469,(0,1):C.GC_5740,(0,2):C.GC_4893})

V_938 = Vertex(name = 'V_938',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS14, L.VVVVSSS2 ],
               couplings = {(0,0):C.GC_5478,(0,1):C.GC_5851,(0,2):C.GC_4977})

V_939 = Vertex(name = 'V_939',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS65 ],
               couplings = {(0,0):C.GC_847})

V_940 = Vertex(name = 'V_940',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS65 ],
               couplings = {(0,0):C.GC_961})

V_941 = Vertex(name = 'V_941',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS14, L.VVVSSSS171, L.VVVSSSS172, L.VVVSSSS67, L.VVVSSSS68, L.VVVSSSS86 ],
               couplings = {(0,2):C.GC_358,(0,3):C.GC_362,(0,1):C.GC_1914,(0,4):C.GC_1918,(0,5):C.GC_365,(0,0):C.GC_1921})

V_942 = Vertex(name = 'V_942',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS14, L.VVVSSSS171, L.VVVSSSS172, L.VVVSSSS67, L.VVVSSSS68, L.VVVSSSS86 ],
               couplings = {(0,2):C.GC_629,(0,3):C.GC_591,(0,1):C.GC_2162,(0,4):C.GC_2108,(0,5):C.GC_607,(0,0):C.GC_2130})

V_943 = Vertex(name = 'V_943',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS117, L.VVVSSSS33, L.VVVSSSS7 ],
               couplings = {(0,2):C.GC_849,(0,1):C.GC_840,(0,0):C.GC_846})

V_944 = Vertex(name = 'V_944',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS117, L.VVVSSSS33, L.VVVSSSS7 ],
               couplings = {(0,2):C.GC_949,(0,1):C.GC_962,(0,0):C.GC_947})

V_945 = Vertex(name = 'V_945',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS112, L.VVVSSSS113, L.VVVSSSS128, L.VVVSSSS15, L.VVVSSSS174, L.VVVSSSS52 ],
               couplings = {(0,2):C.GC_359,(0,1):C.GC_363,(0,5):C.GC_367,(0,0):C.GC_1917,(0,3):C.GC_1920,(0,4):C.GC_1916})

V_946 = Vertex(name = 'V_946',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS112, L.VVVSSSS113, L.VVVSSSS128, L.VVVSSSS15, L.VVVSSSS174, L.VVVSSSS52 ],
               couplings = {(0,2):C.GC_630,(0,1):C.GC_592,(0,5):C.GC_609,(0,0):C.GC_2107,(0,3):C.GC_2129,(0,4):C.GC_2164})

V_947 = Vertex(name = 'V_947',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS108, L.VVVSSSS165, L.VVVSSSS3 ],
               couplings = {(0,2):C.GC_850,(0,0):C.GC_841,(0,1):C.GC_842})

V_948 = Vertex(name = 'V_948',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS108, L.VVVSSSS165, L.VVVSSSS3 ],
               couplings = {(0,2):C.GC_950,(0,0):C.GC_964,(0,1):C.GC_945})

V_949 = Vertex(name = 'V_949',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS124 ],
               couplings = {(0,0):C.GC_843})

V_950 = Vertex(name = 'V_950',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS124 ],
               couplings = {(0,0):C.GC_965})

V_951 = Vertex(name = 'V_951',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS12, L.VVVVSSS5 ],
               couplings = {(0,0):C.GC_5533,(0,2):C.GC_4691,(0,1):C.GC_6055})

V_952 = Vertex(name = 'V_952',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS12, L.VVVVSSS5 ],
               couplings = {(0,0):C.GC_5555,(0,2):C.GC_4739,(0,1):C.GC_6139})

V_953 = Vertex(name = 'V_953',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1240})

V_954 = Vertex(name = 'V_954',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1377})

V_955 = Vertex(name = 'V_955',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS127, L.VVVSSSS139, L.VVVSSSS58, L.VVVSSSS6, L.VVVSSSS80, L.VVVSSSS96 ],
               couplings = {(0,0):C.GC_1460,(0,2):C.GC_1461,(0,3):C.GC_1463,(0,1):C.GC_2510,(0,4):C.GC_2511,(0,5):C.GC_2512})

V_956 = Vertex(name = 'V_956',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS127, L.VVVSSSS139, L.VVVSSSS58, L.VVVSSSS6, L.VVVSSSS80, L.VVVSSSS96 ],
               couplings = {(0,0):C.GC_1658,(0,2):C.GC_1617,(0,3):C.GC_1641,(0,1):C.GC_2757,(0,4):C.GC_2711,(0,5):C.GC_2729})

V_957 = Vertex(name = 'V_957',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS2, L.VVVSSSS88 ],
               couplings = {(0,0):C.GC_1246,(0,1):C.GC_1238})

V_958 = Vertex(name = 'V_958',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS2, L.VVVSSSS88 ],
               couplings = {(0,0):C.GC_1351,(0,1):C.GC_1375})

V_959 = Vertex(name = 'V_959',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1239})

V_960 = Vertex(name = 'V_960',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1376})

V_961 = Vertex(name = 'V_961',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS153, L.VVVSSSS8 ],
               couplings = {(0,1):C.GC_1245,(0,0):C.GC_1237})

V_962 = Vertex(name = 'V_962',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS153, L.VVVSSSS8 ],
               couplings = {(0,1):C.GC_1350,(0,0):C.GC_1373})

V_963 = Vertex(name = 'V_963',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS111, L.VVVSSSS164, L.VVVSSSS4 ],
               couplings = {(0,2):C.GC_751,(0,1):C.GC_1462,(0,0):C.GC_1247})

V_964 = Vertex(name = 'V_964',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS111, L.VVVSSSS164, L.VVVSSSS4 ],
               couplings = {(0,2):C.GC_792,(0,1):C.GC_1618,(0,0):C.GC_1374})

V_965 = Vertex(name = 'V_965',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS114, L.VVVSSSS40, L.VVVSSSS5 ],
               couplings = {(0,2):C.GC_1248,(0,0):C.GC_1242,(0,1):C.GC_1236})

V_966 = Vertex(name = 'V_966',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS114, L.VVVSSSS40, L.VVVSSSS5 ],
               couplings = {(0,2):C.GC_1352,(0,0):C.GC_1349,(0,1):C.GC_1378})

V_967 = Vertex(name = 'V_967',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS116, L.VVVSSSS122, L.VVVSSSS126, L.VVVSSSS173, L.VVVSSSS43 ],
               couplings = {(0,3):C.GC_1460,(0,1):C.GC_1461,(0,0):C.GC_1463,(0,5):C.GC_2510,(0,2):C.GC_2511,(0,4):C.GC_2512})

V_968 = Vertex(name = 'V_968',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS116, L.VVVSSSS122, L.VVVSSSS126, L.VVVSSSS173, L.VVVSSSS43 ],
               couplings = {(0,3):C.GC_1658,(0,1):C.GC_1617,(0,0):C.GC_1641,(0,5):C.GC_2757,(0,2):C.GC_2711,(0,4):C.GC_2729})

V_969 = Vertex(name = 'V_969',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1240})

V_970 = Vertex(name = 'V_970',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS125 ],
               couplings = {(0,0):C.GC_1377})

V_971 = Vertex(name = 'V_971',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5488,(0,0):C.GC_5730,(0,1):C.GC_4885})

V_972 = Vertex(name = 'V_972',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5503,(0,0):C.GC_5847,(0,1):C.GC_4973})

V_973 = Vertex(name = 'V_973',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5485,(0,0):C.GC_5731,(0,1):C.GC_4886})

V_974 = Vertex(name = 'V_974',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5506,(0,0):C.GC_5848,(0,1):C.GC_4974})

V_975 = Vertex(name = 'V_975',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5486,(0,0):C.GC_5728,(0,1):C.GC_4884})

V_976 = Vertex(name = 'V_976',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5504,(0,0):C.GC_5845,(0,1):C.GC_4972})

V_977 = Vertex(name = 'V_977',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5490,(0,0):C.GC_5732,(0,1):C.GC_4887})

V_978 = Vertex(name = 'V_978',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,2):C.GC_5501,(0,0):C.GC_5849,(0,1):C.GC_4975})

V_979 = Vertex(name = 'V_979',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5530,(0,2):C.GC_6054,(0,0):C.GC_5111})

V_980 = Vertex(name = 'V_980',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5557,(0,2):C.GC_6141,(0,0):C.GC_5187})

V_981 = Vertex(name = 'V_981',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5531,(0,2):C.GC_6053,(0,0):C.GC_5110})

V_982 = Vertex(name = 'V_982',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5556,(0,2):C.GC_6140,(0,0):C.GC_5186})

V_983 = Vertex(name = 'V_983',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_748,(0,2):C.GC_1241,(0,0):C.GC_2513})

V_984 = Vertex(name = 'V_984',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_794,(0,2):C.GC_1379,(0,0):C.GC_2730})

V_985 = Vertex(name = 'V_985',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS148, L.VVVSSSS160, L.VVVSSSS167 ],
               couplings = {(0,0):C.GC_750,(0,1):C.GC_1244,(0,2):C.GC_2515})

V_986 = Vertex(name = 'V_986',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS148, L.VVVSSSS160, L.VVVSSSS167 ],
               couplings = {(0,0):C.GC_791,(0,1):C.GC_1381,(0,2):C.GC_2732})

V_987 = Vertex(name = 'V_987',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_749,(0,2):C.GC_1241,(0,0):C.GC_2513})

V_988 = Vertex(name = 'V_988',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS131, L.VVVSSSS148, L.VVVSSSS149 ],
               couplings = {(0,1):C.GC_793,(0,2):C.GC_1379,(0,0):C.GC_2730})

V_989 = Vertex(name = 'V_989',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5489,(0,2):C.GC_5727,(0,0):C.GC_4883})

V_990 = Vertex(name = 'V_990',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5502,(0,2):C.GC_5844,(0,0):C.GC_4971})

V_991 = Vertex(name = 'V_991',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5484,(0,2):C.GC_5726,(0,0):C.GC_4882})

V_992 = Vertex(name = 'V_992',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5507,(0,2):C.GC_5843,(0,0):C.GC_4970})

V_993 = Vertex(name = 'V_993',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5487,(0,2):C.GC_5729,(0,0):C.GC_4884})

V_994 = Vertex(name = 'V_994',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5505,(0,2):C.GC_5846,(0,0):C.GC_4972})

V_995 = Vertex(name = 'V_995',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5491,(0,2):C.GC_5725,(0,0):C.GC_4881})

V_996 = Vertex(name = 'V_996',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS11, L.VVVVSSS7, L.VVVVSSS8 ],
               couplings = {(0,1):C.GC_5500,(0,2):C.GC_5842,(0,0):C.GC_4969})

V_997 = Vertex(name = 'V_997',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS18, L.VVVSSSS93 ],
               couplings = {(0,1):C.GC_4100,(0,0):C.GC_4103})

V_998 = Vertex(name = 'V_998',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS18, L.VVVSSSS93 ],
               couplings = {(0,1):C.GC_4255,(0,0):C.GC_4247})

V_999 = Vertex(name = 'V_999',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS132 ],
               couplings = {(0,0):C.GC_4102})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS132 ],
                couplings = {(0,0):C.GC_4254})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS13, L.VVVVSSS2, L.VVVVSSS3, L.VVVVSSS9 ],
                couplings = {(0,2):C.GC_5534,(0,0):C.GC_6048,(0,1):C.GC_6313,(0,4):C.GC_5227,(0,3):C.GC_4696})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS13, L.VVVVSSS2, L.VVVVSSS3, L.VVVVSSS9 ],
                couplings = {(0,2):C.GC_5558,(0,0):C.GC_6136,(0,1):C.GC_6409,(0,4):C.GC_5244,(0,3):C.GC_4747})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS16, L.VVVSSSS51, L.VVVSSSS60, L.VVVSSSS66, L.VVVSSSS72, L.VVVSSSS87 ],
                couplings = {(0,1):C.GC_1497,(0,2):C.GC_1509,(0,3):C.GC_2490,(0,0):C.GC_3576,(0,4):C.GC_2482,(0,5):C.GC_3584})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS16, L.VVVSSSS51, L.VVVSSSS60, L.VVVSSSS66, L.VVVSSSS72, L.VVVSSSS87 ],
                couplings = {(0,1):C.GC_1661,(0,2):C.GC_1626,(0,3):C.GC_2706,(0,0):C.GC_3784,(0,4):C.GC_2752,(0,5):C.GC_3754})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS104, L.VVVSSSS136, L.VVVSSSS137, L.VVVSSSS36, L.VVVSSSS37, L.VVVSSSS85, L.VVVSSSS91, L.VVVSSSS97 ],
                couplings = {(0,3):C.GC_1496,(0,4):C.GC_1510,(0,6):C.GC_2479,(0,0):C.GC_2497,(0,5):C.GC_3574,(0,2):C.GC_2942,(0,7):C.GC_2488,(0,1):C.GC_1511})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS104, L.VVVSSSS136, L.VVVSSSS137, L.VVVSSSS36, L.VVVSSSS37, L.VVVSSSS85, L.VVVSSSS91, L.VVVSSSS97 ],
                couplings = {(0,3):C.GC_1660,(0,4):C.GC_1627,(0,6):C.GC_2749,(0,0):C.GC_2722,(0,5):C.GC_3782,(0,2):C.GC_3022,(0,7):C.GC_2704,(0,1):C.GC_1642})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS118, L.VVVSSSS141, L.VVVSSSS182, L.VVVSSSS34, L.VVVSSSS41, L.VVVSSSS44, L.VVVSSSS48, L.VVVSSSS99 ],
                couplings = {(0,2):C.GC_1498,(0,7):C.GC_1505,(0,3):C.GC_2481,(0,0):C.GC_2490,(0,5):C.GC_2500,(0,1):C.GC_3580,(0,6):C.GC_2945,(0,4):C.GC_1513})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS118, L.VVVSSSS141, L.VVVSSSS182, L.VVVSSSS34, L.VVVSSSS41, L.VVVSSSS44, L.VVVSSSS48, L.VVVSSSS99 ],
                couplings = {(0,2):C.GC_1662,(0,7):C.GC_1622,(0,3):C.GC_2751,(0,0):C.GC_2706,(0,5):C.GC_2725,(0,1):C.GC_3788,(0,6):C.GC_3025,(0,4):C.GC_1644})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS115, L.VVVSSSS121, L.VVVSSSS123, L.VVVSSSS134, L.VVVSSSS145, L.VVVSSSS147, L.VVVSSSS175, L.VVVSSSS49 ],
                couplings = {(0,2):C.GC_1500,(0,6):C.GC_1507,(0,0):C.GC_2480,(0,7):C.GC_2489,(0,3):C.GC_3578,(0,1):C.GC_2499,(0,5):C.GC_2945,(0,4):C.GC_1515})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS115, L.VVVSSSS121, L.VVVSSSS123, L.VVVSSSS134, L.VVVSSSS145, L.VVVSSSS147, L.VVVSSSS175, L.VVVSSSS49 ],
                couplings = {(0,2):C.GC_1664,(0,6):C.GC_1624,(0,0):C.GC_2750,(0,7):C.GC_2705,(0,3):C.GC_3786,(0,1):C.GC_2724,(0,5):C.GC_3025,(0,4):C.GC_1646})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS101, L.VVVSSSS168, L.VVVSSSS179, L.VVVSSSS29, L.VVVSSSS62, L.VVVSSSS63, L.VVVSSSS64, L.VVVSSSS69 ],
                couplings = {(0,6):C.GC_1501,(0,5):C.GC_1503,(0,4):C.GC_2478,(0,2):C.GC_2496,(0,7):C.GC_3581,(0,1):C.GC_2946,(0,3):C.GC_2493,(0,0):C.GC_1511})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS101, L.VVVSSSS168, L.VVVSSSS179, L.VVVSSSS29, L.VVVSSSS62, L.VVVSSSS63, L.VVVSSSS64, L.VVVSSSS69 ],
                couplings = {(0,6):C.GC_1665,(0,5):C.GC_1620,(0,4):C.GC_2748,(0,2):C.GC_2721,(0,7):C.GC_3789,(0,1):C.GC_3026,(0,3):C.GC_2709,(0,0):C.GC_1642})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS106, L.VVVSSSS142, L.VVVSSSS152, L.VVVSSSS163, L.VVVSSSS176, L.VVVSSSS23 ],
                couplings = {(0,0):C.GC_1495,(0,4):C.GC_1502,(0,1):C.GC_2477,(0,3):C.GC_2487,(0,5):C.GC_3572,(0,2):C.GC_3582})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS106, L.VVVSSSS142, L.VVVSSSS152, L.VVVSSSS163, L.VVVSSSS176, L.VVVSSSS23 ],
                couplings = {(0,0):C.GC_1659,(0,4):C.GC_1619,(0,1):C.GC_2747,(0,3):C.GC_2703,(0,5):C.GC_3780,(0,2):C.GC_3752})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5467,(0,1):C.GC_4556,(0,2):C.GC_5492})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5477,(0,1):C.GC_4606,(0,2):C.GC_5511})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5466,(0,1):C.GC_4555,(0,2):C.GC_5493})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5475,(0,1):C.GC_4605,(0,2):C.GC_5509})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS13, L.VVVVSSS2, L.VVVVSSS3, L.VVVVSSS9 ],
                couplings = {(0,2):C.GC_5535,(0,0):C.GC_6047,(0,1):C.GC_6319,(0,4):C.GC_5228,(0,3):C.GC_4697})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS13, L.VVVVSSS2, L.VVVVSSS3, L.VVVVSSS9 ],
                couplings = {(0,2):C.GC_5559,(0,0):C.GC_6135,(0,1):C.GC_6415,(0,4):C.GC_5245,(0,3):C.GC_4748})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS16, L.VVVSSSS51, L.VVVSSSS60, L.VVVSSSS66, L.VVVSSSS72, L.VVVSSSS87 ],
                couplings = {(0,1):C.GC_1498,(0,2):C.GC_1508,(0,3):C.GC_2489,(0,0):C.GC_3575,(0,4):C.GC_2483,(0,5):C.GC_3583})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS16, L.VVVSSSS51, L.VVVSSSS60, L.VVVSSSS66, L.VVVSSSS72, L.VVVSSSS87 ],
                couplings = {(0,1):C.GC_1662,(0,2):C.GC_1625,(0,3):C.GC_2705,(0,0):C.GC_3783,(0,4):C.GC_2753,(0,5):C.GC_3753})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS104, L.VVVSSSS136, L.VVVSSSS137, L.VVVSSSS36, L.VVVSSSS37, L.VVVSSSS85, L.VVVSSSS91, L.VVVSSSS97 ],
                couplings = {(0,3):C.GC_1496,(0,4):C.GC_1510,(0,6):C.GC_2479,(0,0):C.GC_2497,(0,5):C.GC_3574,(0,2):C.GC_2942,(0,7):C.GC_2488,(0,1):C.GC_1511})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS104, L.VVVSSSS136, L.VVVSSSS137, L.VVVSSSS36, L.VVVSSSS37, L.VVVSSSS85, L.VVVSSSS91, L.VVVSSSS97 ],
                couplings = {(0,3):C.GC_1660,(0,4):C.GC_1627,(0,6):C.GC_2749,(0,0):C.GC_2722,(0,5):C.GC_3782,(0,2):C.GC_3022,(0,7):C.GC_2704,(0,1):C.GC_1642})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS118, L.VVVSSSS141, L.VVVSSSS182, L.VVVSSSS34, L.VVVSSSS41, L.VVVSSSS44, L.VVVSSSS48, L.VVVSSSS99 ],
                couplings = {(0,2):C.GC_1497,(0,7):C.GC_1504,(0,3):C.GC_2480,(0,0):C.GC_2489,(0,5):C.GC_2499,(0,1):C.GC_3579,(0,6):C.GC_2944,(0,4):C.GC_1512})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS118, L.VVVSSSS141, L.VVVSSSS182, L.VVVSSSS34, L.VVVSSSS41, L.VVVSSSS44, L.VVVSSSS48, L.VVVSSSS99 ],
                couplings = {(0,2):C.GC_1661,(0,7):C.GC_1621,(0,3):C.GC_2750,(0,0):C.GC_2705,(0,5):C.GC_2724,(0,1):C.GC_3787,(0,6):C.GC_3024,(0,4):C.GC_1643})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS100, L.VVVSSSS177, L.VVVSSSS180, L.VVVSSSS181, L.VVVSSSS62, L.VVVSSSS75, L.VVVSSSS79, L.VVVSSSS81 ],
                couplings = {(0,0):C.GC_1499,(0,3):C.GC_1506,(0,4):C.GC_2481,(0,1):C.GC_2490,(0,2):C.GC_3577,(0,7):C.GC_2498,(0,6):C.GC_2943,(0,5):C.GC_1514})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS100, L.VVVSSSS177, L.VVVSSSS180, L.VVVSSSS181, L.VVVSSSS62, L.VVVSSSS75, L.VVVSSSS79, L.VVVSSSS81 ],
                couplings = {(0,0):C.GC_1663,(0,3):C.GC_1623,(0,4):C.GC_2751,(0,1):C.GC_2706,(0,2):C.GC_3785,(0,7):C.GC_2723,(0,6):C.GC_3023,(0,5):C.GC_1645})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS50, L.VVVSSSS53, L.VVVSSSS56, L.VVVSSSS57, L.VVVSSSS59, L.VVVSSSS84, L.VVVSSSS94, L.VVVSSSS95 ],
                couplings = {(0,2):C.GC_1503,(0,0):C.GC_2486,(0,1):C.GC_2493,(0,5):C.GC_2503,(0,4):C.GC_3573,(0,7):C.GC_2942,(0,3):C.GC_1501,(0,6):C.GC_1511})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS50, L.VVVSSSS53, L.VVVSSSS56, L.VVVSSSS57, L.VVVSSSS59, L.VVVSSSS84, L.VVVSSSS94, L.VVVSSSS95 ],
                couplings = {(0,2):C.GC_1620,(0,0):C.GC_2756,(0,1):C.GC_2709,(0,5):C.GC_2728,(0,4):C.GC_3781,(0,7):C.GC_3022,(0,3):C.GC_1665,(0,6):C.GC_1642})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS106, L.VVVSSSS142, L.VVVSSSS152, L.VVVSSSS163, L.VVVSSSS176, L.VVVSSSS23 ],
                couplings = {(0,0):C.GC_1495,(0,4):C.GC_1502,(0,1):C.GC_2477,(0,3):C.GC_2487,(0,5):C.GC_3572,(0,2):C.GC_3582})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS106, L.VVVSSSS142, L.VVVSSSS152, L.VVVSSSS163, L.VVVSSSS176, L.VVVSSSS23 ],
                couplings = {(0,0):C.GC_1659,(0,4):C.GC_1619,(0,1):C.GC_2747,(0,3):C.GC_2703,(0,5):C.GC_3780,(0,2):C.GC_3752})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS3, L.VVVVSSS6 ],
                couplings = {(0,0):C.GC_5468,(0,2):C.GC_4615,(0,1):C.GC_5495})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12, L.VVVVSSS3, L.VVVVSSS6 ],
                couplings = {(0,0):C.GC_5476,(0,2):C.GC_4621,(0,1):C.GC_5510})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5465,(0,1):C.GC_4554,(0,2):C.GC_5494})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5474,(0,1):C.GC_4604,(0,2):C.GC_5508})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5466,(0,1):C.GC_4555,(0,2):C.GC_5493})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS14, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_5475,(0,1):C.GC_4605,(0,2):C.GC_5509})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6552,(0,1):C.GC_6553})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6613,(0,1):C.GC_6593})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS136, L.VVVSSSS22 ],
                couplings = {(0,1):C.GC_4099,(0,0):C.GC_4101})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS136, L.VVVSSSS22 ],
                couplings = {(0,1):C.GC_4253,(0,0):C.GC_4246})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS11, L.VVVSSSS41 ],
                couplings = {(0,0):C.GC_4099,(0,1):C.GC_4101})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS11, L.VVVSSSS41 ],
                couplings = {(0,0):C.GC_4253,(0,1):C.GC_4246})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6315,(0,1):C.GC_6321})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6411,(0,1):C.GC_6389})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6316,(0,1):C.GC_6322})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6412,(0,1):C.GC_6390})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6314,(0,1):C.GC_6320})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6410,(0,1):C.GC_6388})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6317,(0,1):C.GC_6323})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6413,(0,1):C.GC_6391})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6316,(0,1):C.GC_6322})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6412,(0,1):C.GC_6390})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6318,(0,1):C.GC_6324})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_6414,(0,1):C.GC_6392})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_5715,(0,1):C.GC_5720})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_5837,(0,1):C.GC_5799})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_5716,(0,1):C.GC_5721})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS2, L.VVVVSSS3 ],
                couplings = {(0,0):C.GC_5840,(0,1):C.GC_5800})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6651})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6668})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS89 ],
                couplings = {(0,0):C.GC_4356})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS89 ],
                couplings = {(0,0):C.GC_4387})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS111 ],
                couplings = {(0,0):C.GC_4357})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS111 ],
                couplings = {(0,0):C.GC_4388})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS154 ],
                couplings = {(0,0):C.GC_4355})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS154 ],
                couplings = {(0,0):C.GC_4386})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS139 ],
                couplings = {(0,0):C.GC_4358})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS139 ],
                couplings = {(0,0):C.GC_4389})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS132 ],
                couplings = {(0,0):C.GC_4359})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS132 ],
                couplings = {(0,0):C.GC_4390})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS43 ],
                couplings = {(0,0):C.GC_4358})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS43 ],
                couplings = {(0,0):C.GC_4389})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6546})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6610})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6547})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6611})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6545})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6609})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6548})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6612})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6544})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6608})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6543})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6607})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6545})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6609})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6542})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6606})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6678})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6687})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6677})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6686})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6679})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS12 ],
                couplings = {(0,0):C.GC_6688})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS250, L.VVVVVSS265, L.VVVVVSS278, L.VVVVVSS44, L.VVVVVSS45, L.VVVVVSS47, L.VVVVVSS6, L.VVVVVSS64, L.VVVVVSS9 ],
                couplings = {(0,5):C.GC_322,(0,6):C.GC_2521,(0,8):C.GC_318,(0,4):C.GC_2518,(0,3):C.GC_326,(0,1):C.GC_324,(0,7):C.GC_1249,(0,2):C.GC_564,(0,0):C.GC_319})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS250, L.VVVVVSS265, L.VVVVVSS64 ],
                couplings = {(0,1):C.GC_464,(0,2):C.GC_1306,(0,0):C.GC_485})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS103, L.VVVVVSS15, L.VVVVVSS18, L.VVVVVSS182, L.VVVVVSS184, L.VVVVVSS185, L.VVVVVSS21, L.VVVVVSS221, L.VVVVVSS23, L.VVVVVSS240, L.VVVVVSS241, L.VVVVVSS244, L.VVVVVSS256, L.VVVVVSS268, L.VVVVVSS269, L.VVVVVSS270, L.VVVVVSS279, L.VVVVVSS36, L.VVVVVSS86, L.VVVVVSS89, L.VVVVVSS90, L.VVVVVSS91, L.VVVVVSS94 ],
                couplings = {(0,9):C.GC_315,(0,2):C.GC_1930,(0,22):C.GC_2526,(0,0):C.GC_856,(0,1):C.GC_2530,(0,23):C.GC_2958,(0,19):C.GC_2962,(0,3):C.GC_2523,(0,21):C.GC_313,(0,20):C.GC_1926,(0,7):C.GC_2955,(0,4):C.GC_854,(0,10):C.GC_316,(0,5):C.GC_1929,(0,6):C.GC_1933,(0,13):C.GC_2525,(0,16):C.GC_2529,(0,14):C.GC_2683,(0,15):C.GC_2957,(0,17):C.GC_2960,(0,11):C.GC_3021,(0,12):C.GC_2528,(0,18):C.GC_2959,(0,8):C.GC_314})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS184, L.VVVVVSS185, L.VVVVVSS221, L.VVVVVSS240, L.VVVVVSS244, L.VVVVVSS256, L.VVVVVSS269, L.VVVVVSS36 ],
                couplings = {(0,3):C.GC_538,(0,0):C.GC_2041,(0,1):C.GC_2059,(0,5):C.GC_2601,(0,6):C.GC_2976,(0,4):C.GC_2577,(0,7):C.GC_2971,(0,2):C.GC_523})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS14, L.VVVVVSS179, L.VVVVVSS180, L.VVVVVSS181, L.VVVVVSS22, L.VVVVVSS242, L.VVVVVSS252, L.VVVVVSS255, L.VVVVVSS27, L.VVVVVSS42, L.VVVVVSS70, L.VVVVVSS80 ],
                couplings = {(0,0):C.GC_835,(0,9):C.GC_2475,(0,8):C.GC_2465,(0,11):C.GC_1874,(0,4):C.GC_2456,(0,1):C.GC_1881,(0,2):C.GC_1884,(0,3):C.GC_1889,(0,6):C.GC_2461,(0,10):C.GC_2468,(0,5):C.GC_2675,(0,7):C.GC_2471})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS179, L.VVVVVSS181, L.VVVVVSS252, L.VVVVVSS70 ],
                couplings = {(0,0):C.GC_2036,(0,1):C.GC_2052,(0,2):C.GC_2597,(0,3):C.GC_2573})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS14, L.VVVVVSS179, L.VVVVVSS180, L.VVVVVSS181, L.VVVVVSS22, L.VVVVVSS27, L.VVVVVSS292, L.VVVVVSS305, L.VVVVVSS306, L.VVVVVSS43, L.VVVVVSS69, L.VVVVVSS80 ],
                couplings = {(0,0):C.GC_832,(0,9):C.GC_2474,(0,5):C.GC_2463,(0,11):C.GC_1877,(0,4):C.GC_2458,(0,1):C.GC_1879,(0,2):C.GC_1885,(0,3):C.GC_1892,(0,6):C.GC_2459,(0,10):C.GC_2466,(0,8):C.GC_2674,(0,7):C.GC_2472})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS179, L.VVVVVSS181, L.VVVVVSS292, L.VVVVVSS69 ],
                couplings = {(0,0):C.GC_2034,(0,1):C.GC_2055,(0,2):C.GC_2599,(0,3):C.GC_2571})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS119, L.VVVVVSS127, L.VVVVVSS129, L.VVVVVSS135, L.VVVVVSS138, L.VVVVVSS141, L.VVVVVSS150, L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS162, L.VVVVVSS164, L.VVVVVSS192, L.VVVVVSS197, L.VVVVVSS202, L.VVVVVSS219, L.VVVVVSS248, L.VVVVVSS259, L.VVVVVSS277, L.VVVVVSS280, L.VVVVVSS299, L.VVVVVSS3, L.VVVVVSS33, L.VVVVVSS4, L.VVVVVSS74 ],
                couplings = {(0,20):C.GC_1475,(0,3):C.GC_1913,(0,2):C.GC_2447,(0,5):C.GC_344,(0,1):C.GC_1900,(0,6):C.GC_355,(0,4):C.GC_2449,(0,22):C.GC_1895,(0,21):C.GC_2435,(0,12):C.GC_341,(0,18):C.GC_566,(0,7):C.GC_1479,(0,14):C.GC_2444,(0,16):C.GC_352,(0,17):C.GC_1898,(0,10):C.GC_1905,(0,15):C.GC_1909,(0,19):C.GC_2075,(0,13):C.GC_2453,(0,9):C.GC_2437,(0,23):C.GC_1470,(0,8):C.GC_1471,(0,0):C.GC_338,(0,11):C.GC_348})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS162, L.VVVVVSS164, L.VVVVVSS192, L.VVVVVSS197, L.VVVVVSS202, L.VVVVVSS277 ],
                couplings = {(0,5):C.GC_487,(0,0):C.GC_1590,(0,7):C.GC_2014,(0,3):C.GC_1999,(0,6):C.GC_2655,(0,2):C.GC_2632,(0,1):C.GC_1583,(0,4):C.GC_466})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS119, L.VVVVVSS127, L.VVVVVSS129, L.VVVVVSS136, L.VVVVVSS138, L.VVVVVSS141, L.VVVVVSS145, L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS162, L.VVVVVSS165, L.VVVVVSS192, L.VVVVVSS197, L.VVVVVSS202, L.VVVVVSS219, L.VVVVVSS243, L.VVVVVSS259, L.VVVVVSS266, L.VVVVVSS280, L.VVVVVSS289, L.VVVVVSS3, L.VVVVVSS33, L.VVVVVSS4, L.VVVVVSS74 ],
                couplings = {(0,20):C.GC_1474,(0,3):C.GC_1912,(0,2):C.GC_2446,(0,5):C.GC_346,(0,1):C.GC_1902,(0,6):C.GC_354,(0,4):C.GC_2448,(0,22):C.GC_1896,(0,21):C.GC_2434,(0,12):C.GC_340,(0,18):C.GC_565,(0,7):C.GC_1480,(0,14):C.GC_2442,(0,16):C.GC_350,(0,17):C.GC_1897,(0,10):C.GC_1904,(0,19):C.GC_1908,(0,15):C.GC_2074,(0,13):C.GC_2454,(0,9):C.GC_2439,(0,23):C.GC_1468,(0,8):C.GC_1473,(0,0):C.GC_337,(0,11):C.GC_349})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS162, L.VVVVVSS165, L.VVVVVSS192, L.VVVVVSS197, L.VVVVVSS202, L.VVVVVSS266 ],
                couplings = {(0,5):C.GC_489,(0,0):C.GC_1591,(0,7):C.GC_2015,(0,3):C.GC_1998,(0,6):C.GC_2656,(0,2):C.GC_2634,(0,1):C.GC_1585,(0,4):C.GC_467})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS12, L.VVVVVSS178, L.VVVVVSS182, L.VVVVVSS20, L.VVVVVSS217, L.VVVVVSS254, L.VVVVVSS263, L.VVVVVSS267, L.VVVVVSS32, L.VVVVVSS35, L.VVVVVSS96 ],
                couplings = {(0,0):C.GC_836,(0,11):C.GC_2473,(0,4):C.GC_2464,(0,9):C.GC_1874,(0,1):C.GC_2456,(0,10):C.GC_1881,(0,3):C.GC_1886,(0,2):C.GC_1889,(0,7):C.GC_2461,(0,5):C.GC_2468,(0,6):C.GC_2675,(0,8):C.GC_2471})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS178, L.VVVVVSS217, L.VVVVVSS263, L.VVVVVSS35 ],
                couplings = {(0,3):C.GC_2036,(0,0):C.GC_2052,(0,2):C.GC_2597,(0,1):C.GC_2573})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS12, L.VVVVVSS178, L.VVVVVSS182, L.VVVVVSS20, L.VVVVVSS218, L.VVVVVSS276, L.VVVVVSS301, L.VVVVVSS303, L.VVVVVSS32, L.VVVVVSS35, L.VVVVVSS97 ],
                couplings = {(0,0):C.GC_838,(0,11):C.GC_2474,(0,4):C.GC_2463,(0,9):C.GC_1873,(0,1):C.GC_2455,(0,10):C.GC_1883,(0,3):C.GC_1885,(0,2):C.GC_1888,(0,6):C.GC_2462,(0,5):C.GC_2469,(0,8):C.GC_2677,(0,7):C.GC_2470})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS178, L.VVVVVSS218, L.VVVVVSS276, L.VVVVVSS35 ],
                couplings = {(0,3):C.GC_2038,(0,0):C.GC_2051,(0,2):C.GC_2596,(0,1):C.GC_2574})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS1, L.VVVVVSS107, L.VVVVVSS109, L.VVVVVSS115, L.VVVVVSS125, L.VVVVVSS175, L.VVVVVSS199, L.VVVVVSS2, L.VVVVVSS203, L.VVVVVSS204, L.VVVVVSS220, L.VVVVVSS281, L.VVVVVSS290, L.VVVVVSS291, L.VVVVVSS293, L.VVVVVSS296, L.VVVVVSS37, L.VVVVVSS50, L.VVVVVSS52, L.VVVVVSS56, L.VVVVVSS60, L.VVVVVSS61, L.VVVVVSS66, L.VVVVVSS7 ],
                couplings = {(0,0):C.GC_1475,(0,3):C.GC_1911,(0,18):C.GC_2445,(0,4):C.GC_345,(0,1):C.GC_355,(0,2):C.GC_1901,(0,19):C.GC_2449,(0,7):C.GC_1895,(0,23):C.GC_2435,(0,16):C.GC_1469,(0,6):C.GC_342,(0,11):C.GC_567,(0,20):C.GC_1472,(0,21):C.GC_1478,(0,10):C.GC_2441,(0,15):C.GC_351,(0,13):C.GC_1898,(0,12):C.GC_1910,(0,14):C.GC_2076,(0,8):C.GC_2438,(0,9):C.GC_2452,(0,5):C.GC_1905,(0,17):C.GC_338,(0,22):C.GC_348})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS175, L.VVVVVSS199, L.VVVVVSS203, L.VVVVVSS204, L.VVVVVSS291, L.VVVVVSS60, L.VVVVVSS61, L.VVVVVSS66 ],
                couplings = {(0,1):C.GC_488,(0,5):C.GC_1584,(0,6):C.GC_1589,(0,4):C.GC_2014,(0,2):C.GC_2633,(0,3):C.GC_2654,(0,0):C.GC_1999,(0,7):C.GC_466})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS1, L.VVVVVSS108, L.VVVVVSS109, L.VVVVVSS116, L.VVVVVSS125, L.VVVVVSS174, L.VVVVVSS199, L.VVVVVSS2, L.VVVVVSS203, L.VVVVVSS204, L.VVVVVSS220, L.VVVVVSS249, L.VVVVVSS251, L.VVVVVSS253, L.VVVVVSS281, L.VVVVVSS296, L.VVVVVSS37, L.VVVVVSS50, L.VVVVVSS52, L.VVVVVSS56, L.VVVVVSS60, L.VVVVVSS61, L.VVVVVSS66, L.VVVVVSS7 ],
                couplings = {(0,0):C.GC_1476,(0,3):C.GC_1912,(0,18):C.GC_2446,(0,4):C.GC_346,(0,1):C.GC_353,(0,2):C.GC_1903,(0,19):C.GC_2450,(0,7):C.GC_1894,(0,23):C.GC_2436,(0,16):C.GC_1468,(0,6):C.GC_343,(0,14):C.GC_568,(0,20):C.GC_1473,(0,21):C.GC_1477,(0,10):C.GC_2443,(0,15):C.GC_350,(0,12):C.GC_1899,(0,11):C.GC_1907,(0,13):C.GC_2077,(0,8):C.GC_2440,(0,9):C.GC_2451,(0,5):C.GC_1906,(0,17):C.GC_339,(0,22):C.GC_347})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS174, L.VVVVVSS199, L.VVVVVSS203, L.VVVVVSS204, L.VVVVVSS251, L.VVVVVSS60, L.VVVVVSS61, L.VVVVVSS66 ],
                couplings = {(0,1):C.GC_486,(0,5):C.GC_1585,(0,6):C.GC_1588,(0,4):C.GC_2013,(0,2):C.GC_2635,(0,3):C.GC_2653,(0,0):C.GC_2000,(0,7):C.GC_465})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS121, L.VVVVVSS126, L.VVVVVSS236, L.VVVVVSS237, L.VVVVVSS238, L.VVVVVSS38, L.VVVVVSS51, L.VVVVVSS59, L.VVVVVSS71 ],
                couplings = {(0,1):C.GC_1843,(0,0):C.GC_1851,(0,4):C.GC_1842,(0,3):C.GC_1847,(0,2):C.GC_2071,(0,5):C.GC_1450,(0,6):C.GC_1841,(0,7):C.GC_746,(0,8):C.GC_1845})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS238, L.VVVVVSS59, L.VVVVVSS71 ],
                couplings = {(0,0):C.GC_2012,(0,1):C.GC_776,(0,2):C.GC_1997})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS122, L.VVVVVSS123, L.VVVVVSS239, L.VVVVVSS294, L.VVVVVSS298, L.VVVVVSS302, L.VVVVVSS38, L.VVVVVSS51, L.VVVVVSS59 ],
                couplings = {(0,1):C.GC_1844,(0,0):C.GC_1849,(0,2):C.GC_1842,(0,4):C.GC_1848,(0,3):C.GC_2072,(0,6):C.GC_1449,(0,7):C.GC_1841,(0,8):C.GC_747,(0,5):C.GC_1845})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS239, L.VVVVVSS302, L.VVVVVSS59 ],
                couplings = {(0,0):C.GC_2012,(0,2):C.GC_777,(0,1):C.GC_1997})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS121, L.VVVVVSS126, L.VVVVVSS236, L.VVVVVSS237, L.VVVVVSS238, L.VVVVVSS38, L.VVVVVSS51, L.VVVVVSS59, L.VVVVVSS71 ],
                couplings = {(0,1):C.GC_1843,(0,0):C.GC_1851,(0,4):C.GC_1842,(0,3):C.GC_1847,(0,2):C.GC_2071,(0,5):C.GC_1450,(0,6):C.GC_1841,(0,7):C.GC_746,(0,8):C.GC_1845})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS238, L.VVVVVSS59, L.VVVVVSS71 ],
                couplings = {(0,0):C.GC_2012,(0,1):C.GC_776,(0,2):C.GC_1997})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS11, L.VVVVVSS12, L.VVVVVSS198, L.VVVVVSS200, L.VVVVVSS201, L.VVVVVSS215, L.VVVVVSS235, L.VVVVVSS30, L.VVVVVSS85, L.VVVVVSS98, L.VVVVVSS99 ],
                couplings = {(0,10):C.GC_1453,(0,7):C.GC_1457,(0,9):C.GC_2505,(0,8):C.GC_2509,(0,1):C.GC_1451,(0,0):C.GC_1839,(0,3):C.GC_1452,(0,5):C.GC_1454,(0,2):C.GC_1235,(0,6):C.GC_1594,(0,4):C.GC_829})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS198, L.VVVVVSS200, L.VVVVVSS201, L.VVVVVSS215 ],
                couplings = {(0,1):C.GC_1572,(0,3):C.GC_1562,(0,0):C.GC_2680,(0,2):C.GC_927})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS11, L.VVVVVSS12, L.VVVVVSS198, L.VVVVVSS201, L.VVVVVSS216, L.VVVVVSS260, L.VVVVVSS264, L.VVVVVSS274, L.VVVVVSS275, L.VVVVVSS300, L.VVVVVSS31, L.VVVVVSS34, L.VVVVVSS85, L.VVVVVSS98, L.VVVVVSS99 ],
                couplings = {(0,14):C.GC_1453,(0,10):C.GC_1459,(0,13):C.GC_2506,(0,12):C.GC_2509,(0,1):C.GC_1451,(0,0):C.GC_1840,(0,6):C.GC_1452,(0,4):C.GC_1454,(0,8):C.GC_1456,(0,9):C.GC_1594,(0,2):C.GC_2508,(0,7):C.GC_2679,(0,11):C.GC_2507,(0,3):C.GC_828,(0,5):C.GC_2504})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS201, L.VVVVVSS216, L.VVVVVSS260, L.VVVVVSS264, L.VVVVVSS34 ],
                couplings = {(0,3):C.GC_1572,(0,1):C.GC_1562,(0,4):C.GC_2575,(0,0):C.GC_926,(0,2):C.GC_2600})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS11, L.VVVVVSS12, L.VVVVVSS198, L.VVVVVSS200, L.VVVVVSS201, L.VVVVVSS215, L.VVVVVSS235, L.VVVVVSS30, L.VVVVVSS85, L.VVVVVSS98, L.VVVVVSS99 ],
                couplings = {(0,10):C.GC_1453,(0,7):C.GC_1457,(0,9):C.GC_2505,(0,8):C.GC_2509,(0,1):C.GC_1451,(0,0):C.GC_1839,(0,3):C.GC_1452,(0,5):C.GC_1454,(0,2):C.GC_1235,(0,6):C.GC_1594,(0,4):C.GC_829})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS198, L.VVVVVSS200, L.VVVVVSS201, L.VVVVVSS215 ],
                couplings = {(0,1):C.GC_1572,(0,3):C.GC_1562,(0,0):C.GC_2680,(0,2):C.GC_927})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS39, L.VVVVVSS41, L.VVVVVSS46, L.VVVVVSS6, L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,2):C.GC_4115,(0,1):C.GC_4121,(0,3):C.GC_3561,(0,0):C.GC_3550,(0,5):C.GC_4119,(0,6):C.GC_3564,(0,4):C.GC_3553})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,1):C.GC_4237,(0,2):C.GC_3710,(0,0):C.GC_3683})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS39, L.VVVVVSS41, L.VVVVVSS46, L.VVVVVSS6, L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,2):C.GC_4114,(0,1):C.GC_4123,(0,3):C.GC_3559,(0,0):C.GC_3551,(0,5):C.GC_4117,(0,6):C.GC_3565,(0,4):C.GC_3552})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,1):C.GC_4238,(0,2):C.GC_3711,(0,0):C.GC_3682})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS101, L.VVVVVSS14, L.VVVVVSS180, L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS19, L.VVVVVSS207, L.VVVVVSS210, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS24, L.VVVVVSS25, L.VVVVVSS26, L.VVVVVSS40, L.VVVVVSS67, L.VVVVVSS81, L.VVVVVSS83, L.VVVVVSS92 ],
                couplings = {(0,14):C.GC_379,(0,13):C.GC_4109,(0,2):C.GC_1952,(0,0):C.GC_3567,(0,1):C.GC_2938,(0,15):C.GC_3211,(0,17):C.GC_2539,(0,12):C.GC_3135,(0,6):C.GC_369,(0,19):C.GC_1945,(0,18):C.GC_3127,(0,16):C.GC_372,(0,8):C.GC_376,(0,9):C.GC_381,(0,5):C.GC_865,(0,3):C.GC_1949,(0,11):C.GC_3570,(0,10):C.GC_3139,(0,7):C.GC_3134,(0,4):C.GC_3130})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS67 ],
                couplings = {(0,5):C.GC_525,(0,2):C.GC_540,(0,1):C.GC_930,(0,4):C.GC_3731,(0,3):C.GC_3169,(0,0):C.GC_3161})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS101, L.VVVVVSS14, L.VVVVVSS180, L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS19, L.VVVVVSS207, L.VVVVVSS210, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS24, L.VVVVVSS25, L.VVVVVSS26, L.VVVVVSS40, L.VVVVVSS67, L.VVVVVSS81, L.VVVVVSS83, L.VVVVVSS92 ],
                couplings = {(0,14):C.GC_377,(0,13):C.GC_4110,(0,2):C.GC_1950,(0,0):C.GC_3566,(0,1):C.GC_2936,(0,15):C.GC_3209,(0,17):C.GC_2541,(0,12):C.GC_3137,(0,6):C.GC_368,(0,19):C.GC_1944,(0,18):C.GC_3126,(0,16):C.GC_373,(0,8):C.GC_374,(0,9):C.GC_382,(0,5):C.GC_866,(0,3):C.GC_1947,(0,11):C.GC_3569,(0,10):C.GC_3138,(0,7):C.GC_3132,(0,4):C.GC_3131})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS67 ],
                couplings = {(0,5):C.GC_526,(0,2):C.GC_541,(0,1):C.GC_931,(0,4):C.GC_3732,(0,3):C.GC_3168,(0,0):C.GC_3162})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS16, L.VVVVVSS182, L.VVVVVSS187, L.VVVVVSS188, L.VVVVVSS279, L.VVVVVSS84, L.VVVVVSS93, L.VVVVVSS94 ],
                couplings = {(0,0):C.GC_855,(0,1):C.GC_857,(0,8):C.GC_3593,(0,6):C.GC_3598,(0,2):C.GC_853,(0,4):C.GC_858,(0,5):C.GC_3596,(0,7):C.GC_851,(0,3):C.GC_852})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS187, L.VVVVVSS188, L.VVVVVSS279 ],
                couplings = {(0,1):C.GC_928,(0,2):C.GC_3733,(0,0):C.GC_924})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS16, L.VVVVVSS182, L.VVVVVSS187, L.VVVVVSS188, L.VVVVVSS279, L.VVVVVSS84, L.VVVVVSS93, L.VVVVVSS94 ],
                couplings = {(0,0):C.GC_855,(0,1):C.GC_857,(0,8):C.GC_3593,(0,6):C.GC_3598,(0,2):C.GC_853,(0,4):C.GC_858,(0,5):C.GC_3596,(0,7):C.GC_851,(0,3):C.GC_852})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS187, L.VVVVVSS188, L.VVVVVSS279 ],
                couplings = {(0,1):C.GC_928,(0,2):C.GC_3733,(0,0):C.GC_924})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS117, L.VVVVVSS137, L.VVVVVSS139, L.VVVVVSS143, L.VVVVVSS154, L.VVVVVSS155, L.VVVVVSS157, L.VVVVVSS158, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS171, L.VVVVVSS172, L.VVVVVSS176, L.VVVVVSS190, L.VVVVVSS208, L.VVVVVSS48, L.VVVVVSS5, L.VVVVVSS53, L.VVVVVSS54, L.VVVVVSS55, L.VVVVVSS63, L.VVVVVSS76, L.VVVVVSS78, L.VVVVVSS79 ],
                couplings = {(0,3):C.GC_860,(0,16):C.GC_1521,(0,1):C.GC_2520,(0,2):C.GC_2952,(0,19):C.GC_328,(0,18):C.GC_1939,(0,15):C.GC_3125,(0,17):C.GC_3588,(0,20):C.GC_4097,(0,11):C.GC_562,(0,10):C.GC_2078,(0,14):C.GC_3585,(0,21):C.GC_1516,(0,23):C.GC_2516,(0,22):C.GC_2947,(0,12):C.GC_862,(0,6):C.GC_1519,(0,4):C.GC_1522,(0,5):C.GC_2519,(0,8):C.GC_2522,(0,9):C.GC_2953,(0,7):C.GC_2949,(0,0):C.GC_4096,(0,13):C.GC_4098})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS154, L.VVVVVSS155, L.VVVVVSS157, L.VVVVVSS158, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS190, L.VVVVVSS63 ],
                couplings = {(0,7):C.GC_4235,(0,2):C.GC_1587,(0,0):C.GC_1592,(0,1):C.GC_2636,(0,4):C.GC_2657,(0,5):C.GC_3011,(0,3):C.GC_3000,(0,6):C.GC_4147})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS110, L.VVVVVSS117, L.VVVVVSS118, L.VVVVVSS128, L.VVVVVSS131, L.VVVVVSS140, L.VVVVVSS142, L.VVVVVSS143, L.VVVVVSS151, L.VVVVVSS154, L.VVVVVSS157, L.VVVVVSS159, L.VVVVVSS168, L.VVVVVSS169, L.VVVVVSS170, L.VVVVVSS173, L.VVVVVSS176, L.VVVVVSS190, L.VVVVVSS191, L.VVVVVSS208, L.VVVVVSS247, L.VVVVVSS257, L.VVVVVSS258, L.VVVVVSS261, L.VVVVVSS262, L.VVVVVSS48, L.VVVVVSS5, L.VVVVVSS53, L.VVVVVSS63, L.VVVVVSS73, L.VVVVVSS75, L.VVVVVSS76 ],
                couplings = {(0,7):C.GC_321,(0,26):C.GC_1520,(0,6):C.GC_1936,(0,4):C.GC_2520,(0,3):C.GC_2951,(0,5):C.GC_1939,(0,25):C.GC_3124,(0,8):C.GC_327,(0,27):C.GC_3587,(0,29):C.GC_2517,(0,2):C.GC_317,(0,0):C.GC_1934,(0,30):C.GC_2948,(0,24):C.GC_320,(0,18):C.GC_323,(0,23):C.GC_563,(0,22):C.GC_1935,(0,20):C.GC_1937,(0,21):C.GC_2079,(0,28):C.GC_3122,(0,19):C.GC_3586,(0,31):C.GC_1517,(0,16):C.GC_325,(0,10):C.GC_1518,(0,9):C.GC_1523,(0,15):C.GC_1938,(0,14):C.GC_2519,(0,13):C.GC_2522,(0,12):C.GC_2954,(0,11):C.GC_2950,(0,1):C.GC_3121,(0,17):C.GC_3123})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS154, L.VVVVVSS157, L.VVVVVSS159, L.VVVVVSS168, L.VVVVVSS169, L.VVVVVSS170, L.VVVVVSS190, L.VVVVVSS191, L.VVVVVSS247, L.VVVVVSS258, L.VVVVVSS262, L.VVVVVSS63 ],
                couplings = {(0,10):C.GC_484,(0,7):C.GC_463,(0,9):C.GC_2016,(0,8):C.GC_2001,(0,11):C.GC_4234,(0,1):C.GC_1586,(0,0):C.GC_1593,(0,5):C.GC_2636,(0,4):C.GC_2657,(0,3):C.GC_3012,(0,2):C.GC_3001,(0,6):C.GC_3150})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS117, L.VVVVVSS137, L.VVVVVSS139, L.VVVVVSS143, L.VVVVVSS154, L.VVVVVSS155, L.VVVVVSS157, L.VVVVVSS158, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS171, L.VVVVVSS172, L.VVVVVSS176, L.VVVVVSS190, L.VVVVVSS208, L.VVVVVSS48, L.VVVVVSS5, L.VVVVVSS53, L.VVVVVSS54, L.VVVVVSS55, L.VVVVVSS63, L.VVVVVSS76, L.VVVVVSS78, L.VVVVVSS79 ],
                couplings = {(0,3):C.GC_860,(0,16):C.GC_1521,(0,1):C.GC_2520,(0,2):C.GC_2952,(0,19):C.GC_328,(0,18):C.GC_1939,(0,15):C.GC_3125,(0,17):C.GC_3588,(0,20):C.GC_4097,(0,11):C.GC_562,(0,10):C.GC_2078,(0,14):C.GC_3585,(0,21):C.GC_1516,(0,23):C.GC_2516,(0,22):C.GC_2947,(0,12):C.GC_862,(0,6):C.GC_1519,(0,4):C.GC_1522,(0,5):C.GC_2519,(0,8):C.GC_2522,(0,9):C.GC_2953,(0,7):C.GC_2949,(0,0):C.GC_4096,(0,13):C.GC_4098})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS154, L.VVVVVSS155, L.VVVVVSS157, L.VVVVVSS158, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS190, L.VVVVVSS63 ],
                couplings = {(0,7):C.GC_4235,(0,2):C.GC_1587,(0,0):C.GC_1592,(0,1):C.GC_2636,(0,4):C.GC_2657,(0,5):C.GC_3011,(0,3):C.GC_3000,(0,6):C.GC_4147})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS39, L.VVVVVSS41, L.VVVVVSS46, L.VVVVVSS6, L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,2):C.GC_4116,(0,1):C.GC_4121,(0,3):C.GC_3562,(0,0):C.GC_3549,(0,5):C.GC_4120,(0,6):C.GC_3563,(0,4):C.GC_3554})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,1):C.GC_4236,(0,2):C.GC_3709,(0,0):C.GC_3684})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS39, L.VVVVVSS41, L.VVVVVSS46, L.VVVVVSS6, L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,2):C.GC_4114,(0,1):C.GC_4122,(0,3):C.GC_3560,(0,0):C.GC_3551,(0,5):C.GC_4118,(0,6):C.GC_3565,(0,4):C.GC_3552})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS62, L.VVVVVSS64, L.VVVVVSS65 ],
                couplings = {(0,1):C.GC_4238,(0,2):C.GC_3711,(0,0):C.GC_3682})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS101, L.VVVVVSS14, L.VVVVVSS180, L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS19, L.VVVVVSS207, L.VVVVVSS210, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS24, L.VVVVVSS25, L.VVVVVSS26, L.VVVVVSS40, L.VVVVVSS67, L.VVVVVSS81, L.VVVVVSS83, L.VVVVVSS92 ],
                couplings = {(0,14):C.GC_379,(0,13):C.GC_4108,(0,2):C.GC_1952,(0,0):C.GC_3568,(0,1):C.GC_2938,(0,15):C.GC_3211,(0,17):C.GC_2539,(0,12):C.GC_3135,(0,6):C.GC_370,(0,19):C.GC_1946,(0,18):C.GC_3128,(0,16):C.GC_371,(0,8):C.GC_376,(0,9):C.GC_380,(0,5):C.GC_864,(0,3):C.GC_1949,(0,11):C.GC_3571,(0,10):C.GC_3140,(0,7):C.GC_3134,(0,4):C.GC_3129})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS67 ],
                couplings = {(0,5):C.GC_524,(0,2):C.GC_539,(0,1):C.GC_929,(0,4):C.GC_3730,(0,3):C.GC_3170,(0,0):C.GC_3160})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS101, L.VVVVVSS14, L.VVVVVSS180, L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS19, L.VVVVVSS207, L.VVVVVSS210, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS24, L.VVVVVSS25, L.VVVVVSS26, L.VVVVVSS40, L.VVVVVSS67, L.VVVVVSS81, L.VVVVVSS83, L.VVVVVSS92 ],
                couplings = {(0,14):C.GC_378,(0,13):C.GC_4110,(0,2):C.GC_1951,(0,0):C.GC_3566,(0,1):C.GC_2937,(0,15):C.GC_3210,(0,17):C.GC_2540,(0,12):C.GC_3136,(0,6):C.GC_368,(0,19):C.GC_1944,(0,18):C.GC_3126,(0,16):C.GC_373,(0,8):C.GC_375,(0,9):C.GC_382,(0,5):C.GC_866,(0,3):C.GC_1948,(0,11):C.GC_3569,(0,10):C.GC_3138,(0,7):C.GC_3133,(0,4):C.GC_3131})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS183, L.VVVVVSS186, L.VVVVVSS211, L.VVVVVSS223, L.VVVVVSS227, L.VVVVVSS67 ],
                couplings = {(0,5):C.GC_526,(0,2):C.GC_541,(0,1):C.GC_931,(0,4):C.GC_3732,(0,3):C.GC_3168,(0,0):C.GC_3162})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS152, L.VVVVVSS17, L.VVVVVSS206, L.VVVVVSS207, L.VVVVVSS212, L.VVVVVSS22, L.VVVVVSS24, L.VVVVVSS245, L.VVVVVSS272, L.VVVVVSS28, L.VVVVVSS282, L.VVVVVSS286, L.VVVVVSS287, L.VVVVVSS295, L.VVVVVSS40, L.VVVVVSS68, L.VVVVVSS95 ],
                couplings = {(0,17):C.GC_1494,(0,0):C.GC_2464,(0,15):C.GC_2939,(0,7):C.GC_834,(0,2):C.GC_1875,(0,6):C.GC_2457,(0,10):C.GC_2475,(0,5):C.GC_2460,(0,16):C.GC_2467,(0,14):C.GC_2471,(0,11):C.GC_2676,(0,4):C.GC_333,(0,3):C.GC_1891,(0,8):C.GC_1482,(0,13):C.GC_1489,(0,9):C.GC_1597,(0,1):C.GC_1880,(0,12):C.GC_1485})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS152, L.VVVVVSS206, L.VVVVVSS212, L.VVVVVSS245, L.VVVVVSS286, L.VVVVVSS68 ],
                couplings = {(0,2):C.GC_2598,(0,5):C.GC_2572,(0,1):C.GC_2054,(0,3):C.GC_1574,(0,0):C.GC_2035,(0,4):C.GC_1563})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS152, L.VVVVVSS17, L.VVVVVSS206, L.VVVVVSS207, L.VVVVVSS212, L.VVVVVSS22, L.VVVVVSS24, L.VVVVVSS245, L.VVVVVSS272, L.VVVVVSS28, L.VVVVVSS282, L.VVVVVSS286, L.VVVVVSS287, L.VVVVVSS295, L.VVVVVSS40, L.VVVVVSS68, L.VVVVVSS95 ],
                couplings = {(0,17):C.GC_1492,(0,0):C.GC_2463,(0,15):C.GC_2941,(0,7):C.GC_831,(0,2):C.GC_1872,(0,6):C.GC_2458,(0,10):C.GC_2474,(0,5):C.GC_2459,(0,16):C.GC_2466,(0,14):C.GC_2470,(0,11):C.GC_2678,(0,4):C.GC_334,(0,3):C.GC_1887,(0,8):C.GC_1481,(0,13):C.GC_1491,(0,9):C.GC_1596,(0,1):C.GC_1879,(0,12):C.GC_1487})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS152, L.VVVVVSS206, L.VVVVVSS212, L.VVVVVSS245, L.VVVVVSS286, L.VVVVVSS68 ],
                couplings = {(0,2):C.GC_2599,(0,5):C.GC_2571,(0,1):C.GC_2050,(0,3):C.GC_1576,(0,0):C.GC_2034,(0,4):C.GC_1565})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS114, L.VVVVVSS124, L.VVVVVSS177, L.VVVVVSS205, L.VVVVVSS208, L.VVVVVSS209, L.VVVVVSS238, L.VVVVVSS283, L.VVVVVSS284, L.VVVVVSS285, L.VVVVVSS297, L.VVVVVSS304, L.VVVVVSS48, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS53, L.VVVVVSS57, L.VVVVVSS71 ],
                couplings = {(0,0):C.GC_1494,(0,1):C.GC_2465,(0,12):C.GC_2939,(0,15):C.GC_833,(0,13):C.GC_1876,(0,6):C.GC_2461,(0,11):C.GC_2471,(0,10):C.GC_2676,(0,4):C.GC_336,(0,3):C.GC_1882,(0,5):C.GC_1890,(0,9):C.GC_1483,(0,7):C.GC_1490,(0,8):C.GC_1598,(0,14):C.GC_2457,(0,16):C.GC_2473,(0,17):C.GC_2467,(0,2):C.GC_1486})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS177, L.VVVVVSS205, L.VVVVVSS209, L.VVVVVSS238, L.VVVVVSS285, L.VVVVVSS71 ],
                couplings = {(0,3):C.GC_2597,(0,1):C.GC_2037,(0,2):C.GC_2053,(0,4):C.GC_1575,(0,5):C.GC_2572,(0,0):C.GC_1564})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS114, L.VVVVVSS124, L.VVVVVSS177, L.VVVVVSS205, L.VVVVVSS208, L.VVVVVSS209, L.VVVVVSS238, L.VVVVVSS283, L.VVVVVSS284, L.VVVVVSS285, L.VVVVVSS297, L.VVVVVSS304, L.VVVVVSS48, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS53, L.VVVVVSS57, L.VVVVVSS71 ],
                couplings = {(0,0):C.GC_1493,(0,1):C.GC_2463,(0,12):C.GC_2940,(0,15):C.GC_837,(0,13):C.GC_1872,(0,6):C.GC_2459,(0,11):C.GC_2472,(0,10):C.GC_2673,(0,4):C.GC_335,(0,3):C.GC_1878,(0,5):C.GC_1893,(0,9):C.GC_1484,(0,7):C.GC_1488,(0,8):C.GC_1599,(0,14):C.GC_2455,(0,16):C.GC_2474,(0,17):C.GC_2469,(0,2):C.GC_1487})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS177, L.VVVVVSS205, L.VVVVVSS209, L.VVVVVSS238, L.VVVVVSS285, L.VVVVVSS71 ],
                couplings = {(0,3):C.GC_2599,(0,1):C.GC_2033,(0,2):C.GC_2056,(0,4):C.GC_1573,(0,5):C.GC_2574,(0,0):C.GC_1565})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS111, L.VVVVVSS112, L.VVVVVSS113, L.VVVVVSS130, L.VVVVVSS132, L.VVVVVSS133, L.VVVVVSS134, L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229, L.VVVVVSS72, L.VVVVVSS77 ],
                couplings = {(0,5):C.GC_868,(0,6):C.GC_385,(0,3):C.GC_4362,(0,4):C.GC_3143,(0,2):C.GC_1953,(0,1):C.GC_2537,(0,14):C.GC_2928,(0,13):C.GC_3555,(0,10):C.GC_1257,(0,8):C.GC_2931,(0,11):C.GC_2934,(0,12):C.GC_3207,(0,15):C.GC_1533,(0,0):C.GC_3201,(0,7):C.GC_753,(0,9):C.GC_3204})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229 ],
                couplings = {(0,6):C.GC_934,(0,3):C.GC_1308,(0,1):C.GC_2998,(0,4):C.GC_3009,(0,5):C.GC_3222,(0,0):C.GC_779,(0,2):C.GC_3216})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS111, L.VVVVVSS112, L.VVVVVSS113, L.VVVVVSS130, L.VVVVVSS132, L.VVVVVSS133, L.VVVVVSS134, L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229, L.VVVVVSS72, L.VVVVVSS77 ],
                couplings = {(0,5):C.GC_867,(0,6):C.GC_383,(0,3):C.GC_4361,(0,4):C.GC_3141,(0,2):C.GC_1955,(0,1):C.GC_2536,(0,14):C.GC_2927,(0,13):C.GC_3558,(0,10):C.GC_1256,(0,8):C.GC_2930,(0,11):C.GC_2933,(0,12):C.GC_3208,(0,15):C.GC_1532,(0,0):C.GC_3202,(0,7):C.GC_754,(0,9):C.GC_3203})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229 ],
                couplings = {(0,6):C.GC_935,(0,3):C.GC_1307,(0,1):C.GC_2997,(0,4):C.GC_3008,(0,5):C.GC_3223,(0,0):C.GC_780,(0,2):C.GC_3215})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS111, L.VVVVVSS112, L.VVVVVSS113, L.VVVVVSS130, L.VVVVVSS132, L.VVVVVSS133, L.VVVVVSS134, L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229, L.VVVVVSS72, L.VVVVVSS77 ],
                couplings = {(0,5):C.GC_869,(0,6):C.GC_385,(0,3):C.GC_4363,(0,4):C.GC_3143,(0,2):C.GC_1953,(0,1):C.GC_2538,(0,14):C.GC_2929,(0,13):C.GC_3556,(0,10):C.GC_1258,(0,8):C.GC_2932,(0,11):C.GC_2935,(0,12):C.GC_3206,(0,15):C.GC_1534,(0,0):C.GC_3200,(0,7):C.GC_752,(0,9):C.GC_3205})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229 ],
                couplings = {(0,6):C.GC_933,(0,3):C.GC_1309,(0,1):C.GC_2999,(0,4):C.GC_3010,(0,5):C.GC_3221,(0,0):C.GC_778,(0,2):C.GC_3217})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS111, L.VVVVVSS112, L.VVVVVSS113, L.VVVVVSS130, L.VVVVVSS132, L.VVVVVSS133, L.VVVVVSS134, L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229, L.VVVVVSS72, L.VVVVVSS77 ],
                couplings = {(0,5):C.GC_867,(0,6):C.GC_384,(0,3):C.GC_4360,(0,4):C.GC_3142,(0,2):C.GC_1954,(0,1):C.GC_2536,(0,14):C.GC_2927,(0,13):C.GC_3557,(0,10):C.GC_1256,(0,8):C.GC_2930,(0,11):C.GC_2933,(0,12):C.GC_3208,(0,15):C.GC_1532,(0,0):C.GC_3202,(0,7):C.GC_754,(0,9):C.GC_3203})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS156, L.VVVVVSS163, L.VVVVVSS189, L.VVVVVSS194, L.VVVVVSS214, L.VVVVVSS222, L.VVVVVSS229 ],
                couplings = {(0,6):C.GC_935,(0,3):C.GC_1307,(0,1):C.GC_2997,(0,4):C.GC_3008,(0,5):C.GC_3223,(0,0):C.GC_780,(0,2):C.GC_3215})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS104, L.VVVVVSS105, L.VVVVVSS111, L.VVVVVSS120, L.VVVVVSS130, L.VVVVVSS144, L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS230, L.VVVVVSS232, L.VVVVVSS233, L.VVVVVSS82, L.VVVVVSS87, L.VVVVVSS88 ],
                couplings = {(0,4):C.GC_4094,(0,5):C.GC_1250,(0,0):C.GC_312,(0,17):C.GC_1527,(0,1):C.GC_1924,(0,15):C.GC_2531,(0,11):C.GC_1253,(0,9):C.GC_3591,(0,12):C.GC_1600,(0,13):C.GC_1927,(0,10):C.GC_1932,(0,14):C.GC_2682,(0,8):C.GC_3120,(0,3):C.GC_3590,(0,16):C.GC_2963,(0,2):C.GC_3116,(0,7):C.GC_3594,(0,6):C.GC_3117})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS232 ],
                couplings = {(0,5):C.GC_542,(0,3):C.GC_3735,(0,6):C.GC_2039,(0,4):C.GC_2058,(0,2):C.GC_3167,(0,1):C.GC_3637,(0,0):C.GC_3158})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS104, L.VVVVVSS105, L.VVVVVSS111, L.VVVVVSS120, L.VVVVVSS130, L.VVVVVSS144, L.VVVVVSS148, L.VVVVVSS149, L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS195, L.VVVVVSS196, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS225, L.VVVVVSS226, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS231, L.VVVVVSS232, L.VVVVVSS234, L.VVVVVSS87 ],
                couplings = {(0,4):C.GC_4095,(0,5):C.GC_1251,(0,0):C.GC_312,(0,7):C.GC_1526,(0,1):C.GC_1925,(0,6):C.GC_2531,(0,17):C.GC_1254,(0,15):C.GC_1524,(0,18):C.GC_1600,(0,19):C.GC_1928,(0,16):C.GC_1931,(0,14):C.GC_2524,(0,20):C.GC_2681,(0,13):C.GC_2956,(0,12):C.GC_3119,(0,10):C.GC_1525,(0,11):C.GC_2527,(0,3):C.GC_3589,(0,21):C.GC_2961,(0,2):C.GC_3115,(0,9):C.GC_2959,(0,8):C.GC_3118})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS195, L.VVVVVSS196, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS225, L.VVVVVSS226, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS232 ],
                couplings = {(0,9):C.GC_542,(0,7):C.GC_1577,(0,10):C.GC_2040,(0,8):C.GC_2057,(0,6):C.GC_2602,(0,5):C.GC_3734,(0,4):C.GC_3166,(0,2):C.GC_1566,(0,3):C.GC_2576,(0,1):C.GC_2971,(0,0):C.GC_3159})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS104, L.VVVVVSS105, L.VVVVVSS111, L.VVVVVSS120, L.VVVVVSS130, L.VVVVVSS144, L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS230, L.VVVVVSS232, L.VVVVVSS233, L.VVVVVSS82, L.VVVVVSS87, L.VVVVVSS88 ],
                couplings = {(0,4):C.GC_4094,(0,5):C.GC_1250,(0,0):C.GC_312,(0,17):C.GC_1527,(0,1):C.GC_1924,(0,15):C.GC_2531,(0,11):C.GC_1253,(0,9):C.GC_3591,(0,12):C.GC_1600,(0,13):C.GC_1927,(0,10):C.GC_1932,(0,14):C.GC_2682,(0,8):C.GC_3120,(0,3):C.GC_3590,(0,16):C.GC_2963,(0,2):C.GC_3116,(0,7):C.GC_3594,(0,6):C.GC_3117})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS189, L.VVVVVSS193, L.VVVVVSS222, L.VVVVVSS224, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS232 ],
                couplings = {(0,5):C.GC_542,(0,3):C.GC_3735,(0,6):C.GC_2039,(0,4):C.GC_2058,(0,2):C.GC_3167,(0,1):C.GC_3637,(0,0):C.GC_3158})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS106, L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4105,(0,1):C.GC_4112})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4208})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS106, L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4106,(0,1):C.GC_4113})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4209})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS106, L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4104,(0,1):C.GC_4111})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4207})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS106, L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4107,(0,1):C.GC_4113})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS213 ],
                couplings = {(0,0):C.GC_4209})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS44 ],
                couplings = {(0,0):C.GC_6043})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS44 ],
                couplings = {(0,0):C.GC_6110})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS10 ],
                couplings = {(0,0):C.GC_6042})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS10 ],
                couplings = {(0,0):C.GC_6109})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS30, L.VVVVVVS34, L.VVVVVVS39, L.VVVVVVS8 ],
                couplings = {(0,1):C.GC_4874,(0,2):C.GC_4876,(0,0):C.GC_4940,(0,3):C.GC_4875})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS34, L.VVVVVVS8 ],
                couplings = {(0,0):C.GC_4909,(0,1):C.GC_4899})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS288, L.VVVVVSS8 ],
                couplings = {(0,1):C.GC_1422,(0,0):C.GC_745})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS288 ],
                couplings = {(0,0):C.GC_783})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS288, L.VVVVVSS8 ],
                couplings = {(0,1):C.GC_1424,(0,0):C.GC_743})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS288 ],
                couplings = {(0,0):C.GC_781})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS23 ],
                couplings = {(0,0):C.GC_5521})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS23 ],
                couplings = {(0,0):C.GC_5539})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS15 ],
                couplings = {(0,0):C.GC_5522})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS15 ],
                couplings = {(0,0):C.GC_5540})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS153, L.VVVVVSS87 ],
                couplings = {(0,0):C.GC_744,(0,1):C.GC_1422})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS153 ],
                couplings = {(0,0):C.GC_782})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS153, L.VVVVVSS87 ],
                couplings = {(0,0):C.GC_743,(0,1):C.GC_1423})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS153 ],
                couplings = {(0,0):C.GC_781})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS46 ],
                couplings = {(0,0):C.GC_5480})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS46 ],
                couplings = {(0,0):C.GC_5496})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS260, L.VVVVVSS29, L.VVVVVSS34 ],
                couplings = {(0,1):C.GC_3597,(0,2):C.GC_3595,(0,0):C.GC_3592})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS260, L.VVVVVSS34 ],
                couplings = {(0,1):C.GC_3638,(0,0):C.GC_3736})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS1, L.VVVVVVS19, L.VVVVVVS25, L.VVVVVVS27, L.VVVVVVS36, L.VVVVVVS38, L.VVVVVVS39, L.VVVVVVS9 ],
                couplings = {(0,0):C.GC_5737,(0,4):C.GC_4557,(0,6):C.GC_5736,(0,5):C.GC_4598,(0,2):C.GC_4888,(0,3):C.GC_4942,(0,1):C.GC_4890,(0,7):C.GC_4559})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS19, L.VVVVVVS25, L.VVVVVVS36, L.VVVVVVS9 ],
                couplings = {(0,2):C.GC_4576,(0,1):C.GC_4911,(0,0):C.GC_4900,(0,3):C.GC_4567})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS2, L.VVVVVVS20, L.VVVVVVS31, L.VVVVVVS33, L.VVVVVVS48, L.VVVVVVS52, L.VVVVVVS55, L.VVVVVVS57 ],
                couplings = {(0,0):C.GC_5738,(0,6):C.GC_4558,(0,3):C.GC_5735,(0,4):C.GC_4599,(0,5):C.GC_4889,(0,1):C.GC_4891,(0,7):C.GC_4943,(0,2):C.GC_4560})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS20, L.VVVVVVS31, L.VVVVVVS52, L.VVVVVVS55 ],
                couplings = {(0,3):C.GC_4575,(0,2):C.GC_4910,(0,0):C.GC_4901,(0,1):C.GC_4568})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS16, L.VVVVVVS4, L.VVVVVVS45, L.VVVVVVS50, L.VVVVVVS51 ],
                couplings = {(0,1):C.GC_6051,(0,0):C.GC_4689,(0,4):C.GC_4690,(0,3):C.GC_6050,(0,2):C.GC_4719})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS16, L.VVVVVVS50, L.VVVVVVS51 ],
                couplings = {(0,0):C.GC_4706,(0,2):C.GC_4700,(0,1):C.GC_5164})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS13, L.VVVVVSS260, L.VVVVVSS271, L.VVVVVSS273, L.VVVVVSS34 ],
                couplings = {(0,0):C.GC_1458,(0,4):C.GC_1234,(0,2):C.GC_1455,(0,3):C.GC_1595,(0,1):C.GC_1233})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS260, L.VVVVVSS34 ],
                couplings = {(0,1):C.GC_1288,(0,0):C.GC_1342})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS6 ],
                couplings = {(0,0):C.GC_5724})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS6 ],
                couplings = {(0,0):C.GC_5777})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS32 ],
                couplings = {(0,0):C.GC_5723})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS32 ],
                couplings = {(0,0):C.GC_5776})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS147, L.VVVVVSS246, L.VVVVVSS58 ],
                couplings = {(0,0):C.GC_863,(0,1):C.GC_859,(0,2):C.GC_861})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS246, L.VVVVVSS58 ],
                couplings = {(0,0):C.GC_932,(0,1):C.GC_918})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS12, L.VVVVVVS22, L.VVVVVVS24, L.VVVVVVS47, L.VVVVVVS5, L.VVVVVVS53, L.VVVVVVS56, L.VVVVVVS58 ],
                couplings = {(0,4):C.GC_6312,(0,6):C.GC_4693,(0,2):C.GC_6044,(0,3):C.GC_4721,(0,5):C.GC_5106,(0,0):C.GC_5108,(0,7):C.GC_5163,(0,1):C.GC_4695})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS12, L.VVVVVVS22, L.VVVVVVS53, L.VVVVVVS56 ],
                couplings = {(0,3):C.GC_4707,(0,2):C.GC_5126,(0,0):C.GC_5119,(0,1):C.GC_4702})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS11, L.VVVVVVS17, L.VVVVVVS26, L.VVVVVVS28, L.VVVVVVS35, L.VVVVVVS37, L.VVVVVVS39, L.VVVVVVS7 ],
                couplings = {(0,2):C.GC_4692,(0,6):C.GC_6045,(0,3):C.GC_4720,(0,4):C.GC_5105,(0,5):C.GC_5162,(0,7):C.GC_6311,(0,0):C.GC_5107,(0,1):C.GC_4694})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS11, L.VVVVVVS17, L.VVVVVVS26, L.VVVVVVS35 ],
                couplings = {(0,2):C.GC_4708,(0,3):C.GC_5127,(0,0):C.GC_5118,(0,1):C.GC_4701})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS29, L.VVVVVVS3 ],
                couplings = {(0,2):C.GC_6551,(0,0):C.GC_6549,(0,1):C.GC_6550})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS29 ],
                couplings = {(0,0):C.GC_6587,(0,1):C.GC_6557})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS29, L.VVVVVVS39, L.VVVVVVS40, L.VVVVVVS41, L.VVVVVVS42, L.VVVVVVS54 ],
                couplings = {(0,0):C.GC_5712,(0,4):C.GC_4613,(0,2):C.GC_5714,(0,3):C.GC_4618,(0,5):C.GC_4941,(0,6):C.GC_4614,(0,1):C.GC_5713})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS29, L.VVVVVVS41, L.VVVVVVS54 ],
                couplings = {(0,0):C.GC_5748,(0,2):C.GC_4617,(0,3):C.GC_4616,(0,1):C.GC_5744})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS14, L.VVVVVVS49 ],
                couplings = {(0,0):C.GC_6326,(0,1):C.GC_6325})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS49 ],
                couplings = {(0,0):C.GC_6381})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS146, L.VVVVVSS153 ],
                couplings = {(0,1):C.GC_1252,(0,0):C.GC_1255})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS153 ],
                couplings = {(0,0):C.GC_1343})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS18 ],
                couplings = {(0,0):C.GC_5733})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS18 ],
                couplings = {(0,0):C.GC_5778})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS43 ],
                couplings = {(0,0):C.GC_5734})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS43 ],
                couplings = {(0,0):C.GC_5779})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS21 ],
                couplings = {(0,0):C.GC_5741})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS21 ],
                couplings = {(0,0):C.GC_5780})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS283, L.VVVVVSS57 ],
                couplings = {(0,0):C.GC_1846,(0,1):C.GC_1850})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS283 ],
                couplings = {(0,0):C.GC_2073})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV2, L.VVVVVVV23, L.VVVVVVV29, L.VVVVVVV3, L.VVVVVVV9 ],
                couplings = {(0,4):C.GC_330,(0,0):C.GC_329,(0,3):C.GC_331,(0,2):C.GC_671,(0,1):C.GC_332})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV23, L.VVVVVVV3 ],
                couplings = {(0,1):C.GC_656,(0,0):C.GC_679})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV15, L.VVVVVVV16, L.VVVVVVV20, L.VVVVVVV6, L.VVVVVVV8 ],
                couplings = {(0,3):C.GC_1869,(0,0):C.GC_1871,(0,1):C.GC_2174,(0,4):C.GC_1868,(0,2):C.GC_1870})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV15, L.VVVVVVV20 ],
                couplings = {(0,0):C.GC_993,(0,1):C.GC_2167})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV13, L.VVVVVVV18, L.VVVVVVV24, L.VVVVVVV25, L.VVVVVVV5 ],
                couplings = {(0,0):C.GC_2533,(0,4):C.GC_2532,(0,2):C.GC_2535,(0,3):C.GC_2768,(0,1):C.GC_2534})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV18, L.VVVVVVV24 ],
                couplings = {(0,1):C.GC_1395,(0,0):C.GC_2761})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV1, L.VVVVVVV10, L.VVVVVVV22, L.VVVVVVV28, L.VVVVVVV30 ],
                couplings = {(0,0):C.GC_1464,(0,1):C.GC_1465,(0,3):C.GC_1466,(0,4):C.GC_1673,(0,2):C.GC_1467})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV22, L.VVVVVVV28 ],
                couplings = {(0,1):C.GC_1669,(0,0):C.GC_809})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV11, L.VVVVVVV12, L.VVVVVVV14, L.VVVVVVV17, L.VVVVVVV19 ],
                couplings = {(0,2):C.GC_1941,(0,0):C.GC_1940,(0,1):C.GC_1942,(0,3):C.GC_1943,(0,4):C.GC_2175})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV12, L.VVVVVVV17 ],
                couplings = {(0,0):C.GC_2168,(0,1):C.GC_994})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV21, L.VVVVVVV26, L.VVVVVVV27, L.VVVVVVV4, L.VVVVVVV7 ],
                couplings = {(0,4):C.GC_1529,(0,1):C.GC_1531,(0,2):C.GC_1674,(0,3):C.GC_1528,(0,0):C.GC_1530})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV21, L.VVVVVVV26 ],
                couplings = {(0,1):C.GC_810,(0,0):C.GC_1670})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_441})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_643})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1269})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1385})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1266})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1382})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_884,(0,1):C.GC_1964})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_971,(0,1):C.GC_2113})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_887,(0,1):C.GC_1965})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_974,(0,1):C.GC_2114})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_882,(0,1):C.GC_1963})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_970,(0,1):C.GC_2112})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1269})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1385})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1271})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_1387})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_881,(0,1):C.GC_1962})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_968,(0,1):C.GC_2111})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_881,(0,1):C.GC_1962})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_968,(0,1):C.GC_2111})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_879,(0,1):C.GC_1966})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_973,(0,1):C.GC_2133})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1541,(0,1):C.GC_763})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1631,(0,1):C.GC_798})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1539,(0,1):C.GC_760})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1629,(0,1):C.GC_796})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1540,(0,1):C.GC_761})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1630,(0,1):C.GC_797})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1538,(0,1):C.GC_758})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1628,(0,1):C.GC_795})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1536,(0,1):C.GC_762})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1667,(0,1):C.GC_789})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1535,(0,1):C.GC_759})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1666,(0,1):C.GC_788})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_762,(0,1):C.GC_1536})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_789,(0,1):C.GC_1667})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_765,(0,1):C.GC_1537})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_790,(0,1):C.GC_1668})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_699,(0,1):C.GC_1399})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_720,(0,1):C.GC_1417})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_699,(0,1):C.GC_1399})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_720,(0,1):C.GC_1417})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_884,(0,1):C.GC_1964})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_971,(0,1):C.GC_2113})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_880,(0,1):C.GC_1961})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_966,(0,1):C.GC_2110})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_882,(0,1):C.GC_1963})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_970,(0,1):C.GC_2112})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_763,(0,1):C.GC_1541})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_798,(0,1):C.GC_1631})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_764,(0,1):C.GC_1542})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_799,(0,1):C.GC_1632})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_761,(0,1):C.GC_1540})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_797,(0,1):C.GC_1630})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_766,(0,1):C.GC_1543})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_800,(0,1):C.GC_1633})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_701,(0,1):C.GC_1402})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_723,(0,1):C.GC_1415})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_700,(0,1):C.GC_1401})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_722,(0,1):C.GC_1414})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_698,(0,1):C.GC_1400})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_721,(0,1):C.GC_1413})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_701,(0,1):C.GC_1402})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_723,(0,1):C.GC_1415})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_3625})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_3801})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_448,(0,1):C.GC_913,(0,2):C.GC_1986})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_650,(0,1):C.GC_987,(0,2):C.GC_2144})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_449,(0,1):C.GC_912,(0,2):C.GC_1985})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_651,(0,1):C.GC_986,(0,2):C.GC_2143})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_769,(0,2):C.GC_1276,(0,0):C.GC_2552})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_803,(0,2):C.GC_1390,(0,0):C.GC_2734})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_770,(0,2):C.GC_1275,(0,0):C.GC_2551})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_801,(0,2):C.GC_1388,(0,0):C.GC_2733})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_768,(0,2):C.GC_1278,(0,0):C.GC_2553})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_804,(0,2):C.GC_1392,(0,0):C.GC_2735})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_448,(0,1):C.GC_913,(0,2):C.GC_1986})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_650,(0,1):C.GC_987,(0,2):C.GC_2144})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_447,(0,1):C.GC_914,(0,2):C.GC_1987})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS10, L.VVVVSSSS14, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_649,(0,1):C.GC_988,(0,2):C.GC_2145})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1281,(0,1):C.GC_1277})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS11 ],
                couplings = {(0,0):C.GC_1353,(0,1):C.GC_1391})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS12, L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_771,(0,2):C.GC_1547,(0,1):C.GC_1280})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS12, L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_802,(0,2):C.GC_1634,(0,1):C.GC_1389})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS12, L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_771,(0,2):C.GC_1547,(0,1):C.GC_1280})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS12, L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_802,(0,2):C.GC_1634,(0,1):C.GC_1389})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_707,(0,0):C.GC_896,(0,1):C.GC_1974})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_730,(0,0):C.GC_980,(0,1):C.GC_2139})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_706,(0,0):C.GC_895,(0,1):C.GC_1973})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_729,(0,0):C.GC_979,(0,1):C.GC_2138})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_710,(0,0):C.GC_899,(0,1):C.GC_1975})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_727,(0,0):C.GC_983,(0,1):C.GC_2140})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_704,(0,0):C.GC_900,(0,1):C.GC_1976})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_733,(0,0):C.GC_984,(0,1):C.GC_2141})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_705,(0,0):C.GC_894,(0,1):C.GC_1972})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_728,(0,0):C.GC_978,(0,1):C.GC_2137})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_712,(0,0):C.GC_901,(0,1):C.GC_1977})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,2):C.GC_725,(0,0):C.GC_985,(0,1):C.GC_2142})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_769,(0,2):C.GC_1276,(0,0):C.GC_2552})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_803,(0,2):C.GC_1390,(0,0):C.GC_2734})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_767,(0,2):C.GC_1279,(0,0):C.GC_2554})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_805,(0,2):C.GC_1393,(0,0):C.GC_2736})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_768,(0,2):C.GC_1278,(0,0):C.GC_2553})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_804,(0,2):C.GC_1392,(0,0):C.GC_2735})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_709,(0,2):C.GC_898,(0,0):C.GC_1974})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_732,(0,2):C.GC_982,(0,0):C.GC_2139})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_708,(0,2):C.GC_897,(0,0):C.GC_1973})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_731,(0,2):C.GC_981,(0,0):C.GC_2138})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_711,(0,2):C.GC_893,(0,0):C.GC_1971})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_726,(0,2):C.GC_977,(0,0):C.GC_2136})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_703,(0,2):C.GC_892,(0,0):C.GC_1970})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_734,(0,2):C.GC_976,(0,0):C.GC_2135})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_706,(0,2):C.GC_895,(0,0):C.GC_1972})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_729,(0,2):C.GC_979,(0,0):C.GC_2137})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_713,(0,2):C.GC_891,(0,0):C.GC_1969})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS11, L.VVVVSSSS7, L.VVVVSSSS8 ],
                couplings = {(0,1):C.GC_724,(0,2):C.GC_975,(0,0):C.GC_2134})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4139})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4266})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_773,(0,0):C.GC_1268,(0,1):C.GC_3610,(0,4):C.GC_2965,(0,3):C.GC_1558})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_807,(0,0):C.GC_1384,(0,1):C.GC_3797,(0,4):C.GC_3028,(0,3):C.GC_1648})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_772,(0,0):C.GC_1270,(0,1):C.GC_3605,(0,4):C.GC_2964,(0,3):C.GC_1557})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_806,(0,0):C.GC_1386,(0,1):C.GC_3792,(0,4):C.GC_3027,(0,3):C.GC_1647})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_444,(0,1):C.GC_392,(0,2):C.GC_715})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_646,(0,1):C.GC_612,(0,2):C.GC_737})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_445,(0,1):C.GC_393,(0,2):C.GC_714})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_648,(0,1):C.GC_613,(0,2):C.GC_739})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_443,(0,1):C.GC_391,(0,2):C.GC_716})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_645,(0,1):C.GC_611,(0,2):C.GC_736})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_773,(0,0):C.GC_1268,(0,1):C.GC_3610,(0,4):C.GC_2965,(0,3):C.GC_1558})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_807,(0,0):C.GC_1384,(0,1):C.GC_3797,(0,4):C.GC_3028,(0,3):C.GC_1648})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_774,(0,0):C.GC_1267,(0,1):C.GC_3613,(0,4):C.GC_2966,(0,3):C.GC_1559})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS13, L.VVVVSSSS2, L.VVVVSSSS3, L.VVVVSSSS9 ],
                couplings = {(0,2):C.GC_808,(0,0):C.GC_1383,(0,1):C.GC_3800,(0,4):C.GC_3029,(0,3):C.GC_1649})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS3, L.VVVVSSSS6 ],
                couplings = {(0,0):C.GC_446,(0,2):C.GC_1405,(0,1):C.GC_718})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS3, L.VVVVSSSS6 ],
                couplings = {(0,0):C.GC_647,(0,2):C.GC_1416,(0,1):C.GC_738})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS3, L.VVVVSSSS6 ],
                couplings = {(0,0):C.GC_446,(0,2):C.GC_1405,(0,1):C.GC_718})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12, L.VVVVSSSS3, L.VVVVSSSS6 ],
                couplings = {(0,0):C.GC_647,(0,2):C.GC_1416,(0,1):C.GC_738})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_444,(0,1):C.GC_392,(0,2):C.GC_715})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_646,(0,1):C.GC_612,(0,2):C.GC_737})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_442,(0,1):C.GC_390,(0,2):C.GC_717})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_644,(0,1):C.GC_610,(0,2):C.GC_735})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_443,(0,1):C.GC_391,(0,2):C.GC_716})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS14, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_645,(0,1):C.GC_611,(0,2):C.GC_736})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_4137,(0,1):C.GC_4138})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_4265,(0,1):C.GC_4248})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_4137,(0,1):C.GC_4138})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_4265,(0,1):C.GC_4248})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3609,(0,1):C.GC_3617})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3796,(0,1):C.GC_3759})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3607,(0,1):C.GC_3615})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3794,(0,1):C.GC_3757})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3608,(0,1):C.GC_3616})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3795,(0,1):C.GC_3758})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3606,(0,1):C.GC_3614})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3793,(0,1):C.GC_3756})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3609,(0,1):C.GC_3617})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3796,(0,1):C.GC_3759})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3611,(0,1):C.GC_3618})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3798,(0,1):C.GC_3760})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3608,(0,1):C.GC_3616})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3795,(0,1):C.GC_3758})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3612,(0,1):C.GC_3619})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_3799,(0,1):C.GC_3761})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_878,(0,1):C.GC_886})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_972,(0,1):C.GC_953})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_877,(0,1):C.GC_885})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_969,(0,1):C.GC_952})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_876,(0,1):C.GC_883})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_967,(0,1):C.GC_951})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_878,(0,1):C.GC_886})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS3 ],
                couplings = {(0,0):C.GC_972,(0,1):C.GC_953})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4364})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4391})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4365})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4392})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4364})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4391})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4129})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4261})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4128})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4260})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4130})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4262})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4131})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4263})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4127})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4259})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4132})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4264})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4129})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4261})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4128})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4260})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4126})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4258})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4125})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4257})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4127})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4259})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4124})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4256})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4445})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4461})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4442})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4458})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4444})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4460})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4443})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4459})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4442})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4458})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4445})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS12 ],
                couplings = {(0,0):C.GC_4461})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS23 ],
                couplings = {(0,0):C.GC_440})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS23 ],
                couplings = {(0,0):C.GC_575})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS48 ],
                couplings = {(0,0):C.GC_1260})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS48 ],
                couplings = {(0,0):C.GC_1345})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS48 ],
                couplings = {(0,0):C.GC_1261})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS48 ],
                couplings = {(0,0):C.GC_1346})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1260})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1345})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1259})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1344})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS33, L.VVVVVVSS37, L.VVVVVVSS42 ],
                couplings = {(0,2):C.GC_1956,(0,3):C.GC_1959,(0,1):C.GC_2080,(0,0):C.GC_1958})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS37 ],
                couplings = {(0,1):C.GC_2017,(0,0):C.GC_2002})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS33, L.VVVVVVSS37, L.VVVVVVSS42 ],
                couplings = {(0,2):C.GC_1956,(0,3):C.GC_1959,(0,1):C.GC_2080,(0,0):C.GC_1958})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS37 ],
                couplings = {(0,1):C.GC_2017,(0,0):C.GC_2002})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS42, L.VVVVVVSS44, L.VVVVVVSS55, L.VVVVVVSS76 ],
                couplings = {(0,2):C.GC_1957,(0,0):C.GC_1960,(0,1):C.GC_2083,(0,3):C.GC_1958})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS55, L.VVVVVVSS76 ],
                couplings = {(0,0):C.GC_2018,(0,1):C.GC_2002})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS26 ],
                couplings = {(0,0):C.GC_756})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS26 ],
                couplings = {(0,0):C.GC_785})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS26 ],
                couplings = {(0,0):C.GC_755})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS26 ],
                couplings = {(0,0):C.GC_784})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17 ],
                couplings = {(0,0):C.GC_756})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17 ],
                couplings = {(0,0):C.GC_785})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17 ],
                couplings = {(0,0):C.GC_757})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17 ],
                couplings = {(0,0):C.GC_786})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_697})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_719})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_697})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_719})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_697})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS52 ],
                couplings = {(0,0):C.GC_719})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS1, L.VVVVVVSS72, L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_3622,(0,1):C.GC_1282,(0,2):C.GC_3620})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS72, L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_1347,(0,1):C.GC_3737})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS2, L.VVVVVVSS21, L.VVVVVVSS28, L.VVVVVVSS30, L.VVVVVVSS39, L.VVVVVVSS41, L.VVVVVVSS42 ],
                couplings = {(0,1):C.GC_911,(0,5):C.GC_397,(0,7):C.GC_906,(0,6):C.GC_572,(0,3):C.GC_1979,(0,4):C.GC_2086,(0,2):C.GC_1983,(0,0):C.GC_399})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS21, L.VVVVVVSS28, L.VVVVVVSS39 ],
                couplings = {(0,3):C.GC_491,(0,2):C.GC_2020,(0,1):C.GC_2004,(0,0):C.GC_470})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS2, L.VVVVVVSS21, L.VVVVVVSS28, L.VVVVVVSS30, L.VVVVVVSS39, L.VVVVVVSS41, L.VVVVVVSS42 ],
                couplings = {(0,1):C.GC_909,(0,5):C.GC_394,(0,7):C.GC_908,(0,6):C.GC_569,(0,3):C.GC_1978,(0,4):C.GC_2084,(0,2):C.GC_1982,(0,0):C.GC_398})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS21, L.VVVVVVSS28, L.VVVVVVSS39 ],
                couplings = {(0,3):C.GC_493,(0,2):C.GC_2022,(0,1):C.GC_2003,(0,0):C.GC_469})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS22, L.VVVVVVSS3, L.VVVVVVSS34, L.VVVVVVSS36, L.VVVVVVSS54, L.VVVVVVSS63, L.VVVVVVSS71, L.VVVVVVSS74 ],
                couplings = {(0,1):C.GC_911,(0,6):C.GC_396,(0,3):C.GC_905,(0,4):C.GC_571,(0,5):C.GC_1980,(0,0):C.GC_1983,(0,7):C.GC_2085,(0,2):C.GC_399})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS22, L.VVVVVVSS34, L.VVVVVVSS63, L.VVVVVVSS71 ],
                couplings = {(0,3):C.GC_490,(0,2):C.GC_2021,(0,0):C.GC_2004,(0,1):C.GC_470})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS22, L.VVVVVVSS3, L.VVVVVVSS34, L.VVVVVVSS36, L.VVVVVVSS54, L.VVVVVVSS63, L.VVVVVVSS71, L.VVVVVVSS74 ],
                couplings = {(0,1):C.GC_910,(0,6):C.GC_395,(0,3):C.GC_907,(0,4):C.GC_570,(0,5):C.GC_1981,(0,0):C.GC_1984,(0,7):C.GC_2087,(0,2):C.GC_400})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS22, L.VVVVVVSS34, L.VVVVVVSS63, L.VVVVVVSS71 ],
                couplings = {(0,3):C.GC_492,(0,2):C.GC_2019,(0,0):C.GC_2005,(0,1):C.GC_471})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18, L.VVVVVVSS5, L.VVVVVVSS50, L.VVVVVVSS57, L.VVVVVVSS58 ],
                couplings = {(0,1):C.GC_1274,(0,0):C.GC_1544,(0,4):C.GC_1545,(0,3):C.GC_1273,(0,2):C.GC_1601})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18, L.VVVVVVSS57, L.VVVVVVSS58 ],
                couplings = {(0,0):C.GC_1578,(0,2):C.GC_1567,(0,1):C.GC_2688})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18, L.VVVVVVSS5, L.VVVVVVSS50, L.VVVVVVSS57, L.VVVVVVSS58 ],
                couplings = {(0,1):C.GC_1274,(0,0):C.GC_1544,(0,4):C.GC_1545,(0,3):C.GC_1273,(0,2):C.GC_1601})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18, L.VVVVVVSS57, L.VVVVVVSS58 ],
                couplings = {(0,0):C.GC_1578,(0,2):C.GC_1567,(0,1):C.GC_2688})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS49, L.VVVVVVSS5, L.VVVVVVSS51, L.VVVVVVSS57, L.VVVVVVSS59, L.VVVVVVSS62, L.VVVVVVSS67, L.VVVVVVSS7 ],
                couplings = {(0,1):C.GC_1274,(0,5):C.GC_1544,(0,4):C.GC_1546,(0,3):C.GC_1272,(0,2):C.GC_1602,(0,7):C.GC_2550,(0,0):C.GC_2689,(0,6):C.GC_2549})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS59, L.VVVVVVSS62, L.VVVVVVSS67, L.VVVVVVSS7 ],
                couplings = {(0,1):C.GC_1578,(0,0):C.GC_1568,(0,3):C.GC_2581,(0,2):C.GC_2607})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_889})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_937})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_890})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS8 ],
                couplings = {(0,0):C.GC_938})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS35 ],
                couplings = {(0,0):C.GC_889})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS35 ],
                couplings = {(0,0):C.GC_937})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS35 ],
                couplings = {(0,0):C.GC_888})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS35 ],
                couplings = {(0,0):C.GC_936})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS4, L.VVVVVVSS60, L.VVVVVVSS65, L.VVVVVVSS68, L.VVVVVVSS69 ],
                couplings = {(0,2):C.GC_4136,(0,6):C.GC_386,(0,3):C.GC_387,(0,4):C.GC_1988,(0,5):C.GC_1989,(0,0):C.GC_3144,(0,1):C.GC_3145})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS60, L.VVVVVVSS65, L.VVVVVVSS68, L.VVVVVVSS69 ],
                couplings = {(0,5):C.GC_576,(0,2):C.GC_468,(0,3):C.GC_944,(0,4):C.GC_2006,(0,0):C.GC_4239,(0,1):C.GC_3151})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS25, L.VVVVVVSS27, L.VVVVVVSS53, L.VVVVVVSS6, L.VVVVVVSS64, L.VVVVVVSS73, L.VVVVVVSS75 ],
                couplings = {(0,4):C.GC_3602,(0,6):C.GC_1552,(0,2):C.GC_1262,(0,3):C.GC_1605,(0,5):C.GC_2544,(0,0):C.GC_2547,(0,7):C.GC_2685,(0,1):C.GC_1555})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS25, L.VVVVVVSS64, L.VVVVVVSS73 ],
                couplings = {(0,3):C.GC_1579,(0,2):C.GC_2605,(0,0):C.GC_2579,(0,1):C.GC_1570})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS25, L.VVVVVVSS27, L.VVVVVVSS53, L.VVVVVVSS6, L.VVVVVVSS64, L.VVVVVVSS73, L.VVVVVVSS75 ],
                couplings = {(0,4):C.GC_3604,(0,6):C.GC_1551,(0,2):C.GC_1264,(0,3):C.GC_1604,(0,5):C.GC_2545,(0,0):C.GC_2548,(0,7):C.GC_2687,(0,1):C.GC_1556})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS25, L.VVVVVVSS64, L.VVVVVVSS73 ],
                couplings = {(0,3):C.GC_1581,(0,2):C.GC_2603,(0,0):C.GC_2580,(0,1):C.GC_1571})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS19, L.VVVVVVSS29, L.VVVVVVSS31, L.VVVVVVSS38, L.VVVVVVSS40, L.VVVVVVSS42, L.VVVVVVSS9 ],
                couplings = {(0,2):C.GC_1553,(0,6):C.GC_1263,(0,3):C.GC_1606,(0,4):C.GC_2543,(0,5):C.GC_2686,(0,7):C.GC_3602,(0,0):C.GC_2547,(0,1):C.GC_1555})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS19, L.VVVVVVSS29, L.VVVVVVSS38 ],
                couplings = {(0,2):C.GC_1580,(0,3):C.GC_2604,(0,0):C.GC_2579,(0,1):C.GC_1570})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS19, L.VVVVVVSS29, L.VVVVVVSS31, L.VVVVVVSS38, L.VVVVVVSS40, L.VVVVVVSS42, L.VVVVVVSS9 ],
                couplings = {(0,2):C.GC_1550,(0,6):C.GC_1265,(0,3):C.GC_1603,(0,4):C.GC_2542,(0,5):C.GC_2684,(0,7):C.GC_3603,(0,0):C.GC_2546,(0,1):C.GC_1554})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS19, L.VVVVVVSS29, L.VVVVVVSS38 ],
                couplings = {(0,2):C.GC_1582,(0,3):C.GC_2606,(0,0):C.GC_2578,(0,1):C.GC_1569})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS4 ],
                couplings = {(0,2):C.GC_4135,(0,0):C.GC_4133,(0,1):C.GC_4134})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32 ],
                couplings = {(0,0):C.GC_4240,(0,1):C.GC_4148})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS4 ],
                couplings = {(0,2):C.GC_4135,(0,0):C.GC_4133,(0,1):C.GC_4134})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32 ],
                couplings = {(0,0):C.GC_4240,(0,1):C.GC_4148})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS42, L.VVVVVVSS43, L.VVVVVVSS45, L.VVVVVVSS46, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_870,(0,4):C.GC_1403,(0,2):C.GC_875,(0,3):C.GC_1412,(0,5):C.GC_2081,(0,6):C.GC_1404,(0,1):C.GC_873})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS45, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_923,(0,2):C.GC_1411,(0,3):C.GC_1410,(0,1):C.GC_920})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS42, L.VVVVVVSS43, L.VVVVVVSS45, L.VVVVVVSS46, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_871,(0,4):C.GC_1403,(0,2):C.GC_874,(0,3):C.GC_1412,(0,5):C.GC_2082,(0,6):C.GC_1404,(0,1):C.GC_872})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS45, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_922,(0,2):C.GC_1411,(0,3):C.GC_1410,(0,1):C.GC_919})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS42, L.VVVVVVSS43, L.VVVVVVSS45, L.VVVVVVSS46, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_870,(0,4):C.GC_1403,(0,2):C.GC_875,(0,3):C.GC_1412,(0,5):C.GC_2081,(0,6):C.GC_1404,(0,1):C.GC_873})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15, L.VVVVVVSS32, L.VVVVVVSS45, L.VVVVVVSS70 ],
                couplings = {(0,0):C.GC_923,(0,2):C.GC_1411,(0,3):C.GC_1410,(0,1):C.GC_920})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_3623,(0,1):C.GC_3621})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_3738})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS56, L.VVVVVVSS61, L.VVVVVVSS66 ],
                couplings = {(0,2):C.GC_775,(0,3):C.GC_1283,(0,0):C.GC_3624,(0,1):C.GC_3620})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS56, L.VVVVVVSS61, L.VVVVVVSS66 ],
                couplings = {(0,1):C.GC_787,(0,2):C.GC_1348,(0,0):C.GC_3737})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_3623,(0,1):C.GC_3621})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_3738})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20 ],
                couplings = {(0,0):C.GC_903})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20 ],
                couplings = {(0,0):C.GC_940})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20 ],
                couplings = {(0,0):C.GC_902})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20 ],
                couplings = {(0,0):C.GC_939})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS47 ],
                couplings = {(0,0):C.GC_903})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS47 ],
                couplings = {(0,0):C.GC_940})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS47 ],
                couplings = {(0,0):C.GC_904})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS47 ],
                couplings = {(0,0):C.GC_941})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_915})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_942})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_916})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_943})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_915})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS24 ],
                couplings = {(0,0):C.GC_942})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV17, L.VVVVVVVV2, L.VVVVVVVV24 ],
                couplings = {(0,1):C.GC_388,(0,2):C.GC_389,(0,0):C.GC_672})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV2, L.VVVVVVVV24 ],
                couplings = {(0,0):C.GC_657,(0,1):C.GC_680})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV16, L.VVVVVVVV22, L.VVVVVVVV4 ],
                couplings = {(0,2):C.GC_1968,(0,0):C.GC_2176,(0,1):C.GC_1967})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV22, L.VVVVVVVV4 ],
                couplings = {(0,1):C.GC_995,(0,0):C.GC_2169})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV21 ],
                couplings = {(0,0):C.GC_702})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV21 ],
                couplings = {(0,0):C.GC_740})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV12, L.VVVVVVVV14, L.VVVVVVVV7 ],
                couplings = {(0,2):C.GC_2556,(0,1):C.GC_2769,(0,0):C.GC_2555})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV12, L.VVVVVVVV7 ],
                couplings = {(0,1):C.GC_1396,(0,0):C.GC_2762})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV10, L.VVVVVVVV18, L.VVVVVVVV6 ],
                couplings = {(0,2):C.GC_1548,(0,0):C.GC_1675,(0,1):C.GC_1549})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV18, L.VVVVVVVV6 ],
                couplings = {(0,1):C.GC_1671,(0,0):C.GC_811})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV15, L.VVVVVVVV3, L.VVVVVVVV9 ],
                couplings = {(0,1):C.GC_1990,(0,0):C.GC_1991,(0,2):C.GC_2177})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV15, L.VVVVVVVV3 ],
                couplings = {(0,1):C.GC_2170,(0,0):C.GC_996})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV1, L.VVVVVVVV19, L.VVVVVVVV25 ],
                couplings = {(0,0):C.GC_1407,(0,1):C.GC_1420,(0,2):C.GC_1406})

V_1572 = Vertex(name = 'V_1572',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV1, L.VVVVVVVV25 ],
                couplings = {(0,0):C.GC_741,(0,1):C.GC_1418})

V_1573 = Vertex(name = 'V_1573',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV11, L.VVVVVVVV13, L.VVVVVVVV8 ],
                couplings = {(0,2):C.GC_1561,(0,1):C.GC_1676,(0,0):C.GC_1560})

V_1574 = Vertex(name = 'V_1574',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV11, L.VVVVVVVV8 ],
                couplings = {(0,1):C.GC_812,(0,0):C.GC_1672})

V_1575 = Vertex(name = 'V_1575',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV20, L.VVVVVVVV23, L.VVVVVVVV5 ],
                couplings = {(0,2):C.GC_1408,(0,1):C.GC_1409,(0,0):C.GC_1421})

V_1576 = Vertex(name = 'V_1576',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV23, L.VVVVVVVV5 ],
                couplings = {(0,1):C.GC_1419,(0,0):C.GC_742})

