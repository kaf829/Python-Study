def test(a, *b, **c):
    print(a + b + c)


test("10", "20", "30", x="mbc", y="kbs", z="sbs")
