# DO NOT MODIFY THIS FILE
# TREAT THIS FILE AS A BLACK BOX. ASSUME YOU DO NOT SEE THIS CODE

.text

printHistRow:
	li $t7, 58	# ':"
	li $t6, 0x20	# ' '
	li $t5, 11	# print char
	li $t4, 42	# ':"
	li $t3, 1	

	add $t2, $a1, $0   # copy of $a1, i	
	add $t1, $0, $a0   # copy of $a0, c	
	add $t0, $0, $0    # i = 0
	
	move $v0, $t5
	move $a0, $t1	  # get char to print 
	syscall

	move $v0, $t5
	add $a0, $0, $t7  # get char to print 
	syscall

	move $v0, $t5
	addi $a0, $t6, 0  # get char to print 
	syscall

printHistRow_Loop:
	bge $t0, $t2, printHistRow_Done
		move $v0, $t5
		move $a0, $t4  # get char to print 
		syscall
 	
		add $t0, $t0, $t3
	j printHistRow_Loop		

printHistRow_Done:
	jr $ra

#################################################

countChars:
	li $t9, 0	# count
	li $t8, 1	# 1
	add $t2, $a1, $0   # copy of $a1, c	
	add $t1, $0, $a0   # copy of $a0, str[]	

countChars_Loop:
	lb $t0, 0($t1)
	beq $t0, $0, countChars_Done
		bne $t0, $t2, countChars_nocount
			add $t9, $t9, $t8	# count++
countChars_nocount:
		add $t1, $t1, $t8
		j countChars_Loop	

countChars_Done:
	move $v0, $t9	# move count to return value
	jr $ra
