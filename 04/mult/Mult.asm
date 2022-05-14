// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.
    // R2 = 0
    @R2
    M = 0
    // i = 0
    @i
    M = 0
    // Checking to see if R = 0, if so, goto to END
    @R0
    D = M
    @END
    D;JEQ
(LOOP)
    // if (i < R0) goto LOOP
    // Adding R1 to R2
    @R1
    D = M
    @R2
    M = M + D
    // Adding 1 to i
    @i
    M = M + 1
    D = M
    @R0
    D = M - D
    // Goto LOOP if i < R0, otherwise it continues to END
    @LOOP
    D;JGT
(END)
    @END
    0;JMP
