from nlgeval import NLGEval

def test_oo_api():
    with open("examples/hyp.txt") as f:
        hyp = f.readlines()
        hyp = [x.strip() for x in hyp]
    with open("examples/ref1.txt") as f:
        ref1 = f.readlines()
        ref1 = [x.strip() for x in ref1]
    with open("examples/ref2.txt") as f:
        ref2 = f.readlines()
        ref2 = [x.strip() for x in ref2]

    nlge = NLGEval()

    res = nlge.compute_individual_metrics([ref1[0]] + [ref2[0]], hyp[0])
    print(res)
    res = nlge.compute_individual_metrics([ref1[1]] + [ref2[1]], hyp[1])
    print(res)

    hyp_list = hyp # 字符串列表不包含空格
    ref_list = [ref1, ref2]
    res = nlge.compute_metrics(ref_list, hyp_list)
    print(res)


if __name__ == '__main__':
    test_oo_api()
