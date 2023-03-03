(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (b (BitVec 64))  (d (BitVec 64))  ) (BitVec 64)
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
				a b d
			)
		)
	)
)

(constraint (= (deobfucated #x0000000027f96261 #x0000000009cac2f8 #x000000000f938c57) #xffffffffdf979152))
(constraint (= (deobfucated #x000000000efd8388 #x000000001a5024e1 #x000000003341ec3d) #xffffffffd243b42c))
(constraint (= (deobfucated #x000000001d5a0bb8 #x00000000228f5288 #x000000001ea6fba2) #xffffffffde865fe6))
(constraint (= (deobfucated #x00000000291c9ab5 #x0000000018937170 #x000000000204473d) #xffffffffc4644338))
(constraint (= (deobfucated #x0000000002adb4ad #x0000000006ed26cb #x000000001885f6e2) #xffffffffe197bff3))
(constraint (= (deobfucated #x00000000042374a7 #x000000000527f36b #x000000001a967ae9) #xffffffffe04e72fa))
(constraint (= (deobfucated #x0000000018e87a42 #x0000000023ca9d00 #x00000000138d9310) #xffffffffd79893ae))
(constraint (= (deobfucated #x00000000324c95c4 #x000000000be4b77c #x000000001a4e1425) #xffffffffde5d5c27))
(constraint (= (deobfucated #x000000002e731f32 #x0000000011fe01ed #x000000000bbb66f0) #xffffffffcbbb86f1))
(constraint (= (deobfucated #x0000000025494ec2 #x000000002a3a2c50 #x00000000363d701a) #xffffffffe6b9e138))
(constraint (= (deobfucated #x00000000004a7b9c #x000000002e9fcaf0 #x000000001c59c5de) #xffffffffcd79c1de))
(constraint (= (deobfucated #x000000000900aa18 #x0000000025389098 #x000000001934c354) #xffffffffcbf38634))
(constraint (= (deobfucated #x000000001d61d9c7 #x0000000035162ebf #x000000001c08301f) #xffffffffde803020))
(constraint (= (deobfucated #x00000000230c0056 #x0000000008cd12fd #x000000001b013807) #xffffffffcf33d508))
(constraint (= (deobfucated #x000000002b04f232 #x0000000006df7c2d #x000000002815b2cb) #xfffffffff835b30c))
(constraint (= (deobfucated #x000000001728422b #x0000000004ef8980 #x000000000bf8137a) #xffffffffe3e8272f))
(constraint (= (deobfucated #x000000002036abf0 #x000000000d76b254 #x00000000357cfba2) #xffffffffe7f5bfaa))
(constraint (= (deobfucated #x000000001baa8045 #x0000000028688d50 #x000000001bbcb47d) #xffffffffdfa9c6d8))
(constraint (= (deobfucated #x00000000182dd3a2 #x000000001040b35a #x0000000008cdafa3) #xffffffffef5fa3a7))
(constraint (= (deobfucated #x0000000016ece51f #x000000002041011f #x000000002a153b27) #xffffffffe30721c8))
(check-synth)