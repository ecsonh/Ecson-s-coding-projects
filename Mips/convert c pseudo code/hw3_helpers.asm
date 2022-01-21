# TREAT THIS FILE AS A BLACK BOX. ASSUME YOU DO NOT SEE THIS CODE
.text
# $a0: Starting address of string s
length:                 
    li $v0,0        
length_nextCh: 
    lb $t0, 0($a0)  
    beqz $t0,length_end 
    addi $v0,$v0,1  
    addi $a0,$a0,1  
    j length_nextCh        
length_end:
    jr $ra


# $a0: Starting address of string s
# $a1: Starting address of string t
equals:
    li $v0, 1 #assume equal       
equals_nextCh: 
    lb $t0, 0($a0)  
    lb $t1, 0($a1)  
    bnez $t0, equals_check
    beqz $t1, equals_endfound
equals_check:
    bne $t0, $t1, equals_not
    addi $a0, $a0, 1
    addi $a1, $a1, 1  
    j equals_nextCh        
equals_not:
    move $v0, $0
equals_endfound:
    jr $ra


# $a0: Starting address of array
# array length is assume to be 255 in all cases
find_empty:
    li $v0, -1
    li $t0, 0
    li $t8, 255
find_empty_loop:
    bge $t0, $t8, find_empty_done
    sll $t1, $t0, 2
    add $t1, $t1, $a0
    lw $t1, 0($t1)
    beq $t1, $v0, find_empty_found
    addi $t0, $t0, 1
    j find_empty_loop
find_empty_found:
    move $v0, $t0
find_empty_done:
    jr $ra