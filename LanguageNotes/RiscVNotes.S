// This is a comment.

/*
This is a multi-line comment.
*/

/*
RiscV Assembly is weird. You're telling the machine what to do with the registers in its cpu.
For example, here's a function checking if two numbers are equal:
*/

.globl eq
eq:
        beq a0, a1, .equal
        mv a0, x0
        ret
.equal:
        addi a0, x0, 1
        ret
    
/*
You can see the method "beq", checks to see if two registers are equal, and to jump if they are.
a0, a1, a2, etc. are the arguments, with a0 being the return value.
x0 is just 0. The "mv" method moves value 1 to value 0, so you're returning 0 if false.
"addi" (add immediate) takes an immediate value, 1, and adds it to another register, and the sum is placed in a0.
*/