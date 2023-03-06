(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (c (BitVec 64))  ) (BitVec 64)
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
				e c
			)
		)
	)
)

(constraint (= (deobfucated #x000000001327e79a #x0000000029ac2c1d) #x000000005590910d))
(constraint (= (deobfucated #x0000000028c6f135 #x0000000026f2cb6c) #x000000000287beb8))
(constraint (= (deobfucated #x000000002b998459 #x000000002c691cc6) #x0000000005ff4962))
(constraint (= (deobfucated #x0000000020c73fae #x000000000b0607d4) #xffffffffdf7d90a0))
(constraint (= (deobfucated #x000000001df3c710 #x00000000285fe5dc) #x0000000034e45e6c))
(constraint (= (deobfucated #x00000000035d9e9f #x0000000015ba150d) #x00000000395aedde))
(constraint (= (deobfucated #x0000000002548ab3 #x000000002b92a781) #x000000007bfe5e9e))
(constraint (= (deobfucated #x00000000274dd46a #x000000000bcf3caa) #xffffffffd184f904))
(constraint (= (deobfucated #x00000000006f707d #x0000000013757621) #x00000000391c114a))
(constraint (= (deobfucated #x000000000ea841a3 #x000000002d584fbc) #x000000005eb02a50))
(constraint (= (deobfucated #x00000000203cb8e7 #x0000000008a436f1) #xffffffffd94f0226))
(constraint (= (deobfucated #x000000002bac9d62 #x00000000260ef1c2) #xfffffffff8c70944))
(constraint (= (deobfucated #x000000001d2feb93 #x00000000331389a8) #x000000004dd73c54))
(constraint (= (deobfucated #x0000000030ce974b #x000000001b7517d1) #xffffffffe07e019e))
(constraint (= (deobfucated #x0000000002bc16e4 #x000000002d286ed2) #x0000000081d917f2))
(constraint (= (deobfucated #x000000001e50d842 #x0000000021a7b100) #x000000002854d280))
(constraint (= (deobfucated #x00000000141513b5 #x000000002ed3b230) #x00000000603fdcf8))
(constraint (= (deobfucated #x0000000017af856d #x000000002541281a) #x000000003b636d6e))
(constraint (= (deobfucated #x00000000057ad19e #x000000002655c277) #x0000000063bae415))
(constraint (= (deobfucated #x000000002cde046d #x000000002c1f7d65) #xfffffffffe846af2))
(check-synth)