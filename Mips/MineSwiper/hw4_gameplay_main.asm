.include "hw4_ecsonh.asm"
.text

.globl main

# $a0, string to print
# $v0, return color
__inputColor:
	move $t1, $a0 
	li $v0, 4
	syscall

	li $v0, 5
	syscall

	bltz $v0, __inputColor_err
    li $t0, 15
	bgt $v0, $t0, __inputColor_err
    jr $ra

__inputColor_err:
    li $v0, 4
    la $a0, invalid_color_str
	syscall
	move $a0, $t1
	j __inputColor


main: 

	# store the filename given on the command line
	lw	$t0, 0($a1)
	la  $t1, filename
	sw	$t0, 0($t1)

	# load the map from the file we opened
	lw	$a0, 0($t1)
	la	$a1, cells_array
	jal	loadMap
	bltz $v0, invalid_file_error

    # Prompt the user for the initial board colors
    la $a0, fg_preset_str
    jal __inputColor
    move $s3, $v0

    la $a0, bg_preset_str
    jal __inputColor
    move $s2, $v0

    move $a0, $s3
    move $a1, $s2
	jal	initDisplay

	while_game:
        # Prompt player to enter row
        li $v0, 4
        la $a0, enter_row_str
        syscall	

        # Take user input for move
        li $v0, 5
        syscall
        move $s4, $v0

        # Prompt player to enter col
        li $v0, 4
        la $a0, enter_col_str
        syscall	

        # Take user input for move
        li $v0, 5
        syscall
        move $s5, $v0

        # Prompt player to enter move
        li $v0, 4
        la $a0, input_message
        syscall	

        # Take user input for action
        li $v0, 12
        syscall
        
		#perform_action based on user input
		la	$a0, cells_array
        move $a1, $s4
        move $a2, $s5
        move $a3, $v0
        addi $sp, $sp, -8
        sw $s3, 4($sp)
	    sw $s2, 0($sp)
    	jal	playerMove
        addi $sp, $sp, 8
		beqz $v0, continue

		# inform the user they have selected an invalid action
		la	$a0, invalid_action
		li	$v0, 4
		syscall

		# since we got bad input, jump back to prompt them again
		j	while_game

	continue:

		# the user successfully performed an action, so check game status
		la	$a0, cells_array
		jal	gameStatus

		# the game is ongoing, jump back to prompt for next action
		beqz $v0, while_game

        # call reveal_map because the game was won or lost
        move $a0, $s4
        move $a1, $s5
        move $a2, $v0
        la	$a3, cells_array
        jal	mapReveal

	exit:
	li	$v0,	10
	syscall

	invalid_file_error:
	# inform the user the file was bad (nonexistant, malformed, etc.)
	la	$a0,	file_error
	li	$v0,	4
	syscall
    j	exit




.data
fg_preset_str: .asciiz "\nEnter a number [0-15] for the board foreground color: "
bg_preset_str: .asciiz "\nEnter a number [0-15] for the board background color: "
invalid_color_str: .asciiz "\nInvalid color! Try again.\n"
enter_row_str: .asciiz "\nEnter the row: "
enter_col_str: .asciiz "\nEnter the col: "
input_message: .asciiz "R or r - reveal\nF or f - flag\nEnter your action: "
file_error: .asciiz "The file provided is either missing or in an invalid format."
invalid_action: .asciiz "The (row,col) or action performed is invalid."

.align 3
filename: .space 48
