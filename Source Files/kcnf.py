#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *

class KCNF(object):
    
    FIRST_CHAR = 'A'
    LAST_CHAR = 'Z'

    def __init__(self, k, m, n):
        self.literals = []
        self.clauses = set([])
        self.generate_literals(n)
        self.generate_clauses(k, m, n)

    def generate_clauses(self, k, m, n, max_time = 2000):
        elapsed_time = 0
        start_time = timeit.default_timer()
        while len(self.clauses) < m and elapsed_time < max_time:
            clause_len = 0
            elapsed_time = (timeit.default_timer() - start_time) * 1000
            while (clause_len < k or clause_validity) and elapsed_time < max_time:
                clause_list = np.random.choice(self.literals, k, replace = False)
                clause = frozenset(clause_list)
                clause_len = len(clause)
                clause_validity = self.is_tautology(clause)
                if clause_len == k and not clause_validity: self.clauses.add(clause)
        if elapsed_time >= max_time: self.clauses = FAILURE

    def generate_literals(self, n):
        symbol = self.FIRST_CHAR
        for i in range(n):
            self.literals.append(symbol);
            self.literals.append(NEGATION_CHAR + symbol);
            symbol = self.next_symbol(symbol)

    def next_char(self, c):
        return chr(ord(c) + 1) if c != self.LAST_CHAR else self.FIRST_CHAR

    def next_symbol(self, current):
        all_z = current.rstrip(self.LAST_CHAR)
        if not all_z: return self.FIRST_CHAR * (len(current) + 1)
        nsubs = len(current) - len(all_z)
        next = all_z[:-1] + self.next_char(all_z[-1])
        next += self.FIRST_CHAR * nsubs
        return next

    def is_tautology(self, clause):
        for literal in clause:
            if literal in clause and self.negated_literal(literal) in clause: return True
        return False

    def negated_literal(self, literal):
        return literal[1:] if literal.startswith(NEGATION_CHAR) else NEGATION_CHAR + literal;
