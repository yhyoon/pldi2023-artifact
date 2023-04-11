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
(constraint (= (f #x8337BA7D7971EF0E) #x8B04C1DAAEE6F1FE))
(constraint (= (f #xEC642CACCD070F3C) #xE2A26E6601D77FCF))
(constraint (= (f #xACF791FBE86120C0) #xA638E8E456E732CC))
(constraint (= (f #x079A03999B889B4A) #x07E3A3A0023012FE))
(constraint (= (f #x0006AFED60068CDE) #x0006C513B606E413))
(constraint (= (f #x1482DB43B028555F) #x1482DB43B028555F))
(constraint (= (f #x9EF151239C2207ED) #x9EF151239C2207ED))
(constraint (= (f #xF10C929D9290EAF7) #xF10C929D9290EAF7))
(constraint (= (f #xB85327C2C44F710F) #xB85327C2C44F710F))
(constraint (= (f #xC13ED4C7F036CCAF) #xC13ED4C7F036CCAF))
(constraint (= (f #x0000000000000001) #x0000000000000001))
(constraint (= (f #xF5B4E38D3EF588CF) #xF5B4E38D3EF588CF))
(constraint (= (f #x648181EFDFA7E0E1) #x648181EFDFA7E0E1))
(constraint (= (f #xEE0880A63CE2E108) #xE0E808AC5F2CCF18))
(constraint (= (f #x8119B5D5CB151D41) #x8119B5D5CB151D41))
(constraint (= (f #xE30260BF85BA4AC2) #xED3246B47DE1EE6E))
(constraint (= (f #x1AF55E750CFBD85E) #x1B5A0B925C3465DB))
(constraint (= (f #x7480743654565887) #x7480743654565887))
(constraint (= (f #xA6B12AAAB9F90FCC) #xACDA380012669F30))
(constraint (= (f #x23AAF6128484FF5E) #x21905973ACCCB0AB))
(constraint (= (f #x8B5B1D7F28E352B8) #x83EEACA8DA6D6793))
(constraint (= (f #x0000000000000001) #x0000000000000001))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvor #x0000000000000001 x) x) x (bvxor (bvudiv x #x0000000000000010) x)))