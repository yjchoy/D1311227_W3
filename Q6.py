print('請輸入二次方程式的三個係數')
a=int(input('輸入係數a:'))
b=int(input('輸入係數b:'))
c=int(input('輸入係數c:'))
ans1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
ans2=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
print('方程式的根為：x1=',ans1,'x2=',ans2)