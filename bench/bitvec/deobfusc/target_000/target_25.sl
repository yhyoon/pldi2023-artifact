(set-logic BV)

(synth-fun deobfucated ( (d (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				d b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000007ce7ac7 #x0000000015d81ded) #x0000000002066202))
(constraint (= (deobfucated #x000000000ecadc03 #x000000001a354d1e) #x0000000004ca9001))
(constraint (= (deobfucated #x000000000ee6dabc #x00000000261ed54c) #x0000000008e00ab0))
(constraint (= (deobfucated #x000000000342b3b2 #x000000001c3b1461) #x000000000340a392))
(constraint (= (deobfucated #x000000002d9331bc #x00000000074232bc) #x0000000028910100))
(constraint (= (deobfucated #x00000000346ccc8b #x000000002e479836) #x0000000010284489))
(constraint (= (deobfucated #x00000000036b7678 #x0000000002cbe009) #x0000000001201670))
(constraint (= (deobfucated #x0000000014fd9a2f #x0000000027fc68be) #x0000000010019201))
(constraint (= (deobfucated #x0000000000a95edd #x000000003a3b14da) #x0000000000804a05))
(constraint (= (deobfucated #x0000000036f9a902 #x0000000038d4a9b6) #x0000000006290000))
(constraint (= (deobfucated #x000000002ff87dc6 #x000000003505aa6d) #x000000000af85582))
(constraint (= (deobfucated #x00000000288231dc #x0000000015beaf4d) #x0000000028001090))
(constraint (= (deobfucated #x000000000bc4ce53 #x0000000010fc562a) #x000000000b008851))
(constraint (= (deobfucated #x00000000280ea0ec #x0000000018b17ed9) #x00000000200e8024))
(constraint (= (deobfucated #x0000000032c10c96 #x00000000077da272) #x0000000030800c84))
(constraint (= (deobfucated #x000000000e0e79aa #x0000000016047a60) #x00000000080a018a))
(constraint (= (deobfucated #x0000000004bbf679 #x00000000200bc258) #x0000000004b03421))
(constraint (= (deobfucated #x000000002119d9bc #x000000001fbd0cdd) #x000000002000d120))
(constraint (= (deobfucated #x00000000290adc83 #x000000000f77753f) #x0000000020088880))
(constraint (= (deobfucated #x00000000010561b4 #x0000000025f313e4) #x0000000000046010))
(check-synth)