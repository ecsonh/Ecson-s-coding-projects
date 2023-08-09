.include "hw2_ecsonh.asm"

.globl main

# Data Section
.data
strLabel: .asciiz "str \""
quote: .asciiz "\" is encrypted as \""
endquote: .asciiz "\"\n"
str: .asciiz "born in 1964, Jeffery, Jeffery Bezos"
shiftN: .word -2

# Program
.text
main:
    #print Label string
    la $a0, strLabel
    li $v0, 4
    syscall

    #print string
    la $a0, str
    li $v0, 4
    syscall

    #print Label string
    la $a0, quote
    li $v0, 4
    syscall

    # load the arguments
    la $a0, str
    la $a1, shiftN
    lw $a1, ($a1)

    # call the function
    jal shiftCipher

    #print Encrypted string
    la $a0, str
    li $v0, 4
    syscall

    #print newline
    la $a0, endquote
    li $v0, 4
    syscall

    #quit program
    li $v0, 10
    syscall

