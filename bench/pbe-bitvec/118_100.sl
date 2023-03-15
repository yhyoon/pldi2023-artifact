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
(constraint (= (f #x7e4072c221ee7eee) #xfc80e58443dcfddc))
(constraint (= (f #xab77666b3c44a820) #x000000ab77666b3c))
(constraint (= (f #x7722c39a84437c67) #x0000007722c39a84))
(constraint (= (f #x11e25602ed04e6a8) #x00000011e25602ed))
(constraint (= (f #x1972bc926a48285b) #x0000001972bc926a))
(constraint (= (f #x0e803ee44e2ddc8e) #x1d007dc89c5bb91c))
(constraint (= (f #xc98c57585e8267be) #x9318aeb0bd04cf7c))
(constraint (= (f #x473d4b07d15adeca) #x8e7a960fa2b5bd94))
(constraint (= (f #x36c5d97958e8cde4) #x00000036c5d97958))
(constraint (= (f #xa3bebed8a8947e4a) #x477d7db15128fc94))
(constraint (= (f #x36ec85a2db43d282) #x6dd90b45b687a504))
(constraint (= (f #xe2bb916aed5e5711) #xc57722d5dabcae20))
(constraint (= (f #xbac314579d272dc1) #x758628af3a4e5b80))
(constraint (= (f #xd5a78c58ac68173a) #xab4f18b158d02e74))
(constraint (= (f #x3a863b09e5eb6350) #x0000003a863b09e5))
(constraint (= (f #x10e6e7abe46a1bed) #x21cdcf57c8d437d8))
(constraint (= (f #x75c3cc3c1ea34a2c) #x00000075c3cc3c1e))
(constraint (= (f #x329ab0a82ac2edde) #x653561505585dbbc))
(constraint (= (f #xeaccc6e285b398b1) #xd5998dc50b673160))
(constraint (= (f #xc627e2b76cdacb48) #x000000c627e2b76c))
(constraint (= (f #x321a1ebbc95eb438) #x000000321a1ebbc9))
(constraint (= (f #xe728ebcc0ad4a928) #x000000e728ebcc0a))
(constraint (= (f #x57b900ad9c131ce4) #x00000057b900ad9c))
(constraint (= (f #x56566ad1539e6065) #xacacd5a2a73cc0c8))
(constraint (= (f #x9c25c65716168921) #x384b8cae2c2d1240))
(constraint (= (f #x09e67cee03ee29da) #x13ccf9dc07dc53b4))
(constraint (= (f #x230086402c7c750c) #x000000230086402c))
(constraint (= (f #xc1e5a2ed2b2bb4ab) #x000000c1e5a2ed2b))
(constraint (= (f #xde920054eb76ce80) #x000000de920054eb))
(constraint (= (f #xe5e3e9ee1ae3b74c) #x000000e5e3e9ee1a))
(constraint (= (f #x404ce67b342651d3) #x000000404ce67b34))
(constraint (= (f #x163eb4c23d5c128b) #x000000163eb4c23d))
(constraint (= (f #xee7ebde3e6a7b670) #x000000ee7ebde3e6))
(constraint (= (f #x10793ee42cc1318a) #x20f27dc859826314))
(constraint (= (f #xc878961935de07bc) #x000000c878961935))
(constraint (= (f #x13224a2607ddadeb) #x00000013224a2607))
(constraint (= (f #x35e2b75e8289ee8c) #x00000035e2b75e82))
(constraint (= (f #x2852ad2eacadb9e0) #x0000002852ad2eac))
(constraint (= (f #x680c296ea06bd8e1) #xd01852dd40d7b1c0))
(constraint (= (f #xbad06a9d69eb1ae8) #x000000bad06a9d69))
(constraint (= (f #xbad455256a6e2a00) #x000000bad455256a))
(constraint (= (f #x87e3ca1e33cec7cc) #x00000087e3ca1e33))
(constraint (= (f #x399eaa7a394e6272) #x733d54f4729cc4e4))
(constraint (= (f #xbba8c48dcba4ea4e) #x7751891b9749d49c))
(constraint (= (f #x7794989281218e2c) #x0000007794989281))
(constraint (= (f #x70e4ed86beaa1980) #x00000070e4ed86be))
(constraint (= (f #xd3d4ea72e4bd515b) #x000000d3d4ea72e4))
(constraint (= (f #x18d7e0a4c6cdc7e0) #x00000018d7e0a4c6))
(constraint (= (f #x8da82b6ce5683ea0) #x0000008da82b6ce5))
(constraint (= (f #xe1edc51e46a961e0) #x000000e1edc51e46))
(constraint (= (f #x1ed7a9a505ad3622) #x3daf534a0b5a6c44))
(constraint (= (f #x79e365708b5653ee) #xf3c6cae116aca7dc))
(constraint (= (f #x9d15325ad62040e7) #x0000009d15325ad6))
(constraint (= (f #xeb23be8247dccdb5) #xd6477d048fb99b68))
(constraint (= (f #x842b59b954eb40ed) #x0856b372a9d681d8))
(constraint (= (f #x6ace8b1ccc71298e) #xd59d163998e2531c))
(constraint (= (f #x3eeb73a8792a0680) #x0000003eeb73a879))
(constraint (= (f #xc4157aa30cd0708e) #x882af54619a0e11c))
(constraint (= (f #x411aec0ba8a1e900) #x000000411aec0ba8))
(constraint (= (f #x6a432db75280b66e) #xd4865b6ea5016cdc))
(constraint (= (f #xe2d9513ed31317ee) #xc5b2a27da6262fdc))
(constraint (= (f #x6391793843030d47) #x0000006391793843))
(constraint (= (f #x8415d2ae27d63d32) #x082ba55c4fac7a64))
(constraint (= (f #x0cc2ec9ae144b395) #x1985d935c2896728))
(constraint (= (f #x22ea6671bc78a6ec) #x00000022ea6671bc))
(constraint (= (f #x6464608de14dd7ed) #xc8c8c11bc29bafd8))
(constraint (= (f #xe704e2e269c1e762) #xce09c5c4d383cec4))
(constraint (= (f #xcd49da161895e99e) #x9a93b42c312bd33c))
(constraint (= (f #x35cdcc914d243960) #x00000035cdcc914d))
(constraint (= (f #xb9aeaad0bd5d9994) #x000000b9aeaad0bd))
(constraint (= (f #x5451d846e0c6a490) #x0000005451d846e0))
(constraint (= (f #x9a30e11a6cd85e6a) #x3461c234d9b0bcd4))
(constraint (= (f #x0abe824d5c56ecec) #x0000000abe824d5c))
(constraint (= (f #x8a74db814ebd6639) #x14e9b7029d7acc70))
(constraint (= (f #x89a35e17a9ec86b8) #x00000089a35e17a9))
(constraint (= (f #x01e7952233e569ed) #x03cf2a4467cad3d8))
(constraint (= (f #xee6660460eaaac66) #xdcccc08c1d5558cc))
(constraint (= (f #x34cd315624014700) #x00000034cd315624))
(constraint (= (f #xb41b884b92d2e502) #x6837109725a5ca04))
(constraint (= (f #x13715d92bc69edd0) #x00000013715d92bc))
(constraint (= (f #xbe1bee6383d3ca73) #x000000be1bee6383))
(constraint (= (f #x666e7d16c0161170) #x000000666e7d16c0))
(constraint (= (f #x77066d6c01c457c9) #xee0cdad80388af90))
(constraint (= (f #xeb01901bb1ec6697) #x000000eb01901bb1))
(constraint (= (f #x1ecb028b0e3e48ce) #x3d9605161c7c919c))
(constraint (= (f #x7c262ae96d23e177) #x0000007c262ae96d))
(constraint (= (f #xa0289a184921c3e5) #x40513430924387c8))
(constraint (= (f #xbee1453a3ead2851) #x7dc28a747d5a50a0))
(constraint (= (f #x535531c964aec21e) #xa6aa6392c95d843c))
(constraint (= (f #xd9b9c35a8be2335a) #xb37386b517c466b4))
(constraint (= (f #x00ad0e8c154e9a13) #x00000000ad0e8c15))
(constraint (= (f #xe5314ade274eedea) #xca6295bc4e9ddbd4))
(constraint (= (f #xbe30e12e531c48c0) #x000000be30e12e53))
(constraint (= (f #x36e68ddae3abbeb6) #x6dcd1bb5c7577d6c))
(constraint (= (f #xc2bc9ce5659e0188) #x000000c2bc9ce565))
(constraint (= (f #xae3c34ac21091b80) #x000000ae3c34ac21))
(constraint (= (f #x9cd012618eca8715) #x39a024c31d950e28))
(constraint (= (f #xc2ee9ea36cc8821e) #x85dd3d46d991043c))
(constraint (= (f #x17183d0094b93706) #x2e307a0129726e0c))
(constraint (= (f #x562ee14280433e9a) #xac5dc28500867d34))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvor #x0000000000000003 x) x) (bvlshr (bvlshr x #x0000000000000010) #x0000000000000008) (ite (= (bvor #x0000000000000001 x) x) (bvxor (bvadd x x) #x0000000000000002) (ite (= (bvor #x0000000000000002 x) x) (bvadd x x) (bvlshr (bvlshr x #x0000000000000010) #x0000000000000008)))))
