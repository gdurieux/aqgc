(* mydir = NotebookDirectory[] *)
mydir = $InputFileName // DirectoryName
(* from http://feynrules.irmp.ucl.ac.be/downloads/feynrules-current.tar.gz *)
$FeynRulesPath = ToFileName[mydir,"feynrules-current"]
$Path = Join[{mydir, $FeynRulesPath}, $Path]
<<FeynRules`


(*** FeynArts model in the unbroken phase ***)
(***
LoadModel["ew-unbroken-phase.fr", "aqgc.fr"]
FeynmanGauge=False;
WriteFeynArtsOutput[
	Total[LagAQGC] + Total[LagAQGCEboliEtAl],
	MaxParticles -> 4,
	FlavorExpand->False,
	CouplingRename->False,
	Output->"aqgc_fa"]
Run["sed -i '/FourVector\/:/{s/^/\(\*/;s/$/\*\)/}' " <> mydir <> "/aqgc_fa/aqgc_fa.gen"]
***)


(*** UFO model in the broken phase ***)
Print["--- Loading model files, attempting to use the unitary gauge" ];
Run["sed -i 's/^FeynmanGauge *=.\+/FeynmanGauge = False; feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar ->0}, {}];/ ' " <> ToFileName[$FeynRulesPath,"Models/SM/SM.fr"]];
Run["sed -i 's/Definitions *-> *{ *Phi\[1\] *->.\+/Definitions    -> { Phi[1] -> -I GP, Phi[2] -> (vev + H + I G0)\/Sqrt[2]  } \/. feynmangaugerules/ ' " <> ToFileName[$FeynRulesPath,"Models/SM/SM.fr"]];
LoadModel[ToFileName[$FeynRulesPath,"Models/SM/SM.fr"], ToFileName[mydir,"su2-structures.fr"], ToFileName[mydir,"aqgc.fr"]]


Print["--- Loading restrictions" ];
LoadRestriction[ToFileName[$FeynRulesPath,"Models/SM/DiagonalCKM.rst"]]
LoadRestriction[ToFileName[$FeynRulesPath,"Models/SM/Massless.rst"]]

(** SM vertices **)
Print["--- SM vertices" ];
filename = ToFileName[mydir,"vertices","sm_vertices.txt"];
If[	FileExistsQ[filename],
	Print["--- Feynman rules already stored for the SM"];,
	smvertices = FeynmanRules[
		LSM,
		FlavorExpand -> {Generation,Colour,SU2D,SU2W}
		];
	Export[ filename, smvertices ];
	];
smvertices = ReadList[filename];



Print["--- aQGC vertices" ];
Lag = Join[LagAQGC, LagAQGCEboliEtAl];
n = Length[Lag];
Print["--- " <> ToString[n] <> " operators in the Lagrangian"]


(** n-point **)
ptmax = 5;
For[ pt = 4, pt<=ptmax, pt++,
Print["--- Including " <> ToString[pt] <> " point vertices"]; 
suffix = "_" <> ToString[pt] <> "pt";

(** compute and save Feynman rules, if not already stored **)
vertices = {};
For[i = 1, i <= n, i++,
	filename = ToFileName[mydir,"vertices","aqgc_vertices_"<>ToString[i]<>suffix<>".txt"];
	If[	FileExistsQ[filename],
		Print["--- Feynman rules already stored for operator number " <> ToString[i]];
		Continue[];
		];
	Print["--- Computing Feynman rules for operator number " <> ToString[i] ];
	vertex = FeynmanRules[
		Lag[[i]],
		FlavorExpand -> {Generation,Colour,SU2D,SU2W},
		MaxParticles -> pt,
		MinParticles -> pt
		];
	Export[ filename, vertex ];
	vertices = Join[vertices, vertex];
];
];

(** load Feynman rules from files **)
Print["--- Loading all Feynman rules from files"]
vertices = smvertices;
For[ pt = 4, pt<=ptmax, pt++, 
suffix = "_" <> ToString[pt] <> "pt";
For[i = 1, i <= n, i++,
	filename = ToFileName[mydir,"vertices","aqgc_vertices_"<>ToString[i]<>suffix<>".txt"];
	vertex = ReadList[ filename ] ;
	vertices = Join[vertices,vertex];
];
];

Print["--- Writing UFO" ];
WriteUFO[{},
	Input->vertices,
	FlavorExpand -> {},
	AddDecays->False,
	Output->"aqgc_ufo"];


Print["--- Done!"]
Exit[]
