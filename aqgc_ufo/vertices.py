from __future__ import absolute_import
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (November 18, 2022)
# Date: Thu 11 Apr 2024 09:37:30


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS6 ],
             couplings = {(0,0):C.GC_246,(0,1):C.GC_15})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS6 ],
             couplings = {(0,0):C.GC_223})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_1028})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_243})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_243})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV37, L.VVVV85, L.VVVV86 ],
             couplings = {(1,1):C.GC_245,(0,0):C.GC_245,(2,2):C.GC_245})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2044})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ta__plus__, P.ta__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2046})

V_9 = Vertex(name = 'V_9',
             particles = [ P.t__tilde__, P.t, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2045})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_62})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS12, L.VVSS16, L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4, L.VVSS7 ],
              couplings = {(0,0):C.GC_9,(0,5):C.GC_1849,(0,1):C.GC_257,(0,3):C.GC_2,(0,6):C.GC_1,(0,4):C.GC_5,(0,2):C.GC_1518})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4 ],
              couplings = {(0,3):C.GC_1880,(0,1):C.GC_203,(0,2):C.GC_169,(0,0):C.GC_1560})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1029})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV113, L.VVVV115, L.VVVV13, L.VVVV16, L.VVVV2, L.VVVV28, L.VVVV29, L.VVVV34, L.VVVV36, L.VVVV39, L.VVVV41, L.VVVV42, L.VVVV47, L.VVVV5, L.VVVV62, L.VVVV63, L.VVVV84, L.VVVV89 ],
              couplings = {(0,6):C.GC_1563,(0,5):C.GC_1565,(0,3):C.GC_52,(0,15):C.GC_573,(0,4):C.GC_55,(0,13):C.GC_569,(0,7):C.GC_53,(0,8):C.GC_575,(0,2):C.GC_756,(0,11):C.GC_757,(0,10):C.GC_811,(0,0):C.GC_809,(0,14):C.GC_51,(0,1):C.GC_755,(0,9):C.GC_1893,(0,16):C.GC_156,(0,12):C.GC_1891,(0,17):C.GC_1892})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV115, L.VVVV39, L.VVVV42, L.VVVV89 ],
              couplings = {(0,2):C.GC_807,(0,0):C.GC_805,(0,1):C.GC_1912,(0,3):C.GC_1911})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_297})

V_17 = Vertex(name = 'V_17',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV100, L.VVVV11, L.VVVV111, L.VVVV113, L.VVVV118, L.VVVV31, L.VVVV36, L.VVVV38, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV6, L.VVVV64, L.VVVV77, L.VVVV80, L.VVVV84, L.VVVV98, L.VVVV99 ],
              couplings = {(0,14):C.GC_1513,(0,13):C.GC_1516,(0,12):C.GC_19,(0,11):C.GC_21,(0,1):C.GC_17,(0,6):C.GC_18,(0,9):C.GC_20,(0,4):C.GC_22,(0,2):C.GC_233,(0,3):C.GC_236,(0,17):C.GC_1512,(0,0):C.GC_1515,(0,16):C.GC_1553,(0,5):C.GC_1511,(0,8):C.GC_1514,(0,15):C.GC_258,(0,7):C.GC_2036,(0,10):C.GC_1641})

V_18 = Vertex(name = 'V_18',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV118, L.VVVV38, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV99 ],
              couplings = {(0,3):C.GC_227,(0,0):C.GC_230,(0,5):C.GC_1546,(0,2):C.GC_1543,(0,1):C.GC_2037,(0,4):C.GC_1642})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV110, L.VVVV112, L.VVVV116, L.VVVV17, L.VVVV19, L.VVVV20, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV44, L.VVVV45, L.VVVV54, L.VVVV55, L.VVVV59, L.VVVV65, L.VVVV70, L.VVVV71, L.VVVV8, L.VVVV87, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
              couplings = {(0,19):C.GC_1445,(0,18):C.GC_1446,(0,5):C.GC_1521,(0,4):C.GC_1522,(0,14):C.GC_1922,(0,15):C.GC_1924,(0,17):C.GC_463,(0,0):C.GC_654,(0,8):C.GC_458,(0,9):C.GC_461,(0,16):C.GC_460,(0,22):C.GC_457,(0,20):C.GC_462,(0,6):C.GC_459,(0,11):C.GC_653,(0,1):C.GC_732,(0,3):C.GC_655,(0,2):C.GC_726,(0,29):C.GC_1855,(0,30):C.GC_1447,(0,28):C.GC_1523,(0,25):C.GC_1923,(0,27):C.GC_1587,(0,26):C.GC_1895,(0,12):C.GC_1519,(0,7):C.GC_1894,(0,13):C.GC_1443,(0,23):C.GC_1444,(0,24):C.GC_1520,(0,10):C.GC_1896,(0,21):C.GC_374})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV116, L.VVVV26, L.VVVV27, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV95, L.VVVV97 ],
              couplings = {(0,2):C.GC_728,(0,0):C.GC_730,(0,8):C.GC_1456,(0,7):C.GC_1551,(0,5):C.GC_1615,(0,6):C.GC_1910,(0,3):C.GC_1455,(0,4):C.GC_1549,(0,1):C.GC_1909})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS14, L.VVSS16, L.VVSS17, L.VVSS19, L.VVSS25, L.VVSS26, L.VVSS7 ],
              couplings = {(0,0):C.GC_455,(0,3):C.GC_1948,(0,1):C.GC_786,(0,4):C.GC_735,(0,6):C.GC_737,(0,5):C.GC_738,(0,2):C.GC_1950})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS19, L.VVSS25, L.VVSS26 ],
              couplings = {(0,1):C.GC_1962,(0,2):C.GC_794,(0,3):C.GC_790,(0,0):C.GC_1966})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1770})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV113, L.VVVV115, L.VVVV13, L.VVVV15, L.VVVV16, L.VVVV30, L.VVVV32, L.VVVV33, L.VVVV35, L.VVVV36, L.VVVV38, L.VVVV39, L.VVVV4, L.VVVV40, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV47, L.VVVV48, L.VVVV5, L.VVVV56, L.VVVV57, L.VVVV62, L.VVVV63, L.VVVV75, L.VVVV76, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV89, L.VVVV99 ],
              couplings = {(0,35):C.GC_1448,(0,32):C.GC_1527,(0,13):C.GC_1620,(0,36):C.GC_1856,(0,38):C.GC_1564,(0,34):C.GC_1566,(0,37):C.GC_1601,(0,33):C.GC_1602,(0,31):C.GC_54,(0,12):C.GC_570,(0,27):C.GC_50,(0,17):C.GC_56,(0,20):C.GC_574,(0,16):C.GC_572,(0,10):C.GC_753,(0,23):C.GC_754,(0,22):C.GC_813,(0,8):C.GC_816,(0,30):C.GC_571,(0,9):C.GC_752,(0,19):C.GC_1945,(0,3):C.GC_1457,(0,29):C.GC_1525,(0,1):C.GC_1554,(0,0):C.GC_1857,(0,4):C.GC_1921,(0,2):C.GC_1567,(0,41):C.GC_1603,(0,11):C.GC_1441,(0,26):C.GC_1524,(0,15):C.GC_1561,(0,5):C.GC_1442,(0,7):C.GC_1526,(0,6):C.GC_1562,(0,14):C.GC_1599,(0,21):C.GC_1600,(0,28):C.GC_1440,(0,39):C.GC_259,(0,18):C.GC_2038,(0,25):C.GC_1944,(0,40):C.GC_1946,(0,24):C.GC_2039})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV102, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV115, L.VVVV38, L.VVVV39, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV56, L.VVVV57, L.VVVV89, L.VVVV99 ],
              couplings = {(0,8):C.GC_815,(0,4):C.GC_814,(0,6):C.GC_1960,(0,11):C.GC_1547,(0,0):C.GC_1585,(0,13):C.GC_1613,(0,1):C.GC_1453,(0,3):C.GC_1544,(0,2):C.GC_1583,(0,7):C.GC_1611,(0,10):C.GC_1454,(0,5):C.GC_2041,(0,12):C.GC_1958,(0,9):C.GC_2040})

V_26 = Vertex(name = 'V_26',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_61})

V_27 = Vertex(name = 'V_27',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_61})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_61})

V_29 = Vertex(name = 'V_29',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_60})

V_30 = Vertex(name = 'V_30',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_60})

V_31 = Vertex(name = 'V_31',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_60})

V_32 = Vertex(name = 'V_32',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_59})

V_33 = Vertex(name = 'V_33',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_59})

V_34 = Vertex(name = 'V_34',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_59})

V_35 = Vertex(name = 'V_35',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_36 = Vertex(name = 'V_36',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_37 = Vertex(name = 'V_37',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_38 = Vertex(name = 'V_38',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_39 = Vertex(name = 'V_39',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_40 = Vertex(name = 'V_40',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_244})

V_41 = Vertex(name = 'V_41',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_42 = Vertex(name = 'V_42',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_43 = Vertex(name = 'V_43',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_44 = Vertex(name = 'V_44',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_45 = Vertex(name = 'V_45',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_46 = Vertex(name = 'V_46',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_47 = Vertex(name = 'V_47',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_48 = Vertex(name = 'V_48',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_49 = Vertex(name = 'V_49',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_50 = Vertex(name = 'V_50',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_51 = Vertex(name = 'V_51',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_52 = Vertex(name = 'V_52',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_260})

V_53 = Vertex(name = 'V_53',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_296,(0,1):C.GC_498})

V_54 = Vertex(name = 'V_54',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_296,(0,1):C.GC_498})

V_55 = Vertex(name = 'V_55',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_296,(0,1):C.GC_498})

V_56 = Vertex(name = 'V_56',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_498})

V_57 = Vertex(name = 'V_57',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_498})

V_58 = Vertex(name = 'V_58',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_498})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_678})

V_60 = Vertex(name = 'V_60',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_678})

V_61 = Vertex(name = 'V_61',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_678})

V_62 = Vertex(name = 'V_62',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_499})

V_63 = Vertex(name = 'V_63',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_499})

V_64 = Vertex(name = 'V_64',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_295,(0,1):C.GC_499})

V_65 = Vertex(name = 'V_65',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS6 ],
              couplings = {(0,0):C.GC_15})

V_66 = Vertex(name = 'V_66',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS6 ],
              couplings = {(0,0):C.GC_223})

V_67 = Vertex(name = 'V_67',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_10,(0,0):C.GC_16})

V_68 = Vertex(name = 'V_68',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_221,(0,0):C.GC_218})

V_69 = Vertex(name = 'V_69',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_14,(0,0):C.GC_12})

V_70 = Vertex(name = 'V_70',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_222,(0,0):C.GC_216})

V_71 = Vertex(name = 'V_71',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS4 ],
              couplings = {(0,0):C.GC_13})

V_72 = Vertex(name = 'V_72',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS4 ],
              couplings = {(0,0):C.GC_220})

V_73 = Vertex(name = 'V_73',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS5 ],
              couplings = {(0,1):C.GC_11,(0,0):C.GC_14})

V_74 = Vertex(name = 'V_74',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS5 ],
              couplings = {(0,1):C.GC_215,(0,0):C.GC_222})

V_75 = Vertex(name = 'V_75',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_10,(0,0):C.GC_16})

V_76 = Vertex(name = 'V_76',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_221,(0,0):C.GC_218})

V_77 = Vertex(name = 'V_77',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1163,(0,1):C.GC_1676})

V_78 = Vertex(name = 'V_78',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1308,(0,1):C.GC_1691})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1677,(0,0):C.GC_1162})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1692,(0,0):C.GC_1305})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_1674})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_1690})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1676,(0,0):C.GC_1163})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1691,(0,0):C.GC_1308})

V_85 = Vertex(name = 'V_85',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS4 ],
              couplings = {(0,1):C.GC_1850,(0,0):C.GC_1517})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS4 ],
              couplings = {(0,1):C.GC_1881,(0,0):C.GC_1557})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1163,(0,1):C.GC_1676})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1308,(0,1):C.GC_1691})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1162,(0,1):C.GC_1677})

V_90 = Vertex(name = 'V_90',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_1305,(0,1):C.GC_1692})

V_91 = Vertex(name = 'V_91',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_1675})

V_92 = Vertex(name = 'V_92',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_1689})

V_93 = Vertex(name = 'V_93',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1676,(0,0):C.GC_1163})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_1691,(0,0):C.GC_1308})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS12, L.VVSS13, L.VVSS2, L.VVSS20, L.VVSS23, L.VVSS24, L.VVSS25, L.VVSS26, L.VVSS7 ],
              couplings = {(0,1):C.GC_3,(0,0):C.GC_8,(0,3):C.GC_1850,(0,2):C.GC_1517,(0,6):C.GC_2,(0,4):C.GC_6,(0,5):C.GC_205,(0,8):C.GC_1,(0,7):C.GC_5})

V_96 = Vertex(name = 'V_96',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS20, L.VVSS25, L.VVSS26 ],
              couplings = {(0,1):C.GC_1881,(0,0):C.GC_1557,(0,2):C.GC_172,(0,3):C.GC_169})

V_97 = Vertex(name = 'V_97',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS12, L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4, L.VVSS7 ],
              couplings = {(0,0):C.GC_9,(0,4):C.GC_1849,(0,2):C.GC_2,(0,5):C.GC_1,(0,3):C.GC_5,(0,1):C.GC_1518})

V_98 = Vertex(name = 'V_98',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4 ],
              couplings = {(0,3):C.GC_1880,(0,1):C.GC_203,(0,2):C.GC_169,(0,0):C.GC_1560})

V_99 = Vertex(name = 'V_99',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS13, L.VVSS23, L.VVSS3 ],
              couplings = {(0,0):C.GC_4,(0,2):C.GC_1848,(0,1):C.GC_7})

V_100 = Vertex(name = 'V_100',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS23, L.VVSS3 ],
               couplings = {(0,1):C.GC_1882,(0,0):C.GC_204})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS27, L.VVVS30, L.VVVS4, L.VVVS43, L.VVVS45, L.VVVS49, L.VVVS70, L.VVVS71 ],
               couplings = {(0,7):C.GC_1156,(0,8):C.GC_1161,(0,3):C.GC_1154,(0,5):C.GC_1155,(0,6):C.GC_1159,(0,2):C.GC_1158,(0,4):C.GC_1295,(0,0):C.GC_1631,(0,1):C.GC_1996})

V_102 = Vertex(name = 'V_102',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS27, L.VVVS30, L.VVVS45 ],
               couplings = {(0,3):C.GC_1267,(0,2):C.GC_1262,(0,0):C.GC_1634,(0,1):C.GC_1999})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS17, L.VVSS4 ],
               couplings = {(0,1):C.GC_1850,(0,0):C.GC_1517})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS17, L.VVSS4 ],
               couplings = {(0,1):C.GC_1881,(0,0):C.GC_1557})

V_105 = Vertex(name = 'V_105',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS39, L.VVVS41, L.VVVS42, L.VVVS74, L.VVVS75 ],
               couplings = {(0,8):C.GC_1157,(0,7):C.GC_1161,(0,5):C.GC_1155,(0,6):C.GC_1160,(0,4):C.GC_1295,(0,0):C.GC_1154,(0,2):C.GC_1158,(0,1):C.GC_1996,(0,3):C.GC_1631})

V_106 = Vertex(name = 'V_106',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS41 ],
               couplings = {(0,3):C.GC_1267,(0,1):C.GC_1262,(0,0):C.GC_1999,(0,2):C.GC_1634})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS8 ],
               couplings = {(0,0):C.GC_1716})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS8 ],
               couplings = {(0,0):C.GC_1756})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,1):C.GC_1712,(0,0):C.GC_1714})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,1):C.GC_1754,(0,0):C.GC_1751})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS5 ],
               couplings = {(0,0):C.GC_1711})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS5 ],
               couplings = {(0,0):C.GC_1753})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS6 ],
               couplings = {(0,1):C.GC_1713,(0,0):C.GC_1715})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS6 ],
               couplings = {(0,1):C.GC_1750,(0,0):C.GC_1755})

V_115 = Vertex(name = 'V_115',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS12, L.VVSS13, L.VVSS21, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS6, L.VVSS8, L.VVSS9 ],
               couplings = {(0,2):C.GC_39,(0,1):C.GC_41,(0,8):C.GC_436,(0,9):C.GC_440,(0,0):C.GC_1854,(0,3):C.GC_1852,(0,4):C.GC_647,(0,5):C.GC_443,(0,7):C.GC_431,(0,6):C.GC_434})

