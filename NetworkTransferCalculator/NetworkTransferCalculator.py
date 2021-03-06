#This program takes user input to provide calculations for over-network transfers

def CalculateNT():
    print('Enter File Size')
    file_size = Input()
    print('Enter Time Alloted')
    time = Input()

    true_file_size = FindSize(file_size)
    true_time = FindTime(time)

    network_transfer_speed = true_file_size / true_time

    # if network_transfer_speed/1000:
    #     # follow up on

    print('The minimum network transfer assuming no overhead or packet loss',
     'would be ' + network_transfer_speed + 'Mbps')

def CalculateTT():
    print('Enter File Size')
    file_size = Input()
    print('Enter Network Speed')
    network_transfer_speed = Input()

    true_file_size = FindSize(file_size)
    true_network_transfer_speed = FindTime(network_transfer_speed)
    time_for_transfer = true_file_size / true_network_transfer_speed
    #if time_for_transfer:
        # follow up on
    print('The time to transfer this size file assuming no overhead or packet',
     'loss would be' + time_for_transfer + 'seconds')


def CalculateMT():
    print('Enter Time Alloted')
    time = Input()
    print('Enter Network Speed')
    network_transfer_speed = Input()
    true_file_size = FindSize(file_size)
    true_time = FindTime(time)
    max_file_transfer = true_time * true_network_transfer_speed
    #if max_file_transfer/1000:
        # follow up on
    print('The maximum size file that can be trasfered assuming no overhead',
    'or packet loss would be ' + max_file_transfer + 'GB')




def FindTime(inputed_time):
    return true_time

def FindSize(inputed_file_size):
    return true_file_size

def FindSpeed(inputed_network_transfer_speed):
    return true_network_transfer_speed

def GetUserInput():
    print('What Are You Lookig to Calculate?')
    print('1) File Size / Time = Network Transfer Speed Needed')
    print('2) File Size / Network Transfer Speed = Time Needed for Transfer')
    print('3) Network Transfer Speed / Time = Max Transfer Amount')
    print('4) Exits Program')
    return input()

def main():
    user_input = GetUserInput()
    if user_input == 1:
        CalculateNT()
        main()
    elif user_input == 2:
        CalculateTT()
        main()
    elif user_input == 3:
        CalculateMT()
        main()
    elif user_input == 4:
        quit()
    else:
      print('Value selected is not recognized')
      main()


if __name__ == '__main__':
  main()
