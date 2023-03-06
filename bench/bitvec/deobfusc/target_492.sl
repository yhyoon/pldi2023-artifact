(set-logic BV)

(synth-fun deobfucated ( (c (BitVec 64))  (a (BitVec 64))  ) (BitVec 64)
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
				c a
			)
		)
	)
)

(constraint (= (deobfucated #x0000000010c79a89 #x000000000eca76c4) #x000000003fea76d6))
(constraint (= (deobfucated #x000000000fa5ad2b #x0000000002c1ade3) #x0000000022cfffff))
(constraint (= (deobfucated #x00000000284d2cf2 #x0000000019250996) #x000000007be57f96))
(constraint (= (deobfucated #x0000000011953082 #x0000000027af6198) #x00000000bfafe5dc))
(constraint (= (deobfucated #x00000000199087a2 #x0000000008bab9c7) #x000000003cfbb9d7))
(constraint (= (deobfucated #x000000003886dbc6 #x000000002c609f6d) #x00000000fdefff7d))
(constraint (= (deobfucated #x000000002d598d35 #x0000000036144fe0) #x00000000f6f77fea))
(constraint (= (deobfucated #x00000000147569bc #x000000002bd1e823) #x00000000bbffebff))
(constraint (= (deobfucated #x000000003a23d40a #x000000001b6a3f54) #x000000009fee3f5c))
(constraint (= (deobfucated #x00000000118fcd1f #x000000002fe0774c) #x00000000afe0774e))
(constraint (= (deobfucated #x0000000004194f03 #x0000000006d25a97) #x000000001efbfadf))
(constraint (= (deobfucated #x0000000019117d9a #x000000001ccd4328) #x000000007fffc3bc))
(constraint (= (deobfucated #x0000000029acf2d2 #x000000000946040c) #x000000006fdff5bc))
(constraint (= (deobfucated #x0000000003e601f8 #x000000000f20bdd7) #x000000003feebfdf))
(constraint (= (deobfucated #x0000000011c83192 #x000000000ab4f963) #x000000003af7ffeb))
(constraint (= (deobfucated #x000000001b7befe5 #x000000000c462742) #x000000004fc6274e))
(constraint (= (deobfucated #x00000000118882be #x00000000021e3053) #x000000002b7fb5df))
(constraint (= (deobfucated #x0000000008fa9776 #x000000001e780836) #x000000007e7d3f3e))
(constraint (= (deobfucated #x00000000098c16c2 #x0000000024d3166d) #x000000007cdf7e6d))
(constraint (= (deobfucated #x000000000e98956a #x0000000039272738) #x00000000ffbfbf3c))
(check-synth)