# Creating a set
my_set = {10, 20, 30, 40, 50}
print("Original set:", my_set)

# Set does not allow duplicates
dup_set = {10, 20, 20, 30}
print("Set with duplicates (automatically removed):", dup_set)

# Creating an empty set (use set(), not {})
empty = set()
print("Empty set:", empty)

# Adding elements
my_set.add(60)
print("After adding 60:", my_set)

# Adding multiple items (update)
my_set.update([70, 80, 90])
print("After update with list:", my_set)

# Removing elements
my_set.remove(20)  # Throws error if not found
print("After removing 20:", my_set)

# Discard (no error if element not found)
my_set.discard(999)
print("After discard (999 not present):", my_set)

# Pop (removes random item)
popped = my_set.pop()
print("Popped item:", popped)
print("Set after pop:", my_set)

# Clear the set
temp_set = {1, 2, 3}
temp_set.clear()
print("Cleared set:", temp_set)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

# Union
print("Union:", a.union(b))

# Intersection
print("Intersection:", a.intersection(b))

# Difference
print("A - B:", a.difference(b))
print("B - A:", b.difference(a))

# Symmetric difference
print("Symmetric Difference:", a.symmetric_difference(b))

# Subset, Superset, Disjoint
print("Is A subset of B?", a.issubset(b))
print("Is A superset of B?", a.issuperset(b))
print("Are A and B disjoint?", a.isdisjoint(b))
