(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (d (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				a d b
			)
		)
	)
)

(constraint (= (deobfucated #x000000001c986f27 #x0000000038609d9d #x0000000032ba6f23) #x0000000028400c1c))
(constraint (= (deobfucated #x00000000302a182a #x0000000014c7b760 #x000000000a6cd8ec) #x00000000108916a0))
(constraint (= (deobfucated #x00000000169524e3 #x0000000028ca713c #x000000002e8b9dc5) #x0000000050148258))
(constraint (= (deobfucated #x000000003b75db30 #x0000000009f3397c #x000000001a6d7fc1) #x000000000a9159a8))
(constraint (= (deobfucated #x00000000297950af #x00000000294a86d4 #x00000000307807f7) #x0000000031420d24))
(constraint (= (deobfucated #x0000000016085cca #x000000001c72ae5b #x0000000028981a95) #x000000002c62889d))
(constraint (= (deobfucated #x0000000036522c53 #x000000002a6c7a2b #x0000000024e81992) #x00000000022c900a))
(constraint (= (deobfucated #x000000000cc17851 #x0000000027d24453 #x000000001a627d4a) #x000000000bc44814))
(constraint (= (deobfucated #x0000000020c0e7d0 #x000000003484e903 #x00000000225aff4b) #x000000001080f103))
(constraint (= (deobfucated #x000000000226560f #x000000001ec3abc9 #x000000002e073bb9) #x000000001c814980))
(constraint (= (deobfucated #x000000002db8de50 #x0000000032081ea5 #x00000000190fe7c7) #x0000000040082f09))
(constraint (= (deobfucated #x000000000e6a0219 #x000000001a4822ad #x000000000e7c6b63) #x000000000a484230))
(constraint (= (deobfucated #x0000000033ef4820 #x000000000af04d5e #x00000000307ba2fc) #x000000000d00509e))
(constraint (= (deobfucated #x0000000011ffa17f #x00000000244f8713 #x000000002e87c2bb) #x00000000488f8710))
(constraint (= (deobfucated #x0000000035209139 #x00000000236b4de5 #x000000002beb2009) #x00000000254b0ee4))
(constraint (= (deobfucated #x00000000243178ab #x000000003ab4b9e5 #x000000002597ab0b) #x0000000010b89a60))
(constraint (= (deobfucated #x0000000014f8901a #x00000000093a307e #x0000000013f4ed2d) #x0000000002083086))
(constraint (= (deobfucated #x00000000138e4da3 #x0000000017a16a36 #x000000002e8e2f0c) #x0000000016018c48))
(constraint (= (deobfucated #x0000000032dbc1d8 #x000000001de10936 #x000000001b800dac) #x0000000009a11136))
(constraint (= (deobfucated #x0000000033415467 #x00000000321ac225 #x000000000d383031) #x00000000521ac028))
(check-synth)