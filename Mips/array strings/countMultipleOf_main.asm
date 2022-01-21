.include "hw2_netid.asm"

.globl main

# Data Section
.data
array: .word 0,2,0,7,0
.word 100
array_len: .word 3
k: .word 7
strLabel1: .asciiz " countMultipleOf("
comma: .asciiz ", "
strLabel2: .asciiz ") returned values: ("
paren: .asciiz ")\n"

# Program 
.text
main:

    # load the arguments
    la $a0, array
    la $a1, array_len
    lw $a1, 0($a1)
    la $a2, k
    lw $a2, 0($a2)

    # call the function
    jal countMultipleOf

    # save the return values
    move $t8, $v0
    move $t9, $v1

    #print label
    la $a0, strLabel1
    li $v0, 4
    syscall

    #print argument value - array address in hex
    la $a0, array
    li $v0, 34
    syscall

    #print comma
    la $a0, comma
    li $v0, 4
    syscall

    #print argument value - len in decimal
    la $a0, array_len
    lw $a0, 0($a0)
    li $v0, 1
    syscall

    #print comma
    la $a0, comma
    li $v0, 4
    syscall

    #print argument value - k in decimal
    la $a0, k
    lw $a0, 0($a0)
    li $v0, 1
    syscall

    #print label2
    la $a0, strLabel2
    li $v0, 4
    syscall

    #print return value1
    move $a0, $t8
    li $v0, 1
    syscall

    #print comma
    la $a0, comma
    li $v0, 4
    syscall

    #print return value2
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

