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
(constraint (= (f #xb15aecabc523e138) #xb6453de108d1a324))
(constraint (= (f #x7e6906e222c8e512) #x86827674009c56c0))
(constraint (= (f #xe8b6160aa49785e3) #x0d16c2c15492f0bc))
(constraint (= (f #x9ca7e280ab46ecdb) #x0394fc501568dd9b))
(constraint (= (f #x4724e084594e7463) #x08e49c108b29ce8c))
(constraint (= (f #x525491c82e78ada6) #x5d2f48abab9122ca))
(constraint (= (f #x07ce6916e9e8e9cb) #x00f9cd22dd3d1d39))
(constraint (= (f #x4124cadc6eb48ae9) #x0824995b8dd6915d))
(constraint (= (f #xa8c9a4229332cdbe) #xae3d09e069ffa0e2))
(constraint (= (f #x92d33380e44421ec) #x99a60048d5ffdfcc))
(constraint (= (f #x76640a27d7b56361) #x0ecc8144faf6ac6c))
(constraint (= (f #x92b2b68e283e7dbe) #x99878b2545ba95e2))
(constraint (= (f #x1b14e2b08be26563) #x03629c56117c4cac))
(constraint (= (f #x001d1b2882a80d23) #x0003a365105501a4))
(constraint (= (f #x8d60e6e26ec909e0) #x948ad87447dc7940))
(constraint (= (f #x9ee3a42c86782833) #x03dc748590cf0506))
(constraint (= (f #x00c7a3c0ce45e672) #x10bb2984c161880a))
(constraint (= (f #xc4eeda64147b4822) #xc89fecbdd333939e))
(constraint (= (f #x8eae14e75d4eb94a) #x95c33398e779cdb4))
(constraint (= (f #x1e3093c7ea5c2b0e) #x2c4d8a8b6bb6685c))
(constraint (= (f #x9e4e0c3e1ec00d1d) #x03c9c187c3d801a3))
(constraint (= (f #xd968a87dbaa0627d) #x0b2d150fb7540c4f))
(constraint (= (f #x10335961a76dbb62) #x1f3023cb8cf6dfaa))
(constraint (= (f #x15e248785510eba9) #x02bc490f0aa21d75))
(constraint (= (f #x0ba6b73ca3a93e18) #x1aec4bc8d96eaa36))
(constraint (= (f #xe7354bc068c567bb) #x0ce6a9780d18acf7))
(constraint (= (f #x5d67ac3bec1e2417) #x0bacf5877d83c482))
(constraint (= (f #x0ee98be5e14de869) #x01dd317cbc29bd0d))
(constraint (= (f #xea2cb928043e11c0) #xeb89ed9583fa30a2))
(constraint (= (f #x8b82d29459aa4e7e) #x92caa56b140fa996))
(constraint (= (f #x0371690876a8050e) #x133a5277ef3d84bc))
(constraint (= (f #x6e61ee5751937745) #x0dcc3dcaea326ee8))
(constraint (= (f #x28d74443498aade8) #x3649cfff14f20308))
(constraint (= (f #x12e864ee37a2357e) #x21b9de9f54281226))
(constraint (= (f #x6ad47a881eea8aa5) #x0d5a8f5103dd5154))
(constraint (= (f #x2b7c50ede8ec8e2e) #x38c48bdf0a5dc54a))
(constraint (= (f #xe77ab37006235eb1) #x0cef566e00c46bd6))
(constraint (= (f #x02abe963a9905c1a) #x12812acd6ef75658))
(constraint (= (f #x00d313a7a3ee8975) #x001a6274f47dd12e))
(constraint (= (f #xbbddc7e2b2477836) #xc01feb64872300b2))
(constraint (= (f #xe41779e7b98365eb) #x0c82ef3cf7306cbd))
(constraint (= (f #x432c446e03144a03) #x0865888dc0628940))
(constraint (= (f #x2d05cbbbce2da576) #x3a356f00114acb1e))
(constraint (= (f #x0c9e50330bc6ba02) #x1bd46b2fdb0a4e60))
(constraint (= (f #x7ac52e07ee6a96ed) #x0f58a5c0fdcd52dd))
(constraint (= (f #x9d033991de055d4d) #x03a067323bc0aba9))
(constraint (= (f #xb6bee845eb1a96aa) #xbb52f9c18c68ed3e))
(constraint (= (f #xe5373278a34e00e6) #xe6e3bf51191920d6))
(constraint (= (f #xb55116c401771271) #x06aa22d8802ee24e))
(constraint (= (f #x566a42590b19b5e3) #x0acd484b216336bc))
(constraint (= (f #x35b2600156a51ca2) #x42573a01413acad6))
(constraint (= (f #x8e53615e5171d075) #x01ca6c2bca2e3a0e))
(constraint (= (f #x4743932883b9770e) #x52cf59f5fb7ddf9c))
(constraint (= (f #x1ea08bae4e43e7eb) #x03d41175c9c87cfd))
(constraint (= (f #x0a3dc5527e4e8d38) #x1999e8fd5669a464))
(constraint (= (f #xc4ea2c97e382e9e1) #x089d4592fc705d3c))
(constraint (= (f #xe509eed46eca5d84) #xe6b94fe727ddb7aa))
(constraint (= (f #x190ebeee47859d75) #x0321d7ddc8f0b3ae))
(constraint (= (f #xe708745498d33e10) #xe897ed0f4f460a2e))
(constraint (= (f #xe5a87ee28e45eeec) #xe74df6f465618ffc))
(constraint (= (f #x81775c4dd888ca0d) #x002eeb89bb111941))
(constraint (= (f #x3a2e6c807e069303) #x0745cd900fc0d260))
(constraint (= (f #x3d80160ca67edbe9) #x07b002c194cfdb7d))
(constraint (= (f #xcb4e55515d16597e) #xce996ffc4744f3e6))
(constraint (= (f #xb0ec71e76dedacc4) #xb5ddaac8f70ed1f6))
(constraint (= (f #x2c94e9744baec4b7) #x05929d2e8975d896))
(constraint (= (f #xdeb7681c8c493ae8) #xe0cbf19ac384a738))
(constraint (= (f #xb393a45e24047a2a) #xb85a6a1841c43286))
(constraint (= (f #xe840350d5b67dac6) #xe9bc31bc85b15d18))
(constraint (= (f #x7b7d398346451ee2) #x83c565eb11e0ccf2))
(constraint (= (f #x76a7b53c2a594853) #x0ed4f6a7854b290a))
(constraint (= (f #xb51ac62eee51d363) #x06a358c5ddca3a6c))
(constraint (= (f #x3344a5a6ec058c31) #x066894b4dd80b186))
(constraint (= (f #x837d47acc09b56e6) #x8b457331f491a176))
(constraint (= (f #x2ecbb8ce3bee90e9) #x05d97719c77dd21d))
(constraint (= (f #xe3e68a658c01b964) #xe5a821bf33419dcc))
(constraint (= (f #x68ba23b02acca100) #x722e8175281fd6ee))
(constraint (= (f #xd675bae2712d11d2) #xd90e5f344a1a40b4))
(constraint (= (f #x19ea065aa967a878) #x284b65f4fed12df0))
(constraint (= (f #x9a4aa98175185cd3) #x034955302ea30b9a))
(constraint (= (f #x8e877809abd45e26) #x959f008911171842))
(constraint (= (f #x81edae5de7e90bd2) #x89ced378096a7b14))
(constraint (= (f #x415268524d908eae) #x4d3d41cd28b785c2))
(constraint (= (f #xa7284e1617868d3e) #xacb5c934b60e246a))
(constraint (= (f #x1eeee0eb369b5c9c) #x2cfff2dc8331a6d2))
(constraint (= (f #x1796479c6e7e920b) #x02f2c8f38dcfd241))
(constraint (= (f #x84805e8bb2eb2acc) #x8c3858a2f7bc781e))
(constraint (= (f #xaa5e08111e1500d2) #xafb827900c33b0c4))
(constraint (= (f #x3db5e9bd0ed4d830) #x49da8b213de78aac))
(constraint (= (f #xee0b53ee13192d3d) #x0dc16a7dc26325a7))
(constraint (= (f #x1e28be4beeec2437) #x03c517c97ddd8486))
(constraint (= (f #x170ec020ee0ebd5b) #x02e1d8041dc1d7ab))
(constraint (= (f #x9c7c56316bec069c) #xa2b490ce552d4632))
(constraint (= (f #xb7b4815610d4822e) #xbc393940afc73a0a))
(constraint (= (f #x1c5444199e15ccdc) #x2a8effd80434700e))
(constraint (= (f #x13ace833b8b4612a) #x227219b07d291b16))
(constraint (= (f #x5e407e46e16caec6) #x685c76627355e3d8))
(constraint (= (f #xdd70e7606757de3a) #xdf99d8ea60e26056))
(constraint (= (f #x707ec6498e18256e) #x7976d9e4f536a316))
(constraint (= (f #x73dd02db2ba92398) #x7c9f32ad78ee915e))
(check-synth)
