
# Ecson Hsu
# ecsonh

.text

##############################
# PART 1 FUNCTIONS
##############################


setCell:
    
    lw $t5, 0($sp)
    li $t0, 0xffff0000
    li $t1, 0
    li $t2, 10
    bge $a0, $t2, error
    bge $a1, $t2, error
    bltz $a0, error
    bltz $a1, error
    bgt $a3, 0x0f, error
    bgt $t5, 0x0f, error
    blt $a3, 0x00, error
    blt $t5, 0x00, error
    
	mul $t3, $a0, $t2 #j * row
	add $t3, $t3, $a1
	sll $t3, $t3, 1
	add $t3, $t3, $t0 #t3 is the address
	sll $t5, $t5, 4  #t5 background
	add $t5, $a3, $t5 #color
	sb $a2, 0($t3)
	sb $t5, 1($t3) 

    li $v0, 0
    jr $ra
error:
	li $v0, -1
    jr $ra

######################################################################################
initDisplay:
    
    
    addi $sp $sp,-24
    sw $s5, 0($sp) 
    sw $ra, 4($sp)
    sw $s0, 8($sp)
	sw $s1, 12($sp)
	sw $s2, 16($sp)
	sw $s3, 20($sp)
    move $s3, $a0 #FG
    move $s5, $a1 #BG
    	li $s0, 0 # i = 0
    	
i_init:
	bge $s0, 10, done_init
	li $s1, 0 #j = 0
	
j_init:
	bge $s1, 10, done_j_init
	li $s2, '\0' #char empty
	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
	move $a3, $s3
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	addi $s1, $s1, 1
    	j j_init
    	
done_j_init:
	addi $s0, $s0, 1 #increment row
	j i_init
	
done_init:
	lw $s0, 8($sp)
	lw $s1, 12($sp)
	lw $s2, 16($sp)
	lw $s3, 20($sp)
	lw $s5, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 24
    jr $ra
######################################################################################

win:
	addi $sp, $sp, -24
	sw $s5, 0($sp)
	sw $ra, 4($sp)
	sw $s0, 8($sp)
	sw $s1, 12($sp)
	sw $s2, 16($sp)
	sw $s3, 20($sp)
	
	li $s0, 15 #fg while
	li $s1, 0 #bg black
	move $a0, $s0
	move $a1, $s1
	jal initDisplay
	
	
    #row 012, column 3,6  row 3 column 3456
    li $s0, 0 # i = 0
win_i:
	bgt $s0, 2, done_win_i
	li $s1, 3 #column
	li $s2, 'B'
	li $s3, 7 #grey for fg
	li $s5, 11 # yellow for bg
	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
	move $a3, $s3
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
	li $s1, 6
	move $a1, $s1
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	addi $s0, $s0, 1
	j win_i
	
done_win_i:
	li $s1, 3
done_win_i_loop:
	li $s0, 3
	move $a0, $s0
	move $a1, $s1
	bgt $s1, 6, w_i
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	addi $s1, $s1, 1
	j done_win_i_loop
	
w_i:
	li $s0, 5
w_loop:
	bge $s0, 10, w_loop2
	li $s1, 0 #column
	li $s2, 'E'
	li $s3, 15 #white
	li $s5, 1 # red
	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
	move $a3, $s3
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	li $s1, 4
	move $a1, $s1
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	addi $s0, $s0, 1
	j w_loop
	
w_loop2:
	li $s0, 8
	li $s1, 1 #column
	move $a0, $s0
	move $a1, $s1
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	li $s1, 3
	move $a1, $s1
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	li $s0, 7
	li $s1, 2
	move $a0, $s0
	move $a1, $s1
	addi $sp, $sp, -4
	
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
	
	li $s0, 5
i_word:
	bge $s0, 10, n_word
	li $s1, 5
	li $s2, 'F'
	li $s3, 13 #magneta
	li $s5, 12 #blue
	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
	move $a3, $s3
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	addi $s0, $s0, 1
	j i_word

n_word:
	li $s0, 5
n_loop:
	bge $s0, 10, n_word2
	li $s1, 6
	li $s2, '8'
	li $s3, 15 #white
	li $s5, 2 #green
	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
	move $a3, $s3
	
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	li $s1, 9
	move $a1, $s1
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
	addi $s0, $s0, 1
	j n_loop
	
n_word2:
	li $s0, 6
	li $s1, 7
	move $a0, $s0
	move $a1, $s1
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
	li $s0, 7
	li $s1, 8
	move $a0, $s0
	move $a1, $s1
	addi $sp, $sp, -4
	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
	
	lw $s0, 8($sp)
	lw $s1, 12($sp)
	lw $s2, 16($sp)
	lw $s3, 20($sp)
	lw $s5, 0($sp)
	lw $ra, 4($sp)
	addi $sp, $sp, 24
	jr $ra
