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

(constraint (= (deobfucated #x0000000011556a52 #x000000000e0c8b0b) #xff0c7ac45a8d496b))
(constraint (= (deobfucated #x000000002fa8c342 #x0000000032a0a5c5) #xf6932186122681f1))
(constraint (= (deobfucated #x000000001113976e #x00000000340fac44) #xfc86f99981b34a1c))
(constraint (= (deobfucated #x0000000038ba71ba #x000000001f808b60) #xf904f01e84d4d720))
(constraint (= (deobfucated #x00000000136296ca #x000000003580e2b2) #xfbf2d45261d2fdde))
(constraint (= (deobfucated #x0000000003ca16c1 #x000000001b917e94) #xff978842f915a6d8))
(constraint (= (deobfucated #x000000000c09b0c4 #x0000000013766c17) #xff15b654ba3fc245))
(constraint (= (deobfucated #x000000001b3b0506 #x0000000029ffcbbc) #xfb8856bc654cdfa4))
(constraint (= (deobfucated #x000000003ad8d208 #x00000000063829b4) #xfe92020fc000e0ac))
(constraint (= (deobfucated #x000000000c5dcc71 #x0000000026b715a4) #xfe213b8e495b9738))
(constraint (= (deobfucated #x0000000001a7d021 #x0000000016607016) #xffdaf475780add14))
(constraint (= (deobfucated #x0000000006556c8d #x000000002613a97c) #xff0ed55a6b447ec0))
(constraint (= (deobfucated #x000000003410d154 #x0000000009f79d96) #xfdf90c5d342e151a))
(constraint (= (deobfucated #x0000000036e88354 #x0000000003f1e4cc) #xff27647f8879abfc))
(constraint (= (deobfucated #x00000000174d94dd #x000000000d134383) #xfecf4e894ce2b758))
(constraint (= (deobfucated #x000000002991c456 #x0000000039965b9e) #xf6a620ff6e6c6572))
(constraint (= (deobfucated #x000000002749fd80 #x0000000019dc2aa8) #xfc07fc1ce04d8658))
(constraint (= (deobfucated #x000000001948dbfc #x000000001b69c7ad) #xfd4ade316a6f14ff))
(constraint (= (deobfucated #x00000000003fc7c3 #x0000000004c4c3e8) #xfffecfdb2f0725e0))
(constraint (= (deobfucated #x0000000027353123 #x00000000131e10df) #xfd1272891927925a))
(check-synth)