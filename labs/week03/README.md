# Lab 03 – Functions & Object-Oriented Programming

## Brief Overview

In this lab, I practiced using functions and object-oriented programming in Python. The tasks focused on breaking problems into reusable functions and creating classes to organize data and behavior.

## Task 1 – Data Cleaning Functions

I created functions to remove invalid sensor readings and calculate the average of the cleaned data.

**Design decision:** The cleaning and average calculations were placed in separate functions so each function has one clear responsibility.

## Task 2 – Student Record Processor

I used functions to calculate student averages, determine pass/fail status, and display a summary for each student.

**Design decision:** Separate functions make the code easier to reuse and understand.

## Task 3 – Simple Dataset Class

I created a `Dataset` class that stores numeric values and provides methods for counting data points and calculating the average.

**Design decision:** The dataset values are stored inside the object, while methods perform operations on that data.

## Task 4 – Rule-Based Classifier

I created a `RuleBasedClassifier` class that stores a threshold and classifies individual values or lists of values.

**Design decision:** The threshold is stored as an attribute so the same classifier object can be reused with different values.

## Concepts Practiced

- Function definitions
- Parameters and return values
- Functions calling other functions
- Lists and dictionaries
- Classes and objects
- Attributes
- Methods
- Constructors
- Conditional logic
- Loops
- Reusable and modular code

## Challenges Faced

One challenge was deciding how to divide each problem into smaller functions or class methods. I also had to understand how attributes and methods work together inside an object.

## AI/ML Relevance

Functions and classes are important in AI and machine learning because AI programs are usually divided into reusable components. For example, data cleaning, datasets, classifiers, and models can each be represented by separate functions or classes.

## Written Reflection

This lab helped me understand how functions make code reusable and organized, while OOP helps combine data and related behavior. One difficulty was understanding how class attributes and methods work together. These concepts are useful in AI and machine learning because large systems are built from separate, reusable components.