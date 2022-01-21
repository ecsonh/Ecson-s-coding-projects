.include "hw2_netid.asm"

.globl main

# Data Section
.data
strLabel: .asciiz "reverseString of \""
qoute: .asciiz"\" is "
str: .asciiz "ICS51 Rules"
revstr: .asciiz "123456789111111111111"
newline: .asciiz "\n"




# Program 
.text
main:

    # load the arguments
    la $a0, str
    la $a1, revstr

    # call the function
    jal reverseString

    # save the return value
    move $t0, $v0

    #print Label string
    la $a0, strLabel
    li $v0, 4
    syscall

    #print string
    la $a0, str
    li $v0, 4
    syscall

    #print Label string
    la $a0, qoute
    li $v0, 4
    syscall
    
    #print reversed string
    la $a0, revstr
    li $v0, 4
    syscall

    #print newline 
    la $a0, newline
    li $v0, 4
    syscall

    #quit program
    li $v0, 10
    syscall

