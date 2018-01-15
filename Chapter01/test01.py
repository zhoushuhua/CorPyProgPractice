import re

# m  = re.match("foo", "foo")
# if m is not None:
#     print(m.group())

# m = re.match("foo", "bar")
# if m is not None: print(m.group())


#m = re.match("foo", "food on the table")
#if m is not None: print(m.group())

# m = re.match("foo", "seafood")
# if m is not None: print(m.group())

# m = re.search("foo", "seafood")
# if m is not None:
#    print(m.group())


bt = "bat|bet|bit"
"""
m = re.match(bt, "bat")
if m is not None: print(m.group())
"""

"""
m = re.match(bt, "bit")
if m is not None: print(m.group())
"""

"""
m = re.match(bt, "He bit me!")
if m is not None: print(m.group())
"""

"""
m = re.search(bt, "He bit me!")
if m is not None: print(m.group())
"""
"""
anyend = ".end"
m = re.match(anyend, "bend")
if m is not None:
    print(m.group())

m = re.match(anyend, "end")
if m is not None:
    print(m.group())

m = re.match(anyend, "\nend")
if m is not None:
    print(m.group())

m = re.search(anyend, "The end.")
if m is not None:
    print(m.group())
"""

"""
patt314 = "3.14"
pi_patt = "3\.14"
m = re.match(pi_patt, "3.14")
if m is not None:
    print(m.group())

m = re.match(patt314, "3014")
if m is not None:
    print(m.group())

m = re.match(patt314, "3.14")
if m is not None:
    print(m.group())
"""

"""
m = re.match("[cr][23][dp][o2]", "c3po")
if m is not None:
    print(m.group())

m = re.match("[cr][23][dp][o2]", "c2do")
if m is not None:
    print(m.group())

m = re.match("r2d2|c3po", "c2do")
if m is not None:
    print(m.group())

m = re.match("r2d2|c3po", "r2d2")
if m is not None:
    print(m.group())
"""

"""
# 需要添加？表示非贪婪匹配
patt = "\w+@(\w+\.)?\w+.com"
print(re.match(patt, "nobody@xxx.com").group())
print(re.match(patt, "nobody@www.xxx.com").group())
"""

"""
m = re.match("\w\w\w-\d\d\d", "abc-123")
if m is not None:
    print(m.group())

m = re.match("\w\w\w-\d\d\d", "abc-xyz")
if m is not None:
    print(m.group())

m = re.match("(\w\w\w)-(\d\d\d)", "abc-123")
if m is not None:
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
"""

m = re.match("ab", "ab")
print(m.group())
print(m.groups())

m = re.match("(ab)", "ab")
print(m.group())
print(m.group(1))
print(m.groups())

m = re.match("(a)(b)", "ab")
print(m.group(1))
print(m.group(2))
print(m.group())
print(m.groups())

m = re.match("(a(b))", "ab")
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())
