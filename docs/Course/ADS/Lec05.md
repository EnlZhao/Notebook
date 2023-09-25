---
password: 21@ZJU@ADS
---

# Divide and Conquer

!!! note
    * Recursivel
     
        1. **Divide** the problem into a number of sub-problems
        2. **Conquer** the sub-problems by solving them recursively
        3. **Combine** the solutions to the sub-problems into the solution for the original problem

    * General recursive: $T(N) = aT(a/b) + f(N)$ 

Three methods for solving recurrences:

$$
T(N) = aT(N/b) + f(N)
$$

* Substitution method
* Recursion tree method
* Master method

??? success "Details to be ignored"
    * if( $N/b$ ) is an integer or not
    * always assume $T(N) = \Theta(1)$ for small $N$

## Substitution method

> Guess, then prove by induction

!!! example "Example"

    === "Question"
        * $T(N) = 2T(\lfloor N/2 \rfloor) + N$ 
        * Guess: $T(N) = O(NlogN)$


    === "Proof"
        * Assume it is true for all $m < N$ , in particular, for $m = \lfloor N/2 \rfloor$
        * Then there eexists a constant $c$ such that $T(m) \leq c m log m$
        * Subsituting into the recurrence:
            $$
            T(N) = 2T(\lfloor N/2 \rfloor) + N
                \leq 2c \lfloor N/2 \rfloor log \lfloor N/2 \rfloor + N
                \leq c N (log N - log 2) + N
                \leq c N log N for c \geq 1
            $$