V_116 = Vertex(name = 'V_116',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS21, L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_1877,(0,1):C.GC_1884,(0,2):C.GC_207,(0,3):C.GC_541,(0,4):C.GC_535})

V_117 = Vertex(name = 'V_117',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS13, L.VVSS18, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS6, L.VVSS8, L.VVSS9 ],
               couplings = {(0,1):C.GC_38,(0,0):C.GC_42,(0,7):C.GC_437,(0,8):C.GC_439,(0,2):C.GC_1851,(0,3):C.GC_645,(0,4):C.GC_444,(0,6):C.GC_430,(0,5):C.GC_433})

V_118 = Vertex(name = 'V_118',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS18, L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_1885,(0,1):C.GC_208,(0,2):C.GC_542,(0,3):C.GC_534})

V_119 = Vertex(name = 'V_119',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS12, L.VVSS13, L.VVSS21, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS6, L.VVSS8, L.VVSS9 ],
               couplings = {(0,2):C.GC_39,(0,1):C.GC_43,(0,8):C.GC_438,(0,9):C.GC_440,(0,0):C.GC_1854,(0,3):C.GC_1852,(0,4):C.GC_644,(0,5):C.GC_443,(0,7):C.GC_431,(0,6):C.GC_434})

V_120 = Vertex(name = 'V_120',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS21, L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_1877,(0,1):C.GC_1884,(0,2):C.GC_207,(0,3):C.GC_541,(0,4):C.GC_535})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS13, L.VVSS18, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS6, L.VVSS8, L.VVSS9 ],
               couplings = {(0,1):C.GC_40,(0,0):C.GC_42,(0,7):C.GC_437,(0,8):C.GC_441,(0,2):C.GC_1853,(0,3):C.GC_646,(0,4):C.GC_442,(0,6):C.GC_432,(0,5):C.GC_435})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS18, L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_1883,(0,1):C.GC_206,(0,2):C.GC_540,(0,3):C.GC_536})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS16, L.VVVS27, L.VVVS30, L.VVVS35, L.VVVS45, L.VVVS47, L.VVVS49, L.VVVS5, L.VVVS50, L.VVVS57, L.VVVS60, L.VVVS67, L.VVVS69, L.VVVS70, L.VVVS9 ],
               couplings = {(0,12):C.GC_1181,(0,10):C.GC_1319,(0,14):C.GC_1177,(0,11):C.GC_889,(0,13):C.GC_890,(0,4):C.GC_1709,(0,9):C.GC_1296,(0,8):C.GC_882,(0,6):C.GC_887,(0,5):C.GC_892,(0,7):C.GC_1179,(0,3):C.GC_884,(0,15):C.GC_1708,(0,1):C.GC_1710,(0,0):C.GC_2012,(0,2):C.GC_2010})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS16, L.VVVS27, L.VVVS30, L.VVVS35, L.VVVS45 ],
               couplings = {(0,4):C.GC_1746,(0,5):C.GC_997,(0,3):C.GC_990,(0,1):C.GC_1739,(0,0):C.GC_2013,(0,2):C.GC_2014})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS26, L.VVVS33, L.VVVS34, L.VVVS48, L.VVVS49, L.VVVS51, L.VVVS56, L.VVVS61, L.VVVS66, L.VVVS68, L.VVVS71 ],
               couplings = {(0,9):C.GC_1176,(0,7):C.GC_1317,(0,11):C.GC_1180,(0,10):C.GC_888,(0,8):C.GC_891,(0,4):C.GC_1178,(0,3):C.GC_1318,(0,0):C.GC_883,(0,5):C.GC_886,(0,6):C.GC_893,(0,2):C.GC_885,(0,1):C.GC_2011})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS26, L.VVVS33, L.VVVS34, L.VVVS48, L.VVVS51 ],
               couplings = {(0,3):C.GC_1297,(0,2):C.GC_1379,(0,4):C.GC_998,(0,1):C.GC_991,(0,0):C.GC_2015})

V_127 = Vertex(name = 'V_127',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS22, L.VVSS25, L.VVSS26, L.VVSS7 ],
               couplings = {(0,0):C.GC_455,(0,1):C.GC_1951,(0,2):C.GC_735,(0,4):C.GC_737,(0,3):C.GC_738})

V_128 = Vertex(name = 'V_128',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS22, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_1967,(0,1):C.GC_794,(0,2):C.GC_790})

V_129 = Vertex(name = 'V_129',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4, L.VVSS7 ],
               couplings = {(0,1):C.GC_454,(0,0):C.GC_456,(0,5):C.GC_1947,(0,3):C.GC_734,(0,6):C.GC_736,(0,4):C.GC_739,(0,2):C.GC_1949})

V_130 = Vertex(name = 'V_130',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS17, L.VVSS25, L.VVSS26, L.VVSS4 ],
               couplings = {(0,3):C.GC_1965,(0,1):C.GC_793,(0,2):C.GC_791,(0,0):C.GC_1963})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS12, L.VVVS13, L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS29, L.VVVS32, L.VVVS41, L.VVVS42, L.VVVS44, L.VVVS52, L.VVVS53, L.VVVS72, L.VVVS73, L.VVVS74, L.VVVS75, L.VVVS76, L.VVVS77 ],
               couplings = {(0,16):C.GC_1704,(0,15):C.GC_1706,(0,17):C.GC_903,(0,18):C.GC_904,(0,14):C.GC_1386,(0,13):C.GC_1387,(0,9):C.GC_1765,(0,12):C.GC_906,(0,11):C.GC_1298,(0,8):C.GC_1388,(0,2):C.GC_900,(0,0):C.GC_1698,(0,7):C.GC_901,(0,6):C.GC_1699,(0,1):C.GC_1383,(0,4):C.GC_1384,(0,10):C.GC_1697,(0,3):C.GC_2016,(0,5):C.GC_2017})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS29, L.VVVS32, L.VVVS41, L.VVVS42, L.VVVS44, L.VVVS53 ],
               couplings = {(0,6):C.GC_1378,(0,8):C.GC_999,(0,5):C.GC_1416,(0,4):C.GC_992,(0,3):C.GC_1743,(0,1):C.GC_1413,(0,7):C.GC_1744,(0,0):C.GC_2025,(0,2):C.GC_2022})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS12, L.VVVS13, L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS29, L.VVVS32, L.VVVS41, L.VVVS42, L.VVVS44, L.VVVS52, L.VVVS53, L.VVVS72, L.VVVS73, L.VVVS74, L.VVVS75, L.VVVS76, L.VVVS77 ],
               couplings = {(0,16):C.GC_1704,(0,15):C.GC_1707,(0,17):C.GC_902,(0,18):C.GC_904,(0,14):C.GC_1385,(0,13):C.GC_1387,(0,9):C.GC_1764,(0,12):C.GC_906,(0,11):C.GC_1298,(0,8):C.GC_1388,(0,2):C.GC_900,(0,0):C.GC_1698,(0,7):C.GC_901,(0,6):C.GC_1699,(0,1):C.GC_1383,(0,4):C.GC_1384,(0,10):C.GC_1697,(0,3):C.GC_2016,(0,5):C.GC_2017})

V_134 = Vertex(name = 'V_134',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS19, L.VVVS25, L.VVVS29, L.VVVS32, L.VVVS41, L.VVVS42, L.VVVS44, L.VVVS53 ],
               couplings = {(0,6):C.GC_1378,(0,8):C.GC_999,(0,5):C.GC_1416,(0,4):C.GC_992,(0,3):C.GC_1743,(0,1):C.GC_1413,(0,7):C.GC_1744,(0,0):C.GC_2025,(0,2):C.GC_2022})

V_135 = Vertex(name = 'V_135',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS11, L.VVVS28, L.VVVS31, L.VVVS46, L.VVVS63 ],
               couplings = {(0,4):C.GC_1762,(0,3):C.GC_1805,(0,0):C.GC_1806,(0,2):C.GC_1807,(0,1):C.GC_2032})

V_136 = Vertex(name = 'V_136',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS28, L.VVVS31, L.VVVS46 ],
               couplings = {(0,2):C.GC_1819,(0,1):C.GC_1818,(0,0):C.GC_2033})

V_137 = Vertex(name = 'V_137',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV105, L.VVVV109, L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV50, L.VVVV68, L.VVVV81, L.VVVV88 ],
               couplings = {(0,7):C.GC_1969,(0,6):C.GC_864,(0,4):C.GC_865,(0,3):C.GC_863,(0,2):C.GC_881,(0,0):C.GC_1976,(0,5):C.GC_1977,(0,1):C.GC_1978,(0,8):C.GC_2042})

V_138 = Vertex(name = 'V_138',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV105, L.VVVV109, L.VVVV117, L.VVVV88 ],
               couplings = {(0,2):C.GC_880,(0,0):C.GC_1986,(0,1):C.GC_1985,(0,3):C.GC_2043})

V_139 = Vertex(name = 'V_139',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS25, L.VVSS26, L.VVSS7 ],
               couplings = {(0,0):C.GC_456,(0,1):C.GC_748,(0,3):C.GC_746,(0,2):C.GC_751})

V_140 = Vertex(name = 'V_140',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_802,(0,1):C.GC_788})

V_141 = Vertex(name = 'V_141',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS25, L.VVSS26, L.VVSS7 ],
               couplings = {(0,1):C.GC_451,(0,0):C.GC_455,(0,2):C.GC_749,(0,4):C.GC_747,(0,3):C.GC_750})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_803,(0,1):C.GC_787})

V_143 = Vertex(name = 'V_143',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS25, L.VVSS26, L.VVSS7 ],
               couplings = {(0,0):C.GC_456,(0,1):C.GC_748,(0,3):C.GC_746,(0,2):C.GC_751})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_802,(0,1):C.GC_788})

V_145 = Vertex(name = 'V_145',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS25, L.VVSS26, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_49,(0,6):C.GC_567,(0,1):C.GC_745,(0,3):C.GC_44,(0,5):C.GC_652,(0,4):C.GC_563,(0,2):C.GC_740})

V_146 = Vertex(name = 'V_146',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_800,(0,1):C.GC_796})

V_147 = Vertex(name = 'V_147',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,1):C.GC_46,(0,0):C.GC_48,(0,8):C.GC_566,(0,9):C.GC_568,(0,2):C.GC_742,(0,3):C.GC_744,(0,5):C.GC_45,(0,7):C.GC_652,(0,6):C.GC_564,(0,4):C.GC_741})

V_148 = Vertex(name = 'V_148',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_799,(0,1):C.GC_797})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS25, L.VVSS26, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS9 ],
               couplings = {(0,0):C.GC_49,(0,6):C.GC_567,(0,1):C.GC_745,(0,3):C.GC_44,(0,5):C.GC_652,(0,4):C.GC_563,(0,2):C.GC_740})

V_150 = Vertex(name = 'V_150',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_800,(0,1):C.GC_796})

V_151 = Vertex(name = 'V_151',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35, L.VVVS54, L.VVVS55, L.VVVS9 ],
               couplings = {(0,2):C.GC_902,(0,3):C.GC_905,(0,1):C.GC_1703,(0,4):C.GC_1702,(0,0):C.GC_1705})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35 ],
               couplings = {(0,1):C.GC_1745,(0,0):C.GC_1738})

V_153 = Vertex(name = 'V_153',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS23, L.VVVS24, L.VVVS3, L.VVVS34, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS40, L.VVVS41, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS6, L.VVVS7 ],
               couplings = {(0,12):C.GC_1766,(0,13):C.GC_1769,(0,3):C.GC_1185,(0,4):C.GC_1186,(0,14):C.GC_1314,(0,15):C.GC_1315,(0,6):C.GC_1767,(0,10):C.GC_1006,(0,7):C.GC_1701,(0,8):C.GC_1187,(0,11):C.GC_1316,(0,9):C.GC_1644,(0,5):C.GC_1643,(0,16):C.GC_1182,(0,17):C.GC_1311,(0,0):C.GC_1645,(0,2):C.GC_1183,(0,1):C.GC_1312})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS34, L.VVVS37, L.VVVS38, L.VVVS41 ],
               couplings = {(0,3):C.GC_1419,(0,4):C.GC_1286,(0,6):C.GC_1373,(0,5):C.GC_1648,(0,0):C.GC_1647,(0,2):C.GC_1274,(0,1):C.GC_1368})

V_155 = Vertex(name = 'V_155',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35, L.VVVS54, L.VVVS55, L.VVVS9 ],
               couplings = {(0,2):C.GC_903,(0,3):C.GC_905,(0,1):C.GC_1703,(0,4):C.GC_1702,(0,0):C.GC_1705})

V_156 = Vertex(name = 'V_156',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35 ],
               couplings = {(0,1):C.GC_1745,(0,0):C.GC_1738})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS23, L.VVVS24, L.VVVS3, L.VVVS34, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS40, L.VVVS41, L.VVVS56, L.VVVS57, L.VVVS58, L.VVVS59, L.VVVS6, L.VVVS7 ],
               couplings = {(0,12):C.GC_1766,(0,13):C.GC_1768,(0,3):C.GC_1184,(0,4):C.GC_1186,(0,14):C.GC_1313,(0,15):C.GC_1315,(0,6):C.GC_1767,(0,10):C.GC_1006,(0,7):C.GC_1700,(0,8):C.GC_1187,(0,11):C.GC_1316,(0,9):C.GC_1644,(0,5):C.GC_1643,(0,16):C.GC_1182,(0,17):C.GC_1311,(0,0):C.GC_1645,(0,2):C.GC_1183,(0,1):C.GC_1312})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS34, L.VVVS37, L.VVVS38, L.VVVS41 ],
               couplings = {(0,3):C.GC_1419,(0,4):C.GC_1286,(0,6):C.GC_1373,(0,5):C.GC_1648,(0,0):C.GC_1647,(0,2):C.GC_1274,(0,1):C.GC_1368})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35, L.VVVS55, L.VVVS9 ],
               couplings = {(0,2):C.GC_1761,(0,1):C.GC_1812,(0,3):C.GC_1811,(0,0):C.GC_1813})

V_160 = Vertex(name = 'V_160',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS35 ],
               couplings = {(0,1):C.GC_1822,(0,0):C.GC_1817})

V_161 = Vertex(name = 'V_161',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS19, L.VVVS21, L.VVVS41, L.VVVS72, L.VVVS74, L.VVVS8 ],
               couplings = {(0,4):C.GC_1190,(0,7):C.GC_1322,(0,6):C.GC_1424,(0,5):C.GC_1810,(0,0):C.GC_1763,(0,8):C.GC_1188,(0,2):C.GC_1320,(0,1):C.GC_1422,(0,3):C.GC_1808})

V_162 = Vertex(name = 'V_162',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS41 ],
               couplings = {(0,1):C.GC_1821,(0,0):C.GC_1820})

V_163 = Vertex(name = 'V_163',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV111, L.VVVV113, L.VVVV114, L.VVVV115, L.VVVV117, L.VVVV118, L.VVVV13, L.VVVV14, L.VVVV16, L.VVVV2, L.VVVV28, L.VVVV34, L.VVVV35, L.VVVV36, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV47, L.VVVV6, L.VVVV62, L.VVVV64, L.VVVV68, L.VVVV89 ],
               couplings = {(0,11):C.GC_1970,(0,9):C.GC_866,(0,23):C.GC_759,(0,22):C.GC_577,(0,10):C.GC_58,(0,8):C.GC_760,(0,20):C.GC_576,(0,0):C.GC_579,(0,12):C.GC_57,(0,14):C.GC_758,(0,16):C.GC_643,(0,13):C.GC_642,(0,7):C.GC_869,(0,18):C.GC_870,(0,5):C.GC_761,(0,6):C.GC_578,(0,17):C.GC_876,(0,3):C.GC_818,(0,1):C.GC_630,(0,2):C.GC_879,(0,21):C.GC_868,(0,4):C.GC_867,(0,15):C.GC_1982,(0,19):C.GC_1981,(0,24):C.GC_1983})

V_164 = Vertex(name = 'V_164',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV115, L.VVVV117, L.VVVV118, L.VVVV39, L.VVVV42, L.VVVV89 ],
               couplings = {(0,4):C.GC_878,(0,1):C.GC_817,(0,2):C.GC_628,(0,0):C.GC_877,(0,3):C.GC_1989,(0,5):C.GC_1984})

