// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
(START)
    //Storing the screen value in i
    @SCREEN
    D = A
    @i
    M = D
    //Access the keyboard and store whether a key is pressed or not
    @KBD 
    D = M
    //Jump if a key is pressed to set the screen to black
    @SETBLACK
    D;JGT
    //Jump if a key is pressed to set the screen to white
    @SETWHITE
    D;JEQ
(SETBLACK)
    //Set the fill color to black
    D = -1
    //Fill the first pixel with the fillcolor
    @i
    A = M 
    M = D
    //Check to see if screen is fully black
    @i
    D = M + 1
    @KBD
    D = A - D
    //Increments to fill the next pixel 
    @i
    M = M + 1
    //Go to the start if the whole screen is black
    @START
    D;JLE
    //Checking if the key is still pressed, if still pressed loop SETBLACK again, otherwise start over
    @KBD
    D = M
    @SETBLACK
    D;JGT
    @START
    0;JMP
(SETWHITE)
    //Set the fill color to white
    D = 0
    //Fill the first pixel with the fillcolor
    @i
    A = M 
    M = D
    //Check to see if screen is fully white
    @i
    D = M + 1
    @KBD
    D = A - D
    //Increments to fill the next pixel 
    @i
    M = M + 1
    //Go to the start if the whole screen is white
    @START
    D;JLE
    //Checking if the key is still pressed, if still not pressed loop SETWHITE again, otherwise start over
    @KBD
    D = M
    @SETWHITE
    D;JEQ
    @START
    0;JMP