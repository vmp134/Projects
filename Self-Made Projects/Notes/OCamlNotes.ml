(*This is a block comment.
It spans multiple lines.*)

(*To declare variables, functions, and else, use "let", with two semicolons.*)
let myInt = 80;;
let myString = "Hello World!";;

(*There are some unique operators in ocaml*)

let floatmult = 2.5 *. 3.0;; (*Float Multiplier*)

(*OCaml is very similar to python, with lists, tuples, and the like.*)

(*For comparison, we use = to check values and == for memory locations.
For Conditionals, we also require the return type to be the same.*)

if (80 = myInt) then print_string "True"
else print_string "False"

(*OCaml is IMMUTABLE. Once things are declared, they stay that way.*)

(*To create Lists, use :: to construct, with a::b meaning element a is prepended to list b.
To describe lists, we do [a;b;c].*)

let newList = 9::[1;2;3];;

(*To pull lists apart, we need to pattern match. This becomes crucial in recursion.*)

let rec sum a l = 
  match l with 
  | [] -> a                   (*Empty list case.*)
  | (x::xs) -> sum (a+x) xs   (*List of type x::xs, where we use recursion.*)

(*Usually, recursion takes up a lot of stack frames, so we use an accumulator for tail recursion.
This function is of type int -> int list -> int, where you have initial variables into return type.*)

(*The wildcard is noted by _, used for any type.
Shadowing is where you rebind a name in an inner scope for a different meaning.*)

let x = 3;
let g x = x + 3;;

(*Key functions that are alternatives to rec are List.map and List.fold.
fold_left and fold_right - only fold_left is tail recursive.*)

let sumFold l = List.fold_left (fun a x - > a + x) 0 l

let addOne l = List.map (fun x -> x + 1) l

(*Parsing and lexing
For a lexer, the simplest implementation is a bunch of else if code blocks to check regex
A better implementation is a list of tuples (regex, (fun _ -> token)) that ensures no priority issues*)

