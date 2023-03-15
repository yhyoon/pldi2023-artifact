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
(constraint (= (f #xdccc2599e7a86e9b) #xb9984b33cf50dd37))
(constraint (= (f #x4a12aee71e5ed348) #x94255dce3cbda691))
(constraint (= (f #x29c415d9ebeba262) #x53882bb3d7d744c5))
(constraint (= (f #xe5e917b8b2c7e4b7) #xcbd22f71658fc96f))
(constraint (= (f #x0ebd0be16767cee1) #x1d7a17c2cecf9dc3))
(constraint (= (f #x011a29aa783c24db) #x02345354f07849b7))
(constraint (= (f #xbadae9a7e2e89a86) #x75b5d34fc5d1350d))
(constraint (= (f #x66b525941791deea) #xcd6a4b282f23bdd5))
(constraint (= (f #xa79756103485a8c3) #x4f2eac20690b5187))
(constraint (= (f #x0102d5badc289042) #x0205ab75b8512085))
(constraint (= (f #x8c294ee4ee0921c9) #x18529dc9dc124393))
(constraint (= (f #x2abdc5d884b484ae) #x557b8bb10969095d))
(constraint (= (f #x750ccb3b231b264d) #xea19967646364c9b))
(constraint (= (f #x5e6467db2161909a) #xbcc8cfb642c32135))
(constraint (= (f #x0e42b79011a1009c) #x1c856f2023420139))
(constraint (= (f #xb008e5a3bd1bbda6) #x6011cb477a377b4d))
(constraint (= (f #xa45de8120731eede) #x48bbd0240e63ddbd))
(constraint (= (f #x8628ac9ca1050b76) #x0c515939420a16ed))
(constraint (= (f #x5dcc06d9baa2cd4b) #xbb980db375459a97))
(constraint (= (f #xe51c753e5696b12e) #xca38ea7cad2d625d))
(constraint (= (f #xc74a1ad867bdeb8c) #x8e9435b0cf7bd719))
(constraint (= (f #x5eb728ed8388ca2a) #xbd6e51db07119455))
(constraint (= (f #xe07bad1cd2a68704) #xc0f75a39a54d0e09))
(constraint (= (f #x5dea977eb9c7873d) #xbbd52efd738f0e7b))
(constraint (= (f #x306b195c148eea58) #x60d632b8291dd4b1))
(constraint (= (f #x7e055eb3d5be5ce7) #xfc0abd67ab7cb9cf))
(constraint (= (f #x60a5c6e49ce5c00e) #xc14b8dc939cb801d))
(constraint (= (f #xeeee72a917e94569) #xdddce5522fd28ad3))
(constraint (= (f #xce9576e03a8e20dc) #x9d2aedc0751c41b9))
(constraint (= (f #xb0d340bc8ee29e0e) #x61a681791dc53c1d))
(constraint (= (f #x991eaded4b32576e) #x323d5bda9664aedd))
(constraint (= (f #xc953e684dd7c2ace) #x92a7cd09baf8559d))
(constraint (= (f #xd3beee7c9bb9e07c) #xa77ddcf93773c0f9))
(constraint (= (f #x459dcb8764571b5e) #x8b3b970ec8ae36bd))
(constraint (= (f #xccdc0e511e2d6506) #x99b81ca23c5aca0d))
(constraint (= (f #xc2be9b7c9e499385) #x857d36f93c93270b))
(constraint (= (f #x334d93b7a7534d4e) #x669b276f4ea69a9d))
(constraint (= (f #xe642ea81990d1ca0) #xcc85d503321a3941))
(constraint (= (f #x1433430d6a54738d) #x2866861ad4a8e71b))
(constraint (= (f #xb6953eeea441e3e9) #x6d2a7ddd4883c7d3))
(constraint (= (f #x4ed7bb47233cce43) #x9daf768e46799c87))
(constraint (= (f #x1ab1540a8b24cabe) #x3562a8151649957d))
(constraint (= (f #x65c5a1eedbd4e7c1) #xcb8b43ddb7a9cf83))
(constraint (= (f #xd59c46d5eb921a6d) #xab388dabd72434db))
(constraint (= (f #xe5dd232ee63bc625) #xcbba465dcc778c4b))
(constraint (= (f #x8602de3d4eeeedc9) #x0c05bc7a9ddddb93))
(constraint (= (f #x78cc91dd617e3be7) #xf19923bac2fc77cf))
(constraint (= (f #xedd6be466c14b834) #xdbad7c8cd8297069))
(constraint (= (f #xd83563c3a8eec64b) #xb06ac78751dd8c97))
(constraint (= (f #xd7529e5460d58e78) #xaea53ca8c1ab1cf1))
(constraint (= (f #x5ae393a95b6a3841) #xb5c72752b6d47083))
(constraint (= (f #xcb016a5a2d800102) #x9602d4b45b000205))
(constraint (= (f #x6bc7d0313e9e4bd2) #xd78fa0627d3c97a5))
(constraint (= (f #xe5921d09e909c6b6) #xcb243a13d2138d6d))
(constraint (= (f #x65e317e15ba71917) #xcbc62fc2b74e322f))
(constraint (= (f #xab44a88ee3c7526c) #x5689511dc78ea4d9))
(constraint (= (f #x1c4ebe73322ee3ab) #x389d7ce6645dc757))
(constraint (= (f #x594e3687ec6a0e48) #xb29c6d0fd8d41c91))
(constraint (= (f #x9e4073864665e891) #x3c80e70c8ccbd123))
(constraint (= (f #xa1ac6baaa9313e81) #x4358d75552627d03))
(constraint (= (f #x937b14ac6e547382) #x26f62958dca8e705))
(constraint (= (f #x8bc2812ea2e26992) #x1785025d45c4d325))
(constraint (= (f #x7b7c481cc27500ca) #xf6f8903984ea0195))
(constraint (= (f #x4ea5ec6e72534bea) #x9d4bd8dce4a697d5))
(constraint (= (f #x4026e35aa60dd992) #x804dc6b54c1bb325))
(constraint (= (f #xc6c7ca5a804c9940) #x8d8f94b500993281))
(constraint (= (f #xec18b79b50b15cda) #xd8316f36a162b9b5))
(constraint (= (f #x8801050bc177d602) #x10020a1782efac05))
(constraint (= (f #x8817971e9eceeb77) #x102f2e3d3d9dd6ef))
(constraint (= (f #x5b7b0ea6ee3688a9) #xb6f61d4ddc6d1153))
(constraint (= (f #x1153de7e62de4e77) #x22a7bcfcc5bc9cef))
(constraint (= (f #x91ecdabc2072e570) #x23d9b57840e5cae1))
(constraint (= (f #x1d1455bdd45d0a2a) #x3a28ab7ba8ba1455))
(constraint (= (f #xba9cb9b31c530984) #x7539736638a61309))
(constraint (= (f #xa8982edcee4ec2be) #x51305db9dc9d857d))
(constraint (= (f #xb80e50e2abe74b87) #x701ca1c557ce970f))
(constraint (= (f #x34d82a54edee68e8) #x69b054a9dbdcd1d1))
(constraint (= (f #x77a3a40bd227986e) #xef474817a44f30dd))
(constraint (= (f #x797b80b62b42a71d) #xf2f7016c56854e3b))
(constraint (= (f #xeb2b49cbdb9860a8) #xd6569397b730c151))
(constraint (= (f #x486a5b69de5b032c) #x90d4b6d3bcb60659))
(constraint (= (f #x3022c81008e3a1dd) #x6045902011c743bb))
(constraint (= (f #x3ecee13c96555e23) #x7d9dc2792caabc47))
(constraint (= (f #xe2ed3b72309c4721) #xc5da76e461388e43))
(constraint (= (f #xbe298e56556eeb4e) #x7c531cacaaddd69d))
(constraint (= (f #x009ceee5d222ece3) #x0139ddcba445d9c7))
(constraint (= (f #xcc590b87731eb23d) #x98b2170ee63d647b))
(constraint (= (f #x209e930c58e2e80d) #x413d2618b1c5d01b))
(constraint (= (f #x4318023d87ed8727) #x8630047b0fdb0e4f))
(constraint (= (f #xa753728ee5b965dc) #x4ea6e51dcb72cbb9))
(constraint (= (f #x9770ce51a74eee44) #x2ee19ca34e9ddc89))
(constraint (= (f #x33eec11e6b7c1e31) #x67dd823cd6f83c63))
(constraint (= (f #xe035e3b956ea7ad8) #xc06bc772add4f5b1))
(constraint (= (f #xa2ceed603e352e64) #x459ddac07c6a5cc9))
(constraint (= (f #x9c083315e9b2ed6b) #x3810662bd365dad7))
(constraint (= (f #x368681715952c0cd) #x6d0d02e2b2a5819b))
(constraint (= (f #xcd08ee5371390a8c) #x9a11dca6e2721519))
(constraint (= (f #xe8896ac2395b0ea7) #xd112d58472b61d4f))
(constraint (= (f #x20997c4e09ee6540) #x4132f89c13dcca81))
(constraint (= (f #x47ba39abbe26145d) #x8f7473577c4c28bb))
(check-synth)
(define-fun f_1 ((x (BitVec 64))) (BitVec 64) (bvsub x (bvnot x)))
