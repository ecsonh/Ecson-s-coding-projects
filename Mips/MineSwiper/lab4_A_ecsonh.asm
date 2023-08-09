# Ecson Hsu
# ecsonh

.text
sumArray:
	li $t0, 0 #sum
	li $t1, 0 #i
	addi $t2, $a2, -1
	move $t3, $a0 #store a0 in t3
sumloop:
	bge $t1, $a1, sum_over
        mul $t5, $t1, $a2
        add $t5, $t5, $t2
        sll $t5, $t5, 2
        add $t5, $t5, $t3
        lw $t4, 0($t5) #load into t4
        add $t0, $t0, $t4
        addi $t1, $t1, 1 #increment
        j sumloop
sum_over:
	move $v0, $t0
	jr $ra

initArray:
		li $t0, 0 #sum
	li $t1, 0 #i
	addi $t2, $a2, -1
	move $t3, $a0 #store a0 in t3
initloop:
	bge $t1, $a1, init_over
        mul $t5, $t1, $a2
        add $t5, $t5, $t2
        sll $t5, $t5, 2
        add $t5, $t5, $t3
        sw $t0, 0($t5) #load into t4
        addi $t1, $t1, 1 #increment
        j initloop
init_over:
	move $v0, $t0
	jr $ra


