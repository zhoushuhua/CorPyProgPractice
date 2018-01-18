# -*- coding: cp936 -*-
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
"""

"""
m = re.search("^The", "The end.")
if m is not None:
    print(m.group())

m = re.search("^The", "end. The") # 不匹配
if m is not None:
    print(m.group())

m = re.search(r"\bthe", "bite the dog")
if m is not None:
    print(m.group())

m = re.search(r"\bthe", "bitethe dog") # 不匹配
if m is not None:
    print(m.group())

m = re.search(r"\Bthe", "bitethe dog")
if m is not None:
    print(m.group())
"""

"""
print(re.findall("car", "car"))
print(re.findall("car", "scary"))
print(re.findall("car", "carry the barcardi to the car"))
"""

s = "This and that."
"""
print(re.findall(r"(th\w+) and (th\w+)", s, re.I))
print(re.finditer(r"(th\w+) and (th\w+)", s, re.I).next().groups())
print(re.finditer(r"(th\w+) and (th\w+)", s, re.I).next().group(1))
print(re.finditer(r"(th\w+) and (th\w+)", s, re.I).next().group(2))
print([g.groups() for g in re.finditer(r"(th\w+) and (th\w+)", s, re.I)])
"""
"""
print(re.findall(r"(th\w+)", s, re.I))
it = re.finditer(r"(th\w+)", s, re.I)
g = it.next()
print(g.groups())
print(g.group(1))
g = it.next()
print(g.groups())
print(g.group(1))
print([g.group(1) for g in re.finditer(r"(th\w+)", s, re.I)])
"""
"""
print(re.sub("X", "Mr. Smith", "attn: X\n\nDear X,\n"))
print(re.subn("X", "Mr. Smith", "attn: X\n\nDear X,\n"))
print(re.sub("X", "Mr. Smith", "attn: X\n\nDear X,\n"))
print(re.sub("[ae]", "X", "abcdef"))
print(re.subn("[ae]", "X", "abcdef"))
"""

"""
# 日期格式化
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "2/20/91"))
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "2/20/1991"))
"""

# print(re.split(":", "str1:str2:str3"))

"""
DATA = (
    "Mountain View, CA 94040",
    "Sunnyvale, CA",
    "Los Altos, 94023",
    "Cupertino 95014",
    "Palo Alto CA"
    )

for datumn in DATA:
    print(re.split(", |(?= (?:\d{5}|[A-Z]{2})) ", datumn))
"""

# print(re.findall(r"(?i)yes", "yes? Yes. YES!!"))
# print(re.findall(r"(?i)th\w+", "The quickest way is through this tunnel."))
# print(re.findall(r"(?im)(^th[\w ]+)", """
# This line is the first,
# another line,
# that line, it's the best
# """))
# print(re.findall(r"th.+", """
# The first line
# the second line
# the third line
# """))
# print(re.findall(r"(?s)th.+", """
# The first line
# the second line
# the third line
# """))

##print(re.search(r"""(?x)
##\((\d{3})\) # 区号
##[ ]         # 空白符
##(\d{3})     # 前缀
##-           # 横线
##(\d{4})     # 终点数字
##""", "(800) 555-1212").groups())

##print(re.findall(r"http://(?:\w+\.)*(\w+\.com)", "http://google.com http://www.google.com http://code.google.com"))
##print(re.sub(r"\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})", "(\g<areacode> \g<prefix>-xxxx)", "(800) 555-1212"))

##print(bool(re.match(r"\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)",
##              "(800) 555-1212 800-555-1212 18005551212")))

##print(bool(re.match(r"""(?x)
### match (800) 555-1212, save areacode,prefix,no
##\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
### space
##[ ]
### match 800-555-1212
##(?P=areacode)-(?P=prefix)-(?P=number)
### space
##[ ]
### match 18005551212
##1(?P=areacode)(?P=prefix)(?P=number)""",
##"(800) 555-1212 800-555-1212 18005551212")))

##print(re.findall(r"\w+(?= van Rossum)", """
##Guido van Rossum
##Tim Peters
##Alex Martelli
##Just van Rossum
##Raymond Hettinger
##"""));
##
##print(re.findall(r"(?m)^\s+(?!noreply|postmaster)(\w+)", """
##    sales@phptr.com
##    postmaster@phptr.com
##    eng@phptr.com
##    noreply@phptr.com
##    admin@phptr.com
##"""));
##
##print(["%s@aw.com" % e.group(1) for e in re.finditer(r"(?m)^\s+(?!noreply|postmaster)(\w+)", """
##    sales@phptr.com
##    postmaster@phptr.com
##    eng@phptr.com
##    noreply@phptr.com
##    admin@phptr.com
##""")]);
##
##print(bool(re.search(r"(?:(x)|(y))(?(1)y|x)", "yx")));
##print(bool(re.search(r"(?:(x)|(y))(?(1)y|x)", "xy")));

##m = re.match("\bblow", "blow");
##if m is not None:
##    print(m.groups());
##
##m = re.match("\\bblow", "blow");
##if m : print(m.group());
##
##m = re.match(r"\bblow", "blow");
##if m : print(m.group())
    
