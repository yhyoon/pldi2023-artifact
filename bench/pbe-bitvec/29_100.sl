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
(constraint (= (f #x8eebab9ce5aee52e) #x1dd75739cb5dca5e))
(constraint (= (f #xd62d982675c53ee3) #xffffffffffffffff))
(constraint (= (f #x5cb39c2e0164b983) #xb967385c02c97308))
(constraint (= (f #xe94c4442a4a35509) #xffffffffffffffff))
(constraint (= (f #xede5eae35d30129e) #xdbcbd5c6ba60253e))
(constraint (= (f #xd958eda4ed9de4c9) #xffffffffffffffff))
(constraint (= (f #x50636bec739394ba) #xa0c6d7d8e7272976))
(constraint (= (f #x26297e918dd244c8) #x4c52fd231ba48992))
(constraint (= (f #xedeee10892ee8854) #xdbddc21125dd10aa))
(constraint (= (f #xd89be04cae312270) #xb137c0995c6244e2))
(constraint (= (f #x1cd4cc8e8d98ceee) #x39a9991d1b319dde))
(constraint (= (f #x93805cbe40d45061) #x2700b97c81a8a0c4))
(constraint (= (f #x4039557e05960c80) #x8072aafc0b2c1902))
(constraint (= (f #x085063a91626e9be) #x10a0c7522c4dd37e))
(constraint (= (f #x8e084c5912431760) #x1c1098b224862ec2))
(constraint (= (f #xc1d16061038001d2) #x83a2c0c2070003a6))
(constraint (= (f #xc496ab1292e259eb) #x892d562525c4b3d8))
(constraint (= (f #xc10ea6ed7e1de90d) #xffffffffffffffff))
(constraint (= (f #x99065ae75e0e4ea3) #x320cb5cebc1c9d48))
(constraint (= (f #x2ee370136195c8db) #xffffffffffffffff))
(constraint (= (f #xeed84ec3ae0787ee) #xddb09d875c0f0fde))
(constraint (= (f #xb53291920e692e7c) #x6a6523241cd25cfa))
(constraint (= (f #x9b74c3375525c360) #x36e9866eaa4b86c2))
(constraint (= (f #x006b969cce1c80b5) #x00d72d399c39016c))
(constraint (= (f #xe1a9a44651ac1484) #xc353488ca358290a))
(constraint (= (f #xee9bee0d46c66971) #xdd37dc1a8d8cd2e4))
(constraint (= (f #xa7ac2bc33e91974c) #x4f5857867d232e9a))
(constraint (= (f #xbaec27a2dea8ec53) #x75d84f45bd51d8a8))
(constraint (= (f #xa316448eacb205bb) #x462c891d59640b78))
(constraint (= (f #x1d1e36e979c5a638) #x3a3c6dd2f38b4c72))
(constraint (= (f #x21ace30d798dec9e) #x4359c61af31bd93e))
(constraint (= (f #x76277aec08e9eba6) #xec4ef5d811d3d74e))
(constraint (= (f #x52a37e5b29d8e014) #xa546fcb653b1c02a))
(constraint (= (f #x53952a9539e24e42) #xa72a552a73c49c86))
(constraint (= (f #xdea008e87a890b41) #xffffffffffffffff))
(constraint (= (f #x81e729363eeb7dbb) #xffffffffffffffff))
(constraint (= (f #x6e41d702e55c0e52) #xdc83ae05cab81ca6))
(constraint (= (f #x0ae433e3ea67d4b6) #x15c867c7d4cfa96e))
(constraint (= (f #xda5e29ea66b6e431) #xb4bc53d4cd6dc864))
(constraint (= (f #xc76a494cd08d33a5) #xffffffffffffffff))
(constraint (= (f #xce812ed05319e237) #xffffffffffffffff))
(constraint (= (f #x947b91b3a3e5a1e6) #x28f7236747cb43ce))
(constraint (= (f #xac2be80d960d71b3) #xffffffffffffffff))
(constraint (= (f #x5cce56b765ad0484) #xb99cad6ecb5a090a))
(constraint (= (f #x1b5c867969ad6a33) #xffffffffffffffff))
(constraint (= (f #x5ee25e673648c96d) #xbdc4bcce6c9192dc))
(constraint (= (f #xaddee856a089ce81) #xffffffffffffffff))
(constraint (= (f #x52e2d2c2b63c52a2) #xa5c5a5856c78a546))
(constraint (= (f #x1678500631351cb5) #xffffffffffffffff))
(constraint (= (f #xec9e9ca65398eed7) #xd93d394ca731ddb0))
(constraint (= (f #x6022a111eab40201) #xc0454223d5680404))
(constraint (= (f #xa4d05e0550b78b65) #xffffffffffffffff))
(constraint (= (f #x83071ae32587798c) #x060e35c64b0ef31a))
(constraint (= (f #x91e5425638382747) #x23ca84ac70704e90))
(constraint (= (f #xee46eda042a2be00) #xdc8ddb4085457c02))
(constraint (= (f #x68db30198084e329) #xd1b660330109c654))
(constraint (= (f #xb21a333c0036e183) #x64346678006dc308))
(constraint (= (f #xaee2a188b5b5ce95) #xffffffffffffffff))
(constraint (= (f #xea5599e91b71bbc3) #xffffffffffffffff))
(constraint (= (f #x97b7e9bcb2ee8782) #x2f6fd37965dd0f06))
(constraint (= (f #xc42dce9e9e217db7) #xffffffffffffffff))
(constraint (= (f #x68677dc0e00ed8cc) #xd0cefb81c01db19a))
(constraint (= (f #xc84186e306b38e6a) #x90830dc60d671cd6))
(constraint (= (f #xb6ce6091beea6c23) #x6d9cc1237dd4d848))
(constraint (= (f #x7ecd0bde2e7ba762) #xfd9a17bc5cf74ec6))
(constraint (= (f #xbe618d7c27611730) #x7cc31af84ec22e62))
(constraint (= (f #x22112ea80e3910e1) #xffffffffffffffff))
(constraint (= (f #x0ed23234eed8ab16) #x1da46469ddb1562e))
(constraint (= (f #x5c4a061ad1d877e5) #xb8940c35a3b0efcc))
(constraint (= (f #x76ee579a52ecbe44) #xeddcaf34a5d97c8a))
(constraint (= (f #x848ea37eeae26bc9) #x091d46fdd5c4d794))
(constraint (= (f #x04c2ec640db2ed49) #x0985d8c81b65da94))
(constraint (= (f #xb26e17dbb1c86ce4) #x64dc2fb76390d9ca))
(constraint (= (f #x9d87c3aa30d51400) #x3b0f875461aa2802))
(constraint (= (f #xad4929ab31a37781) #xffffffffffffffff))
(constraint (= (f #xdb3ac0c300b7a3e2) #xb6758186016f47c6))
(constraint (= (f #x33c788b87273c0ae) #x678f1170e4e7815e))
(constraint (= (f #xba32ed28c045d7e3) #xffffffffffffffff))
(constraint (= (f #x9658864b6bca5216) #x2cb10c96d794a42e))
(constraint (= (f #x0549eba00a40ebe7) #x0a93d7401481d7d0))
(constraint (= (f #xae7b15cee4e54a63) #xffffffffffffffff))
(constraint (= (f #x5981bb8e61a3ec06) #xb303771cc347d80e))
(constraint (= (f #x4d51ad648e5d0479) #xffffffffffffffff))
(constraint (= (f #x0c550996d15bb84b) #xffffffffffffffff))
(constraint (= (f #x3c1b27453e2044dd) #x78364e8a7c4089bc))
(constraint (= (f #x9b489167b6cc8b12) #x369122cf6d991626))
(constraint (= (f #x1eeee7c8dc98ec26) #x3dddcf91b931d84e))
(constraint (= (f #xadd6422a107b15d6) #x5bac845420f62bae))
(constraint (= (f #xd50324cc2e508413) #xaa0649985ca10828))
(constraint (= (f #x102c8ac60ed78bd5) #xffffffffffffffff))
(constraint (= (f #x08e2dbb7a60c00ba) #x11c5b76f4c180176))
(constraint (= (f #x5a835c9da09e1b46) #xb506b93b413c368e))
(constraint (= (f #x11753e848cb39423) #xffffffffffffffff))
(constraint (= (f #x4e7559debe3673bc) #x9ceab3bd7c6ce77a))
(constraint (= (f #x973eda014658e876) #x2e7db4028cb1d0ee))
(constraint (= (f #xd76476d451446083) #xaec8eda8a288c108))
(constraint (= (f #x001596355373035a) #x002b2c6aa6e606b6))
(constraint (= (f #xea405a50aea02704) #xd480b4a15d404e0a))
(constraint (= (f #x8e062e73c9ebd712) #x1c0c5ce793d7ae26))
(constraint (= (f #x00de10bdceb5c61b) #xffffffffffffffff))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvand #x0000000000000001 x) #x0000000000000000) (bvxor (bvadd x x) #x0000000000000002) (ite (= (bvurem x #x0000000000000009) #x0000000000000001) (bvnot #x0000000000000000) (ite (= (bvsrem x #x000000000000000b) #x0000000000000000) (bvnot #x0000000000000000) (ite (= (bvor #x0000000000000002 x) x) (ite (= (bvsrem x #x0000000000000003) #x0000000000000000) (bvneg (bvmul (bvnot x) #x0000000000000002)) (ite (= (bvurem x #x0000000000000005) #x0000000000000001) (bvxor (bvadd x x) #x000000000000000e) (ite (= (bvor #x0000000000000008 x) x) (bvnot #x0000000000000000) (ite (= (bvurem x #x0000000000000007) #x0000000000000000) (bvxor (bvadd x x) #x000000000000000e) (ite (= (bvsrem x #x000000000000000d) #x0000000000000000) (bvneg (bvmul (bvnot x) #x0000000000000002)) (ite (= (bvor #x0000000000000010 x) x) (ite (= (bvand #x0000000000000004 x) #x0000000000000000) (ite (= (bvurem x #x0000000000000007) #x0000000000000001) (bvxor (bvadd x x) #x000000000000000e) (bvnot #x0000000000000000)) (bvnot #x0000000000000000)) (ite (= (bvand #x0000000000000004 x) #x0000000000000000) (ite (= (bvashr x x) #x0000000000000000) (ite (= (bvurem x #x0000000000000007) #x0000000000000001) (bvxor (bvadd x x) #x000000000000000e) (bvnot #x0000000000000000)) (bvnot #x0000000000000000)) (bvneg (bvmul (bvnot x) #x0000000000000002))))))))) (ite (= (bvurem x #x0000000000000003) #x0000000000000001) (bvnot #x0000000000000000) (ite (= (bvurem x #x0000000000000005) #x0000000000000000) (bvxor (bvadd x x) #x0000000000000006) (ite (= (bvurem x #x0000000000000007) #x0000000000000001) (bvxor (bvadd x x) #x0000000000000006) (ite (= (bvsrem x #x0000000000000003) #x0000000000000000) (bvxor (bvadd x x) #x0000000000000006) (ite (= (bvurem x #x0000000000000003) #x0000000000000000) (bvnot #x0000000000000000) (ite (= (bvand #x000000000000000d x) #x0000000000000001) (bvxor (bvadd x x) #x0000000000000006) (ite (= (bvor #x000000000000000c x) x) (bvxor (bvadd x x) #x0000000000000006) (ite (= (bvurem x #x0000000000000005) #x0000000000000001) (ite (= (bvor #x0000000000000008 x) x) (bvnot #x0000000000000000) (bvxor (bvadd x x) #x0000000000000006)) (bvnot #x0000000000000000))))))))))))))
