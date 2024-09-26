"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
def solution(string_a, string_b):
    return string_a.endswith(string_b)

import unittest

class TestStringEndsWith(unittest.TestCase):

    # Cas de tests qui doivent retourner True
    fixed_tests_True = (
        ("samurai", "ai"),
        ("ninja", "ja"),
        ("sensei", "i"),
        ("abc", "abc"),
        ("abcabc", "bc"),
        ("fails", "ails"),
    )

    # Cas de tests qui doivent retourner False
    fixed_tests_False = (
        ("sumo", "omo"),
        ("samurai", "ra"),
        ("abc", "abcd"),
        ("ails", "fails"),
        ("this", "fails"),
        ("spam", "eggs"),
    )

    def test_fixed_tests_true(self):
        for string_a, string_b in self.fixed_tests_True:
            with self.subTest(string_a=string_a, string_b=string_b):
                self.assertTrue(solution(string_a, string_b))

    def test_fixed_tests_false(self):
        for string_a, string_b in self.fixed_tests_False:
            with self.subTest(string_a=string_a, string_b=string_b):
                self.assertFalse(solution(string_a, string_b))

if __name__ == '__main__':
    unittest.main()

