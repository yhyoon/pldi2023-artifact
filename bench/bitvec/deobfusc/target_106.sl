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

(constraint (= (deobfucated #x00000000272c4c64 #x00000000090ac6ed) #x20d93767b2784778))
(constraint (= (deobfucated #x0000000000f74aab #x00000000300d0d6e) #x661b1b67457f97a2))
(constraint (= (deobfucated #x0000000011f7d7a7 #x0000000028a6f3ef) #xcd612a5001543726))
(constraint (= (deobfucated #x0000000016ca473c #x000000001072957e) #x06b1dc5c19cce8b4))
(constraint (= (deobfucated #x000000002cb9943e #x0000000005fdcfbd) #x26efcad8f114d8f8))
(constraint (= (deobfucated #x0000000000eaf06b #x000000000162f603) #xf576f92b3c24131e))
(constraint (= (deobfucated #x000000003a96ca9f #x0000000026d020b8) #x086ca0e3213f111e))
(constraint (= (deobfucated #x000000003007806c #x00000000188f42cd) #x6506218d5210e388))
(constraint (= (deobfucated #x00000000141079ab #x00000000279d4457) #x06d2aadc797551ea))
(constraint (= (deobfucated #x0000000022cccdf5 #x00000000302d12fe) #x5397cb618ef26a7c))
(constraint (= (deobfucated #x000000002ea9cf65 #x0000000016ade174) #xe436747d64a8f9e4))
(constraint (= (deobfucated #x000000000c693887 #x000000001680fbf8) #xeb260669d70efd56))
(constraint (= (deobfucated #x000000000ffe8895 #x00000000145f17dc) #x0c1e7f831e00873c))
(constraint (= (deobfucated #x00000000327b057e #x0000000028ffc2f2) #x09570384aea3bc66))
(constraint (= (deobfucated #x0000000000b0fee0 #x0000000021a68b2a) #xe9fe14636fb09ba0))
(constraint (= (deobfucated #x0000000011fc049f #x000000002bbed9f3) #x9be14acab204f562))
(constraint (= (deobfucated #x00000000260bc997 #x00000000290cfffb) #x63e601dd07cd78e2))
(constraint (= (deobfucated #x000000000b6c24d1 #x0000000020ec4504) #xb43edd605e99c1f8))
(constraint (= (deobfucated #x000000002e30cd3d #x000000003b94a428) #xb2565857623a0ba4))
(constraint (= (deobfucated #x0000000035c9687c #x000000001bfc95f4) #xad13a9e2ca1fb65c))
(check-synth)