#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>


using namespace std;

const int GRID_SIZE = 4;

vector<vector<int>> gameGrid(GRID_SIZE, vector<int>(GRID_SIZE, 0));

char getUserInput() {
    char input;
    cout << "Please use w, a, s, d to play the game: ";
    cin >> input;
    if (input == 'w' || input == 'a' || input == 's' || input == 'd') {
        return input;
    } else {
        cout << "Input is not valid" << endl;
        return getUserInput();
    }
}

void printGame() {
    for (const auto& row : gameGrid) {
        for (int element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

void randomSpawn() {
    srand(time(0));
    while (true) {
        int x = rand() % 4;
        int y = rand() % 4;
        if (gameGrid[x][y] == 0) {
            gameGrid[x][y] = 2;
            break;
        }
    }
}

void moveUp() {
    for (int col = 0; col < gameGrid[0].size(); ++col) {
        for (int row = 1; row < gameGrid.size(); ++row) {
            if (gameGrid[row][col] != 0) {
                int newRow = row;
                while (newRow > 0 && gameGrid[newRow - 1][col] == 0) {
                    gameGrid[newRow - 1][col] = gameGrid[newRow][col];
                    gameGrid[newRow][col] = 0;
                    --newRow;
                }
                if (newRow > 0 && gameGrid[newRow][col] == gameGrid[newRow - 1][col]) {
                    gameGrid[newRow - 1][col] *= 2;
                    gameGrid[newRow][col] = 0;
                }
            }
        }
    }
}

void moveDown() {
    for (int col = 0; col < gameGrid[0].size(); ++col) {
        for (int row = gameGrid.size() - 2; row >= 0; --row) {
            if (gameGrid[row][col] != 0) {
                int newRow = row;
                while (newRow < gameGrid.size() - 1 && gameGrid[newRow + 1][col] == 0) {
                    gameGrid[newRow + 1][col] = gameGrid[newRow][col];
                    gameGrid[newRow][col] = 0;
                    ++newRow;
                }
                if (newRow < gameGrid.size() - 1 && gameGrid[newRow][col] == gameGrid[newRow + 1][col]) {
                    gameGrid[newRow + 1][col] *= 2;
                    gameGrid[newRow][col] = 0;
                }
            }
        }
    }
}

