.section .text # This tells that the text below is code

    .global add # add is defined as global
    #xmm registers are used for SIMD and floating points
    add:
        addss %xmm1, %xmm0 #xmm0=xmm0+xmm1
        ret

    .global sub
    sub:
        subss %xmm1, %xmm0 #xmm0=xmm0-xmm1
        ret

    .global mul
    mul:
        mulss %xmm1,%xmm0 #xmm0=xmm0*xmm1
        ret

    .global fdiv #we use fdiv so that we dont get issue of name conflict with stdlib.h in c
    fdiv:
        divss %xmm1, %xmm0 #xmm0=xmm0/xmm1
        ret#end of the code 