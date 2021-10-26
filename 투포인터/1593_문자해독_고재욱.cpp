#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;
int main() {
	int g, s;
	cin >> g >> s;
	string aws, word;
	cin >> aws >> word;
	unordered_map<int, int> m, tmp;
	for (int i = 0; i <= 'z' - 'A'; i++) {
		m[i] = tmp[i] = 0;
	}

	for (int i = 0; i < g; i++) {
		m[aws[i] -'A']++;
	}

	int cnt = 0;
	int left = 0;

	for (int i = 0; i < s; i++) {
		tmp[word[i] -'A']++;
		if (i - left == g-1) {
			if (tmp == m) cnt++;
			tmp[word[left++] -'A']--;
		}
	}
	cout << cnt;

}