# Final Study Guide

## Section 1
#####1. What are the design issues for names?

> - case sensitive
> - reserve words or keywords

#####2. What is the potential danger of case-sensitive names?

> using the wrong variable with very similar name

#####3. In what way are reserved words better than keywords?

>

#####4. What is an alias?

> Variables when more than one variable name can be used to access the same memory location.


#####5. What category of C++ reference variables is always aliases?

> Union types. Union is a type whose variables may store different type values at different times during program execution.

#####6. What is the l-value of a variable? What is the r-value?

> l-value = address, r-value = value itself

#####7. Define binding and binding time.

> A binding in a program is an association of an attribute with a program component such as an identifier or a symbol. For example the data type of the value of a variable is an attribute that is associated with the variable name. The binding time for an attribute is the time at which the binding occurs. For example, in C the binding time for a variable type is when the program is compiled (because the type cannot be changed without changing and recompiling the program), but the value of the variable is not bound until the program executes (that is, the value of the variable can change during execution).

#####8. After language design and implementation [what are the four times bindings can take place in a program?]

> - ? language design time – bind operator symbols to operations
> - ? language implementation time – bind floating point type to a representation
> - ? writing time
> - compile time - bind a variable to a type in C or Java
> - load time - bind a C or C++ static variable to a memory cell
> - run-time - bind a non-static local variable to a memory cell

#####9. Define static binding and dynamic binding.

> A static binding is  if it first occurs before run time and remains unchanged throughout program execution. A dynamic binding is if it first occurs during execution or can change during execution of the program.

#####10. What are the advantages and disadvantages of implicit declarations?

> - Advantages: Simple in naming conventions. In this case, the compiler or interpreter binds a variable to a type based on the syntactic form of the variable’s name.
> - Disadvantages: Although they are a minor convenience to programmers, implicit declarations can be detrimental to reliability because they prevent the compilation process from detecting some typographical and programmer errors.

#####11. What are the advantages and disadvantages of dynamic type binding?

> - Advantages, It is more easy to write generic code.
> - Disadvantages, High Cost to check type and interpretation


#####12. Define static, stack-dynamic, explicit heap-dynamic, and implicit heap-dynamic variables. What are their advantages and disadvantages?

#####13. Define lifetime, scope, static scope, and dynamic scope.

#####14. How is reference to a nonlocal variable in a static-scoped program connected to its definition?

#####15. What is the general problem with static scoping?

## Section 2

#####1. What is a descriptor?

#####2. What are the advantages and disadvantages of decimal data types?

#####3. What are the design issues for character string types?

#####4. Describe the three string length options.

#####5. Define ordinal, enumeration, and subrange types.

#####6. What are the advantages of user-defined enumeration types?

#####7. In what ways are the user-defined enumeration types of C# more reliable than those of C++?

#####8. What are the design issues for arrays?

#####9. Define static, fixed static-dynamic, stack-dynamic, fixed heap-dynamic, and heap-dynamic arrays. What are the advantages of each?

## Problem sets



