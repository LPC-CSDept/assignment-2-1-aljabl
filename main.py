def main():
   #asks the user for the number of males and females registered in a class
    males = int(input('How many students are male? '))
    females = int(input('How many students are female? '))

    #give total number of students
    total_students = males + females
    
    #assign the percentage of males and females to variables
    m_perc = 100 * males / total_students
    f_perc = 100 * females / total_students  

    #print the total number of students, the number of males and females, and the percentages of males and females
    print('The total number of students: ', total_students)
    print('The number of males and females: ', males, '\t', females)
    print(f'The percentage of males and females: {m_perc:.2f}% \t {f_perc:.2f}%')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

