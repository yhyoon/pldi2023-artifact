(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				e a b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000004b79721 #x00000000383570ff #x000000002ccc59d5) #x00000000280450d6))
(constraint (= (deobfucated #x0000000005c98d9d #x0000000024578402 #x0000000019dde59f) #x0000000000558403))
(constraint (= (deobfucated #x000000001236704c #x000000000ae094b3 #x000000001a40922f) #x000000000a409024))
(constraint (= (deobfucated #x0000000032c2d391 #x0000000014386e9a #x00000000210c0718) #x0000000000080619))
(constraint (= (deobfucated #x0000000008186fdc #x0000000028ce9fbb #x000000002296b804) #x0000000020869801))
(constraint (= (deobfucated #x000000000149625a #x0000000009a4c76f #x00000000262b3861) #x0000000000200062))
(constraint (= (deobfucated #x0000000039648981 #x000000001ecb7c14 #x0000000016443505) #x0000000016403405))
(constraint (= (deobfucated #x0000000037e0cd2c #x000000003a0d0f97 #x00000000107cbedd) #x00000000100c0e96))
(constraint (= (deobfucated #x00000000226894d0 #x00000000002e5179 #x0000000000d6aa67) #x0000000000060062))
(constraint (= (deobfucated #x000000000830059b #x000000002ba8825a #x00000000177072e2) #x0000000003200243))
(constraint (= (deobfucated #x000000000985b39b #x000000001a39454c #x0000000033914bca) #x0000000012114149))
(constraint (= (deobfucated #x000000001340f259 #x000000000fae172b #x0000000011a9989c) #x0000000001a81009))
(constraint (= (deobfucated #x00000000059b2df4 #x0000000006e2c747 #x000000001018b37b) #x0000000000008344))
(constraint (= (deobfucated #x000000002c33ced7 #x0000000005ebb9c5 #x000000000787c966) #x0000000005838945))
(constraint (= (deobfucated #x0000000014304228 #x000000000aed80f2 #x000000002940c10e) #x0000000008408003))
(constraint (= (deobfucated #x000000002dea8b3f #x000000001bfc05dd #x00000000002092f4) #x00000000002000d5))
(constraint (= (deobfucated #x0000000031f1076c #x000000000a96d196 #x000000003339c646) #x000000000210c007))
(constraint (= (deobfucated #x000000001d206fcd #x0000000026176f3c #x0000000002cc5cad) #x0000000002044c2d))
(constraint (= (deobfucated #x000000002ff12b7d #x0000000038c982f5 #x000000002c05cae2) #x00000000280182e1))
(constraint (= (deobfucated #x000000002f24924a #x0000000005c3426f #x000000003400b7a6) #x0000000004000227))
(check-synth)