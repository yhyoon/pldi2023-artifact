(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (b (BitVec 64))  (c (BitVec 64))  ) (BitVec 64)
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
				e b c
			)
		)
	)
)

(constraint (= (deobfucated #x000000000375388c #x00000000300ba5b7 #x0000000006e2c08e) #xffffffffdff77adf))
(constraint (= (deobfucated #x0000000038807841 #x0000000009ff4a29 #x00000000041c35a2) #xfffffffffe9cffff))
(constraint (= (deobfucated #x0000000001d3ca76 #x00000000356f2b01 #x0000000020b42752) #xffffffffebd7feff))
(constraint (= (deobfucated #x000000002533bc9e #x0000000019c2ba35 #x000000001db6a0f4) #xffffffffe7ffffff))
(constraint (= (deobfucated #x0000000039f970e0 #x000000001ab2d1bf #x00000000206dadff) #xfffffffffdfffee0))
(constraint (= (deobfucated #x00000000100f9f3d #x00000000168370f6 #x000000001df12b1f) #xffffffffff7fbf3d))
(constraint (= (deobfucated #x000000000a55a825 #x0000000001d7cd48 #x000000001d3d21e4) #xffffffffff7dfebf))
(constraint (= (deobfucated #x000000001aa988b7 #x00000000236f5203 #x0000000017b07e52) #xfffffffffef9adff))
(constraint (= (deobfucated #x000000002852208a #x0000000034af2a6c #x000000000891f09f) #xfffffffffbf2f7bb))
(constraint (= (deobfucated #x0000000021298464 #x0000000011742f26 #x000000002a75419b) #xffffffffffabd6fd))
(constraint (= (deobfucated #x00000000133191d0 #x0000000014cd4851 #x000000002b1b418a) #xffffffffff7fffff))
(constraint (= (deobfucated #x00000000300bcf74 #x0000000007023a92 #x0000000003ed6509) #xfffffffffcffef7f))
(constraint (= (deobfucated #x000000001b22227a #x00000000006f80ac #x000000001a37a441) #xfffffffffffa7fff))
(constraint (= (deobfucated #x000000003367bf5a #x00000000234955ec #x0000000023617476) #xffffffffffffbfdb))
(constraint (= (deobfucated #x0000000031f19773 #x000000001a604ee5 #x0000000022044450) #xfffffffff7fff77b))
(constraint (= (deobfucated #x0000000038ecf686 #x0000000014503642 #x0000000014080860) #xffffffffffffffbf))
(constraint (= (deobfucated #x00000000127c5348 #x000000002344bca0 #x00000000152b2c13) #xffffffffffff7f7f))
(constraint (= (deobfucated #x0000000015e83f9e #x0000000007a51d26 #x0000000030478800) #xfffffffffdfaffdf))
(constraint (= (deobfucated #x0000000005a375ad #x000000001ceea317 #x000000001bdf51fb) #xfffffffffff3ffed))
(constraint (= (deobfucated #x00000000345fd187 #x000000001c3e55ac #x0000000018876f76) #xffffffffffdffbdf))
(check-synth)