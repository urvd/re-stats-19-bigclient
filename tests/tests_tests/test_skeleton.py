# -*- coding: utf-8 -*-
import unittest


__author__ = "uriel"
__copyright__ = "uriel"
__license__ = "mit"

from random import random


class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)


if __name__ == '__main__':
    unittest.main()