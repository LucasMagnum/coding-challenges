/*
Is Unique:
	Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
*/
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 0 {
		fmt.Println("You need to inform a string")
		os.Exit(1)
	}

	userString := strings.ToLower(os.Args[1])

	fmt.Printf("Brute-force Solution (%v) -> %v \n", userString, bruteForceSolution(userString))
	fmt.Printf("HashMap Solution (%v) -> %v \n", userString, hashMapSolution(userString))
	fmt.Printf("BitArray Solution (%v) -> %v \n", userString, bitArraySolution(userString))

	os.Exit(0)
}

func bruteForceSolution(userString string) bool {
	/* This is a O(N2) solution without extra space */
	for index := 0; index < len(userString); index++ {
		for secondIndex := index + 1; secondIndex < len(userString); secondIndex++ {
			if userString[index] == userString[secondIndex] {
				return false
			}
		}
	}

	return true
}

func hashMapSolution(userString string) bool {
	/* This is a O(N) solution using an extra space */
	counter := make(map[rune]bool)

	for _, character := range userString {
		if _, found := counter[character]; found {
			return false
		}

		counter[character] = true
	}

	return true
}

func bitArraySolution(userString string) bool {
	checker := 0
	startCodePoint := 'a'

	for i := 0; i < len(userString); i++ {
		mask := 1 << (uint(userString[i]) - uint(startCodePoint))

		sameBits := checker & mask

		if sameBits > 0 {
			return false
		}

		checker = checker | mask
	}

	return true
}
