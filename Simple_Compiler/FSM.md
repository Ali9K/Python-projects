. States:

	S0: Start state (before any input).
	S1: After reading 'a'.
	S2: After reading 'ab'.
	S3: After reading 'abb' (accepting state).

. Transitions:

	 From S0 (start state):
	. On input 'a' → transition to S1.
	. On input 'b' → stay in S0.

	 From S1:
	. On input 'a' → stay in S1.
	. On input 'b' → transition to S2.

	From S2:
	. On input 'b' → transition to S3 (accept state).
	. On input 'a' → go back to S1.

	From S3 (accept state):
	. On input 'b' → go back to S0.
	. On input 'a' → go back to S1.
	. If you have no input, accept the string, as it ends in "abb".

. FSM Diagram:

	S0 --a--> S1 --b--> S2 --b--> S3 (accept)
	S0 --b--> S0
	S1 --a--> S1
	S2 --a--> S1
	S3 --a--> S1
	S3 --b--> S0

