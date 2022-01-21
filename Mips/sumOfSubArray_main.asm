.include "hw2_netid.asm"

.globl main

# Data Section
.data
array: .word 0,0,0,0,0
n: .word 5
arg_i: .word 3
arg_j: .word 0

strLabel1: .asciiz "Function returned: ("
comma: .asciiz ", "
paren: .asciiz ")\n"

# Program 
.text
main:

    # load the arguments
    la $a0, array
    la $a1, n
    lw $a1, 0($a1)
    la $a2, arg_i
    lw $a2, 0($a2)
    la $a3, arg_j
    lw $a3, 0($a3)

    # call the function
    jal sumOfSubArray

    # save the return values
    move $t8, $v0
    move $t9, $v1

    #print label
    la $a0, strLabel1
    li $v0, 4
    syscall

    #print first return value
    move $a0, $t8
    li $v0, 1
    syscall

    #print comma
    la $a0, comma
    li $v0, 4
    syscall

    #print second return value
    move $a0, $t9
    li $v0, 1
    syscall

    #print closing paren
    la $a0, paren
    li $v0, 4
    syscall
 
    #quit program
    li $v0, 10
    syscall

