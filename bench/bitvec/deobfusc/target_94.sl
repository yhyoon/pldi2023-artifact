(set-logic BV)

(synth-fun deobfucated ( (c (BitVec 64))  (d (BitVec 64))  ) (BitVec 64)
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
				c d
			)
		)
	)
)

(constraint (= (deobfucated #x0000000027439197 #x000000002a84fb81) #xf388934d89ebfdd8))
(constraint (= (deobfucated #x000000003a471e1f #x000000002e57d79f) #xf14f3b6012e05c20))
(constraint (= (deobfucated #x0000000002793ceb #x00000000084a73a4) #xfff9cd31bb70a4fc))
(constraint (= (deobfucated #x000000001108231f #x000000000520257e) #xfecce073eb15b880))
(constraint (= (deobfucated #x0000000012b8e51b #x00000000290d0ff0) #xfea0e3aaeef6b000))
(constraint (= (deobfucated #x000000001a3cc74f #x0000000011a915b2) #xfbaafaa89d4e4800))
(constraint (= (deobfucated #x000000002acbbf5f #x0000000016dda1b9) #xf51ce03e05484000))
(constraint (= (deobfucated #x00000000261c2233 #x000000000d98128a) #xf8891ff9884de1a4))
(constraint (= (deobfucated #x0000000004ecb2e2 #x000000001c8c29d8) #xff5b514dd200e4b0))
(constraint (= (deobfucated #x0000000011ec289b #x0000000010ca454c) #xfd9afbcac8e1c4b4))
(constraint (= (deobfucated #x000000001e841932 #x0000000032982b74) #xf83ff35f1669ba38))
(constraint (= (deobfucated #x000000002496a2ee #x0000000005e17fbf) #xf9fbdb2589195d12))
(constraint (= (deobfucated #x0000000030949528 #x000000001fa50265) #xf3d6306789ebe598))
(constraint (= (deobfucated #x0000000011720f30 #x0000000032b42c47) #xfb5d8fc453aa87d0))
(constraint (= (deobfucated #x0000000015ad65fc #x0000000038812dc9) #xfa0ea497742b4a14))
(constraint (= (deobfucated #x0000000025ec225d #x0000000001cb566e) #xfa5738ef0fd404c6))
(constraint (= (deobfucated #x00000000041aca22 #x0000000007e6a2a3) #xffdf245b16a36cd6))
(constraint (= (deobfucated #x000000002f1f8158 #x0000000021ce2a97) #xf13ffcb29f8e9ae8))
(constraint (= (deobfucated #x000000001699a47a #x0000000018ec8596) #xfc8e6708ec0ffc00))
(constraint (= (deobfucated #x0000000011968cd6 #x000000003ab3c425) #xfb4f0f17173824ee))
(check-synth)