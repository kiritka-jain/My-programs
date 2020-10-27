def calculate_fine(ret_d_1,ret_m_1,ret_y_1,due_d_2,due_m_2,due_y_2):
    if ret_y_1 <= due_y_2 and ret_m_1 <=due_m_2 and ret_d_1 <= due_d_2:
        return 0
    elif ret_y_1 > due_y_2:
        return 10000
    elif ret_m_1 > due_m_2 and ret_y_1 == due_y_2:
        return (500 *(ret_m_1-due_m_2))
    elif ret_d_1 > due_d_2 and ret_m_1 == due_m_2 and ret_y_1 == due_y_2:
        return (15 *(ret_d_1-due_d_2))
    else:
        return 0



ret_d_1,ret_m_1,ret_y_1 = list(map(int,input().split()))
due_d_2,due_m_2,due_y_2 = list(map(int,input().split()))

print(calculate_fine(ret_d_1,ret_m_1,ret_y_1,due_d_2,due_m_2,due_y_2))

