(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (d (BitVec 64))  ) (BitVec 64)
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
				e d
			)
		)
	)
)

(constraint (= (deobfucated #x0000000033042651 #x0000000022d86afe) #x06feb3ed546fbf51))
(constraint (= (deobfucated #x00000000391dddd4 #x000000002ad1bb7d) #x0ff9ffdafa7fff95))
(constraint (= (deobfucated #x000000000b38d313 #x000000001ee0622c) #x03f9fbbfe7ceffbb))
(constraint (= (deobfucated #x000000002732b7cf #x000000003179c4b7) #x0d9ff77ffbf5ffaf))
(constraint (= (deobfucated #x000000002efa9e93 #x0000000024d6a5ed) #x07cdf2b7a6bfb757))
(constraint (= (deobfucated #x00000000020b536f #x0000000013641001) #x017c17ffbf6e736f))
(constraint (= (deobfucated #x000000000fd77ed0 #x000000000b6f1b50) #x00b2bcd7fdf9d54f))
(constraint (= (deobfucated #x00000000123b2e3b #x0000000031c42d4d) #x09afbfaf91b6d677))
(constraint (= (deobfucated #x0000000029667946 #x000000000efc47bc) #x01fbfa75fdbebbdb))
(constraint (= (deobfucated #x00000000148425e8 #x000000001f4b4392) #x03db537ee6bdded5))
(constraint (= (deobfucated #x000000002e5dbc5f #x0000000021ada7b3) #x05ee3b0dff76ffdf))
(constraint (= (deobfucated #x00000000314eec28 #x0000000005e21787) #x003e9e9ade67a0b7))
(constraint (= (deobfucated #x00000000286a7910 #x000000002c5851f0) #x07fe7fabdbf7b3ef))
(constraint (= (deobfucated #x000000000d2bf529 #x0000000003e6263d) #x000fffee2ffe57d5))
(constraint (= (deobfucated #x000000000a050fd5 #x0000000020a66484) #x042a2d47ff6ffdd7))
(constraint (= (deobfucated #x0000000038729e5e #x00000000382e92d7) #x0c74fab7edeecff7))
(constraint (= (deobfucated #x000000001bb687ef #x0000000010f7eda7) #x01dfeffb7ddbd7ff))
(constraint (= (deobfucated #x0000000006af0a0f #x000000002db30c1d) #x083efffd72d3ffe7))
(constraint (= (deobfucated #x0000000008bc701e #x000000002eeae362) #x08dbe37bff3df4fd))
(constraint (= (deobfucated #x00000000064554cc #x00000000089c8304) #x004a3ff57ccddb33))
(check-synth)