V_165 = Vertex(name = 'V_165',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV18, L.VVVV21, L.VVVV46, L.VVVV49, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV58, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV90, L.VVVV97 ],
               couplings = {(0,16):C.GC_1450,(0,4):C.GC_1529,(0,18):C.GC_1619,(0,17):C.GC_1628,(0,5):C.GC_820,(0,11):C.GC_464,(0,13):C.GC_819,(0,14):C.GC_632,(0,3):C.GC_824,(0,15):C.GC_466,(0,12):C.GC_822,(0,0):C.GC_634,(0,2):C.GC_825,(0,1):C.GC_862,(0,20):C.GC_1980,(0,8):C.GC_1449,(0,6):C.GC_1528,(0,7):C.GC_1971,(0,10):C.GC_1618,(0,9):C.GC_1627,(0,19):C.GC_1979})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV117, L.VVVV90, L.VVVV97 ],
               couplings = {(0,0):C.GC_861,(0,2):C.GC_1988,(0,1):C.GC_1987})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS5 ],
               couplings = {(0,1):C.GC_31,(0,0):C.GC_33,(0,3):C.GC_446,(0,2):C.GC_450,(0,4):C.GC_650,(0,5):C.GC_36,(0,7):C.GC_24,(0,6):C.GC_27})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_547,(0,1):C.GC_192,(0,2):C.GC_182})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS5 ],
               couplings = {(0,1):C.GC_30,(0,0):C.GC_34,(0,3):C.GC_447,(0,2):C.GC_449,(0,4):C.GC_651,(0,5):C.GC_35,(0,7):C.GC_23,(0,6):C.GC_28})

V_170 = Vertex(name = 'V_170',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_191,(0,2):C.GC_183})

V_171 = Vertex(name = 'V_171',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS5 ],
               couplings = {(0,1):C.GC_29,(0,0):C.GC_33,(0,3):C.GC_446,(0,2):C.GC_448,(0,4):C.GC_649,(0,5):C.GC_36,(0,7):C.GC_24,(0,6):C.GC_27})

V_172 = Vertex(name = 'V_172',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_547,(0,1):C.GC_192,(0,2):C.GC_182})

V_173 = Vertex(name = 'V_173',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS10, L.VVSS11, L.VVSS12, L.VVSS13, L.VVSS23, L.VVSS25, L.VVSS26, L.VVSS5 ],
               couplings = {(0,1):C.GC_30,(0,0):C.GC_32,(0,3):C.GC_445,(0,2):C.GC_449,(0,4):C.GC_648,(0,5):C.GC_37,(0,7):C.GC_25,(0,6):C.GC_26})

V_174 = Vertex(name = 'V_174',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS23, L.VVSS25, L.VVSS26 ],
               couplings = {(0,0):C.GC_548,(0,1):C.GC_193,(0,2):C.GC_181})

V_175 = Vertex(name = 'V_175',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS21, L.VVVS23, L.VVVS36, L.VVVS41, L.VVVS42, L.VVVS65, L.VVVS75, L.VVVS8 ],
               couplings = {(0,7):C.GC_894,(0,6):C.GC_898,(0,2):C.GC_1171,(0,1):C.GC_1172,(0,5):C.GC_896,(0,3):C.GC_1169,(0,4):C.GC_1175,(0,8):C.GC_1164,(0,0):C.GC_1167})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS41, L.VVVS42 ],
               couplings = {(0,2):C.GC_1005,(0,1):C.GC_1285,(0,0):C.GC_1273})

V_177 = Vertex(name = 'V_177',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS20, L.VVVS22, L.VVVS24, L.VVVS36, L.VVVS37, L.VVVS42, L.VVVS6, L.VVVS64, L.VVVS74 ],
               couplings = {(0,7):C.GC_895,(0,8):C.GC_899,(0,1):C.GC_1170,(0,2):C.GC_1173,(0,3):C.GC_897,(0,5):C.GC_1168,(0,4):C.GC_1174,(0,6):C.GC_1165,(0,0):C.GC_1166})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS20, L.VVVS36, L.VVVS37 ],
               couplings = {(0,1):C.GC_1004,(0,2):C.GC_1284,(0,0):C.GC_1272})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.a, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS15 ],
               couplings = {(0,0):C.GC_453})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS23, L.VVSS8 ],
               couplings = {(0,0):C.GC_47,(0,2):C.GC_565,(0,1):C.GC_743})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS15 ],
               couplings = {(0,0):C.GC_452})

V_182 = Vertex(name = 'V_182',
               particles = [ P.a, P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS54 ],
               couplings = {(0,0):C.GC_1759})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS22, L.VVVS42, L.VVVS73, L.VVVS75 ],
               couplings = {(0,0):C.GC_1189,(0,3):C.GC_1321,(0,2):C.GC_1423,(0,1):C.GC_1809})

V_184 = Vertex(name = 'V_184',
               particles = [ P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS62 ],
               couplings = {(0,0):C.GC_1760})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV68 ],
               couplings = {(0,3):C.GC_871,(0,2):C.GC_872,(0,1):C.GC_873,(0,0):C.GC_875})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV117 ],
               couplings = {(0,0):C.GC_874})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV114, L.VVVV117, L.VVVV12, L.VVVV14, L.VVVV24, L.VVVV3, L.VVVV60, L.VVVV61, L.VVVV66, L.VVVV68 ],
               couplings = {(0,9):C.GC_826,(0,4):C.GC_821,(0,7):C.GC_465,(0,3):C.GC_827,(0,5):C.GC_467,(0,6):C.GC_633,(0,2):C.GC_635,(0,8):C.GC_823,(0,1):C.GC_828,(0,0):C.GC_860})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV117 ],
               couplings = {(0,0):C.GC_859})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS6 ],
               couplings = {(0,0):C.GC_97,(0,1):C.GC_158})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS6 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_224})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_96,(0,0):C.GC_159})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_217,(0,0):C.GC_225})

V_193 = Vertex(name = 'V_193',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS21 ],
               couplings = {(0,0):C.GC_157})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS21 ],
               couplings = {(0,0):C.GC_226})

V_195 = Vertex(name = 'V_195',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS14, L.VSSSS29 ],
               couplings = {(0,0):C.GC_158,(0,1):C.GC_97})

V_196 = Vertex(name = 'V_196',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS14, L.VSSSS29 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_219})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1680,(0,1):C.GC_1213})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1695,(0,1):C.GC_1310})

V_199 = Vertex(name = 'V_199',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_247,(0,1):C.GC_292})

V_200 = Vertex(name = 'V_200',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_254,(0,1):C.GC_413})

V_201 = Vertex(name = 'V_201',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS35, L.VVSSS42 ],
               couplings = {(0,1):C.GC_1211,(0,0):C.GC_1681})

V_202 = Vertex(name = 'V_202',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS35, L.VVSSS42 ],
               couplings = {(0,1):C.GC_1307,(0,0):C.GC_1696})

V_203 = Vertex(name = 'V_203',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_294,(0,1):C.GC_279,(0,2):C.GC_290})

V_204 = Vertex(name = 'V_204',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_415,(0,1):C.GC_416,(0,2):C.GC_411})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS22, L.VSSSS9 ],
               couplings = {(0,1):C.GC_288,(0,2):C.GC_282,(0,0):C.GC_292})

V_206 = Vertex(name = 'V_206',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS22, L.VSSSS9 ],
               couplings = {(0,1):C.GC_409,(0,2):C.GC_419,(0,0):C.GC_413})

V_207 = Vertex(name = 'V_207',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS2, L.VSSSS20, L.VSSSS7 ],
               couplings = {(0,1):C.GC_284,(0,0):C.GC_294,(0,2):C.GC_285})

V_208 = Vertex(name = 'V_208',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS2, L.VSSSS20, L.VSSSS7 ],
               couplings = {(0,1):C.GC_421,(0,0):C.GC_415,(0,2):C.GC_406})

V_209 = Vertex(name = 'V_209',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_1679})

V_210 = Vertex(name = 'V_210',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_1694})

V_211 = Vertex(name = 'V_211',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_281,(0,0):C.GC_286,(0,2):C.GC_292})

V_212 = Vertex(name = 'V_212',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_418,(0,0):C.GC_407,(0,2):C.GC_413})

V_213 = Vertex(name = 'V_213',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_1680,(0,1):C.GC_1213})

V_214 = Vertex(name = 'V_214',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_1695,(0,1):C.GC_1310})

V_215 = Vertex(name = 'V_215',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_294})

V_216 = Vertex(name = 'V_216',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_415})

V_217 = Vertex(name = 'V_217',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_1043,(0,2):C.GC_1047,(0,0):C.GC_1042})

V_218 = Vertex(name = 'V_218',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_1132,(0,2):C.GC_1141,(0,0):C.GC_1149})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_1041,(0,0):C.GC_1048,(0,1):C.GC_1044})

V_220 = Vertex(name = 'V_220',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_1148,(0,0):C.GC_1142,(0,1):C.GC_1133})

V_221 = Vertex(name = 'V_221',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS78 ],
               couplings = {(0,0):C.GC_1859,(0,1):C.GC_1537})

V_222 = Vertex(name = 'V_222',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS78 ],
               couplings = {(0,0):C.GC_1886,(0,1):C.GC_1558})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1678,(0,1):C.GC_1212})

V_224 = Vertex(name = 'V_224',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1693,(0,1):C.GC_1309})

V_225 = Vertex(name = 'V_225',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_248,(0,1):C.GC_293})

V_226 = Vertex(name = 'V_226',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_255,(0,1):C.GC_414})

V_227 = Vertex(name = 'V_227',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_294,(0,1):C.GC_279,(0,2):C.GC_290})

V_228 = Vertex(name = 'V_228',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_415,(0,1):C.GC_416,(0,2):C.GC_411})

V_229 = Vertex(name = 'V_229',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS21, L.VVSSS44 ],
               couplings = {(0,1):C.GC_1681,(0,0):C.GC_1210})

V_230 = Vertex(name = 'V_230',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS21, L.VVSSS44 ],
               couplings = {(0,1):C.GC_1696,(0,0):C.GC_1306})

V_231 = Vertex(name = 'V_231',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS24, L.VSSSS30, L.VSSSS8 ],
               couplings = {(0,0):C.GC_283,(0,2):C.GC_289,(0,1):C.GC_293})

V_232 = Vertex(name = 'V_232',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS24, L.VSSSS30, L.VSSSS8 ],
               couplings = {(0,0):C.GC_420,(0,2):C.GC_410,(0,1):C.GC_414})

V_233 = Vertex(name = 'V_233',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS33, L.VSSSS4 ],
               couplings = {(0,1):C.GC_291,(0,0):C.GC_284,(0,2):C.GC_294})

V_234 = Vertex(name = 'V_234',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS33, L.VSSSS4 ],
               couplings = {(0,1):C.GC_412,(0,0):C.GC_421,(0,2):C.GC_415})

V_235 = Vertex(name = 'V_235',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_1679})

V_236 = Vertex(name = 'V_236',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_1694})

V_237 = Vertex(name = 'V_237',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_280,(0,0):C.GC_287,(0,2):C.GC_293})

V_238 = Vertex(name = 'V_238',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_417,(0,0):C.GC_408,(0,2):C.GC_414})

V_239 = Vertex(name = 'V_239',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_1678,(0,1):C.GC_1212})

V_240 = Vertex(name = 'V_240',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_1693,(0,1):C.GC_1309})

V_241 = Vertex(name = 'V_241',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_294})

V_242 = Vertex(name = 'V_242',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_415})

V_243 = Vertex(name = 'V_243',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS116, L.VVVSS126, L.VVVSS131, L.VVVSS143, L.VVVSS154, L.VVVSS16, L.VVVSS162, L.VVVSS21, L.VVVSS31, L.VVVSS37, L.VVVSS39, L.VVVSS42, L.VVVSS65, L.VVVSS87, L.VVVSS89 ],
               couplings = {(0,4):C.GC_87,(0,6):C.GC_93,(0,10):C.GC_307,(0,11):C.GC_312,(0,7):C.GC_81,(0,1):C.GC_92,(0,0):C.GC_210,(0,14):C.GC_304,(0,13):C.GC_314,(0,3):C.GC_88,(0,5):C.GC_300,(0,9):C.GC_302,(0,2):C.GC_83,(0,12):C.GC_1859,(0,8):C.GC_1538})

V_244 = Vertex(name = 'V_244',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS131, L.VVVSS143, L.VVVSS31, L.VVVSS37, L.VVVSS65, L.VVVSS87 ],
               couplings = {(0,5):C.GC_392,(0,1):C.GC_170,(0,3):C.GC_386,(0,0):C.GC_174,(0,4):C.GC_1886,(0,2):C.GC_1559})

V_245 = Vertex(name = 'V_245',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS24, L.VVSSS26, L.VVSSS57 ],
               couplings = {(0,0):C.GC_1041,(0,1):C.GC_1048,(0,2):C.GC_1045})

V_246 = Vertex(name = 'V_246',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS24, L.VVSSS26, L.VVSSS57 ],
               couplings = {(0,0):C.GC_1148,(0,1):C.GC_1142,(0,2):C.GC_1134})

V_247 = Vertex(name = 'V_247',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1651,(0,1):C.GC_1048})

V_248 = Vertex(name = 'V_248',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_1670,(0,1):C.GC_1142})

V_249 = Vertex(name = 'V_249',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS32, L.VVSSS5 ],
               couplings = {(0,2):C.GC_1040,(0,0):C.GC_1047,(0,1):C.GC_1043})

V_250 = Vertex(name = 'V_250',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS32, L.VVSSS5 ],
               couplings = {(0,2):C.GC_1147,(0,0):C.GC_1141,(0,1):C.GC_1132})

V_251 = Vertex(name = 'V_251',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS8 ],
               couplings = {(0,0):C.GC_1650})

V_252 = Vertex(name = 'V_252',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS8 ],
               couplings = {(0,0):C.GC_1671})

V_253 = Vertex(name = 'V_253',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS15, L.VVSSS59 ],
               couplings = {(0,0):C.GC_1651,(0,1):C.GC_1048})

V_254 = Vertex(name = 'V_254',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS15, L.VVSSS59 ],
               couplings = {(0,0):C.GC_1670,(0,1):C.GC_1142})

V_255 = Vertex(name = 'V_255',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS13, L.VVVVS14, L.VVVVS143, L.VVVVS145, L.VVVVS15, L.VVVVS161, L.VVVVS198, L.VVVVS208, L.VVVVS211, L.VVVVS235, L.VVVVS251, L.VVVVS258, L.VVVVS26, L.VVVVS27, L.VVVVS33 ],
               couplings = {(0,4):C.GC_1056,(0,2):C.GC_1208,(0,3):C.GC_1203,(0,1):C.GC_1055,(0,13):C.GC_1050,(0,0):C.GC_1200,(0,8):C.GC_1057,(0,11):C.GC_1201,(0,10):C.GC_1207,(0,6):C.GC_1205,(0,14):C.GC_1051,(0,7):C.GC_1052,(0,9):C.GC_1299,(0,12):C.GC_1632,(0,5):C.GC_1997})

V_256 = Vertex(name = 'V_256',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS161, L.VVVVS198, L.VVVVS211, L.VVVVS258, L.VVVVS26, L.VVVVS33 ],
               couplings = {(0,2):C.GC_1120,(0,3):C.GC_1269,(0,1):C.GC_1263,(0,5):C.GC_1116,(0,4):C.GC_1635,(0,0):C.GC_2000})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS106, L.VVVSS111, L.VVVSS170, L.VVVSS186, L.VVVSS4, L.VVVSS49, L.VVVSS66, L.VVVSS69, L.VVVSS83, L.VVVSS99 ],
               couplings = {(0,2):C.GC_268,(0,3):C.GC_278,(0,4):C.GC_261,(0,9):C.GC_266,(0,0):C.GC_274,(0,8):C.GC_272,(0,1):C.GC_399,(0,7):C.GC_1461,(0,5):C.GC_1465,(0,6):C.GC_1469})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS49, L.VVVSS66, L.VVVSS69, L.VVVSS83, L.VVVSS99 ],
               couplings = {(0,4):C.GC_380,(0,3):C.GC_377,(0,2):C.GC_1507,(0,0):C.GC_1495,(0,1):C.GC_1501})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS106, L.VVVSS111, L.VVVSS170, L.VVVSS186, L.VVVSS4, L.VVVSS48, L.VVVSS73, L.VVVSS75, L.VVVSS83, L.VVVSS99 ],
               couplings = {(0,2):C.GC_267,(0,3):C.GC_277,(0,4):C.GC_263,(0,9):C.GC_264,(0,0):C.GC_273,(0,8):C.GC_270,(0,1):C.GC_397,(0,7):C.GC_1463,(0,5):C.GC_1462,(0,6):C.GC_1467})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS48, L.VVVSS73, L.VVVSS75, L.VVVSS83, L.VVVSS99 ],
               couplings = {(0,4):C.GC_382,(0,3):C.GC_375,(0,2):C.GC_1493,(0,0):C.GC_1508,(0,1):C.GC_1499})

