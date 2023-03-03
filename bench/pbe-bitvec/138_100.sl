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
(constraint (= (f #x69d203d5b99413c9) #x69d203d5b99413ca))
(constraint (= (f #x327576d6080e8534) #x000064eaedac101d))
(constraint (= (f #x9e7070561bd5e4ec) #x00003ce0e0ac37ab))
(constraint (= (f #x58e263ea478ed7dc) #x0000b1c4c7d48f1d))
(constraint (= (f #xb2da23093e8d3868) #xb2da23093e8d3869))
(constraint (= (f #x9018267e0d6ced9e) #x000020304cfc1ad9))
(constraint (= (f #x6195b045712e2b29) #x6195b045712e2b2a))
(constraint (= (f #x6948902944b15282) #x6948902944b15283))
(constraint (= (f #xe64e478d82dd3169) #xe64e478d82dd316a))
(constraint (= (f #xbeeb775b656c645d) #x00007dd6eeb6cad8))
(constraint (= (f #x166ec11c208aa60c) #x00002cdd82384115))
(constraint (= (f #x698c572b1ec65c6d) #x0000d318ae563d8c))
(constraint (= (f #xc034206b81720c5d) #x0000806840d702e4))
(constraint (= (f #x7b7b0208037606e7) #x0000f6f6041006ec))
(constraint (= (f #xe64aee8876902b75) #x0000cc95dd10ed20))
(constraint (= (f #xdacb7955522db534) #x0000b596f2aaa45b))
(constraint (= (f #x9ed23499e00533e3) #x9ed23499e00533e4))
(constraint (= (f #x42402be3a3e76a50) #x42402be3a3e76a51))
(constraint (= (f #xe72795a7b2387145) #x0000ce4f2b4f6470))
(constraint (= (f #x15bb9da6680546d9) #x15bb9da6680546da))
(constraint (= (f #xeece75808962063c) #x0000dd9ceb0112c4))
(constraint (= (f #x07587ce8406a78e3) #x07587ce8406a78e4))
(constraint (= (f #xd18eb06407d43ad9) #xd18eb06407d43ada))
(constraint (= (f #xa9905eee12a1d50b) #xa9905eee12a1d50c))
(constraint (= (f #x1d369d055a5ec0ed) #x00003a6d3a0ab4bd))
(constraint (= (f #x244110ea52dbe518) #x244110ea52dbe519))
(constraint (= (f #x16899ca396ccae4e) #x00002d1339472d99))
(constraint (= (f #x57e7ed0ee920d413) #x57e7ed0ee920d414))
(constraint (= (f #xeb186a9e203a2e88) #xeb186a9e203a2e89))
(constraint (= (f #x8a4539d818e22940) #x8a4539d818e22941))
(constraint (= (f #xa580a097880d2d39) #xa580a097880d2d3a))
(constraint (= (f #x6101ed7b4dee0ea9) #x6101ed7b4dee0eaa))
(constraint (= (f #x1915b0c957d1d451) #x1915b0c957d1d452))
(constraint (= (f #x9407640a40a7ee46) #x0000280ec814814f))
(constraint (= (f #x4e951106918cb84a) #x4e951106918cb84b))
(constraint (= (f #x0a5ec2c159dda1b0) #x0a5ec2c159dda1b1))
(constraint (= (f #xd3e88c6115d02458) #xd3e88c6115d02459))
(constraint (= (f #xea2279ea1e992ac6) #x0000d444f3d43d32))
(constraint (= (f #x824b1e53d90009de) #x000004963ca7b200))
(constraint (= (f #x9240049a4b511d0c) #x00002480093496a2))
(constraint (= (f #x9e925a31d3073ee2) #x9e925a31d3073ee3))
(constraint (= (f #xeecb7c42132b9222) #xeecb7c42132b9223))
(constraint (= (f #x4d1e6e756c1e0b6d) #x00009a3cdcead83c))
(constraint (= (f #x0e8ebce6c0d553e2) #x0e8ebce6c0d553e3))
(constraint (= (f #xe4269c8e13402eb2) #xe4269c8e13402eb3))
(constraint (= (f #xec3ae2d105777a40) #xec3ae2d105777a41))
(constraint (= (f #x1d9bc33ce853375a) #x1d9bc33ce853375b))
(constraint (= (f #x59abebe84706cb8b) #x59abebe84706cb8c))
(constraint (= (f #x195e7a9140953c42) #x195e7a9140953c43))
(constraint (= (f #x9893e457a5148e19) #x9893e457a5148e1a))
(constraint (= (f #xcb71c2e1bee32ab6) #x000096e385c37dc6))
(constraint (= (f #xe4470bcd044ccb2b) #xe4470bcd044ccb2c))
(constraint (= (f #x6e6b43c3ea285b26) #x0000dcd68787d450))
(constraint (= (f #x24acb7c53db3c46b) #x24acb7c53db3c46c))
(constraint (= (f #x152ea72d187276eb) #x152ea72d187276ec))
(constraint (= (f #x575c59d24767ec02) #x575c59d24767ec03))
(constraint (= (f #x7eb820146ccc076d) #x0000fd704028d998))
(constraint (= (f #xa13e87a0e3cad185) #x0000427d0f41c795))
(constraint (= (f #xec34da09e56cd5b2) #xec34da09e56cd5b3))
(constraint (= (f #x0242eebd2e30e061) #x0242eebd2e30e062))
(constraint (= (f #x4e6c413a326d9889) #x4e6c413a326d988a))
(constraint (= (f #xadc74c69e8199703) #xadc74c69e8199704))
(constraint (= (f #x86341e813322bc82) #x86341e813322bc83))
(constraint (= (f #x56a7ac11dc4a751c) #x0000ad4f5823b894))
(constraint (= (f #xd13be05ec9373e4e) #x0000a277c0bd926e))
(constraint (= (f #xaceb607dc37c9062) #xaceb607dc37c9063))
(constraint (= (f #x4ac737d249ce5747) #x0000958e6fa4939c))
(constraint (= (f #xc9a413163b16ade8) #xc9a413163b16ade9))
(constraint (= (f #x8db821979dbebbc1) #x8db821979dbebbc2))
(constraint (= (f #x470b8374e6b5755d) #x00008e1706e9cd6a))
(constraint (= (f #x9e4b233e67ce8068) #x9e4b233e67ce8069))
(constraint (= (f #x5a8340b8e2e317b9) #x5a8340b8e2e317ba))
(constraint (= (f #xdb2aac076e18e673) #xdb2aac076e18e674))
(constraint (= (f #xea39dbdd4217e215) #x0000d473b7ba842f))
(constraint (= (f #x74b599ed7e958b25) #x0000e96b33dafd2b))
(constraint (= (f #x4d1c310e6e8cd964) #x00009a38621cdd19))
(constraint (= (f #x5e30c8bad66c4035) #x0000bc619175acd8))
(constraint (= (f #x991e060d1243a44c) #x0000323c0c1a2487))
(constraint (= (f #xc21381e5aa8510be) #x0000842703cb550a))
(constraint (= (f #xdaaae6eac92e8b6d) #x0000b555cdd5925d))
(constraint (= (f #x156eeeedc870e6c9) #x156eeeedc870e6ca))
(constraint (= (f #x274674848ed387c7) #x00004e8ce9091da7))
(constraint (= (f #x797e42bc0c25edca) #x797e42bc0c25edcb))
(constraint (= (f #x6906cec4206ddec3) #x6906cec4206ddec4))
(constraint (= (f #xe93d310b1c099ce5) #x0000d27a62163813))
(constraint (= (f #xa6c98c37ae3c5797) #x00004d93186f5c78))
(constraint (= (f #x201adc1d282e610b) #x201adc1d282e610c))
(constraint (= (f #x63440a3ec590e941) #x63440a3ec590e942))
(constraint (= (f #xce346deb31ea4de8) #xce346deb31ea4de9))
(constraint (= (f #xb441559d5e673584) #x00006882ab3abcce))
(constraint (= (f #xa9e63734a25808c7) #x000053cc6e6944b0))
(constraint (= (f #x4e502985823e43a1) #x4e502985823e43a2))
(constraint (= (f #x008b5eec3a73a2d9) #x008b5eec3a73a2da))
(constraint (= (f #x7d1d342ead6a4eb7) #x0000fa3a685d5ad4))
(constraint (= (f #xd9e33832dc698018) #xd9e33832dc698019))
(constraint (= (f #x812e11382a4a7d9b) #x812e11382a4a7d9c))
(constraint (= (f #xd3ad5d8cda265b91) #xd3ad5d8cda265b92))
(constraint (= (f #x060316a87ae2730e) #x00000c062d50f5c4))
(constraint (= (f #x65775eba816eab19) #x65775eba816eab1a))
(constraint (= (f #xe5e99b245ee14350) #xe5e99b245ee14351))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (ite (= (bvor #x0000000000000004 x) x) (bvlshr (bvadd x x) #x0000000000000010) (ite (= (bvor #x0000000000000001 x) x) (ite (= (bvor #x0000000000000002 x) x) (bvxor #x0000000000000007 x) (bvxor #x0000000000000003 x)) (bvxor #x0000000000000001 x))))
