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

(constraint (= (deobfucated #x0000000025f336c7 #x000000000fa245f1 #x000000000aad6605) #x00000000359f7ffc))
(constraint (= (deobfucated #x000000001647ff57 #x000000000e40efcc #x000000002415b029) #x000000002eddffe7))
(constraint (= (deobfucated #x0000000014ae71d6 #x000000002ad3c510 #x0000000016166414) #x000000003fc7b7e6))
(constraint (= (deobfucated #x0000000028930cfb #x00000000106dff50 #x0000000005edf804) #x000000003d810f5f))
(constraint (= (deobfucated #x000000002868bc0e #x00000000352457e7 #x000000002db854ca) #x000000005d9d13fd))
(constraint (= (deobfucated #x0000000006b76559 #x000000000142d2cd #x00000000164313ba) #x0000000017fbf977))
(constraint (= (deobfucated #x000000000e86b881 #x0000000001fb03ff #x000000000e0d327e) #x000000001ff7bd81))
(constraint (= (deobfucated #x000000000c5538f0 #x0000000019628aaa #x000000002e459891) #x0000000037b7d3bb))
(constraint (= (deobfucated #x000000001ce1b773 #x000000000ab3b89d #x000000002497257f) #x000000002fb5fdf2))
(constraint (= (deobfucated #x0000000039c17e6f #x0000000020e9038e #x00000000176f4cc9) #x000000007faecfff))
(constraint (= (deobfucated #x000000001b7b5ec1 #x0000000021b1a147 #x000000001f236389) #x000000003fbfc2ce))
(constraint (= (deobfucated #x0000000026c879ff #x00000000153cb6c5 #x00000000347d5171) #x000000003d45f7f4))
(constraint (= (deobfucated #x0000000015115197 #x0000000020d4776a #x000000000878e42b) #x000000003deddb41))
(constraint (= (deobfucated #x0000000021e36153 #x0000000022befabe #x000000003b1c203e) #x000000005da2de91))
(constraint (= (deobfucated #x000000001e4779a0 #x0000000038e94b21 #x000000000a5ebc12) #x0000000077b7f7f3))
(constraint (= (deobfucated #x000000002cf66c75 #x0000000012a1fb85 #x00000000078caf9a) #x000000003fbd77ff))
(constraint (= (deobfucated #x0000000033d28d2b #x000000002c25f143 #x000000002ec55869) #x000000005ff8ff6e))
(constraint (= (deobfucated #x0000000003ad9352 #x0000000016354914 #x0000000003127fc3) #x000000001de7fef7))
(constraint (= (deobfucated #x000000003779d97d #x0000000038fcf549 #x000000000ced922a) #x000000007477efe7))
(constraint (= (deobfucated #x000000002a2f79ee #x000000003a789808 #x000000001d6dc0b9) #x0000000067bd59f7))
(check-synth)