(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				e b
			)
		)
	)
)

(constraint (= (deobfucated #x000000002cc9d208 #x000000001a6a20cc) #x000000001a6a20cd))
(constraint (= (deobfucated #x0000000025bf00ba #x000000001598c9b4) #x000000001598c9b5))
(constraint (= (deobfucated #x00000000038e7c94 #x0000000037b4c0c1) #x0000000037b4c0c2))
(constraint (= (deobfucated #x0000000009d1cd42 #x00000000235168ad) #x00000000235168ae))
(constraint (= (deobfucated #x000000000bcb034d #x000000002a087626) #x000000002a087627))
(constraint (= (deobfucated #x000000001b5681a6 #x00000000136b854b) #x00000000136b854c))
(constraint (= (deobfucated #x00000000294c791b #x0000000021e68a5f) #x0000000021e68a60))
(constraint (= (deobfucated #x0000000020090c91 #x000000001799493a) #x000000001799493b))
(constraint (= (deobfucated #x0000000010aa3334 #x000000001c5535ef) #x000000001c5535f0))
(constraint (= (deobfucated #x00000000227fb316 #x000000001f28c618) #x000000001f28c619))
(constraint (= (deobfucated #x000000002ccf526b #x000000000c247503) #x000000000c247504))
(constraint (= (deobfucated #x000000002b6cf585 #x00000000290bb39c) #x00000000290bb39d))
(constraint (= (deobfucated #x00000000173c203b #x0000000019694a4b) #x0000000019694a4c))
(constraint (= (deobfucated #x0000000009317196 #x0000000015438f9a) #x0000000015438f9b))
(constraint (= (deobfucated #x0000000001ed1689 #x000000000fd97e39) #x000000000fd97e3a))
(constraint (= (deobfucated #x000000002f110f49 #x000000001651f76a) #x000000001651f76b))
(constraint (= (deobfucated #x0000000032d44f35 #x000000002ff5ced7) #x000000002ff5ced8))
(constraint (= (deobfucated #x000000001379cde9 #x000000001d9d0eda) #x000000001d9d0edb))
(constraint (= (deobfucated #x000000001a113b59 #x000000001b7b7fe5) #x000000001b7b7fe6))
(constraint (= (deobfucated #x000000002c35c148 #x0000000037ad8c37) #x0000000037ad8c38))
(check-synth)