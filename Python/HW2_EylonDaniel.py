from functools import reduce


def q1(array_of_arrays):
    return reduce(lambda z, w: z + w, map(lambda x: sum(x), array_of_arrays))


print("\nQ1:")
print(q1([[12, 14], [1, 1], [2, 1], [3, 1]]))


def q2_hailstone(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            yield int(n / 2)
            n = n / 2
        else:
            yield int(n * 3 + 1)
            n = n * 3 + 1


class Q2HailstoneClass:
    def __init__(self, num):
        self.num = num
        self.first_time = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.first_time is True:
            self.first_time = False
            return int(self.num)
        if self.num <= 1:
            raise StopIteration
        elif self.num % 2 == 0:
            self.num = self.num / 2
            return int(self.num)
        else:
            self.num = self.num * 3 + 1
            return int(self.num)


print("\nQ2: A")
for i in q2_hailstone(5):
    print(i)

print("\nQ2 B:")
q2_class = Q2HailstoneClass(5)
it = q2_class.__iter__()
for i in it:
    print(i)

print("\nQ2 C:")

q2_generator_Expression = (i for i in q2_hailstone(5))
for n in q2_generator_Expression:
    print(n)

print("\nQ3 C:")
my_graph = {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': ['a'], 'e': ['d']}


def reachable(graph, node):
    list_of_reachable = [node]
    queue = [node]
    visited = {}
    for k in graph.keys():
        visited[k] = False
    while len(queue) > 0:
        u = queue[len(queue) - 1]
        queue.remove(u)
        visited[u] = True
        for v in graph[u]:
            if visited[v] is False:
                list_of_reachable.append(v)
                queue.append(v)
    return list_of_reachable


print(str(reachable(my_graph, 'a')))

# Q4:
# כפי שניתן לראות ערך ה- ID של LIST לא השתנה למרות פעולת השרשור בקטע הקוד הנתון, לעומת ערך ה- ID של ה- TUPLE שכן השתנה.
# ערך ה- TUPLE השתנה מכיוון שלא ניתן לשנות את ערכן של TUPLES בפייתון לאחר שהכרזנו עליהם (מוגדרים כ IMMUTABLE).
# ערך ה- ID של ה LIST לא משתנה כיוון שה REFERENCE שלו נשאר אותו דבר והוא ניתן לשינוי על פי הגדרות פייתון
# לעומת ערך ה- ID של ה- TUPLE שמשתנה כיוון שמוקצה מקום חדש בזיכרון-
# על מנת שלא ידרס ה- ID של ה- TUPLE הישן שהוגדר ב- VAR2 (שהוא IMMUTABLE).









