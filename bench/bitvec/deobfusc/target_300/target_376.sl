(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (c (BitVec 64))  (a (BitVec 64))  ) (BitVec 64)
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
				e c a
			)
		)
	)
)

(constraint (= (deobfucated #x000000002edbf242 #x000000000b025e70 #x00000000009b717f) #xfff950af789386b2))
(constraint (= (deobfucated #x0000000029601809 #x0000000017d11b24 #x0000000039f3aa70) #xfa9bc59cdf3c9190))
(constraint (= (deobfucated #x000000002bd80a45 #x000000000b41cc96 #x00000000261f6c8a) #xfe52d9e417c48cde))
(constraint (= (deobfucated #x0000000029d6ec59 #x000000002a44fc28 #x000000000dd3666b) #xfdb7976cc73dc925))
(constraint (= (deobfucated #x000000001397a363 #x0000000033c30b88 #x0000000017706db7) #xfb42be724b4d0863))
(constraint (= (deobfucated #x00000000164bb58e #x0000000022e7120e #x000000003af3d707) #xf7f66741464c9e18))
(constraint (= (deobfucated #x0000000012a8adcd #x000000003b523e3d #x0000000026a12cd0) #xf70c71a713810b12))
(constraint (= (deobfucated #x000000000c41eaa0 #x0000000026fce911 #x000000002d0a21f6) #xf923fffaa9815153))
(constraint (= (deobfucated #x000000002b33be76 #x000000000aa0ed6d #x0000000001b1a145) #xffedff1c7c72490f))
(constraint (= (deobfucated #x0000000008b8ce00 #x0000000012ce966c #x0000000025977dca) #xfd3d0329d6e7dafd))
(constraint (= (deobfucated #x00000000367975d4 #x0000000001906b71 #x000000000704a8ec) #xfff505c630eb463b))
(constraint (= (deobfucated #x0000000033d2619d #x000000000415161a #x000000000de6eb80) #xffc73f2d8ab06318))
(constraint (= (deobfucated #x0000000027aa4e20 #x000000000664ca0b #x000000002d200aac) #xfedf7b9e8e4d860f))
(constraint (= (deobfucated #x0000000032198a68 #x00000000326db8b0 #x000000002ee24563) #xf6c3b648205e08f4))
(constraint (= (deobfucated #x00000000286d81e2 #x00000000020bee71 #x0000000001e533b5) #xfffc1efb977ca8a7))
(constraint (= (deobfucated #x0000000006ae4944 #x00000000090071dc #x0000000036430422) #xfe178cb8560035d1))
(constraint (= (deobfucated #x000000001d5757a1 #x000000001cac3f73 #x000000000c089da5) #xfea6f5fc6bb0311a))
(constraint (= (deobfucated #x0000000021b4a67f #x000000000a5af8f3 #x0000000031c5df04) #xfdfc95526d17c548))
(constraint (= (deobfucated #x0000000010158e50 #x000000001b62b5f3 #x00000000084770ce) #xff1d45debf9f1bf7))
(constraint (= (deobfucated #x000000002440b98e #x000000001308a8e0 #x0000000027856cf1) #xfd0fc2ac69e5803c))
(check-synth)