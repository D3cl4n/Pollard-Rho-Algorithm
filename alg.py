def next_val(x, s, t):
    c = (x+1) % 3
    if c == 0:
        return

def pollard_rho(p, g, a, n):
    xa, sa, ta = 1, 0, 0
    xb, sb, tb = next_val(1, 0, 0)

def main():
    #solve a^x = b mod p
    #x = log_a(b)
    p = 2199023255867
    a = 3
    b = 1228035139812
    n = (p-1)/2
    res = pollard_rho(p, a, b, n)
    print(f"Computed result: {res}")

if __name__ == '__main__':
    main()