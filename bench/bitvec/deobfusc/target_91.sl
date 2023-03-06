(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (d (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				e d b
			)
		)
	)
)

(constraint (= (deobfucated #x000000000ff842f0 #x000000002fd5df9e #x000000000bdb0ce4) #xfda93ef6afe37680))
(constraint (= (deobfucated #x000000002a643f5f #x000000002397d0a5 #x0000000025a924e3) #xf35755374f96474e))
(constraint (= (deobfucated #x0000000014fb49e1 #x000000000db13eb9 #x0000000032348214) #xb14ff1bbb61541c6))
(constraint (= (deobfucated #x000000001fb14850 #x000000001e1db425 #x000000001e41e73a) #x43491f16cc2d4020))
(constraint (= (deobfucated #x000000000d2f936b #x000000002b246d4c #x00000000289ef7b9) #xcf46e6a15ad4e427))
(constraint (= (deobfucated #x000000001fbe8eef #x000000000eef40ce #x0000000021e5e88d) #xf8d744d427388b55))
(constraint (= (deobfucated #x000000003799dd34 #x0000000034883eee #x0000000025efa81e) #xab3499d6d89033e8))
(constraint (= (deobfucated #x0000000011488c79 #x000000000b29eb2a #x000000003588adba) #xf8885425a2c2707e))
(constraint (= (deobfucated #x0000000014518298 #x000000000d6d306a #x000000000f1cc1ff) #xfbb2b0a56b1efa78))
(constraint (= (deobfucated #x000000000ed70325 #x0000000010e2bfbc #x000000001c95da17) #xd00063bfcc4dac47))
(constraint (= (deobfucated #x0000000018c51d8b #x0000000036c31729 #x000000001875f5e8) #x1efa9cb56cd0f21a))
(constraint (= (deobfucated #x00000000211a460b #x0000000019d83052 #x000000002676913a) #x8623ecd2c380011a))
(constraint (= (deobfucated #x0000000009a2b2e8 #x000000002416e7fd #x000000003840eaf4) #x7a5f4d27467e15f0))
(constraint (= (deobfucated #x000000000b6e1217 #x0000000037583c78 #x00000000246f12d9) #x057cc1f9479b3c27))
(constraint (= (deobfucated #x00000000104cc2af #x0000000012732436 #x0000000000862b8d) #xc4d8022633388bcd))
(constraint (= (deobfucated #x0000000030fa6ba4 #x00000000124e4ef7 #x0000000031551f53) #xa13e5ccc4ca272a0))
(constraint (= (deobfucated #x0000000006d2faba #x000000000923a12e #x0000000028c20815) #x67a5feabc807900e))
(constraint (= (deobfucated #x00000000368d7b43 #x0000000000641dd0 #x0000000012a0bcd4) #x60db63ca1241b7dc))
(constraint (= (deobfucated #x00000000281a202f #x0000000028169bd1 #x0000000023d28556) #x355036c39379e7de))
(constraint (= (deobfucated #x0000000025c85494 #x000000002acb7fc6 #x0000000035e66aae) #x3ce0fca62a62f0e8))
(check-synth)