V_261 = Vertex(name = 'V_261',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_1046,(0,2):C.GC_1049,(0,0):C.GC_1039})

V_262 = Vertex(name = 'V_262',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_1135,(0,2):C.GC_1143,(0,0):C.GC_1146})

V_263 = Vertex(name = 'V_263',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_1041,(0,0):C.GC_1048,(0,1):C.GC_1044})

V_264 = Vertex(name = 'V_264',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_1148,(0,0):C.GC_1142,(0,1):C.GC_1133})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS122, L.VVVSS125, L.VVVSS13, L.VVVSS175, L.VVVSS193, L.VVVSS32, L.VVVSS36, L.VVVSS46, L.VVVSS57, L.VVVSS91 ],
               couplings = {(0,3):C.GC_268,(0,4):C.GC_276,(0,9):C.GC_265,(0,0):C.GC_274,(0,1):C.GC_398,(0,2):C.GC_262,(0,6):C.GC_271,(0,8):C.GC_1464,(0,5):C.GC_1468,(0,7):C.GC_1460})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS32, L.VVVSS36, L.VVVSS46, L.VVVSS57, L.VVVSS91 ],
               couplings = {(0,4):C.GC_381,(0,1):C.GC_376,(0,3):C.GC_1494,(0,0):C.GC_1500,(0,2):C.GC_1506})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS122, L.VVVSS125, L.VVVSS13, L.VVVSS175, L.VVVSS193, L.VVVSS33, L.VVVSS36, L.VVVSS45, L.VVVSS68, L.VVVSS91 ],
               couplings = {(0,3):C.GC_269,(0,4):C.GC_277,(0,9):C.GC_264,(0,0):C.GC_275,(0,1):C.GC_397,(0,2):C.GC_263,(0,6):C.GC_270,(0,8):C.GC_1459,(0,5):C.GC_1467,(0,7):C.GC_1466})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS33, L.VVVSS36, L.VVVSS45, L.VVVSS68, L.VVVSS91 ],
               couplings = {(0,4):C.GC_382,(0,1):C.GC_375,(0,3):C.GC_1505,(0,0):C.GC_1499,(0,2):C.GC_1496})

V_269 = Vertex(name = 'V_269',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS78 ],
               couplings = {(0,0):C.GC_1860,(0,1):C.GC_1538})

V_270 = Vertex(name = 'V_270',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS78 ],
               couplings = {(0,0):C.GC_1887,(0,1):C.GC_1559})

V_271 = Vertex(name = 'V_271',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS140, L.VVVVS151, L.VVVVS164, L.VVVVS19, L.VVVVS202, L.VVVVS209, L.VVVVS21, L.VVVVS213, L.VVVVS217, L.VVVVS220, L.VVVVS24, L.VVVVS59, L.VVVVS64, L.VVVVS69, L.VVVVS75 ],
               couplings = {(0,10):C.GC_1056,(0,0):C.GC_1209,(0,1):C.GC_1204,(0,6):C.GC_1054,(0,14):C.GC_1050,(0,3):C.GC_1200,(0,5):C.GC_1057,(0,9):C.GC_1202,(0,7):C.GC_1207,(0,8):C.GC_1300,(0,2):C.GC_1051,(0,4):C.GC_1053,(0,12):C.GC_1206,(0,11):C.GC_1998,(0,13):C.GC_1633})

V_272 = Vertex(name = 'V_272',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS164, L.VVVVS209, L.VVVVS220, L.VVVVS59, L.VVVVS64, L.VVVVS69 ],
               couplings = {(0,1):C.GC_1120,(0,2):C.GC_1268,(0,0):C.GC_1116,(0,4):C.GC_1264,(0,3):C.GC_2001,(0,5):C.GC_1636})

V_273 = Vertex(name = 'V_273',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS138, L.VVVVS157, L.VVVVS186, L.VVVVS237, L.VVVVS250, L.VVVVS41, L.VVVVS59, L.VVVVS65, L.VVVVS69 ],
               couplings = {(0,1):C.GC_1033,(0,0):C.GC_1037,(0,2):C.GC_1031,(0,3):C.GC_1035,(0,4):C.GC_1125,(0,5):C.GC_1030,(0,7):C.GC_1034,(0,6):C.GC_1990,(0,8):C.GC_1629})

V_274 = Vertex(name = 'V_274',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS186, L.VVVVS59, L.VVVVS65, L.VVVVS69 ],
               couplings = {(0,0):C.GC_1113,(0,2):C.GC_1110,(0,1):C.GC_1993,(0,3):C.GC_1630})

V_275 = Vertex(name = 'V_275',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS27, L.VSSSS5 ],
               couplings = {(0,1):C.GC_692,(0,0):C.GC_688})

V_276 = Vertex(name = 'V_276',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS27, L.VSSSS5 ],
               couplings = {(0,1):C.GC_725,(0,0):C.GC_718})

V_277 = Vertex(name = 'V_277',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS2, L.VVSSS33 ],
               couplings = {(0,0):C.GC_1737,(0,1):C.GC_1736})

V_278 = Vertex(name = 'V_278',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS2, L.VVSSS33 ],
               couplings = {(0,0):C.GC_1752,(0,1):C.GC_1758})

V_279 = Vertex(name = 'V_279',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS12, L.VSSSS17 ],
               couplings = {(0,0):C.GC_689,(0,1):C.GC_685,(0,2):C.GC_682})

V_280 = Vertex(name = 'V_280',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS12, L.VSSSS17 ],
               couplings = {(0,0):C.GC_719,(0,1):C.GC_715,(0,2):C.GC_721})

V_281 = Vertex(name = 'V_281',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS26, L.VSSSS3, L.VSSSS31 ],
               couplings = {(0,0):C.GC_687,(0,2):C.GC_684,(0,1):C.GC_691})

V_282 = Vertex(name = 'V_282',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS26, L.VSSSS3, L.VSSSS31 ],
               couplings = {(0,0):C.GC_717,(0,2):C.GC_724,(0,1):C.GC_720})

V_283 = Vertex(name = 'V_283',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_686,(0,0):C.GC_690})

V_284 = Vertex(name = 'V_284',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_716,(0,0):C.GC_723})

V_285 = Vertex(name = 'V_285',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS45 ],
               couplings = {(0,0):C.GC_1735})

V_286 = Vertex(name = 'V_286',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS45 ],
               couplings = {(0,0):C.GC_1757})

V_287 = Vertex(name = 'V_287',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS15, L.VSSSS16, L.VSSSS29 ],
               couplings = {(0,0):C.GC_685,(0,1):C.GC_683,(0,2):C.GC_689})

V_288 = Vertex(name = 'V_288',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS15, L.VSSSS16, L.VSSSS29 ],
               couplings = {(0,0):C.GC_715,(0,1):C.GC_722,(0,2):C.GC_719})

V_289 = Vertex(name = 'V_289',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS28, L.VSSSS32 ],
               couplings = {(0,0):C.GC_688,(0,1):C.GC_692})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS28, L.VSSSS32 ],
               couplings = {(0,0):C.GC_718,(0,1):C.GC_725})

V_291 = Vertex(name = 'V_291',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS113, L.VVVSS114, L.VVVSS115, L.VVVSS132, L.VVVSS141, L.VVVSS15, L.VVVSS151, L.VVVSS152, L.VVVSS159, L.VVVSS160, L.VVVSS168, L.VVVSS184, L.VVVSS24, L.VVVSS27, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS41, L.VVVSS43, L.VVVSS50, L.VVVSS88, L.VVVSS90, L.VVVSS93, L.VVVSS94 ],
               couplings = {(0,7):C.GC_128,(0,9):C.GC_134,(0,18):C.GC_346,(0,17):C.GC_348,(0,10):C.GC_477,(0,11):C.GC_482,(0,8):C.GC_609,(0,6):C.GC_616,(0,0):C.GC_131,(0,1):C.GC_214,(0,23):C.GC_343,(0,22):C.GC_351,(0,2):C.GC_474,(0,3):C.GC_483,(0,20):C.GC_612,(0,12):C.GC_468,(0,21):C.GC_165,(0,4):C.GC_471,(0,14):C.GC_160,(0,5):C.GC_336,(0,15):C.GC_168,(0,16):C.GC_339,(0,13):C.GC_1864,(0,19):C.GC_1862})

V_292 = Vertex(name = 'V_292',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS132, L.VVVSS141, L.VVVSS27, L.VVVSS35, L.VVVSS38, L.VVVSS50, L.VVVSS88, L.VVVSS90, L.VVVSS93 ],
               couplings = {(0,8):C.GC_395,(0,0):C.GC_543,(0,6):C.GC_624,(0,7):C.GC_180,(0,1):C.GC_537,(0,3):C.GC_175,(0,4):C.GC_389,(0,2):C.GC_1878,(0,5):C.GC_1888})

V_293 = Vertex(name = 'V_293',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_937,(0,5):C.GC_942,(0,1):C.GC_949,(0,2):C.GC_1067,(0,4):C.GC_1073,(0,3):C.GC_1076})

V_294 = Vertex(name = 'V_294',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_1023,(0,5):C.GC_1013,(0,1):C.GC_1020,(0,2):C.GC_1150,(0,4):C.GC_1138,(0,3):C.GC_1144})

V_295 = Vertex(name = 'V_295',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_1654,(0,1):C.GC_939,(0,4):C.GC_944,(0,2):C.GC_1068,(0,3):C.GC_1074})

V_296 = Vertex(name = 'V_296',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_1669,(0,1):C.GC_1025,(0,4):C.GC_1015,(0,2):C.GC_1151,(0,3):C.GC_1139})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS10, L.VVSSS34, L.VVSSS36, L.VVSSS37, L.VVSSS39, L.VVSSS60 ],
               couplings = {(0,2):C.GC_938,(0,4):C.GC_943,(0,3):C.GC_949,(0,1):C.GC_1070,(0,5):C.GC_1072,(0,0):C.GC_1077})

V_298 = Vertex(name = 'V_298',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS10, L.VVSSS34, L.VVSSS36, L.VVSSS37, L.VVSSS39, L.VVSSS60 ],
               couplings = {(0,2):C.GC_1024,(0,4):C.GC_1014,(0,3):C.GC_1020,(0,1):C.GC_1153,(0,5):C.GC_1137,(0,0):C.GC_1145})

V_299 = Vertex(name = 'V_299',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS133, L.VVVSS139, L.VVVSS15, L.VVVSS151, L.VVVSS153, L.VVVSS159, L.VVVSS161, L.VVVSS167, L.VVVSS182, L.VVVSS20, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS41, L.VVVSS43, L.VVVSS60, L.VVVSS88, L.VVVSS90, L.VVVSS93, L.VVVSS94 ],
               couplings = {(0,7):C.GC_130,(0,9):C.GC_136,(0,17):C.GC_345,(0,16):C.GC_347,(0,11):C.GC_479,(0,10):C.GC_480,(0,8):C.GC_610,(0,6):C.GC_615,(0,0):C.GC_133,(0,1):C.GC_212,(0,22):C.GC_342,(0,21):C.GC_352,(0,3):C.GC_476,(0,2):C.GC_485,(0,19):C.GC_613,(0,20):C.GC_163,(0,13):C.GC_162,(0,5):C.GC_337,(0,12):C.GC_470,(0,14):C.GC_166,(0,15):C.GC_338,(0,4):C.GC_473,(0,18):C.GC_1861})

V_300 = Vertex(name = 'V_300',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS121, L.VVVSS139, L.VVVSS35, L.VVVSS38, L.VVVSS60, L.VVVSS88, L.VVVSS90, L.VVVSS93 ],
               couplings = {(0,7):C.GC_396,(0,0):C.GC_545,(0,5):C.GC_623,(0,6):C.GC_178,(0,2):C.GC_177,(0,3):C.GC_388,(0,1):C.GC_539,(0,4):C.GC_1890})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_940,(0,3):C.GC_943,(0,2):C.GC_1652,(0,0):C.GC_948})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_1026,(0,3):C.GC_1014,(0,2):C.GC_1673,(0,0):C.GC_1019})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS70, L.VVVSS76, L.VVVSS79 ],
               couplings = {(0,0):C.GC_1839,(0,1):C.GC_1905,(0,2):C.GC_1577})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS70, L.VVVSS76, L.VVVSS79 ],
               couplings = {(0,0):C.GC_1845,(0,1):C.GC_1920,(0,2):C.GC_1596})

V_305 = Vertex(name = 'V_305',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS113, L.VVVSS114, L.VVVSS115, L.VVVSS132, L.VVVSS141, L.VVVSS15, L.VVVSS151, L.VVVSS152, L.VVVSS159, L.VVVSS160, L.VVVSS168, L.VVVSS184, L.VVVSS24, L.VVVSS27, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS41, L.VVVSS43, L.VVVSS50, L.VVVSS88, L.VVVSS90, L.VVVSS93, L.VVVSS94 ],
               couplings = {(0,7):C.GC_129,(0,9):C.GC_134,(0,18):C.GC_346,(0,17):C.GC_349,(0,10):C.GC_477,(0,11):C.GC_481,(0,8):C.GC_608,(0,6):C.GC_616,(0,0):C.GC_132,(0,1):C.GC_213,(0,23):C.GC_343,(0,22):C.GC_350,(0,2):C.GC_474,(0,3):C.GC_484,(0,20):C.GC_611,(0,12):C.GC_469,(0,21):C.GC_164,(0,4):C.GC_472,(0,14):C.GC_161,(0,5):C.GC_335,(0,15):C.GC_167,(0,16):C.GC_340,(0,13):C.GC_1865,(0,19):C.GC_1863})

V_306 = Vertex(name = 'V_306',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS132, L.VVVSS141, L.VVVSS27, L.VVVSS35, L.VVVSS38, L.VVVSS50, L.VVVSS88, L.VVVSS90, L.VVVSS93 ],
               couplings = {(0,8):C.GC_394,(0,0):C.GC_544,(0,6):C.GC_625,(0,7):C.GC_179,(0,1):C.GC_538,(0,3):C.GC_176,(0,4):C.GC_390,(0,2):C.GC_1879,(0,5):C.GC_1889})

V_307 = Vertex(name = 'V_307',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_941,(0,5):C.GC_946,(0,1):C.GC_950,(0,2):C.GC_1069,(0,4):C.GC_1075,(0,3):C.GC_1077})

V_308 = Vertex(name = 'V_308',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_1027,(0,5):C.GC_1017,(0,1):C.GC_1021,(0,2):C.GC_1152,(0,4):C.GC_1140,(0,3):C.GC_1145})

V_309 = Vertex(name = 'V_309',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_1654,(0,1):C.GC_939,(0,4):C.GC_944,(0,2):C.GC_1068,(0,3):C.GC_1074})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_1669,(0,1):C.GC_1025,(0,4):C.GC_1015,(0,2):C.GC_1151,(0,3):C.GC_1139})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS11, L.VVSSS19, L.VVSSS20, L.VVSSS40, L.VVSSS46, L.VVSSS47 ],
               couplings = {(0,4):C.GC_938,(0,3):C.GC_949,(0,5):C.GC_1070,(0,0):C.GC_1077,(0,2):C.GC_947,(0,1):C.GC_1071})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS11, L.VVSSS19, L.VVSSS20, L.VVSSS40, L.VVSSS46, L.VVSSS47 ],
               couplings = {(0,4):C.GC_1024,(0,3):C.GC_1020,(0,5):C.GC_1153,(0,0):C.GC_1145,(0,2):C.GC_1018,(0,1):C.GC_1136})

