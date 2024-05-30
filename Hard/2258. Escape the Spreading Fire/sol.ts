// Link: https://leetcode.com/problems/escape-the-spreading-fire/description/

function maximumMinutes(grid: number[][]): number {
    let found = false;
    const dir = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    class Mypair {
        x: number;
        y: number;
        time: number;
        constructor(x: number, y: number, time: number) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

    function canReachEnd(grid: number[][], time: number[][], initialWaitTime: number, n: number, m: number): boolean {
        const qe: Mypair[] = [];
        const vis: boolean[][] = Array.from({ length: n }, () => Array(m).fill(false));

        qe.push(new Mypair(0, 0, initialWaitTime));
        vis[0][0] = true;

        while (qe.length > 0) {
            const tt = qe.shift()!;
            if (tt.x === n - 1 && tt.y === m - 1) {
                found = true;
                return true;
            }

            for (let a = 0; a < 4; a++) {
                const newX = tt.x + dir[a][0];
                const newY = tt.y + dir[a][1];
                if (
                    newY < m &&
                    newY >= 0 &&
                    newX < n &&
                    newX >= 0 &&
                    grid[newX][newY] === 0 &&
                    !vis[newX][newY]
                ) {
                    if (
                        tt.time + 1 < time[newX][newY] ||
                        time[newX][newY] === 0 ||
                        (tt.time + 1 <= time[newX][newY] && newX === n - 1 && newY === m - 1)
                    ) {
                        vis[newX][newY] = true;
                        qe.push(new Mypair(newX, newY, tt.time + 1));
                    }
                }
            }
        }

        return false;
    }

    function calMinTimeToBurn(grid: number[][], time: number[][], n: number, m: number): void {
        const qe: Mypair[] = [];
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (grid[i][j] === 1) {
                    qe.push(new Mypair(i, j, 0));
                }
            }
        }

        while (qe.length > 0) {
            const tt = qe.shift()!;
            for (let a = 0; a < 4; a++) {
                const newX = tt.x + dir[a][0];
                const newY = tt.y + dir[a][1];
                if (
                    newY < m &&
                    newY >= 0 &&
                    newX < n &&
                    newX >= 0 &&
                    grid[newX][newY] === 0
                ) {
                    if (time[newX][newY] === 0 || time[newX][newY] > 1 + time[tt.x][tt.y]) {
                        qe.push(new Mypair(newX, newY, 0));
                        time[newX][newY] = time[tt.x][tt.y] + 1;
                    }
                }
            }
        }
    }

    const n = grid.length;
    const m = grid[0].length;
    let ans = -1;
    const time: number[][] = Array.from({ length: n }, () => Array(m).fill(0));

    calMinTimeToBurn(grid, time, n, m);

    let l = 0, hi = time[0][0];

    while (l <= hi) {
        const mid = l + Math.floor((hi - l) / 2);
        if (canReachEnd(grid, time, mid, n, m)) {
            ans = mid;
            l = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    if (time[0][0] === 0 && found) {
        return 1000000000;
    }

    return !found ? -1 : ans;
}
