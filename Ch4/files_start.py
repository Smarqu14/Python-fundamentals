import random
#
# Read and write files using the built-in Python file methods
#


def main():

    #     # Open a file for writing and create it if it doesn't exist
    #     f = open('textfile.txt', 'w+')

    # # Open the file for appending text to the end

    # # write some lines of data to the file
    #     for i in range(10):
    #         f.write('This is lineog ' + str(i) + '\r\n')
    # # close the file when done
    #     f.close()
    # Open the file back up and read the contents

    def files():

        def writeName(firstName='OG', lastName='Papi'):
            testing = open('myfile.txt', 'w+')

            names = [firstName, lastName]
            randomNickname = ['Poopoloco', 'Finchaao',
                              'Lodcd', 'Opencx', 'Estrox', 'Sipsys', 'Dlpaas']
            hasNickname = False
            nickname = ''
            lenght = len(randomNickname)

            for i in range(lenght):
                nickname = randomNickname[3]
                testing.write('You have been called ' +
                              str(nickname) + '\n\n')
                if randomNickname[i] == 'Dlpaas':
                    random.shuffle(randomNickname)
                    nickname = random.choice(randomNickname)
                    hasNickname = True
                    testing.write('You have been called ' +
                                  str(nickname) + '\n\n')
                else:
                    'The trip has been dope'

            first = ''
            second = ''

            if hasNickname == True:
                for index, name in enumerate(names):

                    first = 'you are the shit ' + names[0]
                    second = 'My g ' + names[1]
                    testing.write(str(first) + '\n\n' + str(second))

            testing.close()

        class Car:
            def __init__(self, model='regular', year=0, color='transparent'):
                self.model = model
                self.year = year
                self.color = color

            def carYear(self, ownerName, age):
                testing = open('myfile.txt', 'a+')

                owner = ownerName
                legalAge = age

                if age > 18:
                    print(f'The year of your car is {self.year}j')
                    testing.write(str(f'The year of your car is {self.year}j'))
                    testing.close()
                else:
                    print(f'{ownerName} you are not alowed to drive')
                    testing.write(
                        str(f'{ownerName} you are not alowed to drive'))
                    testing.close()

            def carModel(self, carCondition):
                carModelPrices = {
                    'honda': 1000,
                    'ferrari': 2000,
                    'mazda': 3000
                }

                print('Hello world') if carCondition else print(
                    'Not so hello world')

                if carCondition:
                    for x in carModelPrices.keys():
                        if not carModelPrices['Toyota']:
                            carModelPrices['Toyota'] = 500
                        else:
                            print(
                                'We added it on the carModelPrices my g and we looping')

                else:
                    if carCondition.lower() == 'new':
                        print(
                            f'Your car is {carCondition} and it is from the year {self.year}')

                    else:
                        print(f'Very pretty {self.color}')

                def printCarPrices():
                    for key, value in carModelPrices:
                        title = 'Prices'
                        print(title)
                        print(key, '-----', value)

                printCarPrices()

        def appendingToFile():
            testing = open('myfile.txt', 'a+')

            myMazda = Car('Mazda', 2016, 'Black')
            myHonda = Car('Honda', 2019, 'Green')

            myMazda.carYear('Steve', 25)
            myHonda.carYear('Antonio', 16)
            testing.write('\n adding this og ')
            print('You have appended things')

        def readFiles():
            testing = open('myfile.txt', 'r')

            if testing.mode == 'r':
                content = testing.read()
                print(content)

        def chooseAction(action):
            if action == 'read':
                readFiles()
            elif action == 'write':
                writeName('Steve', 'Antonio')
            else:
                appendingToFile()
                print('Need to create/lol')

        chooseAction('write')
        chooseAction('read')
        chooseAction('append')

    files()


if __name__ == "__main__":
    main()