V_313 = Vertex(name = 'V_313',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS119, L.VVVSS120, L.VVVSS121, L.VVVSS133, L.VVVSS139, L.VVVSS15, L.VVVSS151, L.VVVSS153, L.VVVSS159, L.VVVSS161, L.VVVSS167, L.VVVSS182, L.VVVSS20, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS41, L.VVVSS43, L.VVVSS60, L.VVVSS88, L.VVVSS90, L.VVVSS93, L.VVVSS94 ],
               couplings = {(0,7):C.GC_130,(0,9):C.GC_135,(0,17):C.GC_344,(0,16):C.GC_347,(0,11):C.GC_478,(0,10):C.GC_480,(0,8):C.GC_610,(0,6):C.GC_614,(0,0):C.GC_133,(0,1):C.GC_212,(0,22):C.GC_341,(0,21):C.GC_352,(0,3):C.GC_475,(0,2):C.GC_485,(0,19):C.GC_613,(0,20):C.GC_163,(0,13):C.GC_162,(0,5):C.GC_337,(0,12):C.GC_470,(0,14):C.GC_166,(0,15):C.GC_338,(0,4):C.GC_473,(0,18):C.GC_1861})

V_314 = Vertex(name = 'V_314',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS121, L.VVVSS139, L.VVVSS35, L.VVVSS38, L.VVVSS60, L.VVVSS88, L.VVVSS90, L.VVVSS93 ],
               couplings = {(0,7):C.GC_396,(0,0):C.GC_545,(0,5):C.GC_623,(0,6):C.GC_178,(0,2):C.GC_177,(0,3):C.GC_388,(0,1):C.GC_539,(0,4):C.GC_1890})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_938,(0,3):C.GC_945,(0,2):C.GC_1653,(0,0):C.GC_951})

V_316 = Vertex(name = 'V_316',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_1024,(0,3):C.GC_1016,(0,2):C.GC_1672,(0,0):C.GC_1022})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS118, L.VVVSS127, L.VVVSS136, L.VVVSS140, L.VVVSS145, L.VVVSS159, L.VVVSS166, L.VVVSS178, L.VVVSS185, L.VVVSS186, L.VVVSS25, L.VVVSS26, L.VVVSS61, L.VVVSS88, L.VVVSS96, L.VVVSS97 ],
               couplings = {(0,7):C.GC_320,(0,5):C.GC_503,(0,9):C.GC_326,(0,8):C.GC_73,(0,6):C.GC_76,(0,14):C.GC_324,(0,2):C.GC_401,(0,13):C.GC_506,(0,11):C.GC_64,(0,15):C.GC_70,(0,0):C.GC_79,(0,4):C.GC_67,(0,1):C.GC_319,(0,12):C.GC_1902,(0,10):C.GC_317,(0,3):C.GC_323})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS118, L.VVVSS127, L.VVVSS140, L.VVVSS145, L.VVVSS61, L.VVVSS88 ],
               couplings = {(0,5):C.GC_553,(0,0):C.GC_195,(0,3):C.GC_185,(0,1):C.GC_384,(0,4):C.GC_1917,(0,2):C.GC_379})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS106, L.VVVSS107, L.VVVSS117, L.VVVSS12, L.VVVSS151, L.VVVSS169, L.VVVSS170, L.VVVSS183, L.VVVSS188, L.VVVSS2, L.VVVSS29, L.VVVSS30, L.VVVSS73, L.VVVSS83, L.VVVSS86, L.VVVSS99 ],
               couplings = {(0,8):C.GC_327,(0,4):C.GC_508,(0,6):C.GC_321,(0,7):C.GC_74,(0,5):C.GC_75,(0,14):C.GC_680,(0,1):C.GC_400,(0,9):C.GC_63,(0,2):C.GC_71,(0,15):C.GC_78,(0,0):C.GC_325,(0,13):C.GC_66,(0,3):C.GC_679,(0,11):C.GC_681,(0,10):C.GC_1906,(0,12):C.GC_1901})

V_320 = Vertex(name = 'V_320',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS29, L.VVVSS30, L.VVVSS73, L.VVVSS83, L.VVVSS86, L.VVVSS99 ],
               couplings = {(0,4):C.GC_713,(0,5):C.GC_194,(0,3):C.GC_184,(0,1):C.GC_702,(0,0):C.GC_1913,(0,2):C.GC_1916})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS104, L.VVVSS12, L.VVVSS128, L.VVVSS129, L.VVVSS130, L.VVVSS134, L.VVVSS142, L.VVVSS146, L.VVVSS151, L.VVVSS159, L.VVVSS164, L.VVVSS165, L.VVVSS179, L.VVVSS19, L.VVVSS195, L.VVVSS23, L.VVVSS28, L.VVVSS30, L.VVVSS47, L.VVVSS53, L.VVVSS54, L.VVVSS58, L.VVVSS62, L.VVVSS67, L.VVVSS86, L.VVVSS88 ],
               couplings = {(0,10):C.GC_320,(0,14):C.GC_328,(0,9):C.GC_502,(0,8):C.GC_507,(0,12):C.GC_72,(0,11):C.GC_77,(0,5):C.GC_318,(0,0):C.GC_324,(0,4):C.GC_402,(0,24):C.GC_501,(0,25):C.GC_505,(0,20):C.GC_554,(0,15):C.GC_65,(0,6):C.GC_68,(0,3):C.GC_69,(0,2):C.GC_80,(0,13):C.GC_316,(0,1):C.GC_500,(0,7):C.GC_322,(0,17):C.GC_504,(0,22):C.GC_1475,(0,18):C.GC_1476,(0,16):C.GC_1477,(0,23):C.GC_1573,(0,19):C.GC_1574,(0,21):C.GC_1575})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS128, L.VVVSS134, L.VVVSS142, L.VVVSS146, L.VVVSS28, L.VVVSS30, L.VVVSS47, L.VVVSS53, L.VVVSS58, L.VVVSS62, L.VVVSS67, L.VVVSS86 ],
               couplings = {(0,1):C.GC_383,(0,11):C.GC_533,(0,2):C.GC_186,(0,0):C.GC_196,(0,3):C.GC_378,(0,5):C.GC_532,(0,9):C.GC_1509,(0,6):C.GC_1497,(0,4):C.GC_1502,(0,10):C.GC_1598,(0,7):C.GC_1591,(0,8):C.GC_1594})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS118, L.VVVSS127, L.VVVSS136, L.VVVSS140, L.VVVSS145, L.VVVSS159, L.VVVSS166, L.VVVSS178, L.VVVSS185, L.VVVSS186, L.VVVSS25, L.VVVSS26, L.VVVSS61, L.VVVSS88, L.VVVSS96, L.VVVSS97 ],
               couplings = {(0,7):C.GC_320,(0,5):C.GC_503,(0,9):C.GC_326,(0,8):C.GC_73,(0,6):C.GC_76,(0,14):C.GC_324,(0,2):C.GC_401,(0,13):C.GC_506,(0,11):C.GC_64,(0,15):C.GC_70,(0,0):C.GC_79,(0,4):C.GC_67,(0,1):C.GC_319,(0,12):C.GC_1903,(0,10):C.GC_317,(0,3):C.GC_323})

V_324 = Vertex(name = 'V_324',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS118, L.VVVSS127, L.VVVSS140, L.VVVSS145, L.VVVSS61, L.VVVSS88 ],
               couplings = {(0,5):C.GC_553,(0,0):C.GC_195,(0,3):C.GC_185,(0,1):C.GC_384,(0,4):C.GC_1918,(0,2):C.GC_379})

V_325 = Vertex(name = 'V_325',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS112, L.VVVVS12, L.VVVVS142, L.VVVVS146, L.VVVVS147, L.VVVVS148, L.VVVVS158, L.VVVVS163, L.VVVVS177, L.VVVVS196, L.VVVVS223, L.VVVVS231, L.VVVVS234, L.VVVVS239, L.VVVVS240, L.VVVVS241, L.VVVVS254, L.VVVVS38, L.VVVVS53, L.VVVVS54, L.VVVVS59, L.VVVVS61 ],
               couplings = {(0,6):C.GC_932,(0,3):C.GC_1065,(0,20):C.GC_1198,(0,5):C.GC_1061,(0,4):C.GC_936,(0,19):C.GC_1196,(0,0):C.GC_1058,(0,2):C.GC_1191,(0,9):C.GC_931,(0,11):C.GC_935,(0,12):C.GC_1010,(0,10):C.GC_1193,(0,14):C.GC_1059,(0,13):C.GC_1063,(0,17):C.GC_1127,(0,16):C.GC_1195,(0,15):C.GC_1199,(0,1):C.GC_1062,(0,18):C.GC_929,(0,22):C.GC_934,(0,7):C.GC_1991,(0,8):C.GC_2005,(0,21):C.GC_1638})

V_326 = Vertex(name = 'V_326',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS112, L.VVVVS158, L.VVVVS163, L.VVVVS177, L.VVVVS196, L.VVVVS239, L.VVVVS240, L.VVVVS59, L.VVVVS61 ],
               couplings = {(0,3):C.GC_981,(0,4):C.GC_1276,(0,5):C.GC_1114,(0,6):C.GC_1287,(0,0):C.GC_1111,(0,8):C.GC_978,(0,1):C.GC_1995,(0,2):C.GC_2009,(0,7):C.GC_1640})

V_327 = Vertex(name = 'V_327',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS70, L.VVVSS76, L.VVVSS79 ],
               couplings = {(0,0):C.GC_1840,(0,1):C.GC_1904,(0,2):C.GC_1576})

V_328 = Vertex(name = 'V_328',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS70, L.VVVSS76, L.VVVSS79 ],
               couplings = {(0,0):C.GC_1844,(0,1):C.GC_1919,(0,2):C.GC_1595})

V_329 = Vertex(name = 'V_329',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS105, L.VVVVS111, L.VVVVS113, L.VVVVS120, L.VVVVS130, L.VVVVS131, L.VVVVS139, L.VVVVS144, L.VVVVS159, L.VVVVS160, L.VVVVS161, L.VVVVS168, L.VVVVS176, L.VVVVS2, L.VVVVS221, L.VVVVS230, L.VVVVS233, L.VVVVS242, L.VVVVS248, L.VVVVS253, L.VVVVS255, L.VVVVS28, L.VVVVS81 ],
               couplings = {(0,7):C.GC_932,(0,5):C.GC_1066,(0,3):C.GC_1198,(0,4):C.GC_1060,(0,6):C.GC_936,(0,2):C.GC_1197,(0,13):C.GC_1058,(0,21):C.GC_1191,(0,12):C.GC_931,(0,14):C.GC_935,(0,15):C.GC_1010,(0,20):C.GC_1199,(0,19):C.GC_1059,(0,1):C.GC_1062,(0,16):C.GC_1064,(0,18):C.GC_1126,(0,17):C.GC_1194,(0,0):C.GC_1192,(0,8):C.GC_1992,(0,9):C.GC_2004,(0,22):C.GC_930,(0,11):C.GC_933,(0,10):C.GC_1637})

V_330 = Vertex(name = 'V_330',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS105, L.VVVVS111, L.VVVVS159, L.VVVVS160, L.VVVVS161, L.VVVVS168, L.VVVVS176, L.VVVVS253, L.VVVVS255 ],
               couplings = {(0,6):C.GC_981,(0,8):C.GC_1287,(0,7):C.GC_1114,(0,1):C.GC_1111,(0,0):C.GC_1275,(0,2):C.GC_1994,(0,3):C.GC_2008,(0,5):C.GC_977,(0,4):C.GC_1639})

V_331 = Vertex(name = 'V_331',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS27, L.VVSSS53 ],
               couplings = {(0,0):C.GC_1780,(0,1):C.GC_1777})

V_332 = Vertex(name = 'V_332',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS27, L.VVSSS53 ],
               couplings = {(0,0):C.GC_1804,(0,1):C.GC_1799})

V_333 = Vertex(name = 'V_333',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS30, L.VVSSS6 ],
               couplings = {(0,0):C.GC_1775,(0,1):C.GC_1778})

V_334 = Vertex(name = 'V_334',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS30, L.VVSSS6 ],
               couplings = {(0,0):C.GC_1802,(0,1):C.GC_1800})

V_335 = Vertex(name = 'V_335',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16, L.VVSSS48, L.VVSSS58 ],
               couplings = {(0,0):C.GC_1646,(0,2):C.GC_1776,(0,3):C.GC_1774,(0,1):C.GC_1779})

V_336 = Vertex(name = 'V_336',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16, L.VVSSS48, L.VVSSS58 ],
               couplings = {(0,0):C.GC_1649,(0,2):C.GC_1798,(0,3):C.GC_1803,(0,1):C.GC_1801})

V_337 = Vertex(name = 'V_337',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS51, L.VVSSS59 ],
               couplings = {(0,0):C.GC_1777,(0,1):C.GC_1780})

V_338 = Vertex(name = 'V_338',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS51, L.VVSSS59 ],
               couplings = {(0,0):C.GC_1799,(0,1):C.GC_1804})

V_339 = Vertex(name = 'V_339',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS144, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS176, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS22, L.VVVSS32, L.VVVSS36, L.VVVSS51, L.VVVSS52, L.VVVSS6, L.VVVSS63, L.VVVSS64, L.VVVSS71, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,7):C.GC_355,(0,11):C.GC_358,(0,10):C.GC_488,(0,6):C.GC_493,(0,8):C.GC_117,(0,12):C.GC_119,(0,9):C.GC_599,(0,5):C.GC_604,(0,1):C.GC_253,(0,3):C.GC_124,(0,2):C.GC_403,(0,24):C.GC_782,(0,23):C.GC_607,(0,13):C.GC_105,(0,0):C.GC_659,(0,4):C.GC_112,(0,22):C.GC_664,(0,18):C.GC_595,(0,15):C.GC_598,(0,25):C.GC_658,(0,14):C.GC_1842,(0,16):C.GC_1898,(0,20):C.GC_1571,(0,17):C.GC_1927,(0,21):C.GC_1605,(0,19):C.GC_1481})

V_340 = Vertex(name = 'V_340',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS124, L.VVVSS144, L.VVVSS32, L.VVVSS36, L.VVVSS51, L.VVVSS52, L.VVVSS63, L.VVVSS64, L.VVVSS71, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,0):C.GC_199,(0,11):C.GC_551,(0,10):C.GC_622,(0,1):C.GC_189,(0,9):C.GC_708,(0,3):C.GC_619,(0,12):C.GC_710,(0,2):C.GC_1847,(0,4):C.GC_1915,(0,7):C.GC_1593,(0,5):C.GC_1943,(0,8):C.GC_1617,(0,6):C.GC_1504})

V_341 = Vertex(name = 'V_341',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS144, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS176, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS22, L.VVVSS33, L.VVVSS36, L.VVVSS59, L.VVVSS6, L.VVVSS68, L.VVVSS72, L.VVVSS77, L.VVVSS80, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,7):C.GC_353,(0,11):C.GC_356,(0,10):C.GC_487,(0,6):C.GC_494,(0,8):C.GC_116,(0,12):C.GC_118,(0,9):C.GC_601,(0,5):C.GC_602,(0,1):C.GC_251,(0,3):C.GC_123,(0,2):C.GC_405,(0,24):C.GC_785,(0,23):C.GC_605,(0,13):C.GC_104,(0,0):C.GC_661,(0,4):C.GC_113,(0,22):C.GC_662,(0,17):C.GC_593,(0,15):C.GC_596,(0,25):C.GC_656,(0,16):C.GC_1478,(0,21):C.GC_1479,(0,18):C.GC_1568,(0,20):C.GC_1569,(0,14):C.GC_1925,(0,19):C.GC_1928})

V_342 = Vertex(name = 'V_342',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS124, L.VVVSS144, L.VVVSS33, L.VVVSS36, L.VVVSS59, L.VVVSS68, L.VVVSS72, L.VVVSS77, L.VVVSS80, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,0):C.GC_198,(0,11):C.GC_552,(0,10):C.GC_620,(0,1):C.GC_190,(0,9):C.GC_706,(0,3):C.GC_617,(0,12):C.GC_712,(0,4):C.GC_1510,(0,8):C.GC_1498,(0,5):C.GC_1597,(0,7):C.GC_1590,(0,2):C.GC_1941,(0,6):C.GC_1940})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS144, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS176, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS22, L.VVVSS32, L.VVVSS36, L.VVVSS51, L.VVVSS52, L.VVVSS6, L.VVVSS63, L.VVVSS64, L.VVVSS71, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,7):C.GC_354,(0,11):C.GC_358,(0,10):C.GC_489,(0,6):C.GC_493,(0,8):C.GC_117,(0,12):C.GC_120,(0,9):C.GC_599,(0,5):C.GC_603,(0,1):C.GC_252,(0,3):C.GC_125,(0,2):C.GC_404,(0,24):C.GC_783,(0,23):C.GC_606,(0,13):C.GC_106,(0,0):C.GC_660,(0,4):C.GC_111,(0,22):C.GC_663,(0,18):C.GC_594,(0,15):C.GC_597,(0,25):C.GC_657,(0,14):C.GC_1841,(0,16):C.GC_1897,(0,20):C.GC_1570,(0,17):C.GC_1926,(0,21):C.GC_1604,(0,19):C.GC_1480})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS124, L.VVVSS144, L.VVVSS32, L.VVVSS36, L.VVVSS51, L.VVVSS52, L.VVVSS63, L.VVVSS64, L.VVVSS71, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,0):C.GC_200,(0,11):C.GC_550,(0,10):C.GC_621,(0,1):C.GC_188,(0,9):C.GC_707,(0,3):C.GC_618,(0,12):C.GC_711,(0,2):C.GC_1846,(0,4):C.GC_1914,(0,7):C.GC_1592,(0,5):C.GC_1942,(0,8):C.GC_1616,(0,6):C.GC_1503})

