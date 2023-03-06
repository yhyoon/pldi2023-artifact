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

(constraint (= (deobfucated #x000000002b0a4b33 #x0000000015759cfe #x0000000039dfa618) #x75eedff169d89bc0))
(constraint (= (deobfucated #x0000000008dc9e5e #x000000002b5a0636 #x000000001601a439) #x8e524f04df7adefe))
(constraint (= (deobfucated #x000000002c816af7 #x000000001933599a #x000000000f6f5855) #x7d967159bf9fecff))
(constraint (= (deobfucated #x000000000b8d3490 #x00000000280b84d3 #x000000002f8ed3f3) #x9a322e1ce3bf3390))
(constraint (= (deobfucated #x00000000348e4b04 #x000000002c13dfd4 #x000000002e0c5f22) #xe8bbf89a344fef10))
(constraint (= (deobfucated #x0000000035868d23 #x0000000011c59cb3 #x00000000068d2d51) #x18afa375c546dd03))
(constraint (= (deobfucated #x000000000887a602 #x00000000040094dd #x000000001b70501f) #xe414afe671dcef82))
(constraint (= (deobfucated #x00000000261228e0 #x000000002f5aa009 #x0000000039075556) #x1b092770b25d67c0))
(constraint (= (deobfucated #x000000000472a024 #x00000000285b2355 #x0000000026182197) #x786aeb003fe6be64))
(constraint (= (deobfucated #x000000001b132548 #x000000001554c9ed #x000000000a70d711) #xa424be813ff30748))
(constraint (= (deobfucated #x00000000246196bc #x0000000013e63dc4 #x000000003a42f756) #xf4ac91c3a879fff4))
(constraint (= (deobfucated #x0000000001589496 #x0000000028e44b37 #x000000002c25a232) #xce811576e10fb8d8))
(constraint (= (deobfucated #x000000000752801f #x00000000350520f9 #x0000000007d8984a) #xe2d138f55c52b71e))
(constraint (= (deobfucated #x00000000180f24d0 #x00000000349c3dea #x000000001e40312c) #x1c2b7f702965e500))
(constraint (= (deobfucated #x00000000314de35b #x000000002e9425e2 #x00000000033fd6ce) #x208af818cb6df1ee))
(constraint (= (deobfucated #x00000000023f74e9 #x0000000002a4741c #x0000000011b80717) #x30f2216d7c7fb779))
(constraint (= (deobfucated #x00000000298366fd #x0000000011e683fb #x00000000273e196c) #x1054dd082eab1f54))
(constraint (= (deobfucated #x00000000312e2915 #x0000000031c18ced #x0000000034dae083) #x1e4b9e563ebe30bd))
(constraint (= (deobfucated #x0000000038baf201 #x0000000038a91d84 #x0000000016913596) #xb666ae6f1e58fbe4))
(constraint (= (deobfucated #x00000000248f6304 #x000000001bed155b #x000000000fb2e0f4) #x70ba77c5574f7244))
(check-synth)