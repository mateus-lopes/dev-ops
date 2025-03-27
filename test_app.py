from app import sumF

def test_sumF():
    assert sumF(1, 2) == 3
    assert sumF(1, 1) == 2
    assert sumF(1, 0) == 1
    assert sumF(0, 0) == 0