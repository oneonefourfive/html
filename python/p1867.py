n = int(input())
lvl = 0
hp = 10
jingyan = 0
need_for_up = 0
for i in range(n):
    made = list(map(float, input().split(" ")))
    hp -= made[0]
    if hp >= 10:
        hp=10

    if hp>0:
        jingyan += made[1]

    if hp<=0:
        break

while True:
    print(jingyan)
    if jingyan >= 0:
        need_for_up=jingyan
        jingyan -= 2**lvl
        lvl += 1

        
    if jingyan < 0:
        jingyan =need_for_up
        lvl -= 1

        break
print("{0} {1}".format(lvl, int(jingyan)))
