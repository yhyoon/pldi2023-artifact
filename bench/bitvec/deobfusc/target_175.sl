(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (e (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				a e b
			)
		)
	)
)

(constraint (= (deobfucated #x000000002996dba3 #x000000001e97b9fc #x00000000198d556e) #xffffffffd7fb64dd))
(constraint (= (deobfucated #x00000000377fa29a #x0000000021db339a #x00000000010518b5) #xffffffffebe57d66))
(constraint (= (deobfucated #x0000000024d065bb #x000000002b7a8535 #x000000002f5302a0) #xffffffffdb2f9a75))
(constraint (= (deobfucated #x0000000013e235d9 #x0000000038d9f9b2 #x0000000021630644) #xffffffffffbdce3f))
(constraint (= (deobfucated #x000000000fea276c #x0000000038fcdc49 #x0000000022265e17) #xfffffffffd5dd8f7))
(constraint (= (deobfucated #x0000000034426741 #x00000000199d30fd #x00000000358e31ce) #xffffffffcfbd9cbf))
(constraint (= (deobfucated #x0000000025f988d0 #x0000000009bf9c88 #x0000000024c8bb53) #xffffffffdb57773e))
(constraint (= (deobfucated #x000000001df1416b #x0000000038b462e6 #x0000000002e8b136) #xfffffffffe8fffd7))
(constraint (= (deobfucated #x0000000036b6ef4b #x0000000006b95417 #x0000000004fe6001) #xffffffffd9ff14bd))
(constraint (= (deobfucated #x00000000218cefb3 #x0000000001dde9b6 #x0000000029ad317d) #xffffffffdf7b5cfd))
(constraint (= (deobfucated #x000000002f57aa6b #x0000000017ecf0b3 #x00000000044ecef6) #xfffffffff0aadf9f))
(constraint (= (deobfucated #x000000001a488847 #x0000000009060640 #x00000000380828aa) #xfffffffffdb777bd))
(constraint (= (deobfucated #x00000000091372c4 #x000000002843cb4c #x000000002db20f5f) #xfffffffff7efef3e))
(constraint (= (deobfucated #x0000000029378b78 #x0000000018ac0f67 #x00000000383f5ac9) #xffffffffdfeaf4f9))
(constraint (= (deobfucated #x000000000dbe93a7 #x000000002050387b #x000000000171cc04) #xfffffffff373fcdb))
(constraint (= (deobfucated #x000000001b0f1609 #x0000000027837382 #x000000001d334906) #xffffffffe5faedff))
(constraint (= (deobfucated #x000000000ff7d8ef #x000000003af85109 #x000000003763d490) #xfffffffff9bfff39))
(constraint (= (deobfucated #x000000002e15f820 #x00000000287965d1 #x000000001d76658a) #xfffffffff3ee37e5))
(constraint (= (deobfucated #x0000000037bc7520 #x0000000028c440e2 #x0000000007099152) #xfffffffffed7ebe6))
(constraint (= (deobfucated #x000000002e579886 #x00000000012f505e #x000000000e379094) #xffffffffddbe77fe))
(check-synth)