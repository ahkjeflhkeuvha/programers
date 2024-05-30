function solution(park, routes) {
    var startIdx = [0, 0];

    // 시작 위치 찾기
    for (var i = 0; i < park.length; i++) {
        for (var j = 0; j < park[i].length; j++) {
            if (park[i][j] === "S") {
                startIdx = [i, j];
                break;
            }
        }
    }

    // 경로 따라 이동하기
    for (var i = 0; i < routes.length; i++) {
        var route = routes[i].split(" ");
        var direction = route[0];
        var steps = Number(route[1]);
        var cnt = 0;
        var originalIdx = [...startIdx];

        if (direction === "E") {
            while (cnt < steps && startIdx[1] + 1 < park[0].length && park[startIdx[0]][startIdx[1] + 1] !== "X") {
                startIdx[1]++;
                cnt++;
            }
        } else if (direction === "W") {
            while (cnt < steps && startIdx[1] - 1 >= 0 && park[startIdx[0]][startIdx[1] - 1] !== "X") {
                startIdx[1]--;
                cnt++;
            }
        } else if (direction === "S") {
            while (cnt < steps && startIdx[0] + 1 < park.length && park[startIdx[0] + 1][startIdx[1]] !== "X") {
                startIdx[0]++;
                cnt++;
            }
        } else if (direction === "N") {
            while (cnt < steps && startIdx[0] - 1 >= 0 && park[startIdx[0] - 1][startIdx[1]] !== "X") {
                startIdx[0]--;
                cnt++;
            }
        }

        // 만약 이동 중 장애물(X)을 만나거나 경로가 끝까지 가지 못했을 경우 원래 위치로 되돌리기
        if (cnt < steps) {
            startIdx = originalIdx;
        }
    }

    return startIdx;
}