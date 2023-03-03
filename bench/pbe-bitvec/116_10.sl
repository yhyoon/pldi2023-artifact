(set-logic BV)
(synth-fun f ( (x (BitVec 64)) ) (BitVec 64)
((Start (BitVec 64)
((bvnot Start)
(bvxor Start Start)
(bvand Start Start)
(bvor Start Start)
(bvneg Start)
(bvadd Start Start)
(bvmul Start Start)
(bvudiv Start Start)
(bvurem Start Start)
(bvlshr Start Start)
(bvashr Start Start)
(bvshl Start Start)
(bvsdiv Start Start)
(bvsrem Start Start)
(bvsub Start Start)
x
#x0000000000000000
#x0000000000000001
#x0000000000000002
#x0000000000000003
#x0000000000000004
#x0000000000000005
#x0000000000000006
#x0000000000000007
#x0000000000000008
#x0000000000000009
#x0000000000000009
#x0000000000000009
#x000000000000000A
#x000000000000000B
#x000000000000000C
#x000000000000000D
#x000000000000000E
#x000000000000000F
#x0000000000000010
(ite StartBool Start Start)
))
(StartBool Bool
((= Start Start)
(not StartBool)
(and StartBool StartBool)
(or StartBool StartBool)
))))
(constraint (= (f #x44ccce634ace1b4a) #x09999cc6959c3694))
(constraint (= (f #xa8156b111c178b62) #x0001502ad622382e))
(constraint (= (f #xa6e07852e989c07e) #x00014dc0f0a5d312))
(constraint (= (f #x1127052aee98853e) #x224e0a55dd310a7c))
(constraint (= (f #x84a5e15c77ce2ca0) #x094bc2b8ef9c5940))
(constraint (= (f #x609844195a9e8761) #x0000c1308832b53c))
(constraint (= (f #x3ee4c84a6aa90298) #x00007dc99094d552))
(constraint (= (f #xed8b1e372e1b98dd) #x0001db163c6e5c36))
(constraint (= (f #x437473a7e33042ee) #x06e8e74fc66085dc))
(constraint (= (f #x69dd4e35a0e80909) #x0000d3ba9c6b41d0))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvurem x #x0000000000000003) #x0000000000000000) (ite (= (bvand #x0000000000000001 x) #x0000000000000000) (ite (= (bvand #x0000000000000010 x) #x0000000000000000) (bvudiv (bvmul #x0000000000000004 x) #x0000000000000002) (bvlshr x #x000000000000000f)) (bvlshr x #x000000000000000f)) (ite (= (bvor #x000000000000000a x) x) (ite (= (bvurem x #x0000000000000005) #x0000000000000000) (bvnot (bvneg (bvlshr x #x000000000000000f))) (bvudiv (bvmul #x0000000000000004 x) #x0000000000000002)) (bvnot (bvneg (bvlshr x #x000000000000000f))))))
