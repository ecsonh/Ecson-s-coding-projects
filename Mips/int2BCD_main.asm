.include "hw2_ecsonh.asm"

.globl main

# Data Section
.data
strLabel1: .asciiz "in2BCD returned " 

v: .word 19

# Program 
.text
main:

    # load the arguments
    la $a0, v       # v
    lw $a0, 0($a0)     
    jal int2BCD 

    # save the return value
    move $t0, $v0   

    #print label
    la $a0, strLabel1
    li $v0, 4
    syscall

printHex:
    #print BCD number in Hex
    move $a0, $t0
    li $v0, 34
    syscall


    #quit program
    li $v0, 10
    syscall

