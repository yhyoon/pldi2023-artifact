

(set-logic BV)

(define-fun origCir ((n240 Bool) (n230 Bool) (n150 Bool) )  Bool
  (and n240 (not (and n230 (not n150))))
)


(synth-fun skel ((n240 Bool) (n230 Bool) (n150 Bool) )  Bool (
(Start Bool (depth9) )
 
    (depth9 Bool (
      (and depth8 depth8)
      (or depth8 depth8)
      (xor depth9 depth9)
      (not depth9)
      depth8
      
      )
    )
    
    (depth8 Bool (
      (and depth7 depth7)
      (or depth7 depth7)
      (xor depth8 depth8)
      (not depth8)
      depth7
      n150 
      )
    )
    
    (depth7 Bool (
      (and depth6 depth6)
      (or depth6 depth6)
      (xor depth7 depth7)
      (not depth7)
      depth6
      
      )
    )
    
    (depth6 Bool (
      (and depth5 depth5)
      (or depth5 depth5)
      (xor depth6 depth6)
      (not depth6)
      depth5
      n240 n230 
      )
    )
    
    (depth5 Bool (
      (and depth4 depth4)
      (or depth4 depth4)
      (xor depth5 depth5)
      (not depth5)
      depth4
      
      )
    )
    
    (depth4 Bool (
      (and depth3 depth3)
      (or depth3 depth3)
      (xor depth4 depth4)
      (not depth4)
      depth3
      
      )
    )
    
    (depth3 Bool (
      (and depth2 depth2)
      (or depth2 depth2)
      (xor depth3 depth3)
      (not depth3)
      depth2
      
      )
    )
    
    (depth2 Bool (
      (and depth1 depth1)
      (or depth1 depth1)
      (xor depth2 depth2)
      (not depth2)
      depth1
      
      )
    )
    
    (depth1 Bool (
      (and depth0 depth0)
      (or depth0 depth0)
      (xor depth1 depth1)
      (not depth1)
      depth0
      
      )
    )
     
    (depth0 Bool (
      true
      false
      (xor depth0 depth0)
      (not depth0)
       
    )
  )
  
 )
)
(declare-var n240 Bool)
(declare-var n230 Bool)
(declare-var n150 Bool)

(constraint (= (origCir n240 n230 n150 ) (skel n240 n230 n150 )))
(check-synth)