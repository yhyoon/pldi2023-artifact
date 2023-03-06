(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (a (BitVec 64))  (c (BitVec 64))  ) (BitVec 64)
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
				e a c
			)
		)
	)
)

(constraint (= (deobfucated #x0000000004f63fa3 #x0000000030a745f8 #x000000003128f2f6) #xffffffffa3a7b3b2))
(constraint (= (deobfucated #x0000000013bae960 #x000000002df3e1aa #x00000000294bea7f) #xffffffffb7d3260b))
(constraint (= (deobfucated #x000000002000eda1 #x000000000ee2c94d #x0000000033484376) #x00000000023b5b06))
(constraint (= (deobfucated #x000000001411bb3a #x0000000028511a35 #x0000000022e4666e) #xffffffffc36f86cf))
(constraint (= (deobfucated #x00000000184dff85 #x0000000002992fe2 #x000000003a8de03b) #x00000000131b9fc0))
(constraint (= (deobfucated #x0000000012034438 #x0000000028e0b9c7 #x0000000036994717) #xffffffffc041d0a9))
(constraint (= (deobfucated #x00000000004d8aa6 #x00000000162a0aee #x0000000008fd514f) #xffffffffd3f974c9))
(constraint (= (deobfucated #x00000000119a1c12 #x0000000030dfddd4 #x0000000031697907) #xffffffffafda6069))
(constraint (= (deobfucated #x0000000033197391 #x0000000005ff02de #x0000000003d730d1) #x00000000271b6dd4))
(constraint (= (deobfucated #x00000000274306f0 #x00000000340f178e #x00000000355a0f5e) #xffffffffbf24d7d3))
(constraint (= (deobfucated #x00000000069a8595 #x0000000022039a6e #x0000000012dbe53b) #xffffffffc29350b8))
(constraint (= (deobfucated #x00000000176c047e #x00000000229832a9 #x0000000034ecf40a) #xffffffffd23b9f2b))
(constraint (= (deobfucated #x00000000194eb52c #x000000000e8a9145 #x0000000038d1a71b) #xfffffffffc3992a1))
(constraint (= (deobfucated #x000000000a91035a #x0000000034931b0e #x0000000022fd2465) #xffffffffa16acd3d))
(constraint (= (deobfucated #x00000000264b2000 #x0000000006f7b7b9 #x000000003a0cec99) #x00000000185bb08d))
(constraint (= (deobfucated #x0000000038d15dcf #x000000001829cc7e #x0000000018e6ded3) #x00000000087dc4d2))
(constraint (= (deobfucated #x00000000068a9545 #x000000000620bbb6 #x000000002bd20019) #xfffffffffa491dd8))
(constraint (= (deobfucated #x000000000d519320 #x00000000378be2b2 #x000000000fbee264) #xffffffff9e39cdbb))
(constraint (= (deobfucated #x000000001a96c5b3 #x00000000231cc994 #x000000000cfd3d79) #xffffffffd45d328a))
(constraint (= (deobfucated #x000000002d7f42c6 #x00000000325e8c6e #x0000000021ab7541) #xffffffffc8c229e9))
(check-synth)