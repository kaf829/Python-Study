a = 10
b= 123.456
c = "MBC"
d  = True
print("%d %-10.2f %s %s" %(a,b,c,d))


#이거 차이를 알아야함
output_c  = "#{:^10d}#".format(52)
output_b  = "#{:<10d}#".format(52)
output_a  = "#{:>10d}#".format(52)

print(output_c)