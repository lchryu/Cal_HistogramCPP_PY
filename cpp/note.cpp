for (int i = 1; i <= row; i++) {
    for (int j = 1; j <= col; j++) {
        solve(i, j);
        cout << endl;
    }
}