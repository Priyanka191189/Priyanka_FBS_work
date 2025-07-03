# cost of printing of waals both int and ext, accept area and cost both int and ext of waal

side = int(input("Enter side of waal: "))
cost_int = int(input("Enter cost if interior painting: "))
cost_ext = int(input("Enter cost of exterior painting: "))

total_area = 4* side* side

total_cost = total_area * cost_int + total_area * cost_ext

print("Total cost of painting 2 rooms Rs. : ", 2* total_cost)
