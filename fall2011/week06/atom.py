#!/usr/bin/env python
"""
Assignment for week 7, Tues Nov 22, bring exercise to turn in (hardcopy)

Write a module atom.py that defines a class named Atom whose base
class is object.  An atom has a chemical symbol (a string).  An atom
can have chemical bonds to other atoms.  When an atom is created, it
has no bonds to other atoms.  Each atom can have no more than a
certain maximum number of bonds to other atoms.  When one atom has a
bond to another atom, the second atom must have a bond back to the
first.  An atom may have more than one bond to the same atom.  Every
atom has a method that returns a description string that contains its
chemical symbol, a unique identity, and the chemical symbols and
unique identities of all the atoms to which it has bonds.  The
identity in this string must be different in every atom, and must
always be the same in a given atom.

The atom module defines two more classes that represent hydrogen and
oxygen atoms, each with the base class Atom.  Every hydrogen atom has
the chemical symbol 'H' and has at most one bond.  Every oxygen atom
has the chemical symbol 'O' and has at most two bonds.

Also in atom.py, write code that tests the atom classes.  This test
code should execute only when the module is executed at top level, not
when it is imported.  This test code creates three hydrogen atoms and
two oxygen atoms.  Then this code creates bonds between one of the
oxygens and two of the hydrogens (forming a water molecule).  Then it
prints the description string of every atom.

Hints and reminders:
 This shouldn't take more than a page or two of code
 Use class attributes for data common to all instances of a class
 Instance attributes can be lists, you can have lists of objects
 Turn in what you have on Nov 22, even if it is not finished
"""
class Atom(object):
    def __init__( self,
                  symbol='',
                  max_bonds=0):
        """\
symbol = element symbol, etc.
        """
        self.symbol = symbol
        self.bonds = []
        self.max_bonds = max_bonds
        self.identity = id(self)
        return None

    def add_bond(self, atom):
        if len(self.bonds) < self.max_bonds:
            self.bonds.append(atom)
        else:
            print "First atom has already bonded %d times" % self.max_bonds

        if len(atom.bonds) < atom.max_bonds:
            atom.bonds.append(self)
        else:
            print "Second atom has already bonded %d times" % atom.max_bonds
        return None

    def description(self):
        return ("{\n\tAtom: symbol = " + 
                self.symbol +
                "\n\tbonds = " + 
                str([(atom.symbol, atom.identity)
                     for atom in self.bonds]) +
                "\n\tmax_bonds = " + 
                str(self.max_bonds) +
                "\n\tidentity = "+ 
                str(self.identity) + "\n}")

class Hydrogen(Atom):
    def __init__(self):
        Atom.__init__(self, symbol='H', max_bonds=1)
        return None

class Oxygen(Atom):
    def __init__(self):
        Atom.__init__(self, symbol='O', max_bonds=2)
        return None

if __name__ == "__main__":
    h1, h2, h3 = Hydrogen(), Hydrogen(), Hydrogen()
    o1, o2 = Oxygen(), Oxygen()

    o2.add_bond(h1)
    o2.add_bond(h3)

    print "h1 = ", h1.description()
    print "h2 = ", h2.description()
    print "h3 = ", h3.description()
    print "o1 = ", o1.description()
    print "o2 = ", o2.description()
