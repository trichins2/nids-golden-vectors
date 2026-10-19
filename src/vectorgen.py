import struct

INT32_MIN, INT32_MAX = -2**31, 2**31 - 1

def bytes_to_samples(data: bytes, n: int = 128) -> list[int]:
    """Pack raw packet bytes into n signed 32-bit little-endian samples (zero-padded/truncated)."""
    buf = data[: n * 4].ljust(n * 4, b"\x00")
    return list(struct.unpack(f"<{n}i", buf))

def scale2_reference(samples: list[int]) -> list[int]:
    """Golden model of the AIE scale2 kernel: out = in * 2, with int32 wraparound."""
    return [((s * 2 - INT32_MIN) % 2**32) + INT32_MIN for s in samples]