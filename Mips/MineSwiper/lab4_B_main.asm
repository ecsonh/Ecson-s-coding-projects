.include "lab4_B_ecsonh.asm"
.include "lab4_functions.asm"

.globl main
.text
main:
    la $a0, myhist
	la $t0, rows
	lw $a1, 0($t0)
	jal printHist

	# print newline
    li $v0, 4
    la $a0, newline
    syscall
 	syscall

	la $a0, myhist
	la $t1, rows
	lw $a1, 0($t1)
	la $a2, str_hello
	jal countHist	

    la $a0, myhist
	la $t3, rows
	lw $a1, 0($t3)
	jal printHist

	li $v0, 10
	syscall

.data
n: .word 4

rows: .word 5   
myhist: .word 'A', 2, 'a', 3, '!', 0, 'L', 10, 'b', 4

str_hello: .asciiz "HeLLO!"
newline: .asciiz "\n"


