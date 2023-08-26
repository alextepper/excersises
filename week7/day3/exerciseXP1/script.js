// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    // Here, the value of 'a' will be 3 because the condition a > 1 is true and hence a gets reassigned to 3.
    alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne() // Will alert: "inside the funcOne function 3"

// #1.2
// If the variable is declared with 'const' instead of 'let', an error will be thrown when you try to reassign a value to 'a' inside the if block.


//#2
let a = 0;
function funcTwo() {
    a = 5; // This reassigns the global variable 'a' to 5.
}

function funcThree() {
    // Here, the function will alert the value of global variable 'a'
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree() // Will alert: "inside the funcThree function 0"
funcTwo()   // Will reassign the global variable 'a' to 5
funcThree() // Will alert: "inside the funcThree function 5"

// #2.2
// If the global variable 'a' is declared with 'const' instead of 'let', an error will be thrown when you try to reassign a value to 'a' inside funcTwo().


//#3
function funcFour() {
    window.a = "hello"; // This assigns a global variable 'a' to the string "hello".
}

function funcFive() {
    // This will alert the value of global variable 'a'
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()  // This will assign the string "hello" to the global variable 'a'.
funcFive()  // Will alert: "inside the funcFive function hello"


//#4
let b = 1;
function funcSix() {
    let a = "test"; 
    // Inside this function, there's a local variable 'a' that shadows the global variable. So, the local 'a' will be used.
    alert(`inside the funcSix function ${a}`);
}

// #4.1 - run in the console:
funcSix() // Will alert: "inside the funcSix function test"

// #4.2
// If the inner variable 'a' is declared with 'const' instead of 'let', there won't be any difference in this case. The function will still alert "test".


//#5
let c = 2;
if (true) {
    let a = 5;
    // Inside the if block, there's a local 'a' that shadows the outer variable. So, the inner 'a' will be alerted.
    alert(`in the if block ${a}`);
}
// This will alert the value of the outer 'a' variable since the inner 'a' only exists within the scope of the if block.
alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console:
// It will alert: "in the if block 5" and then "outside of the if block 2"

// #5.2 
// If the inner variable 'a' in the if block is declared with 'const' instead of 'let', the behavior remains the same. It will still alert the same messages.
