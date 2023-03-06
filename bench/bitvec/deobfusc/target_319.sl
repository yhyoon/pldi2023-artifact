(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (c (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				a c b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000022853ebd #x0000000030f48e54 #x00000000007f1978) #x0000000000000000))
(constraint (= (deobfucated #x000000003aa55a20 #x0000000003281f5a #x0000000022d3e3ca) #x0000000000000000))
(constraint (= (deobfucated #x000000002d597acf #x000000000d18747a #x000000001e8831a9) #x0000000000000000))
(constraint (= (deobfucated #x0000000022d63dfd #x0000000015ca38b0 #x0000000013702faf) #x0000000000000000))
(constraint (= (deobfucated #x000000003499a191 #x0000000015cc29d2 #x000000000a238c4e) #x0000000000000000))
(constraint (= (deobfucated #x000000000bc26b68 #x000000000016a34b #x000000001e3bfa7b) #x0000000000000000))
(constraint (= (deobfucated #x000000001aed19e6 #x00000000028eb6fa #x000000001f12d79c) #x0000000000000000))
(constraint (= (deobfucated #x00000000178d6ef2 #x000000002eb42eed #x00000000027a4b91) #x0000000000000000))
(constraint (= (deobfucated #x000000003ac2fb90 #x0000000016b783c5 #x00000000398ac122) #x0000000000000000))
(constraint (= (deobfucated #x0000000006707868 #x000000001e518c52 #x0000000000a4bc44) #x0000000000000000))
(constraint (= (deobfucated #x000000002ad751f9 #x000000000706f10c #x0000000022007571) #x0000000000000000))
(constraint (= (deobfucated #x000000001c37cf68 #x00000000065f1358 #x0000000025f59e40) #x0000000000000000))
(constraint (= (deobfucated #x000000000e36e2ff #x000000002080cc2d #x000000000c33b6df) #x0000000000000000))
(constraint (= (deobfucated #x000000000dc0afbd #x00000000376388d5 #x0000000011dbe23f) #x0000000000000000))
(constraint (= (deobfucated #x000000001aa21c69 #x000000000436df7c #x0000000034df3dba) #x0000000000000000))
(constraint (= (deobfucated #x00000000207037ba #x000000002c98d900 #x000000001f418eb7) #x0000000000000000))
(constraint (= (deobfucated #x00000000247cf5c5 #x000000002adfaaf1 #x00000000196031e4) #x0000000000000000))
(constraint (= (deobfucated #x0000000008a7615b #x00000000040fd028 #x0000000010cbf770) #x0000000000000000))
(constraint (= (deobfucated #x000000001973efc4 #x000000003b702b8b #x0000000015515576) #x0000000000000000))
(constraint (= (deobfucated #x00000000063f50ba #x0000000027659680 #x000000000f9bc917) #x0000000000000000))
(check-synth)