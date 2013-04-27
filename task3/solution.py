from collections import defaultdict


class Person:
    def __init__(self, name, birth_year, gender,
                 father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.children_list = defaultdict(list)
        self.father = father
        if self.father:
            self.father.add_child(self)
        self.mother = mother
        if self.mother:
            self.mother.add_child(self)

    def add_child(self, child):
        self.children_list[child.gender].append(child)

    def get_children(self, gender):
        if self.mother and self.father:
            children = self.mother.children_list[gender]
            for child in self.father.children_list[gender]:
                if child not in children:
                    children.append(child)
            return [child for child in children if child != self]
        elif self.father:
            return [c for c in self.father.children_list[gender] if self != c]
        elif self.mother:
            return [c for c in self.mother.children_list[gender] if self != c]
        else:
            return []

    def get_brothers(self):
        return self.get_children('M')

    def get_sisters(self):
        return self.get_children('F')

    def children(self, **gender):
        if gender:
            key = gender['gender']
            return self.children_list[key]
        else:
            return self.children_list.values()

    def __eq__(self, other):
        person1 = [self.name, self.gender, self.birth_year]
        parents1 = [self.mother, self.father]
        person2 = [other.name, other.gender, other.birth_year]
        parents2 = [other.mother, other.father]
        return person1 == person2 and parents1 == parents2

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_direct_successor(self, other):
        if self.children_list:
            for people in self.children_list.values():
                if other in people:
                    return True
        return False
