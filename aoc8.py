import sys

ls = [[x.split() for x in l.split(' | ')] for l in iter(input,'')]

ps = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".split()

print(sum(sum(len(d) in (2,4,3,7) for d in v) for (_,v) in ls))
