import unittest
from src.graphs.mergingcommunities import MergingCommunities

class TestMergingCommunities(unittest.TestCase):

    def test_merging_communities(self):
        output = []
        people = MergingCommunities(5)
        people.connect(0, 1),
        people.connect(1, 2),
        output.append(people.get_community_size(3)),
        output.append(people.get_community_size(0)),
        people.connect(3, 4),
        output.append(people.get_community_size(4)),
        self.assertEqual(output, [1, 3, 2])