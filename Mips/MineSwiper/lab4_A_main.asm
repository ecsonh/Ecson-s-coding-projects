.include "lab4_A_ecsonh.asm"

.globl main
.text
main:

    # load the argument registers
    la $a0, myarray
    la $a1, rows
    lw $a1, 0($a1)
    la $a2, cols
    lw $a2, 0($a2)

    # call the function
    jal sumArray

    # save the return value
    move $s0, $v0

    # print string
    li $v0, 4
    la $a0, total
    syscall

    # print return value
    li $v0, 1
    move $a0, $s0
    syscall
    
    # print newline
    li $v0, 4
    la $a0, newline
    syscall

    # load the argument registers
    la $a0, myarray
    la $a1, rows
    lw $a1, 0($a1)
    la $a2, cols
    lw $a2, 0($a2)

  
    # call the function
    jal initArray

    # load the argument registers
    la $a0, myarray
    la $a1, rows
    lw $a1, 0($a1)
    la $a2, cols
    lw $a2, 0($a2)

    jal sumArray
    # save the return value
    move $s0, $v0

    # print string
    li $v0, 4
    la $a0, total2
    syscall

    # print return value
    li $v0, 1
    move $a0, $s0
    syscall
    
    # print newline
    li $v0, 4
    la $a0, newline
    syscall

    # Exit the program
    li $v0, 10
    syscall

.data

#set to [2][10], try [4][5], [5][4], [4][4], [2][4]
# or any combination of row*cols less than 20 for the given array
rows: .word 2   
cols: .word 10

myarray: .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

total: .asciiz "The total sum of the last column of the array is: "
total2: .asciiz "The total sum of the last column of the array, after calling initArray, is: "
newline: .asciiz "\n"
