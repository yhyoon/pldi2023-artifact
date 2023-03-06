(set-logic BV)

(synth-fun deobfucated ( (c (BitVec 64))  (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				c a b
			)
		)
	)
)

(constraint (= (deobfucated #x000000003b2b7efb #x000000001ed5eaf6 #x0000000010ff2224) #xffffffffda016bf3))
(constraint (= (deobfucated #x0000000013d30073 #x000000000ca6322b #x0000000001c91aa4) #xffffffffe08acda8))
(constraint (= (deobfucated #x000000001ad9854c #x0000000032c22866 #x0000000013bf3594) #xffffffffd7e452d6))
(constraint (= (deobfucated #x000000000c7afb80 #x000000003407caf2 #x0000000038b6282d) #xffffffffc782ce8e))
(constraint (= (deobfucated #x0000000021652920 #x0000000029feee02 #x00000000185960d3) #xfffffffff76438de))
(constraint (= (deobfucated #x000000000092fb94 #x000000003b0bb976 #x000000001d7785ab) #xffffffffc466bd1e))
(constraint (= (deobfucated #x000000003115c779 #x000000002878da4d #x000000002c2641e9) #xffffffffe692e2cc))
(constraint (= (deobfucated #x0000000000fe9622 #x00000000067a9a91 #x0000000035bf5bb2) #xfffffffff97bf34d))
(constraint (= (deobfucated #x00000000068207fe #x00000000093b38ac #x00000000210e4c72) #xfffffffff046c0ae))
(constraint (= (deobfucated #x0000000005f42a56 #x000000003022e646 #x000000000233e4b4) #xffffffffca2933f0))
(constraint (= (deobfucated #x000000002bda9b1f #x000000001a6a9bde #x0000000038a94677) #xffffffffce4fff3f))
(constraint (= (deobfucated #x000000000ad25de9 #x00000000300dae81 #x0000000015302056) #xffffffffc5200c98))
(constraint (= (deobfucated #x000000000a751892 #x00000000209fce75 #x0000000002ab6225) #xffffffffd5152919))
(constraint (= (deobfucated #x000000001e6607d5 #x0000000003da1dbc #x0000000015924fff) #xffffffffe243e597))
(constraint (= (deobfucated #x0000000029ca4f0f #x000000003535761e #x00000000195d9faa) #xffffffffe300c6ef))
(constraint (= (deobfucated #x00000000237f9a37 #x0000000032043f48 #x000000002fcf8874) #xffffffffee845a81))
(constraint (= (deobfucated #x000000003b09c968 #x000000001cb9686e #x00000000102bd01a) #xffffffffd84f5efa))
(constraint (= (deobfucated #x000000000067948a #x000000003871a178 #x00000000296fa383) #xffffffffc7e9ca0e))
(constraint (= (deobfucated #x00000000104fc324 #x000000001f543326 #x0000000000f7a018) #xfffffffff0e40ffe))
(constraint (= (deobfucated #x000000002b1b114f #x0000000031791521 #x000000002ffc30ee) #xffffffffe59dfb92))
(check-synth)