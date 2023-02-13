# Pay Period Generator

"""
Bi-weekly (14 days)
    Start: Sunday
    End: Saturday
    Pay is next Friday (After the end date)
"""

def pay_period(period_start_date, iterations, year): 

    months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    month = {
        1: "Jan.", 2: "Feb.", 3: "Mar.", 4: "Apr.", 5: "May.", 6: "Jun.",
        7: "Jul.", 8: "Aug.", 9: "Sep.", 10: "Oct.", 11: "Nov.", 12: "Dec." 
    }

    m, d = period_start_date.replace(" ", "").split("/")
    m, d = int(m), int(d)

    period = 13 # days
    pay = 6 # pay is 6 days after the end date

    periods = []

    for _ in range(iterations): 
        start = f"{month[m]}{d}, {year}" # pay period start
        d += period

        if d > months[m]:
            d -= months[m]
            m += 1
            if m > 12: 
                m = 1
                year += 1

        end = f"{month[m]}{d}, {year}" # pay period end

        # Pay date
        pd = d + 6
        pm = m
        if pd > months[pm]:
            pd -= months[pm]
            pm += 1
            if pm > 12: 
                pm = 1
                year += 1

        pay = f"{month[pm]}{pd}, {year}"

        periods.append(f"Start: {start}\t\tEnd: {end}\t\tPay: {pay}\n\n")

        d += 1 # increment the day

    return periods

"""
Function takes 3 input parameters:
    - Pay period start date ex. 1/22
    - The amount of pay periods that you would like
    - year
"""


p = pay_period("1 / 22", 25, 2023) # 25 at a time works amazing for regualar paper


f = open("pay.txt", "w") # writes to a printable file
for line in p:
    f.write(line)
f.close()