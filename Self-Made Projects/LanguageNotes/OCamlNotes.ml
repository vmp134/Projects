(*This is a block comment.
It spans multiple lines.*)

(*To declare variables, functions, and else, use "let", with two semicolons.*)
let myInt = 80;;
let myString = "Hello World!";;

(*There are some unique operators in ocaml*)

let floatmult = 2.5 *. 3.0;; (*Float Multiplier*)

(*OCaml is very similar to python, with lists, tuples, and the like.*)

(*Like java, we use two equals to compare.
Uniquely, we compare pointer locations.*)

if (80 == myInt) then print_string "True"
else print_string "False"

(*OCaml is IMMUTABLE. Once things are declared, they stay that way.*)

(*To create Lists, use :: to construct, with a::b meaning element a is prepended to list b.
To describe lists, we do [a;b;c].*)

let newList = 9::[1;2;3];;

(*To pull lists apart, we need to pattern match. This becomes crucial in recursion.*)

let rec sum a l = 
  match l with 
  | [] -> (a + 0)             (*Empty list case.*)
  | (x::xs) -> sum (a+x) xs   (*List of type x::xs, where we use recursion.*)

(*The wildcard is noted by _, used for any type.
Shadowing is where you rebind a name in an inner scope for a different meaning.*)

let x = 3;
let g x = x + 3;;

