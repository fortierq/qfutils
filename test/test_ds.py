from qfutils.ds import union_json

def test_union_json():
    d1 = {'a': 1, 'b': {0: 1}, 3: [0, 1]}
    d2 = {'a': 2, 'b': {0: 2, 2: 2}, 3: ["2", "1"], 4: 4}
    assert union_json(d1, d2) == {'a': 1, 'b': {0: 1, 2: 2}, 3: [0, 1, "2", "1"], 4: 4}
