(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (b (BitVec 64))  (c (BitVec 64))  ) (BitVec 64)
	(
		(Start (BitVec 64)
			(
				(bvnot Start)
				(bvxor Start Start)
				(bvand Start Start)
				(bvor Start Start)
				(bvneg Start)
				(bvadd Start Start)
				(bvmul Start Start)
				(bvsub Start Start)
				e b c
			)
		)
	)
)

(constraint (= (deobfucated #x0000000020c9b3e4 #x000000001cc48216 #x0000000006bfe7a9) #x00dd4e603fffffff))
(constraint (= (deobfucated #x000000002939ea33 #x000000000c4aa1f9 #x0000000032f956a1) #x083577063ffffffb))
(constraint (= (deobfucated #x000000001dfc1727 #x000000000453afc0 #x000000002081aac4) #x03ceb2ecffffbfff))
(constraint (= (deobfucated #x000000000eeeb4be #x0000000002d84a77 #x000000002ddeba00) #x02acf39fbffefeff))
(constraint (= (deobfucated #x000000000793298c #x000000003435becd #x0000000035cdc55f) #x01978e497fffffff))
(constraint (= (deobfucated #x0000000037d28759 #x00000000189e5961 #x00000000268b8a99) #x0867ad9fbfdfdff9))
(constraint (= (deobfucated #x000000003553a924 #x000000002ac5af87 #x000000002584e4cb) #x07d0c63e3fdfefef))
(constraint (= (deobfucated #x000000002f59683e #x0000000007f05bb0 #x000000001d233944) #x0563a49fffff7ffe))
(constraint (= (deobfucated #x000000002a3d52fe #x0000000002d038c1 #x00000000270460c7) #x06701091fffffbff))
(constraint (= (deobfucated #x0000000033ea5294 #x000000003604bfe0 #x00000000221ebd09) #x06eb5ac337fefffd))
(constraint (= (deobfucated #x000000001368a573 #x0000000030c6e624 #x000000000b8a911d) #x00e00085bbeef77f))
(constraint (= (deobfucated #x000000000992f4fc #x000000001b1b0b2c #x000000002d057fbe) #x01af09b63f9ffffe))
(constraint (= (deobfucated #x00000000022e643a #x00000000285b81e1 #x0000000002888264) #x0005868a3bffffff))
(constraint (= (deobfucated #x0000000015f08846 #x0000000019c6e937 #x000000002daedf03) #x03ea448dbffefff7))
(constraint (= (deobfucated #x0000000023e554e5 #x0000000008a6756c #x0000000024e92949) #x052cf1746fefffed))
(constraint (= (deobfucated #x000000000df05685 #x0000000001df98ca #x000000001eca9cb5) #x01ad32503ffffeff))
(constraint (= (deobfucated #x000000002e3d1f73 #x0000000029d979d9 #x000000000b736ed9) #x021179d4afff7ffb))
(constraint (= (deobfucated #x000000001cf978ea #x000000002093f6e9 #x000000000f1b795c) #x01b5ba21ffffffff))
(constraint (= (deobfucated #x000000002003e85f #x000000000b2c5043 #x00000000308112f9) #x0610dfe97baffaff))
(constraint (= (deobfucated #x0000000018059f9e #x0000000002dcc7a2 #x000000000a8a4908) #x00fd321e9bdfdffe))
(check-synth)