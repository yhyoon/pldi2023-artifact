; Hacker's delight 01, difficulty 1
; Turn off the rightmost 1-bit in a bit-vector.

(set-logic BV)

(define-fun hd01 ((x (BitVec 64))) (BitVec 64) (bvand x (bvsub x #x0000000000000001)))

(synth-fun f ((x (BitVec 64))) (BitVec 64)
    ((Start (BitVec 64) ((bvand Start Start)
                         (bvsub Start Start)
						 (bvor Start Start)
						 (bvadd Start Start)
						 (bvxor Start Start)
                         x
						 #x0000000000000000
						 #xFFFFFFFFFFFFFFFF
                         #x0000000000000001))))

(declare-var x (BitVec 64))
(constraint (= (hd01 x) (f x)))
(check-synth)

