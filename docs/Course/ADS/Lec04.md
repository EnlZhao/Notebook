---
password: 21@ZJU@ADS
---

# Backtracking

DFS + purning = backtracking

Turnpike problem

* For every d remaining in D, at least one of its endpoints is not determined
* For maximum d remaining in D, at least one of its endpoints is a~0~ or a~n-1~

```c
bool Reconstruct(DistType X[ ], DistSet D, int N, int left, int right)
{
    /* X[1]...X[left-1] and X[right+1]...X[N] are solved */
    bool Found = false;
    if ( Is_Empty( D ) ) return true; /* solved */
    D_max = Find_Max( D ); /* option 1：X[right] = D_max */
    /* check if |D_max-X[i]|D is true for all X[i]’s that have been solved */
    OK = Check( D_max, N, left, right ); /* pruning */
    if ( OK ) {
        /* add X[right] and update D */
        X[right] = D_max;
        for ( i=1; i<left; i++ )
            Delete( |X[right]-X[i]|, D);
        for ( i=right+1; i<=N; i++ )
            Delete( |X[right]-X[i]|, D);
        Found = Reconstruct ( X, D, N, left, right-1 );
        if ( !Found ) {
            /* if does not work, undo */
            for ( i=1; i<left; i++ )
                Insert( |X[right]-X[i]|, D);
            for ( i=right+1; i<=N; i++ )
                Insert( |X[right]-X[i]|, D);
        }
    } /* finish checking option 1 */
    if ( !Found ) { /* if option 1 does not work */
        /* option 2: X[left] = X[N]-D_max */
        OK = Check( X[N]-D_max, N, left, right );
        if ( OK ) {
            X[left] = X[N] – D_max;
            for ( i=1; i<left; i++ )
                Delete( |X[left]-X[i]|, D);
            for ( i=right+1; i<=N; i++ )
                Delete( |X[left]-X[i]|, D);
            Found = Reconstruct (X, D, N, left+1, right );
            if ( !Found ) {
                for ( i=1; i<left; i++ )
                    Insert( |X[left]-X[i]|, D);
                for ( i=right+1; i<=N; i++ )
                    Insert( |X[left]-X[i]|, D);
            }
        } /* finish checking option 2 */
    } /* finish checking all the options */
    return Found;
}
```

* worst case: O(2^n) (rare)
* best case: O(n) (most instances)

Game - Tic-Tac-Toe

