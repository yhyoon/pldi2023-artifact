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
(constraint (= (f #x3FE01E3BD0981E21) #x7FC03C77A1303C42))
(constraint (= (f #x3B3160E3EEDA87FE) #x7662C1C7DDB50FFC))
(constraint (= (f #xD5D12DC4A8992107) #xABA25B895132420E))
(constraint (= (f #x9836071034DEB823) #x306C0E2069BD7046))
(constraint (= (f #x8A451D9CA8D7680D) #x148A3B3951AED01A))
(constraint (= (f #x7B931830F161F6E2) #x7B931830F161F6E2))
(constraint (= (f #xE9881CB8B56BA3F4) #xE9881CB8B56BA3F4))
(constraint (= (f #xE6D68AAFD4CCA2B4) #xE6D68AAFD4CCA2B4))
(constraint (= (f #xAC8C14BE7D816052) #xAC8C14BE7D816052))
(constraint (= (f #xEC006761DEA19E5B) #xEC006761DEA19E5B))
(constraint (= (f #x0000000000015E53) #x0000000000015E53))
(constraint (= (f #x000000000001BCF8) #x000000000001BCF8))
(constraint (= (f #x0000000000011931) #x0000000000011931))
(constraint (= (f #x00000000000162A4) #x00000000000162A4))
(constraint (= (f #x000000000001831E) #x000000000001831E))
(constraint (= (f #x292B8CAA59FB5B5B) #x52571954B3F6B6B6))
(constraint (= (f #xC58EAB3F499D7CFD) #x8B1D567E933AF9FA))
(constraint (= (f #x8D0BEF08DC7A7D11) #x1A17DE11B8F4FA22))
(constraint (= (f #x72453B4635A17AC6) #x72453B4635A17AC6))
(constraint (= (f #x8901288CF6F457E9) #x12025119EDE8AFD2))
(constraint (= (f #xB6A4A1C364EF2129) #xB6A4A1C364EF2129))
(constraint (= (f #x149BA0D929D1F296) #x293741B253A3E52C))
(constraint (= (f #x8820101A4FE24673) #x8820101A4FE24673))
(constraint (= (f #x2514F9079255D31A) #x4A29F20F24ABA634))
(constraint (= (f #x48CDAC9ED87CCFB5) #x919B593DB0F99F6A))
(constraint (= (f #xB9D002A054FFB531) #x73A00540A9FF6A62))
(constraint (= (f #xFBD59DA7590B9356) #xFBD59DA7590B9356))
(constraint (= (f #x000000000001D0E4) #x000000000001D0E4))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvand #x0000000000000003 x) #x0000000000000000) x (ite (= (bvor #x0000000000000005 x) x) (bvadd x x) (ite (= (bvurem x #x0000000000000005) #x0000000000000000) x (ite (= (bvand #x0000000000000006 x) #x0000000000000000) (bvadd x x) (ite (= (bvurem x #x0000000000000003) #x0000000000000000) (ite (= (bvor #x0000000000000004 x) x) (ite (= (bvor #x000000000000000e x) x) x (ite (= (bvand #x0000000000000010 x) #x0000000000000000) x (bvadd x x))) x) (ite (= (bvor #x0000000000000008 x) x) (bvadd x x) (ite (= (bvand #x0000000000000010 x) #x0000000000000000) (bvadd x x) x))))))))
