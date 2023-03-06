(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (d (BitVec 64))  ) (BitVec 64)
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
				a d
			)
		)
	)
)

(constraint (= (deobfucated #x000000000b564ee7 #x0000000018819175) #x31bde9a53433f838))
(constraint (= (deobfucated #x0000000006119cd1 #x000000000b9c5627) #x77a2a2479e186de6))
(constraint (= (deobfucated #x000000002db3ccc3 #x000000002d87f612) #xa08f66e07b5c6368))
(constraint (= (deobfucated #x000000001bce21d9 #x0000000000213e85) #xb233577a30c21f42))
(constraint (= (deobfucated #x0000000001b22892 #x000000000dd62e36) #xbbd5de47d0498440))
(constraint (= (deobfucated #x0000000005814a4c #x000000002fd58d0e) #x01ce290e503198b0))
(constraint (= (deobfucated #x00000000202b0b5a #x000000001b3a5cf2) #xb0dc45b568982990))
(constraint (= (deobfucated #x0000000008172551 #x00000000172420db) #x556526fe0d909c6e))
(constraint (= (deobfucated #x0000000039f56294 #x000000003333848e) #x152f618e935f5710))
(constraint (= (deobfucated #x0000000013a6c829 #x000000001535aba2) #xcd0be7dbb2a60d44))
(constraint (= (deobfucated #x000000002c4560a1 #x0000000034da1d9d) #x5625a88153d9544a))
(constraint (= (deobfucated #x0000000000e252e2 #x000000000f946f8b) #x9bd758e092b8b722))
(constraint (= (deobfucated #x0000000008a6adf2 #x0000000015e2e706) #x7dfef015dc0f2d00))
(constraint (= (deobfucated #x000000001c0c6d3e #x0000000038d23f03) #x873c6b840697a3c6))
(constraint (= (deobfucated #x00000000227836e2 #x0000000023806c70) #x0271412d9a434340))
(constraint (= (deobfucated #x000000003936c2ed #x000000002a74a866) #x973489fbe3c74be4))
(constraint (= (deobfucated #x00000000336fe881 #x000000000117d6c8) #x3234229503bdf890))
(constraint (= (deobfucated #x0000000039071a3a #x000000000f2da8f8) #xb36bfa8f28a30d20))
(constraint (= (deobfucated #x000000002b663f7c #x000000000e8bf8ba) #x64d77c0223405ab0))
(constraint (= (deobfucated #x000000002e7a0113 #x000000000309f01d) #xc3e2d4f4c52bb3cc))
(check-synth)