V_345 = Vertex(name = 'V_345',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS122, L.VVVSS123, L.VVVSS124, L.VVVSS144, L.VVVSS173, L.VVVSS174, L.VVVSS175, L.VVVSS176, L.VVVSS191, L.VVVSS192, L.VVVSS193, L.VVVSS194, L.VVVSS22, L.VVVSS33, L.VVVSS36, L.VVVSS59, L.VVVSS6, L.VVVSS68, L.VVVSS72, L.VVVSS77, L.VVVSS80, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,7):C.GC_353,(0,11):C.GC_357,(0,10):C.GC_487,(0,6):C.GC_495,(0,8):C.GC_115,(0,12):C.GC_118,(0,9):C.GC_600,(0,5):C.GC_602,(0,1):C.GC_250,(0,3):C.GC_123,(0,2):C.GC_405,(0,24):C.GC_784,(0,23):C.GC_605,(0,13):C.GC_104,(0,0):C.GC_661,(0,4):C.GC_113,(0,22):C.GC_662,(0,17):C.GC_593,(0,15):C.GC_596,(0,25):C.GC_656,(0,16):C.GC_1478,(0,21):C.GC_1479,(0,18):C.GC_1568,(0,20):C.GC_1569,(0,14):C.GC_1925,(0,19):C.GC_1928})

V_346 = Vertex(name = 'V_346',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS124, L.VVVSS144, L.VVVSS33, L.VVVSS36, L.VVVSS59, L.VVVSS68, L.VVVSS72, L.VVVSS77, L.VVVSS80, L.VVVSS81, L.VVVSS91, L.VVVSS95, L.VVVSS98 ],
               couplings = {(0,0):C.GC_198,(0,11):C.GC_552,(0,10):C.GC_620,(0,1):C.GC_190,(0,9):C.GC_706,(0,3):C.GC_617,(0,12):C.GC_712,(0,4):C.GC_1510,(0,8):C.GC_1498,(0,5):C.GC_1597,(0,7):C.GC_1590,(0,2):C.GC_1941,(0,6):C.GC_1940})

V_347 = Vertex(name = 'V_347',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS102, L.VVVSS13, L.VVVSS171, L.VVVSS173, L.VVVSS190, L.VVVSS191, L.VVVSS32, L.VVVSS36, L.VVVSS40, L.VVVSS44, L.VVVSS5, L.VVVSS6, L.VVVSS63, L.VVVSS82, L.VVVSS91, L.VVVSS95 ],
               couplings = {(0,9):C.GC_361,(0,10):C.GC_363,(0,3):C.GC_512,(0,5):C.GC_514,(0,6):C.GC_639,(0,4):C.GC_641,(0,15):C.GC_840,(0,1):C.GC_762,(0,16):C.GC_838,(0,0):C.GC_763,(0,14):C.GC_764,(0,2):C.GC_774,(0,11):C.GC_360,(0,12):C.GC_637,(0,8):C.GC_836,(0,7):C.GC_1956,(0,13):C.GC_1957})

V_348 = Vertex(name = 'V_348',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS102, L.VVVSS32, L.VVVSS36, L.VVVSS63, L.VVVSS82, L.VVVSS91 ],
               couplings = {(0,5):C.GC_856,(0,0):C.GC_795,(0,4):C.GC_792,(0,2):C.GC_854,(0,1):C.GC_1968,(0,3):C.GC_1964})

V_349 = Vertex(name = 'V_349',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS117, L.VVVVS119, L.VVVVS124, L.VVVVS125, L.VVVVS128, L.VVVVS129, L.VVVVS134, L.VVVVS172, L.VVVVS174, L.VVVVS180, L.VVVVS181, L.VVVVS187, L.VVVVS189, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS21, L.VVVVS212, L.VVVVS23, L.VVVVS35, L.VVVVS37, L.VVVVS39, L.VVVVS40, L.VVVVS59, L.VVVVS62, L.VVVVS69, L.VVVVS70, L.VVVVS71, L.VVVVS92 ],
               couplings = {(0,25):C.GC_1103,(0,6):C.GC_1261,(0,3):C.GC_1399,(0,26):C.GC_1433,(0,1):C.GC_963,(0,5):C.GC_1727,(0,7):C.GC_1345,(0,2):C.GC_964,(0,4):C.GC_1397,(0,23):C.GC_1102,(0,27):C.GC_958,(0,34):C.GC_1097,(0,33):C.GC_1392,(0,18):C.GC_1105,(0,12):C.GC_1401,(0,22):C.GC_962,(0,24):C.GC_967,(0,11):C.GC_1323,(0,10):C.GC_1342,(0,21):C.GC_1381,(0,13):C.GC_1396,(0,19):C.GC_1730,(0,20):C.GC_1304,(0,0):C.GC_1256,(0,29):C.GC_1326,(0,16):C.GC_961,(0,14):C.GC_1259,(0,15):C.GC_1327,(0,8):C.GC_1100,(0,17):C.GC_1101,(0,9):C.GC_1394,(0,35):C.GC_1257,(0,28):C.GC_1339,(0,31):C.GC_1344,(0,30):C.GC_2018,(0,32):C.GC_2020})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS172, L.VVVVS174, L.VVVVS180, L.VVVVS181, L.VVVVS187, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS203, L.VVVVS212, L.VVVVS59, L.VVVVS62, L.VVVVS69, L.VVVVS92 ],
               couplings = {(0,8):C.GC_1122,(0,4):C.GC_1418,(0,9):C.GC_1003,(0,3):C.GC_1367,(0,2):C.GC_1362,(0,7):C.GC_996,(0,5):C.GC_1265,(0,6):C.GC_1364,(0,0):C.GC_1119,(0,1):C.GC_1414,(0,13):C.GC_1271,(0,11):C.GC_1361,(0,10):C.GC_2026,(0,12):C.GC_2023})

V_351 = Vertex(name = 'V_351',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS117, L.VVVVS119, L.VVVVS124, L.VVVVS125, L.VVVVS128, L.VVVVS129, L.VVVVS134, L.VVVVS172, L.VVVVS174, L.VVVVS180, L.VVVVS181, L.VVVVS187, L.VVVVS189, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS21, L.VVVVS212, L.VVVVS23, L.VVVVS35, L.VVVVS37, L.VVVVS39, L.VVVVS40, L.VVVVS59, L.VVVVS62, L.VVVVS69, L.VVVVS70, L.VVVVS71, L.VVVVS92 ],
               couplings = {(0,25):C.GC_1104,(0,6):C.GC_1261,(0,3):C.GC_1398,(0,26):C.GC_1433,(0,1):C.GC_963,(0,5):C.GC_1726,(0,7):C.GC_1345,(0,2):C.GC_965,(0,4):C.GC_1397,(0,23):C.GC_1102,(0,27):C.GC_959,(0,34):C.GC_1098,(0,33):C.GC_1393,(0,18):C.GC_1106,(0,12):C.GC_1400,(0,22):C.GC_962,(0,24):C.GC_966,(0,11):C.GC_1324,(0,10):C.GC_1341,(0,21):C.GC_1380,(0,13):C.GC_1396,(0,19):C.GC_1731,(0,20):C.GC_1303,(0,0):C.GC_1255,(0,29):C.GC_1325,(0,16):C.GC_960,(0,14):C.GC_1260,(0,15):C.GC_1328,(0,8):C.GC_1099,(0,17):C.GC_1101,(0,9):C.GC_1395,(0,35):C.GC_1258,(0,28):C.GC_1340,(0,31):C.GC_1343,(0,30):C.GC_2019,(0,32):C.GC_2021})

V_352 = Vertex(name = 'V_352',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS172, L.VVVVS174, L.VVVVS180, L.VVVVS181, L.VVVVS187, L.VVVVS192, L.VVVVS193, L.VVVVS195, L.VVVVS203, L.VVVVS212, L.VVVVS59, L.VVVVS62, L.VVVVS69, L.VVVVS92 ],
               couplings = {(0,8):C.GC_1123,(0,4):C.GC_1417,(0,9):C.GC_1002,(0,3):C.GC_1366,(0,2):C.GC_1363,(0,7):C.GC_995,(0,5):C.GC_1266,(0,6):C.GC_1365,(0,0):C.GC_1118,(0,1):C.GC_1415,(0,13):C.GC_1270,(0,11):C.GC_1360,(0,10):C.GC_2027,(0,12):C.GC_2024})

V_353 = Vertex(name = 'V_353',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS100, L.VVVVS101, L.VVVVS11, L.VVVVS125, L.VVVVS126, L.VVVVS156, L.VVVVS157, L.VVVVS167, L.VVVVS186, L.VVVVS188, L.VVVVS189, L.VVVVS192, L.VVVVS197, L.VVVVS199, L.VVVVS216, L.VVVVS227, L.VVVVS236, L.VVVVS237, L.VVVVS238, L.VVVVS35, L.VVVVS42, L.VVVVS43, L.VVVVS59, L.VVVVS60, L.VVVVS65, L.VVVVS69, L.VVVVS76, L.VVVVS78, L.VVVVS92, L.VVVVS93, L.VVVVS98, L.VVVVS99 ],
               couplings = {(0,1):C.GC_928,(0,30):C.GC_1096,(0,19):C.GC_1391,(0,5):C.GC_923,(0,6):C.GC_1091,(0,4):C.GC_1228,(0,0):C.GC_1231,(0,3):C.GC_1351,(0,31):C.GC_1353,(0,21):C.GC_1216,(0,23):C.GC_1772,(0,15):C.GC_1008,(0,29):C.GC_1089,(0,18):C.GC_1128,(0,14):C.GC_925,(0,17):C.GC_1094,(0,9):C.GC_1224,(0,16):C.GC_1234,(0,10):C.GC_1350,(0,8):C.GC_1354,(0,2):C.GC_908,(0,27):C.GC_1088,(0,11):C.GC_909,(0,13):C.GC_1092,(0,12):C.GC_1219,(0,20):C.GC_1347,(0,24):C.GC_1348,(0,28):C.GC_907,(0,22):C.GC_2002,(0,26):C.GC_1771,(0,7):C.GC_1773,(0,25):C.GC_2003})

V_354 = Vertex(name = 'V_354',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS167, L.VVVVS186, L.VVVVS192, L.VVVVS197, L.VVVVS199, L.VVVVS236, L.VVVVS59, L.VVVVS60, L.VVVVS65, L.VVVVS69, L.VVVVS92, L.VVVVS93 ],
               couplings = {(0,7):C.GC_1797,(0,11):C.GC_1115,(0,5):C.GC_1289,(0,1):C.GC_1376,(0,2):C.GC_984,(0,4):C.GC_1112,(0,3):C.GC_1278,(0,8):C.GC_1371,(0,10):C.GC_987,(0,6):C.GC_2007,(0,0):C.GC_1792,(0,9):C.GC_2006})

V_355 = Vertex(name = 'V_355',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS14, L.VVVSS189, L.VVVSS74, L.VVVSS85 ],
               couplings = {(0,2):C.GC_772,(0,0):C.GC_829,(0,1):C.GC_832,(0,4):C.GC_833,(0,3):C.GC_1972})

V_356 = Vertex(name = 'V_356',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS74, L.VVVSS85 ],
               couplings = {(0,0):C.GC_852,(0,2):C.GC_849,(0,1):C.GC_1974})

V_357 = Vertex(name = 'V_357',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS14, L.VVVSS172, L.VVVSS189, L.VVVSS67, L.VVVSS85 ],
               couplings = {(0,2):C.GC_768,(0,3):C.GC_771,(0,0):C.GC_830,(0,1):C.GC_831,(0,5):C.GC_834,(0,4):C.GC_1973})

V_358 = Vertex(name = 'V_358',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS67, L.VVVSS85 ],
               couplings = {(0,0):C.GC_851,(0,2):C.GC_850,(0,1):C.GC_1975})

V_359 = Vertex(name = 'V_359',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS107, L.VVVVS118, L.VVVVS123, L.VVVVS127, L.VVVVS135, L.VVVVS136, L.VVVVS137, L.VVVVS162, L.VVVVS170, L.VVVVS18, L.VVVVS183, L.VVVVS184, L.VVVVS194, L.VVVVS201, L.VVVVS252, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS7, L.VVVVS86, L.VVVVS87, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,6):C.GC_1107,(0,22):C.GC_1408,(0,3):C.GC_1249,(0,21):C.GC_1430,(0,1):C.GC_1333,(0,4):C.GC_1662,(0,5):C.GC_974,(0,2):C.GC_1720,(0,20):C.GC_1242,(0,18):C.GC_1329,(0,16):C.GC_1253,(0,10):C.GC_1431,(0,11):C.GC_1782,(0,17):C.GC_1012,(0,9):C.GC_1783,(0,12):C.GC_1786,(0,13):C.GC_1247,(0,15):C.GC_1718,(0,0):C.GC_1331,(0,14):C.GC_1337,(0,19):C.GC_1426,(0,8):C.GC_1428,(0,7):C.GC_2029})

V_360 = Vertex(name = 'V_360',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS107, L.VVVVS162, L.VVVVS170, L.VVVVS183, L.VVVVS184, L.VVVVS194, L.VVVVS201, L.VVVVS252, L.VVVVS259, L.VVVVS260 ],
               couplings = {(0,9):C.GC_1293,(0,3):C.GC_1436,(0,4):C.GC_1795,(0,5):C.GC_1794,(0,6):C.GC_1283,(0,8):C.GC_1131,(0,0):C.GC_1369,(0,7):C.GC_1374,(0,2):C.GC_1435,(0,1):C.GC_2031})

V_361 = Vertex(name = 'V_361',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS107, L.VVVVS118, L.VVVVS123, L.VVVVS127, L.VVVVS135, L.VVVVS136, L.VVVVS137, L.VVVVS162, L.VVVVS170, L.VVVVS18, L.VVVVS183, L.VVVVS184, L.VVVVS194, L.VVVVS201, L.VVVVS252, L.VVVVS259, L.VVVVS260, L.VVVVS261, L.VVVVS7, L.VVVVS86, L.VVVVS87, L.VVVVS95, L.VVVVS96 ],
               couplings = {(0,6):C.GC_1107,(0,22):C.GC_1408,(0,3):C.GC_1250,(0,21):C.GC_1429,(0,1):C.GC_1333,(0,4):C.GC_1663,(0,5):C.GC_974,(0,2):C.GC_1721,(0,20):C.GC_1243,(0,18):C.GC_1330,(0,16):C.GC_1252,(0,10):C.GC_1432,(0,11):C.GC_1781,(0,17):C.GC_1011,(0,9):C.GC_1784,(0,12):C.GC_1785,(0,13):C.GC_1244,(0,15):C.GC_1719,(0,0):C.GC_1332,(0,14):C.GC_1338,(0,19):C.GC_1425,(0,8):C.GC_1427,(0,7):C.GC_2028})

V_362 = Vertex(name = 'V_362',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS107, L.VVVVS162, L.VVVVS170, L.VVVVS183, L.VVVVS184, L.VVVVS194, L.VVVVS201, L.VVVVS252, L.VVVVS259, L.VVVVS260 ],
               couplings = {(0,9):C.GC_1292,(0,3):C.GC_1437,(0,4):C.GC_1796,(0,5):C.GC_1793,(0,6):C.GC_1280,(0,8):C.GC_1130,(0,0):C.GC_1370,(0,7):C.GC_1375,(0,2):C.GC_1434,(0,1):C.GC_2030})

