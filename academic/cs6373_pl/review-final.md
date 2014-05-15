# Final Study Guide

## Section 1
#####1. What are the design issues for names?

> - case sensitive

> - reserve words or keywords

#####2. What is the potential danger of case-sensitive names?

> using the wrong variable with very similar name

#####3. In what way are reserved words better than keywords?

> Reserved words are better than keywords because the redefinition of keywords can be confusing, but not on reserved words.

#####4. What is an alias?

> Variables when more than one variable name can be used to access the same memory location.

#####5. What category of C++ reference variables is always aliases?

> Union types. Union is a type whose variables may store different type values at different times during program execution.

#####6. What is the l-value of a variable? What is the r-value?

> l-value = address, r-value = value itself

#####7. Define binding and binding time.

> - A binding in a program is an association of an attribute with a program component such as an identifier or a symbol. For example the data type of the value of a variable is an attribute that is associated with the variable name.

> - The binding time for an attribute is the time at which the binding occurs. For example, in C the binding time for a variable type is when the program is compiled (because the type cannot be changed without changing and recompiling the program), but the value of the variable is not bound until the program executes (that is, the value of the variable can change during execution).

#####8. After language design and implementation [what are the four times bindings can take place in a program?]

> - compile time - bind a variable to a type in C or Java

> - load time - bind a C or C++ static variable to a memory cell

> - link time

> - run-time - bind a non-static local variable to a memory cell

> - (FYI) language design time – bind operator symbols to operations

> - (FYI) language implementation time – bind floating point type to a representation

#####9. Define static binding and dynamic binding.

> A static binding is  if it first occurs before run time and remains unchanged throughout program execution. A dynamic binding is if it first occurs during execution or can change during execution of the program.

#####10. What are the advantages and disadvantages of implicit declarations?

> - Advantages: Simple in naming conventions. In this case, the compiler or interpreter binds a variable to a type based on the syntactic form of the variable's name.

> - Disadvantages: Although they are a minor convenience to programmers, implicit declarations can be detrimental to reliability because they prevent the compilation process from detecting some typographical and programmer errors.

#####11. What are the advantages and disadvantages of dynamic type binding?

> - Advantages, It is more easy to write generic code.

> - Disadvantages, High Cost to check type and interpretation

#####12. Define static, stack-dynamic, explicit heap-dynamic, and implicit heap-dynamic variables. What are their advantages and disadvantages?

> - Static: bound to memory cells before execution begins and remains bound to the same memory cell throughout the execution.(for example, using 'static' to define a variable in C, static int i = 1;)

> - Stack-dynamic: storage bindings are created for variables when their declaration statements are elaborated. (For example, the variable declarations that appear at the beginning of a Java method are elaborated when the method is called and the variables defined by those declarations are deallocated when the method completes its execution.)

> - Explicit heap-dynamic: allocated and deallocated by explicit directives, specified by the programmer, which take effect during execution. (for example, using 'new' to define a variable in JAVA, List l = new ArrayList<String>();)

> - Implicit heap-dynamic: Allocation and deallocation caused by assignment statements. (for example, highs = [74, 84, 86, 90, 71];)

#####13. Define lifetime, scope, static scope, and dynamic scope.

> - Lifetime: the lifetime of a variable is the period of time beginning when the method is entered and ending when execution of the method terminates.!

> - Scope: the scope of a variable is the range of statements over which the variable is visible.!

> - Static scope: static scope is binding names to non-local variables.!

> - Dynamic scope: Dynamic scoping is based on the calling sequence of subprograms, not on their spatial relationship to each other. Thus, the scope can be determined only at run time.!

#####14. How is reference to a nonlocal variable in a static-scoped program connected to its definition?

> Definition must be within a static ancestor (enclosing static scope).

#####15. What is the general problem with static scoping?

> Usually too much access. Scope structure destroyed as pgm evolves.

## Section 2

#####1. What is a descriptor?

> A descriptor is the collection of the attributes of a variable. It is convenient, both logically and concretely, to think of variables in terms of descriptors.

