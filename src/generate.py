import argparse, random, pathlib
from src.vectorgen import bytes_to_samples, scale2_reference

def main():
    p = argparse.ArgumentParser(description="Generate AIE input + golden output vectors")
    p.add_argument("--n", type=int, default=128)
    p.add_argument("--seed", type=int, default=423)
    p.add_argument("--out", default="out")
    a = p.parse_args()

    rng = random.Random(a.seed)  # fixed seed = same vectors every run
    pkt = bytes(rng.randrange(256) for _ in range(a.n * 4))
    x = bytes_to_samples(pkt, a.n)
    y = scale2_reference(x)

    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "input.txt").write_text("\n".join(map(str, x)) + "\n")
    (out / "golden.txt").write_text("\n".join(map(str, y)) + "\n")
    print(f"wrote {a.n} samples to {out}/")

if __name__ == "__main__":
    main()