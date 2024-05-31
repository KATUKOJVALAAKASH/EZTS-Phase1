the_day=int(input('enter the day'))
if 0<=the_day<85:
    no_of_calls = int(input('enter the no of calls you have today'))
    no_of_messages = int(input('enter the no of messages you have today'))
    data_used = float(input('enter the data you used today'))
    print(f'your plan will be expired in {84 - the_day}')

    if no_of_calls<0:
        print('please enter valid data')
    elif  no_of_calls>3000:
        print('calls could not be connected kindly top up')
    else:
        print(f'yet to call {3000-no_of_calls}')

    if no_of_messages<0:
        print('please enter valid data')
    elif no_of_messages>100:
        print('msg failed')
    else:
        print(f'yet to msg{100-no_of_messages}')

    if data_used<0:
        print('please enter valid data')
    elif data_used>2.0:
        print('your speed reduced')
    else:
        print(f'yet to have{2.0-data_used}')

elif the_day<0:
    print('please enter valid data')
else:
    print('kindly recharge your plan expired')