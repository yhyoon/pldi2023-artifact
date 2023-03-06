(set-logic BV)

(synth-fun deobfucated ( (b (BitVec 64))  ) (BitVec 64)
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
				b
			)
		)
	)
)

(constraint (= (deobfucated #x00000000100f9595) #xfefe0c5a81233747))
(constraint (= (deobfucated #x000000003354f15d) #xf5b50ba5a967c437))
(constraint (= (deobfucated #x0000000024d6a9b5) #xfab2ec44ece38607))
(constraint (= (deobfucated #x0000000026ff51fb) #xfa0f35050fb533e7))
(constraint (= (deobfucated #x0000000019d85bae) #xfd64073d2d8ad5bc))
(constraint (= (deobfucated #x000000001937a9a3) #xfd8414c3d58d6237))
(constraint (= (deobfucated #x0000000036c3ac03) #xf448dddf3bd9f7f7))
(constraint (= (deobfucated #x0000000002a5bcb5) #xfff8fdc05f93a807))
(constraint (= (deobfucated #x000000001c9f129a) #xfcccd1163359fb5c))
(constraint (= (deobfucated #x000000002331d667) #xfb2955ac0f01a28f))
(constraint (= (deobfucated #x000000001f3b9826) #xfc308347500eda5c))
(constraint (= (deobfucated #x0000000016dd6931) #xfdf5326cca2cc49f))
(constraint (= (deobfucated #x0000000023df558d) #xfaf92bc549c31057))
(constraint (= (deobfucated #x000000001f715c2e) #xfc23597a5a32e7bc))
(constraint (= (deobfucated #x000000003a8b65ed) #xf29c89e8c40d2297))
(constraint (= (deobfucated #x0000000015576677) #xfe388b59ac1af4af))
(constraint (= (deobfucated #x00000000206f87b2) #xfbe3ed7c8bb6c83c))
(constraint (= (deobfucated #x000000002758099a) #xf9f40ecc79c3cf5c))
(constraint (= (deobfucated #x0000000012d6ee94) #xfe9d11ff72387a70))
(constraint (= (deobfucated #x000000000221810b) #xfffb75994e1de987))
(check-synth)