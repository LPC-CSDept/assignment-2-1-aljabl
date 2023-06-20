def main():
   #asks the user for the number of males and females registered in a class
    m_perc = int(input('How many students are male? '))
    f_perc = int(input('How many students are female? '))

    #give total number of students
    print('The total number of students: ', m_perc + f_perc)

    #give the number of males and females
    print('The number of males and females: ', m_perc, "\t",  f_perc)

    #give the percentage of males and females
    print(f'The percentage of males and females: {m_perc:.2f}% \t {f_perc:.2f}%')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

