(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				e a b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000005ade595 #x000000001636dcd7 #x0000000037a23484) #x2ec84ab3138e1630))
(constraint (= (deobfucated #x000000000c11b07f #x000000001ed1f30c #x00000000009ae224) #xa9f2881e89b0df89))
(constraint (= (deobfucated #x00000000337d79f9 #x00000000019c62d8 #x0000000027285108) #xa06fb8feafa521f1))
(constraint (= (deobfucated #x0000000017d09808 #x0000000016ee6cf1 #x0000000020a77fb9) #x8589b45a854fee2e))
(constraint (= (deobfucated #x0000000037fac94e #x00000000205294c0 #x0000000014f5e86c) #x2912ab0d125f39c1))
(constraint (= (deobfucated #x000000002a42d22b #x000000000d297fe3 #x0000000006ce225f) #x3fa57a70e58359e9))
(constraint (= (deobfucated #x00000000228bba2c #x000000001f3f183a #x0000000000cf9827) #x37b80b9b8a21ade7))
(constraint (= (deobfucated #x0000000025761560 #x0000000010d138cf #x000000003892a91f) #x58ef6e8246c3f3d2))
(constraint (= (deobfucated #x0000000008a8a123 #x0000000038abdf00 #x000000002cd1d126) #x3b9180ae4b212a01))
(constraint (= (deobfucated #x00000000228cb840 #x000000000450fd9d #x0000000030bc2cdc) #xb7bce1ffbd4667c2))
(constraint (= (deobfucated #x0000000020123483 #x000000002c91de3f #x000000002ba5f840) #xf42a9eefa7325000))
(constraint (= (deobfucated #x000000001c14cd8b #x00000000098a2557 #x000000001ac8d88d) #xcbd6d99941b936e1))
(constraint (= (deobfucated #x00000000069f7f63 #x000000001c2c2d0b #x00000000319b34f2) #x574423e19d35af74))
(constraint (= (deobfucated #x0000000011744e5e #x000000002443650c #x000000001d55efb3) #xb94c70bf3e0b1ec5))
(constraint (= (deobfucated #x000000002d25fec2 #x0000000034096fac #x00000000378d2661) #xb4a1a8be4829f055))
(constraint (= (deobfucated #x00000000325aa5a9 #x0000000007c97cb0 #x000000000a4fb97a) #x11e1729803fa8521))
(constraint (= (deobfucated #x000000000ce67696 #x000000003ab728aa #x000000001d3b41b2) #x9453ca7c1c9be3c3))
(constraint (= (deobfucated #x000000001acccd8e #x0000000029e9bb17 #x000000002ae02414) #x7ac13e0ab986a584))
(constraint (= (deobfucated #x000000000e4bed1d #x0000000008763abf #x0000000011a7952a) #x8834ce6b5c2b75b4))
(constraint (= (deobfucated #x00000000034e0470 #x000000002314d8e8 #x000000002bc257ac) #x4b8eeb96b27dafa9))
(check-synth)