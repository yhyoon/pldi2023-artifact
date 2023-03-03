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

(constraint (= (deobfucated #x0000000020e1c973 #x0000000021bf817a) #xfbaa4bf16e568fbe))
(constraint (= (deobfucated #x0000000009d68b00 #x0000000005b52339) #xffc7d93e377f2d39))
(constraint (= (deobfucated #x00000000272e79ee #x000000002098b79c) #xfb02d10fe1fdd8fc))
(constraint (= (deobfucated #x0000000006ee9ced #x000000001273afbc) #xff801704bf8ffef4))
(constraint (= (deobfucated #x000000001883b47d #x0000000003ac5d70) #xffa5f372b6f3a5d0))
(constraint (= (deobfucated #x000000000877e61a #x00000000295be09f) #xfea1c218fff775fb))
(constraint (= (deobfucated #x0000000008f832f0 #x00000000252d9e50) #xfeb287767edff7b0))
(constraint (= (deobfucated #x000000003588e883 #x000000000c47341c) #xfd6eb13bf57ef5bc))
(constraint (= (deobfucated #x0000000031dc90f9 #x0000000031be1dcc) #xf64fc0bf56467ebc))
(constraint (= (deobfucated #x000000003a2a4505 #x00000000182bc701) #xfa821736fa7fdffb))
(constraint (= (deobfucated #x000000000282284e #x000000002d9191ea) #xff8db1c37295faf6))
(constraint (= (deobfucated #x0000000020996d93 #x0000000024fb025d) #xfb4a75dbff4f0bfb))
(constraint (= (deobfucated #x000000000850150b #x0000000017561078) #xff3e02ac1ff772d8))
(constraint (= (deobfucated #x00000000036fe295 #x00000000078f2091) #xffe604de6d93e9bb))
(constraint (= (deobfucated #x0000000003dc4f77 #x0000000000ac7a90) #xfffd662177549770))
(constraint (= (deobfucated #x000000002add522b #x000000001cdd451b) #xfb2abe617d67ff7f))
(constraint (= (deobfucated #x000000003a743d47 #x0000000033835fbb) #xf43cd873ff87e467))
(constraint (= (deobfucated #x000000001733ee1c #x000000003276d9a6) #xfb6d15d4fe9dfdde))
(constraint (= (deobfucated #x0000000011e73a8f #x000000003515f77b) #xfc499799f7bbeccf))
(constraint (= (deobfucated #x000000001641d5ef #x00000000384a0af4) #xfb1b29385fcef73c))
(check-synth)