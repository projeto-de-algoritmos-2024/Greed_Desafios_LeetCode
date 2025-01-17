#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        // 1. Ordenar cursos por lastDay
        sort(courses.begin(), courses.end(), 
            [](const vector<int>& a, const vector<int>& b){
                return a[1] < b[1];
            }
        );

        // 2. Max-heap para guardar as durações dos cursos selecionados
        priority_queue<int> maxHeap;
        int total_time = 0;

        for (auto &course : courses) {
            int duration = course[0];
            int lastDay  = course[1];

            // Tentar adicionar este curso
            maxHeap.push(duration);
            total_time += duration;

            // Se ultrapassou o prazo, remove o maior curso da heap
            if (total_time > lastDay) {
                int longest = maxHeap.top();
                maxHeap.pop();
                total_time -= longest;
            }
        }

        // Tamanho da heap é o número de cursos que couberam
        return (int)maxHeap.size();
    }
};

int main(){
    // Exemplo do enunciado
    vector<vector<int>> courses = {
        {100, 200},
        {200, 1300},
        {1000, 1250},
        {2000, 3200}
    };

    Solution sol;
    cout << sol.scheduleCourse(courses) << endl;

    return 0;
}
