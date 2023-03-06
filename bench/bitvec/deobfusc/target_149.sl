(set-logic BV)

(synth-fun deobfucated ( (d (BitVec 64))  (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				d a b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000015d31d90 #x000000000adeac17 #x000000000a65c7e6) #xff12c518daa24fe2))
(constraint (= (deobfucated #x0000000008fd2c4a #x000000003437d0c5 #x000000000b7e8f3d) #xfe2a9d47cc55ca00))
(constraint (= (deobfucated #x000000001220ed03 #x000000000d9c3f5f #x00000000057bb4d7) #xff0943698c4f65b3))
(constraint (= (deobfucated #x000000000971031e #x00000000093f1984 #x0000000037c5da77) #xffa8b32373c02076))
(constraint (= (deobfucated #x0000000007891d60 #x00000000212c3301 #x000000002f3b2836) #xff06062527fb79d4))
(constraint (= (deobfucated #x0000000008f844c2 #x0000000033fed4bf #x000000003a39ebdb) #xfe2d9c84aae661ca))
(constraint (= (deobfucated #x0000000025c6f542 #x0000000022545d62 #x0000000032d7fbae) #xfaef205cf3444fe5))
(constraint (= (deobfucated #x00000000145020a2 #x000000002ec19687 #x00000000382daf20) #xfc4a3dc880687130))
(constraint (= (deobfucated #x00000000036aed62 #x0000000025867335 #x00000000101da773) #xff7fc02ec67d0592))
(constraint (= (deobfucated #x00000000193c18b3 #x0000000003054fa1 #x0000000028b3e639) #xffb3c5b028c38de3))
(constraint (= (deobfucated #x0000000007b6aa04 #x000000001d6ed081 #x000000003aa9c9b8) #xff1cf7f81e468cb2))
(constraint (= (deobfucated #x0000000039bb14c8 #x0000000014a9a7ee #x00000000113b4529) #xfb572000cde3ebbe))
(constraint (= (deobfucated #x0000000007d52cd7 #x0000000025909cf9 #x0000000020cde3f0) #xfed9c3cded213bff))
(constraint (= (deobfucated #x00000000115ca710 #x00000000203cce06 #x0000000027839771) #xfdd04b6dc922f90e))
(constraint (= (deobfucated #x000000002c6511cc #x00000000117d805c #x000000001a067409) #xfcf7863540218e9c))
(constraint (= (deobfucated #x000000002339582b #x000000000614dfd3 #x00000000384e6491) #xff29c8a854c8366b))
(constraint (= (deobfucated #x0000000036d8a843 #x0000000018e8d3c2 #x0000000013376c6d) #xfaa9ce82f3179fa4))
(constraint (= (deobfucated #x0000000021117606 #x00000000080b2657 #x00000000183d4839) #xfef6039bf17327ca))
(constraint (= (deobfucated #x0000000030bfc046 #x00000000047525e8 #x0000000007cade62) #xff26b224226757c9))
(constraint (= (deobfucated #x000000002b4da499 #x000000002966ad70 #x000000002ce5d146) #xf8ff325d5a8d4585))
(check-synth)