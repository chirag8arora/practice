#Homework 3 (Xin Zhou 0522261)

##Chapter 7
*7. Describe a situation in which the add operator in a programming language would not be commutative.*

- **such as a + fun(b), and fun(b) will change a**

*20. Consider the following C program:What is the value of x after the assignment statement in main, assuming*

- *operands are evaluated left to right*
- *operands are evaluated right to left*

```
int fun(int *i){
    *i += 5;
    return 4;
}
void main(){
    int x = 3;
    x = x + fun(&x);
}
```

- **7**
- **12**

*21. Why does Java specify that operands in expressions are all evaluated in left-to-right order?*

- **Because Java is an associative language because associative in common language is evaluated from left to right.**

## Chapter 9

*5. Consider the following program written in C syntax:*
*For each of the following parameter-passing methods, what are all of the values of the variables value and list after each of the three calls to swap?*

- *Passed by value*
- *Passed by refrence*
- *Passed by value-result*

```
void swap(int a, int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}
void main(){
    int value = 2, list[5] = {1,3,5,7,9};
    swap(value, list[0]);
    swap(list[0], list[1]);
    swap(value, list[value]);
}
```

- **VALUE = 2; LIST = 1, 3, 5, 7, 9**
- **VALUE = 2; LIST = 3, 1, 5, 7, 9**
- **VALUE = 2; LIST = 3, 1, 5, 7, 9**

*15. What are at least two arguments against the use of pass-by-name parameters?*

- **Pass-by-name can have unsafe semantic effects.**
- **Pass-by-name is difficult to implement. Argument expressions must be compiled to special parameterless procedures called thunks. These thunks are passed into the called procedure and used whenever necessary to evaluate or re-evaluate the argument.**

## Chapter 14

*1. What did the designers of C get in return for not requiring subscript range checking?*

- **Execution overhead of the range checking is very high. Not requiring subscript range checking in C could save a lot resources and time.**
