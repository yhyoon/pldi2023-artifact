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

(constraint (= (deobfucated #x00000000033e0650 #x0000000024ff5c93) #x0000000006000c80))
(constraint (= (deobfucated #x000000001dc6e057 #x000000000be15eb6) #xfffffffff83dc0be))
(constraint (= (deobfucated #x000000002b534060 #x00000000132dbf76) #xffffffffdfa48000))
(constraint (= (deobfucated #x0000000004e8bcd1 #x0000000021cce4d1) #x0000000039c07000))
(constraint (= (deobfucated #x000000002d516e24 #x00000000222e2346) #xfffffffffba3f840))
(constraint (= (deobfucated #x00000000234a5e7f #x000000001c16cd8b) #xffffffffc790fcf8))
(constraint (= (deobfucated #x00000000205e774e #x000000002ee0470a) #x00000000003ffff8))
(constraint (= (deobfucated #x0000000017a43c8a #x000000002126b732) #x000000003f00f110))
(constraint (= (deobfucated #x000000002e0cb733 #x000000001bf79aa8) #xffffffffd811ceee))
(constraint (= (deobfucated #x000000002e263478 #x00000000089ab3c4) #xfffffffffcc8f8f0))
(constraint (= (deobfucated #x00000000396245ab #x000000002a7f1f1c) #xffffffffe20183c6))
(constraint (= (deobfucated #x0000000033174fb7 #x00000000391fec23) #x000000000c003ff8))
(constraint (= (deobfucated #x000000003adb4e02 #x0000000003f0bc37) #xfffffffff03e9c00))
(constraint (= (deobfucated #x000000002897add5 #x000000000d29f867) #xffffffffc12c1f20))
(constraint (= (deobfucated #x0000000015d866b8 #x0000000037ce38f9) #x0000000003e38c00))
(constraint (= (deobfucated #x000000000ffdc20c #x0000000035781334) #x000000001fff8010))
(constraint (= (deobfucated #x000000002a4bab6f #x0000000022c80369) #xfffffffff0fffffc))
(constraint (= (deobfucated #x0000000008411b2e #x000000001f1d1572) #x000000000187f418))
(constraint (= (deobfucated #x0000000011644c58 #x000000003488b54d) #x0000000006c891e0))
(constraint (= (deobfucated #x000000001e7c5be5 #x000000002d213ad4) #x000000003df9bfde))
(check-synth)