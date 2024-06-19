# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Wed 19 Jun 2024 14:43:33


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS6 ],
             couplings = {(0,0):C.GC_526,(0,1):C.GC_12})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS6 ],
             couplings = {(0,0):C.GC_440})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_3243})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_523})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_523})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV37, L.VVVV85, L.VVVV86 ],
             couplings = {(1,1):C.GC_525,(0,0):C.GC_525,(2,2):C.GC_525})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_4972})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ta__plus__, P.ta__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_4974})

V_9 = Vertex(name = 'V_9',
             particles = [ P.t__tilde__, P.t, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_4973})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_26})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS10, L.VVSS13, L.VVSS14, L.VVSS21, L.VVSS22, L.VVSS4, L.VVSS7 ],
              couplings = {(0,0):C.GC_5,(0,5):C.GC_4723,(0,1):C.GC_1150,(0,3):C.GC_1,(0,6):C.GC_350,(0,4):C.GC_2,(0,2):C.GC_4040})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS10, L.VVSS14, L.VVSS21, L.VVSS22, L.VVSS4 ],
              couplings = {(0,0):C.GC_405,(0,4):C.GC_4765,(0,2):C.GC_398,(0,3):C.GC_165,(0,1):C.GC_4104})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_3381})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV113, L.VVVV115, L.VVVV13, L.VVVV16, L.VVVV2, L.VVVV28, L.VVVV29, L.VVVV34, L.VVVV36, L.VVVV39, L.VVVV41, L.VVVV42, L.VVVV47, L.VVVV5, L.VVVV62, L.VVVV63, L.VVVV84, L.VVVV89 ],
              couplings = {(0,6):C.GC_4109,(0,5):C.GC_4124,(0,3):C.GC_490,(0,15):C.GC_2427,(0,4):C.GC_21,(0,13):C.GC_2289,(0,7):C.GC_494,(0,8):C.GC_2431,(0,2):C.GC_2765,(0,11):C.GC_2766,(0,10):C.GC_2943,(0,0):C.GC_2940,(0,14):C.GC_478,(0,1):C.GC_2764,(0,9):C.GC_4785,(0,16):C.GC_60,(0,12):C.GC_4802,(0,17):C.GC_4784})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV115, L.VVVV29, L.VVVV39, L.VVVV42, L.VVVV89 ],
              couplings = {(0,1):C.GC_4133,(0,3):C.GC_2938,(0,0):C.GC_2935,(0,2):C.GC_4805,(0,4):C.GC_4804})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_1573})

V_17 = Vertex(name = 'V_17',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV100, L.VVVV11, L.VVVV111, L.VVVV113, L.VVVV118, L.VVVV31, L.VVVV36, L.VVVV38, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV6, L.VVVV64, L.VVVV77, L.VVVV80, L.VVVV84, L.VVVV98, L.VVVV99 ],
              couplings = {(0,13):C.GC_4037,(0,14):C.GC_4086,(0,12):C.GC_513,(0,11):C.GC_15,(0,1):C.GC_13,(0,6):C.GC_503,(0,9):C.GC_14,(0,4):C.GC_16,(0,2):C.GC_471,(0,3):C.GC_483,(0,17):C.GC_4034,(0,0):C.GC_4036,(0,16):C.GC_4088,(0,5):C.GC_4083,(0,8):C.GC_4035,(0,15):C.GC_1151,(0,7):C.GC_4964,(0,10):C.GC_4192})

V_18 = Vertex(name = 'V_18',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV118, L.VVVV38, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV77, L.VVVV99 ],
              couplings = {(0,5):C.GC_4095,(0,3):C.GC_460,(0,0):C.GC_467,(0,6):C.GC_4069,(0,2):C.GC_4065,(0,1):C.GC_4965,(0,4):C.GC_4193})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV110, L.VVVV112, L.VVVV116, L.VVVV17, L.VVVV19, L.VVVV20, L.VVVV22, L.VVVV23, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV44, L.VVVV45, L.VVVV54, L.VVVV55, L.VVVV59, L.VVVV65, L.VVVV70, L.VVVV71, L.VVVV8, L.VVVV87, L.VVVV9, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV94, L.VVVV95, L.VVVV96, L.VVVV97 ],
              couplings = {(0,19):C.GC_3933,(0,18):C.GC_3944,(0,5):C.GC_4042,(0,4):C.GC_4079,(0,15):C.GC_4821,(0,14):C.GC_4839,(0,17):C.GC_2283,(0,0):C.GC_2490,(0,8):C.GC_2259,(0,9):C.GC_2279,(0,16):C.GC_2269,(0,22):C.GC_2036,(0,20):C.GC_2037,(0,6):C.GC_2265,(0,11):C.GC_2489,(0,1):C.GC_2751,(0,3):C.GC_2491,(0,2):C.GC_2744,(0,30):C.GC_3934,(0,29):C.GC_4750,(0,28):C.GC_4043,(0,25):C.GC_4820,(0,27):C.GC_4129,(0,26):C.GC_4786,(0,12):C.GC_4073,(0,7):C.GC_4806,(0,13):C.GC_3939,(0,23):C.GC_3932,(0,24):C.GC_4041,(0,10):C.GC_4787,(0,21):C.GC_1625})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV116, L.VVVV19, L.VVVV26, L.VVVV27, L.VVVV55, L.VVVV71, L.VVVV90, L.VVVV91, L.VVVV92, L.VVVV93, L.VVVV95, L.VVVV97 ],
              couplings = {(0,5):C.GC_3949,(0,1):C.GC_4094,(0,4):C.GC_4845,(0,3):C.GC_2746,(0,0):C.GC_2748,(0,11):C.GC_3946,(0,10):C.GC_4081,(0,8):C.GC_4161,(0,9):C.GC_4803,(0,6):C.GC_3943,(0,7):C.GC_4077,(0,2):C.GC_4801})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS12, L.VVSS13, L.VVSS14, L.VVSS16, L.VVSS21, L.VVSS22, L.VVSS7 ],
              couplings = {(0,0):C.GC_2179,(0,3):C.GC_4861,(0,1):C.GC_2784,(0,4):C.GC_2753,(0,6):C.GC_2843,(0,5):C.GC_2755,(0,2):C.GC_4863})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS14, L.VVSS16, L.VVSS21, L.VVSS22 ],
              couplings = {(0,1):C.GC_4884,(0,2):C.GC_2852,(0,3):C.GC_2844,(0,0):C.GC_4889})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_4563})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV100, L.VVVV101, L.VVVV102, L.VVVV103, L.VVVV104, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV113, L.VVVV115, L.VVVV13, L.VVVV15, L.VVVV16, L.VVVV30, L.VVVV32, L.VVVV33, L.VVVV35, L.VVVV36, L.VVVV38, L.VVVV39, L.VVVV4, L.VVVV40, L.VVVV41, L.VVVV42, L.VVVV43, L.VVVV47, L.VVVV48, L.VVVV5, L.VVVV56, L.VVVV57, L.VVVV62, L.VVVV63, L.VVVV75, L.VVVV76, L.VVVV78, L.VVVV79, L.VVVV80, L.VVVV82, L.VVVV83, L.VVVV84, L.VVVV89, L.VVVV99 ],
              couplings = {(0,35):C.GC_3935,(0,32):C.GC_4046,(0,13):C.GC_4166,(0,36):C.GC_4756,(0,38):C.GC_4110,(0,34):C.GC_4125,(0,37):C.GC_4148,(0,33):C.GC_4157,(0,31):C.GC_504,(0,12):C.GC_2415,(0,27):C.GC_20,(0,17):C.GC_514,(0,20):C.GC_2290,(0,16):C.GC_2421,(0,10):C.GC_2762,(0,23):C.GC_2763,(0,22):C.GC_2947,(0,8):C.GC_2954,(0,30):C.GC_2418,(0,9):C.GC_2761,(0,19):C.GC_4858,(0,3):C.GC_3947,(0,29):C.GC_4044,(0,1):C.GC_4089,(0,0):C.GC_4727,(0,2):C.GC_4111,(0,4):C.GC_4836,(0,41):C.GC_4149,(0,11):C.GC_3937,(0,26):C.GC_4084,(0,15):C.GC_4120,(0,5):C.GC_3931,(0,7):C.GC_4045,(0,6):C.GC_4108,(0,14):C.GC_4153,(0,21):C.GC_4147,(0,28):C.GC_3930,(0,39):C.GC_1195,(0,18):C.GC_4966,(0,25):C.GC_4878,(0,40):C.GC_4859,(0,24):C.GC_4967})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV102, L.VVVV106, L.VVVV107, L.VVVV108, L.VVVV115, L.VVVV30, L.VVVV38, L.VVVV39, L.VVVV40, L.VVVV42, L.VVVV43, L.VVVV56, L.VVVV57, L.VVVV75, L.VVVV79, L.VVVV82, L.VVVV83, L.VVVV89, L.VVVV99 ],
              couplings = {(0,14):C.GC_3950,(0,13):C.GC_4096,(0,5):C.GC_4175,(0,16):C.GC_4134,(0,15):C.GC_4162,(0,9):C.GC_2950,(0,4):C.GC_2948,(0,7):C.GC_4880,(0,12):C.GC_4070,(0,0):C.GC_4127,(0,18):C.GC_4159,(0,1):C.GC_3938,(0,3):C.GC_4066,(0,2):C.GC_4122,(0,8):C.GC_4155,(0,11):C.GC_3942,(0,6):C.GC_4969,(0,17):C.GC_4874,(0,10):C.GC_4968})

V_26 = Vertex(name = 'V_26',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_25})

V_27 = Vertex(name = 'V_27',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_25})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_25})

V_29 = Vertex(name = 'V_29',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_24})

V_30 = Vertex(name = 'V_30',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_24})

V_31 = Vertex(name = 'V_31',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_24})

V_32 = Vertex(name = 'V_32',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_23})

V_33 = Vertex(name = 'V_33',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_23})

V_34 = Vertex(name = 'V_34',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_23})

V_35 = Vertex(name = 'V_35',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_36 = Vertex(name = 'V_36',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_37 = Vertex(name = 'V_37',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_38 = Vertex(name = 'V_38',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_39 = Vertex(name = 'V_39',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_40 = Vertex(name = 'V_40',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_524})

V_41 = Vertex(name = 'V_41',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_42 = Vertex(name = 'V_42',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_43 = Vertex(name = 'V_43',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_44 = Vertex(name = 'V_44',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_45 = Vertex(name = 'V_45',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_46 = Vertex(name = 'V_46',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_47 = Vertex(name = 'V_47',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_48 = Vertex(name = 'V_48',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_49 = Vertex(name = 'V_49',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_50 = Vertex(name = 'V_50',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_51 = Vertex(name = 'V_51',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_52 = Vertex(name = 'V_52',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1551})

V_53 = Vertex(name = 'V_53',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_1572,(0,1):C.GC_2049})

V_54 = Vertex(name = 'V_54',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_1572,(0,1):C.GC_2049})

V_55 = Vertex(name = 'V_55',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_1572,(0,1):C.GC_2049})

V_56 = Vertex(name = 'V_56',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2049})

V_57 = Vertex(name = 'V_57',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2049})

V_58 = Vertex(name = 'V_58',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2049})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2498})

V_60 = Vertex(name = 'V_60',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2498})

V_61 = Vertex(name = 'V_61',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2498})

V_62 = Vertex(name = 'V_62',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2050})

V_63 = Vertex(name = 'V_63',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2050})

V_64 = Vertex(name = 'V_64',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_1571,(0,1):C.GC_2050})

V_65 = Vertex(name = 'V_65',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS6 ],
              couplings = {(0,0):C.GC_8})

V_66 = Vertex(name = 'V_66',
              particles = [ P.G0, P.G0, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS6 ],
              couplings = {(0,0):C.GC_440})

V_67 = Vertex(name = 'V_67',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_7,(0,0):C.GC_423})

V_68 = Vertex(name = 'V_68',
              particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS3 ],
              couplings = {(0,0):C.GC_438})

V_69 = Vertex(name = 'V_69',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_6,(0,0):C.GC_10})

V_70 = Vertex(name = 'V_70',
              particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_439,(0,0):C.GC_411})

V_71 = Vertex(name = 'V_71',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS4 ],
              couplings = {(0,0):C.GC_11})

V_72 = Vertex(name = 'V_72',
              particles = [ P.G0, P.G__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS4 ],
              couplings = {(0,0):C.GC_437})

V_73 = Vertex(name = 'V_73',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS5 ],
              couplings = {(0,1):C.GC_9,(0,0):C.GC_6})

V_74 = Vertex(name = 'V_74',
              particles = [ P.G0, P.G0, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS5 ],
              couplings = {(0,1):C.GC_410,(0,0):C.GC_439})

V_75 = Vertex(name = 'V_75',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS2, L.SSSS3 ],
              couplings = {(0,1):C.GC_7,(0,0):C.GC_423})

V_76 = Vertex(name = 'V_76',
              particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS3 ],
              couplings = {(0,0):C.GC_438})

V_77 = Vertex(name = 'V_77',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_3785,(0,1):C.GC_4367})

V_78 = Vertex(name = 'V_78',
              particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS7 ],
              couplings = {(0,0):C.GC_4415})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_3596,(0,0):C.GC_3597})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_4416,(0,0):C.GC_3775})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_4365})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.G0, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_4414})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_4367,(0,0):C.GC_3785})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.G__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_4415})

V_85 = Vertex(name = 'V_85',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS14, L.VVSS4 ],
              couplings = {(0,1):C.GC_4038,(0,0):C.GC_4039})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS14, L.VVSS4 ],
              couplings = {(0,1):C.GC_4766,(0,0):C.GC_4099})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_3785,(0,1):C.GC_4367})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS7 ],
              couplings = {(0,0):C.GC_4415})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_3597,(0,1):C.GC_3596})

V_90 = Vertex(name = 'V_90',
              particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1, L.VSSS7 ],
              couplings = {(0,0):C.GC_3775,(0,1):C.GC_4416})

V_91 = Vertex(name = 'V_91',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_4366})

V_92 = Vertex(name = 'V_92',
              particles = [ P.W__plus__, P.G0, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_4413})

V_93 = Vertex(name = 'V_93',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS2, L.VSSS3 ],
              couplings = {(0,1):C.GC_4367,(0,0):C.GC_3785})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__plus__, P.G__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_4415})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS11, L.VVSS17, L.VVSS2, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS7 ],
              couplings = {(0,0):C.GC_372,(0,1):C.GC_4038,(0,2):C.GC_4039,(0,3):C.GC_3,(0,4):C.GC_191,(0,6):C.GC_350,(0,5):C.GC_2})

V_96 = Vertex(name = 'V_96',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS17, L.VVSS2, L.VVSS22 ],
              couplings = {(0,0):C.GC_4766,(0,1):C.GC_4099,(0,2):C.GC_165})

V_97 = Vertex(name = 'V_97',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS14, L.VVSS21, L.VVSS22, L.VVSS4, L.VVSS7 ],
              couplings = {(0,3):C.GC_4723,(0,1):C.GC_191,(0,4):C.GC_350,(0,2):C.GC_2,(0,0):C.GC_4104})

V_98 = Vertex(name = 'V_98',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS22, L.VVSS4 ],
              couplings = {(0,1):C.GC_4765,(0,0):C.GC_165})

V_99 = Vertex(name = 'V_99',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS11, L.VVSS20, L.VVSS3 ],
              couplings = {(0,0):C.GC_373,(0,2):C.GC_4722,(0,1):C.GC_4})

V_100 = Vertex(name = 'V_100',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_4767})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS26, L.VVVS29, L.VVVS4, L.VVVS41, L.VVVS45, L.VVVS59 ],
               couplings = {(0,6):C.GC_3752,(0,3):C.GC_3745,(0,5):C.GC_3594,(0,4):C.GC_3668,(0,2):C.GC_3593,(0,0):C.GC_4182,(0,1):C.GC_4181})

V_102 = Vertex(name = 'V_102',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS26, L.VVVS29 ],
               couplings = {(0,2):C.GC_3658,(0,0):C.GC_4187,(0,1):C.GC_4931})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS4 ],
               couplings = {(0,1):C.GC_4038,(0,0):C.GC_4039})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS4 ],
               couplings = {(0,1):C.GC_4766,(0,0):C.GC_4099})

V_105 = Vertex(name = 'V_105',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS17, L.VVVS19, L.VVVS24, L.VVVS38, L.VVVS39, L.VVVS64 ],
               couplings = {(0,6):C.GC_3753,(0,5):C.GC_3595,(0,4):C.GC_3668,(0,0):C.GC_3745,(0,2):C.GC_3593,(0,1):C.GC_4181,(0,3):C.GC_4182})

V_106 = Vertex(name = 'V_106',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS19, L.VVVS24 ],
               couplings = {(0,1):C.GC_3658,(0,0):C.GC_4931,(0,2):C.GC_4187})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS8 ],
               couplings = {(0,0):C.GC_4450})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS8 ],
               couplings = {(0,0):C.GC_4540})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,1):C.GC_4448,(0,0):C.GC_4528})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS3 ],
               couplings = {(0,0):C.GC_4538})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS5 ],
               couplings = {(0,0):C.GC_4447})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS5 ],
               couplings = {(0,0):C.GC_4537})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS6 ],
               couplings = {(0,1):C.GC_4449,(0,0):C.GC_4446})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS2, L.VSSS6 ],
               couplings = {(0,1):C.GC_4527,(0,0):C.GC_4539})

V_115 = Vertex(name = 'V_115',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS11, L.VVSS18, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS6, L.VVSS8 ],
               couplings = {(0,1):C.GC_375,(0,7):C.GC_2177,(0,0):C.GC_4760,(0,2):C.GC_4725,(0,3):C.GC_18,(0,4):C.GC_2198,(0,6):C.GC_2126,(0,5):C.GC_2160})

V_116 = Vertex(name = 'V_116',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS18, L.VVSS20 ],
               couplings = {(0,0):C.GC_4769,(0,1):C.GC_2150})

V_117 = Vertex(name = 'V_117',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS15, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS6, L.VVSS8 ],
               couplings = {(0,0):C.GC_374,(0,6):C.GC_2176,(0,1):C.GC_4724,(0,2):C.GC_17,(0,3):C.GC_2199,(0,5):C.GC_2125,(0,4):C.GC_2159})

V_118 = Vertex(name = 'V_118',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS15, L.VVSS20 ],
               couplings = {(0,0):C.GC_4770,(0,1):C.GC_2149})

V_119 = Vertex(name = 'V_119',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1, L.VVSS11, L.VVSS18, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS6, L.VVSS8 ],
               couplings = {(0,1):C.GC_375,(0,7):C.GC_2177,(0,0):C.GC_4760,(0,2):C.GC_4725,(0,3):C.GC_18,(0,4):C.GC_2198,(0,6):C.GC_2126,(0,5):C.GC_2160})

V_120 = Vertex(name = 'V_120',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS18, L.VVSS20 ],
               couplings = {(0,0):C.GC_4769,(0,1):C.GC_2148})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS15, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS6, L.VVSS8 ],
               couplings = {(0,0):C.GC_376,(0,6):C.GC_2178,(0,1):C.GC_4726,(0,2):C.GC_19,(0,3):C.GC_2197,(0,5):C.GC_2127,(0,4):C.GC_2161})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS15, L.VVSS20 ],
               couplings = {(0,0):C.GC_4768,(0,1):C.GC_2149})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS15, L.VVVS16, L.VVVS26, L.VVVS29, L.VVVS34, L.VVVS41, L.VVVS43, L.VVVS45, L.VVVS5, L.VVVS58, L.VVVS59, L.VVVS9 ],
               couplings = {(0,10):C.GC_3755,(0,9):C.GC_3182,(0,4):C.GC_4492,(0,8):C.GC_3152,(0,6):C.GC_3166,(0,5):C.GC_3191,(0,7):C.GC_3602,(0,3):C.GC_3174,(0,11):C.GC_4511,(0,1):C.GC_4445,(0,0):C.GC_4944,(0,2):C.GC_4942})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS26 ],
               couplings = {(0,0):C.GC_4485,(0,1):C.GC_4945})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS25, L.VVVS32, L.VVVS33, L.VVVS44, L.VVVS45, L.VVVS46, L.VVVS50, L.VVVS52, L.VVVS56, L.VVVS57, L.VVVS60 ],
               couplings = {(0,9):C.GC_3754,(0,7):C.GC_3858,(0,11):C.GC_3603,(0,10):C.GC_3088,(0,8):C.GC_3183,(0,4):C.GC_3601,(0,3):C.GC_3802,(0,0):C.GC_3153,(0,6):C.GC_3089,(0,5):C.GC_3165,(0,2):C.GC_3087,(0,1):C.GC_4943})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS25, L.VVVS32, L.VVVS33, L.VVVS44, L.VVVS46, L.VVVS57, L.VVVS60 ],
               couplings = {(0,6):C.GC_3771,(0,5):C.GC_3216,(0,3):C.GC_3762,(0,2):C.GC_3860,(0,4):C.GC_3192,(0,1):C.GC_3175,(0,0):C.GC_4946})

V_127 = Vertex(name = 'V_127',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS19, L.VVSS21, L.VVSS22, L.VVSS7 ],
               couplings = {(0,0):C.GC_2179,(0,1):C.GC_4862,(0,2):C.GC_2851,(0,4):C.GC_2607,(0,3):C.GC_2754})

V_128 = Vertex(name = 'V_128',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS19, L.VVSS22 ],
               couplings = {(0,0):C.GC_4890,(0,1):C.GC_2626})

V_129 = Vertex(name = 'V_129',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS14, L.VVSS21, L.VVSS22, L.VVSS4, L.VVSS7 ],
               couplings = {(0,0):C.GC_2180,(0,4):C.GC_4860,(0,2):C.GC_2850,(0,5):C.GC_2606,(0,3):C.GC_2754,(0,1):C.GC_4885})

V_130 = Vertex(name = 'V_130',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS22, L.VVSS4 ],
               couplings = {(0,1):C.GC_4888,(0,0):C.GC_2627})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS12, L.VVVS13, L.VVVS17, L.VVVS19, L.VVVS24, L.VVVS28, L.VVVS31, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS47, L.VVVS61, L.VVVS64, L.VVVS65 ],
               couplings = {(0,13):C.GC_4516,(0,14):C.GC_3184,(0,12):C.GC_3897,(0,9):C.GC_4601,(0,11):C.GC_3193,(0,8):C.GC_3901,(0,2):C.GC_3154,(0,0):C.GC_3746,(0,7):C.GC_3176,(0,6):C.GC_4442,(0,1):C.GC_3883,(0,4):C.GC_3892,(0,10):C.GC_4498,(0,3):C.GC_4947,(0,5):C.GC_4950})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS28, L.VVVS39 ],
               couplings = {(0,2):C.GC_4444,(0,1):C.GC_3659,(0,0):C.GC_4953})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS12, L.VVVS13, L.VVVS17, L.VVVS19, L.VVVS24, L.VVVS28, L.VVVS31, L.VVVS38, L.VVVS39, L.VVVS40, L.VVVS47, L.VVVS61, L.VVVS64, L.VVVS65 ],
               couplings = {(0,13):C.GC_4516,(0,14):C.GC_3184,(0,12):C.GC_3897,(0,9):C.GC_4600,(0,11):C.GC_3193,(0,8):C.GC_3901,(0,2):C.GC_3154,(0,0):C.GC_3746,(0,7):C.GC_3176,(0,6):C.GC_4442,(0,1):C.GC_3883,(0,4):C.GC_3892,(0,10):C.GC_4498,(0,3):C.GC_4947,(0,5):C.GC_4950})

V_134 = Vertex(name = 'V_134',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS17, L.VVVS28, L.VVVS39 ],
               couplings = {(0,2):C.GC_4444,(0,1):C.GC_3659,(0,0):C.GC_4953})

V_135 = Vertex(name = 'V_135',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS11, L.VVVS27, L.VVVS30, L.VVVS42, L.VVVS54 ],
               couplings = {(0,4):C.GC_4604,(0,3):C.GC_4650,(0,0):C.GC_4596,(0,2):C.GC_4602,(0,1):C.GC_4960})

V_136 = Vertex(name = 'V_136',
               particles = [ P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS27, L.VVVS30 ],
               couplings = {(0,1):C.GC_4641,(0,0):C.GC_4961})

V_137 = Vertex(name = 'V_137',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV105, L.VVVV109, L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV50, L.VVVV68, L.VVVV81, L.VVVV88 ],
               couplings = {(0,7):C.GC_4899,(0,6):C.GC_3076,(0,4):C.GC_3033,(0,3):C.GC_3032,(0,2):C.GC_3086,(0,0):C.GC_4905,(0,5):C.GC_4915,(0,1):C.GC_4906,(0,8):C.GC_4970})

V_138 = Vertex(name = 'V_138',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV105, L.VVVV109, L.VVVV117, L.VVVV88 ],
               couplings = {(0,2):C.GC_3085,(0,0):C.GC_4917,(0,1):C.GC_4916,(0,3):C.GC_4971})

V_139 = Vertex(name = 'V_139',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS21, L.VVSS22, L.VVSS7 ],
               couplings = {(0,0):C.GC_2180,(0,1):C.GC_2758,(0,3):C.GC_2887,(0,2):C.GC_2760})

V_140 = Vertex(name = 'V_140',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS21, L.VVSS22 ],
               couplings = {(0,0):C.GC_2897,(0,1):C.GC_2830})

V_141 = Vertex(name = 'V_141',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_307,(0,5):C.GC_2377,(0,0):C.GC_2757,(0,2):C.GC_219,(0,4):C.GC_2638,(0,3):C.GC_2340,(0,1):C.GC_2756})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS21, L.VVSS22 ],
               couplings = {(0,0):C.GC_2879,(0,1):C.GC_2862})

V_143 = Vertex(name = 'V_143',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV111, L.VVVV113, L.VVVV114, L.VVVV115, L.VVVV117, L.VVVV118, L.VVVV13, L.VVVV14, L.VVVV16, L.VVVV2, L.VVVV28, L.VVVV34, L.VVVV35, L.VVVV36, L.VVVV39, L.VVVV4, L.VVVV41, L.VVVV42, L.VVVV47, L.VVVV6, L.VVVV62, L.VVVV64, L.VVVV68, L.VVVV89 ],
               couplings = {(0,11):C.GC_4900,(0,9):C.GC_3077,(0,23):C.GC_2952,(0,22):C.GC_2422,(0,10):C.GC_22,(0,8):C.GC_2767,(0,20):C.GC_2291,(0,0):C.GC_2293,(0,12):C.GC_495,(0,14):C.GC_2946,(0,16):C.GC_2480,(0,13):C.GC_2487,(0,7):C.GC_3035,(0,18):C.GC_3036,(0,5):C.GC_2768,(0,6):C.GC_2292,(0,17):C.GC_3080,(0,3):C.GC_2956,(0,1):C.GC_2433,(0,2):C.GC_3084,(0,21):C.GC_3079,(0,4):C.GC_3034,(0,15):C.GC_4909,(0,19):C.GC_4920,(0,24):C.GC_4910})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV115, L.VVVV117, L.VVVV118, L.VVVV39, L.VVVV42, L.VVVV89 ],
               couplings = {(0,4):C.GC_3082,(0,1):C.GC_2955,(0,2):C.GC_2429,(0,0):C.GC_3081,(0,3):C.GC_4921,(0,5):C.GC_4914})

V_145 = Vertex(name = 'V_145',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV18, L.VVVV21, L.VVVV46, L.VVVV49, L.VVVV51, L.VVVV52, L.VVVV53, L.VVVV58, L.VVVV67, L.VVVV68, L.VVVV69, L.VVVV7, L.VVVV72, L.VVVV73, L.VVVV74, L.VVVV90, L.VVVV97 ],
               couplings = {(0,16):C.GC_3945,(0,4):C.GC_4080,(0,18):C.GC_4173,(0,17):C.GC_4178,(0,5):C.GC_3023,(0,11):C.GC_2270,(0,13):C.GC_3022,(0,14):C.GC_2478,(0,3):C.GC_2957,(0,15):C.GC_2038,(0,12):C.GC_3025,(0,0):C.GC_2436,(0,2):C.GC_2958,(0,1):C.GC_3031,(0,20):C.GC_4908,(0,8):C.GC_3940,(0,6):C.GC_4074,(0,7):C.GC_4901,(0,10):C.GC_4170,(0,9):C.GC_4177,(0,19):C.GC_4907})

V_146 = Vertex(name = 'V_146',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV117, L.VVVV90, L.VVVV97 ],
               couplings = {(0,0):C.GC_3030,(0,2):C.GC_4919,(0,1):C.GC_4918})

V_147 = Vertex(name = 'V_147',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS21, L.VVSS22, L.VVSS7 ],
               couplings = {(0,0):C.GC_2180,(0,1):C.GC_2836,(0,3):C.GC_2886,(0,2):C.GC_2759})

V_148 = Vertex(name = 'V_148',
               particles = [ P.a, P.a, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS22 ],
               couplings = {(0,0):C.GC_2829})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS12, L.VVSS21, L.VVSS22, L.VVSS7 ],
               couplings = {(0,0):C.GC_2179,(0,1):C.GC_2837,(0,3):C.GC_2888,(0,2):C.GC_2759})

V_150 = Vertex(name = 'V_150',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS22 ],
               couplings = {(0,0):C.GC_2828})

V_151 = Vertex(name = 'V_151',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,6):C.GC_307,(0,5):C.GC_2377,(0,0):C.GC_2878,(0,2):C.GC_219,(0,4):C.GC_2214,(0,3):C.GC_2340,(0,1):C.GC_2861})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS22 ],
               couplings = {(0,0):C.GC_2488})

V_153 = Vertex(name = 'V_153',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS6, L.VVSS7, L.VVSS8, L.VVSS9 ],
               couplings = {(0,7):C.GC_306,(0,6):C.GC_2378,(0,0):C.GC_2858,(0,1):C.GC_2877,(0,3):C.GC_220,(0,5):C.GC_2214,(0,4):C.GC_2341,(0,2):C.GC_2863})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS22 ],
               couplings = {(0,0):C.GC_2488})

V_155 = Vertex(name = 'V_155',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS34, L.VVVS49, L.VVVS9 ],
               couplings = {(0,2):C.GC_3185,(0,1):C.GC_4491,(0,3):C.GC_4510,(0,0):C.GC_4484})

V_156 = Vertex(name = 'V_156',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16 ],
               couplings = {(0,0):C.GC_4443})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS23, L.VVVS3, L.VVVS33, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS50, L.VVVS51, L.VVVS6, L.VVVS7 ],
               couplings = {(0,10):C.GC_4611,(0,3):C.GC_3719,(0,11):C.GC_3842,(0,5):C.GC_4562,(0,6):C.GC_4500,(0,7):C.GC_3733,(0,9):C.GC_3849,(0,8):C.GC_4197,(0,4):C.GC_3199,(0,12):C.GC_3679,(0,13):C.GC_3824,(0,0):C.GC_4194,(0,2):C.GC_3704,(0,1):C.GC_3835})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18 ],
               couplings = {(0,0):C.GC_3134})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS34, L.VVVS49, L.VVVS9 ],
               couplings = {(0,2):C.GC_3185,(0,1):C.GC_4491,(0,3):C.GC_4510,(0,0):C.GC_4484})

V_160 = Vertex(name = 'V_160',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS16 ],
               couplings = {(0,0):C.GC_4443})

V_161 = Vertex(name = 'V_161',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18, L.VVVS19, L.VVVS20, L.VVVS23, L.VVVS3, L.VVVS33, L.VVVS35, L.VVVS36, L.VVVS37, L.VVVS38, L.VVVS50, L.VVVS51, L.VVVS6, L.VVVS7 ],
               couplings = {(0,10):C.GC_4611,(0,3):C.GC_3719,(0,11):C.GC_3842,(0,5):C.GC_4562,(0,6):C.GC_4499,(0,7):C.GC_3733,(0,9):C.GC_3849,(0,8):C.GC_4197,(0,4):C.GC_3199,(0,12):C.GC_3679,(0,13):C.GC_3824,(0,0):C.GC_4194,(0,2):C.GC_3704,(0,1):C.GC_3835})

V_162 = Vertex(name = 'V_162',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVS18 ],
               couplings = {(0,0):C.GC_3134})

V_163 = Vertex(name = 'V_163',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS16, L.VVVS34, L.VVVS49, L.VVVS9 ],
               couplings = {(0,2):C.GC_4603,(0,1):C.GC_4649,(0,3):C.GC_4657,(0,0):C.GC_4648})

V_164 = Vertex(name = 'V_164',
               particles = [ P.a, P.a, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS16 ],
               couplings = {(0,0):C.GC_4642})

V_165 = Vertex(name = 'V_165',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS10, L.VVVS12, L.VVVS14, L.VVVS19, L.VVVS21, L.VVVS38, L.VVVS61, L.VVVS63, L.VVVS8 ],
               couplings = {(0,4):C.GC_3720,(0,7):C.GC_3843,(0,6):C.GC_3921,(0,5):C.GC_4656,(0,0):C.GC_4608,(0,8):C.GC_3680,(0,2):C.GC_3825,(0,1):C.GC_3914,(0,3):C.GC_4561})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS19 ],
               couplings = {(0,0):C.GC_4652})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS20, L.VVVS22, L.VVVS23, L.VVVS35, L.VVVS36, L.VVVS39, L.VVVS55, L.VVVS6, L.VVVS63 ],
               couplings = {(0,8):C.GC_3092,(0,6):C.GC_3207,(0,1):C.GC_3599,(0,2):C.GC_3718,(0,3):C.GC_3091,(0,4):C.GC_3600,(0,5):C.GC_3692,(0,7):C.GC_3678,(0,0):C.GC_3598})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS20, L.VVVS22, L.VVVS35, L.VVVS36, L.VVVS63 ],
               couplings = {(0,4):C.GC_3218,(0,1):C.GC_3767,(0,2):C.GC_3212,(0,3):C.GC_3731,(0,0):C.GC_3702})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS48 ],
               couplings = {(0,0):C.GC_4559})

V_170 = Vertex(name = 'V_170',
               particles = [ P.a, P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS48 ],
               couplings = {(0,0):C.GC_4618})

V_171 = Vertex(name = 'V_171',
               particles = [ P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS22, L.VVVS39, L.VVVS62, L.VVVS64 ],
               couplings = {(0,0):C.GC_3604,(0,3):C.GC_3803,(0,2):C.GC_3910,(0,1):C.GC_4651})

V_172 = Vertex(name = 'V_172',
               particles = [ P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS22, L.VVVS62, L.VVVS64 ],
               couplings = {(0,0):C.GC_3768,(0,2):C.GC_3862,(0,1):C.GC_3927})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS53 ],
               couplings = {(0,0):C.GC_4560})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS53 ],
               couplings = {(0,0):C.GC_4619})

V_175 = Vertex(name = 'V_175',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS9 ],
               couplings = {(0,5):C.GC_304,(0,0):C.GC_2229,(0,1):C.GC_256,(0,2):C.GC_326,(0,4):C.GC_217,(0,3):C.GC_283})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS20 ],
               couplings = {(0,0):C.GC_2034})

V_177 = Vertex(name = 'V_177',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS9 ],
               couplings = {(0,5):C.GC_305,(0,0):C.GC_2230,(0,1):C.GC_255,(0,2):C.GC_325,(0,4):C.GC_216,(0,3):C.GC_284})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS20 ],
               couplings = {(0,0):C.GC_2035})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS9 ],
               couplings = {(0,5):C.GC_304,(0,0):C.GC_2229,(0,1):C.GC_254,(0,2):C.GC_326,(0,4):C.GC_217,(0,3):C.GC_283})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS20 ],
               couplings = {(0,0):C.GC_2034})

V_181 = Vertex(name = 'V_181',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS11, L.VVSS20, L.VVSS21, L.VVSS22, L.VVSS5, L.VVSS9 ],
               couplings = {(0,5):C.GC_303,(0,0):C.GC_2228,(0,1):C.GC_255,(0,2):C.GC_327,(0,4):C.GC_218,(0,3):C.GC_282})

V_182 = Vertex(name = 'V_182',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS20 ],
               couplings = {(0,0):C.GC_2033})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS21, L.VVVS35, L.VVVS38, L.VVVS39, L.VVVS64, L.VVVS8 ],
               couplings = {(0,5):C.GC_3206,(0,1):C.GC_3717,(0,4):C.GC_3090,(0,2):C.GC_3693,(0,3):C.GC_3732,(0,6):C.GC_3677,(0,0):C.GC_3703})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV114, L.VVVV117, L.VVVV14, L.VVVV68 ],
               couplings = {(0,3):C.GC_3083,(0,2):C.GC_3037,(0,1):C.GC_3038,(0,0):C.GC_3078})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV117 ],
               couplings = {(0,0):C.GC_3075})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV114, L.VVVV117, L.VVVV12, L.VVVV14, L.VVVV24, L.VVVV3, L.VVVV60, L.VVVV61, L.VVVV66, L.VVVV68 ],
               couplings = {(0,9):C.GC_3028,(0,4):C.GC_3024,(0,7):C.GC_2271,(0,3):C.GC_2959,(0,5):C.GC_2039,(0,6):C.GC_2479,(0,2):C.GC_2437,(0,8):C.GC_3026,(0,1):C.GC_2960,(0,0):C.GC_3029})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV117 ],
               couplings = {(0,0):C.GC_3027})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS20 ],
               couplings = {(0,0):C.GC_2859})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS6 ],
               couplings = {(0,0):C.GC_424,(0,1):C.GC_156})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS6 ],
               couplings = {(0,0):C.GC_451})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_40,(0,0):C.GC_39})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_412,(0,0):C.GC_452})

V_193 = Vertex(name = 'V_193',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS21 ],
               couplings = {(0,0):C.GC_155})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS21 ],
               couplings = {(0,0):C.GC_453})

V_195 = Vertex(name = 'V_195',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS14, L.VSSSS29 ],
               couplings = {(0,0):C.GC_156,(0,1):C.GC_424})

V_196 = Vertex(name = 'V_196',
               particles = [ P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS14 ],
               couplings = {(0,0):C.GC_451})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_4370,(0,1):C.GC_3787})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_4419})

V_199 = Vertex(name = 'V_199',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_791,(0,1):C.GC_1964})

V_200 = Vertex(name = 'V_200',
               particles = [ P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36 ],
               couplings = {(0,0):C.GC_889})

V_201 = Vertex(name = 'V_201',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS35, L.VVSSS42 ],
               couplings = {(0,1):C.GC_3612,(0,0):C.GC_3610})

V_202 = Vertex(name = 'V_202',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS35, L.VVSSS42 ],
               couplings = {(0,1):C.GC_3777,(0,0):C.GC_4420})

V_203 = Vertex(name = 'V_203',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_1966,(0,1):C.GC_1558,(0,2):C.GC_1569})

V_204 = Vertex(name = 'V_204',
               particles = [ P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_1975,(0,1):C.GC_1952})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS10, L.VSSSS22, L.VSSSS9 ],
               couplings = {(0,1):C.GC_1567,(0,2):C.GC_1561,(0,0):C.GC_1964})

V_206 = Vertex(name = 'V_206',
               particles = [ P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS22, L.VSSSS9 ],
               couplings = {(0,0):C.GC_1950,(0,1):C.GC_1978})

V_207 = Vertex(name = 'V_207',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS2, L.VSSSS20, L.VSSSS7 ],
               couplings = {(0,1):C.GC_1563,(0,0):C.GC_1966,(0,2):C.GC_1564})

V_208 = Vertex(name = 'V_208',
               particles = [ P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS20, L.VSSSS7 ],
               couplings = {(0,0):C.GC_1980,(0,1):C.GC_1947})

V_209 = Vertex(name = 'V_209',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_4369})

V_210 = Vertex(name = 'V_210',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_4418})

V_211 = Vertex(name = 'V_211',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_1560,(0,0):C.GC_1565,(0,2):C.GC_1964})

V_212 = Vertex(name = 'V_212',
               particles = [ P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19 ],
               couplings = {(0,1):C.GC_1977,(0,0):C.GC_1948})

V_213 = Vertex(name = 'V_213',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_4370,(0,1):C.GC_3787})

V_214 = Vertex(name = 'V_214',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14 ],
               couplings = {(0,0):C.GC_4419})

V_215 = Vertex(name = 'V_215',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_793,(0,1):C.GC_1966})

V_216 = Vertex(name = 'V_216',
               particles = [ P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23 ],
               couplings = {(0,0):C.GC_891})

V_217 = Vertex(name = 'V_217',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_3391,(0,2):C.GC_3570,(0,0):C.GC_3390})

V_218 = Vertex(name = 'V_218',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38 ],
               couplings = {(0,1):C.GC_3551,(0,0):C.GC_3584})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_3389,(0,0):C.GC_3571,(0,1):C.GC_3392})

V_220 = Vertex(name = 'V_220',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,1):C.GC_3583,(0,0):C.GC_3552})

V_221 = Vertex(name = 'V_221',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS74 ],
               couplings = {(0,0):C.GC_4051,(0,1):C.GC_4053})

V_222 = Vertex(name = 'V_222',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS74 ],
               couplings = {(0,0):C.GC_4771,(0,1):C.GC_4100})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_4368,(0,1):C.GC_3786})

V_224 = Vertex(name = 'V_224',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_4417})

V_225 = Vertex(name = 'V_225',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36, L.VSSSS5 ],
               couplings = {(0,0):C.GC_792,(0,1):C.GC_1965})

V_226 = Vertex(name = 'V_226',
               particles = [ P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS36 ],
               couplings = {(0,0):C.GC_890})

V_227 = Vertex(name = 'V_227',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_1966,(0,1):C.GC_1558,(0,2):C.GC_1569})

V_228 = Vertex(name = 'V_228',
               particles = [ P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS34, L.VSSSS35 ],
               couplings = {(0,0):C.GC_1975,(0,1):C.GC_1952})

V_229 = Vertex(name = 'V_229',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS21, L.VVSSS44 ],
               couplings = {(0,1):C.GC_3610,(0,0):C.GC_3611})

V_230 = Vertex(name = 'V_230',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS21, L.VVSSS44 ],
               couplings = {(0,1):C.GC_4420,(0,0):C.GC_3776})

V_231 = Vertex(name = 'V_231',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS24, L.VSSSS30, L.VSSSS8 ],
               couplings = {(0,0):C.GC_1562,(0,2):C.GC_1568,(0,1):C.GC_1965})

V_232 = Vertex(name = 'V_232',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS24, L.VSSSS8 ],
               couplings = {(0,0):C.GC_1979,(0,1):C.GC_1951})

V_233 = Vertex(name = 'V_233',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS33, L.VSSSS4 ],
               couplings = {(0,1):C.GC_1570,(0,0):C.GC_1563,(0,2):C.GC_1966})

V_234 = Vertex(name = 'V_234',
               particles = [ P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS11, L.VSSSS33 ],
               couplings = {(0,1):C.GC_1953,(0,0):C.GC_1980})

V_235 = Vertex(name = 'V_235',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_4369})

V_236 = Vertex(name = 'V_236',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7 ],
               couplings = {(0,0):C.GC_4418})

V_237 = Vertex(name = 'V_237',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19, L.VSSSS29 ],
               couplings = {(0,1):C.GC_1559,(0,0):C.GC_1566,(0,2):C.GC_1965})

V_238 = Vertex(name = 'V_238',
               particles = [ P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS18, L.VSSSS19 ],
               couplings = {(0,1):C.GC_1976,(0,0):C.GC_1949})

V_239 = Vertex(name = 'V_239',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS17 ],
               couplings = {(0,0):C.GC_4368,(0,1):C.GC_3786})

V_240 = Vertex(name = 'V_240',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14 ],
               couplings = {(0,0):C.GC_4417})

V_241 = Vertex(name = 'V_241',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23, L.VSSSS32 ],
               couplings = {(0,0):C.GC_793,(0,1):C.GC_1966})

V_242 = Vertex(name = 'V_242',
               particles = [ P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS23 ],
               couplings = {(0,0):C.GC_891})

V_243 = Vertex(name = 'V_243',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS113, L.VVVSS117, L.VVVSS129, L.VVVSS138, L.VVVSS16, L.VVVSS21, L.VVVSS31, L.VVVSS37, L.VVVSS41, L.VVVSS61, L.VVVSS83, L.VVVSS85 ],
               couplings = {(0,3):C.GC_379,(0,8):C.GC_1842,(0,5):C.GC_351,(0,0):C.GC_37,(0,11):C.GC_1793,(0,10):C.GC_1866,(0,2):C.GC_33,(0,4):C.GC_1764,(0,7):C.GC_1575,(0,1):C.GC_193,(0,9):C.GC_4051,(0,6):C.GC_4054})

V_244 = Vertex(name = 'V_244',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS129, L.VVVSS31, L.VVVSS37, L.VVVSS61 ],
               couplings = {(0,0):C.GC_166,(0,2):C.GC_1816,(0,3):C.GC_4771,(0,1):C.GC_4101})

V_245 = Vertex(name = 'V_245',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS24, L.VVSSS26, L.VVSSS57 ],
               couplings = {(0,0):C.GC_3389,(0,1):C.GC_3571,(0,2):C.GC_3393})

V_246 = Vertex(name = 'V_246',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS24, L.VVSSS57 ],
               couplings = {(0,0):C.GC_3583,(0,1):C.GC_3553})

V_247 = Vertex(name = 'V_247',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16 ],
               couplings = {(0,0):C.GC_4250,(0,1):C.GC_3571})

V_248 = Vertex(name = 'V_248',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_4333})

V_249 = Vertex(name = 'V_249',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS3, L.VVSSS32, L.VVSSS5 ],
               couplings = {(0,2):C.GC_3388,(0,0):C.GC_3570,(0,1):C.GC_3391})

V_250 = Vertex(name = 'V_250',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS32, L.VVSSS5 ],
               couplings = {(0,1):C.GC_3582,(0,0):C.GC_3551})

V_251 = Vertex(name = 'V_251',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS8 ],
               couplings = {(0,0):C.GC_4249})

V_252 = Vertex(name = 'V_252',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS8 ],
               couplings = {(0,0):C.GC_4334})

V_253 = Vertex(name = 'V_253',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS15, L.VVSSS59 ],
               couplings = {(0,0):C.GC_4250,(0,1):C.GC_3395})

V_254 = Vertex(name = 'V_254',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS15, L.VVSSS59 ],
               couplings = {(0,0):C.GC_4333,(0,1):C.GC_3571})

V_255 = Vertex(name = 'V_255',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS121, L.VVVVS13, L.VVVVS133, L.VVVVS14, L.VVVVS170, L.VVVVS178, L.VVVVS181, L.VVVVS213, L.VVVVS218, L.VVVVS24, L.VVVVS25, L.VVVVS31 ],
               couplings = {(0,3):C.GC_3508,(0,0):C.GC_3756,(0,10):C.GC_3480,(0,1):C.GC_3747,(0,6):C.GC_3516,(0,7):C.GC_3609,(0,8):C.GC_3670,(0,4):C.GC_3607,(0,11):C.GC_3396,(0,5):C.GC_3492,(0,9):C.GC_4185,(0,2):C.GC_4183})

V_256 = Vertex(name = 'V_256',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS133, L.VVVVS170, L.VVVVS24, L.VVVVS31 ],
               couplings = {(0,1):C.GC_3660,(0,3):C.GC_3500,(0,2):C.GC_4188,(0,0):C.GC_4932})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS147, L.VVVSS4, L.VVVSS47, L.VVVSS62, L.VVVSS65, L.VVVSS79, L.VVVSS95 ],
               couplings = {(0,1):C.GC_1913,(0,2):C.GC_1890,(0,0):C.GC_1556,(0,7):C.GC_1736,(0,6):C.GC_1554,(0,5):C.GC_3971,(0,3):C.GC_3975,(0,4):C.GC_4024})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS47, L.VVVSS65, L.VVVSS79 ],
               couplings = {(0,2):C.GC_1710,(0,1):C.GC_4030,(0,0):C.GC_4014})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS147, L.VVVSS4, L.VVVSS46, L.VVVSS69, L.VVVSS71, L.VVVSS79, L.VVVSS95 ],
               couplings = {(0,1):C.GC_1912,(0,2):C.GC_1892,(0,0):C.GC_1555,(0,7):C.GC_1738,(0,6):C.GC_1552,(0,5):C.GC_3973,(0,3):C.GC_3972,(0,4):C.GC_4022})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS46, L.VVVSS71, L.VVVSS79 ],
               couplings = {(0,2):C.GC_1708,(0,1):C.GC_4012,(0,0):C.GC_4031})

V_261 = Vertex(name = 'V_261',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38, L.VVSSS9 ],
               couplings = {(0,1):C.GC_3394,(0,2):C.GC_3572,(0,0):C.GC_3387})

V_262 = Vertex(name = 'V_262',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS31, L.VVSSS38 ],
               couplings = {(0,1):C.GC_3554,(0,0):C.GC_3581})

V_263 = Vertex(name = 'V_263',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS13, L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,2):C.GC_3389,(0,0):C.GC_3571,(0,1):C.GC_3392})

V_264 = Vertex(name = 'V_264',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS18, L.VVSSS43 ],
               couplings = {(0,1):C.GC_3583,(0,0):C.GC_3552})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS13, L.VVVSS151, L.VVVSS32, L.VVVSS36, L.VVVSS44, L.VVVSS53, L.VVVSS87 ],
               couplings = {(0,2):C.GC_1913,(0,0):C.GC_1556,(0,7):C.GC_1737,(0,1):C.GC_1891,(0,4):C.GC_1553,(0,6):C.GC_3974,(0,3):C.GC_4023,(0,5):C.GC_3970})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS36, L.VVVSS44, L.VVVSS53 ],
               couplings = {(0,0):C.GC_1709,(0,2):C.GC_4013,(0,1):C.GC_4029})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS13, L.VVVSS151, L.VVVSS33, L.VVVSS36, L.VVVSS43, L.VVVSS64, L.VVVSS87 ],
               couplings = {(0,2):C.GC_1914,(0,0):C.GC_1557,(0,7):C.GC_1738,(0,1):C.GC_1892,(0,4):C.GC_1552,(0,6):C.GC_3969,(0,3):C.GC_4022,(0,5):C.GC_3976})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS36, L.VVVSS43, L.VVVSS64 ],
               couplings = {(0,0):C.GC_1708,(0,2):C.GC_4028,(0,1):C.GC_4015})

V_269 = Vertex(name = 'V_269',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS74 ],
               couplings = {(0,0):C.GC_4052,(0,1):C.GC_4054})

V_270 = Vertex(name = 'V_270',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS34, L.VVVSS74 ],
               couplings = {(0,0):C.GC_4772,(0,1):C.GC_4101})

V_271 = Vertex(name = 'V_271',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS125, L.VVVVS136, L.VVVVS174, L.VVVVS179, L.VVVVS18, L.VVVVS183, L.VVVVS188, L.VVVVS22, L.VVVVS52, L.VVVVS57, L.VVVVS62, L.VVVVS68 ],
               couplings = {(0,7):C.GC_3508,(0,0):C.GC_3757,(0,11):C.GC_3480,(0,4):C.GC_3747,(0,3):C.GC_3516,(0,5):C.GC_3609,(0,6):C.GC_3669,(0,1):C.GC_3396,(0,2):C.GC_3493,(0,9):C.GC_3608,(0,8):C.GC_4184,(0,10):C.GC_4186})

V_272 = Vertex(name = 'V_272',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS136, L.VVVVS52, L.VVVVS57, L.VVVVS62 ],
               couplings = {(0,0):C.GC_3500,(0,2):C.GC_3661,(0,1):C.GC_4933,(0,3):C.GC_4189})

V_273 = Vertex(name = 'V_273',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS119, L.VVVVS129, L.VVVVS158, L.VVVVS200, L.VVVVS212, L.VVVVS38, L.VVVVS52, L.VVVVS58, L.VVVVS62 ],
               couplings = {(0,0):C.GC_3386,(0,1):C.GC_3532,(0,2):C.GC_3382,(0,3):C.GC_3384,(0,4):C.GC_3540,(0,5):C.GC_3525,(0,7):C.GC_3383,(0,6):C.GC_4925,(0,8):C.GC_4179})

V_274 = Vertex(name = 'V_274',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS119, L.VVVVS158, L.VVVVS52, L.VVVVS58, L.VVVVS62 ],
               couplings = {(0,0):C.GC_3547,(0,1):C.GC_3471,(0,3):C.GC_3462,(0,2):C.GC_4928,(0,4):C.GC_4180})

V_275 = Vertex(name = 'V_275',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS27, L.VSSSS5 ],
               couplings = {(0,1):C.GC_2504,(0,0):C.GC_2508})

V_276 = Vertex(name = 'V_276',
               particles = [ P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS27, L.VSSSS5 ],
               couplings = {(0,1):C.GC_2687,(0,0):C.GC_2656})

V_277 = Vertex(name = 'V_277',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS2, L.VVSSS33 ],
               couplings = {(0,0):C.GC_4529,(0,1):C.GC_4457})

V_278 = Vertex(name = 'V_278',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS33 ],
               couplings = {(0,0):C.GC_4542})

V_279 = Vertex(name = 'V_279',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS1, L.VSSSS12, L.VSSSS17 ],
               couplings = {(0,0):C.GC_2660,(0,1):C.GC_2505,(0,2):C.GC_2500})

V_280 = Vertex(name = 'V_280',
               particles = [ P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS12, L.VSSSS17 ],
               couplings = {(0,0):C.GC_2653,(0,1):C.GC_2683})

V_281 = Vertex(name = 'V_281',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS26, L.VSSSS3, L.VSSSS31 ],
               couplings = {(0,0):C.GC_2507,(0,2):C.GC_2503,(0,1):C.GC_2661})

V_282 = Vertex(name = 'V_282',
               particles = [ P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS26, L.VSSSS31 ],
               couplings = {(0,0):C.GC_2655,(0,1):C.GC_2686})

V_283 = Vertex(name = 'V_283',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_2506,(0,0):C.GC_2502})

V_284 = Vertex(name = 'V_284',
               particles = [ P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSSS13, L.VSSSS25 ],
               couplings = {(0,1):C.GC_2654,(0,0):C.GC_2685})

V_285 = Vertex(name = 'V_285',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS45 ],
               couplings = {(0,0):C.GC_4456})

V_286 = Vertex(name = 'V_286',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS45 ],
               couplings = {(0,0):C.GC_4541})

V_287 = Vertex(name = 'V_287',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS15, L.VSSSS16, L.VSSSS29 ],
               couplings = {(0,0):C.GC_2505,(0,1):C.GC_2501,(0,2):C.GC_2660})

V_288 = Vertex(name = 'V_288',
               particles = [ P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS15, L.VSSSS16 ],
               couplings = {(0,0):C.GC_2653,(0,1):C.GC_2684})

V_289 = Vertex(name = 'V_289',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS28, L.VSSSS32 ],
               couplings = {(0,0):C.GC_2508,(0,1):C.GC_2504})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSSS28, L.VSSSS32 ],
               couplings = {(0,0):C.GC_2656,(0,1):C.GC_2687})

V_291 = Vertex(name = 'V_291',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS105, L.VVVSS106, L.VVVSS118, L.VVVSS127, L.VVVSS136, L.VVVSS141, L.VVVSS15, L.VVVSS155, L.VVVSS24, L.VVVSS27, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS40, L.VVVSS48, L.VVVSS84, L.VVVSS86, L.VVVSS89, L.VVVSS90 ],
               couplings = {(0,4):C.GC_380,(0,13):C.GC_1844,(0,7):C.GC_2183,(0,5):C.GC_2408,(0,0):C.GC_49,(0,18):C.GC_1798,(0,17):C.GC_1869,(0,1):C.GC_2151,(0,2):C.GC_2200,(0,15):C.GC_2303,(0,8):C.GC_2128,(0,16):C.GC_253,(0,3):C.GC_2040,(0,10):C.GC_353,(0,6):C.GC_1766,(0,11):C.GC_159,(0,12):C.GC_1590,(0,9):C.GC_4761,(0,14):C.GC_4730})

V_292 = Vertex(name = 'V_292',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS35, L.VVVSS38, L.VVVSS48 ],
               couplings = {(0,0):C.GC_2162,(0,1):C.GC_170,(0,2):C.GC_1819,(0,3):C.GC_4773})

V_293 = Vertex(name = 'V_293',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_3106,(0,5):C.GC_3111,(0,1):C.GC_3231,(0,2):C.GC_3400,(0,4):C.GC_3406,(0,3):C.GC_3573})

V_294 = Vertex(name = 'V_294',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS29, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_3236,(0,3):C.GC_3222,(0,1):C.GC_3585,(0,2):C.GC_3557})

V_295 = Vertex(name = 'V_295',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_4327,(0,1):C.GC_3108,(0,4):C.GC_3113,(0,2):C.GC_3401,(0,3):C.GC_3407})

V_296 = Vertex(name = 'V_296',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_3238,(0,3):C.GC_3224,(0,1):C.GC_3586,(0,2):C.GC_3558})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS10, L.VVSSS34, L.VVSSS36, L.VVSSS37, L.VVSSS39, L.VVSSS60 ],
               couplings = {(0,2):C.GC_3107,(0,4):C.GC_3112,(0,3):C.GC_3231,(0,1):C.GC_3403,(0,5):C.GC_3405,(0,0):C.GC_3574})

V_298 = Vertex(name = 'V_298',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS34, L.VVSSS36, L.VVSSS39, L.VVSSS60 ],
               couplings = {(0,1):C.GC_3237,(0,2):C.GC_3223,(0,0):C.GC_3588,(0,3):C.GC_3556})

V_299 = Vertex(name = 'V_299',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS109, L.VVVSS110, L.VVVSS119, L.VVVSS125, L.VVVSS137, L.VVVSS141, L.VVVSS145, L.VVVSS15, L.VVVSS20, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS40, L.VVVSS56, L.VVVSS84, L.VVVSS86, L.VVVSS89, L.VVVSS90 ],
               couplings = {(0,4):C.GC_382,(0,12):C.GC_1843,(0,6):C.GC_2181,(0,5):C.GC_2409,(0,0):C.GC_51,(0,17):C.GC_1797,(0,16):C.GC_1870,(0,2):C.GC_2153,(0,1):C.GC_2202,(0,14):C.GC_2304,(0,15):C.GC_251,(0,9):C.GC_355,(0,7):C.GC_1767,(0,8):C.GC_2130,(0,10):C.GC_157,(0,11):C.GC_1589,(0,3):C.GC_2042,(0,13):C.GC_4729})

V_300 = Vertex(name = 'V_300',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS125, L.VVVSS35, L.VVVSS38, L.VVVSS56 ],
               couplings = {(0,1):C.GC_168,(0,2):C.GC_1818,(0,0):C.GC_2164,(0,3):C.GC_4775})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_3109,(0,3):C.GC_3112,(0,2):C.GC_4251,(0,0):C.GC_3230})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,0):C.GC_3239,(0,2):C.GC_3223,(0,1):C.GC_4336})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS66, L.VVVSS72, L.VVVSS75 ],
               couplings = {(0,0):C.GC_4707,(0,1):C.GC_4795,(0,2):C.GC_4143})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS66, L.VVVSS72 ],
               couplings = {(0,0):C.GC_4714,(0,1):C.GC_4817})

V_305 = Vertex(name = 'V_305',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS105, L.VVVSS106, L.VVVSS118, L.VVVSS127, L.VVVSS136, L.VVVSS141, L.VVVSS15, L.VVVSS155, L.VVVSS24, L.VVVSS27, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS40, L.VVVSS48, L.VVVSS84, L.VVVSS86, L.VVVSS89, L.VVVSS90 ],
               couplings = {(0,4):C.GC_381,(0,13):C.GC_1845,(0,7):C.GC_2182,(0,5):C.GC_2407,(0,0):C.GC_50,(0,18):C.GC_1798,(0,17):C.GC_1868,(0,1):C.GC_2151,(0,2):C.GC_2201,(0,15):C.GC_2302,(0,8):C.GC_2129,(0,16):C.GC_252,(0,3):C.GC_2041,(0,10):C.GC_354,(0,6):C.GC_1765,(0,11):C.GC_158,(0,12):C.GC_1591,(0,9):C.GC_4762,(0,14):C.GC_4731})

V_306 = Vertex(name = 'V_306',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS127, L.VVVSS35, L.VVVSS38, L.VVVSS48 ],
               couplings = {(0,0):C.GC_2163,(0,1):C.GC_169,(0,2):C.GC_1820,(0,3):C.GC_4774})

V_307 = Vertex(name = 'V_307',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS28, L.VVSSS29, L.VVSSS4, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_3110,(0,5):C.GC_3115,(0,1):C.GC_3232,(0,2):C.GC_3402,(0,4):C.GC_3408,(0,3):C.GC_3574})

V_308 = Vertex(name = 'V_308',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS22, L.VVSSS29, L.VVSSS41, L.VVSSS56 ],
               couplings = {(0,0):C.GC_3240,(0,3):C.GC_3226,(0,1):C.GC_3587,(0,2):C.GC_3559})

V_309 = Vertex(name = 'V_309',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS12, L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_4327,(0,1):C.GC_3108,(0,4):C.GC_3113,(0,2):C.GC_3401,(0,3):C.GC_3407})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS23, L.VVSSS25, L.VVSSS54, L.VVSSS55 ],
               couplings = {(0,0):C.GC_3238,(0,3):C.GC_3224,(0,1):C.GC_3586,(0,2):C.GC_3558})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS11, L.VVSSS19, L.VVSSS20, L.VVSSS40, L.VVSSS46, L.VVSSS47 ],
               couplings = {(0,4):C.GC_3107,(0,3):C.GC_3231,(0,5):C.GC_3403,(0,0):C.GC_3574,(0,2):C.GC_3116,(0,1):C.GC_3404})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS19, L.VVSSS20, L.VVSSS46, L.VVSSS47 ],
               couplings = {(0,2):C.GC_3237,(0,3):C.GC_3588,(0,1):C.GC_3227,(0,0):C.GC_3555})

V_313 = Vertex(name = 'V_313',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS109, L.VVVSS110, L.VVVSS119, L.VVVSS125, L.VVVSS137, L.VVVSS141, L.VVVSS145, L.VVVSS15, L.VVVSS20, L.VVVSS3, L.VVVSS35, L.VVVSS38, L.VVVSS40, L.VVVSS56, L.VVVSS84, L.VVVSS86, L.VVVSS89, L.VVVSS90 ],
               couplings = {(0,4):C.GC_382,(0,12):C.GC_1843,(0,6):C.GC_2181,(0,5):C.GC_2409,(0,0):C.GC_51,(0,17):C.GC_1796,(0,16):C.GC_1870,(0,2):C.GC_2152,(0,1):C.GC_2202,(0,14):C.GC_2304,(0,15):C.GC_251,(0,9):C.GC_355,(0,7):C.GC_1767,(0,8):C.GC_2130,(0,10):C.GC_157,(0,11):C.GC_1589,(0,3):C.GC_2042,(0,13):C.GC_4729})

V_314 = Vertex(name = 'V_314',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS125, L.VVVSS35, L.VVVSS38, L.VVVSS56 ],
               couplings = {(0,1):C.GC_168,(0,2):C.GC_1818,(0,0):C.GC_2164,(0,3):C.GC_4775})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS17, L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,1):C.GC_3107,(0,3):C.GC_3114,(0,2):C.GC_4252,(0,0):C.GC_3233})

V_316 = Vertex(name = 'V_316',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS49, L.VVSSS50, L.VVSSS52 ],
               couplings = {(0,0):C.GC_3237,(0,2):C.GC_3225,(0,1):C.GC_4335})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS108, L.VVVSS114, L.VVVSS126, L.VVVSS131, L.VVVSS141, L.VVVSS144, L.VVVSS153, L.VVVSS25, L.VVVSS26, L.VVVSS57, L.VVVSS84, L.VVVSS92, L.VVVSS93 ],
               couplings = {(0,6):C.GC_1915,(0,4):C.GC_2238,(0,5):C.GC_309,(0,11):C.GC_1582,(0,10):C.GC_2053,(0,8):C.GC_222,(0,12):C.GC_258,(0,0):C.GC_329,(0,3):C.GC_28,(0,1):C.GC_1740,(0,9):C.GC_4792,(0,7):C.GC_1894,(0,2):C.GC_1581})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS126, L.VVVSS131, L.VVVSS57 ],
               couplings = {(0,1):C.GC_286,(0,2):C.GC_4814,(0,0):C.GC_1712})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS100, L.VVVSS107, L.VVVSS12, L.VVVSS146, L.VVVSS147, L.VVVSS2, L.VVVSS29, L.VVVSS30, L.VVVSS69, L.VVVSS79, L.VVVSS82, L.VVVSS95 ],
               couplings = {(0,4):C.GC_1916,(0,3):C.GC_308,(0,10):C.GC_2597,(0,5):C.GC_221,(0,1):C.GC_259,(0,11):C.GC_328,(0,0):C.GC_1583,(0,9):C.GC_27,(0,2):C.GC_2639,(0,7):C.GC_2499,(0,6):C.GC_4810,(0,8):C.GC_4791})

V_320 = Vertex(name = 'V_320',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS30, L.VVVSS69, L.VVVSS79 ],
               couplings = {(0,2):C.GC_285,(0,0):C.GC_2590,(0,1):C.GC_4813})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS115, L.VVVSS116, L.VVVSS12, L.VVVSS120, L.VVVSS128, L.VVVSS132, L.VVVSS141, L.VVVSS142, L.VVVSS143, L.VVVSS19, L.VVVSS23, L.VVVSS28, L.VVVSS30, L.VVVSS45, L.VVVSS51, L.VVVSS54, L.VVVSS58, L.VVVSS63, L.VVVSS82, L.VVVSS84, L.VVVSS99 ],
               couplings = {(0,7):C.GC_1915,(0,6):C.GC_2237,(0,8):C.GC_310,(0,20):C.GC_1582,(0,3):C.GC_1739,(0,19):C.GC_2052,(0,18):C.GC_2118,(0,10):C.GC_223,(0,4):C.GC_29,(0,1):C.GC_257,(0,0):C.GC_330,(0,9):C.GC_1893,(0,2):C.GC_2218,(0,5):C.GC_1580,(0,12):C.GC_2051,(0,16):C.GC_3980,(0,13):C.GC_3981,(0,11):C.GC_4025,(0,17):C.GC_4115,(0,14):C.GC_4116,(0,15):C.GC_4141})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS128, L.VVVSS132, L.VVVSS30, L.VVVSS45, L.VVVSS51, L.VVVSS58, L.VVVSS63 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_1711,(0,2):C.GC_2108,(0,5):C.GC_4032,(0,3):C.GC_4016,(0,6):C.GC_4146,(0,4):C.GC_4138})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS108, L.VVVSS114, L.VVVSS122, L.VVVSS126, L.VVVSS131, L.VVVSS141, L.VVVSS144, L.VVVSS153, L.VVVSS156, L.VVVSS157, L.VVVSS25, L.VVVSS26, L.VVVSS57, L.VVVSS84, L.VVVSS92, L.VVVSS93 ],
               couplings = {(0,7):C.GC_1915,(0,5):C.GC_2238,(0,9):C.GC_1584,(0,8):C.GC_30,(0,6):C.GC_309,(0,14):C.GC_1582,(0,2):C.GC_1934,(0,13):C.GC_2053,(0,11):C.GC_222,(0,0):C.GC_31,(0,15):C.GC_258,(0,4):C.GC_28,(0,1):C.GC_1579,(0,12):C.GC_4793,(0,10):C.GC_1894,(0,3):C.GC_1581})

V_324 = Vertex(name = 'V_324',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS108, L.VVVSS114, L.VVVSS126, L.VVVSS131, L.VVVSS156, L.VVVSS157, L.VVVSS57, L.VVVSS84 ],
               couplings = {(0,5):C.GC_1943,(0,4):C.GC_403,(0,7):C.GC_2248,(0,0):C.GC_329,(0,3):C.GC_286,(0,1):C.GC_1740,(0,6):C.GC_4815,(0,2):C.GC_1712})

V_325 = Vertex(name = 'V_325',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS101, L.VVVVS12, L.VVVVS122, L.VVVVS123, L.VVVVS130, L.VVVVS135, L.VVVVS149, L.VVVVS168, L.VVVVS191, L.VVVVS198, L.VVVVS202, L.VVVVS203, L.VVVVS204, L.VVVVS36, L.VVVVS48, L.VVVVS52, L.VVVVS54 ],
               couplings = {(0,4):C.GC_3210,(0,15):C.GC_3721,(0,3):C.GC_3534,(0,0):C.GC_3526,(0,2):C.GC_3681,(0,9):C.GC_3105,(0,7):C.GC_3143,(0,8):C.GC_3606,(0,10):C.GC_3398,(0,11):C.GC_3472,(0,13):C.GC_3695,(0,12):C.GC_3734,(0,1):C.GC_3397,(0,14):C.GC_3200,(0,17):C.GC_3104,(0,5):C.GC_4926,(0,6):C.GC_4937,(0,16):C.GC_4191})

V_326 = Vertex(name = 'V_326',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS101, L.VVVVS130, L.VVVVS135, L.VVVVS168, L.VVVVS54 ],
               couplings = {(0,3):C.GC_3706,(0,0):C.GC_3463,(0,4):C.GC_3136,(0,1):C.GC_4930,(0,2):C.GC_4941})

V_327 = Vertex(name = 'V_327',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS66, L.VVVSS72, L.VVVSS75 ],
               couplings = {(0,0):C.GC_4708,(0,1):C.GC_4794,(0,2):C.GC_4142})

V_328 = Vertex(name = 'V_328',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS66, L.VVVSS72 ],
               couplings = {(0,0):C.GC_4713,(0,1):C.GC_4816})

V_329 = Vertex(name = 'V_329',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS100, L.VVVVS106, L.VVVVS115, L.VVVVS120, L.VVVVS131, L.VVVVS132, L.VVVVS133, L.VVVVS140, L.VVVVS148, L.VVVVS189, L.VVVVS197, L.VVVVS2, L.VVVVS205, L.VVVVS215, L.VVVVS216, L.VVVVS26, L.VVVVS73, L.VVVVS94 ],
               couplings = {(0,3):C.GC_3210,(0,1):C.GC_3721,(0,2):C.GC_3533,(0,11):C.GC_3526,(0,15):C.GC_3681,(0,9):C.GC_3105,(0,8):C.GC_3143,(0,14):C.GC_3734,(0,0):C.GC_3397,(0,10):C.GC_3399,(0,13):C.GC_3472,(0,12):C.GC_3694,(0,17):C.GC_3605,(0,4):C.GC_4927,(0,5):C.GC_4936,(0,16):C.GC_3201,(0,7):C.GC_3103,(0,6):C.GC_4190})

V_330 = Vertex(name = 'V_330',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS100, L.VVVVS131, L.VVVVS132, L.VVVVS140, L.VVVVS94 ],
               couplings = {(0,0):C.GC_3463,(0,4):C.GC_3705,(0,1):C.GC_4929,(0,2):C.GC_4940,(0,3):C.GC_3135})

V_331 = Vertex(name = 'V_331',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS27, L.VVSSS53 ],
               couplings = {(0,0):C.GC_4567,(0,1):C.GC_4570})

V_332 = Vertex(name = 'V_332',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS27, L.VVSSS53 ],
               couplings = {(0,0):C.GC_4630,(0,1):C.GC_4622})

V_333 = Vertex(name = 'V_333',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS30, L.VVSSS6 ],
               couplings = {(0,0):C.GC_4568,(0,1):C.GC_4623})

V_334 = Vertex(name = 'V_334',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS30 ],
               couplings = {(0,0):C.GC_4628})

V_335 = Vertex(name = 'V_335',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS16, L.VVSSS48, L.VVSSS58 ],
               couplings = {(0,0):C.GC_4195,(0,2):C.GC_4569,(0,3):C.GC_4566,(0,1):C.GC_4624})

V_336 = Vertex(name = 'V_336',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1, L.VVSSS48, L.VVSSS58 ],
               couplings = {(0,0):C.GC_4199,(0,1):C.GC_4621,(0,2):C.GC_4629})

V_337 = Vertex(name = 'V_337',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS51, L.VVSSS59 ],
               couplings = {(0,0):C.GC_4570,(0,1):C.GC_4571})

V_338 = Vertex(name = 'V_338',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS51, L.VVSSS59 ],
               couplings = {(0,0):C.GC_4622,(0,1):C.GC_4630})

V_339 = Vertex(name = 'V_339',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS111, L.VVVSS112, L.VVVSS130, L.VVVSS149, L.VVVSS151, L.VVVSS161, L.VVVSS163, L.VVVSS22, L.VVVSS32, L.VVVSS36, L.VVVSS49, L.VVVSS50, L.VVVSS59, L.VVVSS6, L.VVVSS60, L.VVVSS67, L.VVVSS77, L.VVVSS87, L.VVVSS91, L.VVVSS94 ],
               couplings = {(0,5):C.GC_1919,(0,6):C.GC_2233,(0,7):C.GC_312,(0,4):C.GC_2382,(0,1):C.GC_264,(0,2):C.GC_333,(0,19):C.GC_2045,(0,18):C.GC_2391,(0,8):C.GC_225,(0,0):C.GC_1895,(0,3):C.GC_47,(0,17):C.GC_2494,(0,14):C.GC_2345,(0,10):C.GC_2301,(0,20):C.GC_2612,(0,9):C.GC_4710,(0,11):C.GC_4789,(0,15):C.GC_4140,(0,12):C.GC_4824,(0,16):C.GC_4165,(0,13):C.GC_4027})

V_340 = Vertex(name = 'V_340',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS130, L.VVVSS32, L.VVVSS36, L.VVVSS49, L.VVVSS50, L.VVVSS77, L.VVVSS91 ],
               couplings = {(0,0):C.GC_1594,(0,7):C.GC_2357,(0,1):C.GC_290,(0,6):C.GC_1715,(0,3):C.GC_2368,(0,2):C.GC_4716,(0,4):C.GC_4812,(0,5):C.GC_4854})

V_341 = Vertex(name = 'V_341',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS111, L.VVVSS112, L.VVVSS130, L.VVVSS149, L.VVVSS151, L.VVVSS161, L.VVVSS163, L.VVVSS22, L.VVVSS33, L.VVVSS36, L.VVVSS55, L.VVVSS6, L.VVVSS64, L.VVVSS68, L.VVVSS73, L.VVVSS76, L.VVVSS77, L.VVVSS87, L.VVVSS91, L.VVVSS94 ],
               couplings = {(0,5):C.GC_1917,(0,6):C.GC_2232,(0,7):C.GC_311,(0,4):C.GC_2380,(0,1):C.GC_261,(0,2):C.GC_332,(0,19):C.GC_2044,(0,18):C.GC_2389,(0,8):C.GC_224,(0,0):C.GC_1897,(0,3):C.GC_48,(0,17):C.GC_2492,(0,12):C.GC_2343,(0,10):C.GC_2299,(0,20):C.GC_2614,(0,11):C.GC_3982,(0,16):C.GC_3983,(0,13):C.GC_4112,(0,15):C.GC_4113,(0,9):C.GC_4822,(0,14):C.GC_4848})

V_342 = Vertex(name = 'V_342',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS130, L.VVVSS33, L.VVVSS36, L.VVVSS55, L.VVVSS64, L.VVVSS73, L.VVVSS76, L.VVVSS77, L.VVVSS91 ],
               couplings = {(0,0):C.GC_1592,(0,9):C.GC_2359,(0,1):C.GC_291,(0,8):C.GC_1713,(0,3):C.GC_2366,(0,4):C.GC_4033,(0,7):C.GC_4017,(0,5):C.GC_4145,(0,6):C.GC_4137,(0,2):C.GC_4852})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS111, L.VVVSS112, L.VVVSS130, L.VVVSS149, L.VVVSS151, L.VVVSS161, L.VVVSS163, L.VVVSS22, L.VVVSS32, L.VVVSS36, L.VVVSS49, L.VVVSS50, L.VVVSS59, L.VVVSS6, L.VVVSS60, L.VVVSS67, L.VVVSS77, L.VVVSS87, L.VVVSS91, L.VVVSS94 ],
               couplings = {(0,5):C.GC_1918,(0,6):C.GC_2234,(0,7):C.GC_313,(0,4):C.GC_2381,(0,1):C.GC_264,(0,2):C.GC_334,(0,19):C.GC_2046,(0,18):C.GC_2390,(0,8):C.GC_226,(0,0):C.GC_1896,(0,3):C.GC_46,(0,17):C.GC_2493,(0,14):C.GC_2344,(0,10):C.GC_2300,(0,20):C.GC_2613,(0,9):C.GC_4709,(0,11):C.GC_4788,(0,15):C.GC_4139,(0,12):C.GC_4823,(0,16):C.GC_4164,(0,13):C.GC_4026})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS130, L.VVVSS32, L.VVVSS36, L.VVVSS49, L.VVVSS50, L.VVVSS77, L.VVVSS91 ],
               couplings = {(0,0):C.GC_1593,(0,7):C.GC_2357,(0,1):C.GC_289,(0,6):C.GC_1714,(0,3):C.GC_2367,(0,2):C.GC_4715,(0,4):C.GC_4811,(0,5):C.GC_4853})

V_345 = Vertex(name = 'V_345',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS111, L.VVVSS112, L.VVVSS130, L.VVVSS149, L.VVVSS151, L.VVVSS161, L.VVVSS163, L.VVVSS22, L.VVVSS33, L.VVVSS36, L.VVVSS55, L.VVVSS6, L.VVVSS64, L.VVVSS68, L.VVVSS73, L.VVVSS76, L.VVVSS77, L.VVVSS87, L.VVVSS91, L.VVVSS94 ],
               couplings = {(0,5):C.GC_1917,(0,6):C.GC_2232,(0,7):C.GC_311,(0,4):C.GC_2380,(0,1):C.GC_260,(0,2):C.GC_332,(0,19):C.GC_2044,(0,18):C.GC_2389,(0,8):C.GC_224,(0,0):C.GC_1897,(0,3):C.GC_48,(0,17):C.GC_2492,(0,12):C.GC_2343,(0,10):C.GC_2299,(0,20):C.GC_2614,(0,11):C.GC_3982,(0,16):C.GC_3983,(0,13):C.GC_4112,(0,15):C.GC_4113,(0,9):C.GC_4822,(0,14):C.GC_4848})

V_346 = Vertex(name = 'V_346',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS130, L.VVVSS33, L.VVVSS36, L.VVVSS55, L.VVVSS64, L.VVVSS73, L.VVVSS76, L.VVVSS77, L.VVVSS91 ],
               couplings = {(0,0):C.GC_1592,(0,9):C.GC_2358,(0,1):C.GC_291,(0,8):C.GC_1713,(0,3):C.GC_2366,(0,4):C.GC_4033,(0,7):C.GC_4017,(0,5):C.GC_4145,(0,6):C.GC_4137,(0,2):C.GC_4852})

V_347 = Vertex(name = 'V_347',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS10, L.VVVSS13, L.VVVSS149, L.VVVSS159, L.VVVSS32, L.VVVSS36, L.VVVSS42, L.VVVSS5, L.VVVSS59, L.VVVSS6, L.VVVSS78, L.VVVSS87, L.VVVSS91, L.VVVSS98 ],
               couplings = {(0,6):C.GC_1847,(0,3):C.GC_2185,(0,2):C.GC_2463,(0,13):C.GC_2853,(0,11):C.GC_3005,(0,12):C.GC_2992,(0,0):C.GC_2608,(0,10):C.GC_2769,(0,7):C.GC_1769,(0,1):C.GC_2400,(0,9):C.GC_2448,(0,5):C.GC_2964,(0,4):C.GC_4866,(0,8):C.GC_4886})

V_348 = Vertex(name = 'V_348',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS32, L.VVVSS36, L.VVVSS78 ],
               couplings = {(0,2):C.GC_2628,(0,1):C.GC_2994,(0,0):C.GC_4891})

V_349 = Vertex(name = 'V_349',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS105, L.VVVVS11, L.VVVVS110, L.VVVVS114, L.VVVVS144, L.VVVVS146, L.VVVVS152, L.VVVVS153, L.VVVVS159, L.VVVVS161, L.VVVVS164, L.VVVVS165, L.VVVVS167, L.VVVVS174, L.VVVVS175, L.VVVVS176, L.VVVVS177, L.VVVVS182, L.VVVVS21, L.VVVVS35, L.VVVVS37, L.VVVVS52, L.VVVVS55, L.VVVVS62, L.VVVVS63, L.VVVVS64, L.VVVVS83 ],
               couplings = {(0,18):C.GC_3511,(0,2):C.GC_3900,(0,3):C.GC_4518,(0,0):C.GC_3188,(0,19):C.GC_3157,(0,25):C.GC_3483,(0,24):C.GC_3885,(0,14):C.GC_3518,(0,8):C.GC_3903,(0,16):C.GC_3169,(0,17):C.GC_3197,(0,6):C.GC_3822,(0,7):C.GC_3833,(0,9):C.GC_3889,(0,15):C.GC_4453,(0,1):C.GC_3749,(0,12):C.GC_3120,(0,10):C.GC_3628,(0,11):C.GC_3804,(0,4):C.GC_3419,(0,13):C.GC_3496,(0,5):C.GC_3871,(0,26):C.GC_3672,(0,20):C.GC_3856,(0,22):C.GC_3809,(0,21):C.GC_4948,(0,23):C.GC_4951})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS144, L.VVVVS146, L.VVVVS164, L.VVVVS167, L.VVVVS52, L.VVVVS55 ],
               couplings = {(0,3):C.GC_3180,(0,2):C.GC_3662,(0,0):C.GC_3503,(0,1):C.GC_3893,(0,5):C.GC_3821,(0,4):C.GC_4954})

V_351 = Vertex(name = 'V_351',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS105, L.VVVVS11, L.VVVVS110, L.VVVVS114, L.VVVVS144, L.VVVVS146, L.VVVVS152, L.VVVVS153, L.VVVVS159, L.VVVVS161, L.VVVVS164, L.VVVVS165, L.VVVVS167, L.VVVVS174, L.VVVVS175, L.VVVVS176, L.VVVVS177, L.VVVVS182, L.VVVVS21, L.VVVVS35, L.VVVVS37, L.VVVVS52, L.VVVVS55, L.VVVVS62, L.VVVVS63, L.VVVVS64, L.VVVVS83 ],
               couplings = {(0,18):C.GC_3512,(0,2):C.GC_3899,(0,3):C.GC_4517,(0,0):C.GC_3189,(0,19):C.GC_3158,(0,25):C.GC_3484,(0,24):C.GC_3886,(0,14):C.GC_3519,(0,8):C.GC_3902,(0,16):C.GC_3169,(0,17):C.GC_3196,(0,6):C.GC_3823,(0,7):C.GC_3832,(0,9):C.GC_3889,(0,15):C.GC_4454,(0,1):C.GC_3748,(0,12):C.GC_3119,(0,10):C.GC_3629,(0,11):C.GC_3805,(0,4):C.GC_3418,(0,13):C.GC_3496,(0,5):C.GC_3872,(0,26):C.GC_3671,(0,20):C.GC_3857,(0,22):C.GC_3808,(0,21):C.GC_4949,(0,23):C.GC_4952})

V_352 = Vertex(name = 'V_352',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS144, L.VVVVS146, L.VVVVS164, L.VVVVS167, L.VVVVS52, L.VVVVS55 ],
               couplings = {(0,3):C.GC_3179,(0,2):C.GC_3663,(0,0):C.GC_3502,(0,1):C.GC_3894,(0,5):C.GC_3820,(0,4):C.GC_4955})

V_353 = Vertex(name = 'V_353',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS111, L.VVVVS112, L.VVVVS128, L.VVVVS129, L.VVVVS139, L.VVVVS158, L.VVVVS160, L.VVVVS161, L.VVVVS164, L.VVVVS169, L.VVVVS171, L.VVVVS186, L.VVVVS193, L.VVVVS199, L.VVVVS200, L.VVVVS201, L.VVVVS33, L.VVVVS39, L.VVVVS40, L.VVVVS52, L.VVVVS53, L.VVVVS58, L.VVVVS62, L.VVVVS69, L.VVVVS71, L.VVVVS83, L.VVVVS84, L.VVVVS88, L.VVVVS89, L.VVVVS90, L.VVVVS91 ],
               couplings = {(0,31):C.GC_3102,(0,28):C.GC_3417,(0,17):C.GC_3870,(0,3):C.GC_3209,(0,4):C.GC_3536,(0,2):C.GC_3618,(0,30):C.GC_3724,(0,1):C.GC_3812,(0,29):C.GC_3847,(0,19):C.GC_3684,(0,21):C.GC_4564,(0,13):C.GC_3214,(0,27):C.GC_3413,(0,16):C.GC_3541,(0,12):C.GC_3100,(0,15):C.GC_3416,(0,14):C.GC_3619,(0,7):C.GC_3699,(0,6):C.GC_3813,(0,8):C.GC_3834,(0,0):C.GC_3150,(0,25):C.GC_3527,(0,9):C.GC_3094,(0,11):C.GC_3414,(0,10):C.GC_3615,(0,18):C.GC_3829,(0,22):C.GC_3810,(0,26):C.GC_3093,(0,20):C.GC_4934,(0,24):C.GC_4609,(0,5):C.GC_4565,(0,23):C.GC_4935})

V_354 = Vertex(name = 'V_354',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS111, L.VVVVS112, L.VVVVS139, L.VVVVS158, L.VVVVS164, L.VVVVS169, L.VVVVS171, L.VVVVS199, L.VVVVS33, L.VVVVS52, L.VVVVS53, L.VVVVS58, L.VVVVS62, L.VVVVS83, L.VVVVS84, L.VVVVS88, L.VVVVS91 ],
               couplings = {(0,16):C.GC_3220,(0,15):C.GC_3548,(0,8):C.GC_3908,(0,1):C.GC_3770,(0,0):C.GC_3863,(0,10):C.GC_4615,(0,14):C.GC_3473,(0,7):C.GC_3736,(0,3):C.GC_3852,(0,4):C.GC_3151,(0,6):C.GC_3464,(0,5):C.GC_3708,(0,11):C.GC_3838,(0,13):C.GC_3162,(0,9):C.GC_4939,(0,2):C.GC_4593,(0,12):C.GC_4938})

V_355 = Vertex(name = 'V_355',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS14, L.VVVSS158, L.VVVSS70, L.VVVSS81, L.VVVSS96 ],
               couplings = {(0,1):C.GC_2871,(0,4):C.GC_2989,(0,0):C.GC_2846,(0,3):C.GC_2961,(0,2):C.GC_4896})

V_356 = Vertex(name = 'V_356',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS70, L.VVVSS81 ],
               couplings = {(0,1):C.GC_2864,(0,0):C.GC_4902})

V_357 = Vertex(name = 'V_357',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS14, L.VVVSS158, L.VVVSS63, L.VVVSS81, L.VVVSS96 ],
               couplings = {(0,1):C.GC_2870,(0,4):C.GC_2988,(0,0):C.GC_2845,(0,3):C.GC_2962,(0,2):C.GC_4897})

V_358 = Vertex(name = 'V_358',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS63, L.VVVSS81 ],
               couplings = {(0,1):C.GC_2865,(0,0):C.GC_4903})

V_359 = Vertex(name = 'V_359',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS109, L.VVVVS113, L.VVVVS118, L.VVVVS134, L.VVVVS142, L.VVVVS155, L.VVVVS156, L.VVVVS166, L.VVVVS17, L.VVVVS173, L.VVVVS214, L.VVVVS219, L.VVVVS220, L.VVVVS7, L.VVVVS78, L.VVVVS79, L.VVVVS86, L.VVVVS96 ],
               couplings = {(0,1):C.GC_3726,(0,16):C.GC_3923,(0,2):C.GC_4318,(0,0):C.GC_3844,(0,15):C.GC_3686,(0,13):C.GC_3826,(0,12):C.GC_3740,(0,5):C.GC_3924,(0,6):C.GC_4598,(0,8):C.GC_3202,(0,7):C.GC_4573,(0,9):C.GC_3627,(0,11):C.GC_4256,(0,17):C.GC_3806,(0,10):C.GC_3850,(0,14):C.GC_3916,(0,4):C.GC_3912,(0,3):C.GC_4957})

V_360 = Vertex(name = 'V_360',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS134, L.VVVVS142, L.VVVVS166, L.VVVVS173, L.VVVVS219, L.VVVVS96 ],
               couplings = {(0,2):C.GC_3138,(0,3):C.GC_3713,(0,4):C.GC_4501,(0,5):C.GC_3836,(0,1):C.GC_3919,(0,0):C.GC_4959})

V_361 = Vertex(name = 'V_361',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS109, L.VVVVS113, L.VVVVS118, L.VVVVS134, L.VVVVS142, L.VVVVS155, L.VVVVS156, L.VVVVS166, L.VVVVS17, L.VVVVS173, L.VVVVS214, L.VVVVS219, L.VVVVS220, L.VVVVS7, L.VVVVS78, L.VVVVS79, L.VVVVS86, L.VVVVS96 ],
               couplings = {(0,1):C.GC_3727,(0,16):C.GC_3922,(0,2):C.GC_4319,(0,0):C.GC_3845,(0,15):C.GC_3687,(0,13):C.GC_3827,(0,12):C.GC_3739,(0,5):C.GC_3925,(0,6):C.GC_4599,(0,8):C.GC_3203,(0,7):C.GC_4572,(0,9):C.GC_3624,(0,11):C.GC_4257,(0,17):C.GC_3807,(0,10):C.GC_3851,(0,14):C.GC_3915,(0,4):C.GC_3911,(0,3):C.GC_4956})

V_362 = Vertex(name = 'V_362',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS134, L.VVVVS142, L.VVVVS166, L.VVVVS173, L.VVVVS219, L.VVVVS96 ],
               couplings = {(0,2):C.GC_3137,(0,3):C.GC_3710,(0,4):C.GC_4501,(0,5):C.GC_3837,(0,1):C.GC_3918,(0,0):C.GC_4958})

V_363 = Vertex(name = 'V_363',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS134, L.VVVVS163, L.VVVVS172, L.VVVVS76, L.VVVVS93 ],
               couplings = {(0,4):C.GC_4653,(0,1):C.GC_4664,(0,3):C.GC_4674,(0,2):C.GC_4665,(0,0):C.GC_4962})

V_364 = Vertex(name = 'V_364',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS134, L.VVVVS163, L.VVVVS172 ],
               couplings = {(0,1):C.GC_4676,(0,2):C.GC_4675,(0,0):C.GC_4963})

V_365 = Vertex(name = 'V_365',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS126, L.VVVVS137, L.VVVVS139, L.VVVVS184, L.VVVVS185, L.VVVVS190, L.VVVVS44, L.VVVVS47, L.VVVVS49, L.VVVVS53, L.VVVVS60, L.VVVVS69, L.VVVVS70 ],
               couplings = {(0,7):C.GC_3617,(0,6):C.GC_3723,(0,8):C.GC_3101,(0,0):C.GC_3209,(0,12):C.GC_3683,(0,9):C.GC_4253,(0,4):C.GC_3213,(0,5):C.GC_3620,(0,3):C.GC_3100,(0,1):C.GC_3614,(0,10):C.GC_3696,(0,11):C.GC_4306,(0,2):C.GC_4254})

V_366 = Vertex(name = 'V_366',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS137, L.VVVVS139, L.VVVVS190, L.VVVVS47, L.VVVVS49, L.VVVVS53 ],
               couplings = {(0,3):C.GC_3769,(0,4):C.GC_3219,(0,5):C.GC_4309,(0,2):C.GC_3737,(0,0):C.GC_3707,(0,1):C.GC_4307})

V_367 = Vertex(name = 'V_367',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS102, L.VVVVS103, L.VVVVS116, L.VVVVS120, L.VVVVS124, L.VVVVS143, L.VVVVS147, L.VVVVS151, L.VVVVS154, L.VVVVS16, L.VVVVS180, L.VVVVS189, L.VVVVS208, L.VVVVS209, L.VVVVS210, L.VVVVS217, L.VVVVS23, L.VVVVS27, L.VVVVS30, L.VVVVS65, L.VVVVS67, L.VVVVS81 ],
               couplings = {(0,1):C.GC_3097,(0,0):C.GC_3186,(0,16):C.GC_3411,(0,9):C.GC_3509,(0,2):C.GC_3623,(0,4):C.GC_3758,(0,21):C.GC_3815,(0,3):C.GC_3859,(0,19):C.GC_3481,(0,20):C.GC_3155,(0,15):C.GC_3098,(0,12):C.GC_3168,(0,10):C.GC_3412,(0,8):C.GC_3495,(0,13):C.GC_3622,(0,14):C.GC_3763,(0,11):C.GC_3814,(0,7):C.GC_4371,(0,5):C.GC_3409,(0,6):C.GC_3096,(0,17):C.GC_4408,(0,18):C.GC_4372})

V_368 = Vertex(name = 'V_368',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS103, L.VVVVS116, L.VVVVS143, L.VVVVS147, L.VVVVS151, L.VVVVS180, L.VVVVS189, L.VVVVS217, L.VVVVS23, L.VVVVS30, L.VVVVS81 ],
               couplings = {(0,0):C.GC_3217,(0,8):C.GC_3546,(0,1):C.GC_3772,(0,10):C.GC_3864,(0,7):C.GC_3195,(0,5):C.GC_3517,(0,6):C.GC_3861,(0,4):C.GC_4405,(0,2):C.GC_3501,(0,3):C.GC_3178,(0,9):C.GC_4404})

V_369 = Vertex(name = 'V_369',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS139, L.VVVVS32, L.VVVVS53, L.VVVVS69 ],
               couplings = {(0,1):C.GC_4654,(0,2):C.GC_4668,(0,3):C.GC_4679,(0,0):C.GC_4669})

V_370 = Vertex(name = 'V_370',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS139, L.VVVVS53 ],
               couplings = {(0,1):C.GC_4680,(0,0):C.GC_4673})

V_371 = Vertex(name = 'V_371',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS142, L.VVVVS15, L.VVVVS155, L.VVVVS66, L.VVVVS75, L.VVVVS77, L.VVVVS78, L.VVVVS80, L.VVVVS85, L.VVVVS86, L.VVVVS87 ],
               couplings = {(0,8):C.GC_3190,(0,1):C.GC_3513,(0,10):C.GC_3898,(0,9):C.GC_3929,(0,2):C.GC_4667,(0,5):C.GC_3159,(0,3):C.GC_3485,(0,4):C.GC_4658,(0,7):C.GC_3884,(0,6):C.GC_3928,(0,0):C.GC_4666})

V_372 = Vertex(name = 'V_372',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS142, L.VVVVS155 ],
               couplings = {(0,1):C.GC_4678,(0,0):C.GC_4677})

V_373 = Vertex(name = 'V_373',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS14, L.VVVSS158, L.VVVSS81, L.VVVSS96 ],
               couplings = {(0,1):C.GC_2186,(0,3):C.GC_2838,(0,0):C.GC_2889,(0,2):C.GC_2773})

V_374 = Vertex(name = 'V_374',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS81 ],
               couplings = {(0,0):C.GC_2831})

V_375 = Vertex(name = 'V_375',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS11, L.VVVSS12, L.VVVSS140, L.VVVSS164, L.VVVSS30, L.VVVSS8, L.VVVSS80, L.VVVSS81, L.VVVSS82, L.VVVSS9, L.VVVSS93, L.VVVSS96, L.VVVSS97 ],
               couplings = {(0,2):C.GC_315,(0,3):C.GC_2379,(0,11):C.GC_2880,(0,8):C.GC_2983,(0,12):C.GC_2615,(0,9):C.GC_230,(0,0):C.GC_2219,(0,5):C.GC_2342,(0,10):C.GC_2860,(0,7):C.GC_2770,(0,6):C.GC_2509,(0,1):C.GC_2474,(0,4):C.GC_2966})

V_376 = Vertex(name = 'V_376',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS30, L.VVVSS80, L.VVVSS81 ],
               couplings = {(0,2):C.GC_2866,(0,1):C.GC_2109,(0,0):C.GC_2445})

V_377 = Vertex(name = 'V_377',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS141, L.VVVVS150, L.VVVVS74, L.VVVVS82 ],
               couplings = {(0,3):C.GC_3189,(0,1):C.GC_4493,(0,2):C.GC_4513,(0,0):C.GC_4451})

V_378 = Vertex(name = 'V_378',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS141 ],
               couplings = {(0,0):C.GC_4486})

V_379 = Vertex(name = 'V_379',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS102, L.VVVSS12, L.VVVSS124, L.VVVSS134, L.VVVSS18, L.VVVSS30, L.VVVSS52, L.VVVSS82 ],
               couplings = {(0,4):C.GC_313,(0,7):C.GC_2235,(0,1):C.GC_335,(0,8):C.GC_2594,(0,5):C.GC_227,(0,0):C.GC_265,(0,3):C.GC_47,(0,2):C.GC_2215,(0,6):C.GC_2497})

V_380 = Vertex(name = 'V_380',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS124, L.VVVSS30 ],
               couplings = {(0,0):C.GC_2047,(0,1):C.GC_290,(0,2):C.GC_2107})

V_381 = Vertex(name = 'V_381',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS103, L.VVVSS104, L.VVVSS12, L.VVVSS123, L.VVVSS135, L.VVVSS154, L.VVVSS17, L.VVVSS30, L.VVVSS82 ],
               couplings = {(0,4):C.GC_314,(0,0):C.GC_331,(0,8):C.GC_2596,(0,6):C.GC_229,(0,2):C.GC_2217,(0,3):C.GC_45,(0,7):C.GC_2495,(0,5):C.GC_2231,(0,1):C.GC_262})

V_382 = Vertex(name = 'V_382',
               particles = [ P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS104, L.VVVSS123, L.VVVSS30 ],
               couplings = {(0,1):C.GC_288,(0,2):C.GC_2105,(0,0):C.GC_2043})

V_383 = Vertex(name = 'V_383',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS123, L.VVVVS138, L.VVVVS139, L.VVVVS145, L.VVVVS157, L.VVVVS162, L.VVVVS191, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS28, L.VVVVS34, L.VVVVS45, L.VVVVS53, L.VVVVS56, L.VVVVS59, L.VVVVS69, L.VVVVS72, L.VVVVS92 ],
               couplings = {(0,12):C.GC_3727,(0,0):C.GC_4612,(0,18):C.GC_3844,(0,17):C.GC_3687,(0,11):C.GC_3827,(0,5):C.GC_3164,(0,9):C.GC_3741,(0,13):C.GC_3882,(0,6):C.GC_4575,(0,8):C.GC_4501,(0,7):C.GC_3851,(0,4):C.GC_3145,(0,1):C.GC_3625,(0,15):C.GC_3806,(0,10):C.GC_3203,(0,3):C.GC_3118,(0,14):C.GC_3121,(0,16):C.GC_3906,(0,2):C.GC_3874})

V_384 = Vertex(name = 'V_384',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS138, L.VVVVS139, L.VVVVS56, L.VVVVS59 ],
               couplings = {(0,0):C.GC_3711,(0,3):C.GC_3836,(0,2):C.GC_3137,(0,1):C.GC_3880})

V_385 = Vertex(name = 'V_385',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS141, L.VVVVS150, L.VVVVS74, L.VVVVS82 ],
               couplings = {(0,3):C.GC_3188,(0,1):C.GC_4494,(0,2):C.GC_4512,(0,0):C.GC_4452})

V_386 = Vertex(name = 'V_386',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS141 ],
               couplings = {(0,0):C.GC_4487})

V_387 = Vertex(name = 'V_387',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS102, L.VVVSS12, L.VVVSS124, L.VVVSS134, L.VVVSS18, L.VVVSS30, L.VVVSS52, L.VVVSS82 ],
               couplings = {(0,4):C.GC_312,(0,7):C.GC_2236,(0,1):C.GC_336,(0,8):C.GC_2595,(0,5):C.GC_228,(0,0):C.GC_265,(0,3):C.GC_46,(0,2):C.GC_2216,(0,6):C.GC_2496})

V_388 = Vertex(name = 'V_388',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSS101, L.VVVSS124, L.VVVSS30 ],
               couplings = {(0,0):C.GC_2048,(0,1):C.GC_289,(0,2):C.GC_2106})

V_389 = Vertex(name = 'V_389',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS103, L.VVVSS104, L.VVVSS12, L.VVVSS123, L.VVVSS135, L.VVVSS154, L.VVVSS17, L.VVVSS30, L.VVVSS82 ],
               couplings = {(0,4):C.GC_314,(0,0):C.GC_331,(0,8):C.GC_2596,(0,6):C.GC_229,(0,2):C.GC_2217,(0,3):C.GC_45,(0,7):C.GC_2495,(0,5):C.GC_2231,(0,1):C.GC_263})

V_390 = Vertex(name = 'V_390',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS104, L.VVVSS123, L.VVVSS30 ],
               couplings = {(0,1):C.GC_288,(0,2):C.GC_2105,(0,0):C.GC_2043})

V_391 = Vertex(name = 'V_391',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS123, L.VVVVS138, L.VVVVS139, L.VVVVS145, L.VVVVS157, L.VVVVS162, L.VVVVS191, L.VVVVS192, L.VVVVS194, L.VVVVS196, L.VVVVS28, L.VVVVS34, L.VVVVS45, L.VVVVS53, L.VVVVS56, L.VVVVS59, L.VVVVS69, L.VVVVS72, L.VVVVS92 ],
               couplings = {(0,12):C.GC_3726,(0,0):C.GC_4613,(0,18):C.GC_3845,(0,17):C.GC_3686,(0,11):C.GC_3826,(0,5):C.GC_3163,(0,9):C.GC_3738,(0,13):C.GC_3881,(0,6):C.GC_4574,(0,8):C.GC_4501,(0,7):C.GC_3850,(0,4):C.GC_3144,(0,1):C.GC_3626,(0,15):C.GC_3807,(0,10):C.GC_3202,(0,3):C.GC_3117,(0,14):C.GC_3122,(0,16):C.GC_3907,(0,2):C.GC_3873})

V_392 = Vertex(name = 'V_392',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVS138, L.VVVVS139, L.VVVVS56, L.VVVVS59 ],
               couplings = {(0,0):C.GC_3712,(0,3):C.GC_3837,(0,2):C.GC_3138,(0,1):C.GC_3879})

V_393 = Vertex(name = 'V_393',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS12, L.VVVSS139, L.VVVSS30, L.VVVSS82 ],
               couplings = {(0,1):C.GC_2869,(0,3):C.GC_2984,(0,0):C.GC_3007,(0,2):C.GC_2965})

V_394 = Vertex(name = 'V_394',
               particles = [ P.a, P.a, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS30 ],
               couplings = {(0,0):C.GC_2982})

V_395 = Vertex(name = 'V_395',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS13, L.VVVSS149, L.VVVSS150, L.VVVSS36, L.VVVSS42, L.VVVSS5, L.VVVSS6, L.VVVSS7, L.VVVSS87 ],
               couplings = {(0,4):C.GC_1846,(0,2):C.GC_2184,(0,1):C.GC_2462,(0,8):C.GC_3004,(0,0):C.GC_2890,(0,5):C.GC_1768,(0,7):C.GC_2131,(0,6):C.GC_2447,(0,3):C.GC_2963})

V_396 = Vertex(name = 'V_396',
               particles = [ P.a, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS36 ],
               couplings = {(0,0):C.GC_2993})

V_397 = Vertex(name = 'V_397',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS114, L.VVVSS126, L.VVVSS15, L.VVVSS152, L.VVVSS25, L.VVVSS38, L.VVVSS40, L.VVVSS88, L.VVVSS89, L.VVVSS91 ],
               couplings = {(0,3):C.GC_378,(0,6):C.GC_1841,(0,7):C.GC_36,(0,9):C.GC_1794,(0,8):C.GC_1865,(0,2):C.GC_1763,(0,5):C.GC_1574,(0,0):C.GC_192,(0,4):C.GC_352,(0,1):C.GC_34})

V_398 = Vertex(name = 'V_398',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS126, L.VVVSS38 ],
               couplings = {(0,1):C.GC_1815,(0,0):C.GC_167})

V_399 = Vertex(name = 'V_399',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS111, L.VVVSS151, L.VVVSS36, L.VVVSS42, L.VVVSS5, L.VVVSS87, L.VVVSS90 ],
               couplings = {(0,1):C.GC_377,(0,3):C.GC_1840,(0,0):C.GC_35,(0,6):C.GC_1795,(0,5):C.GC_1867,(0,4):C.GC_1762,(0,2):C.GC_1576})

V_400 = Vertex(name = 'V_400',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS36 ],
               couplings = {(0,0):C.GC_1817})

V_401 = Vertex(name = 'V_401',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS114, L.VVVSS121, L.VVVSS126, L.VVVSS15, L.VVVSS152, L.VVVSS162, L.VVVSS25, L.VVVSS38, L.VVVSS39, L.VVVSS40, L.VVVSS88, L.VVVSS89, L.VVVSS91 ],
               couplings = {(0,5):C.GC_38,(0,4):C.GC_378,(0,8):C.GC_1577,(0,9):C.GC_1841,(0,10):C.GC_36,(0,1):C.GC_399,(0,11):C.GC_1578,(0,12):C.GC_1794,(0,3):C.GC_1763,(0,7):C.GC_1574,(0,0):C.GC_32,(0,6):C.GC_352,(0,2):C.GC_34})

V_402 = Vertex(name = 'V_402',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS114, L.VVVSS126, L.VVVSS162, L.VVVSS38, L.VVVSS39, L.VVVSS89 ],
               couplings = {(0,2):C.GC_406,(0,4):C.GC_1939,(0,5):C.GC_1865,(0,3):C.GC_1815,(0,0):C.GC_192,(0,1):C.GC_167})

V_403 = Vertex(name = 'V_403',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS184, L.VVVVS41, L.VVVVS46, L.VVVVS5, L.VVVVS50, L.VVVVS60, L.VVVVS61 ],
               couplings = {(0,4):C.GC_3208,(0,2):C.GC_3722,(0,3):C.GC_3682,(0,5):C.GC_3099,(0,1):C.GC_3616,(0,0):C.GC_3697,(0,6):C.GC_3735})

V_404 = Vertex(name = 'V_404',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS41 ],
               couplings = {(0,0):C.GC_3709})

V_405 = Vertex(name = 'V_405',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS107, L.VVVVS117, L.VVVVS178, L.VVVVS19, L.VVVVS195, L.VVVVS20, L.VVVVS205, L.VVVVS206, L.VVVVS207, L.VVVVS29, L.VVVVS3, L.VVVVS4, L.VVVVS9, L.VVVVS95 ],
               couplings = {(0,5):C.GC_3510,(0,1):C.GC_3759,(0,0):C.GC_3187,(0,10):C.GC_3482,(0,11):C.GC_3156,(0,12):C.GC_4514,(0,8):C.GC_3194,(0,3):C.GC_3410,(0,2):C.GC_3494,(0,7):C.GC_3621,(0,4):C.GC_4495,(0,13):C.GC_3095,(0,9):C.GC_4455,(0,6):C.GC_3167})

V_406 = Vertex(name = 'V_406',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS19, L.VVVVS29, L.VVVVS95 ],
               couplings = {(0,0):C.GC_4313,(0,2):C.GC_3177,(0,1):C.GC_4488})

V_407 = Vertex(name = 'V_407',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV135, L.VVVVV136, L.VVVVV137, L.VVVVV152, L.VVVVV153, L.VVVVV159, L.VVVVV17, L.VVVVV40, L.VVVVV42, L.VVVVV50, L.VVVVV51, L.VVVVV54, L.VVVVV59, L.VVVVV76, L.VVVVV77, L.VVVVV8, L.VVVVV99 ],
               couplings = {(0,13):C.GC_4050,(0,14):C.GC_4087,(0,6):C.GC_41,(0,16):C.GC_515,(0,15):C.GC_43,(0,9):C.GC_505,(0,3):C.GC_472,(0,4):C.GC_484,(0,12):C.GC_42,(0,5):C.GC_44,(0,2):C.GC_4047,(0,1):C.GC_4049,(0,0):C.GC_4090,(0,7):C.GC_4001,(0,8):C.GC_4085,(0,10):C.GC_4706,(0,11):C.GC_4048})

V_408 = Vertex(name = 'V_408',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV137, L.VVVVV159, L.VVVVV51, L.VVVVV54, L.VVVVV59, L.VVVVV76 ],
               couplings = {(0,5):C.GC_4097,(0,4):C.GC_461,(0,1):C.GC_468,(0,0):C.GC_4071,(0,2):C.GC_4712,(0,3):C.GC_4067})

V_409 = Vertex(name = 'V_409',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV12, L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV134, L.VVVVV138, L.VVVVV145, L.VVVVV146, L.VVVVV15, L.VVVVV157, L.VVVVV29, L.VVVVV30, L.VVVVV37, L.VVVVV65, L.VVVVV70, L.VVVVV78, L.VVVVV90 ],
               couplings = {(0,13):C.GC_3979,(0,15):C.GC_4807,(0,14):C.GC_4114,(0,9):C.GC_1585,(0,0):C.GC_1587,(0,17):C.GC_2024,(0,16):C.GC_2018,(0,7):C.GC_1997,(0,8):C.GC_2006,(0,10):C.GC_1588,(0,12):C.GC_4006,(0,6):C.GC_1586,(0,11):C.GC_4075,(0,2):C.GC_3977,(0,4):C.GC_3978,(0,1):C.GC_4790,(0,5):C.GC_4007,(0,3):C.GC_4728})

V_410 = Vertex(name = 'V_410',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV122, L.VVVVV123, L.VVVVV124, L.VVVVV126, L.VVVVV138, L.VVVVV157, L.VVVVV37, L.VVVVV65 ],
               couplings = {(0,6):C.GC_4010,(0,7):C.GC_4135,(0,5):C.GC_1995,(0,4):C.GC_1990,(0,1):C.GC_3999,(0,3):C.GC_3997,(0,0):C.GC_4130,(0,2):C.GC_4754})

V_411 = Vertex(name = 'V_411',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV100, L.VVVVV101, L.VVVVV115, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV14, L.VVVVV140, L.VVVVV142, L.VVVVV143, L.VVVVV147, L.VVVVV148, L.VVVVV155, L.VVVVV156, L.VVVVV16, L.VVVVV23, L.VVVVV28, L.VVVVV3, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV38, L.VVVVV39, L.VVVVV6, L.VVVVV64, L.VVVVV68, L.VVVVV69, L.VVVVV7, L.VVVVV79, L.VVVVV81, L.VVVVV91, L.VVVVV92 ],
               couplings = {(0,17):C.GC_4733,(0,19):C.GC_4753,(0,27):C.GC_4829,(0,29):C.GC_4840,(0,0):C.GC_1600,(0,15):C.GC_2055,(0,16):C.GC_2008,(0,31):C.GC_2280,(0,18):C.GC_1598,(0,30):C.GC_2061,(0,20):C.GC_2010,(0,34):C.GC_2284,(0,26):C.GC_2057,(0,33):C.GC_2273,(0,7):C.GC_2059,(0,21):C.GC_2266,(0,8):C.GC_2029,(0,11):C.GC_2257,(0,10):C.GC_2264,(0,9):C.GC_2268,(0,12):C.GC_2286,(0,14):C.GC_2058,(0,13):C.GC_2062,(0,22):C.GC_2009,(0,23):C.GC_1599,(0,24):C.GC_2260,(0,25):C.GC_2056,(0,2):C.GC_2060,(0,6):C.GC_4734,(0,3):C.GC_4751,(0,4):C.GC_4828,(0,32):C.GC_2002,(0,1):C.GC_1597,(0,28):C.GC_4749,(0,5):C.GC_4732})

V_412 = Vertex(name = 'V_412',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV100, L.VVVVV101, L.VVVVV116, L.VVVVV117, L.VVVVV118, L.VVVVV155, L.VVVVV156, L.VVVVV28, L.VVVVV36, L.VVVVV39, L.VVVVV64 ],
               couplings = {(0,7):C.GC_4759,(0,10):C.GC_4846,(0,6):C.GC_2282,(0,5):C.GC_2256,(0,8):C.GC_2023,(0,9):C.GC_2276,(0,1):C.GC_2254,(0,4):C.GC_4755,(0,2):C.GC_4841,(0,0):C.GC_2014,(0,3):C.GC_4752})

V_413 = Vertex(name = 'V_413',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV10, L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV106, L.VVVVV107, L.VVVVV108, L.VVVVV109, L.VVVVV11, L.VVVVV110, L.VVVVV111, L.VVVVV112, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV125, L.VVVVV13, L.VVVVV141, L.VVVVV150, L.VVVVV151, L.VVVVV160, L.VVVVV161, L.VVVVV18, L.VVVVV19, L.VVVVV24, L.VVVVV25, L.VVVVV27, L.VVVVV41, L.VVVVV43, L.VVVVV44, L.VVVVV45, L.VVVVV46, L.VVVVV49, L.VVVVV52, L.VVVVV53, L.VVVVV57, L.VVVVV58, L.VVVVV60, L.VVVVV61, L.VVVVV62, L.VVVVV74, L.VVVVV84, L.VVVVV86, L.VVVVV87, L.VVVVV88, L.VVVVV89, L.VVVVV9, L.VVVVV93, L.VVVVV94 ],
               couplings = {(0,42):C.GC_4757,(0,25):C.GC_4004,(0,43):C.GC_4126,(0,44):C.GC_4158,(0,32):C.GC_3936,(0,31):C.GC_4057,(0,28):C.GC_4169,(0,9):C.GC_54,(0,24):C.GC_58,(0,45):C.GC_496,(0,46):C.GC_516,(0,0):C.GC_52,(0,47):C.GC_56,(0,26):C.GC_491,(0,49):C.GC_506,(0,30):C.GC_4825,(0,17):C.GC_2298,(0,33):C.GC_2423,(0,23):C.GC_2296,(0,48):C.GC_2419,(0,12):C.GC_485,(0,11):C.GC_493,(0,20):C.GC_473,(0,18):C.GC_520,(0,13):C.GC_55,(0,14):C.GC_59,(0,27):C.GC_2416,(0,19):C.GC_2434,(0,22):C.GC_57,(0,21):C.GC_2295,(0,36):C.GC_2420,(0,37):C.GC_2297,(0,29):C.GC_479,(0,34):C.GC_53,(0,35):C.GC_4864,(0,6):C.GC_3948,(0,5):C.GC_4091,(0,16):C.GC_4837,(0,38):C.GC_4002,(0,40):C.GC_4121,(0,39):C.GC_4154,(0,8):C.GC_4735,(0,3):C.GC_3984,(0,1):C.GC_3985,(0,2):C.GC_4117,(0,7):C.GC_4118,(0,10):C.GC_4151,(0,4):C.GC_4150,(0,41):C.GC_4879,(0,15):C.GC_4865})

V_414 = Vertex(name = 'V_414',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV102, L.VVVVV103, L.VVVVV104, L.VVVVV105, L.VVVVV108, L.VVVVV110, L.VVVVV113, L.VVVVV114, L.VVVVV120, L.VVVVV160, L.VVVVV161, L.VVVVV41, L.VVVVV44, L.VVVVV45, L.VVVVV46, L.VVVVV52, L.VVVVV53, L.VVVVV58 ],
               couplings = {(0,14):C.GC_3951,(0,13):C.GC_4098,(0,11):C.GC_4176,(0,12):C.GC_4844,(0,6):C.GC_510,(0,7):C.GC_469,(0,10):C.GC_462,(0,9):C.GC_2425,(0,17):C.GC_2430,(0,15):C.GC_500,(0,16):C.GC_4881,(0,2):C.GC_4003,(0,0):C.GC_4005,(0,1):C.GC_4123,(0,4):C.GC_4128,(0,5):C.GC_4160,(0,3):C.GC_4156,(0,8):C.GC_4875})

V_415 = Vertex(name = 'V_415',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS104, L.VVVVS108, L.VVVVS187, L.VVVVS211, L.VVVVS42, L.VVVVS43, L.VVVVS51, L.VVVVS6, L.VVVVS8, L.VVVVS97, L.VVVVS98, L.VVVVS99 ],
               couplings = {(0,7):C.GC_3535,(0,2):C.GC_3725,(0,1):C.GC_3846,(0,8):C.GC_3685,(0,0):C.GC_4317,(0,9):C.GC_3828,(0,6):C.GC_4255,(0,3):C.GC_4299,(0,4):C.GC_3698,(0,12):C.GC_3415,(0,10):C.GC_3613,(0,11):C.GC_3853,(0,5):C.GC_3811})

V_416 = Vertex(name = 'V_416',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS42, L.VVVVS43, L.VVVVS97 ],
               couplings = {(0,1):C.GC_4296,(0,2):C.GC_4406,(0,0):C.GC_3839})

V_417 = Vertex(name = 'V_417',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV131, L.VVVVV132, L.VVVVV133, L.VVVVV149, L.VVVVV154, L.VVVVV158, L.VVVVV162, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV32, L.VVVVV63, L.VVVVV66, L.VVVVV67, L.VVVVV71, L.VVVVV72, L.VVVVV73, L.VVVVV75, L.VVVVV83, L.VVVVV85, L.VVVVV95, L.VVVVV96, L.VVVVV97, L.VVVVV98 ],
               couplings = {(0,24):C.GC_4877,(0,25):C.GC_4808,(0,14):C.GC_2511,(0,29):C.GC_2025,(0,28):C.GC_2272,(0,15):C.GC_1596,(0,13):C.GC_2059,(0,27):C.GC_2019,(0,26):C.GC_2267,(0,16):C.GC_2261,(0,12):C.GC_2510,(0,10):C.GC_2752,(0,20):C.GC_3941,(0,19):C.GC_3986,(0,21):C.GC_4076,(0,17):C.GC_4119,(0,9):C.GC_2745,(0,11):C.GC_2512,(0,5):C.GC_4796,(0,3):C.GC_4826,(0,6):C.GC_4008,(0,7):C.GC_4055,(0,4):C.GC_4056,(0,8):C.GC_4131,(0,2):C.GC_4168,(0,23):C.GC_4838,(0,18):C.GC_4152,(0,22):C.GC_4171,(0,1):C.GC_4827,(0,0):C.GC_4167})

V_418 = Vertex(name = 'V_418',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV119, L.VVVVV121, L.VVVVV127, L.VVVVV128, L.VVVVV129, L.VVVVV130, L.VVVVV132, L.VVVVV158, L.VVVVV162, L.VVVVV63, L.VVVVV66, L.VVVVV67 ],
               couplings = {(0,8):C.GC_2747,(0,11):C.GC_4011,(0,9):C.GC_4136,(0,7):C.GC_2749,(0,5):C.GC_4686,(0,3):C.GC_4842,(0,6):C.GC_4078,(0,4):C.GC_4082,(0,2):C.GC_4174,(0,10):C.GC_4163,(0,1):C.GC_4835,(0,0):C.GC_4172})

V_419 = Vertex(name = 'V_419',
               particles = [ P.a, P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS133 ],
               couplings = {(0,0):C.GC_2771})

V_420 = Vertex(name = 'V_420',
               particles = [ P.a, P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS133 ],
               couplings = {(0,0):C.GC_2901})

V_421 = Vertex(name = 'V_421',
               particles = [ P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS160, L.VVVSS161, L.VVVSS39, L.VVVSS91 ],
               couplings = {(0,2):C.GC_1595,(0,1):C.GC_2054,(0,0):C.GC_2438,(0,3):C.GC_2991})

V_422 = Vertex(name = 'V_422',
               particles = [ P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS160, L.VVVSS161, L.VVVSS39 ],
               couplings = {(0,2):C.GC_1940,(0,1):C.GC_2250,(0,0):C.GC_2477})

V_423 = Vertex(name = 'V_423',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS148 ],
               couplings = {(0,0):C.GC_2772})

V_424 = Vertex(name = 'V_424',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS148 ],
               couplings = {(0,0):C.GC_2902})

V_425 = Vertex(name = 'V_425',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVS127, L.VVVVS221 ],
               couplings = {(0,0):C.GC_3531,(0,1):C.GC_3385})

V_426 = Vertex(name = 'V_426',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV144, L.VVVVV2, L.VVVVV26, L.VVVVV4, L.VVVVV47, L.VVVVV48, L.VVVVV5, L.VVVVV55, L.VVVVV56, L.VVVVV80, L.VVVVV82 ],
               couplings = {(0,4):C.GC_2775,(0,2):C.GC_56,(0,7):C.GC_2294,(0,3):C.GC_492,(0,5):C.GC_497,(0,10):C.GC_2428,(0,6):C.GC_2432,(0,8):C.GC_2944,(0,1):C.GC_2941,(0,9):C.GC_2776,(0,11):C.GC_480,(0,0):C.GC_2774})

V_427 = Vertex(name = 'V_427',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV139, L.VVVVV56 ],
               couplings = {(0,1):C.GC_2939,(0,0):C.GC_2936})

V_428 = Vertex(name = 'V_428',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSS91 ],
               couplings = {(0,0):C.GC_2991})

V_429 = Vertex(name = 'V_429',
               particles = [ P.a, P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1, L.VVSSSS28 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_427})

V_430 = Vertex(name = 'V_430',
               particles = [ P.a, P.a, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_456})

V_431 = Vertex(name = 'V_431',
               particles = [ P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_79})

V_432 = Vertex(name = 'V_432',
               particles = [ P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_457,(0,1):C.GC_413})

V_433 = Vertex(name = 'V_433',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS16, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_427})

V_434 = Vertex(name = 'V_434',
               particles = [ P.a, P.a, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS16 ],
               couplings = {(0,0):C.GC_456})

V_435 = Vertex(name = 'V_435',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_795,(0,1):C.GC_1968})

V_436 = Vertex(name = 'V_436',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2 ],
               couplings = {(0,0):C.GC_893})

V_437 = Vertex(name = 'V_437',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_1616,(0,0):C.GC_1623,(0,1):C.GC_1970})

V_438 = Vertex(name = 'V_438',
               particles = [ P.a, P.W__minus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS7 ],
               couplings = {(0,1):C.GC_1985,(0,0):C.GC_1959})

V_439 = Vertex(name = 'V_439',
               particles = [ P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS52, L.VVSSSS54, L.VVSSSS68 ],
               couplings = {(0,0):C.GC_1969,(0,1):C.GC_1615,(0,2):C.GC_1622})

V_440 = Vertex(name = 'V_440',
               particles = [ P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS54, L.VVSSSS68 ],
               couplings = {(0,0):C.GC_1984,(0,1):C.GC_1958})

V_441 = Vertex(name = 'V_441',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS81, L.VVVSSS92 ],
               couplings = {(0,0):C.GC_3648,(0,1):C.GC_3636})

V_442 = Vertex(name = 'V_442',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS81, L.VVVSSS92 ],
               couplings = {(0,0):C.GC_3783,(0,1):C.GC_4421})

V_443 = Vertex(name = 'V_443',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS31, L.VVSSSS41, L.VVSSSS96 ],
               couplings = {(0,1):C.GC_1624,(0,2):C.GC_1617,(0,0):C.GC_1970})

V_444 = Vertex(name = 'V_444',
               particles = [ P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS41, L.VVSSSS96 ],
               couplings = {(0,0):C.GC_1960,(0,1):C.GC_1986})

V_445 = Vertex(name = 'V_445',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_1613,(0,1):C.GC_1620,(0,2):C.GC_1968})

V_446 = Vertex(name = 'V_446',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19 ],
               couplings = {(0,0):C.GC_1982,(0,1):C.GC_1956})

V_447 = Vertex(name = 'V_447',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_796,(0,1):C.GC_1970})

V_448 = Vertex(name = 'V_448',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23 ],
               couplings = {(0,0):C.GC_894})

V_449 = Vertex(name = 'V_449',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_3429,(0,0):C.GC_3575,(0,1):C.GC_3428})

V_450 = Vertex(name = 'V_450',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,1):C.GC_3560,(0,0):C.GC_3591})

V_451 = Vertex(name = 'V_451',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1161,(0,0):C.GC_1489,(0,2):C.GC_1164})

V_452 = Vertex(name = 'V_452',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,0):C.GC_1507,(0,1):C.GC_1462})

V_453 = Vertex(name = 'V_453',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_1163,(0,0):C.GC_1486,(0,2):C.GC_1162})

V_454 = Vertex(name = 'V_454',
               particles = [ P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,0):C.GC_1461,(0,1):C.GC_1508})

V_455 = Vertex(name = 'V_455',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_3425,(0,0):C.GC_3576,(0,1):C.GC_3431})

V_456 = Vertex(name = 'V_456',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,1):C.GC_3589,(0,0):C.GC_3562})

V_457 = Vertex(name = 'V_457',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1160,(0,0):C.GC_1488,(0,2):C.GC_1165})

V_458 = Vertex(name = 'V_458',
               particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,0):C.GC_1506,(0,1):C.GC_1463})

V_459 = Vertex(name = 'V_459',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_4062,(0,1):C.GC_4064})

V_460 = Vertex(name = 'V_460',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_4778,(0,1):C.GC_4103})

V_461 = Vertex(name = 'V_461',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2, L.VVSSSS35 ],
               couplings = {(0,0):C.GC_795,(0,1):C.GC_1968})

V_462 = Vertex(name = 'V_462',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS2 ],
               couplings = {(0,0):C.GC_893})

V_463 = Vertex(name = 'V_463',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS28, L.VVSSSS7 ],
               couplings = {(0,2):C.GC_1612,(0,0):C.GC_1619,(0,1):C.GC_1967})

V_464 = Vertex(name = 'V_464',
               particles = [ P.a, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS10, L.VVSSSS7 ],
               couplings = {(0,1):C.GC_1981,(0,0):C.GC_1955})

V_465 = Vertex(name = 'V_465',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS45, L.VVVSSS76 ],
               couplings = {(0,1):C.GC_3636,(0,0):C.GC_3648})

V_466 = Vertex(name = 'V_466',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS45, L.VVVSSS76 ],
               couplings = {(0,1):C.GC_4421,(0,0):C.GC_3783})

V_467 = Vertex(name = 'V_467',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS40, L.VVSSSS73, L.VVSSSS95 ],
               couplings = {(0,2):C.GC_1968,(0,0):C.GC_1621,(0,1):C.GC_1614})

V_468 = Vertex(name = 'V_468',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS40, L.VVSSSS73 ],
               couplings = {(0,0):C.GC_1957,(0,1):C.GC_1983})

V_469 = Vertex(name = 'V_469',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS34, L.VVSSSS44, L.VVSSSS67 ],
               couplings = {(0,1):C.GC_1617,(0,0):C.GC_1970,(0,2):C.GC_1618})

V_470 = Vertex(name = 'V_470',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS44, L.VVSSSS67 ],
               couplings = {(0,0):C.GC_1986,(0,1):C.GC_1954})

V_471 = Vertex(name = 'V_471',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19, L.VVSSSS29 ],
               couplings = {(0,0):C.GC_1613,(0,1):C.GC_1620,(0,2):C.GC_1968})

V_472 = Vertex(name = 'V_472',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS12, L.VVSSSS19 ],
               couplings = {(0,0):C.GC_1982,(0,1):C.GC_1956})

V_473 = Vertex(name = 'V_473',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_794,(0,1):C.GC_1967})

V_474 = Vertex(name = 'V_474',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS23 ],
               couplings = {(0,0):C.GC_892})

V_475 = Vertex(name = 'V_475',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS107, L.VVVVSS110, L.VVVVSS186, L.VVVVSS202, L.VVVVSS208, L.VVVVSS219, L.VVVVSS291, L.VVVVSS294, L.VVVVSS314, L.VVVVSS324, L.VVVVSS356, L.VVVVSS55, L.VVVVSS65, L.VVVVSS66 ],
               couplings = {(0,11):C.GC_1853,(0,2):C.GC_386,(0,0):C.GC_358,(0,1):C.GC_1776,(0,8):C.GC_194,(0,13):C.GC_1356,(0,6):C.GC_1878,(0,9):C.GC_75,(0,7):C.GC_1803,(0,10):C.GC_71,(0,5):C.GC_1630,(0,3):C.GC_4061,(0,12):C.GC_4063,(0,4):C.GC_1197})

V_476 = Vertex(name = 'V_476',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS202, L.VVVVSS219, L.VVVVSS356, L.VVVVSS65 ],
               couplings = {(0,2):C.GC_173,(0,1):C.GC_1826,(0,0):C.GC_4777,(0,3):C.GC_4102})

V_477 = Vertex(name = 'V_477',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS101, L.VVSSSS103, L.VVSSSS57 ],
               couplings = {(0,1):C.GC_1159,(0,2):C.GC_1166,(0,0):C.GC_1487})

V_478 = Vertex(name = 'V_478',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS103, L.VVSSSS57 ],
               couplings = {(0,0):C.GC_1505,(0,1):C.GC_1464})

V_479 = Vertex(name = 'V_479',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS42, L.VVVSSS43, L.VVVSSS9 ],
               couplings = {(0,0):C.GC_3425,(0,1):C.GC_3576,(0,2):C.GC_3432})

V_480 = Vertex(name = 'V_480',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS42, L.VVVSSS9 ],
               couplings = {(0,0):C.GC_3589,(0,1):C.GC_3563})

V_481 = Vertex(name = 'V_481',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS58, L.VVSSSS86, L.VVSSSS88 ],
               couplings = {(0,1):C.GC_1160,(0,2):C.GC_1488,(0,0):C.GC_1167})

V_482 = Vertex(name = 'V_482',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS58, L.VVSSSS86 ],
               couplings = {(0,1):C.GC_1506,(0,0):C.GC_1465})

V_483 = Vertex(name = 'V_483',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS21 ],
               couplings = {(0,0):C.GC_3427,(0,1):C.GC_3433})

V_484 = Vertex(name = 'V_484',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS21 ],
               couplings = {(0,0):C.GC_4337,(0,1):C.GC_3564})

V_485 = Vertex(name = 'V_485',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_587,(0,0):C.GC_1488})

V_486 = Vertex(name = 'V_486',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS26 ],
               couplings = {(0,0):C.GC_720})

V_487 = Vertex(name = 'V_487',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS17, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_587,(0,1):C.GC_1488})

V_488 = Vertex(name = 'V_488',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS17 ],
               couplings = {(0,0):C.GC_720})

V_489 = Vertex(name = 'V_489',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS18, L.VVSSSS8, L.VVSSSS81 ],
               couplings = {(0,1):C.GC_1158,(0,0):C.GC_1486,(0,2):C.GC_1169})

V_490 = Vertex(name = 'V_490',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS8, L.VVSSSS81 ],
               couplings = {(0,0):C.GC_1504,(0,1):C.GC_1467})

V_491 = Vertex(name = 'V_491',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS60, L.VVSSSS9 ],
               couplings = {(0,0):C.GC_1166,(0,2):C.GC_1160,(0,1):C.GC_1488})

V_492 = Vertex(name = 'V_492',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS9 ],
               couplings = {(0,0):C.GC_1464,(0,1):C.GC_1506})

V_493 = Vertex(name = 'V_493',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS13 ],
               couplings = {(0,0):C.GC_586})

V_494 = Vertex(name = 'V_494',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS13 ],
               couplings = {(0,0):C.GC_721})

V_495 = Vertex(name = 'V_495',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS6 ],
               couplings = {(0,0):C.GC_586})

V_496 = Vertex(name = 'V_496',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS6 ],
               couplings = {(0,0):C.GC_721})

V_497 = Vertex(name = 'V_497',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_587,(0,0):C.GC_1170})

V_498 = Vertex(name = 'V_498',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS26 ],
               couplings = {(0,1):C.GC_720,(0,0):C.GC_1488})

V_499 = Vertex(name = 'V_499',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS13, L.VVVVSS15, L.VVVVSS181, L.VVVVSS200, L.VVVVSS257, L.VVVVSS277, L.VVVVSS278, L.VVVVSS28, L.VVVVSS29, L.VVVVSS332, L.VVVVSS344, L.VVVVSS37 ],
               couplings = {(0,1):C.GC_1389,(0,2):C.GC_1921,(0,8):C.GC_1332,(0,0):C.GC_1900,(0,5):C.GC_1405,(0,9):C.GC_1610,(0,10):C.GC_1742,(0,4):C.GC_1606,(0,11):C.GC_1175,(0,6):C.GC_1357,(0,7):C.GC_3991,(0,3):C.GC_3988})

V_500 = Vertex(name = 'V_500',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS200, L.VVVVSS257, L.VVVVSS28, L.VVVVSS37 ],
               couplings = {(0,1):C.GC_1717,(0,3):C.GC_1372,(0,2):C.GC_4019,(0,0):C.GC_4718})

V_501 = Vertex(name = 'V_501',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS14, L.VVVVSS15, L.VVVVSS177, L.VVVVSS200, L.VVVVSS254, L.VVVVSS277, L.VVVVSS278, L.VVVVSS28, L.VVVVSS29, L.VVVVSS334, L.VVVVSS341, L.VVVVSS37 ],
               couplings = {(0,1):C.GC_1388,(0,2):C.GC_1920,(0,8):C.GC_1331,(0,0):C.GC_1898,(0,5):C.GC_1404,(0,10):C.GC_1609,(0,9):C.GC_1743,(0,4):C.GC_1605,(0,11):C.GC_1176,(0,6):C.GC_1358,(0,7):C.GC_3990,(0,3):C.GC_3987})

V_502 = Vertex(name = 'V_502',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS200, L.VVVVSS254, L.VVVVSS28, L.VVVVSS37 ],
               couplings = {(0,1):C.GC_1716,(0,3):C.GC_1373,(0,2):C.GC_4018,(0,0):C.GC_4717})

V_503 = Vertex(name = 'V_503',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS2, L.VVVSSS95 ],
               couplings = {(0,0):C.GC_3265,(0,1):C.GC_3260})

V_504 = Vertex(name = 'V_504',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS2, L.VVVSSS95 ],
               couplings = {(0,0):C.GC_3345,(0,1):C.GC_4237})

V_505 = Vertex(name = 'V_505',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS28, L.VVVSSS39, L.VVVSSS44 ],
               couplings = {(0,2):C.GC_3262,(0,0):C.GC_3268,(0,1):C.GC_3363})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS28, L.VVVSSS44 ],
               couplings = {(0,1):C.GC_3371,(0,0):C.GC_3347})

V_507 = Vertex(name = 'V_507',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS26, L.VVVSSS89, L.VVVSSS91 ],
               couplings = {(0,2):C.GC_3264,(0,0):C.GC_3263,(0,1):C.GC_3361})

V_508 = Vertex(name = 'V_508',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS26, L.VVVSSS91 ],
               couplings = {(0,1):C.GC_3344,(0,0):C.GC_3372})

V_509 = Vertex(name = 'V_509',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS100, L.VVVSSS7 ],
               couplings = {(0,1):C.GC_3259,(0,0):C.GC_3266})

V_510 = Vertex(name = 'V_510',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS100, L.VVVSSS7 ],
               couplings = {(0,1):C.GC_3369,(0,0):C.GC_4234})

V_511 = Vertex(name = 'V_511',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS16, L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,2):C.GC_3429,(0,0):C.GC_3575,(0,1):C.GC_3428})

V_512 = Vertex(name = 'V_512',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS57 ],
               couplings = {(0,1):C.GC_3560,(0,0):C.GC_3591})

V_513 = Vertex(name = 'V_513',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1161,(0,0):C.GC_1489,(0,2):C.GC_1164})

V_514 = Vertex(name = 'V_514',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,0):C.GC_1507,(0,1):C.GC_1462})

V_515 = Vertex(name = 'V_515',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS25, L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,1):C.GC_1168,(0,0):C.GC_1490,(0,2):C.GC_1157})

V_516 = Vertex(name = 'V_516',
               particles = [ P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS36, L.VVSSSS72 ],
               couplings = {(0,0):C.GC_1466,(0,1):C.GC_1503})

V_517 = Vertex(name = 'V_517',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS17, L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,2):C.GC_3426,(0,0):C.GC_3577,(0,1):C.GC_3430})

V_518 = Vertex(name = 'V_518',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS36, L.VVVSSS55 ],
               couplings = {(0,1):C.GC_3590,(0,0):C.GC_3561})

V_519 = Vertex(name = 'V_519',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS22, L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,1):C.GC_1160,(0,0):C.GC_1488,(0,2):C.GC_1165})

V_520 = Vertex(name = 'V_520',
               particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS46, L.VVSSSS62 ],
               couplings = {(0,0):C.GC_1506,(0,1):C.GC_1463})

V_521 = Vertex(name = 'V_521',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS24, L.VVVSSS34 ],
               couplings = {(0,2):C.GC_3267,(0,0):C.GC_3362,(0,1):C.GC_3261})

V_522 = Vertex(name = 'V_522',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS24, L.VVVSSS34 ],
               couplings = {(0,1):C.GC_3346,(0,0):C.GC_3370})

V_523 = Vertex(name = 'V_523',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS13, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_3266,(0,1):C.GC_3259})

V_524 = Vertex(name = 'V_524',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS13, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_4234,(0,1):C.GC_3369})

V_525 = Vertex(name = 'V_525',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS23, L.VVVSSS80 ],
               couplings = {(0,2):C.GC_3258,(0,0):C.GC_3361,(0,1):C.GC_3269})

V_526 = Vertex(name = 'V_526',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS23, L.VVVSSS80 ],
               couplings = {(0,1):C.GC_3368,(0,0):C.GC_3348})

V_527 = Vertex(name = 'V_527',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS194, L.VVVVSS236, L.VVVVSS281, L.VVVVSS359, L.VVVVSS47, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1434,(0,2):C.GC_1154,(0,1):C.GC_1313,(0,4):C.GC_1422,(0,3):C.GC_1153,(0,5):C.GC_3955,(0,6):C.GC_3954})

V_528 = Vertex(name = 'V_528',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS359, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1298,(0,1):C.GC_4697,(0,2):C.GC_3968})

V_529 = Vertex(name = 'V_529',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_4062,(0,1):C.GC_4064})

V_530 = Vertex(name = 'V_530',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_4778,(0,1):C.GC_4103})

V_531 = Vertex(name = 'V_531',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS189, L.VVVVSS203, L.VVVVSS21, L.VVVVSS24, L.VVVVSS273, L.VVVVSS279, L.VVVVSS282, L.VVVVSS287, L.VVVVSS65, L.VVVVSS73, L.VVVVSS77, L.VVVVSS86 ],
               couplings = {(0,3):C.GC_1390,(0,0):C.GC_1921,(0,11):C.GC_1333,(0,2):C.GC_1899,(0,4):C.GC_1406,(0,6):C.GC_1611,(0,7):C.GC_1742,(0,1):C.GC_1174,(0,5):C.GC_1357,(0,9):C.GC_1607,(0,8):C.GC_3988,(0,10):C.GC_3991})

V_532 = Vertex(name = 'V_532',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS203, L.VVVVSS65, L.VVVVSS73, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1371,(0,2):C.GC_1718,(0,1):C.GC_4718,(0,3):C.GC_4019})

V_533 = Vertex(name = 'V_533',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS174, L.VVVVSS20, L.VVVVSS203, L.VVVVSS24, L.VVVVSS273, L.VVVVSS279, L.VVVVSS305, L.VVVVSS325, L.VVVVSS65, L.VVVVSS70, L.VVVVSS77, L.VVVVSS86 ],
               couplings = {(0,3):C.GC_1388,(0,0):C.GC_1922,(0,11):C.GC_1331,(0,1):C.GC_1898,(0,4):C.GC_1404,(0,7):C.GC_1609,(0,6):C.GC_1741,(0,2):C.GC_1176,(0,5):C.GC_1359,(0,9):C.GC_1608,(0,8):C.GC_3989,(0,10):C.GC_3992})

V_534 = Vertex(name = 'V_534',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS203, L.VVVVSS65, L.VVVVSS70, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1373,(0,2):C.GC_1719,(0,1):C.GC_4719,(0,3):C.GC_4020})

V_535 = Vertex(name = 'V_535',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS19, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_3260,(0,1):C.GC_3265})

V_536 = Vertex(name = 'V_536',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS19, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_4237,(0,1):C.GC_3345})

V_537 = Vertex(name = 'V_537',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS193, L.VVVVSS236, L.VVVVSS321, L.VVVVSS359, L.VVVVSS47, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1434,(0,2):C.GC_1154,(0,1):C.GC_1313,(0,4):C.GC_1422,(0,3):C.GC_1153,(0,5):C.GC_3953,(0,6):C.GC_3956})

V_538 = Vertex(name = 'V_538',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS359, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1298,(0,1):C.GC_4698,(0,2):C.GC_3965})

V_539 = Vertex(name = 'V_539',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS175, L.VVVVSS193, L.VVVVSS236, L.VVVVSS321, L.VVVVSS331, L.VVVVSS359, L.VVVVSS47, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1156,(0,1):C.GC_1434,(0,2):C.GC_1152,(0,3):C.GC_1154,(0,4):C.GC_1450,(0,6):C.GC_1422,(0,5):C.GC_1153,(0,7):C.GC_4690,(0,8):C.GC_3957})

V_540 = Vertex(name = 'V_540',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS175, L.VVVVSS236, L.VVVVSS359, L.VVVVSS65, L.VVVVSS77 ],
               couplings = {(0,0):C.GC_1457,(0,1):C.GC_1313,(0,2):C.GC_1298,(0,3):C.GC_4699,(0,4):C.GC_3966})

V_541 = Vertex(name = 'V_541',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS29 ],
               couplings = {(0,0):C.GC_4531,(0,1):C.GC_4472})

V_542 = Vertex(name = 'V_542',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS29 ],
               couplings = {(0,0):C.GC_4549})

V_543 = Vertex(name = 'V_543',
               particles = [ P.a, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS28, L.VVSSSS53, L.VVSSSS59 ],
               couplings = {(0,1):C.GC_2521,(0,2):C.GC_2518,(0,0):C.GC_2662})

V_544 = Vertex(name = 'V_544',
               particles = [ P.a, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS53, L.VVSSSS59 ],
               couplings = {(0,0):C.GC_2658,(0,1):C.GC_2689})

V_545 = Vertex(name = 'V_545',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS20, L.VVSSSS91 ],
               couplings = {(0,0):C.GC_2663,(0,1):C.GC_2523})

V_546 = Vertex(name = 'V_546',
               particles = [ P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS91 ],
               couplings = {(0,0):C.GC_2691})

V_547 = Vertex(name = 'V_547',
               particles = [ P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_2519,(0,1):C.GC_2522})

V_548 = Vertex(name = 'V_548',
               particles = [ P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_2690,(0,1):C.GC_2659})

V_549 = Vertex(name = 'V_549',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS29, L.VVSSSS45, L.VVSSSS51 ],
               couplings = {(0,2):C.GC_2520,(0,1):C.GC_2517,(0,0):C.GC_2662})

V_550 = Vertex(name = 'V_550',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS45, L.VVSSSS51 ],
               couplings = {(0,1):C.GC_2657,(0,0):C.GC_2688})

V_551 = Vertex(name = 'V_551',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_4328,(0,0):C.GC_4259,(0,2):C.GC_4263})

V_552 = Vertex(name = 'V_552',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS63 ],
               couplings = {(0,0):C.GC_4338,(0,1):C.GC_4324})

V_553 = Vertex(name = 'V_553',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_95,(0,3):C.GC_104,(0,2):C.GC_589,(0,1):C.GC_431})

V_554 = Vertex(name = 'V_554',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_443,(0,2):C.GC_417,(0,1):C.GC_723})

V_555 = Vertex(name = 'V_555',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_93,(0,5):C.GC_101,(0,3):C.GC_429,(0,0):C.GC_1184,(0,1):C.GC_1191,(0,2):C.GC_1491})

V_556 = Vertex(name = 'V_556',
               particles = [ P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,2):C.GC_441,(0,3):C.GC_414,(0,0):C.GC_1509,(0,1):C.GC_1470})

V_557 = Vertex(name = 'V_557',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS15, L.VVVSSS67, L.VVVSSS74, L.VVVSSS85, L.VVVSSS86, L.VVVSSS99 ],
               couplings = {(0,4):C.GC_3127,(0,1):C.GC_3129,(0,2):C.GC_3234,(0,3):C.GC_3441,(0,5):C.GC_3442,(0,0):C.GC_3579})

V_558 = Vertex(name = 'V_558',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS67, L.VVVSSS85, L.VVVSSS86, L.VVVSSS99 ],
               couplings = {(0,2):C.GC_3241,(0,0):C.GC_3228,(0,1):C.GC_3592,(0,3):C.GC_3565})

V_559 = Vertex(name = 'V_559',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS14, L.VVSSSS43, L.VVSSSS55, L.VVSSSS56, L.VVSSSS64, L.VVSSSS65 ],
               couplings = {(0,2):C.GC_98,(0,3):C.GC_1186,(0,1):C.GC_432,(0,0):C.GC_1493,(0,5):C.GC_103,(0,4):C.GC_1193})

V_560 = Vertex(name = 'V_560',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS55, L.VVSSSS56, L.VVSSSS64, L.VVSSSS65 ],
               couplings = {(0,0):C.GC_446,(0,1):C.GC_1511,(0,3):C.GC_416,(0,2):C.GC_1472})

V_561 = Vertex(name = 'V_561',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_431,(0,0):C.GC_1493,(0,3):C.GC_96,(0,5):C.GC_103,(0,2):C.GC_1185,(0,4):C.GC_1192})

V_562 = Vertex(name = 'V_562',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_444,(0,3):C.GC_416,(0,0):C.GC_1510,(0,2):C.GC_1471})

V_563 = Vertex(name = 'V_563',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS32, L.VVSSSS38, L.VVSSSS4, L.VVSSSS42, L.VVSSSS97, L.VVSSSS98 ],
               couplings = {(0,5):C.GC_94,(0,1):C.GC_102,(0,0):C.GC_429,(0,4):C.GC_1188,(0,3):C.GC_1190,(0,2):C.GC_1494})

V_564 = Vertex(name = 'V_564',
               particles = [ P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS38, L.VVSSSS42, L.VVSSSS97, L.VVSSSS98 ],
               couplings = {(0,3):C.GC_442,(0,0):C.GC_415,(0,2):C.GC_1513,(0,1):C.GC_1469})

V_565 = Vertex(name = 'V_565',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_4262})

V_566 = Vertex(name = 'V_566',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_4341})

V_567 = Vertex(name = 'V_567',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_99,(0,2):C.GC_102,(0,1):C.GC_588,(0,3):C.GC_428})

V_568 = Vertex(name = 'V_568',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79 ],
               couplings = {(0,0):C.GC_447,(0,2):C.GC_415,(0,1):C.GC_724})

V_569 = Vertex(name = 'V_569',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_4330,(0,0):C.GC_4261,(0,2):C.GC_4265})

V_570 = Vertex(name = 'V_570',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_4340,(0,1):C.GC_4326})

V_571 = Vertex(name = 'V_571',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS198, L.VVVVSS199, L.VVVVSS200 ],
               couplings = {(0,0):C.GC_4711,(0,1):C.GC_4800,(0,2):C.GC_4144})

V_572 = Vertex(name = 'V_572',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS198, L.VVVVSS199 ],
               couplings = {(0,0):C.GC_4721,(0,1):C.GC_4819})

V_573 = Vertex(name = 'V_573',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_4226,(0,2):C.GC_4382,(0,0):C.GC_3794})

V_574 = Vertex(name = 'V_574',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,0):C.GC_4238,(0,1):C.GC_4431})

V_575 = Vertex(name = 'V_575',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_4224,(0,2):C.GC_4381,(0,0):C.GC_3793})

V_576 = Vertex(name = 'V_576',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,0):C.GC_4241,(0,1):C.GC_4430})

V_577 = Vertex(name = 'V_577',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS5, L.VVVSSS63 ],
               couplings = {(0,1):C.GC_4329,(0,0):C.GC_4260,(0,2):C.GC_4264})

V_578 = Vertex(name = 'V_578',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS31, L.VVVSSS63 ],
               couplings = {(0,0):C.GC_4339,(0,1):C.GC_4325})

V_579 = Vertex(name = 'V_579',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS35, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_95,(0,3):C.GC_104,(0,2):C.GC_589,(0,1):C.GC_431})

V_580 = Vertex(name = 'V_580',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS107, L.VVSSSS66, L.VVSSSS80 ],
               couplings = {(0,0):C.GC_443,(0,2):C.GC_417,(0,1):C.GC_723})

V_581 = Vertex(name = 'V_581',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS27, L.VVSSSS30, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,4):C.GC_100,(0,5):C.GC_106,(0,3):C.GC_433,(0,0):C.GC_1187,(0,1):C.GC_1194,(0,2):C.GC_1494})

V_582 = Vertex(name = 'V_582',
               particles = [ P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS102, L.VVSSSS105, L.VVSSSS82, L.VVSSSS83 ],
               couplings = {(0,2):C.GC_448,(0,3):C.GC_419,(0,0):C.GC_1512,(0,1):C.GC_1473})

V_583 = Vertex(name = 'V_583',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS14, L.VVVSSS48, L.VVVSSS49, L.VVVSSS54, L.VVVSSS77, L.VVVSSS97 ],
               couplings = {(0,4):C.GC_3128,(0,2):C.GC_3130,(0,3):C.GC_3235,(0,1):C.GC_3442,(0,0):C.GC_3578,(0,5):C.GC_3441})

V_584 = Vertex(name = 'V_584',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS48, L.VVVSSS49, L.VVVSSS77, L.VVVSSS97 ],
               couplings = {(0,2):C.GC_3242,(0,1):C.GC_3229,(0,0):C.GC_3565,(0,3):C.GC_3592})

V_585 = Vertex(name = 'V_585',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS106, L.VVSSSS24, L.VVSSSS37, L.VVSSSS39, L.VVSSSS74, L.VVSSSS75 ],
               couplings = {(0,3):C.GC_103,(0,2):C.GC_1193,(0,0):C.GC_430,(0,1):C.GC_1492,(0,4):C.GC_97,(0,5):C.GC_1185})

V_586 = Vertex(name = 'V_586',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS37, L.VVSSSS39, L.VVSSSS74, L.VVSSSS75 ],
               couplings = {(0,1):C.GC_416,(0,0):C.GC_1472,(0,2):C.GC_445,(0,3):C.GC_1510})

V_587 = Vertex(name = 'V_587',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS15, L.VVSSSS84, L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_431,(0,0):C.GC_1493,(0,3):C.GC_96,(0,5):C.GC_103,(0,2):C.GC_1185,(0,4):C.GC_1192})

V_588 = Vertex(name = 'V_588',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS87, L.VVSSSS90, L.VVSSSS92, L.VVSSSS94 ],
               couplings = {(0,1):C.GC_444,(0,3):C.GC_416,(0,0):C.GC_1510,(0,2):C.GC_1471})

V_589 = Vertex(name = 'V_589',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS33, L.VVSSSS49, L.VVSSSS5, L.VVSSSS50, L.VVSSSS69, L.VVSSSS70 ],
               couplings = {(0,1):C.GC_94,(0,0):C.GC_429,(0,3):C.GC_1188,(0,2):C.GC_1494,(0,5):C.GC_107,(0,4):C.GC_1189})

V_590 = Vertex(name = 'V_590',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS49, L.VVSSSS50, L.VVSSSS69, L.VVSSSS70 ],
               couplings = {(0,0):C.GC_442,(0,1):C.GC_1513,(0,3):C.GC_420,(0,2):C.GC_1468})

V_591 = Vertex(name = 'V_591',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_4262})

V_592 = Vertex(name = 'V_592',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS68 ],
               couplings = {(0,0):C.GC_4341})

V_593 = Vertex(name = 'V_593',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79, L.VVSSSS99 ],
               couplings = {(0,0):C.GC_94,(0,2):C.GC_105,(0,1):C.GC_590,(0,3):C.GC_434})

V_594 = Vertex(name = 'V_594',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS76, L.VVSSSS77, L.VVSSSS79 ],
               couplings = {(0,0):C.GC_442,(0,2):C.GC_418,(0,1):C.GC_722})

V_595 = Vertex(name = 'V_595',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS166, L.VVVVSS18, L.VVVVSS180, L.VVVVSS182, L.VVVVSS196, L.VVVVSS201, L.VVVVSS212, L.VVVVSS226, L.VVVVSS26, L.VVVVSS264, L.VVVVSS274, L.VVVVSS276, L.VVVVSS28, L.VVVVSS288, L.VVVVSS301, L.VVVVSS307, L.VVVVSS315, L.VVVVSS316, L.VVVVSS33, L.VVVVSS342, L.VVVVSS35, L.VVVVSS358, L.VVVVSS36, L.VVVVSS79, L.VVVVSS80 ],
               couplings = {(0,0):C.GC_316,(0,8):C.GC_1391,(0,3):C.GC_1923,(0,2):C.GC_2245,(0,18):C.GC_1902,(0,24):C.GC_232,(0,23):C.GC_1335,(0,1):C.GC_2224,(0,17):C.GC_266,(0,16):C.GC_338,(0,11):C.GC_1361,(0,10):C.GC_1407,(0,15):C.GC_1640,(0,13):C.GC_2084,(0,19):C.GC_1745,(0,14):C.GC_2122,(0,7):C.GC_1792,(0,9):C.GC_65,(0,6):C.GC_1199,(0,21):C.GC_1638,(0,20):C.GC_2082,(0,22):C.GC_1627,(0,12):C.GC_3995,(0,4):C.GC_3996,(0,5):C.GC_4799})

V_596 = Vertex(name = 'V_596',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS196, L.VVVVSS201, L.VVVVSS212, L.VVVVSS264, L.VVVVSS28, L.VVVVSS35, L.VVVVSS358 ],
               couplings = {(0,3):C.GC_294,(0,2):C.GC_1375,(0,6):C.GC_1720,(0,5):C.GC_2114,(0,4):C.GC_4720,(0,0):C.GC_4021,(0,1):C.GC_4818})

V_597 = Vertex(name = 'V_597',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS101, L.VVVSSS8 ],
               couplings = {(0,1):C.GC_4412,(0,0):C.GC_4377})

V_598 = Vertex(name = 'V_598',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS101 ],
               couplings = {(0,0):C.GC_4426})

V_599 = Vertex(name = 'V_599',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_4378})

V_600 = Vertex(name = 'V_600',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_4427})

V_601 = Vertex(name = 'V_601',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS6, L.VVVSSS89 ],
               couplings = {(0,0):C.GC_4411,(0,1):C.GC_4375})

V_602 = Vertex(name = 'V_602',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS89 ],
               couplings = {(0,0):C.GC_4424})

V_603 = Vertex(name = 'V_603',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS27, L.VVVSSS30 ],
               couplings = {(0,0):C.GC_3274,(0,1):C.GC_3277,(0,2):C.GC_4376})

V_604 = Vertex(name = 'V_604',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS27, L.VVVSSS30 ],
               couplings = {(0,0):C.GC_4239,(0,1):C.GC_3350,(0,2):C.GC_4425})

V_605 = Vertex(name = 'V_605',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS3, L.VVVSSS40, L.VVVSSS62, L.VVVSSS65, L.VVVSSS72, L.VVVSSS96 ],
               couplings = {(0,4):C.GC_3275,(0,2):C.GC_3276,(0,0):C.GC_3364,(0,1):C.GC_3650,(0,3):C.GC_3651,(0,5):C.GC_3791})

V_606 = Vertex(name = 'V_606',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS40, L.VVVSSS62, L.VVVSSS65, L.VVVSSS72 ],
               couplings = {(0,3):C.GC_3373,(0,1):C.GC_3349,(0,0):C.GC_3801,(0,2):C.GC_3784})

V_607 = Vertex(name = 'V_607',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_4379})

V_608 = Vertex(name = 'V_608',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS71 ],
               couplings = {(0,0):C.GC_4428})

V_609 = Vertex(name = 'V_609',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS12, L.VVVVSS142, L.VVVVSS178, L.VVVVSS185, L.VVVVSS195, L.VVVVSS202, L.VVVVSS224, L.VVVVSS255, L.VVVVSS290, L.VVVVSS309, L.VVVVSS327, L.VVVVSS337, L.VVVVSS349, L.VVVVSS45, L.VVVVSS61, L.VVVVSS65, L.VVVVSS67 ],
               couplings = {(0,4):C.GC_388,(0,15):C.GC_1849,(0,3):C.GC_1436,(0,0):C.GC_1425,(0,1):C.GC_1771,(0,9):C.GC_91,(0,7):C.GC_197,(0,8):C.GC_1603,(0,10):C.GC_1182,(0,13):C.GC_1316,(0,12):C.GC_1799,(0,11):C.GC_1872,(0,2):C.GC_1177,(0,14):C.GC_360,(0,17):C.GC_88,(0,5):C.GC_4691,(0,6):C.GC_4743,(0,16):C.GC_4106})

V_610 = Vertex(name = 'V_610',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS142, L.VVVVSS195, L.VVVVSS202, L.VVVVSS255, L.VVVVSS67 ],
               couplings = {(0,3):C.GC_1823,(0,0):C.GC_1299,(0,4):C.GC_175,(0,1):C.GC_4702,(0,2):C.GC_4781})

V_611 = Vertex(name = 'V_611',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS12, L.VVVVSS142, L.VVVVSS178, L.VVVVSS185, L.VVVVSS195, L.VVVVSS202, L.VVVVSS224, L.VVVVSS255, L.VVVVSS290, L.VVVVSS309, L.VVVVSS327, L.VVVVSS337, L.VVVVSS349, L.VVVVSS45, L.VVVVSS61, L.VVVVSS65, L.VVVVSS67 ],
               couplings = {(0,4):C.GC_389,(0,15):C.GC_1850,(0,3):C.GC_1437,(0,0):C.GC_1423,(0,1):C.GC_1772,(0,9):C.GC_90,(0,7):C.GC_196,(0,8):C.GC_1604,(0,10):C.GC_1180,(0,13):C.GC_1314,(0,12):C.GC_1802,(0,11):C.GC_1871,(0,2):C.GC_1179,(0,14):C.GC_359,(0,17):C.GC_89,(0,5):C.GC_4693,(0,6):C.GC_4745,(0,16):C.GC_4107})

V_612 = Vertex(name = 'V_612',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS142, L.VVVVSS195, L.VVVVSS202, L.VVVVSS255, L.VVVVSS67 ],
               couplings = {(0,3):C.GC_1824,(0,0):C.GC_1301,(0,4):C.GC_176,(0,1):C.GC_4701,(0,2):C.GC_4783})

V_613 = Vertex(name = 'V_613',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS4, L.VVVSSS47 ],
               couplings = {(0,1):C.GC_4330,(0,0):C.GC_4261,(0,2):C.GC_4265})

V_614 = Vertex(name = 'V_614',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS12, L.VVVSSS47 ],
               couplings = {(0,0):C.GC_4340,(0,1):C.GC_4326})

V_615 = Vertex(name = 'V_615',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS198, L.VVVVSS199, L.VVVVSS200 ],
               couplings = {(0,0):C.GC_4711,(0,1):C.GC_4800,(0,2):C.GC_4144})

V_616 = Vertex(name = 'V_616',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS198, L.VVVVSS199 ],
               couplings = {(0,0):C.GC_4721,(0,1):C.GC_4819})

V_617 = Vertex(name = 'V_617',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS73, L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,1):C.GC_4226,(0,2):C.GC_4382,(0,0):C.GC_3794})

V_618 = Vertex(name = 'V_618',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS83, L.VVVSSS84 ],
               couplings = {(0,0):C.GC_4238,(0,1):C.GC_4431})

V_619 = Vertex(name = 'V_619',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS78, L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,1):C.GC_4225,(0,2):C.GC_4380,(0,0):C.GC_3792})

V_620 = Vertex(name = 'V_620',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS83, L.VVVSSS87 ],
               couplings = {(0,0):C.GC_4240,(0,1):C.GC_4429})

V_621 = Vertex(name = 'V_621',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS139, L.VVVVSS141, L.VVVVSS160, L.VVVVSS171, L.VVVVSS180, L.VVVVSS198, L.VVVVSS199, L.VVVVSS2, L.VVVVSS200, L.VVVVSS209, L.VVVVSS223, L.VVVVSS288, L.VVVVSS30, L.VVVVSS308, L.VVVVSS335, L.VVVVSS336, L.VVVVSS343, L.VVVVSS93 ],
               couplings = {(0,4):C.GC_387,(0,2):C.GC_1848,(0,3):C.GC_1436,(0,7):C.GC_1424,(0,12):C.GC_1770,(0,11):C.GC_92,(0,10):C.GC_198,(0,14):C.GC_1873,(0,1):C.GC_1178,(0,13):C.GC_1181,(0,16):C.GC_1315,(0,15):C.GC_1800,(0,0):C.GC_1602,(0,5):C.GC_4692,(0,6):C.GC_4744,(0,17):C.GC_360,(0,9):C.GC_88,(0,8):C.GC_4106})

V_622 = Vertex(name = 'V_622',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS139, L.VVVVSS141, L.VVVVSS198, L.VVVVSS199, L.VVVVSS209 ],
               couplings = {(0,1):C.GC_1300,(0,0):C.GC_1822,(0,2):C.GC_4703,(0,3):C.GC_4782,(0,4):C.GC_175})

V_623 = Vertex(name = 'V_623',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS139, L.VVVVSS141, L.VVVVSS160, L.VVVVSS171, L.VVVVSS180, L.VVVVSS198, L.VVVVSS199, L.VVVVSS2, L.VVVVSS200, L.VVVVSS209, L.VVVVSS223, L.VVVVSS288, L.VVVVSS30, L.VVVVSS308, L.VVVVSS335, L.VVVVSS336, L.VVVVSS343, L.VVVVSS93 ],
               couplings = {(0,4):C.GC_389,(0,2):C.GC_1850,(0,3):C.GC_1435,(0,7):C.GC_1423,(0,12):C.GC_1772,(0,11):C.GC_90,(0,10):C.GC_196,(0,14):C.GC_1871,(0,1):C.GC_1179,(0,13):C.GC_1183,(0,16):C.GC_1314,(0,15):C.GC_1801,(0,0):C.GC_1601,(0,5):C.GC_4694,(0,6):C.GC_4742,(0,17):C.GC_361,(0,9):C.GC_87,(0,8):C.GC_4105})

V_624 = Vertex(name = 'V_624',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS139, L.VVVVSS141, L.VVVVSS198, L.VVVVSS199, L.VVVVSS209 ],
               couplings = {(0,1):C.GC_1301,(0,0):C.GC_1821,(0,2):C.GC_4700,(0,3):C.GC_4780,(0,4):C.GC_174})

V_625 = Vertex(name = 'V_625',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS10, L.VVVSSS33 ],
               couplings = {(0,1):C.GC_4579,(0,0):C.GC_4626})

V_626 = Vertex(name = 'V_626',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS33 ],
               couplings = {(0,0):C.GC_4632})

V_627 = Vertex(name = 'V_627',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_2792,(0,0):C.GC_2788})

V_628 = Vertex(name = 'V_628',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_2905,(0,0):C.GC_2914})

V_629 = Vertex(name = 'V_629',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS89, L.VVSSSS93 ],
               couplings = {(0,0):C.GC_2788,(0,1):C.GC_2792})

V_630 = Vertex(name = 'V_630',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS89, L.VVSSSS93 ],
               couplings = {(0,0):C.GC_2914,(0,1):C.GC_2905})

V_631 = Vertex(name = 'V_631',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_2791,(0,2):C.GC_2787,(0,3):C.GC_426,(0,4):C.GC_2908})

V_632 = Vertex(name = 'V_632',
               particles = [ P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61 ],
               couplings = {(0,0):C.GC_455,(0,1):C.GC_2904,(0,2):C.GC_2913})

V_633 = Vertex(name = 'V_633',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS104, L.VVSSSS21 ],
               couplings = {(0,0):C.GC_2790,(0,1):C.GC_2907})

V_634 = Vertex(name = 'V_634',
               particles = [ P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS104 ],
               couplings = {(0,0):C.GC_2912})

V_635 = Vertex(name = 'V_635',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_2789,(0,1):C.GC_2793})

V_636 = Vertex(name = 'V_636',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS47, L.VVSSSS63 ],
               couplings = {(0,0):C.GC_2915,(0,1):C.GC_2906})

V_637 = Vertex(name = 'V_637',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61, L.VVSSSS71, L.VVSSSS85 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_2791,(0,2):C.GC_2787,(0,3):C.GC_425,(0,4):C.GC_2908})

V_638 = Vertex(name = 'V_638',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS11, L.VVSSSS48, L.VVSSSS61 ],
               couplings = {(0,0):C.GC_454,(0,1):C.GC_2904,(0,2):C.GC_2913})

V_639 = Vertex(name = 'V_639',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_2792,(0,0):C.GC_2794})

V_640 = Vertex(name = 'V_640',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS100, L.VVSSSS78 ],
               couplings = {(0,1):C.GC_2905,(0,0):C.GC_2914})

V_641 = Vertex(name = 'V_641',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_3283,(0,3):C.GC_3291,(0,1):C.GC_3639,(0,0):C.GC_3788,(0,6):C.GC_4462,(0,7):C.GC_3866,(0,5):C.GC_3644,(0,2):C.GC_3365})

V_642 = Vertex(name = 'V_642',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS20, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53 ],
               couplings = {(0,2):C.GC_3375,(0,1):C.GC_3355,(0,0):C.GC_3798,(0,4):C.GC_4545,(0,3):C.GC_3779})

V_643 = Vertex(name = 'V_643',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_3285,(0,5):C.GC_3290,(0,1):C.GC_3641,(0,6):C.GC_3646,(0,3):C.GC_3790,(0,7):C.GC_4464,(0,4):C.GC_3868,(0,2):C.GC_3367})

V_644 = Vertex(name = 'V_644',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_3377,(0,2):C.GC_3354,(0,1):C.GC_3800,(0,3):C.GC_3781,(0,4):C.GC_4547})

V_645 = Vertex(name = 'V_645',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS66, L.VVVSSS69, L.VVVSSS70, L.VVVSSS75, L.VVVSSS82, L.VVVSSS98 ],
               couplings = {(0,2):C.GC_3286,(0,3):C.GC_3288,(0,1):C.GC_3638,(0,4):C.GC_4465,(0,5):C.GC_3869,(0,0):C.GC_3647,(0,6):C.GC_3365})

V_646 = Vertex(name = 'V_646',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS66, L.VVVSSS69, L.VVVSSS70, L.VVVSSS75 ],
               couplings = {(0,2):C.GC_3378,(0,3):C.GC_3352,(0,1):C.GC_4422,(0,4):C.GC_4548,(0,0):C.GC_3782})

V_647 = Vertex(name = 'V_647',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_3282,(0,0):C.GC_3287,(0,3):C.GC_3637,(0,5):C.GC_3643,(0,1):C.GC_4460,(0,4):C.GC_4530})

V_648 = Vertex(name = 'V_648',
               particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_3374,(0,0):C.GC_3351,(0,3):C.GC_3797,(0,4):C.GC_3778,(0,1):C.GC_4543})

V_649 = Vertex(name = 'V_649',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS195, L.VVVVSS202, L.VVVVSS65 ],
               couplings = {(0,1):C.GC_4684,(0,2):C.GC_3952,(0,0):C.GC_4695})

V_650 = Vertex(name = 'V_650',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS195, L.VVVVSS202 ],
               couplings = {(0,1):C.GC_4687,(0,0):C.GC_4704})

V_651 = Vertex(name = 'V_651',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS104, L.VVVSSS20, L.VVVSSS22, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53, L.VVVSSS94 ],
               couplings = {(0,4):C.GC_3283,(0,3):C.GC_3291,(0,1):C.GC_3639,(0,0):C.GC_3788,(0,6):C.GC_4462,(0,7):C.GC_3866,(0,5):C.GC_3644,(0,2):C.GC_3365})

V_652 = Vertex(name = 'V_652',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS20, L.VVVSSS35, L.VVVSSS37, L.VVVSSS52, L.VVVSSS53 ],
               couplings = {(0,2):C.GC_3375,(0,1):C.GC_3355,(0,0):C.GC_3798,(0,4):C.GC_4545,(0,3):C.GC_3779})

V_653 = Vertex(name = 'V_653',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS38, L.VVVSSS41, L.VVVSSS46, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_3284,(0,5):C.GC_3289,(0,1):C.GC_3640,(0,6):C.GC_3645,(0,3):C.GC_3789,(0,7):C.GC_4463,(0,4):C.GC_3867,(0,2):C.GC_3366})

V_654 = Vertex(name = 'V_654',
               particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS105, L.VVVSSS32, L.VVVSSS56, L.VVVSSS64, L.VVVSSS79 ],
               couplings = {(0,0):C.GC_3376,(0,2):C.GC_3353,(0,1):C.GC_3799,(0,3):C.GC_3780,(0,4):C.GC_4546})

V_655 = Vertex(name = 'V_655',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS47, L.VVVSSS50, L.VVVSSS51, L.VVVSSS55, L.VVVSSS58, L.VVVSSS59, L.VVVSSS60 ],
               couplings = {(0,5):C.GC_3288,(0,2):C.GC_3642,(0,3):C.GC_3647,(0,6):C.GC_4461,(0,1):C.GC_3866,(0,4):C.GC_3286,(0,0):C.GC_3365})

V_656 = Vertex(name = 'V_656',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS51, L.VVVSSS55, L.VVVSSS58, L.VVVSSS59, L.VVVSSS60 ],
               couplings = {(0,3):C.GC_3352,(0,0):C.GC_4423,(0,1):C.GC_3782,(0,4):C.GC_4544,(0,2):C.GC_3378})

V_657 = Vertex(name = 'V_657',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS88, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_3282,(0,0):C.GC_3287,(0,3):C.GC_3637,(0,5):C.GC_3643,(0,1):C.GC_4460,(0,4):C.GC_4530})

V_658 = Vertex(name = 'V_658',
               particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS103, L.VVVSSS18, L.VVVSSS61, L.VVVSSS80, L.VVVSSS93 ],
               couplings = {(0,2):C.GC_3374,(0,0):C.GC_3351,(0,3):C.GC_3797,(0,4):C.GC_3778,(0,1):C.GC_4543})

V_659 = Vertex(name = 'V_659',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS121, L.VVVVSS157, L.VVVVSS158, L.VVVVSS191, L.VVVVSS192, L.VVVVSS197, L.VVVVSS201, L.VVVVSS205, L.VVVVSS208, L.VVVVSS235, L.VVVVSS240, L.VVVVSS249, L.VVVVSS258, L.VVVVSS285, L.VVVVSS286, L.VVVVSS298, L.VVVVSS318, L.VVVVSS319, L.VVVVSS322, L.VVVVSS355, L.VVVVSS43, L.VVVVSS49, L.VVVVSS66, L.VVVVSS72, L.VVVVSS77, L.VVVVSS88, L.VVVVSS90, L.VVVVSS98 ],
               couplings = {(0,3):C.GC_385,(0,4):C.GC_1439,(0,2):C.GC_1852,(0,1):C.GC_2192,(0,21):C.GC_1776,(0,26):C.GC_357,(0,27):C.GC_1427,(0,20):C.GC_2137,(0,15):C.GC_195,(0,14):C.GC_1317,(0,22):C.GC_2334,(0,13):C.GC_73,(0,18):C.GC_1206,(0,17):C.GC_1807,(0,16):C.GC_1875,(0,10):C.GC_2157,(0,9):C.GC_2206,(0,11):C.GC_62,(0,19):C.GC_1204,(0,12):C.GC_1631,(0,7):C.GC_69,(0,23):C.GC_2078,(0,0):C.GC_247,(0,6):C.GC_4685,(0,5):C.GC_3961,(0,25):C.GC_2402,(0,8):C.GC_2308,(0,24):C.GC_3960})

V_660 = Vertex(name = 'V_660',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS197, L.VVVVSS201, L.VVVVSS205, L.VVVVSS208, L.VVVVSS258, L.VVVVSS355, L.VVVVSS72, L.VVVVSS77 ],
               couplings = {(0,5):C.GC_1302,(0,4):C.GC_1827,(0,2):C.GC_171,(0,6):C.GC_2168,(0,1):C.GC_4688,(0,0):C.GC_3967,(0,3):C.GC_2328,(0,7):C.GC_4705})

V_661 = Vertex(name = 'V_661',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS195, L.VVVVSS202, L.VVVVSS65 ],
               couplings = {(0,1):C.GC_4684,(0,2):C.GC_3952,(0,0):C.GC_4695})

V_662 = Vertex(name = 'V_662',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS195, L.VVVVSS202 ],
               couplings = {(0,1):C.GC_4687,(0,0):C.GC_4704})

V_663 = Vertex(name = 'V_663',
               particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS105, L.VVVVSS108, L.VVVVSS112, L.VVVVSS132, L.VVVVSS135, L.VVVVSS208, L.VVVVSS218, L.VVVVSS242, L.VVVVSS244, L.VVVVSS248, L.VVVVSS263, L.VVVVSS265, L.VVVVSS42, L.VVVVSS65, L.VVVVSS66, L.VVVVSS77, L.VVVVSS88, L.VVVVSS96, L.VVVVSS99 ],
               couplings = {(0,12):C.GC_1859,(0,3):C.GC_2193,(0,4):C.GC_2467,(0,9):C.GC_2854,(0,7):C.GC_3006,(0,14):C.GC_3055,(0,8):C.GC_2208,(0,1):C.GC_366,(0,0):C.GC_2139,(0,11):C.GC_2777,(0,10):C.GC_2086,(0,18):C.GC_1782,(0,17):C.GC_2401,(0,2):C.GC_2452,(0,6):C.GC_2968,(0,13):C.GC_4873,(0,16):C.GC_2486,(0,5):C.GC_3046,(0,15):C.GC_4887})

V_664 = Vertex(name = 'V_664',
               particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208, L.VVVVSS218, L.VVVVSS263, L.VVVVSS265, L.VVVVSS65 ],
               couplings = {(0,3):C.GC_181,(0,2):C.GC_2170,(0,1):C.GC_2997,(0,4):C.GC_4895,(0,0):C.GC_2481})

V_665 = Vertex(name = 'V_665',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11, L.VVVSSS38 ],
               couplings = {(0,0):C.GC_4578,(0,1):C.GC_4625})

V_666 = Vertex(name = 'V_666',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS11 ],
               couplings = {(0,0):C.GC_4631})

V_667 = Vertex(name = 'V_667',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS121, L.VVVVSS153, L.VVVVSS162, L.VVVVSS167, L.VVVVSS168, L.VVVVSS214, L.VVVVSS217, L.VVVVSS228, L.VVVVSS229, L.VVVVSS23, L.VVVVSS237, L.VVVVSS240, L.VVVVSS249, L.VVVVSS250, L.VVVVSS252, L.VVVVSS269, L.VVVVSS270, L.VVVVSS271, L.VVVVSS272, L.VVVVSS279, L.VVVVSS280, L.VVVVSS46, L.VVVVSS48, L.VVVVSS65, L.VVVVSS68, L.VVVVSS77, L.VVVVSS81, L.VVVVSS82 ],
               couplings = {(0,10):C.GC_1395,(0,3):C.GC_2387,(0,5):C.GC_1926,(0,4):C.GC_2241,(0,2):C.GC_319,(0,23):C.GC_236,(0,28):C.GC_1338,(0,27):C.GC_2350,(0,16):C.GC_1410,(0,11):C.GC_2393,(0,19):C.GC_273,(0,21):C.GC_341,(0,8):C.GC_2120,(0,9):C.GC_2146,(0,12):C.GC_2362,(0,18):C.GC_1659,(0,17):C.GC_2074,(0,0):C.GC_1904,(0,15):C.GC_113,(0,13):C.GC_1656,(0,14):C.GC_2064,(0,6):C.GC_1216,(0,20):C.GC_1362,(0,7):C.GC_2311,(0,1):C.GC_1747,(0,22):C.GC_2221,(0,25):C.GC_2070,(0,24):C.GC_4831,(0,26):C.GC_4850})

V_668 = Vertex(name = 'V_668',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS214, L.VVVVSS217, L.VVVVSS249, L.VVVVSS252, L.VVVVSS65, L.VVVVSS68 ],
               couplings = {(0,3):C.GC_297,(0,2):C.GC_1722,(0,0):C.GC_1377,(0,1):C.GC_2370,(0,5):C.GC_2112,(0,4):C.GC_4856})

V_669 = Vertex(name = 'V_669',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS121, L.VVVVSS154, L.VVVVSS159, L.VVVVSS167, L.VVVVSS172, L.VVVVSS214, L.VVVVSS216, L.VVVVSS228, L.VVVVSS229, L.VVVVSS23, L.VVVVSS238, L.VVVVSS240, L.VVVVSS249, L.VVVVSS250, L.VVVVSS253, L.VVVVSS269, L.VVVVSS270, L.VVVVSS279, L.VVVVSS320, L.VVVVSS350, L.VVVVSS351, L.VVVVSS44, L.VVVVSS46, L.VVVVSS65, L.VVVVSS68, L.VVVVSS77, L.VVVVSS78, L.VVVVSS82 ],
               couplings = {(0,10):C.GC_1394,(0,3):C.GC_2388,(0,5):C.GC_1927,(0,4):C.GC_2243,(0,2):C.GC_318,(0,22):C.GC_235,(0,28):C.GC_1337,(0,27):C.GC_2349,(0,16):C.GC_1409,(0,11):C.GC_2394,(0,20):C.GC_271,(0,21):C.GC_343,(0,8):C.GC_2119,(0,9):C.GC_2147,(0,12):C.GC_2361,(0,19):C.GC_1658,(0,17):C.GC_2073,(0,0):C.GC_1905,(0,15):C.GC_114,(0,13):C.GC_1655,(0,14):C.GC_2063,(0,6):C.GC_1217,(0,18):C.GC_1363,(0,7):C.GC_2310,(0,1):C.GC_1748,(0,23):C.GC_2220,(0,25):C.GC_2071,(0,24):C.GC_4830,(0,26):C.GC_4849})

V_670 = Vertex(name = 'V_670',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS214, L.VVVVSS216, L.VVVVSS249, L.VVVVSS253, L.VVVVSS65, L.VVVVSS68 ],
               couplings = {(0,3):C.GC_298,(0,2):C.GC_1721,(0,0):C.GC_1378,(0,1):C.GC_2369,(0,5):C.GC_2113,(0,4):C.GC_4855})

V_671 = Vertex(name = 'V_671',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS121, L.VVVVSS153, L.VVVVSS162, L.VVVVSS167, L.VVVVSS168, L.VVVVSS214, L.VVVVSS217, L.VVVVSS228, L.VVVVSS229, L.VVVVSS23, L.VVVVSS237, L.VVVVSS240, L.VVVVSS249, L.VVVVSS250, L.VVVVSS252, L.VVVVSS269, L.VVVVSS270, L.VVVVSS271, L.VVVVSS272, L.VVVVSS279, L.VVVVSS280, L.VVVVSS46, L.VVVVSS48, L.VVVVSS65, L.VVVVSS68, L.VVVVSS77, L.VVVVSS81, L.VVVVSS82 ],
               couplings = {(0,10):C.GC_1395,(0,3):C.GC_2387,(0,5):C.GC_1926,(0,4):C.GC_2241,(0,2):C.GC_319,(0,23):C.GC_236,(0,28):C.GC_1338,(0,27):C.GC_2350,(0,16):C.GC_1410,(0,11):C.GC_2393,(0,19):C.GC_270,(0,21):C.GC_341,(0,8):C.GC_2120,(0,9):C.GC_2146,(0,12):C.GC_2360,(0,18):C.GC_1659,(0,17):C.GC_2074,(0,0):C.GC_1904,(0,15):C.GC_113,(0,13):C.GC_1656,(0,14):C.GC_2064,(0,6):C.GC_1216,(0,20):C.GC_1364,(0,7):C.GC_2311,(0,1):C.GC_1747,(0,22):C.GC_2221,(0,25):C.GC_2070,(0,24):C.GC_4831,(0,26):C.GC_4850})

V_672 = Vertex(name = 'V_672',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS214, L.VVVVSS217, L.VVVVSS249, L.VVVVSS252, L.VVVVSS65, L.VVVVSS68 ],
               couplings = {(0,3):C.GC_297,(0,2):C.GC_1722,(0,0):C.GC_1377,(0,1):C.GC_2370,(0,5):C.GC_2112,(0,4):C.GC_4856})

V_673 = Vertex(name = 'V_673',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS121, L.VVVVSS154, L.VVVVSS159, L.VVVVSS167, L.VVVVSS172, L.VVVVSS214, L.VVVVSS216, L.VVVVSS228, L.VVVVSS229, L.VVVVSS23, L.VVVVSS238, L.VVVVSS240, L.VVVVSS249, L.VVVVSS250, L.VVVVSS253, L.VVVVSS269, L.VVVVSS270, L.VVVVSS279, L.VVVVSS320, L.VVVVSS350, L.VVVVSS351, L.VVVVSS44, L.VVVVSS46, L.VVVVSS65, L.VVVVSS68, L.VVVVSS77, L.VVVVSS78, L.VVVVSS82 ],
               couplings = {(0,10):C.GC_1396,(0,3):C.GC_2386,(0,5):C.GC_1925,(0,4):C.GC_2240,(0,2):C.GC_321,(0,22):C.GC_238,(0,28):C.GC_1339,(0,27):C.GC_2351,(0,16):C.GC_1411,(0,11):C.GC_2392,(0,20):C.GC_271,(0,21):C.GC_340,(0,8):C.GC_2121,(0,9):C.GC_2145,(0,12):C.GC_2361,(0,19):C.GC_1660,(0,17):C.GC_2076,(0,0):C.GC_1903,(0,15):C.GC_111,(0,13):C.GC_1657,(0,14):C.GC_2065,(0,6):C.GC_1215,(0,18):C.GC_1363,(0,7):C.GC_2312,(0,1):C.GC_1746,(0,23):C.GC_2223,(0,25):C.GC_2069,(0,24):C.GC_4832,(0,26):C.GC_4851})

V_674 = Vertex(name = 'V_674',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS214, L.VVVVSS216, L.VVVVSS249, L.VVVVSS253, L.VVVVSS65, L.VVVVSS68 ],
               couplings = {(0,3):C.GC_295,(0,2):C.GC_1723,(0,0):C.GC_1376,(0,1):C.GC_2371,(0,5):C.GC_2110,(0,4):C.GC_4857})

V_675 = Vertex(name = 'V_675',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS121, L.VVVVSS126, L.VVVVSS127, L.VVVVSS149, L.VVVVSS191, L.VVVVSS193, L.VVVVSS208, L.VVVVSS234, L.VVVVSS239, L.VVVVSS240, L.VVVVSS249, L.VVVVSS256, L.VVVVSS285, L.VVVVSS317, L.VVVVSS321, L.VVVVSS354, L.VVVVSS50, L.VVVVSS51, L.VVVVSS65, L.VVVVSS66, L.VVVVSS71, L.VVVVSS77, L.VVVVSS88, L.VVVVSS91 ],
               couplings = {(0,4):C.GC_384,(0,5):C.GC_1439,(0,2):C.GC_1853,(0,1):C.GC_2192,(0,17):C.GC_1775,(0,19):C.GC_2840,(0,3):C.GC_1317,(0,12):C.GC_74,(0,14):C.GC_1206,(0,8):C.GC_1807,(0,13):C.GC_1876,(0,9):C.GC_2158,(0,7):C.GC_2206,(0,23):C.GC_1426,(0,10):C.GC_62,(0,15):C.GC_1204,(0,11):C.GC_1630,(0,16):C.GC_2138,(0,20):C.GC_2078,(0,0):C.GC_247,(0,18):C.GC_4739,(0,22):C.GC_2892,(0,6):C.GC_2786,(0,21):C.GC_4763})

V_676 = Vertex(name = 'V_676',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208, L.VVVVSS256, L.VVVVSS354, L.VVVVSS65, L.VVVVSS71 ],
               couplings = {(0,2):C.GC_1302,(0,1):C.GC_1826,(0,4):C.GC_2168,(0,3):C.GC_4776,(0,0):C.GC_2833})

V_677 = Vertex(name = 'V_677',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS121, L.VVVVSS125, L.VVVVSS126, L.VVVVSS127, L.VVVVSS128, L.VVVVSS149, L.VVVVSS163, L.VVVVSS164, L.VVVVSS191, L.VVVVSS193, L.VVVVSS208, L.VVVVSS234, L.VVVVSS239, L.VVVVSS240, L.VVVVSS249, L.VVVVSS256, L.VVVVSS285, L.VVVVSS292, L.VVVVSS317, L.VVVVSS321, L.VVVVSS323, L.VVVVSS354, L.VVVVSS39, L.VVVVSS50, L.VVVVSS51, L.VVVVSS65, L.VVVVSS66, L.VVVVSS71, L.VVVVSS77, L.VVVVSS88, L.VVVVSS91 ],
               couplings = {(0,5):C.GC_77,(0,2):C.GC_1207,(0,23):C.GC_2309,(0,9):C.GC_384,(0,10):C.GC_1439,(0,8):C.GC_1634,(0,4):C.GC_1853,(0,7):C.GC_2080,(0,3):C.GC_2192,(0,25):C.GC_1775,(0,27):C.GC_2785,(0,18):C.GC_401,(0,6):C.GC_1203,(0,21):C.GC_1451,(0,17):C.GC_74,(0,20):C.GC_1206,(0,19):C.GC_1635,(0,13):C.GC_1807,(0,12):C.GC_2081,(0,14):C.GC_2158,(0,0):C.GC_214,(0,31):C.GC_1426,(0,15):C.GC_62,(0,22):C.GC_1204,(0,16):C.GC_1630,(0,24):C.GC_2138,(0,28):C.GC_2078,(0,1):C.GC_61,(0,26):C.GC_4740,(0,30):C.GC_2892,(0,11):C.GC_2786,(0,29):C.GC_4741})

V_678 = Vertex(name = 'V_678',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS121, L.VVVVSS125, L.VVVVSS128, L.VVVVSS149, L.VVVVSS163, L.VVVVSS164, L.VVVVSS208, L.VVVVSS234, L.VVVVSS249, L.VVVVSS256, L.VVVVSS317, L.VVVVSS354, L.VVVVSS39, L.VVVVSS65, L.VVVVSS66, L.VVVVSS71, L.VVVVSS77 ],
               couplings = {(0,2):C.GC_408,(0,1):C.GC_1458,(0,12):C.GC_2413,(0,5):C.GC_1942,(0,4):C.GC_2251,(0,14):C.GC_2898,(0,3):C.GC_1317,(0,10):C.GC_1876,(0,7):C.GC_2206,(0,8):C.GC_215,(0,11):C.GC_1302,(0,9):C.GC_1826,(0,15):C.GC_2168,(0,0):C.GC_247,(0,13):C.GC_4779,(0,6):C.GC_2833,(0,16):C.GC_4764})

V_679 = Vertex(name = 'V_679',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS104, L.VVVVSS106, L.VVVVSS114, L.VVVVSS123, L.VVVVSS133, L.VVVVSS136, L.VVVVSS16, L.VVVVSS201, L.VVVVSS211, L.VVVVSS231, L.VVVVSS243, L.VVVVSS245, L.VVVVSS246, L.VVVVSS259, L.VVVVSS260, L.VVVVSS262, L.VVVVSS84, L.VVVVSS87, L.VVVVSS95, L.VVVVSS97 ],
               couplings = {(0,4):C.GC_323,(0,6):C.GC_1397,(0,5):C.GC_2383,(0,3):C.GC_2484,(0,11):C.GC_2881,(0,9):C.GC_3067,(0,12):C.GC_2990,(0,10):C.GC_2617,(0,1):C.GC_240,(0,0):C.GC_1906,(0,19):C.GC_2225,(0,17):C.GC_2347,(0,14):C.GC_2779,(0,15):C.GC_2967,(0,13):C.GC_2524,(0,16):C.GC_1340,(0,18):C.GC_2475,(0,2):C.GC_2482,(0,8):C.GC_3042,(0,7):C.GC_4898})

V_680 = Vertex(name = 'V_680',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS201, L.VVVVSS211, L.VVVVSS259, L.VVVVSS260, L.VVVVSS262 ],
               couplings = {(0,3):C.GC_2868,(0,4):C.GC_1724,(0,2):C.GC_2115,(0,1):C.GC_3062,(0,0):C.GC_4904})

V_681 = Vertex(name = 'V_681',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS102 ],
               couplings = {(0,0):C.GC_4644})

V_682 = Vertex(name = 'V_682',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS102 ],
               couplings = {(0,0):C.GC_4660})

V_683 = Vertex(name = 'V_683',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS30 ],
               couplings = {(0,0):C.GC_4645})

V_684 = Vertex(name = 'V_684',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS30 ],
               couplings = {(0,0):C.GC_4661})

V_685 = Vertex(name = 'V_685',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS90 ],
               couplings = {(0,0):C.GC_4643})

V_686 = Vertex(name = 'V_686',
               particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS90 ],
               couplings = {(0,0):C.GC_4659})

V_687 = Vertex(name = 'V_687',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS40 ],
               couplings = {(0,0):C.GC_4646})

V_688 = Vertex(name = 'V_688',
               particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS40 ],
               couplings = {(0,0):C.GC_4662})

V_689 = Vertex(name = 'V_689',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS114, L.VVVVSS115, L.VVVVSS123, L.VVVVSS143, L.VVVVSS155, L.VVVVSS165, L.VVVVSS173, L.VVVVSS188, L.VVVVSS19, L.VVVVSS201, L.VVVVSS211, L.VVVVSS231, L.VVVVSS232, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS346, L.VVVVSS347, L.VVVVSS348 ],
               couplings = {(0,6):C.GC_1856,(0,3):C.GC_2465,(0,7):C.GC_391,(0,8):C.GC_1441,(0,5):C.GC_2189,(0,2):C.GC_1779,(0,0):C.GC_2133,(0,19):C.GC_1881,(0,12):C.GC_2469,(0,13):C.GC_2856,(0,9):C.GC_363,(0,14):C.GC_2796,(0,15):C.GC_1652,(0,18):C.GC_119,(0,16):C.GC_1219,(0,4):C.GC_2067,(0,17):C.GC_2204,(0,1):C.GC_2450,(0,11):C.GC_2440,(0,10):C.GC_4868})

V_690 = Vertex(name = 'V_690',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS143, L.VVVVSS201, L.VVVVSS211, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS347 ],
               couplings = {(0,3):C.GC_179,(0,4):C.GC_1832,(0,6):C.GC_2154,(0,5):C.GC_1810,(0,0):C.GC_2166,(0,2):C.GC_2457,(0,1):C.GC_4893})

V_691 = Vertex(name = 'V_691',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS114, L.VVVVSS115, L.VVVVSS123, L.VVVVSS143, L.VVVVSS155, L.VVVVSS165, L.VVVVSS173, L.VVVVSS188, L.VVVVSS19, L.VVVVSS201, L.VVVVSS211, L.VVVVSS231, L.VVVVSS232, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS346, L.VVVVSS347, L.VVVVSS348 ],
               couplings = {(0,6):C.GC_1855,(0,3):C.GC_2466,(0,7):C.GC_390,(0,8):C.GC_1440,(0,5):C.GC_2187,(0,2):C.GC_1778,(0,0):C.GC_2132,(0,19):C.GC_1883,(0,12):C.GC_2468,(0,13):C.GC_2855,(0,9):C.GC_362,(0,14):C.GC_2797,(0,15):C.GC_1654,(0,18):C.GC_118,(0,16):C.GC_1218,(0,4):C.GC_2066,(0,17):C.GC_2203,(0,1):C.GC_2451,(0,11):C.GC_2441,(0,10):C.GC_4869})

V_692 = Vertex(name = 'V_692',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS143, L.VVVVSS201, L.VVVVSS211, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS347 ],
               couplings = {(0,3):C.GC_180,(0,4):C.GC_1834,(0,6):C.GC_2155,(0,5):C.GC_1809,(0,0):C.GC_2165,(0,2):C.GC_2458,(0,1):C.GC_4894})

V_693 = Vertex(name = 'V_693',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS114, L.VVVVSS115, L.VVVVSS123, L.VVVVSS143, L.VVVVSS155, L.VVVVSS165, L.VVVVSS173, L.VVVVSS188, L.VVVVSS19, L.VVVVSS201, L.VVVVSS211, L.VVVVSS231, L.VVVVSS232, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS346, L.VVVVSS347, L.VVVVSS348 ],
               couplings = {(0,6):C.GC_1856,(0,3):C.GC_2465,(0,7):C.GC_391,(0,8):C.GC_1441,(0,5):C.GC_2189,(0,2):C.GC_1779,(0,0):C.GC_2133,(0,19):C.GC_1881,(0,12):C.GC_2469,(0,13):C.GC_2856,(0,9):C.GC_363,(0,14):C.GC_2796,(0,15):C.GC_1652,(0,18):C.GC_119,(0,16):C.GC_1219,(0,4):C.GC_2067,(0,17):C.GC_2204,(0,1):C.GC_2450,(0,11):C.GC_2440,(0,10):C.GC_4868})

V_694 = Vertex(name = 'V_694',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS143, L.VVVVSS201, L.VVVVSS211, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS347 ],
               couplings = {(0,3):C.GC_179,(0,4):C.GC_1832,(0,6):C.GC_2156,(0,5):C.GC_1808,(0,0):C.GC_2166,(0,2):C.GC_2457,(0,1):C.GC_4893})

V_695 = Vertex(name = 'V_695',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS114, L.VVVVSS115, L.VVVVSS123, L.VVVVSS143, L.VVVVSS155, L.VVVVSS165, L.VVVVSS173, L.VVVVSS188, L.VVVVSS19, L.VVVVSS201, L.VVVVSS211, L.VVVVSS231, L.VVVVSS232, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS346, L.VVVVSS347, L.VVVVSS348 ],
               couplings = {(0,6):C.GC_1858,(0,3):C.GC_2464,(0,7):C.GC_392,(0,8):C.GC_1442,(0,5):C.GC_2190,(0,2):C.GC_1781,(0,0):C.GC_2135,(0,19):C.GC_1880,(0,12):C.GC_2470,(0,13):C.GC_2857,(0,9):C.GC_365,(0,14):C.GC_2795,(0,15):C.GC_1649,(0,18):C.GC_121,(0,16):C.GC_1220,(0,4):C.GC_2068,(0,17):C.GC_2205,(0,1):C.GC_2449,(0,11):C.GC_2439,(0,10):C.GC_4867})

V_696 = Vertex(name = 'V_696',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS143, L.VVVVSS201, L.VVVVSS211, L.VVVVSS251, L.VVVVSS266, L.VVVVSS333, L.VVVVSS347 ],
               couplings = {(0,3):C.GC_177,(0,4):C.GC_1829,(0,6):C.GC_2155,(0,5):C.GC_1809,(0,0):C.GC_2167,(0,2):C.GC_2456,(0,1):C.GC_4892})

V_697 = Vertex(name = 'V_697',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS131, L.VVVVSS201, L.VVVVSS243, L.VVVVSS259, L.VVVVSS97 ],
               couplings = {(0,0):C.GC_2998,(0,2):C.GC_3059,(0,4):C.GC_2986,(0,3):C.GC_3041,(0,1):C.GC_4912})

V_698 = Vertex(name = 'V_698',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS201, L.VVVVSS259 ],
               couplings = {(0,1):C.GC_2996,(0,0):C.GC_4923})

V_699 = Vertex(name = 'V_699',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS131, L.VVVVSS201, L.VVVVSS243, L.VVVVSS259, L.VVVVSS97 ],
               couplings = {(0,0):C.GC_2999,(0,2):C.GC_3061,(0,4):C.GC_2987,(0,3):C.GC_3040,(0,1):C.GC_4911})

V_700 = Vertex(name = 'V_700',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS201, L.VVVVSS259 ],
               couplings = {(0,1):C.GC_2995,(0,0):C.GC_4922})

V_701 = Vertex(name = 'V_701',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS131, L.VVVVSS201, L.VVVVSS243, L.VVVVSS259, L.VVVVSS97 ],
               couplings = {(0,0):C.GC_2998,(0,2):C.GC_3039,(0,4):C.GC_3057,(0,3):C.GC_3041,(0,1):C.GC_4913})

V_702 = Vertex(name = 'V_702',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS201, L.VVVVSS243, L.VVVVSS259 ],
               couplings = {(0,1):C.GC_3060,(0,2):C.GC_3058,(0,0):C.GC_4924})

V_703 = Vertex(name = 'V_703',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS148, L.VVVVSS190, L.VVVVSS204, L.VVVVSS208, L.VVVVSS283, L.VVVVSS284, L.VVVVSS289, L.VVVVSS353, L.VVVVSS56, L.VVVVSS60, L.VVVVSS62, L.VVVVSS66, L.VVVVSS74, L.VVVVSS88, L.VVVVSS89 ],
               couplings = {(0,9):C.GC_1633,(0,8):C.GC_1852,(0,10):C.GC_76,(0,1):C.GC_384,(0,14):C.GC_1774,(0,0):C.GC_68,(0,5):C.GC_400,(0,11):C.GC_1196,(0,6):C.GC_1636,(0,4):C.GC_74,(0,2):C.GC_1629,(0,12):C.GC_1804,(0,13):C.GC_685,(0,7):C.GC_70,(0,3):C.GC_1197})

V_704 = Vertex(name = 'V_704',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS148, L.VVVVSS204, L.VVVVSS208, L.VVVVSS289, L.VVVVSS353, L.VVVVSS60, L.VVVVSS62, L.VVVVSS66 ],
               couplings = {(0,5):C.GC_1941,(0,6):C.GC_407,(0,0):C.GC_194,(0,7):C.GC_1356,(0,3):C.GC_1877,(0,1):C.GC_1825,(0,4):C.GC_172,(0,2):C.GC_1330})

V_705 = Vertex(name = 'V_705',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS117, L.VVVVSS150, L.VVVVSS151, L.VVVVSS169, L.VVVVSS17, L.VVVVSS180, L.VVVVSS187, L.VVVVSS213, L.VVVVSS222, L.VVVVSS226, L.VVVVSS227, L.VVVVSS230, L.VVVVSS27, L.VVVVSS275, L.VVVVSS288, L.VVVVSS31, L.VVVVSS328, L.VVVVSS329, L.VVVVSS330, L.VVVVSS338, L.VVVVSS357, L.VVVVSS36, L.VVVVSS83, L.VVVVSS85 ],
               couplings = {(0,2):C.GC_66,(0,1):C.GC_316,(0,12):C.GC_1201,(0,4):C.GC_1392,(0,3):C.GC_1641,(0,6):C.GC_1923,(0,0):C.GC_2085,(0,5):C.GC_2246,(0,22):C.GC_1334,(0,23):C.GC_231,(0,19):C.GC_67,(0,16):C.GC_268,(0,13):C.GC_1202,(0,11):C.GC_1361,(0,17):C.GC_1640,(0,18):C.GC_1935,(0,14):C.GC_2083,(0,9):C.GC_1626,(0,10):C.GC_1637,(0,7):C.GC_1198,(0,8):C.GC_64,(0,15):C.GC_874,(0,21):C.GC_1627,(0,20):C.GC_1638})

V_706 = Vertex(name = 'V_706',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS117, L.VVVVSS151, L.VVVVSS169, L.VVVVSS213, L.VVVVSS222, L.VVVVSS226, L.VVVVSS227, L.VVVVSS27, L.VVVVSS275, L.VVVVSS288, L.VVVVSS338, L.VVVVSS357, L.VVVVSS36 ],
               couplings = {(0,1):C.GC_404,(0,7):C.GC_1456,(0,2):C.GC_1944,(0,0):C.GC_2252,(0,10):C.GC_338,(0,8):C.GC_1408,(0,9):C.GC_2249,(0,5):C.GC_1792,(0,6):C.GC_1744,(0,3):C.GC_1374,(0,4):C.GC_293,(0,12):C.GC_1761,(0,11):C.GC_1720})

V_707 = Vertex(name = 'V_707',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208, L.VVVVSS38, L.VVVVSS66, L.VVVVSS88 ],
               couplings = {(0,1):C.GC_3000,(0,2):C.GC_3045,(0,3):C.GC_3069,(0,0):C.GC_3047})

V_708 = Vertex(name = 'V_708',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208, L.VVVVSS66 ],
               couplings = {(0,1):C.GC_3070,(0,0):C.GC_3054})

V_709 = Vertex(name = 'V_709',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS113, L.VVVVSS114, L.VVVVSS116, L.VVVVSS122, L.VVVVSS123, L.VVVVSS124, L.VVVVSS16, L.VVVVSS211, L.VVVVSS231, L.VVVVSS84, L.VVVVSS95 ],
               couplings = {(0,3):C.GC_323,(0,6):C.GC_1398,(0,5):C.GC_2384,(0,4):C.GC_2485,(0,8):C.GC_3044,(0,0):C.GC_240,(0,9):C.GC_1341,(0,10):C.GC_3009,(0,2):C.GC_2346,(0,1):C.GC_2483,(0,7):C.GC_3043})

V_710 = Vertex(name = 'V_710',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS211, L.VVVVSS231 ],
               couplings = {(0,1):C.GC_3066,(0,0):C.GC_3064})

V_711 = Vertex(name = 'V_711',
               particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS131, L.VVVVSS243, L.VVVVSS259, L.VVVVSS97 ],
               couplings = {(0,0):C.GC_2194,(0,1):C.GC_2839,(0,3):C.GC_2891,(0,2):C.GC_2780})

V_712 = Vertex(name = 'V_712',
               particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS259 ],
               couplings = {(0,0):C.GC_2832})

V_713 = Vertex(name = 'V_713',
               particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS102, L.VVVVSS103, L.VVVVSS111, L.VVVVSS118, L.VVVVSS134, L.VVVVSS210, L.VVVVSS225, L.VVVVSS243, L.VVVVSS247, L.VVVVSS259, L.VVVVSS261, L.VVVVSS94 ],
               couplings = {(0,3):C.GC_322,(0,4):C.GC_2385,(0,7):C.GC_2882,(0,6):C.GC_2985,(0,8):C.GC_2616,(0,0):C.GC_241,(0,1):C.GC_2226,(0,2):C.GC_2348,(0,9):C.GC_2778,(0,10):C.GC_2525,(0,11):C.GC_2476,(0,5):C.GC_2969})

V_714 = Vertex(name = 'V_714',
               particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS210, L.VVVVSS259, L.VVVVSS261 ],
               couplings = {(0,1):C.GC_2867,(0,2):C.GC_2116,(0,0):C.GC_2446})

V_715 = Vertex(name = 'V_715',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS100, L.VVVVSS119, L.VVVVSS138, L.VVVVSS210, L.VVVVSS220, L.VVVVSS225, L.VVVVSS267, L.VVVVSS268, L.VVVVSS94 ],
               couplings = {(0,1):C.GC_320,(0,2):C.GC_2242,(0,0):C.GC_237,(0,7):C.GC_342,(0,5):C.GC_2599,(0,4):C.GC_112,(0,6):C.GC_274,(0,8):C.GC_2222,(0,3):C.GC_2514})

V_716 = Vertex(name = 'V_716',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS210, L.VVVVSS220, L.VVVVSS267 ],
               couplings = {(0,1):C.GC_296,(0,2):C.GC_2075,(0,0):C.GC_2111})

V_717 = Vertex(name = 'V_717',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS101, L.VVVVSS120, L.VVVVSS183, L.VVVVSS210, L.VVVVSS221, L.VVVVSS225, L.VVVVSS310, L.VVVVSS311, L.VVVVSS94 ],
               couplings = {(0,1):C.GC_321,(0,2):C.GC_2244,(0,0):C.GC_239,(0,7):C.GC_344,(0,5):C.GC_2598,(0,4):C.GC_111,(0,6):C.GC_272,(0,8):C.GC_2223,(0,3):C.GC_2513})

V_718 = Vertex(name = 'V_718',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS210, L.VVVVSS221, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_295,(0,2):C.GC_2072,(0,0):C.GC_2110})

V_719 = Vertex(name = 'V_719',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS109, L.VVVVSS129, L.VVVVSS137, L.VVVVSS184, L.VVVVSS185, L.VVVVSS206, L.VVVVSS208, L.VVVVSS215, L.VVVVSS233, L.VVVVSS241, L.VVVVSS290, L.VVVVSS293, L.VVVVSS295, L.VVVVSS296, L.VVVVSS297, L.VVVVSS299, L.VVVVSS32, L.VVVVSS41, L.VVVVSS57, L.VVVVSS66, L.VVVVSS69, L.VVVVSS88 ],
               couplings = {(0,18):C.GC_1857,(0,3):C.GC_391,(0,1):C.GC_2188,(0,4):C.GC_2411,(0,0):C.GC_1780,(0,17):C.GC_2134,(0,9):C.GC_249,(0,15):C.GC_1882,(0,19):C.GC_2336,(0,12):C.GC_120,(0,11):C.GC_1808,(0,14):C.GC_2154,(0,13):C.GC_2204,(0,10):C.GC_2317,(0,8):C.GC_200,(0,5):C.GC_1651,(0,2):C.GC_2067,(0,16):C.GC_364,(0,7):C.GC_109,(0,20):C.GC_116,(0,21):C.GC_2404,(0,6):C.GC_2314})

V_720 = Vertex(name = 'V_720',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS137, L.VVVVSS206, L.VVVVSS208, L.VVVVSS69 ],
               couplings = {(0,1):C.GC_1831,(0,0):C.GC_2166,(0,3):C.GC_178,(0,2):C.GC_2330})

V_721 = Vertex(name = 'V_721',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS130, L.VVVVSS146, L.VVVVSS179, L.VVVVSS185, L.VVVVSS207, L.VVVVSS208, L.VVVVSS215, L.VVVVSS233, L.VVVVSS241, L.VVVVSS290, L.VVVVSS300, L.VVVVSS303, L.VVVVSS312, L.VVVVSS313, L.VVVVSS32, L.VVVVSS352, L.VVVVSS40, L.VVVVSS58, L.VVVVSS66, L.VVVVSS69, L.VVVVSS88, L.VVVVSS92 ],
               couplings = {(0,17):C.GC_1858,(0,2):C.GC_390,(0,0):C.GC_2187,(0,3):C.GC_2410,(0,21):C.GC_1781,(0,16):C.GC_2135,(0,8):C.GC_250,(0,10):C.GC_1884,(0,18):C.GC_2337,(0,12):C.GC_121,(0,11):C.GC_1809,(0,15):C.GC_2155,(0,13):C.GC_2205,(0,9):C.GC_2318,(0,7):C.GC_201,(0,4):C.GC_1650,(0,1):C.GC_2066,(0,14):C.GC_365,(0,6):C.GC_110,(0,19):C.GC_115,(0,20):C.GC_2403,(0,5):C.GC_2315})

V_722 = Vertex(name = 'V_722',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS146, L.VVVVSS207, L.VVVVSS208, L.VVVVSS69 ],
               couplings = {(0,1):C.GC_1830,(0,0):C.GC_2165,(0,3):C.GC_177,(0,2):C.GC_2331})

V_723 = Vertex(name = 'V_723',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS100, L.VVVVSS119, L.VVVVSS138, L.VVVVSS210, L.VVVVSS220, L.VVVVSS225, L.VVVVSS267, L.VVVVSS268, L.VVVVSS94 ],
               couplings = {(0,1):C.GC_320,(0,2):C.GC_2242,(0,0):C.GC_237,(0,7):C.GC_342,(0,5):C.GC_2599,(0,4):C.GC_112,(0,6):C.GC_269,(0,8):C.GC_2222,(0,3):C.GC_2514})

V_724 = Vertex(name = 'V_724',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS210, L.VVVVSS220, L.VVVVSS267 ],
               couplings = {(0,1):C.GC_296,(0,2):C.GC_2075,(0,0):C.GC_2111})

V_725 = Vertex(name = 'V_725',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS101, L.VVVVSS120, L.VVVVSS183, L.VVVVSS210, L.VVVVSS221, L.VVVVSS225, L.VVVVSS310, L.VVVVSS311, L.VVVVSS94 ],
               couplings = {(0,1):C.GC_318,(0,2):C.GC_2239,(0,0):C.GC_234,(0,7):C.GC_339,(0,5):C.GC_2600,(0,4):C.GC_114,(0,6):C.GC_272,(0,8):C.GC_2220,(0,3):C.GC_2515})

V_726 = Vertex(name = 'V_726',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS210, L.VVVVSS221, L.VVVVSS310 ],
               couplings = {(0,1):C.GC_298,(0,2):C.GC_2077,(0,0):C.GC_2113})

V_727 = Vertex(name = 'V_727',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS109, L.VVVVSS129, L.VVVVSS137, L.VVVVSS184, L.VVVVSS185, L.VVVVSS206, L.VVVVSS208, L.VVVVSS215, L.VVVVSS233, L.VVVVSS241, L.VVVVSS290, L.VVVVSS293, L.VVVVSS295, L.VVVVSS296, L.VVVVSS297, L.VVVVSS299, L.VVVVSS32, L.VVVVSS41, L.VVVVSS57, L.VVVVSS66, L.VVVVSS69, L.VVVVSS88 ],
               couplings = {(0,18):C.GC_1857,(0,3):C.GC_391,(0,1):C.GC_2188,(0,4):C.GC_2411,(0,0):C.GC_1780,(0,17):C.GC_2134,(0,9):C.GC_249,(0,15):C.GC_1882,(0,19):C.GC_2336,(0,12):C.GC_120,(0,11):C.GC_1810,(0,14):C.GC_2156,(0,13):C.GC_2204,(0,10):C.GC_2317,(0,8):C.GC_200,(0,5):C.GC_1651,(0,2):C.GC_2067,(0,16):C.GC_364,(0,7):C.GC_109,(0,20):C.GC_116,(0,21):C.GC_2404,(0,6):C.GC_2314})

V_728 = Vertex(name = 'V_728',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS137, L.VVVVSS206, L.VVVVSS208, L.VVVVSS69 ],
               couplings = {(0,1):C.GC_1831,(0,0):C.GC_2166,(0,3):C.GC_178,(0,2):C.GC_2330})

V_729 = Vertex(name = 'V_729',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS130, L.VVVVSS146, L.VVVVSS179, L.VVVVSS185, L.VVVVSS207, L.VVVVSS208, L.VVVVSS215, L.VVVVSS233, L.VVVVSS241, L.VVVVSS290, L.VVVVSS300, L.VVVVSS303, L.VVVVSS312, L.VVVVSS313, L.VVVVSS32, L.VVVVSS352, L.VVVVSS40, L.VVVVSS58, L.VVVVSS66, L.VVVVSS69, L.VVVVSS88, L.VVVVSS92 ],
               couplings = {(0,17):C.GC_1855,(0,2):C.GC_392,(0,0):C.GC_2190,(0,3):C.GC_2412,(0,21):C.GC_1778,(0,16):C.GC_2132,(0,8):C.GC_248,(0,10):C.GC_1879,(0,18):C.GC_2335,(0,12):C.GC_118,(0,11):C.GC_1809,(0,15):C.GC_2155,(0,13):C.GC_2203,(0,9):C.GC_2316,(0,7):C.GC_199,(0,4):C.GC_1653,(0,1):C.GC_2068,(0,14):C.GC_362,(0,6):C.GC_108,(0,19):C.GC_117,(0,20):C.GC_2405,(0,5):C.GC_2313})

V_730 = Vertex(name = 'V_730',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS146, L.VVVVSS207, L.VVVVSS208, L.VVVVSS69 ],
               couplings = {(0,1):C.GC_1833,(0,0):C.GC_2167,(0,3):C.GC_180,(0,2):C.GC_2329})

V_731 = Vertex(name = 'V_731',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS148, L.VVVVSS190, L.VVVVSS204, L.VVVVSS208, L.VVVVSS283, L.VVVVSS289, L.VVVVSS353, L.VVVVSS56, L.VVVVSS66, L.VVVVSS74, L.VVVVSS88, L.VVVVSS89 ],
               couplings = {(0,7):C.GC_1852,(0,1):C.GC_384,(0,11):C.GC_1774,(0,0):C.GC_194,(0,8):C.GC_1356,(0,5):C.GC_1877,(0,4):C.GC_74,(0,2):C.GC_1629,(0,9):C.GC_1804,(0,10):C.GC_356,(0,6):C.GC_70,(0,3):C.GC_1197})

V_732 = Vertex(name = 'V_732',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS204, L.VVVVSS353 ],
               couplings = {(0,0):C.GC_1825,(0,1):C.GC_172})

V_733 = Vertex(name = 'V_733',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS150, L.VVVVSS17, L.VVVVSS180, L.VVVVSS187, L.VVVVSS213, L.VVVVSS222, L.VVVVSS226, L.VVVVSS227, L.VVVVSS230, L.VVVVSS275, L.VVVVSS288, L.VVVVSS31, L.VVVVSS328, L.VVVVSS329, L.VVVVSS338, L.VVVVSS357, L.VVVVSS36, L.VVVVSS83, L.VVVVSS85 ],
               couplings = {(0,0):C.GC_316,(0,1):C.GC_1392,(0,3):C.GC_1923,(0,2):C.GC_2246,(0,17):C.GC_1334,(0,18):C.GC_231,(0,12):C.GC_268,(0,14):C.GC_338,(0,8):C.GC_1361,(0,9):C.GC_1408,(0,13):C.GC_1640,(0,10):C.GC_2083,(0,7):C.GC_1744,(0,6):C.GC_1792,(0,4):C.GC_1198,(0,5):C.GC_64,(0,11):C.GC_1901,(0,16):C.GC_1627,(0,15):C.GC_1638})

V_734 = Vertex(name = 'V_734',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS213, L.VVVVSS222, L.VVVVSS357 ],
               couplings = {(0,0):C.GC_1374,(0,1):C.GC_293,(0,2):C.GC_1720})

V_735 = Vertex(name = 'V_735',
               particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208, L.VVVVSS38, L.VVVVSS66, L.VVVVSS88 ],
               couplings = {(0,1):C.GC_3000,(0,2):C.GC_3056,(0,3):C.GC_3068,(0,0):C.GC_3047})

V_736 = Vertex(name = 'V_736',
               particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS208 ],
               couplings = {(0,0):C.GC_3053})

V_737 = Vertex(name = 'V_737',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS113, L.VVVVSS114, L.VVVVSS116, L.VVVVSS122, L.VVVVSS123, L.VVVVSS124, L.VVVVSS16, L.VVVVSS211, L.VVVVSS231, L.VVVVSS84, L.VVVVSS95 ],
               couplings = {(0,3):C.GC_323,(0,6):C.GC_1398,(0,5):C.GC_2384,(0,4):C.GC_2485,(0,8):C.GC_3065,(0,0):C.GC_240,(0,9):C.GC_1341,(0,10):C.GC_3008,(0,2):C.GC_2346,(0,1):C.GC_2483,(0,7):C.GC_3043})

V_738 = Vertex(name = 'V_738',
               particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS211 ],
               couplings = {(0,0):C.GC_3063})

V_739 = Vertex(name = 'V_739',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS306, L.VVVVSS5, L.VVVVSS52, L.VVVVSS59, L.VVVVSS63, L.VVVVSS75, L.VVVVSS76 ],
               couplings = {(0,4):C.GC_383,(0,3):C.GC_1851,(0,1):C.GC_1773,(0,6):C.GC_72,(0,2):C.GC_1632,(0,0):C.GC_1805,(0,5):C.GC_1874})

V_740 = Vertex(name = 'V_740',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS52 ],
               couplings = {(0,0):C.GC_1828})

V_741 = Vertex(name = 'V_741',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS140, L.VVVVSS152, L.VVVVSS170, L.VVVVSS22, L.VVVVSS25, L.VVVVSS278, L.VVVVSS3, L.VVVVSS302, L.VVVVSS336, L.VVVVSS339, L.VVVVSS34, L.VVVVSS340, L.VVVVSS4, L.VVVVSS7 ],
               couplings = {(0,4):C.GC_1393,(0,2):C.GC_1924,(0,1):C.GC_317,(0,6):C.GC_1336,(0,12):C.GC_233,(0,13):C.GC_2640,(0,9):C.GC_337,(0,3):C.GC_1200,(0,5):C.GC_1360,(0,11):C.GC_1639,(0,7):C.GC_2601,(0,0):C.GC_63,(0,10):C.GC_2516,(0,8):C.GC_267})

V_742 = Vertex(name = 'V_742',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS140, L.VVVVSS22, L.VVVVSS34 ],
               couplings = {(0,1):C.GC_691,(0,0):C.GC_292,(0,2):C.GC_2591})

V_743 = Vertex(name = 'V_743',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS11, L.VVVVVS112, L.VVVVVS113, L.VVVVVS114, L.VVVVVS16, L.VVVVVS166, L.VVVVVS167, L.VVVVVS19, L.VVVVVS48, L.VVVVVS56 ],
               couplings = {(0,0):C.GC_3514,(0,7):C.GC_3760,(0,9):C.GC_3489,(0,4):C.GC_3751,(0,1):C.GC_3435,(0,2):C.GC_3497,(0,3):C.GC_3522,(0,8):C.GC_3632,(0,6):C.GC_3674,(0,5):C.GC_3635})

V_744 = Vertex(name = 'V_744',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS112, L.VVVVVS48 ],
               couplings = {(0,0):C.GC_3505,(0,1):C.GC_3664})

V_745 = Vertex(name = 'V_745',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS100, L.VVVVVS101, L.VVVVVS103, L.VVVVVS122, L.VVVVVS125, L.VVVVVS130, L.VVVVVS145, L.VVVVVS165, L.VVVVVS169, L.VVVVVS174, L.VVVVVS22, L.VVVVVS3, L.VVVVVS4, L.VVVVVS51, L.VVVVVS77, L.VVVVVS83, L.VVVVVS87, L.VVVVVS89, L.VVVVVS99 ],
               couplings = {(0,11):C.GC_3331,(0,17):C.GC_3211,(0,15):C.GC_3538,(0,16):C.GC_3728,(0,12):C.GC_3530,(0,10):C.GC_3688,(0,4):C.GC_3147,(0,18):C.GC_3335,(0,6):C.GC_3700,(0,8):C.GC_3126,(0,2):C.GC_3437,(0,7):C.GC_3440,(0,9):C.GC_3476,(0,5):C.GC_3743,(0,1):C.GC_3630,(0,13):C.GC_3326,(0,0):C.GC_3278,(0,14):C.GC_3204,(0,3):C.GC_3125})

V_746 = Vertex(name = 'V_746',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS100, L.VVVVVS101, L.VVVVVS103, L.VVVVVS122 ],
               couplings = {(0,2):C.GC_3466,(0,1):C.GC_3714,(0,0):C.GC_3329,(0,3):C.GC_3140})

V_747 = Vertex(name = 'V_747',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS10, L.VVVVVS111, L.VVVVVS115, L.VVVVVS144, L.VVVVVS15, L.VVVVVS168, L.VVVVVS170, L.VVVVVS21, L.VVVVVS24, L.VVVVVS8 ],
               couplings = {(0,9):C.GC_3515,(0,4):C.GC_3760,(0,7):C.GC_3488,(0,0):C.GC_3750,(0,8):C.GC_3436,(0,2):C.GC_3497,(0,1):C.GC_3521,(0,3):C.GC_3633,(0,6):C.GC_3673,(0,5):C.GC_3634})

V_748 = Vertex(name = 'V_748',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS144, L.VVVVVS24 ],
               couplings = {(0,1):C.GC_3506,(0,0):C.GC_3665})

V_749 = Vertex(name = 'V_749',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1, L.VVVVVS109, L.VVVVVS127, L.VVVVVS131, L.VVVVVS132, L.VVVVVS146, L.VVVVVS178, L.VVVVVS179, L.VVVVVS180, L.VVVVVS2, L.VVVVVS25, L.VVVVVS31, L.VVVVVS36, L.VVVVVS39, L.VVVVVS40, L.VVVVVS45, L.VVVVVS7, L.VVVVVS73, L.VVVVVS81 ],
               couplings = {(0,0):C.GC_3332,(0,18):C.GC_3211,(0,17):C.GC_3539,(0,12):C.GC_3729,(0,9):C.GC_3529,(0,16):C.GC_3689,(0,10):C.GC_3326,(0,2):C.GC_3146,(0,13):C.GC_3278,(0,14):C.GC_3334,(0,5):C.GC_3701,(0,7):C.GC_3126,(0,6):C.GC_3439,(0,8):C.GC_3475,(0,3):C.GC_3631,(0,4):C.GC_3742,(0,1):C.GC_3438,(0,11):C.GC_3205,(0,15):C.GC_3124})

V_750 = Vertex(name = 'V_750',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS109, L.VVVVVS131, L.VVVVVS39, L.VVVVVS45 ],
               couplings = {(0,2):C.GC_3329,(0,1):C.GC_3715,(0,0):C.GC_3467,(0,3):C.GC_3139})

V_751 = Vertex(name = 'V_751',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS157, L.VVVVVS158, L.VVVVVS159, L.VVVVVS26, L.VVVVVS32, L.VVVVVS38, L.VVVVVS49, L.VVVVVS79, L.VVVVVS82 ],
               couplings = {(0,7):C.GC_3424,(0,8):C.GC_3537,(0,2):C.GC_3420,(0,1):C.GC_3423,(0,0):C.GC_3542,(0,3):C.GC_3325,(0,4):C.GC_3528,(0,5):C.GC_4223,(0,6):C.GC_3421})

V_752 = Vertex(name = 'V_752',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS159, L.VVVVVS38, L.VVVVVS49, L.VVVVVS79 ],
               couplings = {(0,3):C.GC_3549,(0,0):C.GC_3474,(0,1):C.GC_4232,(0,2):C.GC_3465})

V_753 = Vertex(name = 'V_753',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS10, L.VVVVVS126, L.VVVVVS128, L.VVVVVS129, L.VVVVVS143, L.VVVVVS156, L.VVVVVS20, L.VVVVVS60, L.VVVVVS66, L.VVVVVS67, L.VVVVVS9 ],
               couplings = {(0,6):C.GC_3273,(0,9):C.GC_3338,(0,7):C.GC_3649,(0,8):C.GC_3761,(0,0):C.GC_3337,(0,10):C.GC_3486,(0,2):C.GC_3270,(0,4):C.GC_3271,(0,1):C.GC_4374,(0,5):C.GC_3339,(0,3):C.GC_4258})

V_754 = Vertex(name = 'V_754',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS126, L.VVVVVS128, L.VVVVVS129, L.VVVVVS143, L.VVVVVS20, L.VVVVVS60 ],
               couplings = {(0,4):C.GC_3342,(0,5):C.GC_3773,(0,1):C.GC_3319,(0,3):C.GC_3314,(0,0):C.GC_3764,(0,2):C.GC_4314})

V_755 = Vertex(name = 'V_755',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS27, L.VVVVVS28, L.VVVVVS41, L.VVVVVS43, L.VVVVVS44, L.VVVVVS6 ],
               couplings = {(0,1):C.GC_4614,(0,5):C.GC_4508,(0,0):C.GC_4497,(0,3):C.GC_4581,(0,4):C.GC_4509,(0,2):C.GC_4458})

V_756 = Vertex(name = 'V_756',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS41, L.VVVVVS43 ],
               couplings = {(0,1):C.GC_4504,(0,0):C.GC_4507})

V_757 = Vertex(name = 'V_757',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS113, L.VVVVVS116, L.VVVVVS117, L.VVVVVS135, L.VVVVVS138, L.VVVVVS139, L.VVVVVS14, L.VVVVVS148, L.VVVVVS150, L.VVVVVS18, L.VVVVVS46, L.VVVVVS58, L.VVVVVS63, L.VVVVVS68 ],
               couplings = {(0,9):C.GC_4606,(0,13):C.GC_4519,(0,6):C.GC_3161,(0,12):C.GC_3491,(0,11):C.GC_3888,(0,10):C.GC_3131,(0,4):C.GC_3172,(0,5):C.GC_3198,(0,2):C.GC_3446,(0,0):C.GC_3498,(0,8):C.GC_4459,(0,7):C.GC_3905,(0,3):C.GC_3890,(0,1):C.GC_3878})

V_758 = Vertex(name = 'V_758',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS116, L.VVVVVS117, L.VVVVVS46 ],
               couplings = {(0,2):C.GC_3181,(0,1):C.GC_4316,(0,0):C.GC_3896})

V_759 = Vertex(name = 'V_759',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS115, L.VVVVVS118, L.VVVVVS119, L.VVVVVS12, L.VVVVVS173, L.VVVVVS59, L.VVVVVS64, L.VVVVVS65, L.VVVVVS8 ],
               couplings = {(0,8):C.GC_4267,(0,3):C.GC_4312,(0,5):C.GC_4471,(0,7):C.GC_4520,(0,2):C.GC_4268,(0,0):C.GC_4310,(0,4):C.GC_4470,(0,6):C.GC_4308,(0,1):C.GC_4266})

V_760 = Vertex(name = 'V_760',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS118, L.VVVVVS119, L.VVVVVS173, L.VVVVVS59, L.VVVVVS8 ],
               couplings = {(0,4):C.GC_4323,(0,3):C.GC_4525,(0,1):C.GC_4315,(0,2):C.GC_4521,(0,0):C.GC_4311})

V_761 = Vertex(name = 'V_761',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS104, L.VVVVVS105, L.VVVVVS107, L.VVVVVS108, L.VVVVVS110, L.VVVVVS121, L.VVVVVS136, L.VVVVVS29, L.VVVVVS33, L.VVVVVS34, L.VVVVVS35, L.VVVVVS42, L.VVVVVS5, L.VVVVVS52, L.VVVVVS54, L.VVVVVS55, L.VVVVVS76, L.VVVVVS86, L.VVVVVS88, L.VVVVVS90, L.VVVVVS94, L.VVVVVS95, L.VVVVVS97, L.VVVVVS98 ],
               couplings = {(0,19):C.GC_4320,(0,12):C.GC_3333,(0,17):C.GC_3730,(0,18):C.GC_3848,(0,10):C.GC_3123,(0,9):C.GC_3445,(0,7):C.GC_3877,(0,8):C.GC_4466,(0,11):C.GC_4576,(0,3):C.GC_3215,(0,2):C.GC_3543,(0,6):C.GC_4506,(0,13):C.GC_3327,(0,15):C.GC_3690,(0,14):C.GC_3831,(0,4):C.GC_4270,(0,22):C.GC_3292,(0,20):C.GC_3293,(0,21):C.GC_3652,(0,0):C.GC_3653,(0,1):C.GC_3818,(0,23):C.GC_3817,(0,16):C.GC_4610,(0,5):C.GC_4577})

V_762 = Vertex(name = 'V_762',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS104, L.VVVVVS105, L.VVVVVS121, L.VVVVVS29, L.VVVVVS33, L.VVVVVS34, L.VVVVVS35, L.VVVVVS42, L.VVVVVS94, L.VVVVVS95, L.VVVVVS97, L.VVVVVS98 ],
               couplings = {(0,6):C.GC_3221,(0,5):C.GC_3550,(0,3):C.GC_3909,(0,4):C.GC_4524,(0,7):C.GC_4616,(0,10):C.GC_3330,(0,8):C.GC_3336,(0,9):C.GC_3716,(0,0):C.GC_3744,(0,1):C.GC_3855,(0,11):C.GC_3841,(0,2):C.GC_4594})

V_763 = Vertex(name = 'V_763',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS27, L.VVVVVS28, L.VVVVVS41, L.VVVVVS43, L.VVVVVS44, L.VVVVVS6 ],
               couplings = {(0,1):C.GC_4614,(0,5):C.GC_4508,(0,0):C.GC_4497,(0,3):C.GC_4581,(0,4):C.GC_4509,(0,2):C.GC_4458})

V_764 = Vertex(name = 'V_764',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS41, L.VVVVVS43 ],
               couplings = {(0,1):C.GC_4505,(0,0):C.GC_4507})

V_765 = Vertex(name = 'V_765',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS113, L.VVVVVS116, L.VVVVVS117, L.VVVVVS135, L.VVVVVS138, L.VVVVVS139, L.VVVVVS14, L.VVVVVS148, L.VVVVVS150, L.VVVVVS18, L.VVVVVS46, L.VVVVVS58, L.VVVVVS63, L.VVVVVS68 ],
               couplings = {(0,9):C.GC_4606,(0,13):C.GC_4519,(0,6):C.GC_3161,(0,12):C.GC_3491,(0,11):C.GC_3888,(0,10):C.GC_3131,(0,4):C.GC_3173,(0,5):C.GC_3198,(0,2):C.GC_3446,(0,0):C.GC_3499,(0,8):C.GC_4459,(0,7):C.GC_3905,(0,3):C.GC_3891,(0,1):C.GC_3878})

V_766 = Vertex(name = 'V_766',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS116, L.VVVVVS117, L.VVVVVS46 ],
               couplings = {(0,2):C.GC_3181,(0,1):C.GC_4316,(0,0):C.GC_3896})

V_767 = Vertex(name = 'V_767',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS144, L.VVVVSS145, L.VVVVSS147, L.VVVVSS156, L.VVVVSS161, L.VVVVSS304, L.VVVVSS345, L.VVVVSS53, L.VVVVSS54, L.VVVVSS6, L.VVVVSS64, L.VVVVSS8, L.VVVVSS9 ],
               couplings = {(0,10):C.GC_1438,(0,3):C.GC_1854,(0,4):C.GC_2191,(0,12):C.GC_1777,(0,11):C.GC_698,(0,9):C.GC_2136,(0,8):C.GC_591,(0,5):C.GC_672,(0,6):C.GC_1806,(0,2):C.GC_1205,(0,0):C.GC_1628,(0,1):C.GC_2207,(0,7):C.GC_2079})

V_768 = Vertex(name = 'V_768',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS144, L.VVVVSS53, L.VVVVSS54 ],
               couplings = {(0,2):C.GC_668,(0,0):C.GC_869,(0,1):C.GC_2169})

V_769 = Vertex(name = 'V_769',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS13, L.VVVVVS134, L.VVVVVS135, L.VVVVVS140, L.VVVVVS16, L.VVVVVS160, L.VVVVVS162, L.VVVVVS17, L.VVVVVS176, L.VVVVVS177, L.VVVVVS47, L.VVVVVS69, L.VVVVVS92 ],
               couplings = {(0,11):C.GC_3760,(0,7):C.GC_3514,(0,0):C.GC_3487,(0,4):C.GC_3751,(0,10):C.GC_3632,(0,9):C.GC_3634,(0,3):C.GC_3674,(0,2):C.GC_3170,(0,1):C.GC_3520,(0,6):C.GC_3281,(0,8):C.GC_3321,(0,12):C.GC_3435,(0,5):C.GC_3279})

V_770 = Vertex(name = 'V_770',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS160, L.VVVVVS47, L.VVVVVS92 ],
               couplings = {(0,1):C.GC_3664,(0,2):C.GC_3505,(0,0):C.GC_3315})

V_771 = Vertex(name = 'V_771',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS106, L.VVVVVS133, L.VVVVVS136, L.VVVVVS137, L.VVVVVS159, L.VVVVVS163, L.VVVVVS164, L.VVVVVS181, L.VVVVVS30, L.VVVVVS32, L.VVVVVS33, L.VVVVVS49, L.VVVVVS80 ],
               couplings = {(0,12):C.GC_3760,(0,10):C.GC_3515,(0,8):C.GC_3487,(0,7):C.GC_3635,(0,4):C.GC_3674,(0,2):C.GC_3171,(0,1):C.GC_3434,(0,3):C.GC_3523,(0,6):C.GC_3280,(0,5):C.GC_3320,(0,9):C.GC_3750,(0,11):C.GC_3633,(0,0):C.GC_3279})

V_772 = Vertex(name = 'V_772',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS106, L.VVVVVS133, L.VVVVVS49 ],
               couplings = {(0,1):C.GC_3504,(0,2):C.GC_3665,(0,0):C.GC_3315})

V_773 = Vertex(name = 'V_773',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS102, L.VVVVVS120, L.VVVVVS124, L.VVVVVS142, L.VVVVVS147, L.VVVVVS152, L.VVVVVS50, L.VVVVVS53, L.VVVVVS74, L.VVVVVS75, L.VVVVVS84, L.VVVVVS85, L.VVVVVS96 ],
               couplings = {(0,11):C.GC_4321,(0,10):C.GC_4655,(0,9):C.GC_3691,(0,6):C.GC_3830,(0,5):C.GC_4271,(0,2):C.GC_3655,(0,0):C.GC_3816,(0,3):C.GC_3854,(0,4):C.GC_3926,(0,7):C.GC_3328,(0,8):C.GC_3917,(0,12):C.GC_3295,(0,1):C.GC_3913})

V_774 = Vertex(name = 'V_774',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS102, L.VVVVVS120, L.VVVVVS124, L.VVVVVS152, L.VVVVVS96 ],
               couplings = {(0,3):C.GC_4503,(0,2):C.GC_4407,(0,0):C.GC_3840,(0,4):C.GC_4233,(0,1):C.GC_3920})

V_775 = Vertex(name = 'V_775',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS102, L.VVVVVS120, L.VVVVVS124, L.VVVVVS142, L.VVVVVS147, L.VVVVVS152, L.VVVVVS50, L.VVVVVS53, L.VVVVVS74, L.VVVVVS75, L.VVVVVS84, L.VVVVVS85, L.VVVVVS96 ],
               couplings = {(0,11):C.GC_4321,(0,10):C.GC_4655,(0,9):C.GC_3691,(0,6):C.GC_3830,(0,5):C.GC_4271,(0,2):C.GC_3655,(0,0):C.GC_3816,(0,3):C.GC_3854,(0,4):C.GC_3926,(0,7):C.GC_3328,(0,8):C.GC_3917,(0,12):C.GC_3295,(0,1):C.GC_3913})

V_776 = Vertex(name = 'V_776',
               particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS102, L.VVVVVS120, L.VVVVVS124, L.VVVVVS152, L.VVVVVS96 ],
               couplings = {(0,3):C.GC_4502,(0,2):C.GC_4407,(0,0):C.GC_3840,(0,4):C.GC_4233,(0,1):C.GC_3920})

V_777 = Vertex(name = 'V_777',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS120, L.VVVVVS123, L.VVVVVS147, L.VVVVVS149, L.VVVVVS151, L.VVVVVS152, L.VVVVVS153, L.VVVVVS154, L.VVVVVS155, L.VVVVVS57, L.VVVVVS61, L.VVVVVS62, L.VVVVVS70, L.VVVVVS71, L.VVVVVS74, L.VVVVVS78, L.VVVVVS84, L.VVVVVS91 ],
               couplings = {(0,16):C.GC_4605,(0,17):C.GC_4409,(0,12):C.GC_3160,(0,11):C.GC_3294,(0,13):C.GC_3490,(0,9):C.GC_3654,(0,5):C.GC_4384,(0,3):C.GC_4467,(0,6):C.GC_3340,(0,7):C.GC_3443,(0,4):C.GC_3444,(0,8):C.GC_3765,(0,2):C.GC_3876,(0,15):C.GC_4515,(0,10):C.GC_3819,(0,14):C.GC_3887,(0,1):C.GC_4468,(0,0):C.GC_3875})

V_778 = Vertex(name = 'V_778',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS120, L.VVVVVS123, L.VVVVVS147, L.VVVVVS149, L.VVVVVS151, L.VVVVVS152, L.VVVVVS154, L.VVVVVS57, L.VVVVVS61, L.VVVVVS62 ],
               couplings = {(0,9):C.GC_3343,(0,7):C.GC_3774,(0,5):C.GC_4198,(0,3):C.GC_4522,(0,6):C.GC_3507,(0,4):C.GC_3524,(0,2):C.GC_3904,(0,8):C.GC_3865,(0,1):C.GC_4489,(0,0):C.GC_3895})

V_779 = Vertex(name = 'V_779',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141, L.VVVVVS72 ],
               couplings = {(0,1):C.GC_4597,(0,0):C.GC_4580})

V_780 = Vertex(name = 'V_780',
               particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141 ],
               couplings = {(0,0):C.GC_4607})

V_781 = Vertex(name = 'V_781',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141, L.VVVVVS72 ],
               couplings = {(0,1):C.GC_4597,(0,0):C.GC_4580})

V_782 = Vertex(name = 'V_782',
               particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS141 ],
               couplings = {(0,0):C.GC_4607})

V_783 = Vertex(name = 'V_783',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV11, L.VVVVVV114, L.VVVVVV115, L.VVVVVV128, L.VVVVVV15, L.VVVVVV23, L.VVVVVV24, L.VVVVVV40, L.VVVVVV65, L.VVVVVV66, L.VVVVVV71, L.VVVVVV72, L.VVVVVV84, L.VVVVVV85, L.VVVVVV86, L.VVVVVV98, L.VVVVVV99 ],
               couplings = {(0,1):C.GC_80,(0,5):C.GC_85,(0,0):C.GC_1211,(0,10):C.GC_517,(0,11):C.GC_507,(0,6):C.GC_1537,(0,17):C.GC_84,(0,4):C.GC_86,(0,3):C.GC_474,(0,2):C.GC_486,(0,7):C.GC_1210,(0,9):C.GC_1549,(0,14):C.GC_4058,(0,15):C.GC_4060,(0,13):C.GC_4092,(0,8):C.GC_4059,(0,12):C.GC_1534,(0,16):C.GC_1209})

V_784 = Vertex(name = 'V_784',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV128, L.VVVVVV24, L.VVVVVV40, L.VVVVVV85, L.VVVVVV98, L.VVVVVV99 ],
               couplings = {(0,5):C.GC_463,(0,0):C.GC_470,(0,1):C.GC_788,(0,3):C.GC_4072,(0,2):C.GC_4068,(0,4):C.GC_1539})

V_785 = Vertex(name = 'V_785',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV10, L.VVVVVV104, L.VVVVVV113, L.VVVVVV47, L.VVVVVV59, L.VVVVVV77, L.VVVVVV91 ],
               couplings = {(0,0):C.GC_1171,(0,3):C.GC_1545,(0,2):C.GC_1528,(0,5):C.GC_1173,(0,4):C.GC_1541,(0,1):C.GC_1172,(0,6):C.GC_4689})

V_786 = Vertex(name = 'V_786',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV104, L.VVVVVV77, L.VVVVVV91 ],
               couplings = {(0,1):C.GC_781,(0,0):C.GC_1521,(0,2):C.GC_4696})

V_787 = Vertex(name = 'V_787',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV103, L.VVVVVV107, L.VVVVVV112, L.VVVVVV118, L.VVVVVV123, L.VVVVVV21, L.VVVVVV26, L.VVVVVV30, L.VVVVVV32, L.VVVVVV44, L.VVVVVV5, L.VVVVVV54, L.VVVVVV55, L.VVVVVV6, L.VVVVVV60, L.VVVVVV69, L.VVVVVV90, L.VVVVVV93, L.VVVVVV94 ],
               couplings = {(0,13):C.GC_1642,(0,5):C.GC_1647,(0,10):C.GC_1645,(0,11):C.GC_2020,(0,15):C.GC_2026,(0,9):C.GC_2011,(0,4):C.GC_1648,(0,3):C.GC_1998,(0,2):C.GC_2007,(0,1):C.GC_2030,(0,6):C.GC_4798,(0,0):C.GC_1646,(0,12):C.GC_1644,(0,7):C.GC_2003,(0,8):C.GC_1643,(0,14):C.GC_3993,(0,18):C.GC_3994,(0,17):C.GC_4797,(0,16):C.GC_4009})

V_788 = Vertex(name = 'V_788',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV103, L.VVVVVV123, L.VVVVVV26, L.VVVVVV32, L.VVVVVV55, L.VVVVVV60, L.VVVVVV93, L.VVVVVV94 ],
               couplings = {(0,1):C.GC_1996,(0,2):C.GC_4809,(0,0):C.GC_1991,(0,4):C.GC_945,(0,3):C.GC_2015,(0,5):C.GC_4000,(0,7):C.GC_3998,(0,6):C.GC_4132})

V_789 = Vertex(name = 'V_789',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV108, L.VVVVVV109, L.VVVVVV124, L.VVVVVV126, L.VVVVVV13, L.VVVVVV14, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV39, L.VVVVVV41, L.VVVVVV51, L.VVVVVV52, L.VVVVVV63, L.VVVVVV64, L.VVVVVV65, L.VVVVVV7, L.VVVVVV72, L.VVVVVV73, L.VVVVVV81, L.VVVVVV83, L.VVVVVV98 ],
               couplings = {(0,6):C.GC_122,(0,0):C.GC_1223,(0,21):C.GC_125,(0,5):C.GC_2307,(0,16):C.GC_499,(0,17):C.GC_518,(0,8):C.GC_1538,(0,7):C.GC_4872,(0,11):C.GC_2424,(0,18):C.GC_127,(0,9):C.GC_1222,(0,2):C.GC_475,(0,1):C.GC_522,(0,23):C.GC_508,(0,10):C.GC_2417,(0,4):C.GC_126,(0,3):C.GC_2305,(0,19):C.GC_124,(0,24):C.GC_2435,(0,14):C.GC_2306,(0,20):C.GC_1550,(0,12):C.GC_482,(0,13):C.GC_123,(0,15):C.GC_4870,(0,22):C.GC_1535,(0,26):C.GC_1221,(0,25):C.GC_4871})

V_790 = Vertex(name = 'V_790',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV124, L.VVVVVV126, L.VVVVVV22, L.VVVVVV24, L.VVVVVV37, L.VVVVVV39, L.VVVVVV41, L.VVVVVV63, L.VVVVVV64, L.VVVVVV83, L.VVVVVV98 ],
               couplings = {(0,2):C.GC_4883,(0,7):C.GC_487,(0,3):C.GC_789,(0,1):C.GC_464,(0,0):C.GC_2426,(0,8):C.GC_512,(0,5):C.GC_2951,(0,4):C.GC_502,(0,6):C.GC_4882,(0,10):C.GC_1540,(0,9):C.GC_4876})

V_791 = Vertex(name = 'V_791',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV101, L.VVVVVV120, L.VVVVVV124, L.VVVVVV125, L.VVVVVV129, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV25, L.VVVVVV35, L.VVVVVV39, L.VVVVVV41, L.VVVVVV62, L.VVVVVV68, L.VVVVVV81, L.VVVVVV83, L.VVVVVV86, L.VVVVVV87, L.VVVVVV88, L.VVVVVV89, L.VVVVVV95 ],
               couplings = {(0,7):C.GC_1208,(0,6):C.GC_1213,(0,5):C.GC_83,(0,13):C.GC_1546,(0,12):C.GC_1542,(0,9):C.GC_498,(0,3):C.GC_1212,(0,4):C.GC_1214,(0,0):C.GC_1529,(0,1):C.GC_1536,(0,8):C.GC_481,(0,2):C.GC_81,(0,14):C.GC_521,(0,10):C.GC_82,(0,11):C.GC_4736,(0,18):C.GC_3958,(0,16):C.GC_4738,(0,17):C.GC_3964,(0,19):C.GC_4093,(0,20):C.GC_3959,(0,15):C.GC_4737})

V_792 = Vertex(name = 'V_792',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV124, L.VVVVVV125, L.VVVVVV129, L.VVVVVV39, L.VVVVVV41, L.VVVVVV83, L.VVVVVV88, L.VVVVVV95 ],
               couplings = {(0,1):C.GC_1522,(0,2):C.GC_1527,(0,0):C.GC_501,(0,3):C.GC_511,(0,4):C.GC_4748,(0,6):C.GC_3963,(0,7):C.GC_3962,(0,5):C.GC_4747})

V_793 = Vertex(name = 'V_793',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV106, L.VVVVVV116, L.VVVVVV117, L.VVVVVV121, L.VVVVVV122, L.VVVVVV19, L.VVVVVV20, L.VVVVVV28, L.VVVVVV4, L.VVVVVV42, L.VVVVVV45, L.VVVVVV49, L.VVVVVV50, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV61, L.VVVVVV78, L.VVVVVV79, L.VVVVVV92 ],
               couplings = {(0,6):C.GC_1661,(0,8):C.GC_1665,(0,5):C.GC_2091,(0,10):C.GC_2013,(0,11):C.GC_2027,(0,12):C.GC_2275,(0,1):C.GC_1999,(0,0):C.GC_2032,(0,2):C.GC_2288,(0,14):C.GC_2021,(0,7):C.GC_2263,(0,4):C.GC_1667,(0,3):C.GC_2089,(0,13):C.GC_1664,(0,17):C.GC_1668,(0,18):C.GC_2090,(0,15):C.GC_2004,(0,16):C.GC_1662,(0,9):C.GC_4834,(0,19):C.GC_4833})

V_794 = Vertex(name = 'V_794',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV121, L.VVVVVV122, L.VVVVVV42, L.VVVVVV56, L.VVVVVV61, L.VVVVVV78, L.VVVVVV79, L.VVVVVV92 ],
               couplings = {(0,1):C.GC_1992,(0,0):C.GC_2278,(0,3):C.GC_946,(0,5):C.GC_942,(0,6):C.GC_2750,(0,4):C.GC_2016,(0,2):C.GC_4847,(0,7):C.GC_4843})

V_795 = Vertex(name = 'V_795',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV119, L.VVVVVV12, L.VVVVVV127, L.VVVVVV43, L.VVVVVV53, L.VVVVVV80, L.VVVVVV82 ],
               couplings = {(0,1):C.GC_592,(0,3):C.GC_790,(0,5):C.GC_594,(0,0):C.GC_780,(0,4):C.GC_787,(0,2):C.GC_593,(0,6):C.GC_4746})

V_796 = Vertex(name = 'V_796',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV127, L.VVVVVV80, L.VVVVVV82 ],
               couplings = {(0,1):C.GC_782,(0,0):C.GC_779,(0,2):C.GC_4758})

V_797 = Vertex(name = 'V_797',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS161 ],
               couplings = {(0,0):C.GC_3257})

V_798 = Vertex(name = 'V_798',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS161 ],
               couplings = {(0,0):C.GC_4229})

V_799 = Vertex(name = 'V_799',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS93 ],
               couplings = {(0,0):C.GC_3257})

V_800 = Vertex(name = 'V_800',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS93 ],
               couplings = {(0,0):C.GC_4229})

V_801 = Vertex(name = 'V_801',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS172, L.VVVVVS23 ],
               couplings = {(0,1):C.GC_4469,(0,0):C.GC_4496})

V_802 = Vertex(name = 'V_802',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS23 ],
               couplings = {(0,0):C.GC_4490})

V_803 = Vertex(name = 'V_803',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS171, L.VVVVVS172, L.VVVVVS23 ],
               couplings = {(0,2):C.GC_4373,(0,0):C.GC_3272,(0,1):C.GC_4400})

V_804 = Vertex(name = 'V_804',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS23 ],
               couplings = {(0,0):C.GC_4399})

V_805 = Vertex(name = 'V_805',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS175, L.VVVVVS37 ],
               couplings = {(0,1):C.GC_4269,(0,0):C.GC_4300})

V_806 = Vertex(name = 'V_806',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS37 ],
               couplings = {(0,0):C.GC_4297})

V_807 = Vertex(name = 'V_807',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS93 ],
               couplings = {(0,0):C.GC_4383})

V_808 = Vertex(name = 'V_808',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS93 ],
               couplings = {(0,0):C.GC_4401})

V_809 = Vertex(name = 'V_809',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS176, L.VVVVSS326 ],
               couplings = {(0,0):C.GC_1433,(0,1):C.GC_1155})

V_810 = Vertex(name = 'V_810',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS164 ],
               couplings = {(0,0):C.GC_3422})

V_811 = Vertex(name = 'V_811',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV102, L.VVVVVV105, L.VVVVVV3, L.VVVVVV34, L.VVVVVV38, L.VVVVVV74 ],
               couplings = {(0,2):C.GC_2781,(0,3):C.GC_2953,(0,4):C.GC_2783,(0,0):C.GC_2942,(0,5):C.GC_2949,(0,1):C.GC_2782})

V_812 = Vertex(name = 'V_812',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV105, L.VVVVVV38 ],
               couplings = {(0,1):C.GC_2945,(0,0):C.GC_2937})

V_813 = Vertex(name = 'V_813',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV100, L.VVVVVV110, L.VVVVVV111, L.VVVVVV2, L.VVVVVV27, L.VVVVVV29, L.VVVVVV31, L.VVVVVV33, L.VVVVVV46, L.VVVVVV48, L.VVVVVV67, L.VVVVVV70, L.VVVVVV75, L.VVVVVV76, L.VVVVVV8, L.VVVVVV9, L.VVVVVV96, L.VVVVVV97 ],
               couplings = {(0,3):C.GC_1666,(0,15):C.GC_2087,(0,14):C.GC_2092,(0,4):C.GC_2012,(0,8):C.GC_2285,(0,9):C.GC_2274,(0,5):C.GC_1664,(0,12):C.GC_2094,(0,0):C.GC_2031,(0,1):C.GC_2258,(0,2):C.GC_2287,(0,13):C.GC_2090,(0,6):C.GC_2262,(0,10):C.GC_2281,(0,7):C.GC_2088,(0,16):C.GC_2093,(0,11):C.GC_2005,(0,17):C.GC_1663})

V_814 = Vertex(name = 'V_814',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV29, L.VVVVVV33, L.VVVVVV75, L.VVVVVV76, L.VVVVVV96, L.VVVVVV97 ],
               couplings = {(0,0):C.GC_946,(0,2):C.GC_2743,(0,3):C.GC_2750,(0,1):C.GC_2277,(0,4):C.GC_2255,(0,5):C.GC_2017})

V_815 = Vertex(name = 'V_815',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS77 ],
               couplings = {(0,0):C.GC_163})

V_816 = Vertex(name = 'V_816',
               particles = [ P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS77 ],
               couplings = {(0,0):C.GC_458})

V_817 = Vertex(name = 'V_817',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS9 ],
               couplings = {(0,0):C.GC_4387})

V_818 = Vertex(name = 'V_818',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS9 ],
               couplings = {(0,0):C.GC_4432})

V_819 = Vertex(name = 'V_819',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS84, L.VVVSSSS92, L.VVVSSSS97 ],
               couplings = {(0,1):C.GC_1973,(0,0):C.GC_1684,(0,2):C.GC_1681})

V_820 = Vertex(name = 'V_820',
               particles = [ P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS84, L.VVVSSSS97 ],
               couplings = {(0,0):C.GC_1962,(0,1):C.GC_1988})

V_821 = Vertex(name = 'V_821',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS56, L.VVVSSSS79, L.VVVSSSS95 ],
               couplings = {(0,2):C.GC_1685,(0,1):C.GC_1680,(0,0):C.GC_1971})

V_822 = Vertex(name = 'V_822',
               particles = [ P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS79, L.VVVSSSS95 ],
               couplings = {(0,1):C.GC_1963,(0,0):C.GC_1987})

V_823 = Vertex(name = 'V_823',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,2):C.GC_1239,(0,0):C.GC_1497,(0,1):C.GC_1234})

V_824 = Vertex(name = 'V_824',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,1):C.GC_1475,(0,0):C.GC_1516})

V_825 = Vertex(name = 'V_825',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS25, L.VVVSSSS46, L.VVVSSSS61 ],
               couplings = {(0,1):C.GC_1238,(0,0):C.GC_1495,(0,2):C.GC_1237})

V_826 = Vertex(name = 'V_826',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS46, L.VVVSSSS61 ],
               couplings = {(0,0):C.GC_1474,(0,1):C.GC_1518})

V_827 = Vertex(name = 'V_827',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,2):C.GC_1233,(0,0):C.GC_1497,(0,1):C.GC_1240})

V_828 = Vertex(name = 'V_828',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,1):C.GC_1515,(0,0):C.GC_1476})

V_829 = Vertex(name = 'V_829',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3453,(0,1):C.GC_3457})

V_830 = Vertex(name = 'V_830',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4347,(0,1):C.GC_3569})

V_831 = Vertex(name = 'V_831',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3452,(0,1):C.GC_3456})

V_832 = Vertex(name = 'V_832',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4345,(0,1):C.GC_3568})

V_833 = Vertex(name = 'V_833',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS9 ],
               couplings = {(0,0):C.GC_4388})

V_834 = Vertex(name = 'V_834',
               particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS9 ],
               couplings = {(0,0):C.GC_4433})

V_835 = Vertex(name = 'V_835',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS53, L.VVVSSSS79, L.VVVSSSS96 ],
               couplings = {(0,2):C.GC_1972,(0,1):C.GC_1682,(0,0):C.GC_1683})

V_836 = Vertex(name = 'V_836',
               particles = [ P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS53, L.VVVSSSS79 ],
               couplings = {(0,1):C.GC_1989,(0,0):C.GC_1961})

V_837 = Vertex(name = 'V_837',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS50, L.VVVSSSS74, L.VVVSSSS94 ],
               couplings = {(0,1):C.GC_1680,(0,0):C.GC_1971,(0,2):C.GC_1685})

V_838 = Vertex(name = 'V_838',
               particles = [ P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS74, L.VVVSSSS94 ],
               couplings = {(0,0):C.GC_1987,(0,1):C.GC_1963})

V_839 = Vertex(name = 'V_839',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_3451,(0,1):C.GC_3455})

V_840 = Vertex(name = 'V_840',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_4344,(0,1):C.GC_3567})

V_841 = Vertex(name = 'V_841',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS102, L.VVVSSSS15, L.VVVSSSS64 ],
               couplings = {(0,2):C.GC_1232,(0,0):C.GC_1496,(0,1):C.GC_1242})

V_842 = Vertex(name = 'V_842',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS15, L.VVVSSSS64 ],
               couplings = {(0,1):C.GC_1514,(0,0):C.GC_1478})

V_843 = Vertex(name = 'V_843',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS12, L.VVVSSSS42, L.VVVSSSS43 ],
               couplings = {(0,1):C.GC_1233,(0,2):C.GC_1497,(0,0):C.GC_1242})

V_844 = Vertex(name = 'V_844',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS12, L.VVVSSSS42 ],
               couplings = {(0,1):C.GC_1515,(0,0):C.GC_1478})

V_845 = Vertex(name = 'V_845',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS19, L.VVVSSSS68 ],
               couplings = {(0,0):C.GC_1236,(0,1):C.GC_1243})

V_846 = Vertex(name = 'V_846',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS19, L.VVVSSSS68 ],
               couplings = {(0,0):C.GC_725,(0,1):C.GC_1479})

V_847 = Vertex(name = 'V_847',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS13, L.VVVSSSS20, L.VVVSSSS75 ],
               couplings = {(0,1):C.GC_1241,(0,0):C.GC_1235,(0,2):C.GC_1499})

V_848 = Vertex(name = 'V_848',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS13, L.VVVSSSS20 ],
               couplings = {(0,1):C.GC_1477,(0,0):C.GC_1517})

V_849 = Vertex(name = 'V_849',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3306,(0,1):C.GC_3300})

V_850 = Vertex(name = 'V_850',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3357,(0,1):C.GC_4243})

V_851 = Vertex(name = 'V_851',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3307,(0,1):C.GC_3301})

V_852 = Vertex(name = 'V_852',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3358,(0,1):C.GC_4244})

V_853 = Vertex(name = 'V_853',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3305,(0,1):C.GC_3299})

V_854 = Vertex(name = 'V_854',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3356,(0,1):C.GC_4242})

V_855 = Vertex(name = 'V_855',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS35, L.VVVSSSS85, L.VVVSSSS91 ],
               couplings = {(0,2):C.GC_989,(0,0):C.GC_979,(0,1):C.GC_1126})

V_856 = Vertex(name = 'V_856',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS35, L.VVVSSSS91 ],
               couplings = {(0,1):C.GC_1111,(0,0):C.GC_1131})

V_857 = Vertex(name = 'V_857',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS55, L.VVVSSSS59, L.VVVSSSS65 ],
               couplings = {(0,2):C.GC_980,(0,0):C.GC_990,(0,1):C.GC_1124})

V_858 = Vertex(name = 'V_858',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS55, L.VVVSSSS65 ],
               couplings = {(0,1):C.GC_1132,(0,0):C.GC_1112})

V_859 = Vertex(name = 'V_859',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS52, L.VVVSSSS80, L.VVVSSSS83 ],
               couplings = {(0,2):C.GC_984,(0,0):C.GC_982,(0,1):C.GC_1122})

V_860 = Vertex(name = 'V_860',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS52, L.VVVSSSS83 ],
               couplings = {(0,1):C.GC_1106,(0,0):C.GC_1134})

V_861 = Vertex(name = 'V_861',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS36, L.VVVSSSS41, L.VVVSSSS44 ],
               couplings = {(0,2):C.GC_980,(0,0):C.GC_988,(0,1):C.GC_1124})

V_862 = Vertex(name = 'V_862',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS36, L.VVVSSSS44 ],
               couplings = {(0,1):C.GC_1132,(0,0):C.GC_1110})

V_863 = Vertex(name = 'V_863',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS34, L.VVVSSSS90, L.VVVSSSS93 ],
               couplings = {(0,2):C.GC_983,(0,0):C.GC_982,(0,1):C.GC_1121})

V_864 = Vertex(name = 'V_864',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS34, L.VVVSSSS93 ],
               couplings = {(0,1):C.GC_1105,(0,0):C.GC_1134})

V_865 = Vertex(name = 'V_865',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS54, L.VVVSSSS63, L.VVVSSSS66 ],
               couplings = {(0,2):C.GC_976,(0,0):C.GC_992,(0,1):C.GC_1122})

V_866 = Vertex(name = 'V_866',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS54, L.VVVSSSS66 ],
               couplings = {(0,1):C.GC_1128,(0,0):C.GC_1114})

V_867 = Vertex(name = 'V_867',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3298,(0,1):C.GC_3306})

V_868 = Vertex(name = 'V_868',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_3379,(0,1):C.GC_4235})

V_869 = Vertex(name = 'V_869',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,2):C.GC_1240,(0,0):C.GC_1498,(0,1):C.GC_1233})

V_870 = Vertex(name = 'V_870',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,1):C.GC_1476,(0,0):C.GC_1515})

V_871 = Vertex(name = 'V_871',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS25, L.VVVSSSS46, L.VVVSSSS61 ],
               couplings = {(0,1):C.GC_1238,(0,0):C.GC_1495,(0,2):C.GC_1237})

V_872 = Vertex(name = 'V_872',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS46, L.VVVSSSS61 ],
               couplings = {(0,0):C.GC_1474,(0,1):C.GC_1518})

V_873 = Vertex(name = 'V_873',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS22, L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,2):C.GC_1234,(0,0):C.GC_1498,(0,1):C.GC_1239})

V_874 = Vertex(name = 'V_874',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS39, L.VVVSSSS62 ],
               couplings = {(0,1):C.GC_1516,(0,0):C.GC_1475})

V_875 = Vertex(name = 'V_875',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3308,(0,1):C.GC_3304})

V_876 = Vertex(name = 'V_876',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4236,(0,1):C.GC_3380})

V_877 = Vertex(name = 'V_877',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS17, L.VVVSSSS51, L.VVVSSSS57 ],
               couplings = {(0,2):C.GC_986,(0,0):C.GC_1123,(0,1):C.GC_981})

V_878 = Vertex(name = 'V_878',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS51, L.VVVSSSS57 ],
               couplings = {(0,1):C.GC_1108,(0,0):C.GC_1133})

V_879 = Vertex(name = 'V_879',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS14, L.VVVSSSS33, L.VVVSSSS38 ],
               couplings = {(0,2):C.GC_986,(0,0):C.GC_1123,(0,1):C.GC_978})

V_880 = Vertex(name = 'V_880',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS33, L.VVVSSSS38 ],
               couplings = {(0,1):C.GC_1108,(0,0):C.GC_1130})

V_881 = Vertex(name = 'V_881',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS16, L.VVVSSSS32, L.VVVSSSS47 ],
               couplings = {(0,2):C.GC_979,(0,0):C.GC_1125,(0,1):C.GC_987})

V_882 = Vertex(name = 'V_882',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS32, L.VVVSSSS47 ],
               couplings = {(0,1):C.GC_1131,(0,0):C.GC_1109})

V_883 = Vertex(name = 'V_883',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS18, L.VVVSSSS40, L.VVVSSSS58 ],
               couplings = {(0,2):C.GC_985,(0,0):C.GC_1122,(0,1):C.GC_982})

V_884 = Vertex(name = 'V_884',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS40, L.VVVSSSS58 ],
               couplings = {(0,1):C.GC_1107,(0,0):C.GC_1134})

V_885 = Vertex(name = 'V_885',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS23, L.VVVSSSS45, L.VVVSSSS60 ],
               couplings = {(0,2):C.GC_977,(0,0):C.GC_1122,(0,1):C.GC_991})

V_886 = Vertex(name = 'V_886',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS45, L.VVVSSSS60 ],
               couplings = {(0,1):C.GC_1129,(0,0):C.GC_1113})

V_887 = Vertex(name = 'V_887',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS24, L.VVVSSSS31, L.VVVSSSS82 ],
               couplings = {(0,2):C.GC_975,(0,0):C.GC_1121,(0,1):C.GC_991})

V_888 = Vertex(name = 'V_888',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS31, L.VVVSSSS82 ],
               couplings = {(0,1):C.GC_1127,(0,0):C.GC_1113})

V_889 = Vertex(name = 'V_889',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3246,(0,1):C.GC_3245})

V_890 = Vertex(name = 'V_890',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4213,(0,1):C.GC_3256})

V_891 = Vertex(name = 'V_891',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3450,(0,1):C.GC_3454})

V_892 = Vertex(name = 'V_892',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4342,(0,1):C.GC_3566})

V_893 = Vertex(name = 'V_893',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3452,(0,1):C.GC_3456})

V_894 = Vertex(name = 'V_894',
               particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4345,(0,1):C.GC_3568})

V_895 = Vertex(name = 'V_895',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3302,(0,1):C.GC_3308})

V_896 = Vertex(name = 'V_896',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4245,(0,1):C.GC_3359})

V_897 = Vertex(name = 'V_897',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3301,(0,1):C.GC_3307})

V_898 = Vertex(name = 'V_898',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4244,(0,1):C.GC_3358})

V_899 = Vertex(name = 'V_899',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3303,(0,1):C.GC_3309})

V_900 = Vertex(name = 'V_900',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4246,(0,1):C.GC_3360})

V_901 = Vertex(name = 'V_901',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_3244,(0,1):C.GC_3247})

V_902 = Vertex(name = 'V_902',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4214,(0,1):C.GC_3254})

V_903 = Vertex(name = 'V_903',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4202,(0,1):C.GC_3248})

V_904 = Vertex(name = 'V_904',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4215,(0,1):C.GC_3255})

V_905 = Vertex(name = 'V_905',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS6, L.VVVSSSS69 ],
               couplings = {(0,0):C.GC_2676,(0,1):C.GC_2572})

V_906 = Vertex(name = 'V_906',
               particles = [ P.a, P.a, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS69 ],
               couplings = {(0,0):C.GC_2728})

V_907 = Vertex(name = 'V_907',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS77 ],
               couplings = {(0,0):C.GC_2573})

V_908 = Vertex(name = 'V_908',
               particles = [ P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS77 ],
               couplings = {(0,0):C.GC_2729})

V_909 = Vertex(name = 'V_909',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS3, L.VVVVSSS7 ],
               couplings = {(0,2):C.GC_4196,(0,0):C.GC_4362,(0,1):C.GC_3580})

V_910 = Vertex(name = 'V_910',
               particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS10, L.VVVVSSS7 ],
               couplings = {(0,1):C.GC_4200,(0,0):C.GC_4292})

V_911 = Vertex(name = 'V_911',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS48 ],
               couplings = {(0,0):C.GC_607})

V_912 = Vertex(name = 'V_912',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS48 ],
               couplings = {(0,0):C.GC_733})

V_913 = Vertex(name = 'V_913',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS21, L.VVVSSSS71, L.VVVSSSS72, L.VVVSSSS78, L.VVVSSSS88, L.VVVSSSS89 ],
               couplings = {(0,5):C.GC_142,(0,1):C.GC_144,(0,4):C.GC_1259,(0,2):C.GC_1262,(0,3):C.GC_436,(0,0):C.GC_1500})

V_914 = Vertex(name = 'V_914',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS71, L.VVVSSSS72, L.VVVSSSS88, L.VVVSSSS89 ],
               couplings = {(0,3):C.GC_450,(0,0):C.GC_422,(0,2):C.GC_1519,(0,1):C.GC_1481})

V_915 = Vertex(name = 'V_915',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS37, L.VVVSSSS7, L.VVVSSSS70 ],
               couplings = {(0,1):C.GC_712,(0,0):C.GC_596,(0,2):C.GC_606})

V_916 = Vertex(name = 'V_916',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS37, L.VVVSSSS70 ],
               couplings = {(0,0):C.GC_731,(0,1):C.GC_706})

V_917 = Vertex(name = 'V_917',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS100, L.VVVSSSS101, L.VVVSSSS26, L.VVVSSSS49, L.VVVSSSS81, L.VVVSSSS99 ],
               couplings = {(0,1):C.GC_141,(0,5):C.GC_143,(0,3):C.GC_435,(0,0):C.GC_1260,(0,4):C.GC_1261,(0,2):C.GC_1501})

V_918 = Vertex(name = 'V_918',
               particles = [ P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS100, L.VVVSSSS101, L.VVVSSSS81, L.VVVSSSS99 ],
               couplings = {(0,1):C.GC_449,(0,3):C.GC_421,(0,0):C.GC_1520,(0,2):C.GC_1480})

V_919 = Vertex(name = 'V_919',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS5, L.VVVSSSS67, L.VVVSSSS98 ],
               couplings = {(0,0):C.GC_715,(0,1):C.GC_598,(0,2):C.GC_603})

V_920 = Vertex(name = 'V_920',
               particles = [ P.a, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS67, L.VVVSSSS98 ],
               couplings = {(0,0):C.GC_741,(0,1):C.GC_705})

V_921 = Vertex(name = 'V_921',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS73 ],
               couplings = {(0,0):C.GC_605})

V_922 = Vertex(name = 'V_922',
               particles = [ P.a, P.W__minus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS73 ],
               couplings = {(0,0):C.GC_742})

V_923 = Vertex(name = 'V_923',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS5, L.VVVVSSS6, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_4228,(0,1):C.GC_4391,(0,2):C.GC_3795})

V_924 = Vertex(name = 'V_924',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS5, L.VVVVSSS6 ],
               couplings = {(0,0):C.GC_4247,(0,1):C.GC_4434})

V_925 = Vertex(name = 'V_925',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS5, L.VVVVSSS6, L.VVVVSSS8 ],
               couplings = {(0,0):C.GC_4227,(0,1):C.GC_4395,(0,2):C.GC_3796})

V_926 = Vertex(name = 'V_926',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS5, L.VVVVSSS6 ],
               couplings = {(0,0):C.GC_4248,(0,1):C.GC_4438})

V_927 = Vertex(name = 'V_927',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS76, L.VVVSSSS86, L.VVVSSSS87 ],
               couplings = {(0,1):C.GC_559,(0,2):C.GC_828,(0,0):C.GC_1974})

V_928 = Vertex(name = 'V_928',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS86, L.VVVSSSS87 ],
               couplings = {(0,0):C.GC_575,(0,1):C.GC_919})

V_929 = Vertex(name = 'V_929',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_835,(0,3):C.GC_806,(0,7):C.GC_806,(0,9):C.GC_835,(0,10):C.GC_832,(0,11):C.GC_809,(0,1):C.GC_809,(0,2):C.GC_832,(0,4):C.GC_832,(0,5):C.GC_809,(0,6):C.GC_809,(0,8):C.GC_832})

V_930 = Vertex(name = 'V_930',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_927,(0,3):C.GC_895,(0,7):C.GC_895,(0,9):C.GC_927,(0,10):C.GC_925,(0,11):C.GC_897,(0,1):C.GC_897,(0,2):C.GC_925,(0,4):C.GC_925,(0,5):C.GC_897,(0,6):C.GC_897,(0,8):C.GC_925})

V_931 = Vertex(name = 'V_931',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_829,(0,3):C.GC_829,(0,7):C.GC_824,(0,9):C.GC_824,(0,10):C.GC_819,(0,11):C.GC_819,(0,1):C.GC_816,(0,2):C.GC_816,(0,4):C.GC_819,(0,5):C.GC_819,(0,6):C.GC_816,(0,8):C.GC_816})

V_932 = Vertex(name = 'V_932',
               particles = [ P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_921,(0,3):C.GC_921,(0,7):C.GC_917,(0,9):C.GC_917,(0,10):C.GC_911,(0,11):C.GC_911,(0,1):C.GC_906,(0,2):C.GC_906,(0,4):C.GC_911,(0,5):C.GC_911,(0,6):C.GC_906,(0,8):C.GC_906})

V_933 = Vertex(name = 'V_933',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4293,(0,1):C.GC_4293,(0,2):C.GC_4294})

V_934 = Vertex(name = 'V_934',
               particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4363,(0,1):C.GC_4363,(0,2):C.GC_4364})

V_935 = Vertex(name = 'V_935',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,4):C.GC_609,(0,5):C.GC_609,(0,0):C.GC_609,(0,1):C.GC_607,(0,2):C.GC_607,(0,3):C.GC_607})

V_936 = Vertex(name = 'V_936',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,4):C.GC_732,(0,5):C.GC_732,(0,0):C.GC_732,(0,1):C.GC_733,(0,2):C.GC_733,(0,3):C.GC_733})

V_937 = Vertex(name = 'V_937',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_611,(0,3):C.GC_612,(0,7):C.GC_612,(0,9):C.GC_614,(0,10):C.GC_714,(0,11):C.GC_608,(0,1):C.GC_608,(0,2):C.GC_615,(0,4):C.GC_611,(0,5):C.GC_613,(0,6):C.GC_613,(0,8):C.GC_597})

V_938 = Vertex(name = 'V_938',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_737,(0,3):C.GC_711,(0,7):C.GC_711,(0,9):C.GC_738,(0,10):C.GC_740,(0,1):C.GC_740,(0,2):C.GC_739,(0,4):C.GC_737,(0,5):C.GC_735,(0,6):C.GC_735,(0,8):C.GC_736})

V_939 = Vertex(name = 'V_939',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
               couplings = {(0,0):C.GC_713,(0,5):C.GC_710,(0,7):C.GC_710,(0,8):C.GC_610,(0,1):C.GC_596,(0,2):C.GC_596,(0,3):C.GC_610,(0,4):C.GC_606,(0,6):C.GC_606})

V_940 = Vertex(name = 'V_940',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8 ],
               couplings = {(0,5):C.GC_734,(0,0):C.GC_731,(0,1):C.GC_731,(0,2):C.GC_734,(0,3):C.GC_706,(0,4):C.GC_706})

V_941 = Vertex(name = 'V_941',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_600,(0,3):C.GC_600,(0,7):C.GC_602,(0,9):C.GC_619,(0,10):C.GC_617,(0,11):C.GC_617,(0,1):C.GC_620,(0,2):C.GC_716,(0,4):C.GC_601,(0,5):C.GC_601,(0,6):C.GC_599,(0,8):C.GC_619})

V_942 = Vertex(name = 'V_942',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_709,(0,2):C.GC_709,(0,6):C.GC_745,(0,8):C.GC_744,(0,9):C.GC_727,(0,10):C.GC_727,(0,1):C.GC_726,(0,3):C.GC_728,(0,4):C.GC_728,(0,5):C.GC_743,(0,7):C.GC_744})

V_943 = Vertex(name = 'V_943',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_715,(0,2):C.GC_715,(0,6):C.GC_708,(0,7):C.GC_598,(0,8):C.GC_598,(0,1):C.GC_604,(0,3):C.GC_616,(0,4):C.GC_616,(0,5):C.GC_604})

V_944 = Vertex(name = 'V_944',
               particles = [ P.a, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,4):C.GC_741,(0,5):C.GC_741,(0,0):C.GC_729,(0,1):C.GC_707,(0,2):C.GC_707,(0,3):C.GC_729})

V_945 = Vertex(name = 'V_945',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS9 ],
               couplings = {(0,5):C.GC_605,(0,0):C.GC_605,(0,1):C.GC_605,(0,2):C.GC_618,(0,3):C.GC_618,(0,4):C.GC_618})

V_946 = Vertex(name = 'V_946',
               particles = [ P.a, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS9 ],
               couplings = {(0,5):C.GC_742,(0,0):C.GC_742,(0,1):C.GC_742,(0,2):C.GC_730,(0,3):C.GC_730,(0,4):C.GC_730})

V_947 = Vertex(name = 'V_947',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4392,(0,1):C.GC_4393,(0,2):C.GC_4393})

V_948 = Vertex(name = 'V_948',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4436,(0,1):C.GC_4435,(0,2):C.GC_4435})

V_949 = Vertex(name = 'V_949',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_820,(0,7):C.GC_820,(0,0):C.GC_820,(0,1):C.GC_820,(0,2):C.GC_821,(0,3):C.GC_821,(0,4):C.GC_821,(0,5):C.GC_821})

V_950 = Vertex(name = 'V_950',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_914,(0,7):C.GC_914,(0,0):C.GC_914,(0,1):C.GC_914,(0,2):C.GC_913,(0,3):C.GC_913,(0,4):C.GC_913,(0,5):C.GC_913})

V_951 = Vertex(name = 'V_951',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,5):C.GC_819,(0,7):C.GC_815,(0,8):C.GC_817,(0,9):C.GC_817,(0,0):C.GC_803,(0,1):C.GC_823,(0,2):C.GC_814,(0,3):C.GC_814,(0,4):C.GC_827,(0,6):C.GC_802})

V_952 = Vertex(name = 'V_952',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,5):C.GC_909,(0,7):C.GC_904,(0,8):C.GC_882,(0,9):C.GC_882,(0,0):C.GC_910,(0,1):C.GC_903,(0,2):C.GC_883,(0,3):C.GC_883,(0,4):C.GC_908,(0,6):C.GC_905})

V_953 = Vertex(name = 'V_953',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_881,(0,3):C.GC_881,(0,7):C.GC_881,(0,9):C.GC_887,(0,10):C.GC_811,(0,11):C.GC_811,(0,1):C.GC_811,(0,2):C.GC_834,(0,4):C.GC_811,(0,5):C.GC_811,(0,6):C.GC_811,(0,8):C.GC_834})

V_954 = Vertex(name = 'V_954',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_900,(0,7):C.GC_900,(0,0):C.GC_900,(0,1):C.GC_926,(0,2):C.GC_900,(0,3):C.GC_900,(0,4):C.GC_900,(0,5):C.GC_926})

V_955 = Vertex(name = 'V_955',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_812,(0,7):C.GC_812,(0,0):C.GC_812,(0,1):C.GC_812,(0,2):C.GC_813,(0,3):C.GC_813,(0,4):C.GC_813,(0,5):C.GC_813})

V_956 = Vertex(name = 'V_956',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_902,(0,7):C.GC_902,(0,0):C.GC_902,(0,1):C.GC_902,(0,2):C.GC_901,(0,3):C.GC_901,(0,4):C.GC_901,(0,5):C.GC_901})

V_957 = Vertex(name = 'V_957',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_880,(0,3):C.GC_886,(0,7):C.GC_886,(0,9):C.GC_886,(0,10):C.GC_807,(0,11):C.GC_831,(0,1):C.GC_831,(0,2):C.GC_831,(0,4):C.GC_807,(0,5):C.GC_831,(0,6):C.GC_831,(0,8):C.GC_831})

V_958 = Vertex(name = 'V_958',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_896,(0,7):C.GC_922,(0,0):C.GC_922,(0,1):C.GC_922,(0,2):C.GC_896,(0,3):C.GC_922,(0,4):C.GC_922,(0,5):C.GC_922})

V_959 = Vertex(name = 'V_959',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
               couplings = {(0,0):C.GC_810,(0,4):C.GC_832,(0,5):C.GC_808,(0,1):C.GC_833,(0,2):C.GC_808,(0,3):C.GC_833})

V_960 = Vertex(name = 'V_960',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
               couplings = {(0,0):C.GC_899,(0,4):C.GC_924,(0,5):C.GC_898,(0,1):C.GC_923,(0,2):C.GC_898,(0,3):C.GC_923})

V_961 = Vertex(name = 'V_961',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_885,(0,3):C.GC_885,(0,7):C.GC_884,(0,9):C.GC_884,(0,10):C.GC_826,(0,11):C.GC_826,(0,1):C.GC_804,(0,2):C.GC_804,(0,4):C.GC_805,(0,5):C.GC_805,(0,6):C.GC_822,(0,8):C.GC_822})

V_962 = Vertex(name = 'V_962',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_879,(0,7):C.GC_879,(0,0):C.GC_915,(0,1):C.GC_915,(0,2):C.GC_918,(0,3):C.GC_918,(0,4):C.GC_878,(0,5):C.GC_878})

V_963 = Vertex(name = 'V_963',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_819,(0,3):C.GC_815,(0,8):C.GC_803,(0,9):C.GC_823,(0,1):C.GC_817,(0,2):C.GC_817,(0,4):C.GC_827,(0,5):C.GC_802,(0,6):C.GC_814,(0,7):C.GC_814})

V_964 = Vertex(name = 'V_964',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_909,(0,3):C.GC_904,(0,8):C.GC_910,(0,9):C.GC_903,(0,1):C.GC_882,(0,2):C.GC_882,(0,4):C.GC_908,(0,5):C.GC_905,(0,6):C.GC_883,(0,7):C.GC_883})

V_965 = Vertex(name = 'V_965',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_820,(0,7):C.GC_820,(0,0):C.GC_820,(0,1):C.GC_820,(0,2):C.GC_821,(0,3):C.GC_821,(0,4):C.GC_821,(0,5):C.GC_821})

V_966 = Vertex(name = 'V_966',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS30, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,6):C.GC_914,(0,7):C.GC_914,(0,0):C.GC_914,(0,1):C.GC_914,(0,2):C.GC_913,(0,3):C.GC_913,(0,4):C.GC_913,(0,5):C.GC_913})

V_967 = Vertex(name = 'V_967',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4285,(0,1):C.GC_4285,(0,2):C.GC_4286})

V_968 = Vertex(name = 'V_968',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4356,(0,1):C.GC_4356,(0,2):C.GC_4357})

V_969 = Vertex(name = 'V_969',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4286,(0,1):C.GC_4286,(0,2):C.GC_4288})

V_970 = Vertex(name = 'V_970',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4358,(0,1):C.GC_4358,(0,2):C.GC_4360})

V_971 = Vertex(name = 'V_971',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4283,(0,1):C.GC_4283,(0,2):C.GC_4284})

V_972 = Vertex(name = 'V_972',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4354,(0,1):C.GC_4354,(0,2):C.GC_4355})

V_973 = Vertex(name = 'V_973',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4287,(0,1):C.GC_4287,(0,2):C.GC_4289})

V_974 = Vertex(name = 'V_974',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4359,(0,1):C.GC_4359,(0,2):C.GC_4361})

V_975 = Vertex(name = 'V_975',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4398,(0,1):C.GC_4397,(0,2):C.GC_4397})

V_976 = Vertex(name = 'V_976',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4441,(0,1):C.GC_4440,(0,2):C.GC_4440})

V_977 = Vertex(name = 'V_977',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4396,(0,1):C.GC_4394,(0,2):C.GC_4394})

V_978 = Vertex(name = 'V_978',
               particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4439,(0,1):C.GC_4437,(0,2):C.GC_4437})

V_979 = Vertex(name = 'V_979',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_824,(0,3):C.GC_824,(0,7):C.GC_829,(0,9):C.GC_829,(0,10):C.GC_816,(0,11):C.GC_816,(0,1):C.GC_819,(0,2):C.GC_819,(0,4):C.GC_816,(0,5):C.GC_816,(0,6):C.GC_819,(0,8):C.GC_819})

V_980 = Vertex(name = 'V_980',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_917,(0,3):C.GC_917,(0,7):C.GC_921,(0,9):C.GC_921,(0,10):C.GC_906,(0,11):C.GC_906,(0,1):C.GC_911,(0,2):C.GC_911,(0,4):C.GC_906,(0,5):C.GC_906,(0,6):C.GC_911,(0,8):C.GC_911})

V_981 = Vertex(name = 'V_981',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_835,(0,3):C.GC_806,(0,7):C.GC_806,(0,9):C.GC_835,(0,10):C.GC_832,(0,11):C.GC_809,(0,1):C.GC_809,(0,2):C.GC_832,(0,4):C.GC_832,(0,5):C.GC_809,(0,6):C.GC_809,(0,8):C.GC_832})

V_982 = Vertex(name = 'V_982',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_927,(0,3):C.GC_895,(0,7):C.GC_895,(0,9):C.GC_927,(0,10):C.GC_925,(0,11):C.GC_897,(0,1):C.GC_897,(0,2):C.GC_925,(0,4):C.GC_925,(0,5):C.GC_897,(0,6):C.GC_897,(0,8):C.GC_925})

V_983 = Vertex(name = 'V_983',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_825,(0,3):C.GC_825,(0,7):C.GC_830,(0,9):C.GC_830,(0,10):C.GC_815,(0,11):C.GC_815,(0,1):C.GC_818,(0,2):C.GC_818,(0,4):C.GC_815,(0,5):C.GC_815,(0,6):C.GC_818,(0,8):C.GC_818})

V_984 = Vertex(name = 'V_984',
               particles = [ P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_916,(0,3):C.GC_916,(0,7):C.GC_920,(0,9):C.GC_920,(0,10):C.GC_907,(0,11):C.GC_907,(0,1):C.GC_912,(0,2):C.GC_912,(0,4):C.GC_907,(0,5):C.GC_907,(0,6):C.GC_912,(0,8):C.GC_912})

V_985 = Vertex(name = 'V_985',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4281,(0,1):C.GC_4282,(0,2):C.GC_4282})

V_986 = Vertex(name = 'V_986',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4351,(0,1):C.GC_4353,(0,2):C.GC_4353})

V_987 = Vertex(name = 'V_987',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4279,(0,1):C.GC_4281,(0,2):C.GC_4281})

V_988 = Vertex(name = 'V_988',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4349,(0,1):C.GC_4352,(0,2):C.GC_4352})

V_989 = Vertex(name = 'V_989',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4284,(0,1):C.GC_4283,(0,2):C.GC_4283})

V_990 = Vertex(name = 'V_990',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4355,(0,1):C.GC_4354,(0,2):C.GC_4354})

V_991 = Vertex(name = 'V_991',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4278,(0,1):C.GC_4280,(0,2):C.GC_4280})

V_992 = Vertex(name = 'V_992',
               particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4348,(0,1):C.GC_4350,(0,2):C.GC_4350})

V_993 = Vertex(name = 'V_993',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
               couplings = {(0,0):C.GC_2806,(0,4):C.GC_2801,(0,5):C.GC_2806,(0,1):C.GC_2801,(0,2):C.GC_2807,(0,3):C.GC_2800})

V_994 = Vertex(name = 'V_994',
               particles = [ P.a, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
               couplings = {(0,0):C.GC_2922,(0,4):C.GC_2917,(0,5):C.GC_2922,(0,1):C.GC_2917,(0,2):C.GC_2923,(0,3):C.GC_2916})

V_995 = Vertex(name = 'V_995',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_2804,(0,3):C.GC_2804,(0,7):C.GC_2805,(0,9):C.GC_2805,(0,10):C.GC_2804,(0,11):C.GC_2804,(0,1):C.GC_2805,(0,2):C.GC_2805,(0,4):C.GC_2804,(0,5):C.GC_2804,(0,6):C.GC_2805,(0,8):C.GC_2805})

V_996 = Vertex(name = 'V_996',
               particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_2920,(0,3):C.GC_2920,(0,7):C.GC_2921,(0,9):C.GC_2921,(0,10):C.GC_2920,(0,11):C.GC_2920,(0,1):C.GC_2921,(0,2):C.GC_2921,(0,4):C.GC_2920,(0,5):C.GC_2920,(0,6):C.GC_2921,(0,8):C.GC_2921})

V_997 = Vertex(name = 'V_997',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4474,(0,1):C.GC_4474,(0,2):C.GC_4550})

V_998 = Vertex(name = 'V_998',
               particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
               couplings = {(0,0):C.GC_4551,(0,1):C.GC_4551,(0,2):C.GC_4473})

V_999 = Vertex(name = 'V_999',
               particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
               couplings = {(0,0):C.GC_2543,(0,3):C.GC_2543,(0,7):C.GC_2543,(0,9):C.GC_2553,(0,10):C.GC_2543,(0,11):C.GC_2543,(0,1):C.GC_2543,(0,2):C.GC_2553,(0,4):C.GC_798,(0,5):C.GC_798,(0,6):C.GC_798,(0,8):C.GC_2672})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2701,(0,3):C.GC_2701,(0,7):C.GC_2701,(0,8):C.GC_2714,(0,9):C.GC_2701,(0,10):C.GC_2701,(0,1):C.GC_2701,(0,2):C.GC_2714,(0,4):C.GC_2669,(0,5):C.GC_2669,(0,6):C.GC_2669})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2536,(0,3):C.GC_2536,(0,7):C.GC_2537,(0,9):C.GC_2563,(0,10):C.GC_2536,(0,11):C.GC_2536,(0,1):C.GC_2537,(0,2):C.GC_2563,(0,4):C.GC_2534,(0,5):C.GC_2534,(0,6):C.GC_2665,(0,8):C.GC_2727})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2697,(0,3):C.GC_2697,(0,6):C.GC_2696,(0,8):C.GC_2725,(0,9):C.GC_2697,(0,10):C.GC_2697,(0,1):C.GC_2696,(0,2):C.GC_2725,(0,4):C.GC_2693,(0,5):C.GC_2693,(0,7):C.GC_2565})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2554,(0,3):C.GC_2539,(0,7):C.GC_2538,(0,9):C.GC_2538,(0,10):C.GC_2554,(0,11):C.GC_2539,(0,1):C.GC_2538,(0,2):C.GC_2538,(0,4):C.GC_2721,(0,5):C.GC_2666,(0,6):C.GC_2545,(0,8):C.GC_2545})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2717,(0,3):C.GC_2699,(0,6):C.GC_2700,(0,8):C.GC_2700,(0,9):C.GC_2717,(0,10):C.GC_2699,(0,1):C.GC_2700,(0,2):C.GC_2700,(0,4):C.GC_2558,(0,5):C.GC_2704,(0,7):C.GC_2704})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2550,(0,3):C.GC_2548,(0,7):C.GC_2546,(0,9):C.GC_2546,(0,10):C.GC_2550,(0,11):C.GC_2548,(0,1):C.GC_2546,(0,2):C.GC_2546,(0,4):C.GC_2671,(0,5):C.GC_2559,(0,6):C.GC_2544,(0,8):C.GC_2544})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2710,(0,3):C.GC_2713,(0,6):C.GC_2706,(0,8):C.GC_2706,(0,9):C.GC_2710,(0,10):C.GC_2713,(0,1):C.GC_2706,(0,2):C.GC_2706,(0,4):C.GC_2720,(0,5):C.GC_2707,(0,7):C.GC_2707})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2561,(0,3):C.GC_2535,(0,7):C.GC_2535,(0,9):C.GC_2562,(0,10):C.GC_2561,(0,11):C.GC_2535,(0,1):C.GC_2535,(0,2):C.GC_2562,(0,4):C.GC_2564,(0,5):C.GC_2533,(0,6):C.GC_2533,(0,8):C.GC_2675})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2724,(0,3):C.GC_2694,(0,7):C.GC_2694,(0,8):C.GC_2723,(0,9):C.GC_2724,(0,10):C.GC_2694,(0,1):C.GC_2694,(0,2):C.GC_2723,(0,4):C.GC_2726,(0,5):C.GC_2695,(0,6):C.GC_2695})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2532,(0,3):C.GC_2560,(0,7):C.GC_2560,(0,9):C.GC_2560,(0,10):C.GC_2532,(0,11):C.GC_2560,(0,1):C.GC_2560,(0,2):C.GC_2560,(0,4):C.GC_2664,(0,5):C.GC_797,(0,6):C.GC_797,(0,8):C.GC_797})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2692,(0,3):C.GC_2722,(0,6):C.GC_2722,(0,8):C.GC_2722,(0,9):C.GC_2692,(0,10):C.GC_2722,(0,1):C.GC_2722,(0,2):C.GC_2722,(0,4):C.GC_2674,(0,5):C.GC_2674,(0,7):C.GC_2674})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4204,(0,1):C.GC_4204,(0,2):C.GC_4210})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4221,(0,1):C.GC_4221,(0,2):C.GC_4216})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4207,(0,1):C.GC_4207,(0,2):C.GC_4208})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4218,(0,1):C.GC_4218,(0,2):C.GC_4220})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4480,(0,1):C.GC_4480,(0,2):C.GC_4558})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4557,(0,1):C.GC_4557,(0,2):C.GC_4481})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2540,(0,3):C.GC_2540,(0,7):C.GC_2540,(0,9):C.GC_2555,(0,10):C.GC_2540,(0,11):C.GC_2540,(0,1):C.GC_2540,(0,2):C.GC_2555,(0,4):C.GC_799,(0,5):C.GC_799,(0,6):C.GC_799,(0,8):C.GC_2673})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2698,(0,3):C.GC_2698,(0,7):C.GC_2698,(0,8):C.GC_2716,(0,9):C.GC_2698,(0,10):C.GC_2698,(0,1):C.GC_2698,(0,2):C.GC_2716,(0,4):C.GC_2667,(0,5):C.GC_2667,(0,6):C.GC_2667})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2536,(0,3):C.GC_2536,(0,7):C.GC_2537,(0,9):C.GC_2563,(0,10):C.GC_2536,(0,11):C.GC_2536,(0,1):C.GC_2537,(0,2):C.GC_2563,(0,4):C.GC_2534,(0,5):C.GC_2534,(0,6):C.GC_2665,(0,8):C.GC_2727})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2697,(0,3):C.GC_2697,(0,6):C.GC_2696,(0,8):C.GC_2725,(0,9):C.GC_2697,(0,10):C.GC_2697,(0,1):C.GC_2696,(0,2):C.GC_2725,(0,4):C.GC_2693,(0,5):C.GC_2693,(0,7):C.GC_2565})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2552,(0,3):C.GC_2542,(0,7):C.GC_2541,(0,9):C.GC_2541,(0,10):C.GC_2552,(0,11):C.GC_2542,(0,1):C.GC_2541,(0,2):C.GC_2541,(0,4):C.GC_2719,(0,5):C.GC_2668,(0,6):C.GC_2551,(0,8):C.GC_2551})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2715,(0,3):C.GC_2702,(0,6):C.GC_2703,(0,8):C.GC_2703,(0,9):C.GC_2715,(0,10):C.GC_2702,(0,1):C.GC_2703,(0,2):C.GC_2703,(0,4):C.GC_2556,(0,5):C.GC_2709,(0,7):C.GC_2709})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2547,(0,3):C.GC_2549,(0,7):C.GC_2549,(0,9):C.GC_2544,(0,10):C.GC_2547,(0,11):C.GC_2549,(0,1):C.GC_2549,(0,2):C.GC_2544,(0,4):C.GC_2670,(0,5):C.GC_2548,(0,6):C.GC_2548,(0,8):C.GC_2557})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2705,(0,3):C.GC_2711,(0,6):C.GC_2711,(0,8):C.GC_2708,(0,9):C.GC_2705,(0,10):C.GC_2711,(0,1):C.GC_2711,(0,2):C.GC_2708,(0,4):C.GC_2712,(0,5):C.GC_2712,(0,7):C.GC_2718})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2535,(0,3):C.GC_2535,(0,7):C.GC_2561,(0,9):C.GC_2562,(0,10):C.GC_2535,(0,11):C.GC_2535,(0,1):C.GC_2561,(0,2):C.GC_2562,(0,4):C.GC_2533,(0,5):C.GC_2533,(0,6):C.GC_2564,(0,8):C.GC_2675})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2694,(0,3):C.GC_2694,(0,7):C.GC_2724,(0,8):C.GC_2723,(0,9):C.GC_2694,(0,10):C.GC_2694,(0,1):C.GC_2724,(0,2):C.GC_2723,(0,4):C.GC_2695,(0,5):C.GC_2695,(0,6):C.GC_2726})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2532,(0,3):C.GC_2560,(0,7):C.GC_2560,(0,9):C.GC_2560,(0,10):C.GC_2532,(0,11):C.GC_2560,(0,1):C.GC_2560,(0,2):C.GC_2560,(0,4):C.GC_2664,(0,5):C.GC_797,(0,6):C.GC_797,(0,8):C.GC_797})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2692,(0,3):C.GC_2722,(0,6):C.GC_2722,(0,8):C.GC_2722,(0,9):C.GC_2692,(0,10):C.GC_2722,(0,1):C.GC_2722,(0,2):C.GC_2722,(0,4):C.GC_2674,(0,5):C.GC_2674,(0,7):C.GC_2674})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4206,(0,1):C.GC_4206,(0,2):C.GC_4205})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4212,(0,1):C.GC_4212,(0,2):C.GC_4219})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4209,(0,1):C.GC_4209,(0,2):C.GC_4203})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4217,(0,1):C.GC_4217,(0,2):C.GC_4222})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4207,(0,1):C.GC_4207,(0,2):C.GC_4208})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4218,(0,1):C.GC_4218,(0,2):C.GC_4220})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4592,(0,1):C.GC_4592,(0,2):C.GC_4627})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4640,(0,1):C.GC_4640})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4 ],
                couplings = {(0,3):C.GC_2802,(0,5):C.GC_2803,(0,0):C.GC_2802,(0,1):C.GC_2803,(0,2):C.GC_2909,(0,4):C.GC_2910})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS3, L.VVVSSSS4 ],
                couplings = {(0,2):C.GC_2918,(0,3):C.GC_2919,(0,0):C.GC_2918,(0,1):C.GC_2919})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2802,(0,1):C.GC_2803,(0,4):C.GC_2802,(0,5):C.GC_2803,(0,2):C.GC_2909,(0,3):C.GC_2910})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS2, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2918,(0,1):C.GC_2919,(0,2):C.GC_2918,(0,3):C.GC_2919})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4476,(0,1):C.GC_4476,(0,2):C.GC_4533})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4553,(0,1):C.GC_4553})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4477,(0,1):C.GC_4477,(0,2):C.GC_4534})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4554,(0,1):C.GC_4554})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4475,(0,1):C.GC_4475,(0,2):C.GC_4532})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4552,(0,1):C.GC_4552})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4478,(0,1):C.GC_4478,(0,2):C.GC_4535})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4555,(0,1):C.GC_4555})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4477,(0,1):C.GC_4477,(0,2):C.GC_4534})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4554,(0,1):C.GC_4554})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4479,(0,1):C.GC_4479,(0,2):C.GC_4536})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4556,(0,1):C.GC_4556})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4275,(0,1):C.GC_4275,(0,2):C.GC_4331})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
                couplings = {(0,0):C.GC_4343,(0,1):C.GC_4343})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4276,(0,1):C.GC_4276,(0,2):C.GC_4277})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4346,(0,1):C.GC_4346,(0,2):C.GC_4332})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4647,(0,1):C.GC_4647,(0,2):C.GC_4647})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4663,(0,1):C.GC_4663,(0,2):C.GC_4663})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2971,(0,3):C.GC_2971,(0,7):C.GC_2971,(0,9):C.GC_2979,(0,10):C.GC_2971,(0,11):C.GC_2971,(0,1):C.GC_2971,(0,2):C.GC_2979,(0,4):C.GC_2971,(0,5):C.GC_2971,(0,6):C.GC_2971,(0,8):C.GC_2979})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_3011,(0,3):C.GC_3011,(0,7):C.GC_3011,(0,9):C.GC_3019,(0,10):C.GC_3011,(0,11):C.GC_3011,(0,1):C.GC_3011,(0,2):C.GC_3019,(0,4):C.GC_3011,(0,5):C.GC_3011,(0,6):C.GC_3011,(0,8):C.GC_3019})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
                couplings = {(0,0):C.GC_2972,(0,4):C.GC_2977,(0,5):C.GC_2972,(0,1):C.GC_2977,(0,2):C.GC_2972,(0,3):C.GC_2977})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS11, L.VVVSSSS27, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8 ],
                couplings = {(0,0):C.GC_3012,(0,4):C.GC_3017,(0,5):C.GC_3012,(0,1):C.GC_3017,(0,2):C.GC_3012,(0,3):C.GC_3017})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2970,(0,3):C.GC_2978,(0,7):C.GC_2978,(0,9):C.GC_2978,(0,10):C.GC_2970,(0,11):C.GC_2978,(0,1):C.GC_2978,(0,2):C.GC_2978,(0,4):C.GC_2970,(0,5):C.GC_2978,(0,6):C.GC_2978,(0,8):C.GC_2978})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_3010,(0,3):C.GC_3018,(0,7):C.GC_3018,(0,9):C.GC_3018,(0,10):C.GC_3010,(0,11):C.GC_3018,(0,1):C.GC_3018,(0,2):C.GC_3018,(0,4):C.GC_3010,(0,5):C.GC_3018,(0,6):C.GC_3018,(0,8):C.GC_3018})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4 ],
                couplings = {(0,3):C.GC_2974,(0,5):C.GC_2973,(0,0):C.GC_2974,(0,1):C.GC_2973,(0,2):C.GC_2974,(0,4):C.GC_2973})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4 ],
                couplings = {(0,3):C.GC_3014,(0,5):C.GC_3013,(0,0):C.GC_3014,(0,1):C.GC_3013,(0,2):C.GC_3014,(0,4):C.GC_3013})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2976,(0,3):C.GC_2976,(0,7):C.GC_2975,(0,9):C.GC_2975,(0,10):C.GC_2976,(0,11):C.GC_2976,(0,1):C.GC_2975,(0,2):C.GC_2975,(0,4):C.GC_2976,(0,5):C.GC_2976,(0,6):C.GC_2975,(0,8):C.GC_2975})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS10, L.VVVSSSS11, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS29, L.VVVSSSS3, L.VVVSSSS30, L.VVVSSSS4, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_3016,(0,3):C.GC_3016,(0,7):C.GC_3015,(0,9):C.GC_3015,(0,10):C.GC_3016,(0,11):C.GC_3016,(0,1):C.GC_3015,(0,2):C.GC_3015,(0,4):C.GC_3016,(0,5):C.GC_3016,(0,6):C.GC_3015,(0,8):C.GC_3015})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_2974,(0,1):C.GC_2973,(0,4):C.GC_2974,(0,5):C.GC_2973,(0,2):C.GC_2974,(0,3):C.GC_2973})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVSSSS1, L.VVVSSSS2, L.VVVSSSS27, L.VVVSSSS28, L.VVVSSSS8, L.VVVSSSS9 ],
                couplings = {(0,0):C.GC_3014,(0,1):C.GC_3013,(0,4):C.GC_3014,(0,5):C.GC_3013,(0,2):C.GC_3014,(0,3):C.GC_3013})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4586,(0,1):C.GC_4586,(0,2):C.GC_4586})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4637,(0,1):C.GC_4637,(0,2):C.GC_4637})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4587,(0,1):C.GC_4587,(0,2):C.GC_4587})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4638,(0,1):C.GC_4638,(0,2):C.GC_4638})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4585,(0,1):C.GC_4585,(0,2):C.GC_4585})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4636,(0,1):C.GC_4636,(0,2):C.GC_4636})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4588,(0,1):C.GC_4588,(0,2):C.GC_4588})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4639,(0,1):C.GC_4639,(0,2):C.GC_4639})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4584,(0,1):C.GC_4584,(0,2):C.GC_4584})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4635,(0,1):C.GC_4635,(0,2):C.GC_4635})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4583,(0,1):C.GC_4583,(0,2):C.GC_4583})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4634,(0,1):C.GC_4634,(0,2):C.GC_4634})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4585,(0,1):C.GC_4585,(0,2):C.GC_4585})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4636,(0,1):C.GC_4636,(0,2):C.GC_4636})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4582,(0,1):C.GC_4582,(0,2):C.GC_4582})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4633,(0,1):C.GC_4633,(0,2):C.GC_4633})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4671,(0,1):C.GC_4671,(0,2):C.GC_4671})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4682,(0,1):C.GC_4682,(0,2):C.GC_4682})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4670,(0,1):C.GC_4670,(0,2):C.GC_4670})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4681,(0,1):C.GC_4681,(0,2):C.GC_4681})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4672,(0,1):C.GC_4672,(0,2):C.GC_4672})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSS1, L.VVVVSSS2, L.VVVVSSS4 ],
                couplings = {(0,0):C.GC_4683,(0,1):C.GC_4683,(0,2):C.GC_4683})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS205, L.VVVVVSS216, L.VVVVVSS34, L.VVVVVSS36, L.VVVVVSS51, L.VVVVVSS6, L.VVVVVSS8 ],
                couplings = {(0,3):C.GC_394,(0,5):C.GC_1864,(0,6):C.GC_368,(0,2):C.GC_1788,(0,1):C.GC_130,(0,4):C.GC_836,(0,0):C.GC_203})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS216, L.VVVVVSS51 ],
                couplings = {(0,0):C.GC_183,(0,1):C.GC_870})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS13, L.VVVVVSS142, L.VVVVVSS144, L.VVVVVSS145, L.VVVVVSS16, L.VVVVVSS181, L.VVVVVSS19, L.VVVVVSS198, L.VVVVVSS199, L.VVVVVSS209, L.VVVVVSS21, L.VVVVVSS219, L.VVVVVSS220, L.VVVVVSS225, L.VVVVVSS30, L.VVVVVSS74, L.VVVVVSS75, L.VVVVVSS76, L.VVVVVSS79 ],
                couplings = {(0,10):C.GC_324,(0,0):C.GC_1403,(0,17):C.GC_1933,(0,18):C.GC_2247,(0,4):C.GC_1911,(0,16):C.GC_243,(0,15):C.GC_1352,(0,6):C.GC_2227,(0,1):C.GC_688,(0,7):C.GC_345,(0,2):C.GC_1265,(0,3):C.GC_1421,(0,12):C.GC_1693,(0,9):C.GC_1754,(0,13):C.GC_2102,(0,11):C.GC_2124,(0,8):C.GC_1692,(0,14):C.GC_2101,(0,5):C.GC_128})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS144, L.VVVVVSS181, L.VVVVVSS199, L.VVVVVSS30 ],
                couplings = {(0,0):C.GC_1387,(0,2):C.GC_1731,(0,3):C.GC_2117,(0,1):C.GC_299})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS12, L.VVVVVSS139, L.VVVVVSS140, L.VVVVVSS141, L.VVVVVSS20, L.VVVVVSS207, L.VVVVVSS208, L.VVVVVSS24, L.VVVVVSS57, L.VVVVVSS67 ],
                couplings = {(0,0):C.GC_1401,(0,7):C.GC_1930,(0,9):C.GC_1346,(0,4):C.GC_1908,(0,1):C.GC_1249,(0,2):C.GC_1365,(0,3):C.GC_1414,(0,8):C.GC_1675,(0,5):C.GC_1750,(0,6):C.GC_1678})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS139, L.VVVVVSS57 ],
                couplings = {(0,0):C.GC_1382,(0,1):C.GC_1727})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS12, L.VVVVVSS139, L.VVVVVSS140, L.VVVVVSS141, L.VVVVVSS20, L.VVVVVSS234, L.VVVVVSS24, L.VVVVVSS241, L.VVVVVSS56, L.VVVVVSS67 ],
                couplings = {(0,0):C.GC_1399,(0,6):C.GC_1928,(0,9):C.GC_1349,(0,4):C.GC_1910,(0,1):C.GC_1247,(0,2):C.GC_1366,(0,3):C.GC_1417,(0,8):C.GC_1673,(0,5):C.GC_1752,(0,7):C.GC_1679})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS139, L.VVVVVSS56 ],
                couplings = {(0,0):C.GC_1380,(0,1):C.GC_1725})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS106, L.VVVVVSS108, L.VVVVVSS120, L.VVVVVSS121, L.VVVVVSS122, L.VVVVVSS124, L.VVVVVSS152, L.VVVVVSS157, L.VVVVVSS162, L.VVVVVSS179, L.VVVVVSS203, L.VVVVVSS211, L.VVVVVSS224, L.VVVVVSS27, L.VVVVVSS3, L.VVVVVSS4, L.VVVVVSS61, L.VVVVVSS93 ],
                couplings = {(0,15):C.GC_1088,(0,2):C.GC_395,(0,0):C.GC_1445,(0,1):C.GC_1861,(0,16):C.GC_1430,(0,14):C.GC_1784,(0,8):C.GC_205,(0,3):C.GC_1094,(0,10):C.GC_1814,(0,12):C.GC_140,(0,6):C.GC_1253,(0,11):C.GC_1257,(0,13):C.GC_1320,(0,9):C.GC_1887,(0,5):C.GC_1669,(0,17):C.GC_1076,(0,4):C.GC_1002,(0,18):C.GC_370,(0,7):C.GC_136})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS121, L.VVVVVSS122, L.VVVVVSS124, L.VVVVVSS152 ],
                couplings = {(0,2):C.GC_1305,(0,1):C.GC_1835,(0,0):C.GC_1082,(0,3):C.GC_185})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS100, L.VVVVVSS106, L.VVVVVSS108, L.VVVVVSS120, L.VVVVVSS121, L.VVVVVSS122, L.VVVVVSS125, L.VVVVVSS152, L.VVVVVSS157, L.VVVVVSS162, L.VVVVVSS179, L.VVVVVSS211, L.VVVVVSS217, L.VVVVVSS231, L.VVVVVSS27, L.VVVVVSS3, L.VVVVVSS4, L.VVVVVSS61, L.VVVVVSS93 ],
                couplings = {(0,15):C.GC_1087,(0,2):C.GC_397,(0,0):C.GC_1447,(0,1):C.GC_1860,(0,16):C.GC_1431,(0,14):C.GC_1783,(0,8):C.GC_207,(0,3):C.GC_1095,(0,10):C.GC_1812,(0,11):C.GC_138,(0,6):C.GC_1252,(0,13):C.GC_1256,(0,12):C.GC_1321,(0,9):C.GC_1888,(0,5):C.GC_1671,(0,17):C.GC_1074,(0,4):C.GC_1004,(0,18):C.GC_369,(0,7):C.GC_137})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS121, L.VVVVVSS122, L.VVVVVSS125, L.VVVVVSS152 ],
                couplings = {(0,2):C.GC_1304,(0,1):C.GC_1837,(0,0):C.GC_1084,(0,3):C.GC_186})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS11, L.VVVVVSS138, L.VVVVVSS142, L.VVVVVSS177, L.VVVVVSS18, L.VVVVVSS214, L.VVVVVSS218, L.VVVVVSS26, L.VVVVVSS29, L.VVVVVSS9 ],
                couplings = {(0,9):C.GC_1401,(0,4):C.GC_1929,(0,7):C.GC_1346,(0,0):C.GC_1908,(0,8):C.GC_1249,(0,2):C.GC_1367,(0,1):C.GC_1414,(0,3):C.GC_1675,(0,5):C.GC_1750,(0,6):C.GC_1678})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS177, L.VVVVVSS29 ],
                couplings = {(0,1):C.GC_1382,(0,0):C.GC_1727})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS11, L.VVVVVSS138, L.VVVVVSS142, L.VVVVVSS178, L.VVVVVSS18, L.VVVVVSS223, L.VVVVVSS238, L.VVVVVSS26, L.VVVVVSS29, L.VVVVVSS9 ],
                couplings = {(0,9):C.GC_1402,(0,4):C.GC_1928,(0,7):C.GC_1345,(0,0):C.GC_1907,(0,8):C.GC_1251,(0,2):C.GC_1366,(0,1):C.GC_1413,(0,3):C.GC_1676,(0,5):C.GC_1749,(0,6):C.GC_1677})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS178, L.VVVVVSS29 ],
                couplings = {(0,1):C.GC_1384,(0,0):C.GC_1728})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS1, L.VVVVVSS135, L.VVVVVSS159, L.VVVVVSS163, L.VVVVVSS164, L.VVVVVSS180, L.VVVVVSS2, L.VVVVVSS232, L.VVVVVSS233, L.VVVVVSS236, L.VVVVVSS31, L.VVVVVSS39, L.VVVVVSS44, L.VVVVVSS47, L.VVVVVSS48, L.VVVVVSS53, L.VVVVVSS7, L.VVVVVSS87, L.VVVVVSS98 ],
                couplings = {(0,0):C.GC_1088,(0,18):C.GC_396,(0,17):C.GC_1446,(0,12):C.GC_1861,(0,6):C.GC_1430,(0,16):C.GC_1784,(0,10):C.GC_1075,(0,2):C.GC_206,(0,13):C.GC_1003,(0,14):C.GC_1093,(0,5):C.GC_1811,(0,9):C.GC_139,(0,7):C.GC_1258,(0,8):C.GC_1320,(0,3):C.GC_1670,(0,4):C.GC_1886,(0,1):C.GC_1253,(0,11):C.GC_370,(0,15):C.GC_136})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS135, L.VVVVVSS163, L.VVVVVSS47, L.VVVVVSS53 ],
                couplings = {(0,2):C.GC_1083,(0,1):C.GC_1836,(0,0):C.GC_1305,(0,3):C.GC_185})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS1, L.VVVVVSS134, L.VVVVVSS159, L.VVVVVSS163, L.VVVVVSS164, L.VVVVVSS180, L.VVVVVSS2, L.VVVVVSS204, L.VVVVVSS206, L.VVVVVSS236, L.VVVVVSS31, L.VVVVVSS39, L.VVVVVSS44, L.VVVVVSS47, L.VVVVVSS48, L.VVVVVSS53, L.VVVVVSS7, L.VVVVVSS87, L.VVVVVSS98 ],
                couplings = {(0,0):C.GC_1089,(0,18):C.GC_397,(0,17):C.GC_1448,(0,12):C.GC_1862,(0,6):C.GC_1429,(0,16):C.GC_1785,(0,10):C.GC_1074,(0,2):C.GC_204,(0,13):C.GC_1004,(0,14):C.GC_1092,(0,5):C.GC_1813,(0,9):C.GC_138,(0,7):C.GC_1255,(0,8):C.GC_1319,(0,3):C.GC_1672,(0,4):C.GC_1885,(0,1):C.GC_1254,(0,11):C.GC_371,(0,15):C.GC_135})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS134, L.VVVVVSS163, L.VVVVVSS47, L.VVVVVSS53 ],
                couplings = {(0,2):C.GC_1084,(0,1):C.GC_1838,(0,0):C.GC_1306,(0,3):C.GC_184})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS195, L.VVVVVSS196, L.VVVVVSS32, L.VVVVVSS40, L.VVVVVSS46, L.VVVVVSS58, L.VVVVVSS99 ],
                couplings = {(0,6):C.GC_1443,(0,0):C.GC_1229,(0,1):C.GC_1318,(0,2):C.GC_1073,(0,3):C.GC_1428,(0,4):C.GC_993,(0,5):C.GC_1227})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS46, L.VVVVVSS58 ],
                couplings = {(0,0):C.GC_567,(0,1):C.GC_1303})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS197, L.VVVVVSS237, L.VVVVVSS239, L.VVVVVSS32, L.VVVVVSS40, L.VVVVVSS46, L.VVVVVSS96 ],
                couplings = {(0,6):C.GC_1444,(0,1):C.GC_1230,(0,0):C.GC_1318,(0,3):C.GC_1072,(0,4):C.GC_1428,(0,5):C.GC_994,(0,2):C.GC_1227})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS239, L.VVVVVSS46 ],
                couplings = {(0,1):C.GC_568,(0,0):C.GC_1303})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS194, L.VVVVVSS195, L.VVVVVSS196, L.VVVVVSS32, L.VVVVVSS40, L.VVVVVSS46, L.VVVVVSS58, L.VVVVVSS95, L.VVVVVSS99 ],
                couplings = {(0,7):C.GC_1231,(0,8):C.GC_1443,(0,2):C.GC_1226,(0,1):C.GC_1229,(0,0):C.GC_1452,(0,3):C.GC_1073,(0,4):C.GC_1428,(0,5):C.GC_558,(0,6):C.GC_1227})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS196, L.VVVVVSS46, L.VVVVVSS58, L.VVVVVSS95 ],
                couplings = {(0,3):C.GC_1459,(0,0):C.GC_1318,(0,1):C.GC_567,(0,2):C.GC_1303})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS11, L.VVVVVSS158, L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS175, L.VVVVVSS80, L.VVVVVSS81 ],
                couplings = {(0,7):C.GC_1099,(0,6):C.GC_1931,(0,1):C.GC_1098,(0,0):C.GC_1342,(0,5):C.GC_996,(0,2):C.GC_801,(0,3):C.GC_1061,(0,4):C.GC_1225})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS161, L.VVVVVSS175 ],
                couplings = {(0,1):C.GC_1051,(0,0):C.GC_693})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS11, L.VVVVVSS158, L.VVVVVSS161, L.VVVVVSS176, L.VVVVVSS212, L.VVVVVSS215, L.VVVVVSS222, L.VVVVVSS28, L.VVVVVSS80, L.VVVVVSS81 ],
                couplings = {(0,10):C.GC_1099,(0,9):C.GC_1932,(0,1):C.GC_1098,(0,0):C.GC_1343,(0,4):C.GC_996,(0,7):C.GC_998,(0,6):C.GC_1061,(0,2):C.GC_1687,(0,8):C.GC_1686,(0,3):C.GC_1224,(0,5):C.GC_1753})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS161, L.VVVVVSS176, L.VVVVVSS28 ],
                couplings = {(0,1):C.GC_1051,(0,2):C.GC_1729,(0,0):C.GC_692})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS10, L.VVVVVSS11, L.VVVVVSS158, L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS175, L.VVVVVSS193, L.VVVVVSS25, L.VVVVVSS71, L.VVVVVSS80, L.VVVVVSS81 ],
                couplings = {(0,7):C.GC_999,(0,10):C.GC_1099,(0,8):C.GC_1688,(0,9):C.GC_1931,(0,1):C.GC_1098,(0,0):C.GC_1342,(0,3):C.GC_995,(0,5):C.GC_996,(0,2):C.GC_801,(0,6):C.GC_1100,(0,4):C.GC_595})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS158, L.VVVVVSS160, L.VVVVVSS161, L.VVVVVSS175, L.VVVVVSS25, L.VVVVVSS71 ],
                couplings = {(0,4):C.GC_1103,(0,5):C.GC_1945,(0,1):C.GC_1061,(0,3):C.GC_1051,(0,0):C.GC_1936,(0,2):C.GC_693})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS33, L.VVVVVSS35, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS52, L.VVVVVSS6 ],
                couplings = {(0,1):C.GC_2895,(0,5):C.GC_2633,(0,0):C.GC_2610,(0,3):C.GC_2812,(0,4):C.GC_2636,(0,2):C.GC_2527})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS49, L.VVVVVSS51 ],
                couplings = {(0,1):C.GC_2623,(0,0):C.GC_2630})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS33, L.VVVVVSS35, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS52, L.VVVVVSS6 ],
                couplings = {(0,1):C.GC_2894,(0,5):C.GC_2632,(0,0):C.GC_2611,(0,3):C.GC_2811,(0,4):C.GC_2637,(0,2):C.GC_2526})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS49, L.VVVVVSS51 ],
                couplings = {(0,1):C.GC_2621,(0,0):C.GC_2629})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS140, L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS167, L.VVVVVSS17, L.VVVVVSS170, L.VVVVVSS171, L.VVVVVSS183, L.VVVVVSS187, L.VVVVVSS23, L.VVVVVSS54, L.VVVVVSS69, L.VVVVVSS77, L.VVVVVSS82 ],
                couplings = {(0,9):C.GC_2875,(0,13):C.GC_2644,(0,4):C.GC_245,(0,12):C.GC_1354,(0,11):C.GC_2355,(0,10):C.GC_146,(0,5):C.GC_281,(0,6):C.GC_347,(0,2):C.GC_1273,(0,0):C.GC_1370,(0,8):C.GC_2530,(0,7):C.GC_2398,(0,3):C.GC_2365,(0,1):C.GC_2325})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS54 ],
                couplings = {(0,2):C.GC_301,(0,1):C.GC_696,(0,0):C.GC_2375})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS140, L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS167, L.VVVVVSS17, L.VVVVVSS170, L.VVVVVSS171, L.VVVVVSS183, L.VVVVVSS187, L.VVVVVSS23, L.VVVVVSS54, L.VVVVVSS69, L.VVVVVSS77, L.VVVVVSS82 ],
                couplings = {(0,9):C.GC_2876,(0,13):C.GC_2643,(0,4):C.GC_244,(0,12):C.GC_1353,(0,11):C.GC_2354,(0,10):C.GC_147,(0,5):C.GC_279,(0,6):C.GC_348,(0,2):C.GC_1274,(0,0):C.GC_1368,(0,8):C.GC_2529,(0,7):C.GC_2397,(0,3):C.GC_2363,(0,1):C.GC_2326})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS54 ],
                couplings = {(0,2):C.GC_302,(0,1):C.GC_697,(0,0):C.GC_2376})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS14, L.VVVVVSS142, L.VVVVVSS147, L.VVVVVSS148, L.VVVVVSS225, L.VVVVVSS78, L.VVVVVSS79 ],
                couplings = {(0,0):C.GC_690,(0,6):C.GC_2646,(0,1):C.GC_687,(0,3):C.GC_694,(0,4):C.GC_2570,(0,5):C.GC_686,(0,2):C.GC_621})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS147 ],
                couplings = {(0,0):C.GC_689})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS14, L.VVVVVSS142, L.VVVVVSS147, L.VVVVVSS148, L.VVVVVSS225, L.VVVVVSS70, L.VVVVVSS78, L.VVVVVSS79, L.VVVVVSS9 ],
                couplings = {(0,8):C.GC_622,(0,0):C.GC_690,(0,5):C.GC_2571,(0,7):C.GC_2646,(0,3):C.GC_623,(0,1):C.GC_687,(0,4):C.GC_2570,(0,6):C.GC_686,(0,2):C.GC_621})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS147, L.VVVVVSS148, L.VVVVVSS225, L.VVVVVSS70, L.VVVVVSS9 ],
                couplings = {(0,4):C.GC_704,(0,3):C.GC_2651,(0,1):C.GC_694,(0,2):C.GC_2647,(0,0):C.GC_689})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS105, L.VVVVVSS107, L.VVVVVSS110, L.VVVVVSS114, L.VVVVVSS115, L.VVVVVSS117, L.VVVVVSS118, L.VVVVVSS126, L.VVVVVSS127, L.VVVVVSS136, L.VVVVVSS150, L.VVVVVSS168, L.VVVVVSS5, L.VVVVVSS50, L.VVVVVSS63, L.VVVVVSS65, L.VVVVVSS66, L.VVVVVSS91 ],
                couplings = {(0,2):C.GC_699,(0,12):C.GC_1091,(0,0):C.GC_1863,(0,1):C.GC_2196,(0,13):C.GC_2841,(0,11):C.GC_2624,(0,14):C.GC_1077,(0,16):C.GC_1786,(0,15):C.GC_2143,(0,9):C.GC_625,(0,5):C.GC_1013,(0,3):C.GC_1096,(0,4):C.GC_1689,(0,7):C.GC_1889,(0,8):C.GC_2212,(0,6):C.GC_2098,(0,17):C.GC_2893,(0,10):C.GC_2799})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS115, L.VVVVVSS117, L.VVVVVSS118, L.VVVVVSS150 ],
                couplings = {(0,1):C.GC_1086,(0,0):C.GC_1839,(0,2):C.GC_2174,(0,3):C.GC_2834})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS101, L.VVVVVSS103, L.VVVVVSS109, L.VVVVVSS110, L.VVVVVSS114, L.VVVVVSS117, L.VVVVVSS119, L.VVVVVSS128, L.VVVVVSS129, L.VVVVVSS130, L.VVVVVSS133, L.VVVVVSS136, L.VVVVVSS150, L.VVVVVSS151, L.VVVVVSS168, L.VVVVVSS202, L.VVVVVSS210, L.VVVVVSS213, L.VVVVVSS5, L.VVVVVSS50, L.VVVVVSS60, L.VVVVVSS62, L.VVVVVSS63, L.VVVVVSS88, L.VVVVVSS91, L.VVVVVSS92 ],
                couplings = {(0,3):C.GC_393,(0,18):C.GC_1090,(0,2):C.GC_1449,(0,1):C.GC_1863,(0,0):C.GC_2195,(0,20):C.GC_1787,(0,25):C.GC_367,(0,23):C.GC_1432,(0,21):C.GC_2144,(0,13):C.GC_129,(0,17):C.GC_202,(0,15):C.GC_1267,(0,16):C.GC_1322,(0,19):C.GC_2338,(0,14):C.GC_2625,(0,22):C.GC_1078,(0,11):C.GC_131,(0,5):C.GC_1012,(0,4):C.GC_1097,(0,10):C.GC_1268,(0,9):C.GC_1689,(0,8):C.GC_1889,(0,7):C.GC_2213,(0,6):C.GC_2099,(0,24):C.GC_2406,(0,12):C.GC_2322})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS117, L.VVVVVSS119, L.VVVVVSS130, L.VVVVVSS150, L.VVVVVSS151, L.VVVVVSS202 ],
                couplings = {(0,4):C.GC_182,(0,5):C.GC_1307,(0,0):C.GC_1085,(0,2):C.GC_1839,(0,1):C.GC_2175,(0,3):C.GC_2332})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS105, L.VVVVVSS107, L.VVVVVSS110, L.VVVVVSS114, L.VVVVVSS115, L.VVVVVSS117, L.VVVVVSS118, L.VVVVVSS126, L.VVVVVSS127, L.VVVVVSS131, L.VVVVVSS132, L.VVVVVSS136, L.VVVVVSS150, L.VVVVVSS168, L.VVVVVSS37, L.VVVVVSS41, L.VVVVVSS42, L.VVVVVSS43, L.VVVVVSS5, L.VVVVVSS50, L.VVVVVSS63, L.VVVVVSS65, L.VVVVVSS66, L.VVVVVSS91 ],
                couplings = {(0,2):C.GC_699,(0,18):C.GC_1091,(0,0):C.GC_1863,(0,1):C.GC_2196,(0,17):C.GC_132,(0,16):C.GC_1269,(0,14):C.GC_2323,(0,15):C.GC_2566,(0,19):C.GC_2798,(0,10):C.GC_402,(0,9):C.GC_1453,(0,13):C.GC_2624,(0,20):C.GC_1077,(0,22):C.GC_1786,(0,21):C.GC_2143,(0,11):C.GC_625,(0,5):C.GC_1013,(0,3):C.GC_1014,(0,4):C.GC_1689,(0,7):C.GC_1690,(0,8):C.GC_2100,(0,6):C.GC_2098,(0,23):C.GC_2893,(0,12):C.GC_2799})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS114, L.VVVVVSS115, L.VVVVVSS117, L.VVVVVSS118, L.VVVVVSS126, L.VVVVVSS127, L.VVVVVSS150, L.VVVVVSS37, L.VVVVVSS41, L.VVVVVSS42, L.VVVVVSS43, L.VVVVVSS50 ],
                couplings = {(0,10):C.GC_409,(0,9):C.GC_1460,(0,7):C.GC_2414,(0,8):C.GC_2650,(0,11):C.GC_2899,(0,2):C.GC_1086,(0,0):C.GC_1096,(0,1):C.GC_1839,(0,4):C.GC_1889,(0,5):C.GC_2212,(0,3):C.GC_2174,(0,6):C.GC_2834})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS33, L.VVVVVSS35, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS52, L.VVVVVSS6 ],
                couplings = {(0,1):C.GC_2896,(0,5):C.GC_2634,(0,0):C.GC_2609,(0,3):C.GC_2813,(0,4):C.GC_2635,(0,2):C.GC_2528})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS49, L.VVVVVSS51 ],
                couplings = {(0,1):C.GC_2623,(0,0):C.GC_2631})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS33, L.VVVVVSS35, L.VVVVVSS49, L.VVVVVSS51, L.VVVVVSS52, L.VVVVVSS6 ],
                couplings = {(0,1):C.GC_2894,(0,5):C.GC_2632,(0,0):C.GC_2611,(0,3):C.GC_2811,(0,4):C.GC_2637,(0,2):C.GC_2526})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS49, L.VVVVVSS51 ],
                couplings = {(0,1):C.GC_2622,(0,0):C.GC_2629})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS140, L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS167, L.VVVVVSS17, L.VVVVVSS170, L.VVVVVSS171, L.VVVVVSS183, L.VVVVVSS187, L.VVVVVSS23, L.VVVVVSS54, L.VVVVVSS69, L.VVVVVSS77, L.VVVVVSS82 ],
                couplings = {(0,9):C.GC_2874,(0,13):C.GC_2645,(0,4):C.GC_246,(0,12):C.GC_1355,(0,11):C.GC_2356,(0,10):C.GC_145,(0,5):C.GC_281,(0,6):C.GC_346,(0,2):C.GC_1272,(0,0):C.GC_1370,(0,8):C.GC_2531,(0,7):C.GC_2399,(0,3):C.GC_2365,(0,1):C.GC_2324})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS54 ],
                couplings = {(0,2):C.GC_300,(0,1):C.GC_695,(0,0):C.GC_2374})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS140, L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS167, L.VVVVVSS17, L.VVVVVSS170, L.VVVVVSS171, L.VVVVVSS183, L.VVVVVSS187, L.VVVVVSS23, L.VVVVVSS54, L.VVVVVSS69, L.VVVVVSS77, L.VVVVVSS82 ],
                couplings = {(0,9):C.GC_2876,(0,13):C.GC_2643,(0,4):C.GC_244,(0,12):C.GC_1353,(0,11):C.GC_2354,(0,10):C.GC_147,(0,5):C.GC_280,(0,6):C.GC_348,(0,2):C.GC_1274,(0,0):C.GC_1369,(0,8):C.GC_2529,(0,7):C.GC_2397,(0,3):C.GC_2364,(0,1):C.GC_2326})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS143, L.VVVVVSS146, L.VVVVVSS54 ],
                couplings = {(0,2):C.GC_302,(0,1):C.GC_697,(0,0):C.GC_2376})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS112, L.VVVVVSS15, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS172, L.VVVVVSS20, L.VVVVVSS200, L.VVVVVSS22, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS235, L.VVVVVSS55, L.VVVVVSS83 ],
                couplings = {(0,12):C.GC_1929,(0,7):C.GC_1400,(0,1):C.GC_1347,(0,5):C.GC_1909,(0,11):C.GC_1674,(0,10):C.GC_1678,(0,4):C.GC_1751,(0,3):C.GC_275,(0,2):C.GC_1416,(0,9):C.GC_1009,(0,6):C.GC_1063,(0,0):C.GC_1248,(0,8):C.GC_1005})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS112, L.VVVVVSS228, L.VVVVVSS55 ],
                couplings = {(0,2):C.GC_1726,(0,0):C.GC_1381,(0,1):C.GC_1052})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS112, L.VVVVVSS15, L.VVVVVSS166, L.VVVVVSS167, L.VVVVVSS172, L.VVVVVSS20, L.VVVVVSS200, L.VVVVVSS22, L.VVVVVSS228, L.VVVVVSS229, L.VVVVVSS235, L.VVVVVSS55, L.VVVVVSS83 ],
                couplings = {(0,12):C.GC_1928,(0,7):C.GC_1399,(0,1):C.GC_1344,(0,5):C.GC_1910,(0,11):C.GC_1673,(0,10):C.GC_1677,(0,4):C.GC_1752,(0,3):C.GC_276,(0,2):C.GC_1412,(0,9):C.GC_1011,(0,6):C.GC_1065,(0,0):C.GC_1247,(0,8):C.GC_1007})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS112, L.VVVVVSS228, L.VVVVVSS55 ],
                couplings = {(0,2):C.GC_1725,(0,0):C.GC_1380,(0,1):C.GC_1054})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS137, L.VVVVVSS165, L.VVVVVSS168, L.VVVVVSS169, L.VVVVVSS196, L.VVVVVSS226, L.VVVVVSS227, L.VVVVVSS240, L.VVVVVSS38, L.VVVVVSS40, L.VVVVVSS41, L.VVVVVSS58, L.VVVVVSS97 ],
                couplings = {(0,12):C.GC_1930,(0,10):C.GC_1400,(0,8):C.GC_1348,(0,7):C.GC_1678,(0,4):C.GC_1750,(0,2):C.GC_278,(0,1):C.GC_1250,(0,3):C.GC_1415,(0,5):C.GC_1010,(0,6):C.GC_1064,(0,9):C.GC_1909,(0,11):C.GC_1674,(0,0):C.GC_1006})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS137, L.VVVVVSS165, L.VVVVVSS58 ],
                couplings = {(0,1):C.GC_1383,(0,2):C.GC_1726,(0,0):C.GC_1053})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS137, L.VVVVVSS165, L.VVVVVSS168, L.VVVVVSS169, L.VVVVVSS196, L.VVVVVSS226, L.VVVVVSS227, L.VVVVVSS240, L.VVVVVSS38, L.VVVVVSS40, L.VVVVVSS41, L.VVVVVSS58, L.VVVVVSS97 ],
                couplings = {(0,12):C.GC_1928,(0,10):C.GC_1402,(0,8):C.GC_1344,(0,7):C.GC_1679,(0,4):C.GC_1752,(0,2):C.GC_277,(0,1):C.GC_1246,(0,3):C.GC_1418,(0,5):C.GC_1008,(0,6):C.GC_1062,(0,9):C.GC_1907,(0,11):C.GC_1676,(0,0):C.GC_1007})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS137, L.VVVVVSS165, L.VVVVVSS58 ],
                couplings = {(0,1):C.GC_1379,(0,2):C.GC_1728,(0,0):C.GC_1054})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS104, L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS174, L.VVVVVSS182, L.VVVVVSS189, L.VVVVVSS59, L.VVVVVSS64, L.VVVVVSS89, L.VVVVVSS90 ],
                couplings = {(0,1):C.GC_701,(0,0):C.GC_3002,(0,12):C.GC_1790,(0,9):C.GC_2141,(0,8):C.GC_627,(0,5):C.GC_1698,(0,3):C.GC_2096,(0,6):C.GC_2210,(0,7):C.GC_2472,(0,10):C.GC_1080,(0,11):C.GC_2454,(0,2):C.GC_1020,(0,4):C.GC_2443})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS189 ],
                couplings = {(0,4):C.GC_2618,(0,3):C.GC_872,(0,1):C.GC_2172,(0,0):C.GC_570,(0,2):C.GC_2460})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS104, L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS174, L.VVVVVSS182, L.VVVVVSS189, L.VVVVVSS59, L.VVVVVSS64, L.VVVVVSS89, L.VVVVVSS90 ],
                couplings = {(0,1):C.GC_700,(0,0):C.GC_3001,(0,12):C.GC_1789,(0,9):C.GC_2140,(0,8):C.GC_626,(0,5):C.GC_1697,(0,3):C.GC_2095,(0,6):C.GC_2209,(0,7):C.GC_2473,(0,10):C.GC_1079,(0,11):C.GC_2455,(0,2):C.GC_1021,(0,4):C.GC_2442})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS189 ],
                couplings = {(0,4):C.GC_2620,(0,3):C.GC_871,(0,1):C.GC_2171,(0,0):C.GC_571,(0,2):C.GC_2459})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS104, L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS174, L.VVVVVSS182, L.VVVVVSS189, L.VVVVVSS59, L.VVVVVSS64, L.VVVVVSS89, L.VVVVVSS90 ],
                couplings = {(0,1):C.GC_702,(0,0):C.GC_3003,(0,12):C.GC_1791,(0,9):C.GC_2142,(0,8):C.GC_628,(0,5):C.GC_1699,(0,3):C.GC_2097,(0,6):C.GC_2211,(0,7):C.GC_2471,(0,10):C.GC_1081,(0,11):C.GC_2453,(0,2):C.GC_1019,(0,4):C.GC_2444})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS189 ],
                couplings = {(0,4):C.GC_2618,(0,3):C.GC_873,(0,1):C.GC_2173,(0,0):C.GC_569,(0,2):C.GC_2461})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS104, L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS174, L.VVVVVSS182, L.VVVVVSS189, L.VVVVVSS59, L.VVVVVSS64, L.VVVVVSS89, L.VVVVVSS90 ],
                couplings = {(0,1):C.GC_700,(0,0):C.GC_3001,(0,12):C.GC_1789,(0,9):C.GC_2140,(0,8):C.GC_626,(0,5):C.GC_1697,(0,3):C.GC_2095,(0,6):C.GC_2209,(0,7):C.GC_2473,(0,10):C.GC_1079,(0,11):C.GC_2455,(0,2):C.GC_1021,(0,4):C.GC_2442})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS116, L.VVVVVSS123, L.VVVVVSS149, L.VVVVVSS154, L.VVVVVSS189 ],
                couplings = {(0,4):C.GC_2619,(0,3):C.GC_871,(0,1):C.GC_2171,(0,0):C.GC_571,(0,2):C.GC_2459})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS111, L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS182, L.VVVVVSS184, L.VVVVVSS188, L.VVVVVSS189, L.VVVVVSS191, L.VVVVVSS84, L.VVVVVSS85, L.VVVVVSS89, L.VVVVVSS94 ],
                couplings = {(0,0):C.GC_2872,(0,1):C.GC_875,(0,9):C.GC_242,(0,10):C.GC_1350,(0,7):C.GC_838,(0,5):C.GC_2603,(0,8):C.GC_1263,(0,6):C.GC_1420,(0,4):C.GC_2396,(0,12):C.GC_2642,(0,11):C.GC_2353,(0,3):C.GC_2568,(0,2):C.GC_2319})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS189, L.VVVVVSS191 ],
                couplings = {(0,2):C.GC_349,(0,3):C.GC_1385,(0,1):C.GC_2592,(0,0):C.GC_2372})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS111, L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS155, L.VVVVVSS156, L.VVVVVSS182, L.VVVVVSS184, L.VVVVVSS185, L.VVVVVSS186, L.VVVVVSS188, L.VVVVVSS189, L.VVVVVSS191, L.VVVVVSS84, L.VVVVVSS85, L.VVVVVSS89, L.VVVVVSS94 ],
                couplings = {(0,0):C.GC_2873,(0,1):C.GC_876,(0,13):C.GC_242,(0,14):C.GC_1351,(0,11):C.GC_840,(0,9):C.GC_1066,(0,12):C.GC_1264,(0,10):C.GC_1419,(0,8):C.GC_1755,(0,7):C.GC_2123,(0,6):C.GC_2395,(0,4):C.GC_1015,(0,5):C.GC_1691,(0,16):C.GC_2641,(0,15):C.GC_2352,(0,3):C.GC_2101,(0,2):C.GC_2320})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS155, L.VVVVVSS156, L.VVVVVSS189, L.VVVVVSS191 ],
                couplings = {(0,4):C.GC_349,(0,5):C.GC_1386,(0,2):C.GC_1055,(0,3):C.GC_1730,(0,1):C.GC_2117,(0,0):C.GC_2373})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS102, L.VVVVVSS111, L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS182, L.VVVVVSS184, L.VVVVVSS188, L.VVVVVSS189, L.VVVVVSS190, L.VVVVVSS191, L.VVVVVSS192, L.VVVVVSS68, L.VVVVVSS72, L.VVVVVSS73, L.VVVVVSS84, L.VVVVVSS85, L.VVVVVSS89, L.VVVVVSS94 ],
                couplings = {(0,0):C.GC_2872,(0,1):C.GC_875,(0,14):C.GC_242,(0,13):C.GC_1016,(0,15):C.GC_1350,(0,11):C.GC_1694,(0,7):C.GC_839,(0,5):C.GC_2567,(0,8):C.GC_1101,(0,9):C.GC_1263,(0,6):C.GC_1266,(0,10):C.GC_1937,(0,4):C.GC_2321,(0,17):C.GC_2642,(0,12):C.GC_2103,(0,16):C.GC_2353,(0,3):C.GC_2568,(0,2):C.GC_2319})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS149, L.VVVVVSS153, L.VVVVVSS182, L.VVVVVSS184, L.VVVVVSS188, L.VVVVVSS189, L.VVVVVSS191, L.VVVVVSS68, L.VVVVVSS72, L.VVVVVSS73 ],
                couplings = {(0,9):C.GC_1104,(0,7):C.GC_1946,(0,5):C.GC_349,(0,3):C.GC_2648,(0,6):C.GC_1385,(0,4):C.GC_1420,(0,2):C.GC_2396,(0,8):C.GC_2253,(0,1):C.GC_2592,(0,0):C.GC_2372})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173, L.VVVVVSS86 ],
                couplings = {(0,1):C.GC_2848,(0,0):C.GC_2809})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173 ],
                couplings = {(0,0):C.GC_2884})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173, L.VVVVVSS86 ],
                couplings = {(0,1):C.GC_2849,(0,0):C.GC_2810})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173 ],
                couplings = {(0,0):C.GC_2885})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173, L.VVVVVSS86 ],
                couplings = {(0,1):C.GC_2847,(0,0):C.GC_2808})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173 ],
                couplings = {(0,0):C.GC_2883})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173, L.VVVVVSS86 ],
                couplings = {(0,1):C.GC_2849,(0,0):C.GC_2810})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS173 ],
                couplings = {(0,0):C.GC_2885})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS24, L.VVVVVVS28, L.VVVVVVS31, L.VVVVVVS4 ],
                couplings = {(0,1):C.GC_3447,(0,2):C.GC_3449,(0,0):C.GC_3544,(0,3):C.GC_3448})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS28, L.VVVVVVS4 ],
                couplings = {(0,0):C.GC_3477,(0,1):C.GC_3468})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS38 ],
                couplings = {(0,0):C.GC_4201})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS38 ],
                couplings = {(0,0):C.GC_4211})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS12, L.VVVVVVS2, L.VVVVVVS37, L.VVVVVVS40, L.VVVVVVS41 ],
                couplings = {(0,1):C.GC_4390,(0,0):C.GC_3310,(0,4):C.GC_3311,(0,3):C.GC_4389,(0,2):C.GC_3341})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS12, L.VVVVVVS2, L.VVVVVVS40, L.VVVVVVS41 ],
                couplings = {(0,1):C.GC_4410,(0,0):C.GC_3322,(0,3):C.GC_3316,(0,2):C.GC_3766})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS1, L.VVVVVVS23, L.VVVVVVS9 ],
                couplings = {(0,0):C.GC_4591,(0,2):C.GC_4589,(0,1):C.GC_4590})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS1, L.VVVVVVS23, L.VVVVVVS9 ],
                couplings = {(0,0):C.GC_4620,(0,2):C.GC_4617,(0,1):C.GC_4595})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS23, L.VVVVVVS31, L.VVVVVVS32, L.VVVVVVS33, L.VVVVVVS34, L.VVVVVVS44, L.VVVVVVS9 ],
                couplings = {(0,6):C.GC_4272,(0,3):C.GC_3249,(0,1):C.GC_4274,(0,2):C.GC_3253,(0,4):C.GC_3545,(0,5):C.GC_3250,(0,0):C.GC_4273})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS23, L.VVVVVVS33, L.VVVVVVS44, L.VVVVVVS9 ],
                couplings = {(0,3):C.GC_4301,(0,1):C.GC_3252,(0,2):C.GC_3251,(0,0):C.GC_4298})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS10, L.VVVVVVS39 ],
                couplings = {(0,0):C.GC_4483,(0,1):C.GC_4482})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS10, L.VVVVVVS39 ],
                couplings = {(0,0):C.GC_4526,(0,1):C.GC_4523})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS17 ],
                couplings = {(0,0):C.GC_4295})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS17 ],
                couplings = {(0,0):C.GC_4322})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS36 ],
                couplings = {(0,0):C.GC_3657})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS36 ],
                couplings = {(0,0):C.GC_4402})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS6 ],
                couplings = {(0,0):C.GC_3656})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS6 ],
                couplings = {(0,0):C.GC_4403})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS19 ],
                couplings = {(0,0):C.GC_3296})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS19 ],
                couplings = {(0,0):C.GC_4231})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS230 ],
                couplings = {(0,0):C.GC_974})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS230 ],
                couplings = {(0,0):C.GC_560})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS230 ],
                couplings = {(0,0):C.GC_972})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS230 ],
                couplings = {(0,0):C.GC_562})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS11 ],
                couplings = {(0,0):C.GC_3297})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS11 ],
                couplings = {(0,0):C.GC_4230})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_973})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_561})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_972})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_562})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS212, L.VVVVVSS28 ],
                couplings = {(0,1):C.GC_2569,(0,0):C.GC_2602})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS28 ],
                couplings = {(0,0):C.GC_2593})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS15, L.VVVVVVS21, L.VVVVVVS30, L.VVVVVVS31, L.VVVVVVS5 ],
                couplings = {(0,3):C.GC_4291,(0,2):C.GC_3149,(0,1):C.GC_3479,(0,0):C.GC_3460,(0,4):C.GC_3132})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS15, L.VVVVVVS5 ],
                couplings = {(0,0):C.GC_3469,(0,1):C.GC_3141})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS16, L.VVVVVVS25, L.VVVVVVS27, L.VVVVVVS42, L.VVVVVVS45 ],
                couplings = {(0,2):C.GC_4290,(0,4):C.GC_3148,(0,0):C.GC_3461,(0,3):C.GC_3478,(0,1):C.GC_3133})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS16, L.VVVVVVS25 ],
                couplings = {(0,0):C.GC_3470,(0,1):C.GC_3142})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS212, L.VVVVVSS221, L.VVVVVSS28 ],
                couplings = {(0,2):C.GC_800,(0,1):C.GC_997,(0,0):C.GC_862})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS28 ],
                couplings = {(0,0):C.GC_861})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS3 ],
                couplings = {(0,0):C.GC_3459})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS3 ],
                couplings = {(0,0):C.GC_4302})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS26 ],
                couplings = {(0,0):C.GC_3458})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS26 ],
                couplings = {(0,0):C.GC_4303})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS201, L.VVVVVSS45 ],
                couplings = {(0,1):C.GC_624,(0,0):C.GC_673})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS45 ],
                couplings = {(0,0):C.GC_669})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS18, L.VVVVVVS20, L.VVVVVVS43, L.VVVVVVS46, L.VVVVVVS8 ],
                couplings = {(0,1):C.GC_4385,(0,3):C.GC_3323,(0,4):C.GC_3657,(0,2):C.GC_3675,(0,0):C.GC_3313})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS18, L.VVVVVVS8 ],
                couplings = {(0,1):C.GC_3667,(0,0):C.GC_3318})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS22, L.VVVVVVS29, L.VVVVVVS31, L.VVVVVVS7 ],
                couplings = {(0,3):C.GC_4386,(0,1):C.GC_3324,(0,2):C.GC_3676,(0,4):C.GC_3656,(0,0):C.GC_3312})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS13, L.VVVVVVS7 ],
                couplings = {(0,1):C.GC_3666,(0,0):C.GC_3317})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_837})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS113 ],
                couplings = {(0,0):C.GC_863})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS14 ],
                couplings = {(0,0):C.GC_3460})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS14 ],
                couplings = {(0,0):C.GC_4305})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS35 ],
                couplings = {(0,0):C.GC_3461})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVS35 ],
                couplings = {(0,0):C.GC_4304})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVSS226 ],
                couplings = {(0,0):C.GC_1228})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV2, L.VVVVVVV23, L.VVVVVVV29, L.VVVVVVV3, L.VVVVVVV9 ],
                couplings = {(0,4):C.GC_519,(0,0):C.GC_509,(0,3):C.GC_133,(0,2):C.GC_476,(0,1):C.GC_134})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV23, L.VVVVVVV3 ],
                couplings = {(0,1):C.GC_465,(0,0):C.GC_488})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV15, L.VVVVVVV16, L.VVVVVVV20, L.VVVVVVV6, L.VVVVVVV8 ],
                couplings = {(0,3):C.GC_1547,(0,0):C.GC_1245,(0,1):C.GC_1530,(0,4):C.GC_1543,(0,2):C.GC_1244})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV15, L.VVVVVVV20 ],
                couplings = {(0,0):C.GC_783,(0,1):C.GC_1523})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV13, L.VVVVVVV18, L.VVVVVVV24, L.VVVVVVV25, L.VVVVVVV5 ],
                couplings = {(0,0):C.GC_2028,(0,4):C.GC_2022,(0,2):C.GC_1696,(0,3):C.GC_2000,(0,1):C.GC_1695})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV18, L.VVVVVVV24 ],
                couplings = {(0,1):C.GC_943,(0,0):C.GC_1993})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV1, L.VVVVVVV10, L.VVVVVVV22, L.VVVVVVV28, L.VVVVVVV30 ],
                couplings = {(0,0):C.GC_1146,(0,1):C.GC_1148,(0,3):C.GC_1000,(0,4):C.GC_1142,(0,2):C.GC_1001})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV22, L.VVVVVVV28 ],
                couplings = {(0,1):C.GC_1138,(0,0):C.GC_582})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV11, L.VVVVVVV12, L.VVVVVVV14, L.VVVVVVV17, L.VVVVVVV19 ],
                couplings = {(0,2):C.GC_1548,(0,0):C.GC_1544,(0,1):C.GC_1270,(0,3):C.GC_1271,(0,4):C.GC_1531})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV12, L.VVVVVVV17 ],
                couplings = {(0,0):C.GC_1524,(0,1):C.GC_784})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV21, L.VVVVVVV26, L.VVVVVVV27, L.VVVVVVV4, L.VVVVVVV7 ],
                couplings = {(0,4):C.GC_1149,(0,1):C.GC_1018,(0,2):C.GC_1143,(0,3):C.GC_1147,(0,0):C.GC_1017})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVV21, L.VVVVVVV26 ],
                couplings = {(0,1):C.GC_583,(0,0):C.GC_1139})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_164})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.a, P.a, P.a, P.a, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_459})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_846})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_929})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_845})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_928})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS3, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1281,(0,1):C.GC_1285})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS3, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_751,(0,1):C.GC_1484})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1282,(0,1):C.GC_1282,(0,2):C.GC_1286})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_754,(0,1):C.GC_754,(0,2):C.GC_1485})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1280,(0,1):C.GC_1280,(0,2):C.GC_1284})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_750,(0,1):C.GC_750,(0,2):C.GC_1483})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_846,(0,1):C.GC_846,(0,2):C.GC_846})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_929,(0,1):C.GC_929,(0,2):C.GC_929})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_847,(0,1):C.GC_847,(0,2):C.GC_847})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.a, P.a, P.a, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_930,(0,1):C.GC_930,(0,2):C.GC_930})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_636,(0,1):C.GC_636,(0,2):C.GC_1281})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_748,(0,1):C.GC_748,(0,2):C.GC_751})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_636,(0,1):C.GC_636,(0,2):C.GC_1281})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_748,(0,1):C.GC_748,(0,2):C.GC_751})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_638,(0,1):C.GC_638,(0,2):C.GC_1502})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_753,(0,1):C.GC_753})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1037,(0,1):C.GC_1029,(0,2):C.GC_1029})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1118,(0,1):C.GC_579,(0,2):C.GC_579})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1035,(0,1):C.GC_1027,(0,2):C.GC_1027})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1116,(0,1):C.GC_577,(0,2):C.GC_577})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1036,(0,1):C.GC_1028,(0,2):C.GC_1028})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1117,(0,1):C.GC_578,(0,2):C.GC_578})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1034,(0,1):C.GC_1026,(0,2):C.GC_1026})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1115,(0,1):C.GC_576,(0,2):C.GC_576})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1030,(0,1):C.GC_1036,(0,2):C.GC_1036})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1136,(0,1):C.GC_573,(0,2):C.GC_573})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1025,(0,1):C.GC_1035,(0,2):C.GC_1035})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1135,(0,1):C.GC_572,(0,2):C.GC_572})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1036,(0,1):C.GC_1036,(0,2):C.GC_1030})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_573,(0,1):C.GC_573,(0,2):C.GC_1136})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1038,(0,1):C.GC_1038,(0,2):C.GC_1033})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_574,(0,1):C.GC_574,(0,2):C.GC_1137})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_951,(0,1):C.GC_951,(0,2):C.GC_949})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_542,(0,1):C.GC_542,(0,2):C.GC_967})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_951,(0,1):C.GC_951,(0,2):C.GC_949})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_542,(0,1):C.GC_542,(0,2):C.GC_967})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1281,(0,1):C.GC_1281,(0,2):C.GC_1285})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_751,(0,1):C.GC_751,(0,2):C.GC_1484})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1279,(0,1):C.GC_1279,(0,2):C.GC_1283})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_746,(0,1):C.GC_746,(0,2):C.GC_1482})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1280,(0,1):C.GC_1280,(0,2):C.GC_1284})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.a, P.a, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_750,(0,1):C.GC_750,(0,2):C.GC_1483})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1029,(0,1):C.GC_1029,(0,2):C.GC_1037})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_579,(0,1):C.GC_579,(0,2):C.GC_1118})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1031,(0,1):C.GC_1031,(0,2):C.GC_1038})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_580,(0,1):C.GC_580,(0,2):C.GC_1119})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1028,(0,1):C.GC_1028,(0,2):C.GC_1036})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_578,(0,1):C.GC_578,(0,2):C.GC_1117})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_1032,(0,1):C.GC_1032,(0,2):C.GC_1039})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_581,(0,1):C.GC_581,(0,2):C.GC_1120})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_950,(0,1):C.GC_950,(0,2):C.GC_954})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_545,(0,1):C.GC_545,(0,2):C.GC_966})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_949,(0,1):C.GC_949,(0,2):C.GC_953})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_544,(0,1):C.GC_544,(0,2):C.GC_965})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_948,(0,1):C.GC_948,(0,2):C.GC_952})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_543,(0,1):C.GC_543,(0,2):C.GC_964})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_528,(0,1):C.GC_528,(0,2):C.GC_954})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_545,(0,1):C.GC_545,(0,2):C.GC_966})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2589,(0,1):C.GC_2589,(0,2):C.GC_2589})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.a, P.a, P.a, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2742,(0,1):C.GC_2742,(0,2):C.GC_2742})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_661,(0,1):C.GC_661,(0,2):C.GC_662})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_775,(0,1):C.GC_775,(0,2):C.GC_776})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_660,(0,1):C.GC_660,(0,2):C.GC_659})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.a, P.a, P.W__minus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_774,(0,1):C.GC_774,(0,2):C.GC_773})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_856,(0,1):C.GC_853,(0,2):C.GC_853})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_937,(0,1):C.GC_935,(0,2):C.GC_935})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_851,(0,1):C.GC_852,(0,2):C.GC_852})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_931,(0,1):C.GC_932,(0,2):C.GC_932})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_858,(0,1):C.GC_855,(0,2):C.GC_855})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_939,(0,1):C.GC_936,(0,2):C.GC_936})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_661,(0,1):C.GC_661,(0,2):C.GC_662})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_775,(0,1):C.GC_775,(0,2):C.GC_776})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_663,(0,1):C.GC_663,(0,2):C.GC_664})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.a, P.a, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_777,(0,1):C.GC_777,(0,2):C.GC_778})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_888,(0,1):C.GC_857,(0,2):C.GC_857})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_938,(0,1):C.GC_938})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_853,(0,1):C.GC_854,(0,2):C.GC_854})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_934,(0,1):C.GC_933,(0,2):C.GC_933})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_853,(0,1):C.GC_854,(0,2):C.GC_854})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_934,(0,1):C.GC_933,(0,2):C.GC_933})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_647,(0,1):C.GC_647,(0,2):C.GC_649})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_764,(0,1):C.GC_764,(0,2):C.GC_766})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_646,(0,1):C.GC_646,(0,2):C.GC_648})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_763,(0,1):C.GC_763,(0,2):C.GC_765})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_650,(0,1):C.GC_650,(0,2):C.GC_651})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_767,(0,1):C.GC_767,(0,2):C.GC_768})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_651,(0,1):C.GC_651,(0,2):C.GC_653})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_769,(0,1):C.GC_769,(0,2):C.GC_771})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_645,(0,1):C.GC_645,(0,2):C.GC_646})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_761,(0,1):C.GC_761,(0,2):C.GC_762})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_652,(0,1):C.GC_652,(0,2):C.GC_654})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_770,(0,1):C.GC_770,(0,2):C.GC_772})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_856,(0,1):C.GC_853,(0,2):C.GC_853})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_937,(0,1):C.GC_935,(0,2):C.GC_935})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_860,(0,1):C.GC_859,(0,2):C.GC_859})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_941,(0,1):C.GC_940,(0,2):C.GC_940})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_858,(0,1):C.GC_855,(0,2):C.GC_855})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.a, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_939,(0,1):C.GC_936,(0,2):C.GC_936})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_649,(0,1):C.GC_647,(0,2):C.GC_647})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_766,(0,1):C.GC_764,(0,2):C.GC_764})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_648,(0,1):C.GC_646,(0,2):C.GC_646})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_765,(0,1):C.GC_763,(0,2):C.GC_763})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_643,(0,1):C.GC_644,(0,2):C.GC_644})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_758,(0,1):C.GC_760,(0,2):C.GC_760})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_641,(0,1):C.GC_643,(0,2):C.GC_643})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_756,(0,1):C.GC_759,(0,2):C.GC_759})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_646,(0,1):C.GC_645,(0,2):C.GC_645})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_762,(0,1):C.GC_761,(0,2):C.GC_761})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_640,(0,1):C.GC_642,(0,2):C.GC_642})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_755,(0,1):C.GC_757,(0,2):C.GC_757})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2827,(0,1):C.GC_2827,(0,2):C.GC_2827})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2934,(0,1):C.GC_2934,(0,2):C.GC_2934})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2580,(0,1):C.GC_2580,(0,2):C.GC_2737})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2736,(0,1):C.GC_2736,(0,2):C.GC_2581})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2575,(0,1):C.GC_2575,(0,2):C.GC_2730})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2731,(0,1):C.GC_2731,(0,2):C.GC_2574})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_532,(0,1):C.GC_532,(0,2):C.GC_536})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_549,(0,1):C.GC_549,(0,2):C.GC_551})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_531,(0,1):C.GC_531,(0,2):C.GC_538})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_553,(0,1):C.GC_553,(0,2):C.GC_546})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_534,(0,1):C.GC_534,(0,2):C.GC_535})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.W__minus__, P.W__minus__, P.Z, P.Z, P.G__plus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_548,(0,1):C.GC_548,(0,2):C.GC_552})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2580,(0,1):C.GC_2580,(0,2):C.GC_2737})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2736,(0,1):C.GC_2736,(0,2):C.GC_2581})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2584,(0,1):C.GC_2584,(0,2):C.GC_2741})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2740,(0,1):C.GC_2740,(0,2):C.GC_2585})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_533,(0,1):C.GC_533,(0,2):C.GC_532})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_541,(0,1):C.GC_541,(0,2):C.GC_550})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_533,(0,1):C.GC_533,(0,2):C.GC_532})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_541,(0,1):C.GC_541,(0,2):C.GC_550})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_532,(0,1):C.GC_532,(0,2):C.GC_536})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_549,(0,1):C.GC_549,(0,2):C.GC_551})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_537,(0,1):C.GC_537,(0,2):C.GC_530})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_547,(0,1):C.GC_547,(0,2):C.GC_554})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_534,(0,1):C.GC_534,(0,2):C.GC_535})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_548,(0,1):C.GC_548,(0,2):C.GC_552})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2826,(0,1):C.GC_2826,(0,2):C.GC_2911})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.a, P.a, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2933,(0,1):C.GC_2933})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2826,(0,1):C.GC_2826,(0,2):C.GC_2911})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.a, P.a, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2933,(0,1):C.GC_2933})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2579,(0,1):C.GC_2579,(0,2):C.GC_2680})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2735,(0,1):C.GC_2735})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2577,(0,1):C.GC_2577,(0,2):C.GC_2678})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2733,(0,1):C.GC_2733})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2578,(0,1):C.GC_2578,(0,2):C.GC_2679})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2734,(0,1):C.GC_2734})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2576,(0,1):C.GC_2576,(0,2):C.GC_2677})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.a, P.W__minus__, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2732,(0,1):C.GC_2732})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2579,(0,1):C.GC_2579,(0,2):C.GC_2680})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2735,(0,1):C.GC_2735})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2582,(0,1):C.GC_2582,(0,2):C.GC_2681})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2738,(0,1):C.GC_2738})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2578,(0,1):C.GC_2578,(0,2):C.GC_2679})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2734,(0,1):C.GC_2734})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2583,(0,1):C.GC_2583,(0,2):C.GC_2682})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.a, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_2739,(0,1):C.GC_2739})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_637,(0,1):C.GC_637,(0,2):C.GC_719})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_752,(0,1):C.GC_752})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_635,(0,1):C.GC_635,(0,2):C.GC_718})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_749,(0,1):C.GC_749})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_634,(0,1):C.GC_634,(0,2):C.GC_717})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
                couplings = {(0,0):C.GC_747,(0,1):C.GC_747})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_637,(0,1):C.GC_637,(0,2):C.GC_639})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_752,(0,1):C.GC_752,(0,2):C.GC_719})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_2980,(0,1):C.GC_2980,(0,2):C.GC_2980})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2, L.VVVVSSSS4 ],
                couplings = {(0,0):C.GC_3020,(0,1):C.GC_3020,(0,2):C.GC_3020})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2981})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3021})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2980})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.a, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3020})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2819})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2929})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2818})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2928})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2820})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2930})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2821})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2931})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2817})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2927})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2822})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.W__minus__, P.Z, P.Z, P.Z, P.G__plus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2932})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2819})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2929})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2818})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2928})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2816})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2926})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2815})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2925})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2817})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2927})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2814})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_2924})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3051})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3074})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3048})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3071})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3050})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3073})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3049})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G0, P.G0, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3072})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3048})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3071})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3052})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVSSSS5 ],
                couplings = {(0,0):C.GC_3074})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS26, L.VVVVVVSS30, L.VVVVVVSS33, L.VVVVVVSS5 ],
                couplings = {(0,1):C.GC_1275,(0,2):C.GC_1277,(0,0):C.GC_1454,(0,3):C.GC_1276})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS30, L.VVVVVVSS5 ],
                couplings = {(0,0):C.GC_1323,(0,1):C.GC_1308})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_527})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_540})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS2, L.VVVVVVSS39, L.VVVVVVSS43, L.VVVVVVSS44 ],
                couplings = {(0,1):C.GC_850,(0,0):C.GC_1040,(0,4):C.GC_1041,(0,3):C.GC_849,(0,2):C.GC_1102})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS2, L.VVVVVVSS43, L.VVVVVVSS44 ],
                couplings = {(0,1):C.GC_877,(0,0):C.GC_1067,(0,3):C.GC_1056,(0,2):C.GC_1938})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS1, L.VVVVVVSS10, L.VVVVVVSS25 ],
                couplings = {(0,0):C.GC_2825,(0,1):C.GC_2823,(0,2):C.GC_2824})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS1, L.VVVVVVSS10, L.VVVVVVSS25 ],
                couplings = {(0,0):C.GC_2903,(0,1):C.GC_2900,(0,2):C.GC_2835})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25, L.VVVVVVSS33, L.VVVVVVSS34, L.VVVVVVSS35, L.VVVVVVSS36, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_629,(0,4):C.GC_955,(0,2):C.GC_633,(0,3):C.GC_963,(0,5):C.GC_1455,(0,6):C.GC_956,(0,1):C.GC_631})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25, L.VVVVVVSS35, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_676,(0,2):C.GC_962,(0,3):C.GC_961,(0,1):C.GC_671})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS42 ],
                couplings = {(0,0):C.GC_2588,(0,1):C.GC_2587})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS11, L.VVVVVVSS42 ],
                couplings = {(0,0):C.GC_2652,(0,1):C.GC_2649})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_666})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_703})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18 ],
                couplings = {(0,0):C.GC_148})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS18 ],
                couplings = {(0,0):C.GC_213})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS38 ],
                couplings = {(0,0):C.GC_1701})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS38 ],
                couplings = {(0,0):C.GC_865})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS38 ],
                couplings = {(0,0):C.GC_1702})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS38 ],
                couplings = {(0,0):C.GC_864})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS7 ],
                couplings = {(0,0):C.GC_1701})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS7 ],
                couplings = {(0,0):C.GC_865})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS7 ],
                couplings = {(0,0):C.GC_1700})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS7 ],
                couplings = {(0,0):C.GC_866})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS30, L.VVVVVVSS33, L.VVVVVVSS5 ],
                couplings = {(0,1):C.GC_1277,(0,0):C.GC_1323,(0,2):C.GC_1276})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS5 ],
                couplings = {(0,0):C.GC_1308})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS33, L.VVVVVVSS41, L.VVVVVVSS60 ],
                couplings = {(0,0):C.GC_1278,(0,1):C.GC_1324,(0,2):C.GC_1276})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS60 ],
                couplings = {(0,0):C.GC_1308})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS21 ],
                couplings = {(0,0):C.GC_1023})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS21 ],
                couplings = {(0,0):C.GC_564})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS21 ],
                couplings = {(0,0):C.GC_1022})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS21 ],
                couplings = {(0,0):C.GC_565})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1023})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_564})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_1024})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS12 ],
                couplings = {(0,0):C.GC_563})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_947})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_539})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_947})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS40 ],
                couplings = {(0,0):C.GC_539})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4, L.VVVVVVSS58 ],
                couplings = {(0,1):C.GC_1704,(0,0):C.GC_2104})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4, L.VVVVVVSS58 ],
                couplings = {(0,1):C.GC_868,(0,0):C.GC_2604})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS23, L.VVVVVVSS32, L.VVVVVVSS33, L.VVVVVVSS6 ],
                couplings = {(0,3):C.GC_656,(0,2):C.GC_210,(0,1):C.GC_1326,(0,0):C.GC_1293,(0,4):C.GC_153})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS6 ],
                couplings = {(0,0):C.GC_1310,(0,1):C.GC_189})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS23, L.VVVVVVSS32, L.VVVVVVSS33, L.VVVVVVSS6 ],
                couplings = {(0,3):C.GC_658,(0,2):C.GC_212,(0,1):C.GC_1328,(0,0):C.GC_1292,(0,4):C.GC_152})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS16, L.VVVVVVSS6 ],
                couplings = {(0,0):C.GC_1309,(0,1):C.GC_188})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17, L.VVVVVVSS27, L.VVVVVVSS29, L.VVVVVVSS49, L.VVVVVVSS57 ],
                couplings = {(0,2):C.GC_655,(0,4):C.GC_209,(0,0):C.GC_1293,(0,3):C.GC_1327,(0,1):C.GC_153})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17, L.VVVVVVSS27 ],
                couplings = {(0,0):C.GC_1310,(0,1):C.GC_189})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17, L.VVVVVVSS27, L.VVVVVVSS29, L.VVVVVVSS49, L.VVVVVVSS57 ],
                couplings = {(0,2):C.GC_657,(0,4):C.GC_211,(0,0):C.GC_1294,(0,3):C.GC_1325,(0,1):C.GC_154})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS17, L.VVVVVVSS27 ],
                couplings = {(0,0):C.GC_1311,(0,1):C.GC_190})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS3, L.VVVVVVSS43, L.VVVVVVSS45, L.VVVVVVSS48, L.VVVVVVSS53 ],
                couplings = {(0,2):C.GC_1042,(0,1):C.GC_848,(0,3):C.GC_1067,(0,0):C.GC_1703,(0,4):C.GC_1760})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS3, L.VVVVVVSS45 ],
                couplings = {(0,1):C.GC_1057,(0,0):C.GC_1735})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4 ],
                couplings = {(0,0):C.GC_1290})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4 ],
                couplings = {(0,0):C.GC_678})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4 ],
                couplings = {(0,0):C.GC_1291})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS4 ],
                couplings = {(0,0):C.GC_677})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS28 ],
                couplings = {(0,0):C.GC_1290})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS28 ],
                couplings = {(0,0):C.GC_678})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS28 ],
                couplings = {(0,0):C.GC_1289})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS28 ],
                couplings = {(0,0):C.GC_679})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25 ],
                couplings = {(0,0):C.GC_2842,(0,1):C.GC_2824})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS25 ],
                couplings = {(0,0):C.GC_2835})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25, L.VVVVVVSS46, L.VVVVVVSS51, L.VVVVVVSS54, L.VVVVVVSS55 ],
                couplings = {(0,2):C.GC_149,(0,5):C.GC_208,(0,4):C.GC_1295,(0,3):C.GC_1329,(0,0):C.GC_2339,(0,1):C.GC_2327})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS25, L.VVVVVVSS46, L.VVVVVVSS54 ],
                couplings = {(0,1):C.GC_187,(0,2):C.GC_1312,(0,0):C.GC_2333})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25, L.VVVVVVSS33, L.VVVVVVSS35, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_675,(0,2):C.GC_633,(0,3):C.GC_962,(0,4):C.GC_956,(0,1):C.GC_631})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS25, L.VVVVVVSS56 ],
                couplings = {(0,1):C.GC_961,(0,0):C.GC_671})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS10, L.VVVVVVSS25, L.VVVVVVSS33, L.VVVVVVSS35, L.VVVVVVSS56 ],
                couplings = {(0,0):C.GC_674,(0,2):C.GC_632,(0,3):C.GC_962,(0,4):C.GC_956,(0,1):C.GC_630})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS25, L.VVVVVVSS56 ],
                couplings = {(0,1):C.GC_961,(0,0):C.GC_670})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS13, L.VVVVVVSS43, L.VVVVVVSS44 ],
                couplings = {(0,2):C.GC_1041,(0,1):C.GC_849,(0,0):C.GC_1067})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS44 ],
                couplings = {(0,0):C.GC_1056})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20, L.VVVVVVSS22, L.VVVVVVSS50, L.VVVVVVSS59, L.VVVVVVSS9 ],
                couplings = {(0,1):C.GC_841,(0,3):C.GC_1068,(0,4):C.GC_1701,(0,2):C.GC_1758,(0,0):C.GC_1046})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20, L.VVVVVVSS9 ],
                couplings = {(0,1):C.GC_1733,(0,0):C.GC_1059})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20, L.VVVVVVSS22, L.VVVVVVSS50, L.VVVVVVSS59, L.VVVVVVSS9 ],
                couplings = {(0,1):C.GC_843,(0,3):C.GC_1070,(0,4):C.GC_1702,(0,2):C.GC_1756,(0,0):C.GC_1047})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS20, L.VVVVVVSS9 ],
                couplings = {(0,1):C.GC_1734,(0,0):C.GC_1060})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS24, L.VVVVVVSS31, L.VVVVVVSS33, L.VVVVVVSS8 ],
                couplings = {(0,3):C.GC_842,(0,1):C.GC_1069,(0,2):C.GC_1757,(0,4):C.GC_1701,(0,0):C.GC_1046})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS8 ],
                couplings = {(0,1):C.GC_1733,(0,0):C.GC_1059})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS24, L.VVVVVVSS31, L.VVVVVVSS33, L.VVVVVVSS8 ],
                couplings = {(0,3):C.GC_844,(0,1):C.GC_1071,(0,2):C.GC_1759,(0,4):C.GC_1700,(0,0):C.GC_1045})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS14, L.VVVVVVSS8 ],
                couplings = {(0,1):C.GC_1732,(0,0):C.GC_1058})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS42 ],
                couplings = {(0,0):C.GC_2586})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS42 ],
                couplings = {(0,0):C.GC_2605})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS42, L.VVVVVVSS47, L.VVVVVVSS52 ],
                couplings = {(0,1):C.GC_1048,(0,2):C.GC_1705,(0,0):C.GC_2104})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS42, L.VVVVVVSS47, L.VVVVVVSS52 ],
                couplings = {(0,1):C.GC_566,(0,2):C.GC_867,(0,0):C.GC_2604})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15 ],
                couplings = {(0,0):C.GC_1293})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15 ],
                couplings = {(0,0):C.GC_681})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15 ],
                couplings = {(0,0):C.GC_1292})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS15 ],
                couplings = {(0,0):C.GC_682})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS37 ],
                couplings = {(0,0):C.GC_1293})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS37 ],
                couplings = {(0,0):C.GC_681})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS37 ],
                couplings = {(0,0):C.GC_1294})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS37 ],
                couplings = {(0,0):C.GC_680})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_665})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_684})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_667})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVSS19 ],
                couplings = {(0,0):C.GC_683})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV17, L.VVVVVVVV2, L.VVVVVVVV24 ],
                couplings = {(0,1):C.GC_150,(0,2):C.GC_151,(0,0):C.GC_477})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV2, L.VVVVVVVV24 ],
                couplings = {(0,0):C.GC_466,(0,1):C.GC_489})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV16, L.VVVVVVVV22, L.VVVVVVVV4 ],
                couplings = {(0,2):C.GC_1288,(0,0):C.GC_1532,(0,1):C.GC_1287})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV22, L.VVVVVVVV4 ],
                couplings = {(0,1):C.GC_785,(0,0):C.GC_1525})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV21 ],
                couplings = {(0,0):C.GC_529})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV21 ],
                couplings = {(0,0):C.GC_555})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV12, L.VVVVVVVV14, L.VVVVVVVV7 ],
                couplings = {(0,2):C.GC_1707,(0,1):C.GC_2001,(0,0):C.GC_1706})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV12, L.VVVVVVVV7 ],
                couplings = {(0,1):C.GC_944,(0,0):C.GC_1994})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV10, L.VVVVVVVV18, L.VVVVVVVV6 ],
                couplings = {(0,2):C.GC_1043,(0,0):C.GC_1144,(0,1):C.GC_1044})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV18, L.VVVVVVVV6 ],
                couplings = {(0,1):C.GC_1140,(0,0):C.GC_584})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV15, L.VVVVVVVV3, L.VVVVVVVV9 ],
                couplings = {(0,1):C.GC_1296,(0,0):C.GC_1297,(0,2):C.GC_1533})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV15, L.VVVVVVVV3 ],
                couplings = {(0,1):C.GC_1526,(0,0):C.GC_786})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV1, L.VVVVVVVV19, L.VVVVVVVV25 ],
                couplings = {(0,0):C.GC_958,(0,1):C.GC_970,(0,2):C.GC_957})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV1, L.VVVVVVVV25 ],
                couplings = {(0,0):C.GC_556,(0,1):C.GC_968})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV11, L.VVVVVVVV13, L.VVVVVVVV8 ],
                couplings = {(0,2):C.GC_1050,(0,1):C.GC_1145,(0,0):C.GC_1049})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV11, L.VVVVVVVV8 ],
                couplings = {(0,1):C.GC_585,(0,0):C.GC_1141})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV20, L.VVVVVVVV23, L.VVVVVVVV5 ],
                couplings = {(0,2):C.GC_959,(0,1):C.GC_960,(0,0):C.GC_971})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVVVVVV23, L.VVVVVVVV5 ],
                couplings = {(0,1):C.GC_969,(0,0):C.GC_557})

