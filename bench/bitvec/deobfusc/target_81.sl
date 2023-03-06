(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				a b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000021573c4c #x0000000039d22824) #x0000000000000000))
(constraint (= (deobfucated #x000000003a3338ec #x0000000039594a4a) #x0000000000000000))
(constraint (= (deobfucated #x000000000346cb94 #x000000002cf5b0d1) #x0000000000000000))
(constraint (= (deobfucated #x00000000341464f2 #x0000000011441081) #x0000000000000000))
(constraint (= (deobfucated #x000000002e9cca3d #x000000000920d449) #x0000000000000000))
(constraint (= (deobfucated #x000000002abfc420 #x000000001ccf76ca) #x0000000000000000))
(constraint (= (deobfucated #x000000000fa3b498 #x000000003a8836d0) #x0000000000000000))
(constraint (= (deobfucated #x0000000005ac7979 #x0000000011218f75) #x0000000000000000))
(constraint (= (deobfucated #x0000000019526f26 #x000000001c13f778) #x0000000000000000))
(constraint (= (deobfucated #x0000000025426009 #x0000000010b3fb20) #x0000000000000000))
(constraint (= (deobfucated #x0000000025995066 #x00000000392b747a) #x0000000000000000))
(constraint (= (deobfucated #x00000000395b6b66 #x000000001104fb66) #x0000000000000000))
(constraint (= (deobfucated #x0000000013720759 #x0000000020b92be0) #x0000000000000000))
(constraint (= (deobfucated #x00000000232d87b8 #x0000000002aab60b) #x0000000000000000))
(constraint (= (deobfucated #x0000000030222777 #x000000002ed2cc1b) #x0000000000000000))
(constraint (= (deobfucated #x000000001606a6b9 #x0000000011612751) #x0000000000000000))
(constraint (= (deobfucated #x0000000000fdb631 #x0000000005f40c06) #x0000000000000000))
(constraint (= (deobfucated #x0000000009a00d61 #x000000000c5af159) #x0000000000000000))
(constraint (= (deobfucated #x000000002bc4a828 #x0000000036508afb) #x0000000000000000))
(constraint (= (deobfucated #x0000000001a0e0c6 #x0000000015748d94) #x0000000000000000))
(check-synth)