V_363 = Vertex(name = 'V_363',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS104, L.VVVVS162, L.VVVVS191, L.VVVVS200, L.VVVVS84 ],
               couplings = {(0,0):C.GC_1814,(0,2):C.GC_1823,(0,4):C.GC_1824,(0,3):C.GC_1825,(0,1):C.GC_2034})

V_364 = Vertex(name = 'V_364',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS162, L.VVVVS191, L.VVVVS200 ],
               couplings = {(0,1):C.GC_1833,(0,2):C.GC_1832,(0,0):C.GC_2035})

V_365 = Vertex(name = 'V_365',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS14, L.VVVSS172, L.VVVSS189, L.VVVSS85 ],
               couplings = {(0,2):C.GC_510,(0,3):C.GC_515,(0,0):C.GC_777,(0,1):C.GC_775,(0,4):C.GC_778})

V_366 = Vertex(name = 'V_366',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS85 ],
               couplings = {(0,0):C.GC_804,(0,1):C.GC_789})

V_367 = Vertex(name = 'V_367',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS101, L.VVVSS11, L.VVVSS12, L.VVVSS149, L.VVVSS158, L.VVVSS163, L.VVVSS196, L.VVVSS30, L.VVVSS8, L.VVVSS84, L.VVVSS85, L.VVVSS86, L.VVVSS9, L.VVVSS97 ],
               couplings = {(0,4):C.GC_138,(0,5):C.GC_139,(0,6):C.GC_581,(0,7):C.GC_582,(0,0):C.GC_773,(0,12):C.GC_844,(0,1):C.GC_694,(0,13):C.GC_137,(0,2):C.GC_693,(0,9):C.GC_580,(0,14):C.GC_766,(0,11):C.GC_765,(0,10):C.GC_695,(0,3):C.GC_841,(0,8):C.GC_846})

V_368 = Vertex(name = 'V_368',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS101, L.VVVSS30, L.VVVSS84, L.VVVSS85, L.VVVSS86 ],
               couplings = {(0,0):C.GC_801,(0,5):C.GC_858,(0,1):C.GC_714,(0,4):C.GC_798,(0,3):C.GC_709,(0,2):C.GC_848})

V_369 = Vertex(name = 'V_369',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS103, L.VVVSS108, L.VVVSS109, L.VVVSS12, L.VVVSS138, L.VVVSS148, L.VVVSS156, L.VVVSS18, L.VVVSS30, L.VVVSS55, L.VVVSS56, L.VVVSS86 ],
               couplings = {(0,6):C.GC_114,(0,5):C.GC_120,(0,9):C.GC_490,(0,10):C.GC_492,(0,2):C.GC_126,(0,11):C.GC_670,(0,0):C.GC_551,(0,7):C.GC_107,(0,1):C.GC_676,(0,4):C.GC_112,(0,3):C.GC_665,(0,8):C.GC_673})

V_370 = Vertex(name = 'V_370',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS109, L.VVVSS138, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,0):C.GC_201,(0,3):C.GC_703,(0,1):C.GC_189,(0,2):C.GC_701})

V_371 = Vertex(name = 'V_371',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS105, L.VVVSS110, L.VVVSS112, L.VVVSS12, L.VVVSS137, L.VVVSS150, L.VVVSS157, L.VVVSS17, L.VVVSS180, L.VVVSS181, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,6):C.GC_115,(0,5):C.GC_121,(0,1):C.GC_122,(0,11):C.GC_668,(0,0):C.GC_549,(0,7):C.GC_109,(0,3):C.GC_667,(0,4):C.GC_110,(0,10):C.GC_671,(0,8):C.GC_486,(0,9):C.GC_497,(0,2):C.GC_674})

V_372 = Vertex(name = 'V_372',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS110, L.VVVSS137, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,0):C.GC_197,(0,3):C.GC_705,(0,1):C.GC_187,(0,2):C.GC_699})

V_373 = Vertex(name = 'V_373',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS169, L.VVVVS178, L.VVVVS82, L.VVVVS90, L.VVVVS91 ],
               couplings = {(0,3):C.GC_963,(0,4):C.GC_965,(0,1):C.GC_1725,(0,2):C.GC_1723,(0,0):C.GC_1728})

V_374 = Vertex(name = 'V_374',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS169, L.VVVVS178 ],
               couplings = {(0,1):C.GC_1748,(0,0):C.GC_1740})

V_375 = Vertex(name = 'V_375',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS141, L.VVVVS148, L.VVVVS166, L.VVVVS167, L.VVVVS173, L.VVVVS185, L.VVVVS190, L.VVVVS223, L.VVVVS224, L.VVVVS225, L.VVVVS226, L.VVVVS228, L.VVVVS232, L.VVVVS30, L.VVVVS36, L.VVVVS49, L.VVVVS50, L.VVVVS60, L.VVVVS63, L.VVVVS66, L.VVVVS76, L.VVVVS79, L.VVVVS80 ],
               couplings = {(0,18):C.GC_1250,(0,1):C.GC_1334,(0,3):C.GC_1787,(0,2):C.GC_1791,(0,17):C.GC_1248,(0,0):C.GC_1335,(0,24):C.GC_1243,(0,16):C.GC_1330,(0,8):C.GC_952,(0,14):C.GC_1254,(0,19):C.GC_1404,(0,10):C.GC_1420,(0,9):C.GC_1790,(0,12):C.GC_1011,(0,13):C.GC_1717,(0,11):C.GC_1338,(0,7):C.GC_970,(0,4):C.GC_1245,(0,21):C.GC_1331,(0,23):C.GC_954,(0,15):C.GC_969,(0,6):C.GC_957,(0,20):C.GC_972,(0,22):C.GC_1402,(0,5):C.GC_1407})

V_376 = Vertex(name = 'V_376',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS166, L.VVVVS167, L.VVVVS173, L.VVVVS185, L.VVVVS190, L.VVVVS225, L.VVVVS232, L.VVVVS60, L.VVVVS63, L.VVVVS66 ],
               couplings = {(0,4):C.GC_989,(0,6):C.GC_1294,(0,7):C.GC_1412,(0,5):C.GC_1375,(0,3):C.GC_983,(0,0):C.GC_1281,(0,9):C.GC_1369,(0,2):C.GC_986,(0,8):C.GC_979,(0,1):C.GC_1410})

V_377 = Vertex(name = 'V_377',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS169, L.VVVVS178, L.VVVVS82, L.VVVVS90, L.VVVVS91 ],
               couplings = {(0,3):C.GC_963,(0,4):C.GC_964,(0,1):C.GC_1724,(0,2):C.GC_1722,(0,0):C.GC_1729})

V_378 = Vertex(name = 'V_378',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS169, L.VVVVS178 ],
               couplings = {(0,1):C.GC_1747,(0,0):C.GC_1741})

V_379 = Vertex(name = 'V_379',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS103, L.VVVSS108, L.VVVSS109, L.VVVSS12, L.VVVSS138, L.VVVSS148, L.VVVSS156, L.VVVSS18, L.VVVSS30, L.VVVSS55, L.VVVSS56, L.VVVSS86 ],
               couplings = {(0,6):C.GC_114,(0,5):C.GC_119,(0,9):C.GC_491,(0,10):C.GC_492,(0,2):C.GC_127,(0,11):C.GC_669,(0,0):C.GC_550,(0,7):C.GC_108,(0,1):C.GC_677,(0,4):C.GC_111,(0,3):C.GC_666,(0,8):C.GC_672})

V_380 = Vertex(name = 'V_380',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS109, L.VVVSS138, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,0):C.GC_202,(0,3):C.GC_704,(0,1):C.GC_188,(0,2):C.GC_700})

V_381 = Vertex(name = 'V_381',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS105, L.VVVSS110, L.VVVSS112, L.VVVSS12, L.VVVSS137, L.VVVSS150, L.VVVSS157, L.VVVSS17, L.VVVSS180, L.VVVSS181, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,6):C.GC_116,(0,5):C.GC_121,(0,1):C.GC_122,(0,11):C.GC_668,(0,0):C.GC_549,(0,7):C.GC_109,(0,3):C.GC_667,(0,4):C.GC_110,(0,10):C.GC_671,(0,8):C.GC_486,(0,9):C.GC_496,(0,2):C.GC_675})

V_382 = Vertex(name = 'V_382',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS110, L.VVVSS137, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,0):C.GC_197,(0,3):C.GC_705,(0,1):C.GC_187,(0,2):C.GC_699})

V_383 = Vertex(name = 'V_383',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS141, L.VVVVS148, L.VVVVS166, L.VVVVS167, L.VVVVS173, L.VVVVS185, L.VVVVS190, L.VVVVS223, L.VVVVS224, L.VVVVS225, L.VVVVS226, L.VVVVS228, L.VVVVS232, L.VVVVS30, L.VVVVS36, L.VVVVS49, L.VVVVS50, L.VVVVS60, L.VVVVS63, L.VVVVS66, L.VVVVS76, L.VVVVS79, L.VVVVS80 ],
               couplings = {(0,18):C.GC_1249,(0,1):C.GC_1334,(0,3):C.GC_1788,(0,2):C.GC_1791,(0,17):C.GC_1248,(0,0):C.GC_1336,(0,24):C.GC_1242,(0,16):C.GC_1329,(0,8):C.GC_953,(0,14):C.GC_1251,(0,19):C.GC_1405,(0,10):C.GC_1421,(0,9):C.GC_1789,(0,12):C.GC_1012,(0,13):C.GC_1717,(0,11):C.GC_1337,(0,7):C.GC_971,(0,4):C.GC_1246,(0,21):C.GC_1332,(0,23):C.GC_955,(0,15):C.GC_968,(0,6):C.GC_956,(0,20):C.GC_973,(0,22):C.GC_1403,(0,5):C.GC_1406})

V_384 = Vertex(name = 'V_384',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS166, L.VVVVS167, L.VVVVS173, L.VVVVS185, L.VVVVS190, L.VVVVS225, L.VVVVS232, L.VVVVS60, L.VVVVS63, L.VVVVS66 ],
               couplings = {(0,4):C.GC_988,(0,6):C.GC_1291,(0,7):C.GC_1411,(0,5):C.GC_1374,(0,3):C.GC_982,(0,0):C.GC_1282,(0,9):C.GC_1370,(0,2):C.GC_985,(0,8):C.GC_980,(0,1):C.GC_1409})

V_385 = Vertex(name = 'V_385',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS152, L.VVVVS165, L.VVVVS167, L.VVVVS214, L.VVVVS215, L.VVVVS222, L.VVVVS48, L.VVVVS52, L.VVVVS56, L.VVVVS60, L.VVVVS67, L.VVVVS76, L.VVVVS77 ],
               couplings = {(0,7):C.GC_1225,(0,6):C.GC_1230,(0,0):C.GC_923,(0,8):C.GC_927,(0,12):C.GC_1215,(0,9):C.GC_1655,(0,4):C.GC_1007,(0,5):C.GC_1235,(0,3):C.GC_925,(0,1):C.GC_1218,(0,10):C.GC_1221,(0,11):C.GC_1656,(0,2):C.GC_1657})

V_386 = Vertex(name = 'V_386',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS165, L.VVVVS167, L.VVVVS222, L.VVVVS60 ],
               couplings = {(0,3):C.GC_1667,(0,2):C.GC_1290,(0,0):C.GC_1277,(0,1):C.GC_1666})

V_387 = Vertex(name = 'V_387',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS114, L.VVVVS115, L.VVVVS132, L.VVVVS144, L.VVVVS150, L.VVVVS17, L.VVVVS171, L.VVVVS175, L.VVVVS179, L.VVVVS182, L.VVVVS210, L.VVVVS221, L.VVVVS245, L.VVVVS246, L.VVVVS247, L.VVVVS25, L.VVVVS257, L.VVVVS29, L.VVVVS32, L.VVVVS72, L.VVVVS74, L.VVVVS89 ],
               couplings = {(0,1):C.GC_916,(0,0):C.GC_918,(0,15):C.GC_1083,(0,5):C.GC_1085,(0,4):C.GC_1236,(0,2):C.GC_1241,(0,3):C.GC_1356,(0,21):C.GC_1359,(0,19):C.GC_1078,(0,20):C.GC_910,(0,12):C.GC_915,(0,16):C.GC_921,(0,9):C.GC_1082,(0,10):C.GC_1087,(0,13):C.GC_1239,(0,14):C.GC_1301,(0,11):C.GC_1357,(0,8):C.GC_1684,(0,6):C.GC_1080,(0,7):C.GC_913,(0,17):C.GC_1683,(0,18):C.GC_1685})

V_388 = Vertex(name = 'V_388',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS171, L.VVVVS175, L.VVVVS179, L.VVVVS210, L.VVVVS221, L.VVVVS257, L.VVVVS32 ],
               couplings = {(0,5):C.GC_1001,(0,3):C.GC_1121,(0,4):C.GC_1382,(0,2):C.GC_1687,(0,0):C.GC_1117,(0,1):C.GC_994,(0,6):C.GC_1686})

V_389 = Vertex(name = 'V_389',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS12, L.VVVSS155, L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,1):C.GC_770,(0,3):C.GC_843,(0,0):C.GC_842,(0,2):C.GC_845})

V_390 = Vertex(name = 'V_390',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS30, L.VVVSS86 ],
               couplings = {(0,1):C.GC_857,(0,0):C.GC_847})

V_391 = Vertex(name = 'V_391',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS13, L.VVVSS173, L.VVVSS174, L.VVVSS36, L.VVVSS44, L.VVVSS5, L.VVVSS6, L.VVVSS7, L.VVVSS91 ],
               couplings = {(0,4):C.GC_362,(0,2):C.GC_513,(0,1):C.GC_640,(0,8):C.GC_839,(0,0):C.GC_776,(0,5):C.GC_359,(0,7):C.GC_509,(0,6):C.GC_636,(0,3):C.GC_835})

V_392 = Vertex(name = 'V_392',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS36, L.VVVSS91 ],
               couplings = {(0,1):C.GC_855,(0,0):C.GC_853})

V_393 = Vertex(name = 'V_393',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS167, L.VVVVS34, L.VVVVS60, L.VVVVS76 ],
               couplings = {(0,1):C.GC_1815,(0,2):C.GC_1829,(0,3):C.GC_1828,(0,0):C.GC_1830})

V_394 = Vertex(name = 'V_394',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS167, L.VVVVS60 ],
               couplings = {(0,1):C.GC_1836,(0,0):C.GC_1831})

V_395 = Vertex(name = 'V_395',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS16, L.VVVVS170, L.VVVVS183, L.VVVVS73, L.VVVVS83, L.VVVVS85, L.VVVVS86, L.VVVVS88, L.VVVVS94, L.VVVVS95, L.VVVVS97 ],
               couplings = {(0,8):C.GC_976,(0,0):C.GC_1109,(0,10):C.GC_1390,(0,9):C.GC_1439,(0,2):C.GC_1827,(0,5):C.GC_975,(0,3):C.GC_1108,(0,4):C.GC_1816,(0,7):C.GC_1389,(0,6):C.GC_1438,(0,1):C.GC_1826})

V_396 = Vertex(name = 'V_396',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS170, L.VVVVS183 ],
               couplings = {(0,1):C.GC_1835,(0,0):C.GC_1834})

V_397 = Vertex(name = 'V_397',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS135, L.VVVSS140, L.VVVSS15, L.VVVSS177, L.VVVSS193, L.VVVSS25, L.VVVSS38, L.VVVSS40, L.VVVSS41, L.VVVSS92, L.VVVSS93, L.VVVSS95 ],
               couplings = {(0,4):C.GC_86,(0,5):C.GC_95,(0,8):C.GC_308,(0,9):C.GC_311,(0,10):C.GC_91,(0,1):C.GC_209,(0,12):C.GC_305,(0,11):C.GC_313,(0,3):C.GC_299,(0,7):C.GC_301,(0,0):C.GC_84,(0,6):C.GC_82,(0,2):C.GC_89})

V_398 = Vertex(name = 'V_398',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS140, L.VVVSS38, L.VVVSS93 ],
               couplings = {(0,3):C.GC_391,(0,2):C.GC_385,(0,0):C.GC_173,(0,1):C.GC_171})

V_399 = Vertex(name = 'V_399',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS122, L.VVVSS175, L.VVVSS187, L.VVVSS36, L.VVVSS43, L.VVVSS44, L.VVVSS5, L.VVVSS91, L.VVVSS94 ],
               couplings = {(0,1):C.GC_85,(0,2):C.GC_94,(0,4):C.GC_309,(0,5):C.GC_310,(0,0):C.GC_90,(0,8):C.GC_306,(0,7):C.GC_315,(0,6):C.GC_298,(0,3):C.GC_303})

