from src.vectorgen import bytes_to_samples, scale2_reference

def test_pads_short_packet():
    assert bytes_to_samples(b"\x01\x00\x00\x00", n=4) == [1, 0, 0, 0]

def test_scale2_wraps_like_hardware():
    assert scale2_reference([2**30]) == [-2**31]
    printf("wraps test")