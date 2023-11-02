import re

cc_list = '''Ezra Koenig <ekoenig@ubuntu.org>,
...: Rostam Batmanglij <rostam@vpwk.com>,
...: Chris Tomson <ctomson@vpwk.com,
...: Bobbi Baio <bbaio@vpwk.com'''

ee_list = """john.doe@gmail.com,
sarah.smith@yahoo.com,
michael.jones@outlook.com,
emily.wilson@aol.com,
david.brown@protonmail.com,
lisa.jackson@icloud.com,
robert.davis@hotmail.com,
mary.white@live.com,
james.thompson@yandex.ru,
jennifer.harris@mail.com,
william.anderson@mydomain.com,
laura.martin@yourcompany.org,
matthew.robinson@techblog.net,
emma.miller@startup.biz """


# Searching
find = "Rostam" in cc_list # type: ignore
print(find)

# using re.search
find = re.search(r"Rostam", cc_list)
print(find)

# using an if statement with re.search
if find:
    print("Found Rostam")


# Character Sets
find = re.search(r"[R,B]obb[i,y]", cc_list)
print(find)

# also -->
find = re.search(r"Chr[a-z][a-z]", cc_list)
print(find)

find = re.search(r"[A-Za-z]+", cc_list)
print(find)

find = re.search(r"[A-Za-z]{6}", cc_list)
print(find)

find = re.search(r"[A-Za-z]+@[a-z]+\.[a-z]+", cc_list)
print(find)


# Character Classes
find = re.search(r"\w+", cc_list)
print(find)

find = re.search(r"\w+\@\w+\.\w+", cc_list)
print(find)


# Groups
matched = re.search(r"(\w+)\@(\w+)\.(\w+)", cc_list)
m1 = matched.group(0)
m2 = matched.group(1)
m3 = matched.group(2)
m4 = matched.group(3)

print(f"m1 : {m1}, m2: {m2}, m3: {m3}, m4: {m4}")

# Named Groups
matched = re.search(r"(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
matched.group("name")
print(f"""name: {matched.group("name")}
      Secondary Level Domain: {matched.group("SLD")}
      Top Level Domain: {matched.group("TLD")}""")

# Find All
matched = re.findall(r"\w+\@\w+\.\w+", ee_list)
print(matched)

matched = re.findall(r"(\w+)\@(\w+)\.(\w+)", cc_list)
print(matched)

names = [x[0] for x in matched]
print(names)

print("..........")

# Find Iterator
matched = re.finditer(r"\w+\@\w+\.\w+", ee_list)
print(matched)
n1 = next(matched)
n2 = next(matched)
n3 = next(matched)
print(f"n1: {n1}\n, n2: {n2}\n, n3: {n3}\n")

print("........")
# using the iterator object, "matched", in a for loop
matched = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", ee_list)
for m in matched:
    print(m.groupdict())

print(".........")

# Substitution
re.sub("\d", "#", "The passcode you entered was 0849343")
users = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",
               "\g<TLD>.\g<SLD>.\g<name>", ee_list)
print(users)

print("........")

# Compiling
regex = re.compile(r"\w+\@\w+\.w+")
result = regex.search(cc_list)
print(result)