##############################
# PART 2 FUNCTION
##########################################################################################

loadMap:
    #count bomb num?

    addi $sp, $sp, -32

    sw $s0, 4($sp)#file
    sw $s1, 8($sp)#cell array
    sw $s2, 16($sp)#bomb num
    sw $s3, 20($sp)#s3 is the current address
    sw $s4, 24($sp)
    sw $s5, 28($sp)
    
    move $s0, $a0 #file
    move $s1, $a1 #cell array
    li $t8, 0x80 #initilize the board
    
    li $t3, 0
    move $t1, $s1
initialize_loop:
	bge $t3, 100, openfile
	sb $t8, 0($t1)
	addi $t3, $t3, 1
	addi $t1, $t1, 1
	j initialize_loop
openfile:
	#t0 = file
 	#t1 = row
 	#t2 = column
     li $v0, 13 #openfile
     li $a1, 0 #flags
     li $a2, 0 #mode
     syscall
     move $t0, $v0 #the file
     
readfile:
     li $v0, 14 #how to read file
     move $a0, $t0
     move $a1, $sp
     li $a2, 4
     syscall
     beq $v0, 0, closefile
     lb $t1, 0($sp) #row
     addi $t1, $t1, -0x30
     lb $t5, 1($sp) #space
     lb $t2, 2($sp) #column
     addi $t2, $t2, -0x30
     lb $t6, 3($sp) #newline
     bge $s2, 100, loadMap_error #at most 99 bombs
     bne $t5, ' ', loadMap_error #position valid
     bne $t6, '\n', loadMap_error #position valid
     blt $t1, 0, loadMap_error #position valid
     blt $t2, 0, loadMap_error #position valid
     
     
	li $t7, 10
     li $t3, 0 #(0,0) board
loadMap_loop_i:
	bge $t3, 10, loadMap_i_end
	li $t4, 0
	
	loadMap_loop_j:
	bge $t4, 10, done_loop_i
	mul $s3, $t3, $t7
	add $s3, $s3, $t4 #s3 is the current address
	add $s3, $s3, $s1
	lb $t5, 0($s3)
	#check if the row and column have bomb
	bne $t4, $t2, no_bomb #current column == column in file
     	bne $t3, $t1, no_bomb
     	addi $s2, $s2, 1
   
     	li $t6, 0x20 #does have bomb
	or $t5, $t5, $t6
	sb $t5, 0($s3)
	#sb $t5, 0($s3) #store info into array
     	
     	adjacent_bomb:
	li $t6, 1
	
	
	top_left:
	beq $t3, 0, top
	beq $t4, 0, top
	addi $t9, $t3, -1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, -1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	top:
	beq $t3, 0, top_right
	addi $t9, $t3, -1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	top_right:
	beq $t3, 0, mid_right
	beq $t4, 9, mid_right
	addi $t9, $t3, -1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, 1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1#add 001
	sb $t5, 0($s4)
	
	mid_right:
	beq $t4, 9, bottom_right

	mul $s4, $t3, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, 1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	bottom_right:
	beq $t4, 9, bottom
	beq $t3, 9, bottom
	addi $t9, $t3, 1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, 1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	bottom:
	beq $t3, 9, bottom_left
	addi $t9, $t3, 1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right

	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	bottom_left:
	beq $t3, 9, mid_left
	beq $t4, 0, mid_left
	addi $t9, $t3, 1
	mul $s4, $t9, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, -1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1 #add 001
	sb $t5, 0($s4)
	
	mid_left:
	beq $t4, 0, readfile
	mul $s4, $t3, $t7
	add $s4, $t4, $s4 #bomb on the right
	addi $s4, $s4, -1
	add $s4, $s4, $s1
	lb $t5, 0($s4)
	addi $t5, $t5, 1#add 001
	sb $t5, 0($s4)
	j readfile
	
	no_bomb:

     	addi $t4, $t4, 1
     	j loadMap_loop_j
     	
done_loop_i:
	addi $t3, $t3, 1
	j loadMap_loop_i
	
	
loadMap_i_end:
	beq $s2, 0, loadMap_error #at most 99 bombs
    

#Close the file 
closefile:
	li   $v0, 16       # system call for close file
	move $a0, $t0      # file descriptor to close
	syscall            # close file
    
    li $v0, 0
    lw $s0, 4($sp)
    lw $s1, 8($sp)
    lw $s2, 16($sp)
    lw $s3, 20($sp)
    lw $s4, 24($sp)
    lw $s5, 28($sp)
    addi $sp, $sp, 32
    jr $ra
