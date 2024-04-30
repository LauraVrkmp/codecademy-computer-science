from board import Board

def main():
    size = '800x800'
    # print('What are your prefered dimensions? (tile by tile)')
    # dimensions = input()
    dimensions = [20, 20]

    Board(size, dimensions).draw()

if __name__ == '__main__':
    main()