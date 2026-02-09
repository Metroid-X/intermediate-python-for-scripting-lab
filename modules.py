import random, string, datetime, math

def rand_pass(n):
    if(f'{n}'.isdigit()):
        L=int(n)
        if(L<=8):
            print("Input value was less than 8.\n")
            return ValueError
        else:
            chars = string.ascii_letters + string.digits
            rand = ''.join(random.choice(chars) for i in range(L))
            print(f'Password: {rand}\n')
            return rand
    else:
        print("Input value was invalid.\n")
        return ValueError

# rand_pass(input("Choose a length greater than 8: "))

def date_diff(d1,d2):

    d1a=f'{d1}'.split("-")
    d2a=f'{d2}'.split("-")

    mes='Invalid date input(s).\n'
    res=ValueError

    if((len(d1a)&len(d2a))==3):
        y_correct_len=(len(d1a[0])&len(d2a[0]))==4
        m_d_correct_len=(len(d1a[1])&len(d1a[2])&len(d2a[1])&len(d2a[2]))==2
        if(y_correct_len&m_d_correct_len):
            aredigits=f'{d1}{d2}'.replace("-","").isdigit()
            if(aredigits):
                mm=(int(d1a[1])&int(d2a[1]))
                mm_correct=mm > 0 & mm <= 12
                dd=(int(d1a[2])&int(d2a[2]))
                dd_correct=dd > 0 & dd <= 31
                if(mm_correct&dd_correct):
                    D1 = datetime.date.fromisoformat(d1)
                    D2 = datetime.date.fromisoformat(d2)
                    
                    Dates=[D1,D2]
                    Dates.sort()
                    
                    mes=f'Difference between {D1} and {D2}: {(Dates[1]-Dates[0]).days} Days\n'
                    res = (Dates[1]-Dates[0]).days
    print(mes)
    return res

# dates=input("Type two dates in YYYY-MM-DD format separated by commas: ").replace(" ","").split(",")

# date1 = ValueError if len(dates[0]) != 10 else dates[0]
# date2 = ValueError if len(dates) != 2 else dates[1]

# date_diff(date1,date2)

def circle_area(rad):
    if(f'{rad}'.isdigit() | f'{rad}'.isdecimal()):
        PI=math.pi
        Radius=int(rad)
        Area=PI*(Radius^2)
        print(f'The area of a circle with a radius of {Radius} units is {Area} square units.\n')
        return Area
    else:
        print('That is not a valid input.\n')
        return ValueError
# circle_area(input("Enter the radius of the circle to find the area of: "))
