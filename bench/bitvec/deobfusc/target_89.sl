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

(constraint (= (deobfucated #x00000000098c4e77 #x000000002a4d6fce #x0000000034e80758) #xffffffff8ec1f88b))
(constraint (= (deobfucated #x000000003122bcb8 #x0000000016ab2945 #x000000000a544c77) #xffffffff7cbb2933))
(constraint (= (deobfucated #x0000000018130d4d #x0000000038b2b43f #x0000000014cc0b84) #xffffffffa25b37aa))
(constraint (= (deobfucated #x000000001cae0d2e #x000000000affc923 #x000000002f7adf5c) #xffffffffa47d573c))
(constraint (= (deobfucated #x000000000679ee4d #x0000000037a4bed6 #x00000000326ea382) #xffffffff8dca050d))
(constraint (= (deobfucated #x000000002ba85af8 #x0000000026d4a206 #x00000000279158ab) #xffffffffa14a00ae))
(constraint (= (deobfucated #x0000000039c3562a #x000000002ee7a96c #x00000000070e9858) #xffffffff588731f7))
(constraint (= (deobfucated #x000000002bb736ae #x000000002c96bca4 #x000000001e0e39d1) #xffffffff71f8fd2e))
(constraint (= (deobfucated #x000000000a5717bc #x000000001c2f9dc6 #x000000001a590b2e) #xffffffffc96b2deb))
(constraint (= (deobfucated #x000000002b3d0423 #x000000000307ebb6 #x000000001e0cb87b) #xffffffff9c8953ce))
(constraint (= (deobfucated #x0000000023eec0fa #x0000000027dc15ae #x00000000362f3d66) #xffffffff9e732bbb))
(constraint (= (deobfucated #x000000000dd7f9fe #x00000000126c1641 #x000000001142358c) #xffffffffc326234e))
(constraint (= (deobfucated #x00000000041d2344 #x0000000034e3c9a1 #x000000002be84084) #xffffffff9709af5a))
(constraint (= (deobfucated #x000000003aabbfe6 #x000000002b786112 #x000000000a407fbd) #xffffffff68f01eac))
(constraint (= (deobfucated #x000000002555b2c0 #x000000000e221487 #x0000000015f2a55f) #xffffffff9be12119))
(constraint (= (deobfucated #x0000000025979251 #x000000003af5c8ed #x000000003444538e) #xffffffff8d9ee2e2))
(constraint (= (deobfucated #x00000000301e6597 #x00000000372da8a1 #x000000002e45b72b) #xffffffff7a581f0b))
(constraint (= (deobfucated #x0000000004f2e121 #x000000001631af58 #x000000001210531d) #xffffffffcdf8bd4a))
(constraint (= (deobfucated #x00000000170a5463 #x00000000195c6a5e #x000000003a091e0d) #xffffffffa295f6d0))
(constraint (= (deobfucated #x000000001e2b0dcb #x0000000007afbf0b #x00000000019a59fd) #xffffffffba73def3))
(check-synth)