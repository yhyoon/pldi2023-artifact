(set-logic BV)

(synth-fun deobfucated ( (a (BitVec 64))  (b (BitVec 64))  ) (BitVec 64)
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
				a b
			)
		)
	)
)

(constraint (= (deobfucated #x0000000028a56aaf #x000000001f6b0018) #x000000002fad0028))
(constraint (= (deobfucated #x0000000035baa48f #x0000000024b60651) #xfffffffffd5a3e53))
(constraint (= (deobfucated #x000000000c4ddb5e #x00000000155bf4a3) #x000000001aac14a7))
(constraint (= (deobfucated #x00000000355ee178 #x00000000393837d3) #xffffffffdf484873))
(constraint (= (deobfucated #x0000000011a19c26 #x000000000e886c1d) #x000000000f887425))
(constraint (= (deobfucated #x000000001c9acaf1 #x000000000868871a) #x00000000187b8b3a))
(constraint (= (deobfucated #x000000001405efa5 #x000000000310ac40) #x000000000311d440))
(constraint (= (deobfucated #x0000000032137c16 #x000000000b8749ee) #x000000001798d9f2))
(constraint (= (deobfucated #x0000000017a0488a #x0000000007eedd1f) #x0000000018112de3))
(constraint (= (deobfucated #x000000001c1c02b1 #x000000002da57772) #x0000000035aa8b92))
(constraint (= (deobfucated #x0000000015aad8df #x000000003b739e7d) #xffffffffddbcee87))
(constraint (= (deobfucated #x000000001b111614 #x000000002b8d8556) #x0000000035939eae))
(constraint (= (deobfucated #x0000000019421306 #x000000002dae2257) #x0000000033d23fab))
(constraint (= (deobfucated #x0000000019963a96 #x0000000031517542) #xffffffffdfb29546))
(constraint (= (deobfucated #x0000000000725e56 #x000000001cd32d96) #xffffffffe36f35ea))
(constraint (= (deobfucated #x0000000028e65650 #x0000000010e7c455) #x000000001f185fb5))
(constraint (= (deobfucated #x00000000071740a1 #x000000002c5fb110) #xffffffffd5a1b110))
(constraint (= (deobfucated #x0000000028bdef68 #x0000000033eb8c92) #xfffffffffc3cb492))
(constraint (= (deobfucated #x000000002954f395 #x0000000011b0fb00) #x000000001fd70500))
(constraint (= (deobfucated #x00000000200fde3e #x00000000361f45a4) #xffffffffc9e1ce6c))
(check-synth)