loadMap_error:
	li   $v0, 16       # system call for close file
	move $a0, $t0      # file descriptor to close
	syscall        
	li $v0, -1
    lw $s0, 4($sp)
    lw $s1, 8($sp)
    lw $s2, 16($sp)
    lw $s3, 20($sp)
    lw $s4, 24($sp)
    lw $s5, 28($sp)
    addi $sp, $sp, 32
    jr $ra

####################################################################################################################
# PART 3 FUNCTION
##############################

mapReveal:
    #Define your code here
    addi $sp, $sp, -32
    sw $ra 0($sp)
    sw $s0, 4($sp) #move rol
    sw $s1, 8($sp) #move col
    sw $s3, 12($sp)#gamestatus
    sw $s5, 16($sp)#cell array
    sw $s2, 20($sp)
    sw $s4, 24($sp)
    sw $s6, 28($sp)

    move $s0, $a0
    move $s1, $a1
    move $s3, $a3
    beq $a2, 1, win_reveal #gameStatus
    beqz $a2, ongoing
    
    
    li $s4, 0 #row = 0
loop_map_i:
	bge $s4, 10, done_loop_map_i
   	li $s6, 0 #column = 0
	loop_map_j:
    	bge $s6, 10, done_loop_map_j
    	lbu $t2, 0($s3)
    	li $t8, 0xB0 #10110000
    	and $t3, $t2, $t8#if it's a flag bomb
    	beq $t3, $t8, map_flag_bomb
    	
    	li $t8, 0xA0 #10100000
    	and $t3, $t2, $t8#if it's a bomb
    	beq $t3, $t8, map_bomb
    	
    	li $t8, 0x90 #10010000
    	and $t3, $t2, $t8
    	beq $t3, $t8, map_flag_wrong
    	
    	li $t8, 0x80 # 10000000
    	beq $t2, $t8, map_empty
    	
    	move $a2, $t2
    	sub $a2, $a2, $t8
    	addi $a2, $a2, 0x30
    	
    	j map_num
    	
    	
    	
    	
    	map_bomb:
    	move $a0, $s4
    	move $a1, $s6
    	li $a2, 'B'
    	li $a3, 7 #grey
    	li $s5, 0 #black
    	j to_loop_j
    	
    	map_num:
    	move $a0, $s4
    	move $a1, $s6
    	li $a3, 13 #bright meg
    	li $s5, 0 #black
    	j to_loop_j
    	
    	map_flag_bomb:
    	move $a0, $s4
    	move $a1, $s6
    	li $a2, 'F'
    	li $a3, 12 #bright blue
    	li $s5, 10 #bright green
    	j to_loop_j
    	
    	map_flag_wrong:
    	move $a0, $s4
    	move $a1, $s6
    	li $a2, 'F'
    	li $a3, 12 #bright blue
    	li $s5, 9 #bright red
    	j to_loop_j
    	
    	map_empty:
    	move $a0, $s4
    	move $a1, $s6
    	li $a2, '\0'
    	li $a3, 15 #white
    	li $s5, 0 #black
    	
to_loop_j:
	addi $sp, $sp, -4
    	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	addi $s6, $s6, 1
    	addi $s3, $s3, 1
    	j loop_map_j
    	
done_loop_map_j:
	addi $s4, $s4, 1
	j loop_map_i
	
	
done_loop_map_i:
	#map_explode_bomb
	move $a0, $s0
	move $a1, $s1
    	li $a2, 'E'
    	li $a3, 15 #white
    	li $s5, 9 #bright red
    	addi $sp, $sp, -4
    	sw $s5, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4
    	
	j done_map

win_reveal:
	jal win
	j done_map
    
ongoing:

done_map:
	lw $ra 0($sp)
    lw $s0, 4($sp) #move rol
    lw $s1, 8($sp) #move col
    lw $s3, 12($sp)#gamestatus
    lw $s5, 16($sp)#cell array
    lw $s2, 20($sp)
    lw $s4, 24($sp)
    lw $s6, 28($sp)
    addi $sp, $sp, 32
    jr $ra
#########################################################################
# PART 4 FUNCTIONS
##############################

playerMove:
	lw $t4, 0($sp)#FG
	lw $t5, 4($sp)#BG
   addi $sp, $sp, -40
	sw $ra, 0($sp)
	sw $s0, 4($sp)#array
    sw $s1, 8($sp)#row
    sw $s2, 16($sp)#column
    sw $s3, 20($sp)#action
    sw $s4, 24($sp)#FG
    sw $s5, 28($sp)#BG
    sw $s6, 32($sp)
    sw $s7, 36($sp)

        
    
    move $s0, $a0
    move $s1, $a1
    move $s2, $a2
    move $s3, $a3
    move $s4, $t4
    move $s5, $t5
    
    bltz $s1, player_error
    bltz $s2, player_error
    bge $s1, 10, player_error
    bge $s2, 10, player_error
    
    li $t0, 10
    mul $s6, $t0, $s1
    add $s6, $s6, $s2
    add $s6, $s6, $s0
    lbu $t2, 0($s6)
    andi $t3, $t2, 0x40
    beq $t3, 0x40, player_error #revealed
	
    beq $s3, 'F', flag_that_shit
    beq $s3, 'f', flag_that_shit
    beq $s3, 'r', reveal
    beq $s3, 'R', reveal
    j player_error
    

