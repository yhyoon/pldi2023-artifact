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

(constraint (= (deobfucated #x000000002816d996 #x000000002fdfc1e7 #x000000002dd554da) #x0000000000000000))
(constraint (= (deobfucated #x000000000b1658c0 #x000000000a5a58ae #x0000000002419aa0) #x0000000000000000))
(constraint (= (deobfucated #x000000001c55933a #x000000002e7c954e #x000000001d1aee70) #x0000000000000000))
(constraint (= (deobfucated #x000000001d9d6540 #x0000000039091923 #x0000000024b83439) #x0000000000000000))
(constraint (= (deobfucated #x0000000004901f78 #x00000000042556bd #x000000001ee7adbd) #x0000000000000000))
(constraint (= (deobfucated #x000000000b5d7a85 #x00000000378b3109 #x000000001d471611) #x0000000000000000))
(constraint (= (deobfucated #x000000003b4a6d33 #x0000000002fd9dd4 #x0000000003d46a1a) #x0000000000000000))
(constraint (= (deobfucated #x000000002fcd1c13 #x000000000bb493c8 #x00000000318b1a1b) #x0000000000000000))
(constraint (= (deobfucated #x0000000016cbe737 #x000000003a04772c #x000000001721c251) #x0000000000000000))
(constraint (= (deobfucated #x000000000fc64ff4 #x000000001bbeef35 #x0000000021751cd1) #x0000000000000000))
(constraint (= (deobfucated #x0000000030dbb083 #x000000000532f901 #x0000000016dec974) #x0000000000000000))
(constraint (= (deobfucated #x0000000026c214fd #x0000000030a82e6e #x000000000dbd95a0) #x0000000000000000))
(constraint (= (deobfucated #x0000000024bc0b82 #x000000003165829e #x0000000021574c41) #x0000000000000000))
(constraint (= (deobfucated #x0000000026c00523 #x0000000011ed7c16 #x000000000073e3d2) #x0000000000000000))
(constraint (= (deobfucated #x000000002a401c71 #x000000002dd6b241 #x0000000005dea187) #x0000000000000000))
(constraint (= (deobfucated #x000000000a5a1298 #x00000000162d2318 #x0000000027ad99f9) #x0000000000000000))
(constraint (= (deobfucated #x000000002380674b #x000000003640ae6d #x00000000138b73ec) #x0000000000000000))
(constraint (= (deobfucated #x000000002b278eea #x0000000012a8d594 #x000000002517b5bc) #x0000000000000000))
(constraint (= (deobfucated #x00000000068259a3 #x000000002f4f3fe5 #x0000000037135e13) #x0000000000000000))
(constraint (= (deobfucated #x0000000008fa0d32 #x0000000013051777 #x00000000242a855d) #x0000000000000000))
(check-synth)