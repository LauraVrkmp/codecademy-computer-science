from board import Board

def main():
    size = '800x800'
    # print('What is your prefered size?')
    # size = input()

    Board(size).draw()

if __name__ == '__main__':
    main()