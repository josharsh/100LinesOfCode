VARIABLE picky

: COLLECT_PICKY DUP 1- picky ! ;

: NPICK COLLECT_PICKY 2 * 0 ?DO picky @ PICK LOOP ;

: SPLIT BEGIN DUP WHILE 10 /MOD REPEAT DROP DEPTH ;

: First_Line
  CASE
  0 OF SPACE ." _  " ENDOF 1 OF SPACE SPACE ENDOF
  2 OF SPACE ." _  " ENDOF 3 OF ." _  " ENDOF
  4 OF SPACE SPACE SPACE SPACE ENDOF 5 OF SPACE ." _  " ENDOF
  6 OF SPACE ." _  "ENDOF 7 OF ." _   "  ENDOF 
  8 OF SPACE ." _  " ENDOF 9 OF SPACE ." _  " ENDOF
  ENDCASE ;
  
: Second_Line
  CASE
  0 OF ." | | " ENDOF 1 OF ." | " ENDOF
  2 OF SPACE ." _| " ENDOF 3 OF ." _| " ENDOF
  4 OF ." |_| " ENDOF 5 OF ." |_  " ENDOF
  6 OF ." |_  "ENDOF 7 OF SPACE ." |  "  ENDOF 
  8 OF ." |_| " ENDOF 9 OF ." |_| " ENDOF
  ENDCASE ;
  
: Third_Line
  CASE
  0 OF ." |_| " ENDOF 1 OF ." | " ENDOF
  2 OF ." |_  " ENDOF 3 OF ." _| " ENDOF
  4 OF SPACE SPACE ." | " ENDOF 5 OF SPACE ." _| " ENDOF
  6 OF ." |_| "ENDOF 7 OF SPACE ." |  "  ENDOF 
  8 OF ." |_| " ENDOF 9 OF SPACE ." _| " ENDOF
  ENDCASE ;

: LED 
  SPLIT
  NPICK
  DEPTH 3 / 0 ?DO First_Line LOOP CR
  DEPTH 2 / 0 ?DO Second_Line LOOP CR
  DEPTH 0 ?DO Third_Line LOOP ;
