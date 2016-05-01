def create_tri_num(num):
    triangle_num = int((num*(num+1))/2)
    return triangle_num




largest_divisor = {'count': 0, 'tri_num': 0, 'count_num': 0}
start_value = 1
while largest_divisor['count'] <= 500:
    triangle_value = create_tri_num(start_value)
    divisor_count = 0
    for num in range(1, int((triangle_value/2)+1)):
        if triangle_value%num == 0:
            divisor_count += 1
    if divisor_count > largest_divisor['count']:
        largest_divisor['count'], largest_divisor['tri_num'], largest_divisor['count_num'] = divisor_count, triangle_value, start_value
        print(largest_divisor)
    start_value += 1
print(largest_divisor)