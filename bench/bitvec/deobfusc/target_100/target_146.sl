(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				e b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000014109512 #x000000002c24d638) #xffffffffd3db29c8))
(constraint (= (deobfucated #x0000000012590f94 #x000000000425fc21) #xfffffffffbda03df))
(constraint (= (deobfucated #x0000000038a2f364 #x0000000024c317de) #xffffffffdb3ce822))
(constraint (= (deobfucated #x000000001101f3d8 #x0000000013b7caf6) #xffffffffec48350a))
(constraint (= (deobfucated #x00000000342bb7a2 #x00000000247109c5) #xffffffffdb8ef63b))
(constraint (= (deobfucated #x000000002b435e12 #x0000000023738b0c) #xffffffffdc8c74f4))
(constraint (= (deobfucated #x00000000149261e0 #x00000000132f610f) #xffffffffecd09ef1))
(constraint (= (deobfucated #x0000000018901f22 #x000000001e3df13c) #xffffffffe1c20ec4))
(constraint (= (deobfucated #x0000000003bf3034 #x0000000024fee4db) #xffffffffdb011b25))
(constraint (= (deobfucated #x0000000036f91e84 #x000000003167ed6a) #xffffffffce981296))
(constraint (= (deobfucated #x000000000b55ab2e #x00000000357ccf77) #xffffffffca833089))
(constraint (= (deobfucated #x000000003790c86c #x0000000033862b3e) #xffffffffcc79d4c2))
(constraint (= (deobfucated #x000000002b559ddd #x000000003691f890) #xffffffffc96e0770))
(constraint (= (deobfucated #x0000000001129de8 #x00000000269d6c39) #xffffffffd96293c7))
(constraint (= (deobfucated #x0000000027051d19 #x0000000035d084af) #xffffffffca2f7b51))
(constraint (= (deobfucated #x000000001f8c26fe #x000000001fe0b890) #xffffffffe01f4770))
(constraint (= (deobfucated #x00000000383c095d #x000000002aa1a1a2) #xffffffffd55e5e5e))
(constraint (= (deobfucated #x0000000005872f25 #x0000000022086f75) #xffffffffddf7908b))
(constraint (= (deobfucated #x000000003826a24a #x000000002ebf9a84) #xffffffffd140657c))
(constraint (= (deobfucated #x000000001a0125fe #x0000000008c51c88) #xfffffffff73ae378))
(check-synth)