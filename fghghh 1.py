
# def strcounter(s):
#     print(set(s))
#     for sym in set(s):
#         count = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 count += 1
#         print(sym, "-", count)
#
# strcounter("ssa")

def strcounter(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym,0) + 1

    for sym, count in sym_counter.items():
        print(sym, count)

strcounter("bjnsfbnmrgsbjnsghjb")