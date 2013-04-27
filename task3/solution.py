class Person:
    def __init__(self, name, birth_year, gender,
                 father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self._children = []
        self.father = father
        self.mother = mother
        self._add_child(father, mother)

    def _add_child(self, *parents):
        for parent in parents:
            if parent:
                parent._children.append(self)

    def _get_relatives(self, gender):
        from_mam, from_dad = [], []
        if self.mother:
            from_mam = [c for c in self.mother.children(gender) if self != c]
        if self.father:
            from_dad = [c for c in self.father.children(gender) if self != c]
        return list(set(from_mam + from_dad))

    def get_brothers(self):
        return self._get_relatives('M')

    def get_sisters(self):
        return self._get_relatives('F')

    def children(self, gender=None):
        if gender:
            return [c for c in self._children if c.gender == gender]
        else:
            return self._children

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        person1 = [self.name, self.gender, self.birth_year]
        parents1 = [self.mother, self.father]
        person2 = [other.name, other.gender, other.birth_year]
        parents2 = [other.mother, other.father]
        return person1 == person2 and parents1 == parents2

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_direct_successor(self, child):
        return child in self._children
