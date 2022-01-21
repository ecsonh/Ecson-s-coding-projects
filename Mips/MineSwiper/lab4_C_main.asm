.include "lab4_A_ecsonh.asm"
.include "lab4_B_ecsonh.asm"
.include "lab4_functions.asm"

.globl main
.text
main:
	la $s1, footer
	la $s2, strings
	la $s3, myhist
	la $t1, rows
	lw $s4, 0($t1)
	li $s5, 2
	add $s6, $0, $0
	la $t0, n
	lw $s7, 0($t0)

	move $a0, $s3
	move $a1, $s4
	move $a2, $s5
	jal initArray

	li $s0, 0
countStr:
	bge $s0, $s7, printHeader
	
	sll $t7, $s0, 2
	add $t8, $t7, $s2
	lw $t0, 0($t8)	  # strings[i]
	
	move $a0, $s3
	move $a1, $s4
	move $a2, $t0	
	jal countHist

	addi $s0, $s0, 1

	j countStr

printHeader:

	move $a0, $s3
	move $a1, $s4
	li $a2, 2
	jal sumArray
	move $s6, $v0	

	li $v0, 4
	la $a0, header
	syscall

	move $a0, $s3
	move $a1, $s4
	jal printHist

	li $v0, 4
	move $a0, $s1
	syscall

	li $v0, 4
	la $a0, stat1
	syscall
	li $v0, 1
	move $a0, $s7 
	syscall
	li $v0, 4
	la $a0, stat2
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall 
	li $s0, 0
printStr:
	bge $s0, $s7, printstat
	sll $t7, $s0, 2
	add $t8, $t7, $s2
	li $v0, 4
	la $a0, qoute
	syscall
	lw $a0, 0($t8)	  # strings[i]
	syscall
	la $a0, qoute
	syscall
	la $a0, newline
	syscall 
	addi $s0, $s0, 1
	j printStr
printstat:
	la $a0, stat1
	syscall
	li $v0, 1
	move $a0, $s4 
	syscall
	li $v0, 4
	la $a0, stat3
	syscall
	li $v0, 1
	move $a0, $s5 
	syscall
	li $v0, 4
	la $a0, stat4
	syscall

	move $a0, $s6
	li $v0, 1
	syscall
	li $v0, 4
	la $a0, newline
	syscall 
	li $v0, 10
	syscall

.data
strings: .word str_abc, str_hello, str_b, str_foo
n: .word 4

rows: .word 7   
myhist: .word 'A', 200, 'O', 7, '!', 100, 'L', 10, 'b', 4, 'h', 20, 'e', 4

str_foo: .asciiz "FOO"
str_hello: .asciiz "HeLLO!"
str_abc: .asciiz "Abc"
str_b: .asciiz "b"

header: .asciiz "########## HISTOGRAM ##########\n"
footer: .asciiz "###############################\n"
stat1: .asciiz "There are "
stat2: .asciiz " strings in the array.\nThe strings are "
qoute: .asciiz "\""
newline: .asciiz "\n"
stat3: .asciiz " rows and "
stat4: .asciiz " columns in the histogram.\nThe sum of the histogram is "
