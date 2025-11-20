"""
LINEAR SEARCH MASTER NOTES
Author: Ritik
Purpose: Long-term reference to understand how simple linear search evolves
from beginner level to high-performance + industry-level search strategies.

This file contains:
1. Basic linear search
2. Pythonic improvements
3. Edge cases + multiple matches
4. Optimal O(n) approach
5. Hash-based (O(1)) search
6. String & substring search
7. Nested data search
8. Pandas column search
9. Distributed search (Spark placeholder)
10. Semantic search (AI level placeholder)

NOTE:
Code sections using external libraries are optional and commented for modular use.
"""

# ------------------------------------------------------------------------------
# 1️⃣ BASIC LINEAR SEARCH (BEGINNER LEVEL)
# ------------------------------------------------------------------------------
def linear_search(arr, target):
    """
    Basic linear search:
    - Scans elements one by one
    - Returns first index if found else -1
    Time Complexity: O(n)
    Use Case:
        - Small lists, quick checks, competitive programming
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# Example
print("Basic Search:", linear_search([1, 2, 3, 4, 5], 4))


# ------------------------------------------------------------------------------
# 2️⃣ IMPROVED VERSION WITH EDGE CASE HANDLING
# ------------------------------------------------------------------------------
def linear_search_safe(arr, target):
    """
    Handles:
    - Empty list
    - None values
    - Invalid input
    Use Case:
        - Scripts that process user input / external data
    """
    if not arr or target is None:
        return -1
    
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


print("Safe Search:", linear_search_safe([], 3))


# ------------------------------------------------------------------------------
# 3️⃣ SEARCH ALL OCCURRENCES (DATA CLEANING / LOG ANALYSIS)
# ------------------------------------------------------------------------------
def linear_search_all(arr, target):
    """
    Returns list of all indexes where target appears.
    Useful for:
        - Log scanning
        - Duplicate detection
        - Analytics preprocessing
    """
    return [i for i, v in enumerate(arr) if v == target]


print("Multiple Occurrences:", linear_search_all([2, 3, 2, 5, 2], 2))


# ------------------------------------------------------------------------------
# 4️⃣ OPTIMIZED O(N) APPROACH WITH SET TRACKING (FASTER CHECKS)
# ------------------------------------------------------------------------------
def linear_search_fast(arr, target):
    """
    Performs lookup using set membership which is faster than list membership.
    Still scans linearly but membership check = O(1)
    Use Case:
        - Large data, repeated lookup
    """
    seen = set()
    for i, v in enumerate(arr):
        seen.add(v)
        if v == target:
            return i
    return -1


print("Fast Search:", linear_search_fast([10, 20, 30, 40], 30))


# ------------------------------------------------------------------------------
# 5️⃣ HASH MAP (O(1) LOOKUPS) — INDUSTRY STANDARD
# ------------------------------------------------------------------------------
def fast_lookup(arr):
    """
    Converts list to dictionary for O(1) lookup.
    Use Case:
        - Config lookup
        - Caching
        - Compiler symbol table
    Trade-off:
        - Extra memory but extremely fast lookups
    """
    return {v: i for i, v in enumerate(arr)}


lookup_table = fast_lookup([10, 20, 30])
print("Hash Lookup:", lookup_table.get(30))


# ------------------------------------------------------------------------------
# 6️⃣ SEARCH IN STRINGS (LOG PARSING / NLP)
# ------------------------------------------------------------------------------
def substring_search(text, target):
    """
    Searches substring inside text.
    Use Case:
        - Searching keywords in logs, chat messages, medical notes
    """
    return text.find(target)


print("Substring Search:", substring_search("Payment failed due to timeout", "timeout"))


# ------------------------------------------------------------------------------
# 7️⃣ SEARCH IN NESTED DATA (JSON / API / ETL)
# ------------------------------------------------------------------------------
def search_nested(data, target):
    """
    Searches recursively in nested lists/dicts.
    Use Case:
        - API JSON responses
        - Config files
        - Complex ETL pipeline validation
    """
    if isinstance(data, dict):
        return any(search_nested(v, target) for v in data.values())
    if isinstance(data, list):
        return any(search_nested(i, target) for i in data)
    return data == target


nested_data = {"users": [{"name": "A"}, {"name": "Ritik"}]}
print("Nested Search:", search_nested(nested_data, "Ritik"))


# ------------------------------------------------------------------------------
# 8️⃣ DATA ENGINEERING — COLUMN SEARCH (PANDAS)
# ------------------------------------------------------------------------------
"""
Uncomment to use

import pandas as pd

df = pd.DataFrame({"values": [5, 10, 15, 20]})
print(df[df["values"] == 15])
"""

# ------------------------------------------------------------------------------
# 9️⃣ BIG DATA — SPARK DISTRIBUTED SEARCH (PSEUDOCODE)
# ------------------------------------------------------------------------------
"""
Used when dataset is huge (GB/TB scale)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("search").getOrCreate()
df = spark.read.csv("data.csv")
result = df.filter(df.column == target)
result.show()
"""

# ------------------------------------------------------------------------------
# 🔟 SEMANTIC SEARCH (AI LEVEL) — CONCEPT ONLY
# ------------------------------------------------------------------------------
"""
Used when meaning matters, not text match.

Example: Searching for "heart attack" should match "myocardial infarction"

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
query = model.encode("heart attack")
"""

# End of File
print("\n--- FILE EXECUTED SUCCESSFULLY ---")
