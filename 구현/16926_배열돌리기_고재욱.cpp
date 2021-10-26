#include <iostream>
using namespace std;
int map[301][301];
int main() {
	int n, m, r;
	cin >> n >> m >> r;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}
	while (r--) {
		int x1 = 0, x2 = m - 1;
		int y1 = 0, y2 = n - 1;

		while (x1 < x2 && y1 < y2) {
			int tmp = map[y2][x1];

			for (int i = y2; i > y1; i--) {
				map[i][x1] = map[i - 1][x1];
			}

			for (int i = x1; i < x2; i++) {		// À­ÁÙ
				map[y1][i] = map[y1][i + 1];
			}

			for (int i = y1; i < y2; i++) {		// ¿À¸¥ÂÊ
				map[i][x2] = map[i + 1][x2];
			}

			for (int i = x2; i > x1+1; i--) {
				map[y2][i] = map[y2][i - 1];
			}

			map[y2][x1+1] = tmp;
			
			x1++;
			y1++;
			x2--;
			y2--;
		}
		
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << map[i][j] << " ";
		}
		cout << "\n";
	}

}