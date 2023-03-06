(set-logic BV)

(synth-fun deobfucated ( (e (BitVec 64))  (a (BitVec 64))  ) (BitVec 64)
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
				e a
			)
		)
	)
)

(constraint (= (deobfucated #x00000000255e9d06 #x0000000022fd6bc0) #xffffffffe2052846))
(constraint (= (deobfucated #x00000000175b10f7 #x000000002783c457) #xffffffffe8d44c49))
(constraint (= (deobfucated #x000000000d2d2b35 #x000000002f92d943) #xffffffffd09a48f1))
(constraint (= (deobfucated #x0000000025f585d2 #x00000000053ba76a) #x000000001b885926))
(constraint (= (deobfucated #x0000000019d4e482 #x00000000332e4f5c) #xffffffffd5a25126))
(constraint (= (deobfucated #x000000000480d0fb #x000000002b0470c3) #xffffffffd97c0f75))
(constraint (= (deobfucated #x000000000e1b3c12 #x00000000221ac833) #xffffffffe9e66bcd))
(constraint (= (deobfucated #x0000000033460249 #x000000002ad181fa) #xffffffffe6348007))
(constraint (= (deobfucated #x0000000007b85bc2 #x0000000015908794) #xffffffffec97d0ae))
(constraint (= (deobfucated #x000000002766d848 #x00000000187ccd01) #x000000000e854347))
(constraint (= (deobfucated #x0000000000b63dbc #x0000000023d58407) #xffffffffdc4cb5b1))
(constraint (= (deobfucated #x00000000284aee20 #x0000000000df771b) #x0000000027211105))
(constraint (= (deobfucated #x00000000354ddbd0 #x000000000f0fc22a) #x00000000213057a6))
(constraint (= (deobfucated #x000000002ea698d3 #x0000000002d99961) #x00000000294c6731))
(constraint (= (deobfucated #x000000001e9398b8 #x0000000021fb3517) #xfffffffffc055391))
(constraint (= (deobfucated #x000000002e5aa14b #x000000002d45f47c) #xffffffffd4d40c87))
(constraint (= (deobfucated #x0000000009e406e1 #x000000002ab6ce5e) #xffffffffd6893243))
(constraint (= (deobfucated #x00000000078621a7 #x00000000070b1b34) #xfffffffff979054f))
(constraint (= (deobfucated #x00000000317eb789 #x00000000299af2f4) #xffffffffe6c91215))
(constraint (= (deobfucated #x000000002f6c8e66 #x000000000a6eb8a9) #x000000001a914d9d))
(check-synth)