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

(constraint (= (deobfucated #x0000000030384d10 #x0000000020252065) #x03090fcfbd10c78f))
(constraint (= (deobfucated #x0000000017ba323b #x0000000026a7bf8b) #x048d60d69413f78f))
(constraint (= (deobfucated #x000000001ba44e6a #x00000000222237b7) #x06361a9f2b63a47d))
(constraint (= (deobfucated #x00000000159fc394 #x000000002b9f9a35) #x053cb8effb4743eb))
(constraint (= (deobfucated #x0000000038eb4fb6 #x00000000294b73eb) #x03eb40c8bbd45ad9))
(constraint (= (deobfucated #x00000000010dd719 #x000000001ce669e3) #x001f89db65d35b65))
(constraint (= (deobfucated #x000000002df7ccb8 #x000000000c4f95f6) #x060e0b87fbd357ef))
(constraint (= (deobfucated #x000000001189f6a2 #x000000003071c81a) #x0253cabd9313704f))
(constraint (= (deobfucated #x000000001c58bdbe #x00000000368d7037) #x04be3bb9397a3041))
(constraint (= (deobfucated #x00000000105e3b10 #x00000000162a094f) #x0069a34d91bd08ef))
(constraint (= (deobfucated #x00000000275bcd5d #x0000000011724219) #x0853c10c3dfe7f83))
(constraint (= (deobfucated #x000000000ddab49a #x0000000028f73f86) #x0203131334e120d7))
(constraint (= (deobfucated #x000000001629715e #x0000000017f3413d) #x00290cec30927721))
(constraint (= (deobfucated #x0000000029c69126 #x000000002eff821a) #x012dbe519d39d6d7))
(constraint (= (deobfucated #x000000003608162c #x000000001eb54bff) #x08993b3c86cbbdbb))
(constraint (= (deobfucated #x00000000133fd233 #x0000000014c02576) #x0099fde961cf923e))
(constraint (= (deobfucated #x000000000f1662a3 #x00000000354f0186) #x037056f8ecf2488e))
(constraint (= (deobfucated #x000000000a0e44de #x0000000031ddb101) #x02599d4a14af7361))
(constraint (= (deobfucated #x00000000282b87a4 #x000000000bd18da7) #x05a52fa009f4fce3))
(constraint (= (deobfucated #x000000001cbdff9f #x0000000038c1500e) #x0418b7b0255f7a0e))
(check-synth)