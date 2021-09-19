def main():
    #write your code below this line
    sum = 0
    count = 0
    
    while True:
        num = int(input('Give a number:'))
        
        if num == 0:
            break
            
        count += 1
        sum += num
        
    print('Average of numbers: ' + str(sum/count))

    

if __name__ == '__main__':
    main()
