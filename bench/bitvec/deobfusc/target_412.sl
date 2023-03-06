(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (c (BitVec 64))  (d (BitVec 64))  ) (BitVec 64)
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
				a c d
			)
		)
	)
)

(constraint (= (deobfucated #x0000000000602e57 #x00000000118e9e29 #x0000000030867130) #xffffffffbe6b40c6))
(constraint (= (deobfucated #x000000000e153809 #x000000000c408500 #x000000002beda9a2) #xffffffffcff9f15f))
(constraint (= (deobfucated #x000000003420464c #x00000000054e5a9a #x000000002fa0319e) #xfffffffff311745f))
(constraint (= (deobfucated #x0000000002226b05 #x00000000153e4fc5 #x0000000000e28fbb) #xffffffffea1fa689))
(constraint (= (deobfucated #x000000000bab1b3f #x00000000288ad696 #x0000000001da2e24) #xffffffffd6ed2169))
(constraint (= (deobfucated #x000000001565dbd8 #x0000000038ca79b7 #x000000002ff05d40) #xffffffffc2053e08))
(constraint (= (deobfucated #x000000001143036a #x000000000e101e67 #x0000000012f50ec6) #xffffffffe17ed996))
(constraint (= (deobfucated #x00000000158dc02f #x00000000337de95d #x0000000002017386) #xffffffffcc81a322))
(constraint (= (deobfucated #x0000000016547dd3 #x000000000f733fd7 #x0000000011454b90) #xffffffffdf47c018))
(constraint (= (deobfucated #x00000000342a088b #x000000001d12a624 #x0000000001f99177) #xffffffffe143d97a))
(constraint (= (deobfucated #x000000002977903c #x000000001c157ad9 #x00000000098f2a49) #xffffffffdaea7b25))
(constraint (= (deobfucated #x000000000f96fa79 #x000000003132b9c2 #x0000000016ef8e06) #xffffffffce0b3c39))
(constraint (= (deobfucated #x000000002a20a6b4 #x0000000010ad5ebb #x0000000035d000f9) #xffffffffcdc2a0b3))
(constraint (= (deobfucated #x00000000081c781c #x00000000133d0374 #x0000000021684545) #xffffffffcb82f746))
(constraint (= (deobfucated #x000000000f5b71c8 #x00000000027353e4 #x000000000af049e0) #xfffffffffd4ca3bb))
(constraint (= (deobfucated #x000000000e0554cc #x0000000035f68afd #x000000002eba0a6c) #xffffffffa759729e))
(constraint (= (deobfucated #x000000002f7027ad #x0000000011e7c0c2 #x00000000250da9f0) #xffffffffcd0a9e9d))
(constraint (= (deobfucated #x000000001d194f30 #x000000002a81cda9 #x0000000006448fdd) #xffffffffd13a30b9))
(constraint (= (deobfucated #x000000002232daa3 #x0000000025c03050 #x000000000cab8aad) #xffffffffd1b5c506))
(constraint (= (deobfucated #x00000000229d890c #x0000000028ec874d #x00000000071c2891) #xffffffffd50f5031))
(check-synth)