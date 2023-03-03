(set-logic BV)

(synth-fun deobfucated ( (c (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				c b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000019aafebe #x00000000048939c0) #xffffffffc3978f03))
(constraint (= (deobfucated #x000000000f23b8af #x00000000362e2f4a) #xffffffff755c300d))
(constraint (= (deobfucated #x000000001226dc03 #x0000000017aacd3f) #xffffffffac5cad7b))
(constraint (= (deobfucated #x00000000209d642e #x0000000005ee6a00) #xffffffffb2e863a3))
(constraint (= (deobfucated #x00000000275d0787 #x000000002cf9b2cc) #xffffffff57528b59))
(constraint (= (deobfucated #x00000000145d3900 #x0000000037a9f287) #xffffffff67f1a8f1))
(constraint (= (deobfucated #x0000000000c2c607 #x000000000f251dcf) #xffffffffe0303853))
(constraint (= (deobfucated #x000000001cbbb92a #x000000000979402f) #xffffffffb3960d4d))
(constraint (= (deobfucated #x00000000322d8b5b #x00000000183c01b1) #xffffffff6b2ce5e7))
(constraint (= (deobfucated #x000000001d41679f #x0000000031d80930) #xffffffff61cd1e61))
(constraint (= (deobfucated #x000000002ba421de #x0000000016b85865) #xffffffff7b470b79))
(constraint (= (deobfucated #x00000000006bac2c #x000000000f47783f) #xffffffffe099b729))
(constraint (= (deobfucated #x000000000d77b8ad #x000000000c52a658) #xffffffffcc6b41f5))
(constraint (= (deobfucated #x00000000225c2b78 #x000000000eecdc83) #xffffffff9d6df009))
(constraint (= (deobfucated #x000000002be6b50b #x000000001ba0031b) #xffffffff70f28fb3))
(constraint (= (deobfucated #x000000003a8bc79c #x000000003b1f450b) #xffffffff14a9e6b1))
(constraint (= (deobfucated #x000000002af40e9e #x000000003812eb18) #xffffffff39f20c93))
(constraint (= (deobfucated #x0000000001c8bd4c #x000000003aad8b62) #xffffffff87136ea3))
(constraint (= (deobfucated #x0000000017deac85 #x000000000f7e9ef6) #xffffffffb1456909))
(constraint (= (deobfucated #x00000000326f2561 #x0000000019816531) #xffffffff681eeadb))
(check-synth)