V_400 = Vertex(name = 'V_400',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS122, L.VVVSS36, L.VVVSS91 ],
               couplings = {(0,0):C.GC_211,(0,2):C.GC_393,(0,1):C.GC_387})

V_401 = Vertex(name = 'V_401',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS135, L.VVVSS140, L.VVVSS15, L.VVVSS177, L.VVVSS193, L.VVVSS25, L.VVVSS38, L.VVVSS40, L.VVVSS41, L.VVVSS92, L.VVVSS93, L.VVVSS95 ],
               couplings = {(0,4):C.GC_86,(0,5):C.GC_95,(0,8):C.GC_308,(0,9):C.GC_311,(0,10):C.GC_91,(0,1):C.GC_209,(0,12):C.GC_305,(0,11):C.GC_313,(0,3):C.GC_299,(0,7):C.GC_301,(0,0):C.GC_84,(0,6):C.GC_82,(0,2):C.GC_89})

V_402 = Vertex(name = 'V_402',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS140, L.VVVSS38, L.VVVSS93 ],
               couplings = {(0,3):C.GC_391,(0,2):C.GC_385,(0,0):C.GC_173,(0,1):C.GC_171})

V_403 = Vertex(name = 'V_403',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS153, L.VVVVS214, L.VVVVS44, L.VVVVS47, L.VVVVS5, L.VVVVS51, L.VVVVS57, L.VVVVS67, L.VVVVS68 ],
               couplings = {(0,6):C.GC_922,(0,0):C.GC_926,(0,3):C.GC_1227,(0,5):C.GC_1229,(0,4):C.GC_1214,(0,7):C.GC_924,(0,2):C.GC_1220,(0,1):C.GC_1222,(0,8):C.GC_1233})

V_404 = Vertex(name = 'V_404',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS44, L.VVVVS67, L.VVVVS68 ],
               couplings = {(0,1):C.GC_1009,(0,0):C.GC_1279,(0,2):C.GC_1288})

V_405 = Vertex(name = 'V_405',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS106, L.VVVVS113, L.VVVVS121, L.VVVVS133, L.VVVVS139, L.VVVVS14, L.VVVVS149, L.VVVVS20, L.VVVVS208, L.VVVVS22, L.VVVVS229, L.VVVVS242, L.VVVVS243, L.VVVVS244, L.VVVVS256, L.VVVVS3, L.VVVVS31, L.VVVVS4, L.VVVVS9 ],
               couplings = {(0,5):C.GC_1084,(0,9):C.GC_1086,(0,3):C.GC_1237,(0,6):C.GC_1240,(0,2):C.GC_919,(0,4):C.GC_1358,(0,1):C.GC_917,(0,15):C.GC_1079,(0,17):C.GC_911,(0,18):C.GC_1732,(0,13):C.GC_920,(0,7):C.GC_1658,(0,8):C.GC_1081,(0,10):C.GC_1733,(0,12):C.GC_1238,(0,14):C.GC_1302,(0,0):C.GC_912,(0,16):C.GC_1734,(0,11):C.GC_914})

V_406 = Vertex(name = 'V_406',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS106, L.VVVVS20, L.VVVVS229, L.VVVVS244, L.VVVVS31 ],
               couplings = {(0,3):C.GC_1000,(0,1):C.GC_1668,(0,2):C.GC_1749,(0,0):C.GC_993,(0,4):C.GC_1742})

V_407 = Vertex(name = 'V_407',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV135, L.VVVVV136, L.VVVVV137, L.VVVVV152, L.VVVVV153, L.VVVVV159, L.VVVVV17, L.VVVVV40, L.VVVVV42, L.VVVVV50, L.VVVVV51, L.VVVVV54, L.VVVVV59, L.VVVVV76, L.VVVVV77, L.VVVVV8, L.VVVVV99 ],
               couplings = {(0,14):C.GC_1533,(0,13):C.GC_1536,(0,6):C.GC_98,(0,16):C.GC_100,(0,15):C.GC_102,(0,9):C.GC_99,(0,3):C.GC_234,(0,4):C.GC_237,(0,12):C.GC_101,(0,5):C.GC_103,(0,2):C.GC_1532,(0,1):C.GC_1535,(0,0):C.GC_1555,(0,7):C.GC_1470,(0,8):C.GC_1531,(0,10):C.GC_1838,(0,11):C.GC_1534})

V_408 = Vertex(name = 'V_408',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV137, L.VVVVV159, L.VVVVV51, L.VVVVV54, L.VVVVV59 ],
               couplings = {(0,4):C.GC_228,(0,1):C.GC_231,(0,0):C.GC_1548,(0,2):C.GC_1843,(0,3):C.GC_1545})

V_409 = Vertex(name = 'V_409',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV12, L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV134, L.VVVVV138, L.VVVVV145, L.VVVVV146, L.VVVVV15, L.VVVVV157, L.VVVVV29, L.VVVVV30, L.VVVVV37, L.VVVVV65, L.VVVVV70, L.VVVVV78, L.VVVVV90 ],
               couplings = {(0,15):C.GC_1899,(0,13):C.GC_1474,(0,14):C.GC_1572,(0,9):C.GC_329,(0,0):C.GC_333,(0,17):C.GC_331,(0,16):C.GC_330,(0,7):C.GC_424,(0,8):C.GC_425,(0,10):C.GC_334,(0,12):C.GC_1471,(0,6):C.GC_332,(0,11):C.GC_1530,(0,2):C.GC_1472,(0,4):C.GC_1473,(0,1):C.GC_1900,(0,5):C.GC_1491,(0,3):C.GC_1858})

V_410 = Vertex(name = 'V_410',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV138, L.VVVVV157 ],
               couplings = {(0,5):C.GC_423,(0,4):C.GC_422,(0,1):C.GC_1488,(0,3):C.GC_1487,(0,0):C.GC_1588,(0,2):C.GC_1875})

V_411 = Vertex(name = 'V_411',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV100, L.VVVVV101, L.VVVVV115, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV14, L.VVVVV140, L.VVVVV142, L.VVVVV143, L.VVVVV147, L.VVVVV148, L.VVVVV155, L.VVVVV156, L.VVVVV16, L.VVVVV23, L.VVVVV28, L.VVVVV3, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV38, L.VVVVV39, L.VVVVV6, L.VVVVV64, L.VVVVV68, L.VVVVV69, L.VVVVV7, L.VVVVV79, L.VVVVV81, L.VVVVV91, L.VVVVV92 ],
               couplings = {(0,17):C.GC_1869,(0,19):C.GC_1870,(0,29):C.GC_1933,(0,27):C.GC_1936,(0,0):C.GC_372,(0,15):C.GC_516,(0,16):C.GC_367,(0,31):C.GC_526,(0,18):C.GC_368,(0,30):C.GC_530,(0,20):C.GC_369,(0,34):C.GC_528,(0,26):C.GC_522,(0,33):C.GC_524,(0,7):C.GC_527,(0,21):C.GC_520,(0,8):C.GC_429,(0,11):C.GC_557,(0,10):C.GC_558,(0,9):C.GC_559,(0,12):C.GC_562,(0,14):C.GC_525,(0,13):C.GC_531,(0,22):C.GC_426,(0,23):C.GC_370,(0,24):C.GC_517,(0,25):C.GC_519,(0,2):C.GC_529,(0,3):C.GC_1868,(0,6):C.GC_1871,(0,4):C.GC_1935,(0,32):C.GC_365,(0,1):C.GC_366,(0,28):C.GC_1866,(0,5):C.GC_1867})

V_412 = Vertex(name = 'V_412',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV100, L.VVVVV101, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV155, L.VVVVV156, L.VVVVV36, L.VVVVV39 ],
               couplings = {(0,6):C.GC_561,(0,5):C.GC_556,(0,7):C.GC_428,(0,8):C.GC_560,(0,1):C.GC_555,(0,4):C.GC_1876,(0,2):C.GC_1938,(0,0):C.GC_427,(0,3):C.GC_1874})

V_413 = Vertex(name = 'V_413',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV10, L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV106, L.VVVVV107, L.VVVVV108, L.VVVVV109, L.VVVVV11, L.VVVVV110, L.VVVVV111, L.VVVVV112, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV125, L.VVVVV13, L.VVVVV141, L.VVVVV150, L.VVVVV151, L.VVVVV160, L.VVVVV161, L.VVVVV18, L.VVVVV19, L.VVVVV24, L.VVVVV25, L.VVVVV27, L.VVVVV41, L.VVVVV43, L.VVVVV44, L.VVVVV45, L.VVVVV46, L.VVVVV49, L.VVVVV52, L.VVVVV53, L.VVVVV57, L.VVVVV58, L.VVVVV60, L.VVVVV61, L.VVVVV62, L.VVVVV74, L.VVVVV84, L.VVVVV86, L.VVVVV87, L.VVVVV88, L.VVVVV89, L.VVVVV9, L.VVVVV93, L.VVVVV94 ],
               couplings = {(0,42):C.GC_1872,(0,25):C.GC_1484,(0,43):C.GC_1580,(0,44):C.GC_1608,(0,32):C.GC_1452,(0,31):C.GC_1542,(0,28):C.GC_1624,(0,9):C.GC_146,(0,24):C.GC_154,(0,45):C.GC_147,(0,46):C.GC_152,(0,0):C.GC_140,(0,47):C.GC_151,(0,26):C.GC_144,(0,49):C.GC_150,(0,30):C.GC_1930,(0,17):C.GC_591,(0,33):C.GC_588,(0,23):C.GC_587,(0,48):C.GC_586,(0,12):C.GC_238,(0,11):C.GC_239,(0,20):C.GC_235,(0,18):C.GC_242,(0,13):C.GC_149,(0,14):C.GC_155,(0,27):C.GC_584,(0,19):C.GC_631,(0,22):C.GC_153,(0,21):C.GC_585,(0,36):C.GC_626,(0,37):C.GC_589,(0,29):C.GC_141,(0,34):C.GC_143,(0,35):C.GC_1954,(0,6):C.GC_1458,(0,5):C.GC_1556,(0,16):C.GC_1929,(0,38):C.GC_1482,(0,40):C.GC_1578,(0,39):C.GC_1606,(0,8):C.GC_1873,(0,3):C.GC_1483,(0,1):C.GC_1485,(0,2):C.GC_1579,(0,7):C.GC_1581,(0,10):C.GC_1609,(0,4):C.GC_1607,(0,41):C.GC_1953,(0,15):C.GC_1955})

V_414 = Vertex(name = 'V_414',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV108, L.VVVVV110, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV160, L.VVVVV161, L.VVVVV52, L.VVVVV53, L.VVVVV58 ],
               couplings = {(0,6):C.GC_241,(0,7):C.GC_232,(0,10):C.GC_229,(0,9):C.GC_627,(0,13):C.GC_629,(0,11):C.GC_240,(0,12):C.GC_1961,(0,2):C.GC_1489,(0,0):C.GC_1490,(0,1):C.GC_1584,(0,4):C.GC_1586,(0,5):C.GC_1614,(0,3):C.GC_1612,(0,8):C.GC_1959})

V_415 = Vertex(name = 'V_415',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS108, L.VVVVS109, L.VVVVS110, L.VVVVS116, L.VVVVS122, L.VVVVS153, L.VVVVS154, L.VVVVS218, L.VVVVS219, L.VVVVS249, L.VVVVS45, L.VVVVS46, L.VVVVS55, L.VVVVS58, L.VVVVS6, L.VVVVS8 ],
               couplings = {(0,6):C.GC_926,(0,7):C.GC_1095,(0,14):C.GC_1090,(0,13):C.GC_1226,(0,5):C.GC_1232,(0,4):C.GC_1352,(0,15):C.GC_1217,(0,0):C.GC_1659,(0,16):C.GC_1346,(0,9):C.GC_1660,(0,12):C.GC_1661,(0,8):C.GC_1129,(0,10):C.GC_1223,(0,3):C.GC_1093,(0,1):C.GC_1682,(0,2):C.GC_1355,(0,11):C.GC_1349})

V_416 = Vertex(name = 'V_416',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS108, L.VVVVS109, L.VVVVS219, L.VVVVS45, L.VVVVS46 ],
               couplings = {(0,2):C.GC_1665,(0,4):C.GC_1664,(0,0):C.GC_1688,(0,1):C.GC_1377,(0,3):C.GC_1372})

V_417 = Vertex(name = 'V_417',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV131, L.VVVVV132, L.VVVVV133, L.VVVVV149, L.VVVVV154, L.VVVVV158, L.VVVVV162, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV32, L.VVVVV63, L.VVVVV66, L.VVVVV67, L.VVVVV71, L.VVVVV72, L.VVVVV73, L.VVVVV75, L.VVVVV83, L.VVVVV85, L.VVVVV95, L.VVVVV96, L.VVVVV97, L.VVVVV98 ],
               couplings = {(0,24):C.GC_1952,(0,25):C.GC_1907,(0,14):C.GC_697,(0,29):C.GC_373,(0,28):C.GC_523,(0,15):C.GC_364,(0,13):C.GC_527,(0,27):C.GC_371,(0,26):C.GC_521,(0,16):C.GC_518,(0,12):C.GC_696,(0,10):C.GC_733,(0,20):C.GC_1451,(0,19):C.GC_1486,(0,21):C.GC_1539,(0,17):C.GC_1582,(0,9):C.GC_727,(0,11):C.GC_698,(0,5):C.GC_1908,(0,3):C.GC_1932,(0,6):C.GC_1492,(0,7):C.GC_1540,(0,4):C.GC_1541,(0,8):C.GC_1589,(0,2):C.GC_1623,(0,23):C.GC_1931,(0,18):C.GC_1610,(0,22):C.GC_1621,(0,1):C.GC_1934,(0,0):C.GC_1622})

V_418 = Vertex(name = 'V_418',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV132, L.VVVVV158, L.VVVVV162 ],
               couplings = {(0,8):C.GC_729,(0,7):C.GC_731,(0,5):C.GC_1837,(0,3):C.GC_1939,(0,6):C.GC_1550,(0,4):C.GC_1552,(0,2):C.GC_1626,(0,1):C.GC_1937,(0,0):C.GC_1625})

V_419 = Vertex(name = 'V_419',
               particles = [ P.a, P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS147 ],
               couplings = {(0,0):C.GC_767})

V_420 = Vertex(name = 'V_420',
               particles = [ P.a, P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS147 ],
               couplings = {(0,0):C.GC_767})

V_421 = Vertex(name = 'V_421',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS191, L.VVVSS192, L.VVVSS40, L.VVVSS95 ],
               couplings = {(0,2):C.GC_361,(0,1):C.GC_511,(0,0):C.GC_638,(0,3):C.GC_837})

V_422 = Vertex(name = 'V_422',
               particles = [ P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS191, L.VVVSS192, L.VVVSS40, L.VVVSS95 ],
               couplings = {(0,2):C.GC_361,(0,1):C.GC_511,(0,0):C.GC_638,(0,3):C.GC_837})

V_423 = Vertex(name = 'V_423',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172 ],
               couplings = {(0,0):C.GC_769})

V_424 = Vertex(name = 'V_424',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS172 ],
               couplings = {(0,0):C.GC_769})

V_425 = Vertex(name = 'V_425',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS154, L.VVVVS155, L.VVVVS262 ],
               couplings = {(0,1):C.GC_1032,(0,0):C.GC_1038,(0,2):C.GC_1036})

V_426 = Vertex(name = 'V_426',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS262 ],
               couplings = {(0,0):C.GC_1124})

V_427 = Vertex(name = 'V_427',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV144, L.VVVVV2, L.VVVVV26, L.VVVVV4, L.VVVVV47, L.VVVVV48, L.VVVVV5, L.VVVVV55, L.VVVVV56, L.VVVVV80, L.VVVVV82 ],
               couplings = {(0,4):C.GC_780,(0,2):C.GC_151,(0,7):C.GC_583,(0,3):C.GC_145,(0,5):C.GC_148,(0,10):C.GC_590,(0,6):C.GC_592,(0,8):C.GC_812,(0,1):C.GC_810,(0,9):C.GC_781,(0,11):C.GC_142,(0,0):C.GC_779})

V_428 = Vertex(name = 'V_428',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV56 ],
               couplings = {(0,1):C.GC_808,(0,0):C.GC_806})