flag_that_shit:
	andi $t3, $t2, 0x90 #10010000 flagged bomb
	beq $t3, 0x90, flagged
	beq $t3, 0x80, n_flag

flagged:
	addi $t2, $t2, -0x10
	sb $t2, 0($s6)
	move $a0, $s1
	move $a1, $s2
	li $a2, '\0'
    	move $a3, $s5
    	move $s7, $s4
	j r_loop_j
	
n_flag:
	addi $t2, $t2, 0x10
	sb $t2, 0($s6)
	move $a0, $s1
	move $a1, $s2
	li $a2, 'F'
    	li $a3, 12 #bright blue
    	li $s7, 7 #grey
	j r_loop_j
reveal:

	li $t8, 0xA0 #10100000
    	and $t3, $t2, $t8#reveal bomb
    	beq $t3, $t8, r_bomb
    	
    	
    	li $t8, 0x80 # 10000000
    	beq $t2, $t8, r_empty
    	li $t8, 0x90 # 10010000
    	beq $t2, $t8, r_empty
    	
    	li $t8, 0x80 # 10000000
    	

    	andi $t2, $t2, 0xEF #flag or unflagged num
    	ori $t2 $t2, 0x40
    	move $a2, $t2
    	
    	addi $a2, $a2, -0xC0
    	addi $a2, $a2, 0x30
    	
    	j r_num
    	
  
    	r_bomb:
    	andi $t2, $t2, 0xEF #11101111
    	sb $t2, 0($s6)
    	move $a0, $s1
    	move $a1, $s2
    	li $a2, 'E'
    	li $a3, 9 #grey
    	li $s7, 15 #black
    	j r_loop_j
    	
    	r_num:
    	sb $t2, 0($s6)
    	move $a0, $s1
    	move $a1, $s2
    	
    	li $a3, 13 #bright meg
    	li $s7, 0 #black
    	j r_loop_j
    	
    	
    	r_empty:
    	ori $t2, $t2, 0x40 #11001111
    	sb $t2, 0($s6)
    	move $a0, $s0
	move $a1, $s1
	move $a2, $s2
    	jal revealCells
    	move $a0, $s1
    	move $a1, $s2
    	li $a2, '\0'
    	li $a3, 15 #white
    	li $s7, 0 #black
r_loop_j:
	
	addi $sp, $sp, -4
    	sw $s7, 0($sp)
    	jal setCell
    	addi $sp, $sp, 4

	
	j player_pass
player_error:
	li $v0, -1
	j player_done
player_pass:
	li $v0, 0
player_done:
	lw $ra, 0($sp)
    lw $s0, 4($sp)#array
    lw $s1, 8($sp)#row
    lw $s2, 16($sp)#column
    lw $s3, 20($sp)#action
    lw $s4, 24($sp)
    lw $s5, 28($sp)
    lw $s6, 32($sp)
    lw $s7, 36($sp)
    addi $sp, $sp, 40
    
    ##########################################
    jr $ra

gameStatus:
    li $t0, 0
    move $t1, $a0
 
    check_explode:
    bge $t0, 100, game_loop
    add $t2, $t0, $t1
    lbu $t2, 0($t2)
    andi $t3, $t2, 0xF0
    beq $t3, 0xE0, lose
    addi $t0, $t0, 1
    j check_explode
    
game_loop:
    li $t0, 0
    gameStatus_loop:
    bge $t0, 100, win_game
    lbu $t1, 0($a0)
    li $t3, 0xE0
    and $t2, $t1, $t3
    beq $t2, $t3, lose
    
    li $t3, 0xB0
    and $t2, $t1, $t3
    beq $t2, $t3, loop_back #flag on bomb

    beq $t2, 0x90, done_gameStatus
    beq $t2, 0xA0, done_gameStatus

loop_back:
	addi $t0, $t0, 1
	addi $a0, $a0, 1
	j gameStatus_loop
lose:
	li $v0, -1
    jr $ra

done_gameStatus:
	beq $t1, 0, win_game
    li $v0, 0
    jr $ra

win_game:
	li $v0, 1
    jr $ra

##############################
# PART EC FUNCTIONS
##############################

revealCells:
    #Define your code here
    jr $ra


#################################################################
# Student defined data section
#################################################################
.data
.align 2  # Align next items to word boundary
cells_array: .space 200

