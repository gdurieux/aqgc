# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (November 18, 2022)
# Date: Mon 13 Jan 2025 13:32:37



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
FS0 = Parameter(name = 'FS0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FS0}',
                lhablock = 'aqgc',
                lhacode = [ 1 ])

FS1 = Parameter(name = 'FS1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FS1}',
                lhablock = 'aqgc',
                lhacode = [ 2 ])

FS2 = Parameter(name = 'FS2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FS2}',
                lhablock = 'aqgc',
                lhacode = [ 3 ])

FM0 = Parameter(name = 'FM0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM0}',
                lhablock = 'aqgc',
                lhacode = [ 4 ])

FM1 = Parameter(name = 'FM1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM1}',
                lhablock = 'aqgc',
                lhacode = [ 5 ])

FM2 = Parameter(name = 'FM2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM2}',
                lhablock = 'aqgc',
                lhacode = [ 6 ])

FM3 = Parameter(name = 'FM3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM3}',
                lhablock = 'aqgc',
                lhacode = [ 7 ])

FM4 = Parameter(name = 'FM4',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM4}',
                lhablock = 'aqgc',
                lhacode = [ 8 ])

FM5 = Parameter(name = 'FM5',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM5}',
                lhablock = 'aqgc',
                lhacode = [ 9 ])

FM7 = Parameter(name = 'FM7',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM7}',
                lhablock = 'aqgc',
                lhacode = [ 10 ])

FM8 = Parameter(name = 'FM8',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM8}',
                lhablock = 'aqgc',
                lhacode = [ 11 ])

FM9 = Parameter(name = 'FM9',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FM9}',
                lhablock = 'aqgc',
                lhacode = [ 12 ])

FT0 = Parameter(name = 'FT0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT0}',
                lhablock = 'aqgc',
                lhacode = [ 13 ])

FT1 = Parameter(name = 'FT1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT1}',
                lhablock = 'aqgc',
                lhacode = [ 14 ])

FT2 = Parameter(name = 'FT2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT2}',
                lhablock = 'aqgc',
                lhacode = [ 15 ])

FT3 = Parameter(name = 'FT3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT3}',
                lhablock = 'aqgc',
                lhacode = [ 16 ])

FT4 = Parameter(name = 'FT4',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT4}',
                lhablock = 'aqgc',
                lhacode = [ 17 ])

FT5 = Parameter(name = 'FT5',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT5}',
                lhablock = 'aqgc',
                lhacode = [ 18 ])

FT6 = Parameter(name = 'FT6',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT6}',
                lhablock = 'aqgc',
                lhacode = [ 19 ])

FT7 = Parameter(name = 'FT7',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT7}',
                lhablock = 'aqgc',
                lhacode = [ 20 ])

FT8 = Parameter(name = 'FT8',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT8}',
                lhablock = 'aqgc',
                lhacode = [ 21 ])

FT9 = Parameter(name = 'FT9',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{FT9}',
                lhablock = 'aqgc',
                lhacode = [ 22 ])

FM1odd = Parameter(name = 'FM1odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM1odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 23 ])

FM2odd = Parameter(name = 'FM2odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM2odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 24 ])

FM3odd = Parameter(name = 'FM3odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM3odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 25 ])

FM4odd = Parameter(name = 'FM4odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM4odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 26 ])

FM5odd = Parameter(name = 'FM5odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM5odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 27 ])

FM6odd = Parameter(name = 'FM6odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FM6odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 28 ])

FT1odd = Parameter(name = 'FT1odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT1odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 29 ])

FT2odd = Parameter(name = 'FT2odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT2odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 30 ])

FT3odd = Parameter(name = 'FT3odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT3odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 31 ])

FT4odd = Parameter(name = 'FT4odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT4odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 32 ])

FT5odd = Parameter(name = 'FT5odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT5odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 33 ])

FT6odd = Parameter(name = 'FT6odd',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{FT6odd}',
                   lhablock = 'aqgc',
                   lhacode = [ 34 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

cS1 = Parameter(name = 'cS1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cS1}',
                lhablock = 'aqgc_bis',
                lhacode = [ 1 ])

cS2 = Parameter(name = 'cS2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cS2}',
                lhablock = 'aqgc_bis',
                lhacode = [ 2 ])

cS3 = Parameter(name = 'cS3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cS3}',
                lhablock = 'aqgc_bis',
                lhacode = [ 3 ])

cM1 = Parameter(name = 'cM1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM1}',
                lhablock = 'aqgc_bis',
                lhacode = [ 4 ])

cM2 = Parameter(name = 'cM2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM2}',
                lhablock = 'aqgc_bis',
                lhacode = [ 5 ])

cM3 = Parameter(name = 'cM3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM3}',
                lhablock = 'aqgc_bis',
                lhacode = [ 6 ])

cM4 = Parameter(name = 'cM4',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM4}',
                lhablock = 'aqgc_bis',
                lhacode = [ 7 ])

cM5 = Parameter(name = 'cM5',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM5}',
                lhablock = 'aqgc_bis',
                lhacode = [ 8 ])

cM6 = Parameter(name = 'cM6',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM6}',
                lhablock = 'aqgc_bis',
                lhacode = [ 9 ])

cM7 = Parameter(name = 'cM7',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM7}',
                lhablock = 'aqgc_bis',
                lhacode = [ 10 ])

cM8 = Parameter(name = 'cM8',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM8}',
                lhablock = 'aqgc_bis',
                lhacode = [ 11 ])

cM9 = Parameter(name = 'cM9',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cM9}',
                lhablock = 'aqgc_bis',
                lhacode = [ 12 ])

cT1 = Parameter(name = 'cT1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT1}',
                lhablock = 'aqgc_bis',
                lhacode = [ 13 ])

cT2 = Parameter(name = 'cT2',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT2}',
                lhablock = 'aqgc_bis',
                lhacode = [ 14 ])

cT3 = Parameter(name = 'cT3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT3}',
                lhablock = 'aqgc_bis',
                lhacode = [ 15 ])

cT4 = Parameter(name = 'cT4',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT4}',
                lhablock = 'aqgc_bis',
                lhacode = [ 16 ])

cT5 = Parameter(name = 'cT5',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT5}',
                lhablock = 'aqgc_bis',
                lhacode = [ 17 ])

cT6 = Parameter(name = 'cT6',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT6}',
                lhablock = 'aqgc_bis',
                lhacode = [ 18 ])

cT7 = Parameter(name = 'cT7',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT7}',
                lhablock = 'aqgc_bis',
                lhacode = [ 19 ])

cT8 = Parameter(name = 'cT8',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT8}',
                lhablock = 'aqgc_bis',
                lhacode = [ 20 ])

cT9 = Parameter(name = 'cT9',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cT9}',
                lhablock = 'aqgc_bis',
                lhacode = [ 21 ])

cT10 = Parameter(name = 'cT10',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cT10}',
                 lhablock = 'aqgc_bis',
                 lhacode = [ 22 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

