/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => a - b);

    let total = 0;
    let currentSum = 0;

    for (let i = satisfaction.length - 1; i >= 0; i--) {
        if (currentSum + satisfaction[i] > 0) {
            currentSum += satisfaction[i];
            total += currentSum;
        } else {
            break;
        }
    }

    return total;
};
