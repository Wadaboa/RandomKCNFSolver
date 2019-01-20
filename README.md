# RandomKCNFSolver
This repository provides tools to generate random K-CNF(M, N) formulas and check their satisfiability, by using a WalkSAT algorithm implementation. You can get a brief help on how to use these tools by running `python randomkcnfsolver.py --help` or `python randomkcnfsolver.py -h` from the command line.

Software was made using python version 3.7.
If you have both python 2 and python 3 installed on your machine, you should run `python3 randomkcnfsolver.py`.
From now on I'll call `python randomkcnfsolver.py` or `python3 randomkcnfsolver.py` → `<header>`.

# Prerequisites
Software was made using the following libs:
* NumPy (http://www.numpy.org/)
* Matplotlib (https://matplotlib.org/)

# Usage
First of all, download the *Source Files* folder on your system. Now, open a terminal window and navigate to that folder. if you just run the program using `<header>` it will automatically start as if you typed `<header> -o plot` or `<header> --output plot`. You can also start the software using the following, not required, options:
1. `<header> -o model` or `<header> --output model`: Computes a single random K-CNF(M, N) formula and returns a model that satisfies it or failure. You can also provide additional (optional) inputs and combine them together:
    * `<header> -o model -k K`: K represents the K factor in a single randomly generated K-CNF(M, N) formula. Defaults to 10.
    * `<header> -o model -m M`: M represents the M factor in a single randomly generated K-CNF(M, N) formula. Defaults to 10.
    * `<header> -o model -n N`: N represents the N factor in a single randomly generated K-CNF(M, N) formula. Defaults to 5.
    * `<header> -o model -p P`: Probability of going for a 'random walk' in WalkSAT. Defaults to 0.5.
    * `<header> -o model -f FLIPS` or `<header> -o model --flips FLIPS`: Maximum number of iterations in WalkSAT. Defaults to 1000.
1. `<header> -o plot` or `<header> --output plot`: Computes random K-CNF(M, N) formulas and displays two plots which relates M/N ratio with P(satisfiable) and WalkSAT runtime. You can also provide additional (optional) inputs and combine them together:
    * `<header> -o plot -k K`: As described above.
    * `<header> -o plot --max_m MAX_M`: Maximum M factor for a randomly generated M to use in a K-CNF(M, N) formula. Defaults to 100.
    * `<header> -o plot --max_n MAX_N`: Maximum N factor for a randomly generated M to use in a K-CNF(M, N) formula. Defaults to 50.
    * `<header> -o plot -p P`: As described above.
    * `<header> -o plot -f FLIPS` or `<header> -o model --flips FLIPS`: As described above.
    * `<header> -o plot -t TRIES` or `<header> -o plot --tries TRIES`: Number of different tries to average P(satisfiable) per each M/N ratio. Defaults to 5.
    * `<header> -o plot -l LOOPS` or `<header> -o plot --loops LOOPS`: Number of different M/N ratios to generate. Defaults to 30.
    
Remember to grant executable permissions for each file in the *Source Files* folder, using `chmod +x <source_file.py>`.
