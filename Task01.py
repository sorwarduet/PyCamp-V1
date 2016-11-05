def stringPermutations(s):
    if len(s) < 2:
        yield s
        return
    for pos in range(0, len(s)):
        char = s[pos]
        permForRemaining = list(stringPermutations(s[0:pos] + s[pos+1:]))
        for perm in permForRemaining:
            yield char + perm


string=input("Enter the String:")
result=stringPermutations(string)
for i in result:
    print(i)