.include "hw3_ecsonh.asm"   # change this line

.globl main
.data
return_string: .asciiz "The return value is ("
comma_string: .asciiz ", "
end_string: .asciiz ")\n"

str: 	  .asciiz "FIND"
pattern: .asciiz "AD"  	
	


.text
main:
    la $a0, str    # print string
    li $v0, 4
    syscall

    li $a0, '\n'    #print newline
    li $v0, 11
    syscall

	# Load arguments
	la $a0, str
	la $a1, pattern
    li $a2, 'A'

	# Function call
	jal find_glob

    move $t0, $v0
    move $t1, $v1

	la $a0, return_string
	li $v0, 4
	syscall

    move $a0, $t0
    li $v0, 1
    syscall

	la $a0, comma_string
	li $v0, 4
	syscall

    move $a0, $t1
    li $v0, 1
    syscall

	la $a0, end_string
	li $v0, 4
	syscall


	# Terminate
	li $v0, 10
	syscall

