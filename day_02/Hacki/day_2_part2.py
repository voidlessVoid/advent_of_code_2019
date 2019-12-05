"""An Intcode program is a list.txt of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0).

Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.


1 : Opcode 1 adds together numbers read from two positions and stores the result in a third position.

	-  The three integers immediately after the opcode tell you these three positions
	-  the first two indicate the positions from which you should read the input values,
	-  and the third indicates the position at which the output should be stored.


	For example, if your Intcode computer encounters 1,10,20,30,
	it should read the values at positions 10 and 20, add those values,
	and then overwrite the value at position 30 with their sum.


2 : Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
	- Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions."""

ls = open('list.txt', 'r')

for line in ls.readlines():
	ls = line.rstrip().split(',')
	ls = [int(i) for i in ls]

def int_comp(list_input = None, exit_instruction = 99, instruction_pointer = 0):

	if list_input is None:
		print('integer data list required')

	else:

		computed_list = list_input.copy() # copy of input_list to keep in memory otherwise pointer will be replaced and the original list is overwritten

		while computed_list[instruction_pointer] != exit_instruction: # while the list value is unequal (exit_instruction = 99) do...

			parameters = [instruction_pointer+1, instruction_pointer+2, exit_instruction] # parameter list to calculate len and address parameters
			instructions = {1: computed_list[computed_list[parameters[0]]] + computed_list[computed_list[parameters[1]]], # instruction dictionary with keys 1,2,...
					        2: computed_list[computed_list[parameters[0]]] * computed_list[computed_list[parameters[1]]]}

			calc = instructions[computed_list[instruction_pointer]] # read and compile dict key respectively to list value on instruction_pointer
			computed_list[computed_list[instruction_pointer + len(parameters)]] = calc # replace list entry [instruction_pointer + sum of len(parameters) by calculation
			instruction_pointer += len(parameters)+1 # advance in list by length of parameters and len(instruction_pointer)

		return {'in' : list_input, 'out' : computed_list} # output dictionary with original list and computed list

def output_search(required_output = 19690720, list_input = None, outputposition = 0):

	import random as rn # to generate random numbers

	ls_input, output = int_comp(list_input = list_input)['in'], int_comp(list_input = list_input)['out'][outputposition] # predefinition of in and output

	while output != required_output: # while the output is unequal to required_output rerun output calculation with randomized integern values for noun and verb

		noun, verb = rn.randint(0,99), rn.randint(0,99) # randomize integer in between 0,99
		ls_input[1], ls_input[2] = noun, verb # replace input keys by noun and verb
		output = int_comp(list_input = ls_input)['out'][outputposition] # recalculate output
		print(100*noun+verb) # required answer

output_search(list_input=ls)
