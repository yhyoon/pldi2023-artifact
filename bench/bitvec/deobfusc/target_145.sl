(set-logic BV)

(synth-fun deobfucated ( (c (BitVec 64))  (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				c a b
			)
		)
	)
)

(constraint (= (deobfucated #x00000000198e385c #x000000001b91e0cb #x000000000d3deb09) #x27bfdf7fe29f4b60))
(constraint (= (deobfucated #x000000003a38ee00 #x000000002aef7c76 #x000000002645aa5b) #x6bd6165771343c00))
(constraint (= (deobfucated #x000000002f862093 #x0000000016bf45a1 #x000000000962cb3c) #x6b3a1cf59f61d07c))
(constraint (= (deobfucated #x0000000005732f73 #x0000000028c011a4 #x000000002f4b2699) #x3183d3ca6f4e8e00))
(constraint (= (deobfucated #x000000000bc9efca #x000000001672227d #x00000000369a2b06) #xca3f686a8813c3e6))
(constraint (= (deobfucated #x0000000016b14055 #x00000000293e8afe #x00000000304b35d5) #x335429c511e6a598))
(constraint (= (deobfucated #x0000000037cac5dd #x000000002a9ed8e2 #x000000003354243a) #x2abf5820008cd4c0))
(constraint (= (deobfucated #x000000001987359a #x000000002e605457 #x00000000150c64ff) #x7ca9be7fa3cd70d4))
(constraint (= (deobfucated #x000000000d6fea49 #x000000000fb6af72 #x0000000029c26c06) #xfe779de724fc7800))
(constraint (= (deobfucated #x000000001de1ea71 #x0000000000301fb0 #x0000000025940eb6) #xa31ecbb0585db460))
(constraint (= (deobfucated #x000000001f023d73 #x000000002b863929 #x00000000364cb5e2) #x60d1f8e99dda7e9c))
(constraint (= (deobfucated #x00000000061e1b3a #x000000002cfdc904 #x0000000005a592d3) #x1dbe4d06dac50000))
(constraint (= (deobfucated #x000000000a3690fc #x000000002142212f #x0000000009253013) #xffe5e7c7da679218))
(constraint (= (deobfucated #x000000002718eecb #x000000003b037cd1 #x000000000e724efc) #xc0e3291ab6404304))
(constraint (= (deobfucated #x000000002a8460b4 #x000000003a809ad9 #x00000000281cf248) #x1b9a76e9e8f87844))
(constraint (= (deobfucated #x0000000008c27259 #x0000000030e69c56 #x000000000ceb9edb) #xcc54853e18d369b4))
(constraint (= (deobfucated #x0000000035c9520a #x000000000aca0193 #x0000000018cd6117) #xf4aa355de9b589bc))
(constraint (= (deobfucated #x00000000276f00b7 #x0000000036697deb #x000000001904f8e4) #xe477256beb5f6198))
(constraint (= (deobfucated #x000000001fc700c5 #x000000003a65b91b #x0000000015734a71) #x8fa9c50d893a75e0))
(constraint (= (deobfucated #x000000003947a758 #x0000000014ca30cd #x000000002bca60cc) #x7c2c80a38eab7458))
(check-synth)