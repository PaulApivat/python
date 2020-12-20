sh = input("Enter hours: ")
sr = input("Enter rate: ")


def compute(hours: str, rate: str) -> str:
    print("computing...")
    try:
        fh = float(hours)
        fr = float(rate)
    except:
        print("Error, please enter numeric input.")
        quit()

    print(fh, fr)
    if fh > 40:
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        xp = fh * fr
    print(f"Function Pay: {xp}")


compute(sh, sr)
