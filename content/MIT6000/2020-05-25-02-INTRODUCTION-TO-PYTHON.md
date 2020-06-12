---
title: 02 INTRODUCTION TO PYTHON
subtitle: 
author: John Qu
date: 2020-05-25
slug: introduction-to-python
tags:
- 
categories:
- MIT600
- ICPP booknotes
typora-root-url: ../../static
show_toc: yes
output: html_notebook
---

### What dimensions can be used to describe the difference between programming languages?

- Low-level versus high-level
- General versus targeted
- Interpreted versus compiled

Python is a general-purpose programming language that can be used effectively to build almost any kind of program that does not need direct access to the computer’s hardware.

### What is the disadvantages and advantages over other languages?

Python is not optimal for programs that have high reliability constraints (because of its weak static semantic checking) or that are built and maintained by many people or over a long period of time (again because of the weak static semantic checking).

## 2.1 The Basic Elements of Python

### What is objects and types in Python?

Objects are the core things that Python programs manipulate. Every object has a type that defines the kinds of things that programs can do with that object. 

Types are either scalar or non-scalar. Scalar objects are indivisible. Think of them as the atoms of the language. Non-scalar objects, for example strings, have internal structure. Many types of objects can be denoted by literals[^literal] in the text of a program. For example, the text `2` is a literal representing a number and the text `'abc'` a literal representing a string.

[^literal]: n. 印刷错误【计】 文字; 直接量; 字面量; 句节

### What is the relationship of an object and names?

Variables provide a way to associate names with objects. In Python, a variable is just a name, nothing more. Remember this—it is important. An assignment statement associates the name to the left of the = symbol with the object denoted by the expression to the right of the =. Remember this too. An object can have one, more than one, or no name associated with it.

### Why should we choose apt variable names?

Consider the two code fragments

```{python}
# too simple variable names
a = 3.14159 
b = 11.2
c = a*(b**2)

# meaningful variable names
pi = 3.14159
diameter = 11.2
area = pi*(diameter**2)
```

As far as Python is concerned, they are not different. When executed, they will do the same thing. To a human reader, however, they are quite different. When we read the fragment on the left, there is no a priori [^ a priori] reason to suspect that anything is amiss[^amiss]. However, a quick glance at the code on the right should prompt us to be suspicious that something is wrong. Either the variable should have been named radius rather than diameter, or diameter should have been divided by 2.0 in the calculation of the area.

[^ a priori]:  〖＜ラテン〗形容詞 副詞 演繹（えんえき）的な[に]; 先天[先験]的な[に] (↔ a posteriori ｟かたく｠ 帰納的な[に](inductive); 経験に基づいた[て])

[^amiss]: a.  Wrong; faulty; out of order; improper; as, *it may not be amiss to ask advice.* [Used only in the predicate 表语.] 

## 2.2 Branching Programs

### Why does Python set indentation to be semantically meaningful?

An advantage of the Python approach is that it ensures that the visual structure of a program is an accurate representation of the semantic structure of that program. Because indentation is semantically important, the notion of a line is important.

### What does it mean when we say a class of programs run in constant time?

A program for which the maximum running time is bounded by the length of the program is said to run in constant time. This does not mean that each time it is run it executes the same number of steps. It means that there exists a constant, k, such that the program is guaranteed to take no more than k steps to run. This implies that the running time does not grow with the size of the input to the program. Constant-time programs are quite limited in what they can do.

## 2.3 Strings and Input

### What can an overloaded operator do?

The operator `+` is said to be overloaded: It has different meanings depending upon the types of the objects to which it is applied. For example, it means addition when applied to two numbers and concatenation when applied to two strings.

### How do we instructs Python to use UTF-8 encoding?

The Unicode standard is a character coding system designed to support the digital processing and display of the written texts of all languages. The standard contains more than 120,000 different characters—covering 129 modern and historic scripts and multiple symbol sets. The Unicode standard can be implemented using different internal character encodings.

Insert a comment as the first or second line of your program.

```
# -*- coding: utf-8 -*-
```

If you don’t have such a comment in your program, most Python implementations will default to UTF-8.

## 2.4 Iteration

When we want a program to do the same thing many times, we can use **iteration**. A generic iteration (also called **looping**) mechanism is shown in the boxed-in part of Figure 2.4. Like a conditional statement, it begins with a test. If the test evaluates to True, the program executes the loop body once, and then goes back to reevaluate the test. This process is repeated until the test evaluates to `False`, after which control passes to the code following the iteration statement.

![image-20200525153045426](/images/2020-05-25-02-INTRODUCTION-TO-PYTHON//image-20200525153045426.png)