#####2. What are the advantages and disadvantages of decimal data types?

> - Decimal data types store a fixed number of decimal digits, with the decimal point at a fixed position in the value.
> - Decimal types have the advantage of being able to precisely store decimal values, at least those within a restricted range, which cannot be done with floating-point.
> - The disadvantages of decimal types are that the range of values is restricted because no exponents are allowed, and their representation in memory is wasteful.

#####3. What are the design issues for character string types?

> - Should strings be simply a special kind of character array or a primitive type (with no array-style subscripting operations)?
> - Should strings have static or dynamic length?

#####4. Describe the three string length options.

> - A static length string is a string whose length is static and set when the string is created.

> - A limited dynamic length string is a string that has a varying length up to a declared and fixed maximum set by the variable's definition.  Such string variables can store any number of characters between zero and the maximum.

> - A dynamic length string is a string that has a varying length and no maximum.  This option requires the overhead of dynamic storage allocation and deallocation but provides maximum flexibility.

#####5. Define ordinal, enumeration, and subrange types.

> - An ordinal type is one in which the range of possible values can be easily associated with the set of positive integers.  In Java, for example, the primitive ordinal types are integer, char, and boolean.

> - An enumeration type is one in which all of the possible values, which are named constants, are provided in the definition.  Enumeration types provide a way of defining and grouping collections of name constants, which are called enumeration constants.  An example in C#:
enum days {Mon, Tue, Wed, Thu, Fri, Sat, Sun};

> - A subrange type is a contiguous subsequence of an ordinal type.

#####6. What are the advantages of user-defined enumeration types?

> Enumeration types can provide advantages in both readability and reliability.  Readability is enhanced in a very direct way.  Named values are easily recognized, whereas coded values are not.  In the area of reliability, the enumeration types of Ada, C#, and Java 5.0 provide two advantages.  First, no arithmetic operations are legal on enumeration types.  Second, no enumeration variable can be assigned a value outside its defined range.

#####7. In what ways are the user-defined enumeration types of C# more reliable than those of C++?

> Because enumeration type variables in C# are never coerced to integer types

#####8. What are the design issues for arrays?

> - What types are legal for subscripts?

> - Are subscripting expressions in element references range-checked?

> - When are subscript ranges bound?

> - When does array allocation take place?

> - Are ragged or rectangular multidimensioned arrays allowed, or both?

> - Can arrays be initialized when they have their storage allocated?

> - What kinds of slices are allowed, if any?

#####9. Define static, fixed static-dynamic, stack-dynamic, fixed heap-dynamic, and heap-dynamic arrays. What are the advantages of each?

> - A static array is one in which the subscript ranges are statically bound and storage allocation is static (done before run time).  The advantage of static arrays is efficiency:  No dynamic allocation or deallocation is required.

> - A fixed stack-dynamic array is one in which the subscript ranges are statically bound, but the allocation is done at declaration elaboration time during execution.  The advantage of fixed stack-dynamic arrays over static arrays is space efficiency.

> - A stack-dynamic array is one in which the subscript ranges are dynamically bound and the storage allocation is dynamic (done during run time).  One the subscript ranges are bound and the storage is allocated, however, they remain fixed during the lifetime of the variable.  The advantage of stack-dynamic arrays over static and fixed stack-dynamic arrays is flexibility.  The size of an array need not be known until the array is about to be used.

> - A fixed heap-dynamic array is similar to the fixed stack-dynamic array, in that the subscript ranges are dynamically bound and the storage binding is dynamic, but they are fixed after storage is allocated.  The differences are that the bindings are done when the user program requests them, rather than at elaboration time, and the storage is allocated from the heap, rather than the stack.  Assumption (not stated in text):  The advantage of fixed heap-dynamic arrays is space efficiency.

> - A heap-dynamic array is one in which the binding of subscript ranges and storage allocation is dynamic and can change any number of times during the array's lifetime.  The advantage of heap-dynamic arrays over the others is flexibility.

## Problem sets



