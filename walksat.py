#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *

class WalkSAT(object):    

    def __init__(self, clauses):
        self.model = dict()
        self.clauses = set([])
        self.clauses = clauses
        self.get_model()

    def at(self, s, n):
        i = 0
        for e in s:
            if i == n: return e
            i += 1
    
    def get_model(self):
        symbols = set([])
        for clause in self.clauses:
            for literal in clause:
                symbols.add(self.get_symbol(literal))
        self.model = {l : bool(np.random.randint(0, 1 + 1)) for l in symbols}

    def get_symbol(self, literal):
        return literal.replace(NEGATION_CHAR, EMPTY_CHAR)

    def is_literal_satisfiable(self, literal):
        if literal.startswith(NEGATION_CHAR): return not self.model[self.get_symbol(literal)]
        return self.model[literal]
    
    def is_clause_satisfiable(self, clause):
        for literal in clause:
            if self.is_literal_satisfiable(literal): return True
        return False

    def unsatisfied_clauses(self):
        unsatisfied_clauses = 0
        for clause in self.clauses:
            if not self.is_clause_satisfiable(clause): unsatisfied_clauses += 1
        return unsatisfied_clauses

    def get_random_clause(self):
        return self.at(self.clauses, np.random.randint(0, len(self.clauses)))

    def get_random_symbol(self, clause):
        return self.get_symbol(self.at(clause, np.random.randint(0, len(clause))))

    def get_maximizing_symbol(self, clause):
        min = len(self.clauses) + 1
        for literal in clause:
            symbol = self.get_symbol(literal)
            self.model[symbol] = not self.model[symbol]
            unsatisfied_clauses = self.unsatisfied_clauses()
            if unsatisfied_clauses < min:
                min = unsatisfied_clauses
                min_symbol = symbol
            self.model[symbol] = not self.model[symbol]
        return min_symbol

    def solve(self, max_flips = 1000, p = 0.5):
        check = False
        for i in range(max_flips):
            if self.unsatisfied_clauses() == 0: return self.model
            while not check:
                clause = self.get_random_clause()
                if not self.is_clause_satisfiable(clause): check = True
            check = False
            probability = np.random.uniform()
            if probability <= p: l = self.get_random_symbol(clause)
            else: l = self.get_maximizing_symbol(clause)
            self.model[l] = not self.model[l]
        return FAILURE
