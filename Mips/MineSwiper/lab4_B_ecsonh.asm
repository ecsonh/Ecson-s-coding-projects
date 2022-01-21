# Ecson Hsu
# ecsonh
.text
printHist:
	addi $sp, $sp, -20
	sw $s4, 0($sp) 
    	sw $s1, 4($sp) 
    	sw $s2, 8($sp) 
    	sw $s3, 16($sp) #str length
    	sw $ra, 12($sp)
    	
	li $s1, 0 #i
	li $s2, 2
	move $s3, $a0 #store a0 in t3
	move $s4, $a1
printloop:
	bge $s1, $s4, printover
        mul $t5, $s1, $s2 #i * num column
        addi $t6, $t5, 1 #row 1
        sll $t6, $t6, 2
        add $t6, $t6, $s3 #plus address
        lw $a1, 0($t6)
        sll $t5, $t5, 2
        add $t5, $t5, $s3
        lbu $a0, 0($t5)
        jal printHistRow
        li $a0, '\n'
        li $v0, 11
        syscall
        addi $s1, $s1, 1 #increment
        j printloop
printover:
	lw $s4, 0($sp) 
    	lw $s1, 4($sp) 
    	lw $s2, 8($sp) 
    	lw $s3, 16($sp) #str length
    	lw $ra, 12($sp)
    	addi $sp, $sp, 20
	jr $ra



countHist:
	addi $sp, $sp, -28
	sw $s4, 0($sp) 
    	sw $s1, 4($sp) 
    	sw $s2, 8($sp) 
    	sw $s3, 16($sp) #str length
    	sw $s5, 20($sp)
    	sw $s6, 24($sp)
    	sw $ra, 12($sp)
	li $s1, 0 #i = 0
	li $s2, 2
	move $s3, $a0 #store a0 in t3
	move $s4, $a1
	move $s5, $a2 
countloop:
	bge $s1, $s4, countover
	mul $t5, $s1, $s2 #i * num column
        addi $s6, $t5, 1 #row 1
        sll $s6, $s6, 2
        add $s6, $s6, $s3 #plus address
        sll $t5, $t5, 2
        add $t5, $t5, $s3
        lbu $a1, 0($t5)
        move $a0, $s5 #char
        jal countChars
        lw $a1, 0($s6)
        add $a1, $a1, $v0
        sw $a1, 0($s6)
        addi $s1, $s1, 1 #increment
        j countloop
   	# Place your code here
countover:
	lw $s4, 0($sp) 
    	lw $s1, 4($sp) 
    	lw $s2, 8($sp) 
    	lw $s3, 16($sp) #str length
    	lw $s5, 20($sp)
    	lw $s6, 24($sp)
    	lw $ra, 12($sp)
    	addi $sp, $sp, 28
	jr $ra
	

