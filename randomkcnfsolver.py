from common import *
from kcnf import *
from walksat import *
        
def nCr(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n - k)

def model(k, m, n, max_flips, p):
    formula = KCNF(k, m, n)
    if formula.clauses == FAILURE:
        print("Error while computing clauses set.")
        sys.exit()
    print("Clauses set: ")
    print(formula.clauses)
    solver = WalkSAT(formula.clauses)
    result = solver.solve(max_flips, p)
    if result == FAILURE: print("Couldn't figure out satisfiability.")
    else: print("Model: " + str(result))

def plot(loops, tries, k, max_m_value, max_n_value, max_flips, p):
    prob = dict()
    time = dict()    
    for i in range(loops):
        m = np.random.randint(1, max_m_value)
        n = np.random.randint(k, max_n_value)
        print("M = " + str(m) + " / N = " + str(n))
        ratio = m / n
        prob[ratio] = 0
        time[ratio] = 0
        if nCr(2 * n, k) > m:
            for j in range(tries):
                print("Test #" + str(j + 1))
                formula = KCNF(k, m, n)
                if formula.clauses == FAILURE: break
                solver = WalkSAT(formula.clauses)
                start_time = timeit.default_timer()
                result = solver.solve(max_flips, p)
                stop_time = timeit.default_timer()
                if result != FAILURE: prob[ratio] += 1
                time[ratio] += (stop_time - start_time) * 1000
            prob[ratio] /= tries
            time[ratio] /= tries
            print("")
    
    plt.subplot(1, 2, 1)
    x, y = zip(*sorted(prob.items()))
    plt.xlim(0, 8)
    plt.ylim(0, 1)
    plt.xlabel('Clause/Symbol ratio M/N')
    plt.ylabel('P(satisfiable)')
    plt.plot(x, y, marker = "x")

    plt.subplot(1, 2, 2)
    x, y = zip(*sorted(time.items()))
    plt.xlim(0, 8)
    plt.ylim(0, 2000)
    plt.xlabel('Clause/Symbol ratio M/N')
    plt.ylabel('Runtime')
    plt.plot(x, y, marker = "x")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'randomkcnfsolver', description = "Random KCNF formulas generator and WalkSAT solver implementation")
    parser.add_argument('-o', '--output', default = 'plot', choices = ['plot', 'model'], help = "'plot': Computes random K-CNF(M, N) formulas and displays two plots which relates M/N ratio with P(satisfiable) and WalkSAT runtime; 'model': Computes a single random K-CNF(M, N) formula and returns a model that satisfies it or failure. Defaults to 'plot'.")
    parser.add_argument('-p', default = 0.5, type = float, help = "[--output = 'plot' or --output = 'model'] Probability of going for a 'random walk' in WalkSAT. Defaults to 0.5.")
    parser.add_argument('-f', '--flips', default = 1000, type = int, help = "[--output = 'plot' or --output = 'model'] Maximum number of iterations in WalkSAT. Defaults to 1000.")
    parser.add_argument('-k', default = 3, type = int, help = "[--output = 'plot' or --output = 'model'] K factor in a K-CNF(M, N) formula. Defaults to 3.")
    parser.add_argument('-l', '--loops', default = 30, type = int, help = "[--output = 'plot'] Number of different M/N ratios to generate. Defaults to 30.")
    parser.add_argument('-t', '--tries', default = 5, type = int, help = "[--output = 'plot'] Number of different tries to average P(satisfiable) per each M/N ratio. Defaults to 5.")
    parser.add_argument('--max_m', default = 100, type = int, help = "[--output = 'plot'] Maximum M factor for a randomly generated M to use in a K-CNF(M, N) formula. Defaults to 100.")
    parser.add_argument('--max_n', default = 50, type = int, help = "[--output = 'plot'] Maximum N factor for a randomly generated M to use in a K-CNF(M, N) formula. Defaults to 50.")
    parser.add_argument('-m', default = 10, type = int, help = "[--output = 'model'] M factor in a K-CNF(M, N) formula. Defaults to 10.")
    parser.add_argument('-n', default = 5, type = int, help = "[--output = 'model'] N factor in a K-CNF(M, N) formula. Defaults to 5.")
    args = parser.parse_args()

    if args.output == 'model': model(args.k, args.m, args.n, args.flips, args.p)
    else: plot(args.loops, args.tries, args.k, args.max_m, args.max_n, args.flips, args.p)
    sys.exit()
