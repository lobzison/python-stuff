print("test of integer division")
let a = 3
let b = 2

print(a / b) // 1

print("test of constant redefenition")

print(/*let a:Double = 3
let b:Double = 2
invalid, need to declare a new constant*/)

let c:Double = 3
let d:Double = 2

print(c / d) // 1.5

print("test of negative reminder")
let x = -9
let y = 4

print(x % y) // -1
print("imitate python reminder")
print((x % y) + y)

print("simple loop")
var i = 0
while i < 10 { // if youll miss the space after <= you're fucked
    print(i)
    i += 1
}

print("lest try to compare tuples")
print((1, "a") == (1, "a"))
print((2, "a") > (1, "a"))
print("cant compare print((2, \"a\") > (1, 0.0)), datatypes should be the same")

print("conditional operator ? :")
while i < 10 {
    print(i)
    print(i > 6 ? "more then 6" : "less than 6")
    i += 1
}
