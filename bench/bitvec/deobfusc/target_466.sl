(set-logic BV)

(synth-fun deobfucated ( (d (BitVec 64))  ) (BitVec 64)
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
				d
			)
		)
	)
)

(constraint (= (deobfucated #x0000000012903d78) #xffffffffdadf8517))
(constraint (= (deobfucated #x0000000012485534) #xffffffffdb6f559b))
(constraint (= (deobfucated #x000000002bd88cfb) #xffffffffa84ee60a))
(constraint (= (deobfucated #x00000000248a7795) #xffffffffb6eb10d6))
(constraint (= (deobfucated #x000000002b3c9035) #xffffffffa986df96))
(constraint (= (deobfucated #x0000000004702ce2) #xfffffffff71fa63d))
(constraint (= (deobfucated #x000000000eae3601) #xffffffffe2a393fe))
(constraint (= (deobfucated #x000000001e9ac36b) #xffffffffc2ca792a))
(constraint (= (deobfucated #x00000000279bf294) #xffffffffb0c81adb))
(constraint (= (deobfucated #x0000000029bab389) #xffffffffac8a98ee))
(constraint (= (deobfucated #x000000003af51389) #xffffffff8a15d8ee))
(constraint (= (deobfucated #x0000000016eb4f4b) #xffffffffd229616a))
(constraint (= (deobfucated #x00000000242b1161) #xffffffffb7a9dd3e))
(constraint (= (deobfucated #x00000000042e7247) #xfffffffff7a31b72))
(constraint (= (deobfucated #x0000000026d725f3) #xffffffffb251b41a))
(constraint (= (deobfucated #x000000003b01cddd) #xffffffff89fc6446))
(constraint (= (deobfucated #x000000002c8921d8) #xffffffffa6edbc57))
(constraint (= (deobfucated #x000000002349536a) #xffffffffb96d592d))
(constraint (= (deobfucated #x000000000f55d2c5) #xffffffffe1545a76))
(constraint (= (deobfucated #x0000000005241f0a) #xfffffffff5b7c1ed))
(check-synth)